# Write a Python program that prints the first 10 odd numbers.

# Expected output: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19.

"""
Understand the Prompt:

- Print the first 10 odd numbers.
- I need a way to select the odd numbers, but not the even numbers.

- Inputs:
    - A number to iterate through. 
    
- Outputs:
    - The first 10 numbers from the iterated number. 
    
- What are my "tools"?
    - Function?
    - List to iterate through?
    - Control Flow
        - If statement?
    - Modulus?

Plan:
    - Use a for loop to iterate through a range of numbers.
    - Use the modulus operator to filter out odd numbers using a remainder of 1.
    - Print the numbers.

Execute:

Review:
"""
# Iteration 1
for num in range(1,21):
   if num % 2 == 1:
       print(num)
