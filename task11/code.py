def process_results(marks, max_marks, pass_marks, max_grace_subject, total_grace_allowed):
    total_grace_used = 0
    updated_marks = list(marks)
    
    for i in range(len(updated_marks)):
        if updated_marks[i] < pass_marks:
            deficit = pass_marks - updated_marks[i]
            if deficit <= max_grace_subject and (total_grace_used + deficit) <= total_grace_allowed:
                updated_marks[i] += deficit
                total_grace_used += deficit
                
    passed = all(mark >= pass_marks for mark in updated_marks)
    total = sum(updated_marks)
    percentage = (total / (max_marks * len(marks))) * 100
    
    if passed:
        if percentage >= 75:
            classification = "Distinction"
        elif percentage >= 60:
            classification = "First Class"
        elif percentage >= 50:
            classification = "Second Class"
        else:
            classification = "Pass"
    else:
        classification = "Fail"
        
    return updated_marks, total, percentage, classification

marks = [62, 38, 55, 70, 37]
max_marks = 100
pass_marks = 40
max_grace_subject = 5
total_grace_allowed = 10

final_marks, total_score, percent, result = process_results(
    marks, max_marks, pass_marks, max_grace_subject, total_grace_allowed
)

print(f"Final Marks: {final_marks}")
print(f"Total Marks: {total_score}")
print(f"Percentage: {percent:.2f}%")
print(f"Classification: {result}")
