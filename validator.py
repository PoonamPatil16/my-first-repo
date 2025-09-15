import re

def check_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_file(file_path):
    invalid = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        email = line.strip()
        if not check_email(email):
            invalid.append((i, email))
    return invalid

if __name__ == "__main__":
    # Example usage
    file = "emails.txt"
    result = validate_file(file)
    if result:
        for line_no, email in result:
            print(f"Invalid email at line {line_no}: {email}")
    else:
        print("All emails valid!")
