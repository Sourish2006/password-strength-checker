import getpass
from checker import check_password_strength

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