import re

# Load your input (replace with actual file read if needed)
with open("numbered_contacts.vcf", "r", encoding="utf-8") as file:
    vcard_data = file.read()

# Replace (EMAIL:) with EMAIL:
cleaned_data = re.sub(r'\(EMAIL:\)', 'EMAIL:', vcard_data)

# Save to a new file (or overwrite the original if you prefer)
with open("cleaned_contacts.vcf", "w", encoding="utf-8") as file:
    file.write(cleaned_data)

print("Brackets removed from EMAIL fields successfully.")




