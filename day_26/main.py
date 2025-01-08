import pandas
# import csv
PATH= "day_26/nato_phonetic_alphabet.csv"
# with open(PATH,"r") as data_file:
#     data=csv.reader(data_file)

# print(data)


data=pandas.read_csv(PATH)
# print(file)


dict_data={row.letter:row.code for (index,row) in data.iterrows()}

print(dict_data)

word=input('Enter a word:').upper()
output_list=[dict_data[letter] for letter in word]
print(output_list)

