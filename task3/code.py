def process_billing(patient):
    name = patient.get("name")
    category = patient.get("category")
    consultation = patient.get("consultation", 0)
    diagnostic = patient.get("diagnostic", 0)
    treatment = patient.get("treatment", 0)
    
    if consultation < 0 or diagnostic < 0 or treatment < 0:
        return {"name": name, "error": "Invalid charges. Must be non-negative."}
    
    base_bill = consultation + diagnostic + treatment
    discount = 0.0
    
    if category == "BPL":
        discount = base_bill * 0.50
    elif category == "Senior Citizen":
        discount = base_bill * 0.20
    elif category == "General" and base_bill > 10000:
        discount = base_bill * 0.10
        
    discounted_bill = base_bill - discount
    final_bill = discounted_bill + (discounted_bill * 0.05)
    
    if final_bill < 5000:
        classification = "Standard"
    else:
        classification = "Premium"
        
    return {
        "name": name,
        "base_bill": base_bill,
        "discount": discount,
        "final_bill": round(final_bill, 2),
        "classification": classification
    }

patients = [
    {"name": "John Doe", "category": "General", "consultation": 500, "diagnostic": 1500, "treatment": 2000},
    {"name": "Jane Smith", "category": "Senior Citizen", "consultation": 800, "diagnostic": 2000, "treatment": 5000},
    {"name": "Mark Twain", "category": "BPL", "consultation": 300, "diagnostic": 500, "treatment": 1000},
    {"name": "Alan Turing", "category": "General", "consultation": 1000, "diagnostic": 4000, "treatment": 6000},
    {"name": "Grace Hopper", "category": "General", "consultation": -100, "diagnostic": 500, "treatment": 500}
]

for p in patients:
    result = process_billing(p)
    if "error" in result:
        print(f"Patient: {result['name']} | Error: {result['error']}")
    else:
        print(f"Patient: {result['name']} | Final Bill: ${result['final_bill']} | Classification: {result['classification']}")
