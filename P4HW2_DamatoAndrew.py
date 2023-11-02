#Andrew D'Amato
#11/2/23

# Get employee name from user
Name = input("Enter employee's name: \n  ")
num_employees= 0

while Name != "Done":
    num_employees = num_employees + 1
    # Get number of hours from user
    Hours = int(input("Enter number of hours worked: \n  "))
    # Get pay rate per hour from user
    PayRate = float(input("Enter employee's pay rate: \n  "))
    # Determine if employee worked more than 40 hours
    if Hours > 40:
        # Calculate OT hours
        OTHours = Hours - 40
        # Calculate reg hours worked
        RegHours = Hours - OTHours
        # Calculate pay for reg hours
        RegPay = RegHours * PayRate
        # Calculate OT pay
        OTPay = OTHours * (PayRate * 1.5)
        ## Calculate gross pay
        GrossPay = RegPay + OTPay
        # Display name, payrate, reg hours. OT hours, OT pay, gross pay
        print("------------------------------------")
        print(f"Employee Name: {Name}\n")
        print("Hours Worked  |  Pay Rate  |  OverTime  |  OverTime Pay  |  RegHour Pay  |  Gross Pay")
        print("-------------------------------------------------------------------------------------------")
        print(f"   ,  {Hours}       |     {PayRate}    |     {OTHours}     |    ${OTPay}     |    ${RegPay}     |    ${GrossPay}")
        Name = input("Enter employee's name: \n  ")

print(f"The number of employees entered is {num_employees}")
