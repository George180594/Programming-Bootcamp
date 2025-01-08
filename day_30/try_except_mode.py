#FileNotFound
try:
    file= open('day_30/a_file.txt') 
    a_dictionary={"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file= open('day_30/a_file.txt',"w") 
    file.write("Something")
    file.write("new")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content=file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")

# KeyError
# a_dictionary={"key": "value"}
# value=a_dictionary["non_existen_key"]

#IndexErro
# fruit_list=["apple","Banana","Pear"]
# fruit=fruit_list

#TypeError 
# text="abc"
# print(text+5)