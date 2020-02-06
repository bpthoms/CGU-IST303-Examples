days=['Sunday', 'Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday']

#Let's build our function what_day
def what_day(day):
    return days[day]

#Let's initialize our user input
user_input=1
while user_input > 0:
    #let's grab our user input
    user_input = input("Enter a numeric day of the week as (1, 2, 3, 4, 5, 6, 7) --> ")
    if user_input > 0 and user_input < 8:
         print("That day of the week is " + what_day(user_input-1) )
    else:
        print("Thanks for coming.")
        break
