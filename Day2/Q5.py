num_str=input("Enter the numbers separated byb space : ")
number=[int(x) for x in num_str.split()]
maximum=max(number)
minimum=min(number)

file_name="minmax_data.txt"
with open(file_name, "w") as file:
    file.write(f"Maximum: {maximum}\n")
    file.write(f"Minimum: {minimum}\n")

with open(file_name, "r") as file:
    content = file.read()

print(content)