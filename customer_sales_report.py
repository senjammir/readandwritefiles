# Write a program that reads the sales.csv file and
# Creates a new file with the customer ID and calculated total

infile = open("sales.csv", "r")
outfile = open("salesreport.csv", "w")
outfile.write("CutomerID | Total Amount\n")

for i in range(80):
    x = infile.readline()
    if i != 0:
        x = x.split(",")
        total = float(x[3]) + float(x[4]) + float(x[5])
        total = round(total, 2)
        outfile.write(f"{x[0]}\t\t\t${total}\n")
outfile.close()
