# Basic-Web-Application-Firewall-WAF
# **Web Application Firewall (WAF) - Complete Guide
## Building and Deploying a WAF using Python & Flask

---

## **📌 1. Project Overview**
### **Objective**
This project aims to create a **Web Application Firewall (WAF)** that monitors and filters **HTTP requests** to protect a web application from common web attacks like:
- **SQL Injection**
- **Cross-Site Scripting (XSS)**
- **IP Blocking**
- **Rate Limiting**

### **Technologies Used**
- **Programming Language**: Python
- **Framework**: Flask
- **Libraries**: Regular Expressions (Regex), Flask-Limiter (for rate limiting)
- **Deployment Options**: Heroku, AWS, or a local server

---

## **📌 2. Setting Up the Development Environment**
### **Step 1: Install Required Software**
#### ✅ Install Python (If not installed)
1. Check if Python is installed:
   ```bash
   python --version
   ```
   OR  
   ```bash
   python3 --version
   ```
2. If Python is not installed, download it from:
   👉 [Python Official Website](https://www.python.org/downloads/)

#### ✅ Install Git (For Deployment)
1. Check if Git is installed:
   ```bash
   git --version
   ```
2. If Git is not installed, download it from:
   👉 [Git Official Website](https://git-scm.com/downloads)

#### ✅ Install Heroku CLI (Optional for Deployment)
1. Check if Heroku CLI is installed:
   ```bash
   heroku --version
   ```
2. If not installed, download it from:
   👉 [Heroku CLI Download](https://devcenter.heroku.com/articles/heroku-cli)

---

## **📌 3. Creating the WAF Project**
### **Step 2: Create a Project Directory**
1. Open **Command Prompt (CMD) / Terminal** and create a project folder:
   ```bash
   mkdir web_app_firewall
   cd web_app_firewall
   ```

### **Step 3: Set Up a Virtual Environment**
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

### **Step 4: Install Required Python Packages**
1. Install Flask and dependencies:
   ```bash
   pip install Flask flask-limiter gunicorn
   ```

---

## **📌 4. Creating the Web Application**
### **Step 5: Create `app.py`**
1. Inside the **web_app_firewall** folder, create a new file named **app.py** and add:

```python
from flask import Flask, request, abort
from waf import detect_sql_injection, detect_xss, block_ip
from flask_limiter import Limiter

app = Flask(__name__)
limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.before_request
def check_security():
    user_ip = request.remote_addr

    if block_ip(user_ip):
        abort(403, description="Your IP is blocked.")

    for key in request.form.keys():
        if detect_sql_injection(request.form[key]):
            abort(400, description="SQL Injection detected.")
        if detect_xss(request.form[key]):
            abort(400, description="XSS detected.")

@app.route('/')
def home():
    return "Welcome to the Web App!"

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('user_input')
    return f"You entered: {user_input}"

if __name__ == '__main__':
    app.run(debug=True)
```

---

### **Step 6: Create `waf.py` (WAF Logic)**
1. Inside the **web_app_firewall** folder, create **waf.py** and add:

```python
import re

SQL_INJECTION_PATTERN = r"(\bselect\b|\binsert\b|\bunion\b|\b--\b|\b;\b|\bdrop\b)"
XSS_PATTERN = r"<script.*?>.*?</script>"
BLOCKED_IPS = ["192.168.0.1"]

def detect_sql_injection(input_data):
    return bool(re.search(SQL_INJECTION_PATTERN, input_data, re.IGNORECASE))

def detect_xss(input_data):
    return bool(re.search(XSS_PATTERN, input_data, re.IGNORECASE))

def block_ip(ip):
    return ip in BLOCKED_IPS
```

---

## **📌 5. Running & Testing the WAF**
### **Step 7: Run the Web Application**
1. Start the Flask application:
   ```bash
   python app.py
   ```
2. Open the web browser and go to:
   **http://127.0.0.1:5000/**

### **Step 8: Test SQL Injection & XSS**
1. Use **cURL** or **Postman** to send requests:
   ```bash
   curl -X POST -d "user_input=' OR 1=1 --" http://127.0.0.1:5000/submit
   ```
   **Expected Output:** `400 Bad Request: SQL Injection detected`

2. Test XSS:
   ```bash
   curl -X POST -d "user_input=<script>alert('XSS')</script>" http://127.0.0.1:5000/submit
   ```
   **Expected Output:** `400 Bad Request: XSS detected`

---

## **📌 6. Deploying to GitHub**
### **Step 9: Initialize Git Repository**
1. Run the following commands:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

### **Step 10: Create a GitHub Repository**
1. Go to **GitHub** and create a new repository.
2. Copy the repository URL.

### **Step 11: Push Code to GitHub**
1. Link the local repository to GitHub:
   ```bash
   git remote add origin <repository-url>
   ```
2. Push the code:
   ```bash
   git push -u origin main
   ```

---

## **📌 7. Deploying to Heroku**
### **Step 12: Create a Procfile**
1. Inside the **web_app_firewall** folder, create a file named **Procfile** (without extension) and add:
   ```
   web: gunicorn app:app
   ```

### **Step 13: Deploy to Heroku**
1. Login to Heroku:
   ```bash
   heroku login
   ```
2. Create a Heroku app:
   ```bash
   heroku create my-waf-app
   ```
3. Deploy the code:
   ```bash
   git push heroku main
   ```

---

## **📌 8. Troubleshooting & Error Solutions**
|                  Error                         |           Cause          |                         Solution                                            |
|------------------------------------------------|--------------------------|-----------------------------------------------------------------------------|
| `python: command not found`                    | Python not installed     | Install Python from [python.org](https://www.python.org/downloads/)         |
| `ModuleNotFoundError: No module named 'flask'` | Flask not installed      | Run `pip install Flask`                                                     |
| `git: command not found`                       | Git not installed        | Install from [git-scm.com](https://git-scm.com/downloads)                   |
| `heroku: command not found`                    | Heroku CLI not installed | Install from [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) |
| `fatal: not a git repository`                  | Git not initialized      | Run `git init` in project folder                                            |

---

## **✅ Conclusion**
You have successfully built and deployed a **basic Web Application Firewall (WAF)** that protects web applications from SQL Injection and XSS attacks. 🚀  

If you need further help, feel free to ask! 🎯
