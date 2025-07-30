# Find the computer must find the square root of the number given

num = int(input("Enter a number so that we can find the square root "))
num2 = num ** 0.5

if num2.is_integer(): 
    print("The square root of", num, "is", int(num2))
else:
    print("It's not a perfect square.")
