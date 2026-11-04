**Problem Statement**
Design a manufacturing analysis system that evaluates the profitability of a production run. The system must calculate the total production cost by aggregating raw material costs, labor charges, machine operational costs, and wastage penalties. It will then compute the total revenue generated from the selling price, determine the net profit or loss, calculate the profit margin percentage, and evaluate whether the production meets a predefined target profit margin.

**Algorithm**

1. Read the input parameters: number of units produced, material cost per unit, labor hours, labor rate, machine hours, machine rate, total wastage cost, selling price per unit, and the target profit margin percentage.
2. Calculate total material cost by multiplying units produced by the material cost per unit.
3. Calculate total labor cost by multiplying labor hours by the labor rate.
4. Calculate total machine cost by multiplying machine hours by the machine rate.
5. Calculate the total production cost by summing the material cost, labor cost, machine cost, and wastage cost.
6. Calculate the total revenue by multiplying the units produced by the selling price per unit.
7. Calculate the net profit (or loss) by subtracting the total production cost from the total revenue.
8. Calculate the actual profit margin percentage as (net profit / total production cost) * 100.
9. Compare the actual profit margin with the target profit margin to determine if the target was met.
10. Output the computed costs, revenue, profit amount, profit margin, and the target evaluation status.

**Flowchart**

```mermaid
graph TD
    A[Start] --> B[Input Production Data & Target Margin]
    B --> C[Calculate Material Cost = Units * Material Rate]
    C --> D[Calculate Labor Cost = Labor Hrs * Labor Rate]
    D --> E[Calculate Machine Cost = Machine Hrs * Machine Rate]
    E --> F[Calculate Total Cost = Material + Labor + Machine + Wastage]
    F --> G[Calculate Total Revenue = Units * Selling Price]
    G --> H[Calculate Profit = Total Revenue - Total Cost]
    H --> I[Calculate Margin % = Profit / Total Cost * 100]
    I --> J{Margin % >= Target Margin?}
    J -- Yes --> K[Set Status = Target Achieved]
    J -- No --> L[Set Status = Target Not Achieved]
    K --> M[Output Financial Summary & Status]
    L --> M
    M --> N[End]

```



**Sample Input**

```json
{
    "units": 1000,
    "material_rate": 15.0,
    "labor_hours": 200,
    "labor_rate": 25.0,
    "machine_hours": 50,
    "machine_rate": 100.0,
    "wastage_cost": 500.0,
    "selling_price": 35.0,
    "target_margin": 30.0
}

```

**Sample Output**

```text
Total Production Cost: $25500.0
Total Revenue: $35000.0
Net Profit: $9500.0
Profit Margin: 37.25%
Status: Profit target achieved.

```
