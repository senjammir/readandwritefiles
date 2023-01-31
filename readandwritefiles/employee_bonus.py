# Write a program that reads the EmployeePay.csv file and prints out details of each employee

infile = open("EmployeePay.csv", "r")

for i in range(92):
    x = infile.readline()
    if i != 0:
        x = x.split(",")
        bonus = float(x[3]) * float(x[4])
        bonus = round(bonus, 2)
        print(
            f"Employee Name: {x[1]} {x[2]}\nEmployee Salary: ${x[3]}\nEmployee Bonus: ${bonus}\n"
        )
        user_input = input("Press ENTER to continue and type STOP to end program")
        if user_input == "STOP":
            break
