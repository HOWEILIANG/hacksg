def calculate_future_value(A, i, N):
    F = A * (((1 + i) ** N - 1) / i)
    return F

def calculate_present_value(A, i, N):
    P = A * (1 - (1 + i) ** -N) / i
    return P

def calculate_annual_investment(FVA, i, N):
    P = FVA * i / (((1 + i) ** N) - 1)
    return P

def amount_needed_for_retirement(current_salary, current_age, retirement_age, end_age, inflation_rate):
    # Annual amount needed based on current salary
    annual_expense = current_salary * 12

    # Number of years until retirement
    years_until_retirement = retirement_age - current_age

    # Calculate the amount needed per year at the start of retirement
    annual_expense_at_retirement = annual_expense * ((1 + inflation_rate) ** years_until_retirement)

    # Number of years in retirement
    years_in_retirement = end_age - retirement_age

    # Calculate the total amount needed for the retirement period
    total_amount_needed = calculate_present_value(annual_expense_at_retirement, inflation_rate, years_in_retirement)

    return total_amount_needed

def retirement_plan(current_salary, current_age, retirement_age, end_age, inflation_rate, expected_return):
    # Number of years until retirement
    years_until_retirement = retirement_age - current_age
    # Calculate the total amount needed for the retirement period
    total_amount_needed = amount_needed_for_retirement(current_salary, current_age, retirement_age, end_age, inflation_rate)

    # Calculate the annual investment required to accumulate the needed amount by retirement
    annual_investment = calculate_annual_investment(total_amount_needed, expected_return, years_until_retirement)

    return annual_investment
