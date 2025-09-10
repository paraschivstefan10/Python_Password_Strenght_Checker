# Python_Password_Strenght_Checker
A simple Python tool to check the strength of a password.

## ✨ Features
- Checks password strength based on:
  - Length (≥ 12 characters recommended)
  - Uppercase, lowercase letters
  - Digits
  - Special characters
- Classifies passwords as **Weak**, **Moderate**, or **Strong**
- (Bonus) Integrates with Have I Been Pwned (HIBP) to see if the password has been leaked in real-world breaches
- Clear output with pass/fail indicators ✔️ ❌

---

## 📦 Requirements
- Python 3.9+ (works with Python 3.13 too)
- `requests` library for the HIBP integration

Install dependencies with:
```bash
pip install requests
