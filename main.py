def calculate_tip():
    print("\nWelcome to the Tip Calculator!")

    try:
        bill = float(input("What was the total bill? ₹"))
        tip = float(input("What percentage tip would you like to give? "))
        people = int(input("How many people to split the bill? "))

        tip_percent = tip / 100
        total_tip = bill * tip_percent
        total_bill = bill + total_tip
        bill_per_person = total_bill / people

        final_amount = "{:.2f}".format(bill_per_person)
        print(f"Each person should pay: ₹{final_amount}")

    except ValueError:
        print("Please enter valid numbers only.")

while True:
    calculate_tip()
    again = input("\nDo you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break
