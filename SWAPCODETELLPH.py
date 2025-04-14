def swap_tel_email(vcard_text):
    swapped_vcards = []
    vcards = vcard_text.strip().split("BEGIN:VCARD")
    for vcard in vcards:
        if not vcard.strip():
            continue
        vcard = "BEGIN:VCARD" + vcard  # Re-add the header
        lines = vcard.strip().splitlines()
        new_lines = []
        tel_value = ""
        email_value = ""
        for line in lines:
            if line.startswith("TEL:"):
                tel_value = line.split("TEL:")[1].strip()
            elif line.startswith("EMAIL:"):
                email_value = line.split("EMAIL:")[1].strip()
        
        for line in lines:
            if line.startswith("TEL:"):
                new_lines.append(f"TEL:{email_value}")
            elif line.startswith("EMAIL:"):
                new_lines.append(f"EMAIL:{tel_value}")
            else:
                new_lines.append(line)
        swapped_vcards.append("\n".join(new_lines))
    return "\n".join(swapped_vcards)


# Input VCARD text
input_vcards = """BEGIN:VCARD
VERSION:3.0
FN:new MAHALAXMI P
TEL:SUBBIAH VIDYALAYAM GIRLS HSS
EMAIL:9751068263
END:VCARD
BEGIN:VCARD
VERSION:3.0
FN:new RAMALAKSHMI K
TEL:SUBBIAH VIDYALAYAM GIRLS HSS
EMAIL:9688925311
END:VCARD"""

# Swap and print result
output_vcards = swap_tel_email(input_vcards)
print(output_vcards)

