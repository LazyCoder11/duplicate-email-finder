import csv

emails = """
enteryouremail@gmail.com
"""

email_list = [e.strip() for e in emails.splitlines() if e.strip()]
unique_emails = list(set(email_list))
duplicates_count = len(email_list) - len(unique_emails)

# Print counts
print(f"Total emails: {len(email_list)}")
print(f"Unique emails: {len(unique_emails)}")
print(f"Duplicate emails: {duplicates_count}")

# Save unique emails into a CSV file
with open("unique_emails.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Email"])  # Header
    for email in sorted(unique_emails):  # Sort for readability
        writer.writerow([email])

print("✅ Unique emails saved to unique_emails.csv")