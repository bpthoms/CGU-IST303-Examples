#Let's assign our list
days=['Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for day in days:
    if day == "Saturday":
        print("Yay! It's " + day + " and time to relax.")
    elif day == "Sunday":
        print("Yay! It's " + day + " funday!")
    else:
        print("No funday " + day + "!")
