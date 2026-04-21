import re
from utils import COMMON_PASSWORDS, SEQUENTIAL_PATTERNS

def check_password_strength(password):
    score = 0
    feedback = []

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        print("\n📊 Password Strength Result:")
        print(f"Password: {'*' * len(password)}")
        print("🔴 Strength: VERY WEAK")
        print("\n❌ This is a very common password — avoid it!")
        return

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ At least 8 characters required")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter (A-Z)")

    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (a-z)")

    # Number check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9)")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (!@#$...)")

    # Repeated characters check
    if re.search(r'(.)\1{2,}', password):
        feedback.append("⚠️  Avoid repeated characters (aaa, 111)")

    # Sequential pattern check
    for pattern in SEQUENTIAL_PATTERNS:
        if pattern in password.lower():
            feedback.append("⚠️  Avoid sequential patterns like 123 or abc")
            break

    # Result
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