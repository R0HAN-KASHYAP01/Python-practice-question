num = int(input("Enter the number: "))
original_num = num
reverse = 0
while(num!= 0):
    digit = num %10
    reverse = reverse *10 + digit
    num = num // 10

print(f"The reverse of {num} is {reverse}")
