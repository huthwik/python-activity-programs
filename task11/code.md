**Problem Statement**
Write a program to perform financial planning for a campus event. The program must accept fixed costs (venue, equipment, transport), variable costs per person (catering, certificates), existing sponsorship, registration fee per participant, and the expected number of participants. It must calculate the total cost, participant contributions, any sponsorship shortfall, and the minimum number of registrations required to break even.

**Algorithm**

1. Start.
2. Read `venue`, `equipment`, `transport`, `catering_per_person`, `cert_per_person`, `sponsorship`, `reg_fee`, and `participants`.
3. Calculate `fixed_costs = venue + equipment + transport`.
4. Calculate `var_cost_per_person = catering_per_person + cert_per_person`.
5. Calculate `total_cost = fixed_costs + (var_cost_per_person * participants)`.
6. Calculate `participant_contribution = reg_fee * participants`.
7. Calculate `total_revenue = participant_contribution + sponsorship`.
8. Calculate `shortfall = total_cost - total_revenue`. If `shortfall < 0`, set `shortfall = 0`.
9. Check break-even condition:
a. If `reg_fee > var_cost_per_person`:
i. `remaining_fixed = fixed_costs - sponsorship`
ii. If `remaining_fixed <= 0`, `break_even = 0`.
iii. Else, `break_even = ceiling(remaining_fixed / (reg_fee - var_cost_per_person))`.
b. Else:
i. If `fixed_costs <= sponsorship`, `break_even = 0`.
ii. Else, `break_even = -1` (impossible to break even).
10. Print `total_cost`, `participant_contribution`, `shortfall`, and `break_even`.
11. Stop.

**Flowchart**

```mermaid
graph TD
    A[Start] --> B[/Input fixed costs, variable costs, sponsorship, reg_fee, participants/]
    B --> C[fixed_costs = venue + equipment + transport<br>var_cost_per_person = catering + cert]
    C --> D[total_cost = fixed_costs + var_cost_per_person * participants]
    D --> E[participant_contribution = reg_fee * participants<br>total_revenue = participant_contribution + sponsorship]
    E --> F[shortfall = total_cost - total_revenue]
    F --> G{shortfall < 0?}
    G -- Yes --> H[shortfall = 0]
    G -- No --> I{reg_fee > var_cost_per_person?}
    H --> I
    I -- Yes --> J[remaining = fixed_costs - sponsorship]
    I -- No --> K{fixed_costs <= sponsorship?}
    K -- Yes --> L[break_even = 0]
    K -- No --> M[break_even = -1]
    J --> N{remaining <= 0?}
    N -- Yes --> O[break_even = 0]
    N -- No --> P[break_even = ceil(remaining / (reg_fee - var_cost_per_person))]
    L --> Q
    M --> Q
    O --> Q
    P --> Q
    Q[/Print total_cost, participant_contribution, shortfall, break_even/]
    Q --> R[Stop]

```

**Python Source Code**

```python
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

```

**Sample Input**

```text
Enter venue cost: 2000
Enter equipment cost: 500
Enter transport cost: 300
Enter catering cost per person: 15
Enter certificate cost per person: 5
Enter sponsorship amount: 1000
Enter registration fee per participant: 50
Enter expected number of participants: 60

```

**Sample Output**

```text
Total Cost: 4000.00
Participant Contributions: 3000.00
Sponsorship Shortfall: 0.00
Minimum Registrations to Break Even: 60

```
