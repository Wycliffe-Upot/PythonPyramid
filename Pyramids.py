# Create a variable 'n' to store the user's number of rows. Use an int data structure for the number value that the user will insert for the rows.
# Use input function to get the user's input.
n = int(input("Enter the number of rows in your pyramid: "))
for i in range(n): # 'i' is a variable for the number of rows.
    for j in range(n - i - 1): # 'j' is the variable for the number of spaces.
        print(" ",end="")
    for j in range(i + 1):
        print("*", end=" ")
    print()