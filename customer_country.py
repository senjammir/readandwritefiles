# Write a program that reads the file customers.csv and
# Produces a new file containing the customer name and country they are from

customer_infile = open("customers.csv", "r")
customer_outfile = open("customer_country.csv", "w")

for i in range(92):  # for loop to iterate over the 92 lines in the file
    x = customer_infile.readline()  # convert line into string
    x = x.split(",")  # convert string into list
    customer_outfile.write(
        f"{x[1]},{x[2]},{x[4]}\n"
    )  # write the desired fields into new file
customer_outfile.close()
