PLACEHOLDER ='[name]'



with open("mail_merge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("mail_merge/Input/Letters/starting_letter.txt") as text:
    text_list= text.read()
    for name in names:
        stripped_name= name.strip()
        new_text= text_list.replace(PLACEHOLDER,stripped_name)
        with open (f"mail_merge/Output/ReadyToSend/letter_for_{stripped_name}.docx",mode="w") as completed_letter:
            completed_letter.write(new_text)

            




