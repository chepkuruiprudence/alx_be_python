def safe_divide(numerator, denominator):
    """
    Safely perform division with error handling.

    Args:
        numerator (str or float): The numerator value.
        denominator (str or float): The denominator value.

    Returns:
        str: Result of the division or an error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)

        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
