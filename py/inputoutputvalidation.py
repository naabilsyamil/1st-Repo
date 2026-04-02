name = input("Enter your name:")
height = float(input("Enter Your Height:"))  # convert to float

# Input Validation
while True:
    try:
        age = int(input("Enter Your Age:"))
        if age > 0 :
            break
        else:
            print("Age Must Be Positive!")
    except ValueError:
        print("Please Enter A Valid Number!")

#Output Validation
print(f"Hello,{name}!") 
print(f"You Are {age} Years Old and {height} Metres Tall")       
