# any number divisible by three is replaced by the word fizz 
# and any number divisible by five by the word buzz. 
# Numbers divisible by 15 i.e divisible by 3 and 5 
# become fizzbuzz

# using range function
for i in range(1, 16): # 16-1=15 (n-1)
    if (i % 3 == 0) and (i % 5 == 0):
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

# Passing input through a function

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        print("fizzbuzz")
    if input % 3 == 0:
        print("fizz")
    if input % 5 == 0:
        print("buzz")
    print("\n",input)

fizz_buzz(2)