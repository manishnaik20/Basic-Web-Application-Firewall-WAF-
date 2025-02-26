A Web Application Firewall (WAF) is a security system designed to monitor and filter HTTP traffic between a web application and the internet, providing an extra layer of protection against common web application attacks like SQL injection, Cross-Site Scripting (XSS), and Cross-Site Request Forgery (CSRF). Developing a basic WAF as a project can be a great hands-on way to understand web application security and HTTP traffic filtering.

Below is a detailed guide on how to build and execute a Web Application Firewall (WAF) project.

---

### *Project: Building a Basic Web Application Firewall (WAF)*

#### *Objective:*
To build a simple Web Application Firewall that can detect and filter common web-based attacks, such as SQL injection, XSS, and others.

#### *Tools & Technologies:*
- *Programming Language:* Python (using Flask for the web app and libraries for filtering traffic)
- *Web Framework:* Flask (for the web application that the WAF will protect)
- *WAF Logic:* Custom Python code to analyze and block malicious HTTP requests
- *Other Tools*: Regular expressions (Regex), HTTP libraries, and firewall rule sets

---

### *Step-by-Step Execution:*

---

### *1. Set Up Your Development Environment*

1. *Install Python*: Make sure Python 3.x is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).
   
2. *Install Flask*: Flask will be used to set up the basic web application.
   bash
   pip install Flask
   

3. *Create a Project Directory*: Create a folder for your project to keep everything organized.
   bash
   mkdir web_app_firewall
   cd web_app_firewall
   

4. *Create Virtual Environment (Optional but recommended)*:
   bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   venv\Scripts\activate  # For Windows
   

---

### *2. Create a Basic Web Application*

1. **Create a app.py file**:
   This file will contain the basic Flask web application that the WAF will protect.
   
   python
   from flask import Flask, request

   app = Flask(__name__)

   @app.route('/')
   def home():
       return "Welcome to the Web App!"

   @app.route('/submit', methods=['POST'])
   def submit():
       user_input = request.form.get('user_input')
       return f"You entered: {user_input}"

   if __name__ == '__main__':
       app.run(debug=True)
   

2. *Run the web app*:
   bash
   python app.py
   
   The application will be running locally on http://127.0.0.1:5000/.

---

### *3. Implement WAF Logic*

Now, we’ll add a basic WAF layer that will filter out malicious inputs before they reach the web application.

1. **Create a waf.py file**:
   This will contain the core WAF logic to detect and block common attacks.

   *Basic WAF Detection Features*:
   - SQL Injection Detection
   - XSS Detection
   - Blocked IP addresses

   Here's an example of how the waf.py file might look:

   python
   import re

   # Simple rule for detecting SQL injection patterns
   SQL_INJECTION_PATTERN = r"(\bselect\b|\binsert\b|\bunion\b|\b--\b|\b;\b|\bdrop\b)"

   # Simple rule for detecting Cross-Site Scripting (XSS)
   XSS_PATTERN = r"<script.*?>.*?</script>"

   # Blocked IPs (e.g., a blacklist of known malicious IPs)
   BLOCKED_IPS = ["192.168.0.1"]

   def detect_sql_injection(input_data):
       if re.search(SQL_INJECTION_PATTERN, input_data, re.IGNORECASE):
           return True
       return False

   def detect_xss(input_data):
       if re.search(XSS_PATTERN, input_data, re.IGNORECASE):
           return True
       return False

   def block_ip(ip):
       if ip in BLOCKED_IPS:
           return True
       return False
   

2. *Integrating WAF with Flask App*:
   You need to integrate the WAF logic with your Flask web application, so it can filter requests before they reach your endpoints.

   Modify the app.py file:

   python
   from flask import Flask, request, abort
   from waf import detect_sql_injection, detect_xss, block_ip

   app = Flask(__name__)

   @app.before_request
   def check_security():
       # Get the user's IP address
       user_ip = request.remote_addr

       # Block request if IP is in blocked list
       if block_ip(user_ip):
           abort(403, description="Your IP is blocked.")

       # Check for SQL injection in the query string, form data, or JSON
       for key in request.form.keys():
           if detect_sql_injection(request.form[key]):
               abort(400, description="SQL Injection attempt detected.")
           if detect_xss(request.form[key]):
               abort(400, description="XSS attempt detected.")
       
       for key in request.args.keys():
           if detect_sql_injection(request.args[key]):
               abort(400, description="SQL Injection attempt detected.")
           if detect_xss(request.args[key]):
               abort(400, description="XSS attempt detected.")

   @app.route('/')
   def home():
       return "Welcome to the Web App!"

   @app.route('/submit', methods=['POST'])
   def submit():
       user_input = request.form.get('user_input')
       return f"You entered: {user_input}"

   if __name__ == '__main__':
       app.run(debug=True)
   

---

### *4. Testing the WAF*

1. *Run your Flask Application* again:
   bash
   python app.py
   

2. *Test the WAF*:
   - Open your browser or use a tool like Postman to send requests to the application.
   - *Test SQL Injection*: Try submitting input like ' OR 1=1 --.
   - *Test XSS*: Try submitting input like <script>alert('XSS')</script>.
   - *Test Blocked IP*: If you’re testing locally, you can spoof the IP by modifying the Flask app to simulate a blocked IP address.

3. *Verify that the WAF blocks malicious requests*:
   - SQL injection attempts should result in a 400 Bad Request response.
   - XSS attempts should also return a 400 Bad Request response.
   - Blocked IP addresses should return a 403 Forbidden response.

---

### *5. Enhance Your WAF (Optional)*

After building the basic functionality, you can enhance the WAF by adding more complex filtering techniques such as:
- *Rate Limiting*: Prevent DDoS attacks by limiting the number of requests a user can make within a set time.
- *Advanced Signature-based Detection*: Add more sophisticated detection patterns for different attack types.
- *Logging and Alerts*: Set up logging to capture attack attempts and alert administrators.
- *Deploy the WAF*: Deploy your Flask app on a cloud service (AWS, Heroku, etc.) for real-world testing.

---

### *6. Final Testing and Deployment*

1. *Test all edge cases*: Make sure you test various types of attack vectors and also ensure legitimate traffic is not blocked.
2. *Deploy to Production*: Deploy the app and the WAF to a production server once it’s ready for real-world traffic.
3. *Ongoing Improvements*: Keep improving your WAF by adding new detection rules and fine-tuning the existing ones.

---

### *Conclusion*

Building a basic Web Application Firewall is a fantastic project for freshers looking to dive into web security. This project covers:
- *Basic Flask web application creation*
- *WAF implementation using Python*
- *Traffic filtering based on common attack patterns*

As you progress, you can refine your WAF with more advanced techniques, such as machine learning-based detection or integration with other security services.
