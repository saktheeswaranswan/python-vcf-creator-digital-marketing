# Read the vCard file
with open("contacts3.vcf", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Initialize counter
fn_count = 1
updated_lines = []

# Process each line
for line in lines:
    if line.startswith("FN:"):
        # Extract the name after "FN:"
        name = line[3:].strip()
        # Format it with numbering
        new_line = f"FN: {fn_count} {name}\n"
        updated_lines.append(new_line)
        fn_count += 1
    else:
        updated_lines.append(line)

# Write to a new file
with open("numbered_contacts.vcf", "w", encoding="utf-8") as file:
    file.writelines(updated_lines)

print("FN lines updated with numbering correctly.")

