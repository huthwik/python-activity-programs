def calculate_bill(units):
    bill = 0
    if units <= 100:
        bill = units * 1.5
    elif units <= 300:
        bill = (100 * 1.5) + ((units - 100) * 2.5)
    else:
        bill = (100 * 1.5) + (200 * 2.5) + ((units - 300) * 4.0)
    
    bill += 10
    
    if bill > 100:
        bill += bill * 0.10
        
    if units < 100:
        bill -= bill * 0.05
        
    return round(bill, 2)

def analyze_bills(monthly_consumption):
    bills = []
    for month, units in monthly_consumption.items():
        bills.append({"month": month, "units": units, "bill": calculate_bill(units)})
    
    alerts = []
    for i in range(1, len(bills)):
        prev_bill = bills[i-1]["bill"]
        curr_bill = bills[i]["bill"]
        if prev_bill > 0:
            increase = ((curr_bill - prev_bill) / prev_bill) * 100
            if increase > 50:
                alerts.append(f"Unusual increase of {increase:.1f}% detected from {bills[i-1]['month']} to {bills[i]['month']}.")
    
    return bills, alerts

monthly_data = {
    "January": 80,
    "February": 120,
    "March": 130,
    "April": 310,
    "May": 150
}

bills, alerts = analyze_bills(monthly_data)

for b in bills:
    print(f"{b['month']}: Units = {b['units']}, Total Bill = ${b['bill']}")

for alert in alerts:
    print(alert)
