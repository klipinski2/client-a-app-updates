# client-a-app-updates

# Calculate lead time for MRO part delivery

def calculate_lead_time(order_date, delivery_date):
    """
    Returns the number of days between order and delivery.
    """
    delta = delivery_date - order_date
    return delta.days

# Example usage
import datetime

order_date = datetime.date(2025, 6, 1)
delivery_date = datetime.date(2025, 6, 10)

lead_time = calculate_lead_time(order_date, delivery_date)
print(f"Lead time for MRO part delivery: {lead_time} days")
