print("Welcome to the tip calculator")
print("-----------------------------")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

final_bill = total_bill + (total_bill * tip_percentage / 100)
final_bill_per_person = round(final_bill / number_of_people, 2)

print(f"Each person should pay ${final_bill_per_person}.")