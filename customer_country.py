# Write a program that reads the file customers.csv and
# Produces a new file containing the customer name and country they are from

customer_infile = open("customers.csv", "r")
customer_outfile = open("customer_country.csv", "w")
customer_outfile.write("Customer Name, Country\n")
count = 0
for i in customer_infile.readlines()[1:]:
    x = i.split(",")
    customer_outfile.write(f"{x[2]} {x[1]}, {x[4]}\n")
    count += 1

print("Total number of customers:", count)

customer_outfile.close()
