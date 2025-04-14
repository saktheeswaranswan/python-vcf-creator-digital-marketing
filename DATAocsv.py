import csv
import os

def csv_to_vcf(csv_filename, output_dir='vcf_files'):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the CSV file
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        
        # Process each row in the CSV
        for index, row in enumerate(reader):
            # Assuming the CSV has three columns: Name, Phone, Email
            if len(row) < 3:
                continue  # Skip rows with insufficient columns
            
            name = row[0].strip()  # First column: Name
            phone = row[1].strip()  # Second column: Phone
            email = row[2].strip() if len(row) > 2 else ''  # Third column: Email (optional)
            
            # Skip rows with missing name or phone
            if not name or not phone:
                continue

            # Create the VCF content
            vcf_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email if email else ''}
END:VCARD
"""
            # Define the VCF filename using an index (to avoid overwriting)
            vcf_filename = os.path.join(output_dir, f"contact_{index + 1}.vcf")
            
            # Write the VCF content to a file
            with open(vcf_filename, 'w', encoding='utf-8') as vcf_file:
                vcf_file.write(vcf_content)
                print(f"Created VCF for {name} at {vcf_filename}")

# Example usage with your CSV file
csv_to_vcf('DATAocsv.csv')

