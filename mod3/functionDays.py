days={'second':'Monday','third':'Tuesday','fourth':'Wednesday', 'fifth':'Thursday', 'sixth':'Friday', 'seventh':'Saturday','first':'Sunday'}

#Let's build our function what_day
def what_day(day):
    return days[day]

print("The first day of the week is " + what_day('first'))
