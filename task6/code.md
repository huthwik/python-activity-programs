**Problem Statement**
Design a railway fare calculation system that computes the ticket cost for multiple passengers based on the distance traveled, the class of accommodation, age-based concessions, and fixed reservation fees. The system must also calculate the penalty amount for any passengers who cancel their tickets, providing a final breakdown of individual fares, penalties, and the total valid revenue generated from the booking.

**Algorithm**

1. Read the journey details: travel distance (in kilometers) and travel class (e.g., SL, 3A, 2A, 1A).
2. Calculate the base fare using distance slabs:
* 0 to 100 km: $0.50 per km
* 101 to 500 km: $50 + $0.40 per km over 100
* > 500 km: $210 + $0.30 per km over 500




3. Apply the class multiplier to the base fare (e.g., SL = 1, 3A = 2, 2A = 3, 1A = 4) to get the standard class fare.
4. Initialize variables to track the total active fare and total cancellation penalties.
5. For each passenger in the booking:
a. Check the passenger's age to determine concessions:
* If age < 12 (Child): Apply a 50% discount on the standard class fare.
* If age >= 60 (Senior): Apply a 30% discount on the standard class fare.
* Otherwise: No discount.
b. Add a fixed reservation fee to the discounted fare to compute the final ticket fare.
c. Check if the passenger's ticket is marked as cancelled.
d. If cancelled, calculate the cancellation penalty (e.g., 20% of the final ticket fare) and add to total penalties.
e. If not cancelled, add the final ticket fare to the total active fare.
f. Store the individual passenger's final fare and penalty details.


6. Output the detailed ticket breakdown for each passenger and the aggregate booking totals.

**Flowchart**

```mermaid
graph TD
    A[Start] --> B[Input Distance and Travel Class]
    B --> C[Calculate Base Fare via Distance Slabs]
    C --> D[Apply Class Multiplier to Base Fare]
    D --> E[Input Passenger List]
    E --> F{More Passengers to Process?}
    F -- Yes --> G[Check Passenger Age]
    G -- Age < 12 --> H[Apply 50% Discount]
    G -- Age >= 60 --> I[Apply 30% Discount]
    G -- 12 <= Age < 60 --> J[No Discount]
    H --> K[Add Fixed Reservation Fee]
    I --> K
    J --> K
    K --> L{Is Ticket Cancelled?}
    L -- Yes --> M[Calculate 20% Cancellation Penalty]
    L -- No --> N[Set Penalty = 0, Add to Total Active Fare]
    M --> O[Add to Total Penalties]
    N --> P[Save Passenger Fare Details]
    O --> P
    P --> F
    F -- No --> Q[Output Individual Details and Totals]
    Q --> R[End]

```




**Sample Input**

```json
distance = 650
travel_class = "3A"
passengers_data = [
    {"name": "Alice", "age": 35, "cancelled": False},
    {"name": "Bob", "age": 65, "cancelled": False},
    {"name": "Charlie", "age": 10, "cancelled": False},
    {"name": "David", "age": 40, "cancelled": True}
]

```

**Sample Output**

```text
Passenger: Alice | Status: Confirmed | Fare: $530.0 | Penalty: $0
Passenger: Bob | Status: Confirmed | Fare: $377.0 | Penalty: $0
Passenger: Charlie | Status: Confirmed | Fare: $275.0 | Penalty: $0
Passenger: David | Status: Cancelled | Fare: $0 | Penalty: $106.0
----------------------------------------
Total Active Fare: $1182.0
Total Penalties Collected: $106.0

```
