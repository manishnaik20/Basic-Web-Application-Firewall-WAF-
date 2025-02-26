from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging

# Initialize the Limiter object
limiter = Limiter(app, key_func=get_remote_address)

# Rate limit for all routes: 5 requests per minute per IP
@app.route('/')
@limiter.limit("5 per minute")
def home():
    return '''
        <h2>Enter Input</h2>
        <form action="/submit" method="post">
            <input type="text" name="user_input">
            <button type="submit">Submit</button>
        </form>
    '''


# Set up logging
logging.basicConfig(filename='waf.log', level=logging.INFO)

# Log an alert when an attack is detected
@app.before_request
def check_security():
    """Security middleware to check for SQL injection and XSS"""
    for key, value in request.form.items():
        if detect_sql_injection(value):
            logging.info(f"SQL Injection detected from {request.remote_addr}: {value}")
            abort(400, description="🚨 SQL Injection attempt detected! 🚨")
        
        if detect_xss(value):
            logging.info(f"XSS attempt detected from {request.remote_addr}: {value}")
            abort(400, description="🚨 XSS attempt detected! 🚨")
