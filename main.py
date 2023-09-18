# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

avarage = sum(temp_list) / len(temp_list)
print(avarage)

print(data["temp"].mean())
print(data["temp"].max())

#get data from colum condition
print(data.condition)

#Get data in row
print(data[data.day == "Monday"])

#Get Max temp and data
print(data[data.temp == data.temp.max()])

#Get data from operator
monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

#Create a data frame from scratch:
data_dict_scratch = {
    "students": ["Alex", "Oleg", "Max"],
    "scores": [76, 56, 65]
}
data_scratch = pandas.DataFrame(data_dict_scratch)
print(data_scratch)
data_scratch.to_csv("new_data.csv")
