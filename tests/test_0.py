import pytest
from definition_00826e6b8fe44564b3d2c60cb2f17802 import calculate_premium_payment

@pytest.mark.parametrize("notional_amount, premium_rate, expected", [
    # Valid cases
    (1000000.0, 0.01, 10000.0),       # Standard valid input
    (500000.0, 0.005, 2500.0),        # Another valid input
    (1.0, 0.01, 0.01),                # Small notional amount
    (1000000000.0, 0.0001, 100000.0), # Large notional amount, small rate
    (0.0, 0.01, 0.0),                 # Zero notional amount
    (1000000.0, 0.0, 0.0),            # Zero premium rate
    (0.0, 0.0, 0.0),                  # Both zero
    (12345.67, 0.0123, 151.851741),   # Decimal inputs, non-round result

    # Edge cases - Negative inputs (function performs multiplication, so it will return negative)
    (-1000000.0, 0.01, -10000.0),     # Negative notional amount
    (1000000.0, -0.01, -10000.0),     # Negative premium rate
    (-1000000.0, -0.01, 10000.0),     # Both negative

    # Type error cases (inputs that are not numbers)
    ("1000000", 0.01, TypeError),     # String for notional_amount
    (1000000.0, "0.01", TypeError),   # String for premium_rate
    (None, 0.01, TypeError),          # None for notional_amount
    (1000000.0, None, TypeError),     # None for premium_rate
    ([1000000.0], 0.01, TypeError),   # List for notional_amount
    (1000000.0, [0.01], TypeError),   # List for premium_rate
    ({}, 0.01, TypeError),            # Dictionary for notional_amount
    (1000000.0, {}, TypeError),       # Dictionary for premium_rate
    (True, 0.01, float(0.01)),        # Boolean for notional_amount (True is 1, False is 0 in multiplication)
    (1000000.0, False, float(0.0)),   # Boolean for premium_rate
    (1, 0.01, 0.01),                  # Integer for notional_amount
    (1000000.0, 1, 1000000.0),        # Integer for premium_rate
])
def test_calculate_premium_payment(notional_amount, premium_rate, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculate_premium_payment(notional_amount, premium_rate)
    else:
        result = calculate_premium_payment(notional_amount, premium_rate)
        # Using pytest.approx for float comparison due to potential precision issues
        assert result == pytest.approx(expected)