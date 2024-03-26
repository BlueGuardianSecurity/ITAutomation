#used this to look for common entries in two csv files and write to new csv with all common columns
import pandas as pd

def extract_emails_from_excel(file_path, email_column):
    """
    Extracts emails from a given column in an Excel file.
    :param file_path: Path to the Excel file.
    :param email_column: The name of the column containing email addresses.
    :return: A set of email addresses.
    """
    try:
        df = pd.read_excel(file_path)
        return set(df[email_column].dropna().unique())
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return set()

def main():
    file_path1 = 'C:\pathtofile1.xlsx'
    file_path2 = 'C:\pathtofile2.xlsx'
    email_column = 'Email'

    emails_file1 = extract_emails_from_excel(file_path1, email_column)
    emails_file2 = extract_emails_from_excel(file_path2, email_column)

    common_emails = emails_file1.intersection(emails_file2)
    unique_emails = (emails_file1.union(emails_file2)) - common_emails
    
    print("Common Emails:")
    for email in common_emails:
        print(email)

    print("\nUnique Emails:")
    for email in unique_emails:
        print(email)

    with open ('Phone_Output1.txt', 'w') as file:
        file.write("Common Emails:\n")
        for email in common_emails:
            file.write(email + '\n')

        file.write("\nUnique Emails:\n")
        for email in unique_emails:
            file.write(email + '\n')

if __name__ == "__main__":
    main()
