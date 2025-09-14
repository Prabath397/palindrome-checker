# Palindrome Checker

def is_palindrome(text):
    # Remove spaces and convert to lowercase
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

while True:
    print("\n--- Palindrome Checker ---")
    user_input = input("Enter a word, phrase, or number (or 'q' to quit): ")

    if user_input.lower() == 'q':
        print("👋 Exiting program. Bye!")
        break

    if is_palindrome(user_input):
        print(f"✅ '{user_input}' is a Palindrome!")
    else:
        print(f"❌ '{user_input}' is NOT a Palindrome.")
