# with open("./day_25/weather_data.csv",'r') as data_file:
#     data=data_file.readlines()
    
#     print(data)
import csv
import pandas



# PATH="./day_25/weather_data.csv"
# with open("./day_25/weather_data.csv",'r') as data_file:
#     data=csv.reader(data_file)
#     print(data)
#     temperatures=[]
#     # for week,temp,weeding in data:
# #         temperatures.append(temp)
# # temperatures.pop(0)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
# print(temperatures)

# data=pandas.read_csv(PATH)
# print(data['temp'])
# data_dict= data.to_dict()
# print(data_dict)

# temp_list= data['temp'].to_list()
# # print(sum(temp_list)/len(temp_list))
# # print(data['temp'].mean())
# # print(data['temp'].max())

# #get data in columns
# print(data['condition'])
# print(data.condition)

#get data in the row
# maximo= data['temp'].max()
# print(data[data.temp == maximo])


# monday= data[data.day == "Monday"]
# monday_temp= monday.temp[0] * 9/5 +32
# print(monday_temp)

#creat a dataframe drom scratch
# data_dict={
#     "students": ["Amy","James","Angela"],
#     "scores": [76,56,65]
# }
# data= pandas.DataFrame(data_dict)
# data.to_csv("day_25/new_data.csv")

##########################################################################################
##########################################################################################
# How many squirrel: gray, cinamon, black - Primary Fur Color
PATH="./day_25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
data=pandas.read_csv(PATH)
squirrel=data["Primary Fur Color"]
gray=len(data[(squirrel=="Gray")])
cinnamon=len(data[(squirrel=="Cinnamon")])
black=len(data[(squirrel=="Black")])
print(f"Black={black}, Gray= {gray}, Cinnamon={cinnamon}")

data_dict={
    "Fur Colo":["Gray","Cinnamon","Black"],
    "Count":[gray,cinnamon,black]
}
df=pandas.DataFrame(data_dict)
df.to_csv("./day_25/squirrel_count.csv")
