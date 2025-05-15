# # Step 1: Custom Exception Class
# class UnderAgeError(Exception):
#     pass  # Hum kuch nahi likh rahe isme, sirf ek naam se custom exception banayi

# # Step 2: Function to check age
# def check_age(age):
#     if age < 18:
#         # Step 3: Raise custom exception
#         raise UnderAgeError("You must be at least 18 years old.")
#     else:
#         print("Access granted ✅")

# # Step 4: Try-Except block
# try:
#     user_age = int(input("Enter your age: "))
#     check_age(user_age)

# except UnderAgeError as e:
#     print(" Error:", e)



# Step 1: Custom Exception class
# class UserNameError(Exception):
#     pass

# # Step 2: Function to check username
# def check(name):
#     if name == "Varsha":
#         print("Good ✅")
#     else:
#         raise UserNameError("❌ Enter the right name!")

# # Step 3: Try-Except block
# try:
#     name = input("Enter your name: ")
#     check(name)
# except UserNameError as e:
#     print(e)

class UserName(Exception):
     pass
     
def check(name):
     if name == "Varsha":
        print("Good")
     else:
        raise UserName("Enter right name ")    
    
try:
    name = str(input("Enter your name "))
    check(name)
except UserName as e:
    print("Please try again")
    

