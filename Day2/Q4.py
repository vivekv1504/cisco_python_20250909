names = input("Enter names separated by spaces: ").split()
sorted_list = sorted(names)
names_tuple = tuple(sorted_list)
filename = "names_data.txt"

with open(filename, "w") as file:
    file.write(f"Sorted list: {sorted_list}\n")
    file.write(f"Tuple: {names_tuple}\n")

with open(filename, "r") as file:
    content = file.read()

print(content)