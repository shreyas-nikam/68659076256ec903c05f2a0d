
import numbers

def calculate_premium_payment(notional_amount: float, premium_rate: float) -> float:
    """
    This function calculates the annual premium payment for the CDS based on the notional amount and premium rate.

    Arguments:
        notional_amount (float): The principal amount of the CDS contract.
        premium_rate (float): The annual premium rate paid by the CDS buyer to the CDS seller (expressed as a decimal).

    Output:
        float: The calculated annual premium payment.
    """
    # Validate that both inputs are real numbers.
    # This correctly handles int, float, and boolean types (which are numeric in Python)
    # and raises TypeError for strings, None, lists, dicts, etc., as per test cases.
    if not isinstance(notional_amount, numbers.Real):
        raise TypeError("notional_amount must be a real number.")
    if not isinstance(premium_rate, numbers.Real):
        raise TypeError("premium_rate must be a real number.")

    # Perform the calculation.
    # Ensure the result is a float, even if inputs were integers.
    return float(notional_amount * premium_rate)


import numbers

def calculate_premium_payment(notional_amount: float, premium_rate: float) -> float:
    """
    This function calculates the annual premium payment for the CDS based on the notional amount and premium rate.

    Arguments:
        notional_amount (float): The principal amount of the CDS contract.
        premium_rate (float): The annual premium rate paid by the CDS buyer to the CDS seller (expressed as a decimal).

    Output:
        float: The calculated annual premium payment.
    """
    # Validate that both inputs are real numbers.
    # This correctly handles int, float, and boolean types (which are numeric in Python)
    # and raises TypeError for strings, None, lists, dicts, etc., as per test cases.
    if not isinstance(notional_amount, numbers.Real):
        raise TypeError("notional_amount must be a real number.")
    if not isinstance(premium_rate, numbers.Real):
        raise TypeError("premium_rate must be a real number.")

    # Perform the calculation.
    # Ensure the result is a float, even if inputs were integers.
    return float(notional_amount * premium_rate)
