material_cost = float(input("Enter material cost: "))
labour_charge = float(input("Enter labour charge: "))
wastage_cost = float(input("Enter wastage cost: "))
machine_cost = float(input("Enter machine cost: "))
selling_price = float(input("Enter selling price: "))
profit_target = float(input("Enter profit target: "))

total_cost = material_cost + labour_charge + wastage_cost + machine_cost
profit = selling_price - total_cost

print(f"\nTotal Cost: {total_cost:.2f}")
print(f"Profit: {profit:.2f}")

if profit >= profit_target:
    print("Target Met: Yes")
else:
    print("Target Met: No")
