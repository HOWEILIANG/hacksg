from dbschallenge.models import UserProfile


def recommend_portfolio_mix(user_profile):
    """https://www.stashaway.sg/r/best-investment-options-singapore"""
    age = user_profile.age
    risk_appetite = user_profile.risk_appetite

    # Define base allocation percentages based on risk appetite
    if risk_appetite == UserProfile.LOW:
        base_allocations = {'cash': 30, 'bonds': 40, 'reits': 10, 'stocks': 20}
    elif risk_appetite == UserProfile.MEDIUM:
        base_allocations = {'cash': 20, 'bonds': 30, 'reits': 20, 'stocks': 30}
    else:  # HIGH risk appetite
        base_allocations = {'cash': 10, 'bonds': 20, 'reits': 20, 'stocks': 50}

    # Adjust allocations based on age
    if age < 30:
        base_allocations['stocks'] += 10
        base_allocations['cash'] -= 5
        base_allocations['bonds'] -= 5
    elif age > 60:
        base_allocations['stocks'] -= 10
        base_allocations['cash'] += 5
        base_allocations['bonds'] += 5
    elif age >= 30 and age <= 60:
        adjustment_factor = (age - 30) / 30  # Adjustment factor increases linearly from 0 to 1
        base_allocations['stocks'] -= adjustment_factor * 10
        base_allocations['cash'] += adjustment_factor * 5
        base_allocations['bonds'] += adjustment_factor * 5

    if age > 70:
        base_allocations['cash'] += 100 - (base_allocations['bonds'] + base_allocations['reits'] + base_allocations['cash'])
        base_allocations['stocks'] = 0
    return base_allocations
