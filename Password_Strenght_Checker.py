import re
import hashlib

try:
    import requests  # Ensure requests is available
except ImportError:
    requests = None
    print("⚠️ The 'requests' library is not installed. HIBP checks will be skipped.")

# Function to check password strength based on common rules
while True:
    def check_password_strength(password):
        strength = {
            "length": len(password) >= 12,  # At least 12 characters long
            "uppercase": bool(re.search(r"[A-Z]", password)),  # Contains uppercase
            "lowercase": bool(re.search(r"[a-z]", password)),  # Contains lowercase
            "digits": bool(re.search(r"[0-9]", password)),  # Contains digits
            "special": bool(re.search(r"[^A-Za-z0-9]", password)),  # Contains special chars
        }

        # Calculate score based on how many rules are satisfied
        score = sum(strength.values())
        if score == 5:
            verdict = "Strong"
        elif 3 <= score < 5:
            verdict = "Moderate"
        else:
            verdict = "Weak"

        return verdict, strength

    # Function to check if a password has been leaked in breaches using HaveIBeenPwned API
    def check_hibp(password):
        if requests is None:
            return "HIBP check skipped (requests not installed)."

        sha1_pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix, suffix = sha1_pass[:5], sha1_pass[5:]  # Use k-anonymity model

        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url)
        if response.status_code != 200:
            return "Error checking HIBP API"

        hashes = (line.split(":") for line in response.text.splitlines())
        for hash_suffix, count in hashes:
            if hash_suffix == suffix:
                return f"⚠️ Password found in breaches {count} times!"

        return "✅ Password not found in known breaches."

    # Main runner for interactive input
    def main():
        password = input("Enter a password to check: ")

        verdict, details = check_password_strength(password)
        print(f"\nPassword Strength: {verdict}")
        print("Details:")
        for rule, passed in details.items():
            print(f" - {rule.capitalize()}: {'✔️' if passed else '❌'}")

        print("\nChecking HaveIBeenPwned...")
        hibp_result = check_hibp(password)
        print(hibp_result)

    if __name__ == "__main__":
        main()