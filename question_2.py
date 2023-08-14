employees = [
    {'name':'Susheel kumar','salary':3000,'designation':'developer'},
    {'name':'Aman','salary':4000,'designation':'manager'},
    {'name':'Himanshu','salary':3500,'designation':'tester'}
]

max = 0
dict = {}
for employee in employees:
    if max < employee['salary']:
        max = employee['salary']
        dict = employee

print(dict)