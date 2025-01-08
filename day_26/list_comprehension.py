numbers=[1,2,3]
# new_list=[]
# for n in numbers:
#     add_1=n+1
# new_list.append(add_1)
# new_list=[n+1 for n in numbers]
# print(new_list)
# new_list=[n+n for n in range(1,5) if n<3]
# print(new_list)



# names=["Alex","Beth","Caroline","Dave","Elanor","Freddie"]
# short_names=[name.upper() for name in names if len(name) >5]
# print(short_names)
# list1=["1","2","3"]
# list2=["1","2","3"]
# print(list1 == list2)
import random
names=["Alex","Beth","Caroline","Dave","Elanor","Freddie"]
student_score={students:random.randint(0,100) for students in names}
print(student_score)

passed_students={student:score for (student,score) in student_score.items() if score >= 60}
print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# # result ={word:len(word) for word in sentence.split()} 
# # print(result)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# weather_f = {key:((temp* 9/5) + 32 )for (key, temp) in weather_c.items()}

# print(weather_f)
import pandas

student_dict={
    "student":["Angela","James","Lily"],
    "score":[56,76,98]
}
student_data_frame=pandas.DataFrame(student_dict)
# print(student_data_frame)

#Loop through a data frame

# for (key,value) in student_data_frame.item():
#     print(key)
#     print(value)

#Loop through row of a dta frame
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    if row.student == "Angela":
        print(row.score)