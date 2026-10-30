def generate_invoice(cart, threshold, discount_rate, max_concession):
    tax_rates = {
        "Electronics": 0.18,
        "Clothing": 0.12,
        "Grocery": 0.05
    }
    
    subtotal = 0
    total_tax = 0
    itemized_list = []
    
    for item in cart:
        base_price = item["price"] * item["quantity"]
        rate = tax_rates.get(item["category"], 0.0)
        item_tax = base_price * rate
        
        subtotal += base_price
        total_tax += item_tax
        
        itemized_list.append({
            "name": item["name"],
            "base_price": round(base_price, 2),
            "tax": round(item_tax, 2)
        })
        
    gross_total = subtotal + total_tax
    discount = 0
    
    if gross_total > threshold:
        calc_discount = gross_total * discount_rate
        discount = min(calc_discount, max_concession)
        
    net_total = gross_total - discount
    
    return {
        "items": itemized_list,
        "subtotal": round(subtotal, 2),
        "total_tax": round(total_tax, 2),
        "gross_total": round(gross_total, 2),
        "discount": round(discount, 2),
        "net_total": round(net_total, 2)
    }

cart_data = [
    {"name": "Smartphone", "category": "Electronics", "price": 600.0, "quantity": 1},
    {"name": "Jeans", "category": "Clothing", "price": 40.0, "quantity": 2},
    {"name": "Rice", "category": "Grocery", "price": 25.0, "quantity": 4}
]

invoice = generate_invoice(cart_data, 500, 0.10, 50)

print("ITEMIZED INVOICE")
print("-" * 30)
for i in invoice["items"]:
    print(f"{i['name']}: Base = ${i['base_price']}, Tax = ${i['tax']}")
print("-" * 30)
print(f"Subtotal: ${invoice['subtotal']}")
print(f"Total Tax: ${invoice['total_tax']}")
print(f"Gross Total: ${invoice['gross_total']}")
print(f"Discount Applied: -${invoice['discount']}")
print(f"Net Payable: ${invoice['net_total']}")
