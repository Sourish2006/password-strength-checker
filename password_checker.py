import re
import getpass

def check_password_strength(password):
    score = 0
    feedback = []

    # 🔴 Common password check (early exit)
    common_passwords = ["password", "123456", "password123", "admin", "letmein", "qwerty"]
    if password.lower() in common_passwords:
        print("\n📊 Password Strength Result:")
        print(f"Password: {'*' * len(password)}")
        print("🔴 Strength: VERY WEAK")
        print("\n❌ This is a very common password — avoid it!")
        return

    # 🔹 Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ At least 8 characters required")

    # 🔹 Uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter (A-Z)")

    # 🔹 Lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (a-z)")

    # 🔹 Number
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9)")

    # 🔹 Special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (!@#$...)")

    # 🔹 Repeated characters
    if re.search(r'(.)\1{2,}', password):
        feedback.append("⚠️ Avoid repeated characters (aaa, 111)")

    # 🔹 Sequential patterns
    if "123" in password or "abc" in password:
        feedback.append("⚠️ Avoid sequential patterns like 123 or abc")

    # 🔹 Final Result
    print("\n📊 Password Strength Result:")
    print(f"Password: {'*' * len(password)}")
    print(f"Score: {score}/6")

    if score <= 2:
        print("🔴 Strength: WEAK")
    elif score <= 4:
        print("🟡 Strength: MODERATE")
    elif score <= 5:
        print("🟠 Strength: STRONG")
    else:
        print("🟢 Strength: VERY STRONG")

    if feedback:
        print("\n💡 Suggestions:")
        for tip in feedback:
            print(f"  {tip}")
    else:
        print("\n✅ Excellent! Your password is very strong.")


def main():
    print("=" * 50)
    print("     🔐 Advanced Password Strength Checker")
    print("=" * 50)
    print("⚠️  For educational purposes only.\n")

    while True:
        password = getpass.getpass("Enter a password to check (or type 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("Goodbye! Stay secure! 🔐")
            break

        check_password_strength(password)
        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    main()