import re

print("=" * 50)
print("EMAIL EXTRACTOR AUTOMATION")
print("=" * 50)

try:
    with open("sample.txt", "r") as file:
        content = file.read()

    emails = re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        content
    )

    with open("extracted_emails.txt", "w") as file:
        for email in emails:
            file.write(email + "\n")

    print("\nEmails Found:")
    print("-" * 30)

    for i, email in enumerate(emails, start=1):
        print(f"{i}. {email}")

    print("\nTotal Emails Found:", len(emails))
    print("Results saved to extracted_emails.txt")

except FileNotFoundError:
    print("sample.txt not found!")