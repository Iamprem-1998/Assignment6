import json
with open ("D:\\DATA SCIENCE CLASS\\Assignment6\\question_1\\employee.json") as file:
    data=json.load(file)
    print(data)
for i in file:
    print(i)