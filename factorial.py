# Recursive function to find factorial of a number
def factorial(n):
  if n==1:
    return 1
  else:
    return n*factorial(n-1)

# main function
if __name__ == '__main__':
  num=int(input("Enter a number: "))
  if num<0:
    print("Factorial does not exist for negative numbers")
  elif num==0:
    print("Factorial of 0 is 1")
  else:
    print(f"Factorial of {num} is {factorial(num)}")
