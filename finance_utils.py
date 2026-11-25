
# Finance Utility Functions

def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


def calculate_compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    interest = amount - principal
    return interest


def calculate_total_amount(principal, interest):
    return principal + interest


def calculate_discount(price, discount_percent):
    discount = (price * discount_percent) / 100
    return price - discount


def calculate_profit(cost_price, selling_price):
    return selling_price - cost_price


# Main Program
if __name__ == "__main__":
    print("Finance Utility Program")

    p = 10000
    r = 5
    t = 2

    si = calculate_simple_interest(p, r, t)
    ci = calculate_compound_interest(p, r, t)

    print("Simple Interest:", si)
    print("Compound Interest:", round(ci, 2))
    print("Total Amount:", calculate_total_amount(p, si))
    print("Discounted Price:", calculate_discount(2000, 10))
    print("Profit:", calculate_profit(500, 700))

