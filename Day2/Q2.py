numbers=list(map(int,input("Enter the numbers with spaces :").split()))
total=sum(numbers)
avg=total/len(numbers) if numbers else 0
file_name = "numbers.txt"
with open(file_name,'w') as writer:
    writer.write(f'List:{numbers}\n')
    writer.write(f'Sum:{total}\n')
    writer.write(f'avg:{avg}')
with open (file_name,'r') as reader:
    content=reader.read()
print(content)