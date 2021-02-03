#income = 1000
#tax = 0.3
#calculate_income
print("Type your income")
income =  input()
tax = 0.3
tax_deducted = int(income) * tax
gross_income = int(income) - tax_deducted
print("your income"+str(gross_income))
