import csv
import os

def csv_to_single_vcf(csv_filename, output_filename='contacts.vcf'):
    # Open the CSV file
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        
        # Start the VCF file
        with open(output_filename, 'w', encoding='utf-8') as vcf_file:
            # Write the beginning of the VCF file
            for row in reader:
                # Assuming the CSV has three columns: Name, Phone, and Email
                if len(row) < 3:
                    continue  # Skip rows with insufficient columns
                
                name = row[0].strip()  # First column: Name
                phone = row[1].strip()  # Second column: Phone
                email = row[2].strip() if len(row) > 2 else ''  # Third column: Email (optional)

                # Skip rows with missing name or phone
                if not name or not phone:
                    continue

                # Write each contact to the VCF file
                vcf_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email if email else ''}
END:VCARD
"""
                vcf_file.write(vcf_content)

            print(f"Created a single VCF file: {output_filename}")

# Example usage with your CSV file
csv_to_single_vcf('DATAocsv.csv')

