sentence=input("Enter the sentence:")
words_list = sentence.split()
words_tuple = tuple(word.upper() for word in words_list)
file_name='sentence.txt'
with open (file_name,'w') as file:
    file.write(f'List of words:{words_list}\n')
    file.write(f'tuple :{words_tuple}')
with open(file_name,'r') as file:
    content=file.read()
print(content)