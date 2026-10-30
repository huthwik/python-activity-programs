budget = float(input("Enter total budget (Base Currency): "))
fee_pct = float(input("Enter conversion fee percentage: "))
n = int(input("Enter number of expense categories: "))

total_expense = 0.0
max_expense = 0.0
max_category = ""

for _ in range(n):
    cat = input("Enter category name: ")
    amount = float(input(f"Enter amount for {cat} (Foreign Currency): "))
    rate = float(input(f"Enter exchange rate (Base per Foreign) for {cat}: "))
    
    base_cost = amount * rate
    final_cost = base_cost + (base_cost * (fee_pct / 100))
    total_expense += final_cost
    
    if final_cost > max_expense:
        max_expense = final_cost
        max_category = cat

print(f"\nTotal Expense: {total_expense:.2f}")
print(f"Largest Expense Category: {max_category} ({max_expense:.2f})")

if total_expense <= budget:
    print("Status: Within budget")
else:
    print("Status: Over budget")
  
