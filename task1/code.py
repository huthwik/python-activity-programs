def rank_applicants(students, min_agg, min_sub, min_att, max_inc):
    eligible = []
    for s in students:
        if s['aggregate'] >= min_agg and all(score >= min_sub for score in s['subjects']) and s['attendance'] >= min_att and s['income'] <= max_inc:
            eligible.append(s)
    
    eligible.sort(key=lambda x: (-x['aggregate'], -x['attendance'], x['income'], x['name']))
    return eligible

students_data = [
    {"name": "Alice", "aggregate": 85, "subjects": [75, 80, 85], "attendance": 90, "income": 40000},
    {"name": "Bob", "aggregate": 82, "subjects": [65, 85, 90], "attendance": 88, "income": 35000},
    {"name": "Charlie", "aggregate": 85, "subjects": [80, 80, 85], "attendance": 92, "income": 45000},
    {"name": "David", "aggregate": 85, "subjects": [80, 85, 80], "attendance": 90, "income": 30000},
    {"name": "Eve", "aggregate": 90, "subjects": [90, 90, 90], "attendance": 95, "income": 20000}
]

ranked_students = rank_applicants(students_data, 80, 70, 85, 50000)

for rank, student in enumerate(ranked_students, 1):
    print(f"Rank {rank}: {student['name']} (Agg: {student['aggregate']}, Att: {student['attendance']}, Inc: {student['income']})")
