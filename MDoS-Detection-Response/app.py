from flask import Flask, render_template_string
app = Flask(__name__)
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>M-DoS Detection</title>
</head>

<body style="font-family:Arial;background:#f2f2f2;">
<div style="width:500px;margin:auto;margin-top:80px;
background:white;padding:40px;border-radius:20px;text-align:center;">
<h1>🛡️ M-DoS Detection</h1>
<h2>Cloud Security Monitoring Dashboard</h2>
<div style="padding:20px;border:2px solid red;
border-radius:10px;color:red;font-size:28px;">

SYSTEM STATUS: UNDER ATTACK
</div>
<button style="margin-top:30px;padding:15px;width:100%;
background:green;color:white;border:none;border-radius:10px;
font-size:24px;">
NEUTRALIZE ATTACK
</button>
</div>
</body>
</html>
"""
@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
