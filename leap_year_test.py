# year = int(input("enter a year!"))

# if year % 4 ==0 :
#     if year % 100 ==0:
#         if year % 400 ==0:
#             print(f"{year} is leap year ")
#         else:
#           print(f"{year} is not leap year ")  
#     # else:
#     #    print(f"{year} is not leap year ") 

#     print(f"{year} is leap year ") 
# else:
#    print(f"{year} is not leap year ")  
        
# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

# # Input from the user
# year = int(input("Enter a year: "))

# # Check if the year is a leap year
# if is_leap_year(year):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
#------------------------------------------------
#year = int(input("Which year do you want to check?\n"))
 
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")
#-------------------
start_year = int(input("Enter a year: "))
end_year = int(input("Enter a year: "))
if end_year < start_year:
    print("invalid entry")
leap = []
for year in range(int(start_year), int(end_year)):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
                leap.append(year)
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
            leap.append(year)
    else:
        print("Not leap year.")
print(leap)

