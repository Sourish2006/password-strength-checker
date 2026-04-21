# 🔐 Advanced Password Strength Checker

> A command-line tool built in Python that analyzes password strength and provides actionable feedback to improve security.

![Language](https://img.shields.io/badge/Language-Python-blue)
![Field](https://img.shields.io/badge/Field-Cybersecurity-red)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 🎯 Overview

Weak passwords are one of the most common causes of security breaches.  
This tool evaluates password strength based on multiple criteria and provides a detailed report along with suggestions to make passwords more secure.

---

## 🛠️ Features

- 🔴 Detects commonly used passwords instantly
- 📏 Checks password length (8+ and 12+ characters)
- 🔠 Validates uppercase and lowercase letters
- 🔢 Ensures inclusion of numbers
- 🔣 Checks for special characters
- 🔁 Detects repeated characters (e.g., aaa, 111)
- 🔗 Detects sequential patterns (e.g., 123, abc, qwerty)
- 👁️ Secure input (password hidden using `getpass`)
- 💡 Provides actionable suggestions to improve password strength

---

## 📁 Project Structure
password_checker/
├── main.py          → Entry point, user interaction
├── checker.py       → Core password analysis logic
├── utils.py         → Common passwords & pattern lists
├── requirements.txt → Dependencies (all built-in)
└── README.md        → Project documentation

---

---

## 💻 How to Run

```bash
python main.py
```

Then enter any password to check:

---

## 📌 Sample Output

**Strong Password:**
```
📊 Password Strength Result:
Password: **************
Score: 6/6
🟢 Strength: VERY STRONG
✅ Excellent! Your password is very strong.
```

**Weak Password:**
```
📊 Password Strength Result:
Password: ********
Score: 2/6
🔴 Strength: WEAK

💡 Suggestions:
  ❌ Add at least one uppercase letter (A-Z)
  ❌ Add at least one special character (!@#$...)
  ⚠️  Avoid sequential patterns like 123 or abc
```
## 🧠 Concepts Used

| Concept | Details |
|---|---|
| Language | Python 3 |
| Pattern Matching | Regular Expressions (re) |
| Secure Input | getpass module |
| Architecture | Modular (multi-file structure) |
| Security | Common password detection |

---

## 📚 What I Learned

- How attackers exploit weak passwords
- Regular expressions for pattern matching
- Secure input handling with getpass
- Modular code structure in Python
- Real-world password security standards

---

## ⚠️ Disclaimer
This tool is for **educational purposes only**.

---

## 🧑‍💻 Author
**Sourish Giri** — BSc IT (Cyber Security) Student
[GitHub](https://github.com/Sourish2006) | [LinkedIn](https://www.linkedin.com/in/sourish-giri)