import random
import string

def generate_password(length=12):
    """Generate a random password of specified length."""
    if length < 6:
        raise ValueError("Password length should be at least 6 characters.")
    
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Ensure at least one of each type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest randomly
    all_chars = lower + upper + digits + symbols
    password += random.choices(all_chars, k=length - 4)
    
    # Shuffle the password for randomness
    random.shuffle(password)
    
    return ''.join(password)

def check_password_strength(password):
    """Check the strength of a given password."""
    criteria = {
        "length ≥8": len(password) >= 8,
        "has uppercase": any(c.isupper() for c in password),
        "has lowercase": any(c.islower() for c in password),
        "has digit": any(c.isdigit() for c in password),
        "has symbol": any(c in string.punctuation for c in password),
    }
    
    score = sum(criteria.values())
    
    if score <= 2:
        strength = "Weak ❌"
    elif score == 3:
        strength = "Moderate ⚠️"
    else:
        strength = "Strong ✅"
    
    print("\n--- Password Analysis ---")
    for key, met in criteria.items():
        print(f"{key}: {'✔' if met else '✘'}")
    
    return strength

def main():
    print("=== Password Tools ===")
    print("1. Generate Password")
    print("2. Check Password Strength")
    choice = input("Choose (1/2): ")

    if choice == "1":
        try:
            length = int(input("Enter password length (min 6): ") or 12)
            password = generate_password(length)
            print(f"\nGenerated Password: {password}")
            print(f"Strength: {check_password_strength(password)}")
        except ValueError:
            print("Error: Please enter a valid number.")
    
    elif choice == "2":
        password = input("Enter password to check: ").strip()
        print(f"\nStrength: {check_password_strength(password)}")
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()

