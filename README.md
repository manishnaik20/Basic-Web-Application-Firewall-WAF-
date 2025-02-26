# **Web Application Firewall (WAF) - README**  

## **📌 Project Description**  
This project is a **Web Application Firewall (WAF)** built using **Python and Flask** to protect web applications from common cyber threats like **SQL Injection, Cross-Site Scripting (XSS), IP Blocking, and Rate Limiting**.  

The WAF monitors incoming HTTP requests and applies security rules before processing them, ensuring the web application remains secure against malicious attacks.  

---

## **📌 Features**
- **SQL Injection Detection**: Blocks malicious SQL queries in user input.  
- **Cross-Site Scripting (XSS) Protection**: Prevents injection of harmful JavaScript code.  
- **IP Blocking**: Restricts access from specific blocked IP addresses.  
- **Rate Limiting**: Limits the number of requests to prevent abuse.  
- **Logging & Monitoring**: Keeps logs of blocked requests for security analysis.  

---

## **📌 Technologies Used**
- **Programming Language**: Python  
- **Web Framework**: Flask  
- **Security Techniques**: Regex for threat detection, IP blocking, and rate limiting  
- **Deployment Options**: GitHub, Heroku (optional), or any cloud platform  

---

## **📌 How It Works**
1. The WAF intercepts incoming HTTP requests before they reach the web application.  
2. It scans user inputs for **SQL Injection and XSS patterns** using **regular expressions**.  
3. Requests from **blocked IP addresses** are denied automatically.  
4. **Rate limiting** is enforced to prevent excessive requests from a single user.  
5. If a request is identified as **malicious**, the server responds with a **400 Bad Request** or **403 Forbidden** message.  
6. If no threats are detected, the request is processed normally.  

---

## **📌 Setup & Installation**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/web-app-firewall.git
cd web-app-firewall
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate      # For Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Application**
```bash
python app.py
```

Access the application in your browser at:  
👉 **http://127.0.0.1:5000/**  

---

## **📌 API Endpoints**
| **Method** | **Endpoint** | **Description** |
|------------|------------|----------------|
| `GET`  | `/`  | Home page |
| `POST` | `/submit` | Processes user input & applies WAF rules |

---

## **📌 Testing the WAF**
### **1️⃣ Test SQL Injection**
```bash
curl -X POST -d "user_input=' OR 1=1 --" http://127.0.0.1:5000/submit
```
**Expected Output:** `400 Bad Request: SQL Injection detected`

### **2️⃣ Test XSS Attack**
```bash
curl -X POST -d "user_input=<script>alert('XSS')</script>" http://127.0.0.1:5000/submit
```
**Expected Output:** `400 Bad Request: XSS detected`

---

## **📌 Deployment to Heroku**
### **1️⃣ Initialize Git Repository**
```bash
git init
git add .
git commit -m "Initial commit"
```

### **2️⃣ Create a Heroku App**
```bash
heroku login
heroku create my-waf-app
```

### **3️⃣ Deploy the App**
```bash
git push heroku main
```

---

## **📌 Troubleshooting**
| **Error** | **Solution** |
|------------|-------------|
| `ModuleNotFoundError: No module named 'flask'` | Run `pip install Flask` |
| `git: command not found` | Install Git from [git-scm.com](https://git-scm.com/downloads) |
| `heroku: command not found` | Install Heroku CLI from [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) |




### **Step-by-Step Guide to Executing the Web Application Firewall (WAF) Project**  

This guide will walk you through setting up and running a **basic Web Application Firewall (WAF)** using Python and Flask. The WAF will protect a simple web application from **SQL injection (SQLi), Cross-Site Scripting (XSS), and IP-based attacks**.  

---

## **1. Set Up Your Development Environment**  

### **1.1 Install Python**  
Ensure you have **Python 3.x** installed. Download it from the [official Python website](https://www.python.org/downloads/) if necessary.  

Check installation:  
```bash
python --version
```

### **1.2 Install Flask**  
Flask will be used to create the web application. Install it using:  
```bash
pip install Flask
```

### **1.3 Create a Project Directory**  
Organize your files by creating a dedicated project folder:  
```bash
mkdir web_app_firewall
cd web_app_firewall
```

### **1.4 (Optional) Create a Virtual Environment**  
To isolate dependencies, set up a virtual environment:  
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
```

---

## **2. Create a Basic Web Application**  

### **2.1 Create `app.py`**  
This file will contain a simple **Flask web application** with a form for user input.

**Create and add the following code in `app.py`:**  
```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>Enter Input</h2>
        <form action="/submit" method="post">
            <input type="text" name="user_input">
            <button type="submit">Submit</button>
        </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('user_input')
    return f"You entered: {user_input}"

if __name__ == '__main__':
    app.run(debug=True)
```

### **2.2 Run the Web Application**  
Start the server:  
```bash
python app.py
```
You should see the Flask app running at:  
📌 **http://127.0.0.1:5000/**  

Try submitting inputs to ensure it works correctly.

---

## **3. Implement WAF Logic**  

### **3.1 Create `waf.py`**  
This file will contain the **WAF logic** to detect malicious inputs.

**Create `waf.py` and add the following code:**  
```python
import re

# Patterns for detecting attacks
SQL_INJECTION_PATTERN = r"(\bselect\b|\binsert\b|\bunion\b|\b--\b|\b;\b|\bdrop\b)"
XSS_PATTERN = r"<script.*?>.*?</script>"

# List of blocked IPs
BLOCKED_IPS = ["192.168.0.1"]  # Add malicious IPs here

def detect_sql_injection(input_data):
    return bool(re.search(SQL_INJECTION_PATTERN, input_data, re.IGNORECASE))

def detect_xss(input_data):
    return bool(re.search(XSS_PATTERN, input_data, re.IGNORECASE))

def block_ip(ip):
    return ip in BLOCKED_IPS
```

---

### **3.2 Integrate WAF into the Web Application**  
Modify `app.py` to include WAF protection.

**Update `app.py` with WAF checks:**  
```python
from flask import Flask, request, abort
from waf import detect_sql_injection, detect_xss, block_ip

app = Flask(__name__)

@app.before_request
def check_security():
    user_ip = request.remote_addr

    # Block IP if listed
    if block_ip(user_ip):
        abort(403, description="Your IP is blocked.")

    # Check form and query string for attacks
    for key in request.form.keys():
        if detect_sql_injection(request.form[key]) or detect_xss(request.form[key]):
            abort(400, description="Malicious request detected.")

    for key in request.args.keys():
        if detect_sql_injection(request.args[key]) or detect_xss(request.args[key]):
            abort(400, description="Malicious request detected.")

@app.route('/')
def home():
    return '''
        <h2>Enter Input</h2>
        <form action="/submit" method="post">
            <input type="text" name="user_input">
            <button type="submit">Submit</button>
        </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('user_input')
    return f"You entered: {user_input}"

if __name__ == '__main__':
    app.run(debug=True)
```

---

## **4. Test the WAF**  

### **4.1 Run the Application**  
Restart your Flask application:  
```bash
python app.py
```

### **4.2 Test SQL Injection Prevention**  
- Open **http://127.0.0.1:5000/**
- Try entering SQL Injection payloads, such as:  
  ```
  ' OR 1=1 --
  ```
- The application should **block the request with a 400 error**.

### **4.3 Test XSS Prevention**  
- Try entering an XSS payload like:  
  ```html
  <script>alert('Hacked!')</script>
  ```
- The WAF should **block the request with a 400 error**.

### **4.4 Test IP Blocking**  
- Modify `waf.py` to include your IP in `BLOCKED_IPS`.  
- Restart the Flask app and try accessing the site.  
- You should get a **403 Forbidden error**.

---

## **5. Enhance the WAF (Optional Improvements)**  

After successfully building a basic WAF, you can enhance it by adding:  

✅ **Rate Limiting** – Prevent DoS attacks using Flask-Limiter:  
```bash
pip install flask-limiter
```
```python
from flask_limiter import Limiter
limiter = Limiter(app, key_func=lambda: request.remote_addr)
```

✅ **Logging and Alerts** – Log attack attempts for security monitoring:  
```python
import logging
logging.basicConfig(filename='waf.log', level=logging.INFO)
```

✅ **Deploy on a Server** – Host the app using **Heroku, AWS, or a cloud platform**.  

---

## **6. Deploy and Monitor the WAF**  

### **6.1 Deploy on Heroku (Example)**
```bash
pip install gunicorn
echo "web: gunicorn app:app" > Procfile
git init
git add .
git commit -m "Deploy WAF"
heroku create my-waf-app
git push heroku main
```

### **6.2 Monitor Logs**  
```bash
heroku logs --tail
```
or  
```bash
cat waf.log
```

---

## **7. Conclusion**  

You have successfully built and tested a **basic Web Application Firewall (WAF)** using Python and Flask. This project helps in understanding **web security, HTTP traffic filtering, and cybersecurity best practices**.

🔹 **Key Takeaways:**  
✅ Built a **Flask web application**  
✅ Implemented a **basic WAF to filter SQL injection and XSS**  
✅ Tested the WAF by simulating **malicious requests**  
✅ Improved security with **IP blocking and request filtering**  

---


---

## ⭐ **Contribute**  
Want to improve this project?  
- **Fork the repository**  
- **Submit a pull request** with improvements  
- **Report bugs or suggest features** in the Issues section  

---

## 🎯 **Author**  
👤 **Manish Naik** 
📩 [Manishmnaik20@gmail.com]  
🔗 [https://github.com/manishnaik20]  

## **📌 License**
This project is open-source and available under the **MIT License**.

---

🎯 **If you found this project helpful, please ⭐ star the repository!** 🚀
