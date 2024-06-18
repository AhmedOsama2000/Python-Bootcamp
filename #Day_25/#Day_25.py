"""
Pandas library is the most famous python library in Data Analysis
useful for analyze data from exel sheets for example
CSV files stands for comma seperated values
CSV library is helpful to work with CSV files instead of just read file
"""

"""
More about pandas library:
dataframes vs. series (Two primary data structure of pandas)
1) dataframes (two dimensional): like a CSV table
2) series (one dimensional) : a single column from CSV table

Iterate over dataFrames using iterrows (built-in loop method), it returns list of both (index, row)

"""

# filename = "weather_data.csv"
# with open(filename) as file:
#     data = file.readlines()
#

# import csv
#
# with open(filename) as data_file:
#     temperatures = []
#     data = csv.reader(data_file)  # returns an object that can be looped through
#     data = list(data)
#     for row in data[1:]:
#         temperatures.append(int(row[1]))
#
#     print(temperatures)

# Another way to do such a thing -> using Pandas
import pandas
# data = pandas.read_csv("weather_data.csv")

# print(type(data["day"]))
#
# print(type(data))

# Convert the CSV dataframe into a dictionary
# data_dict = data.to_dict()
# print(data_dict)

# Convert a CSV series into a list
# data_list = data["temp"].to_list()
# max_value = data["temp"].max()
# print(data_list)
# # print("average temperature is: " + str(sum(data_list)/len(data_list)))
#
# # Or, you can do this!
# print(data["temp"].mean())  # mean() is used to get the average value of a series
#
# print(max_value)

# pandas take the headlines of the columns and save it as attributes
# print(data.condition)

# Get data in rows of the dataframe
# print(data[data.day == "Monday"])

# Return the day that has the max temperature
# print(data[data.temp == max_value])

# get the temperature of monday in Fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# degree_in_f = monday_temp*(9/5) + 32.0
# print(degree_in_f)

# Create data frame from scratch
# data_dict = {
#     "students": ["Ahmed", "Mai", "Menna"],
#     "scores": [76, 78, 80]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# # and we can convert this data into csv file
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

fur_colors = data["Primary Fur Color"].drop_duplicates().dropna().to_list()

squirrel_num = data["Primary Fur Color"].value_counts().to_list()

squirrel_dict = {
    "Fur Color": fur_colors,
    "Count": squirrel_num
}

data_frame = pandas.DataFrame(squirrel_dict)
data_frame.to_csv("Squirrel_data.csv")





