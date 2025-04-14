import csv

def csv_to_single_vcf(csv_filename, output_filename='contacts7.vcf'):
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = list(csv.reader(csvfile))

    with open(output_filename, 'w', encoding='utf-8') as vcf_file:
        i = 0
        while i < len(reader):
            row = reader[i]
            if len(row) < 3:
                i += 1
                continue

            school = row[0].strip()   # School name goes to TEL
            name = row[1].strip()     # Person's full name
            phone1 = row[2].strip()   # Primary phone goes into EMAIL

            phone2 = ""
            if i + 1 < len(reader):
                next_row = reader[i + 1]
                if len(next_row) == 1 and next_row[0].strip().isdigit():
                    phone2 = next_row[0].strip()
                    i += 1  # Skip the next row as it's a secondary phone number

            if name and phone1:
                vcf_file.write(f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{school}
EMAIL:{phone1}
END:VCARD
""")

            if name and phone2:
                vcf_file.write(f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{school}
EMAIL:{phone2}
END:VCARD
""")

            i += 1

    print(f"✅ VCF file created: {output_filename}")

# Example usage
csv_to_single_vcf('DATA7csvcvcs.csv')

