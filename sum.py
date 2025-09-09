#sum of two numbers
def sum():
    first=int(input("Enter the first number:"))
    second= int(input("enter the second number:"))
    result=first+second
    print(result)
sum()

#with parameters 
def sum(first,second):
    result=first+second
    return result
res=sum(33.5,55)
print(res)
res1=sum(2,7)
print(res1)