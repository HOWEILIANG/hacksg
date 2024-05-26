import decimal
import math
from datetime import datetime, timedelta

import pandas as pd
import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Max, Q
from django.shortcuts import redirect, render

from dbschallenge.forms import UserProfileForm
from dbschallenge.models import (
    Company,
    Dividend,
    Inflation,
    PriceData,
    Reit,
    TreasuryYield,
    UserProfile,
)
from dbschallenge.portfolio_mix import recommend_portfolio_mix
from dbschallenge.retirement import (
    amount_needed_for_retirement,
    retirement_plan,
)
from dbschallenge.talkstack import TalkStack

from .forms import LoginForm, SignUpForm

companies = ("msft", "appl", "nvda", "goog", "amzn", "meta", "brk-b", "lly", "v", "wmt", "XOM", "MA", "PG", "SBUX", "MDLZ", "BA", "DELL")
# Create your views here.

def user_input_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save()
                # if user_profile.mobile:
                # response = TalkStack(user_profile.mobile).post()
            return redirect('result', pk=user_profile.pk)
    else:
        form = UserProfileForm()
    return render(request, 'input_form.html', {'form': form})

def format_us_currency(x):
    return '${:,.2f}'.format(x)


def call(request):
    if request.method == "POST":
        user_profile = UserProfile.objects.get(pk=request.POST['pk'])
        TalkStack(user_profile.mobile).post()
    return redirect('result', pk=user_profile.pk)


def result(request, pk):
    user_profile = UserProfile.objects.get(pk=pk)
    comfortable_amount = int(user_profile.comfortable_amount)
    current_age = int(user_profile.age)
    retirement_age = 63 #Singapore Retirement Age
    end_age = 83 #Singapore Life Expectancy
    inflation_rate = 0.04  # 3% annual inflation
    expected_return = float(user_profile.expected_returns)
    risk_appetite = user_profile.risk_appetite

    type(user_profile.expected_returns)
    if current_age < 63:
        annual_investment_required = retirement_plan(comfortable_amount, current_age, retirement_age, end_age, inflation_rate, expected_return)
        print(f"Annual investment required: ${annual_investment_required:,.2f}")

        total_needed = amount_needed_for_retirement(comfortable_amount, current_age, retirement_age, end_age, inflation_rate)
        print(f"Total amount needed for retirement: ${total_needed:,.2f}")
    else:
        annual_investment_required = 0
        total_needed = 0
    allocation = recommend_portfolio_mix(user_profile)
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=365)

    price_data_previous_year = PriceData.objects.filter(date__range=[start_date, end_date]).prefetch_related('company')

    price_data_previous_year = PriceData.objects.filter(date__range=[start_date, end_date]).values(
        'company__ticker', 'date', 'open', 'high', 'low', 'close', 'adj_close', 'volume'
    )
    df = pd.DataFrame(list(price_data_previous_year))
    df_sorted = df.sort_values(by=['company__ticker', 'date'])
    grouped_df = df_sorted.groupby('company__ticker').agg({'open': 'first', 'close': 'last'})
    grouped_df['one_year_return'] = round(((grouped_df['close'] - grouped_df['open']) / grouped_df['open']) * 100, 2)

    grouped_df.drop(columns=['open'], inplace=True)
    dividends = Dividend.objects.all().values('company__ticker', 'dividend_yield')
    df_dividends = pd.DataFrame(list(dividends))
    reits_dividend = Reit.objects.all().values("distribution_yield", "dpu",  "name", "nav", "price")
    treasury_yield = TreasuryYield.objects.all().values('name', 'coupon', 'price', 'yield_percent')
    merged_df = pd.merge(grouped_df, df_dividends, on='company__ticker', how='left')
    desired_dividends = [120000, 240000, 360000]
    for desired_dividend in desired_dividends:
        merged_df['close'] = merged_df['close'].round(0).astype(int)
        merged_df[f'stocks_needed_{desired_dividend}'] = desired_dividend / merged_df['dividend_yield']
        merged_df[f'stocks_needed_{desired_dividend}'] = merged_df[f'stocks_needed_{desired_dividend}'].fillna(0)
        merged_df[f'stocks_needed_{desired_dividend}'] = merged_df[f'stocks_needed_{desired_dividend}'].round(0).astype(int)
        merged_df[f'amount_needed_{desired_dividend}'] = merged_df['close'] * merged_df[f'stocks_needed_{desired_dividend}']
        merged_df[f'amount_needed_{desired_dividend}'] = merged_df[f'amount_needed_{desired_dividend}'].apply(format_us_currency)

    merged_df.dropna(subset=['dividend_yield'], inplace=True)
    new_column_names = {
        'company__ticker': 'Company Ticker',
        'close': 'Close',
        'one_year_return': 'One Year Return',
        'dividend_yield': 'Dividend Yield',
        'amount_needed_120000': 'Passive Income of $10,000(monthly)',
        'amount_needed_240000': 'Passive Income of $20,000(monthly)',
        'amount_needed_360000': 'Passive Income of $30,000(monthly)'
    }

    # Rename columns in merged_df
    merged_df.rename(columns=new_column_names, inplace=True)

    # Drop columns containing 'stocks_needed'
    columns_to_drop = [col for col in merged_df.columns if 'stocks_needed' in col]
    merged_df.drop(columns=columns_to_drop, inplace=True)
    html_table = merged_df.to_html(index=False,table_id="myTable", classes="display")
    inflation_queryset = Inflation.objects.values_list('year', 'inflation_rate').order_by('year')
    year, inflation_rate = zip(*inflation_queryset)
    rounded_investment = round(annual_investment_required)
    formatted_investment = '${:,.0f}'.format(rounded_investment)
    total_needed = round(total_needed)
    formatted_total_needed = '${:,.0f}'.format(total_needed)

    return render(request,'pie_chart.html', {"allocation": allocation, "html_table": html_table, "year": list(year), "inflation_rate":list(inflation_rate), "user_profile": user_profile, "annual_investment_required": formatted_investment, "total_needed": formatted_total_needed})

def dashboard(request):
    return render(request, 'dashboard.html', {})

def calculate_investment_for_dividend(desired_dividend, dividend_yield):
    investment_needed = desired_dividend / dividend_yield
    return investment_needed

def get_company_investment_amount(request):
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=365)

    # Filter PriceData instances for the desired year and group by companies
    price_data_for_year = PriceData.objects.filter(date__range=[start_date, end_date]).values('company').annotate(
        max_date=Max('date'), initial_price=Max('close', filter=Q(date__lt=start_date))
    )

    PriceData.objects.prefetch_related('company')
    companies = Company.objects.all()

def favorite(request):
    pass


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user_login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_input')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})