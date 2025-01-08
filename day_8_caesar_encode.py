


####functions####
def caesar(original_text, shift_amount, encode_or_decode):
    import string as st
    letters=st.ascii_lowercase
    alphabet=[]
    for l in letters:
        alphabet+=l
    ######################################
    output_text=''
    if encode_or_decode=='decode':
        shift_amount*=-1
    for letter in original_text:
        if letter not in alphabet:
            output_text+=letter
        else:
            if encode_or_decode=='decode':
                shift_amount*=-1
                
            shifted_position= alphabet.index(letter)+shift_amount
            shifted_position=shifted_position % len(alphabet)
            output_text+=alphabet[shifted_position] 
    print(f'Here is the decoded result: {output_text}')

should_continue= True
while should_continue:
    ##### Constants####
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input('Type the shift number:\n'))
    caesar(original_text=text, shift_amount=shift,encode_or_decode= direction)
    restart=input("Type 'yes' if you want to go again. Otherwise, type'no'.").lower()
    if restart=='no':
        should_continue=False
        print('Goodbye')
