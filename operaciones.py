# operaciones.py

def validate_sales(sales):
    """
    Validates that the sales amount is not negative.
    """
    return sales >= 0


def validate_name(name):
    """
    Validates that the seller's name is not empty.
    """
    return name.strip() != ""


def get_sales_category(sales):
    """
    Returns the sales category based on the sales amount.
    """
    if sales >= 50000:
        return "Top Sales"
    elif sales >= 25000:
        return "High Sales"
    elif sales >= 10000:
        return "Medium Sales"
    else:
        return "Low Sales"


def format_money(amount):
    """
    Formats an amount as currency.
    """
    return f"${amount:,.2f}"


def create_seller_record(name, sales):
    """
    Creates a seller record using a dictionary.
    """
    return {
        "name": name,
        "sales": sales
    }