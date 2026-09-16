# Lesson 2 - Data Cleaning without Pandas

employees = [
    {"name": "Rajina", "department": "Analytics", "salary": 85000},
    {"name": "Ritesh", "department": "IT", "salary": None},
    {"name": "Anu", "department": "HR", "salary": 62000},
    {"name": "John", "department": "Finance", "salary": None}
]

print("Original Data")
print("-" * 30)

for emp in employees:
    print(emp)

# Replace missing salaries with 50000
for emp in employees:
    if emp["salary"] is None:
        emp["salary"] = 50000

print("\nCleaned Data")
print("-" * 30)

for emp in employees:
    print(emp)