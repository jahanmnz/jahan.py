"""x = input ("Enter your age=> ")

if int(x) < 18:
    print(x + " you are minor ")
else:
     print(x + " you are an adult ")
     
print()""



first = float(input("Enter your first number=> "))
sec = float(input("Enter your second numer=>  "))
opr = input("select your operation(+ , - , * , /)")

print(eval (f"{first} {opr} {sec}"))



even_numbers = [2 * x for x in range(1, 11)]

for number in even_numbers:
    
    print(number)"""



second = "second"
minute = "minute"
day = "day"
year = "year"

num = int(input("Enter how many years you want to convert "))
opr = input("Which you want to convert")

if opr == second:
    print(num * 60 * 60 * 24 * 365)
elif opr == minute:
    print(num * 60 * 24 * 365)
elif opr == day:
    print(num * 24 * 365)
elif opr == year:
    print(num * 365)
else:
    print("Invalid choice")


# initialize the counter
counter = 1

# loop until the counter reaches 5
while counter <= 5:
  # calculate the square of the counter
  square = counter ** 2

  # print the square
  print(square)

  # increment the counter by 1
  counter += 1



# define the function is_palindrome
def is_palindrome(string):
  # convert the string to lowercase and remove spaces and punctuation
  string = string.lower().replace(" ", "").replace(".", "").replace(",", "")

  # reverse the string
  reversed_string = string[::-1]

  # check if the string and its reverse are equal
  if string == reversed_string:
    # return True if they are equal
    return True
  else:
    # return False otherwise
    return False

# demonstrate the usage of the function by checking some strings
print(is_palindrome("radar")) # prints True
print(is_palindrome("Python")) # prints False


# define the function sum_multiples
def sum_multiples(n):
  # initialize the sum to zero
  sum = 0

  # loop through all the numbers from 1 to n-1
  for i in range(1, n):
    # check if the number is a multiple of 3 or 5
    if i % 3 == 0 or i % 5 == 0:
      # add the number to the sum
      sum += i

  # return the sum
  return sum

# demonstrate the usage of the function by calculating the sum of multiples of 3 and 5 less than 100
print(sum_multiples(100)) # prints 2318


# define the function print_triangle
def print_triangle(n):
  # loop through the rows from 1 to n
  for i in range(1, n+1):
    # print i asterisks followed by a newline
    print("*" * i)

# demonstrate the usage of the function by printing a triangle with 5 rows
print_triangle(5)
