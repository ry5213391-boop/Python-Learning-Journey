print("-----Welcome to simple interest calculator----------")
principal = float(input("Enter principal amount: "))
no_of_years = float(input("Enter number of years: "))
rate = float(input("Enter rate on interest: "))
simple_interest = (principal * no_of_years * rate) / 100
print(f"SIMPLE INTEREST: {simple_interest}")