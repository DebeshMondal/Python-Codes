# temp = 30

# if temp >= 30:
#     print("Its hot")
# else:
#     print("It's cold.")


name = input("Enter name:  ")

print("Curent charc in your name",len(name))


if len(name) < 3:
    print("Name must be atleast 3 characters")
elif len(name) > 50:
    print("Name must be max of 50 characters")
else:
    print("Your Name is valid.")