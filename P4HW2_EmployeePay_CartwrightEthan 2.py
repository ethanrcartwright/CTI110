def overtimeCalc(hours):
  hours = hours - 40
  if hours > 0:
    return hours 
  else:
    return 0 

def employeePay(overtimeHours, hourlyWage, hoursWorked):
  if overtimeHours > 0:
    regularHour = hoursWorked - overtimeHours
    regularPay = regularHour * hourlyWage
    return regularPay
  else:
    regularPay = hourlyWage * hoursWorked
    return regularPay

def grossPay(overtimePay, regularPay):
  grossPay = overtimePay + regularPay
  return grossPay




  
  

def main():
  employeeName = input("Enter name of Employee: ")
  hoursWorked = float(input("Enter Hours Worked: "))
  hourlyWage = float(input("Enter Hourly Wage: "))


  print()
  print("Employee Name:  ", employeeName)
  print("-" * 30)
  print()
  print("Hours Worked:" , hoursWorked)
  print("Pay Rate:  ", hourlyWage)
  #overtimeCalc function.


  #used to calc if employee has overtime hours. 
  hours = hoursWorked
  overtimeHours = overtimeCalc(hours)


  #print overtime hours and calc overtime pay
  print("Overtime Hours: ", overtimeCalc(hours))
  overtimePay = (overtimeHours * hourlyWage)*1.5
  print("Overtime Wage: ", overtimePay)
  #regular employee pay 
  regularPay = employeePay(overtimeHours, hourlyWage, hoursWorked)
  print("Regular Pay:  ", regularPay)
  #print grossPay
  print("Gross Pay:  ", grossPay(overtimePay, regularPay))
  print()
  print("To enter another employee, type 'Another'. If you wish to leave the program, type 'Done.'.")
  
  #Loopstarts here
  loopstarter = input("")
  
  while loopstarter != 'Done.':
    #asking 
    employeeName = input("Enter name of Employee: ")
    hoursWorked = float(input("Enter Hours Worked: "))
    hourlyWage = float(input("Enter Hourly Wage: "))

    print()
    print("Employee Name:  ", employeeName)
    print("-" * 30)
    print()
    print("Hours Worked:" , hoursWorked)
    print("Pay Rate:  ", hourlyWage)

    hours = hoursWorked
    overtimeHours = overtimeCalc(hours)

    print("Overtime Hours: ", overtimeCalc(hours))
    overtimePay = (overtimeHours * hourlyWage)*1.5
    print("Overtime Wage: ", overtimePay)
    #regular employee pay 
    regularPay = employeePay(overtimeHours, hourlyWage, hoursWorked)
    print("Regular Pay:  ", regularPay)
    #print grossPay
    print("Gross Pay:  ", grossPay(overtimePay, regularPay))

    print("To enter another employee, type 'Another'. If you wish to leave the program, type 'Done.'.")

    


  
main() 








  

























