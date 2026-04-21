#The match statement is used to perform different actions based on different conditions.
#Instead of writing many if..else statements, you can use the match statement.
#The match statement selects one of many code blocks to be executed.

day = 3
match day :
        case 1 :
                print("Monday")
        case 2 :
                print("Tuesday")
        case 3 :
                print("wednesday")
        case 4 :
                print("Thursday")
        case 5 :
                print("friday")
        case 6 : 
                print("Saturday")
        case 7 :
                print("Sunday")

day = 3
match day :
        case 4 : print("thursday")
        case 5 : print("friday")
        case _ : print("looking forward to the weeknd!")

#Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches.
#The value _ will always match, so it is important to place it as the last case to make it behave as a default case.

#pipe character as or for multiple cases
day = 3
match day :
        case 1|2|3|4|5|6 :
                print("Today is a weekday.")
        case _ :
                print("today is weeknd")

#using if statements : You can add if statements in the case evaluation as an extra condition-check.
month = 3
day = 5
match day :
        case 1|2|3|4|5|6 if month == 3 :
                print("A weekday in March")
        case 1|2|3|4|5|6 if month == 4 :
                print("A weekday in April")