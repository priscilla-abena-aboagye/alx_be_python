user_monthly_income = int(input("Enter your monthly income: "))
user_monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = user_monthly_income - user_monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are ${int(monthly_savings)}")
print(f"Projected savings after one year, with interest, is ${int(projected_savings)}")