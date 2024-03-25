#Question 3
#Task 1
user_input= input("Hello! What is your query? ").lower()

def filter_words(user_input):
    predefined_commands= ["help", "issue", "contact support"]
    for word in user_input.split():
    
        if word in predefined_commands:
            if word == "help":
                print("How can we help?")
            elif word == "issue":#Task 2
                user_issue=input("Can you explain the issue further?")
                keywords = ["login", "performance", "error"]
                for issue in user_issue.split():
                    if issue.lower() in keywords:
                        print(f"The category is: {issue}")
                
            elif word == "contact support":
                print("Can you describe the reason you need contact support so we can direct your call appropriately.")
            else:
                pass


filter_words(user_input)