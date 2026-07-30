def calculate_due_amount(bill_amount, paid_amount):
    """
    Calculates the balance after a customer pays a bill.
    Negative result means the customer still owes money.
    Positive result means change is owed back to the customer.
    """ 
    balance = paid_amount - bill_amount
    return balance
input_bill = float(input("Enter the total bill amount: "))
input_paid = float(input("Enter the amount paid by the customer: "))
resulting_balance = calculate_due_amount(bill_amount=input_bill, paid_amount=input_paid)
print("\n--- Transaction Summary ---")
print(f"Total Bill   : ${input_bill:.2f}")
print(f"Amount Paid  : ${input_paid:.2f}")

if resulting_balance < 0:
     print(f"Status       : Customer still owes ${abs(resulting_balance):.2f}")
elif resulting_balance > 0:
    print(f"Status       : Change due to customer: ${resulting_balance:.2f}")
else:
    print("Status       : Bill fully paid. No balance due.")
