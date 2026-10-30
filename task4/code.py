def generate_payroll(employees):
    statements = []
    
    for emp in employees:
        ot_pay = emp['ot_hours'] * emp['ot_rate']
        gross_salary = emp['basic'] + emp['allowances'] + ot_pay + emp['incentives']
        
        deductions = 0
        if gross_salary > 100000:
            deductions = (50000 * 0.10) + ((gross_salary - 100000) * 0.20)
        elif gross_salary > 50000:
            deductions = (gross_salary - 50000) * 0.10
            
        net_salary = gross_salary - deductions
        
        statements.append({
            "emp_id": emp['emp_id'],
            "name": emp['name'],
            "gross": round(gross_salary, 2),
            "deductions": round(deductions, 2),
            "net": round(net_salary, 2)
        })
        
    return statements

employees_data = [
    {"emp_id": "E101", "name": "Alice", "basic": 40000, "allowances": 8000, "ot_hours": 10, "ot_rate": 200, "incentives": 0},
    {"emp_id": "E102", "name": "Bob", "basic": 60000, "allowances": 15000, "ot_hours": 5, "ot_rate": 300, "incentives": 5000},
    {"emp_id": "E103", "name": "Charlie", "basic": 90000, "allowances": 20000, "ot_hours": 20, "ot_rate": 500, "incentives": 15000},
    {"emp_id": "E104", "name": "Diana", "basic": 30000, "allowances": 5000, "ot_hours": 0, "ot_rate": 0, "incentives": 2000}
]

payroll_statements = generate_payroll(employees_data)

for stmt in payroll_statements:
    print(f"ID: {stmt['emp_id']} | Name: {stmt['name']}")
    print(f"Gross Salary: ${stmt['gross']} | Deductions: ${stmt['deductions']} | Net Salary: ${stmt['net']}")
    print("-" * 50)
