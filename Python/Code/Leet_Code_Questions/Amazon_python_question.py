employees = [
    {"name": "Alice", "department": "HR", "salary": 60000},
    {"name": "Bob", "department": "Engineering", "salary": 95000},
    {"name": "Charlie", "department": "Engineering", "salary": 105000},
    {"name": "Diana", "department": "Sales", "salary": 70000}
]

count = 0
total = 0
d = {}
for i in employees:
    emp = i['name']
    sal = i['salary']
    count = count + 1
    total = total + sal 

avg = round(total/count, 2)
print(avg)
d['total_count'] = count 
d['total_salary'] = total
d['average'] = avg

print(d)    


# # Sample employee table as a list of dictionaries
# employees = [
#     {"name": "Alice", "department": "HR", "salary": 60000},
#     {"name": "Bob", "department": "Engineering", "salary": 95000},
#     {"name": "Charlie", "department": "Engineering", "salary": 105000},
#     {"name": "Diana", "department": "Sales", "salary": 70000}
# ]

# # 1. Count the number of employees
# emp_count = len(employees)

# # 2. Sum the salaries (using a generator expression)
# total_salary = sum(emp['salary'] for emp in employees)

# # 3. Calculate the average salary
# avg_salary = total_salary / emp_count if emp_count > 0 else 0

# print(f"Total Count: {emp_count}")
# print(f"Total Salary Sum: ${total_salary:,}")
# print(f"Average Salary: ${avg_salary:,.2f}")