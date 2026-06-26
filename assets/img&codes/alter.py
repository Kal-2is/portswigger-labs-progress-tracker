import sys
if len(sys.argv)<3:
    print("Usage: python3 alter.py <filename> <word to make between>")
    sys.exit(1)
input_file=sys.argv[1]
tmp=sys.argv[2]
def alter_password_list(input_file,tmp, output_file):
   
    # Read your passwords
    with open(input_file, 'r') as f:
        passwords = [line.strip() for line in f if line.strip()]
    
    # Create new list with "peter" inserted between each
    altered_passwords = []
    for pwd in passwords:
        altered_passwords.append(pwd)
        altered_passwords.append(tmp)
    
    # Save to file
    with open(output_file, 'w') as f:
        for pwd in altered_passwords:
            f.write(f"{pwd}\n")
    
    print(f"[+] Original passwords: {len(passwords)}")
    print(f"[+] Altered passwords: {len(altered_passwords)}")
    print(f"[+] Saved to: {output_file}")
    
    
    print("\nPreview (first 10):")
    for i, pwd in enumerate(altered_passwords[:10], 1):
        print(f"{i}. {pwd}")

# Usage
alter_password_list(input_file,tmp, "alteredlist.txt")