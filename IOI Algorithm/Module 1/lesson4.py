# act1 

# Python program to print the multiplication table of 23 from 1 to 10
# Loop from 1 to 10
for i in range(1, 11):
    # Print the multiplication of 23 by i
    print(f"23 x {i} = {23 * i}")


# act2

# Python program to print a star pattern based on the number of rows specified by the user
# Get the number of rows from user
n = int(input("Enter the number of rows: "))
# Outer loop for each row
for i in range(1, n+1):
    # Inner loop for each column in the row
    for j in range(i):
        # Print star, end with space instead of new line
        print('*', end=' ')
    # After each row, print a new line
    print()

#act 3

# Python program to calculate the sum of the first ten natural numbers using a while loop

total_sum = 0
num = 1

while num <= 10:
    total_sum += num
    num += 1

print(f"The sum of the first ten natural numbers is {total_sum}")


# act 4

# Python program to check if a number is prime
# Take input from the user
num = int(input("Enter a number: "))
# Check if number is greater than 1 (since primes are > 1)
if num > 1:
    # Loop only up to the square root of num for efficiency
    for i in range(2, int(num**0.5) + 1):
        # If num is divisible by any number, it's not prime
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        # If no divisors were found, the number is prime
        print(f"{num} is a prime number.")
else:
    # Numbers less than 2 are not prime
    print(f"{num} is not a prime number.")