def generate_usernames():
    """Generate 200 usernames: carlos, wiener, carlos, wiener..."""
    usernames = []
    
    for i in range(200):
        if i % 2 == 0:  # Even index (0, 2, 4...) -> carlos
            usernames.append("carlos")
        else:           # Odd index (1, 3, 5...) -> wiener
            usernames.append("wiener")
    
    return usernames

# Generate and save
usernames = generate_usernames()

# Save to file
with open("usernames.txt", "w") as f:
    for username in usernames:
        f.write(f"{username}\n")

# Print preview (first 20)
print("Username list (200 items):")
print("-" * 40)
for i, username in enumerate(usernames[:20], 1):
    print(f"{i}. {username}")
print("... (200 total)")

# Print all for copying to Burp
print("\n" + "="*50)
print("COPY THIS INTO BURP SUITE INTRUDER:")
print("="*50)
for username in usernames:
    print(username)