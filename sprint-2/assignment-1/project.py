def allocate_projects(employees,projects):
    for employee in employees:
        for project in projects:
            if employee['skills']==project['required_skills']:
                employee['current_project']=project['name']
employees = [
    {'name':'John','skills':['Python','Database'],'current_project':None},
    {'name':'Emma','skills':['Java','Testing'],'current_project':None},
    {'name':'Kelly','skills':['Python','Java'],'current_project':None}
]

projects = [
    {'name':'Project A','required_skills':['Python','Database']},
    {'name':'Project B','required_skills':['Java','Testing']},
    {'name':'Project C','required_skills':['Python','Java']}
]


allocate_projects(employees,projects)        
print(employees)