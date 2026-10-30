import math

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
transport = float(input("Enter transport cost: "))
catering_per_person = float(input("Enter catering cost per person: "))
cert_per_person = float(input("Enter certificate cost per person: "))
sponsorship = float(input("Enter sponsorship amount: "))
reg_fee = float(input("Enter registration fee per participant: "))
participants = int(input("Enter expected number of participants: "))

fixed_costs = venue + equipment + transport
var_cost_per_person = catering_per_person + cert_per_person
total_cost = fixed_costs + (var_cost_per_person * participants)

participant_contribution = reg_fee * participants
total_revenue = participant_contribution + sponsorship

shortfall = total_cost - total_revenue
if shortfall < 0:
    shortfall = 0.0

if reg_fee > var_cost_per_person:
    remaining_fixed = fixed_costs - sponsorship
    if remaining_fixed <= 0:
        break_even = 0
    else:
        break_even = math.ceil(remaining_fixed / (reg_fee - var_cost_per_person))
else:
    if fixed_costs <= sponsorship:
        break_even = 0
    else:
        break_even = -1

print(f"\nTotal Cost: {total_cost:.2f}")
print(f"Participant Contributions: {participant_contribution:.2f}")
print(f"Sponsorship Shortfall: {shortfall:.2f}")
if break_even == -1:
    print("Minimum Registrations to Break Even: Impossible (Variable cost exceeds registration fee)")
else:
    print(f"Minimum Registrations to Break Even: {break_even}")
