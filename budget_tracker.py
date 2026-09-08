import csv
print("Welcome To EPA Budget Tracker!   ")
totals = {}
choice = ""

while choice != "quit":
    print("1.Log an expense\n2.View totals\n3.Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        category = input("Food,Rent,Fun: ")
        amount_spent = float(input("Enter the amount spent: "))
        with open("expenses.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([category, amount_spent])
    elif choice == "2":
        totals = {}
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                category, amount = row
                category = category.lower()
                amount = float(amount)
                if category in totals:
                    totals[category] += amount
                else:
                    totals[category] = amount

        grand_total = 0
        for category, total in totals.items():
            grand_total += total
            print(f"{category}: ${total}")
        print(f"Grand Total: ${grand_total}")
    elif choice == "3" or choice == "q":
        print("Goodbye !!")
        break

 


