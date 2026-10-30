def find_best_plan(req_data, req_calls, budget, plans):
    best_plan = None
    min_cost = float('inf')
    
    for plan in plans:
        excess_data = max(0, req_data - plan['data_limit'])
        excess_calls = max(0, req_calls - plan['call_limit'])
        
        excess_data_cost = excess_data * plan['data_rate']
        excess_call_cost = excess_calls * plan['call_rate']
        
        total_cost = plan['cost'] + excess_data_cost + excess_call_cost
        
        if total_cost <= budget and total_cost < min_cost:
            min_cost = total_cost
            best_plan = plan['name']
            
    if best_plan:
        return {"plan": best_plan, "total_cost": round(min_cost, 2)}
    else:
        return {"error": "No eligible plan found within budget."}

user_req_data = 45
user_req_calls = 600
user_budget = 60.00

available_plans = [
    {"name": "Basic", "cost": 20.0, "data_limit": 15, "call_limit": 300, "data_rate": 1.5, "call_rate": 0.10},
    {"name": "Standard", "cost": 35.0, "data_limit": 40, "call_limit": 500, "data_rate": 1.0, "call_rate": 0.05},
    {"name": "Premium", "cost": 50.0, "data_limit": 100, "call_limit": 1000, "data_rate": 0.5, "call_rate": 0.02},
    {"name": "Data Heavy", "cost": 40.0, "data_limit": 60, "call_limit": 200, "data_rate": 1.0, "call_rate": 0.15}
]

result = find_best_plan(user_req_data, user_req_calls, user_budget, available_plans)

if "error" in result:
    print(result["error"])
else:
    print(f"Most Economical Plan: {result['plan']}")
    print(f"Total Calculated Cost: ${result['total_cost']}")
