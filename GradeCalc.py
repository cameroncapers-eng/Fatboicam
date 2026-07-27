name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your grade in the class?")
print(f"Your grade is {fav1}")

number = int(fav1)
if number >= 95:
    print("A")
elif number >= 86:
    print("B")
elif number >= 78:
    print("C")
elif number >= 62:
    print("D")      
else:
    print("F")