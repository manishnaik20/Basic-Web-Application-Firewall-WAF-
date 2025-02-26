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

---

## **📌 Contributors**
👤 **Your Name** – *Developer*  
📧 Contact: [your-email@example.com](mailto:your-email@example.com)  

---

## **📌 License**
This project is open-source and available under the **MIT License**.

---

🎯 **If you found this project helpful, please ⭐ star the repository!** 🚀
