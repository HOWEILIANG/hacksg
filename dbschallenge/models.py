
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

    RISK_APPETITE_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]
    mobile = models.CharField(max_length=20, null=True, blank=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)])
    comfortable_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    bank_statement = models.FileField(upload_to='bank_statements/', null=True, blank=True)
    expected_returns = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(1.0)]
    )
    risk_appetite = models.CharField(max_length=6, choices=RISK_APPETITE_CHOICES, default=MEDIUM)

    def __str__(self):
        return f"User Profile {self.id} - Age: {self.age}"


class Investment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='investments')
    amount_sgd = models.DecimalField(max_digits=15, decimal_places=2)
    covered_with_insurance = models.BooleanField(default=False)

    def __str__(self):
        return f"Investment {self.id} for User {self.user.id}"

class InsuranceProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    premium = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.ticker}"

class Dividend(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    dividend_yield = models.FloatField()

    def __str__(self):
        return f"{self.company} - {self.dividend_yield}"

class PriceData(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return f"{self.date} - {self.close}"

class TreasuryYield(models.Model):
    name = models.CharField(max_length=50)
    coupon = models.FloatField()
    price = models.FloatField()
    yield_percent = models.FloatField()
    one_month_change = models.IntegerField()
    one_year_change = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.date} - {self.yield_percent}"


class Reit(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    distribution_yield = models.FloatField()
    price_to_book = models.FloatField()
    dpu = models.FloatField()  # DPU stands for Distribution Per Unit
    nav = models.FloatField()  # NAV stands for Net Asset Value
    property_yield = models.FloatField()
    gearing_ratio = models.FloatField()

    def __str__(self):
        return f"{self.name}-{self.distribution_yield}"


class Inflation(models.Model):
    year = models.IntegerField(unique=True)
    inflation_rate = models.FloatField()
    annual_change = models.FloatField()

    def __str__(self):
        return f"{self.year}: {self.inflation_rate}, {self.annual_change}"
