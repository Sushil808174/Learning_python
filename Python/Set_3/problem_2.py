
def add_dic(name,age,dict):
    dict[name] = age;

def update_dic(name,age,dict):
    if name in dict:
        dict[name] = age;
def delete_dict(name,age,dict):
    if name in dict:
        del dict[name];

dict = {}
add_dic("susheel",21,dict)
print(dict)
update_dic("susheel",22,dict)
print(dict)
delete_dict("susheel",22,dict)
print(dict)