sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

res_dictonary={key: sample_dict[key] for key in keys}
print(res_dictonary)