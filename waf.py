import re

# Simple rule for detecting SQL injection patterns
SQL_INJECTION_PATTERN = r"(\bselect\b|\binsert\b|\bunion\b|\b--\b|\b;\b|\bdrop\b)"

# Simple rule for detecting Cross-Site Scripting (XSS)
XSS_PATTERN = r"<script.*?>.*?</script>"

def detect_sql_injection(input_data):
    """Check for SQL injection patterns"""
    if re.search(SQL_INJECTION_PATTERN, input_data, re.IGNORECASE):
        return True
    return False

def detect_xss(input_data):
    """Check for XSS attack patterns"""
    if re.search(XSS_PATTERN, input_data, re.IGNORECASE):
        return True
    return False
