valid=False
while not valid:
    try:
        bill_amount=float(input("Enter the bill amount: "))
        discount_amount=float(input("Enter the discount amount: "))
        numberofpeople=int(input("Enter the number of people"))
        discount=(discount_amount/100)*bill_amount
        final_amount=bill_amount-discount
        final_amountperperson=final_amount/numberofpeople
    except ValueError as ve:
        print(ve,"I need a decimal number")
    except ZeroDivisionError as zde:
        print(zde,"You cannot divide by zero") 
if bill_amount==0 and discount_amount==0:
        raise ValueError
else:
    print("Summary of your purchase")
    print("************************")
    print(f"The bill amount is {bill_amount}")
    print(f"The discount amount is {discount_amount}")
    print(f"The number of people is {numberofpeople}")
    print(f"The discount is {discount}")
    print(f"The final amount to pay is {final_amount}")
    print(f"The final amount per person is {final_amountperperson}")
    print("Thank you for your purchase lets hope we meet again 😊")
        


