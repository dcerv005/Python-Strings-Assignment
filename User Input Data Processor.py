#Question 2 Task 1 
def length_check(first_name, last_name):
    if len(first_name) < 2:
        return f"{first_name} is too short. Must be two characters or more"
    elif len(last_name) < 2:
        return f"{last_name} is too short. Must be two characters or more"
    return f"Hello {first_name} {last_name}!"
    
a = input("What is your first name? ")
b = input("What is your last name? ")

print(length_check(a,b))
#Task 2
def password(pass_word):
    if len(pass_word) < 8: 
        print("Password must be atleast eight characters long.")    
    for char in pass_word:
        if char.isupper():
            Uppercase = True
            break
        else:
            Uppercase = False
    if Uppercase == False:
        print("The password is missing an uppercase letter.")      
    
    for char in pass_word:
        if char.islower():
            Lowercase = True
            break
        else:
            Lowercase = False
    if Lowercase == False:
        print("The password is missing a lowercase letter.")
    
    for char in pass_word:
        if char.isdigit():
            Digit = True
            break
        else:
            Digit = False
    if Digit == False:
        print("The password is missing a digit.")

        
while True:
    user_password = input("Set your password. Must be eight characters long, must contain an uppercase, must contain a lowercase, and a number: ")
    password(user_password)
    user_continue= input("Do you want to set another password?(yes/no) ").lower()
    if user_continue != "yes":
        break

#Task 3
def email_config(email):
    new_email= email + '@example.com'  
    return new_email
email_list =[]
while True:

    user_email = input("Please provide the names to generate emails like this: firstname_lastname ")
    email_config(user_email)
    email_list.append(email_config(user_email))
    user_continue = input("Do you have more emails to generate? (yes/no) ").lower()
    if user_continue != 'yes':
        break
print(email_list)