def remove_email_and_keep_tel(input_file, output_file=None):
    # Read the original vcf file
    with open(input_file, 'r', encoding='utf-8') as file:
        vcard_text = file.read()

    # Split and process VCARDs
    cleaned_vcards = []
    vcards = vcard_text.strip().split("BEGIN:VCARD")
    
    for vcard in vcards:
        if not vcard.strip():
            continue
        vcard = "BEGIN:VCARD" + vcard  # Re-add the header
        lines = vcard.strip().splitlines()
        new_lines = []

        # Remove EMAIL line and keep TEL line
        for line in lines:
            if line.startswith("EMAIL:"):
                continue  # Skip this line
            new_lines.append(line)
        
        cleaned_vcards.append("\n".join(new_lines))

    # Join all VCARDs
    final_text = "\n".join(cleaned_vcards)

    # Write to output (overwrite or new file)
    output_path = output_file if output_file else input_file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(final_text)

    print(f"VCARDs with EMAIL removed written to: {output_path}")


# Call the function
remove_email_and_keep_tel('cleaned_contacts3.vcf')  # Overwrites original
# remove_email_and_keep_tel('cleaned_contacts3.vcf', 'cleaned_no_email.vcf')  # For new file

