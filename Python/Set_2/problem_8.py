employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

emp_dictionary = {}

for emp in employees:
    emp_dictionary[emp] = defaults;
print(emp_dictionary);