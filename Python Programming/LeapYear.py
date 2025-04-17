# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a leap year.")
# else:
#     print(year, "not a leap year.")

# def isleapyear(year):
#     return ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

# year = int(input("Enter a year: "))
# if isleapyear(year):
#     print(year, "is a leap year.")
# else:
#     print(year, "not a leap year.")


#Print Leap Years in a given range
def leapyearrange(year):
    return ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))
    
    
year1 = int(input("Enter the 1st year: "))
year2 = int(input("Enter the 2nd year: "))
if year1 > year2:
    print("Invalid input.")
else:
    print("Leap Years: ")
    for year in range(year1, year2+1):
        flag = leapyearrange(year)
        if flag == True:
            print(year, end=" ")
            
            
#Print non Leap Years in a given range
def leapyearrange(year):
    return ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))
    
    
year1 = int(input("Enter the 1st year: "))
year2 = int(input("Enter the 2nd year: "))
if year1 > year2:
    print("Invalid input.")
else:
    print("Leap Years: ")
    for year in range(year1, year2+1):
        flag = leapyearrange(year)
        if flag == True:
            print(year, end=" ")

def leapyearrange(year):
    return ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))
    
    
year1 = int(input("Enter the 1st year: "))
year2 = int(input("Enter the 2nd year: "))
if year1 > year2:
    print("Invalid input.")
else:
    for i in range(year1, year2+1):
        flag = leapyearrange(i)
        if flag == True:
            print("Leap Years:")
            print(year, end=" ")
        elif flag == False:
            print("Non Leap Years:")
            print(year, end=" ")