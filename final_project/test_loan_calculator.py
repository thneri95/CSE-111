import pytest
from final_project import ( 
    validate_positive_float,
    validate_non_negative_float,
    calculate_monthly_payment,
    calculate_loan_totals,
    generate_amortization_schedule,
)


def test_validate_positive_float_valid():
    assert validate_positive_float(1000, "amount") is True
    assert validate_positive_float(0.01, "rate") is True

def test_validate_positive_float_invalid():
    assert validate_positive_float(0, "amount") is False
    assert validate_positive_float(-100, "amount") is False

def test_validate_non_negative_float_valid():
    assert validate_non_negative_float(1000, "amount") is True
    assert validate_non_negative_float(0, "rate") is True
    assert validate_non_negative_float(0.05, "rate") is True

def test_validate_non_negative_float_invalid():
    assert validate_non_negative_float(-0.01, "rate") is False
    assert validate_non_negative_float(-50, "amount") is False

def test_calculate_monthly_payment_basic():
    principal = 1000
    monthly_rate = 0.05 / 12
    num_payments = 12
    expected_payment = 85.60747548652537
    assert pytest.approx(calculate_monthly_payment(principal, monthly_rate, num_payments), rel=1e-6) == expected_payment

def test_calculate_monthly_payment_zero_interest():
    principal = 1000
    monthly_rate = 0
    num_payments = 10
    expected_payment = 100
    assert calculate_monthly_payment(principal, monthly_rate, num_payments) == expected_payment

def test_calculate_monthly_payment_large_loan():
    principal = 1000000
    monthly_rate = 0.01  # 1% ao mês
    num_payments = 360  # 30 anos
    expected_payment = 10286.13282953386
    assert pytest.approx(calculate_monthly_payment(principal, monthly_rate, num_payments), rel=1e-6) == expected_payment

def test_calculate_loan_totals_basic():
    principal = 1000
    monthly_rate = 0.05 / 12
    num_payments = 12
    monthly_payment = calculate_monthly_payment(principal, monthly_rate, num_payments)
    expected_total_paid = monthly_payment * num_payments
    expected_total_interest = expected_total_paid - principal
    total_paid, total_interest = calculate_loan_totals(principal, monthly_rate, num_payments)
    assert pytest.approx(total_paid, rel=1e-6) == expected_total_paid
    assert pytest.approx(total_interest, rel=1e-6) == expected_total_interest

def test_calculate_loan_totals_zero_interest():
    principal = 2000
    monthly_rate = 0
    num_payments = 24
    total_paid, total_interest = calculate_loan_totals(principal, monthly_rate, num_payments)
    assert total_paid == 2000
    assert total_interest == 0

def test_generate_amortization_schedule_basic():
    principal = 1000
    monthly_rate = 0.05 / 12
    num_payments = 2
    schedule = generate_amortization_schedule(principal, monthly_rate, num_payments)
    assert len(schedule) == 2
    assert pytest.approx(schedule[0]['Payment'], rel=1e-6) == calculate_monthly_payment(principal, monthly_rate, num_payments)
    assert pytest.approx(schedule[1]['Remaining Balance'], abs=1e-9) == 0

def test_generate_amortization_schedule_zero_interest():
    principal = 500
    monthly_rate = 0
    num_payments = 5
    schedule = generate_amortization_schedule(principal, monthly_rate, num_payments)
    assert len(schedule) == 5
    assert schedule[0]['Principal Paid'] == 100
    assert schedule[0]['Interest Paid'] == 0
    assert schedule[0]['Remaining Balance'] == 400
    assert schedule[-1]['Remaining Balance'] == 0


# To do this test please: 
# Open the Terminal 
# Write >>>  python -m pytest  
# Press enter