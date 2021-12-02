#p3T1
#Pass Or Fail
#Ethan Cartwright

userGrade = int(input("Please Enter a Grade between 0 and 100:  "))

if userGrade < 0:
  print(" Entered grade is not valid. It must be between 0 and 100. Try Again...")
  userGrade = int(input("Please Enter a Grade between 0-100: "))

if userGrade > 100:
  print("Entered grade is not valid. it must be between 0 and 100. ")
  userGrade = int(input("Please Enter a Grade between 0-100: "))

if userGrade >= 60:
  print(userGrade , "is a passing grade.")
else:
  print(userGrade , " is not a passing grade.")




    

