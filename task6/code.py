def calculate_railway_fare(distance, travel_class, passengers):
    if distance <= 100:
        base_fare = distance * 0.50
    elif distance <= 500:
        base_fare = 50 + ((distance - 100) * 0.40)
    else:
        base_fare = 210 + ((distance - 500) * 0.30)
        
    class_multipliers = {"SL": 1, "3A": 2, "2A": 3, "1A": 4}
    multiplier = class_multipliers.get(travel_class, 1)
    class_fare = base_fare * multiplier
    
    reservation_fee = 20
    cancellation_rate = 0.20
    
    results = []
    total_active_fare = 0
    total_penalties = 0
    
    for p in passengers:
        discount = 0
        if p["age"] < 12:
            discount = class_fare * 0.50
        elif p["age"] >= 60:
            discount = class_fare * 0.30
            
        ticket_fare = (class_fare - discount) + reservation_fee
        
        if p.get("cancelled", False):
            penalty = ticket_fare * cancellation_rate
            total_penalties += penalty
            results.append({"name": p["name"], "status": "Cancelled", "fare": 0, "penalty": round(penalty, 2)})
        else:
            total_active_fare += ticket_fare
            results.append({"name": p["name"], "status": "Confirmed", "fare": round(ticket_fare, 2), "penalty": 0})
            
    return results, round(total_active_fare, 2), round(total_penalties, 2)

distance = 650
travel_class = "3A"
passengers_data = [
    {"name": "Alice", "age": 35, "cancelled": False},
    {"name": "Bob", "age": 65, "cancelled": False},
    {"name": "Charlie", "age": 10, "cancelled": False},
    {"name": "David", "age": 40, "cancelled": True}
]

details, total_fare, total_penalty = calculate_railway_fare(distance, travel_class, passengers_data)

for d in details:
    print(f"Passenger: {d['name']} | Status: {d['status']} | Fare: ${d['fare']} | Penalty: ${d['penalty']}")
print("-" * 40)
print(f"Total Active Fare: ${total_fare}")
print(f"Total Penalties Collected: ${total_penalty}")
