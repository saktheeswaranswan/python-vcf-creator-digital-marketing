import csv

# Specify your CSV file here
csv_file = 'DATA3csv.csv'  # Replace with the path to your CSV file
vcf_file = 'rerecontacts.vcf'   # The name of the output VCF file

# Read CSV and extract data
names = []
phone_numbers = []

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)  # Read all rows into a list
    # Extract names (column B) and phone numbers (column C)
    for i in range(1, 10):  # Assuming we're processing the first 9 rows
        if len(rows) > i:  # Ensure there's enough rows in the CSV
            name = rows[i][1]  # Column B is index 1
            phone_number = rows[i][2]  # Column C is index 2
            names.append(name)
            phone_numbers.append(phone_number)

# Write to VCF file
with open(vcf_file, 'w') as vcf:
    for i in range(len(names)):
        vcf.write(f"BEGIN:VCARD\n")
        vcf.write(f"VERSION:3.0\n")
        vcf.write(f"N:{names[i]}\n")
        vcf.write(f"TEL:{phone_numbers[i]}\n")
        vcf.write(f"END:VCARD\n")

    print(f"VCF file '{vcf_file}' created successfully.")

