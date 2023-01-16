dayOfWeek = "Thursday"

if dayOfWeek == "Monday":
    print("It's Monday..")
elif dayOfWeek == "Tuesday":
    print("it's Tuesday..")
elif dayOfWeek == "Wednesday":
    print("It's Wednesday..")

# Switch cases are used when you have a finite amount of options for an if else 

fruit = input("Whats your fav fruit: ")

# What variable am I checking 
match fruit: 
    # What result of named variable am I expecting 
    case "mango":
        print("Good choice!")
    case "kiwi":
        print("Make sure you eat with the skin on")
    case "apple":
        print("Solid choice")
    case _: 
        print("This is the default")