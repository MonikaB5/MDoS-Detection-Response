# MDoS-Detection-Response --> https://mdos-detection-response.onrender.com
This project demonstrates a cloud-based cybersecurity solution designed to detect and mitigate Memory Denial of Service (M‑DoS) attacks in real time. The system integrates AWS CloudWatch monitoring, Lambda automated response, and a Flask web dashboard to provide both technical defense and a user-friendly interface for visualization.


🛡️ Real-Time M‑DoS Detection & Automated Response
✨ Project Summary
A cloud-native cybersecurity solution that detects and mitigates Memory Denial of Service (M‑DoS) attacks in real time.
It integrates AWS CloudWatch monitoring, Lambda automated defense, and a Flask dashboard for visualization.
This project demonstrates practical skills in cloud computing, automation, and web development, while also showcasing professional documentation and reproducibility.

⚙️ Key Features
Stress Tool Simulation → Generate artificial memory load for testing.

CloudWatch Agent → Collects memory metrics (mem_used_percent).

CloudWatch Alarms → Detects abnormal memory usage (>80%).

AWS Lambda Function → Automated response to stop EC2 and log forensic data.

S3 Bucket → Stores forensic logs for analysis.

Flask Dashboard → Premium web interface for monitoring and attack simulation.

🌐 Deployment Notes
This project was implemented in the AWS Academy Sandbox, which provides a temporary cloud environment.
⚠️ Important: All EC2 instances, CloudWatch alarms, and Lambda functions are deleted once the sandbox session ends.

To ensure the project remains professional and demonstrable, this repository includes:

Flask Dashboard Code (src/app.py)

Screenshots from EC2, CloudWatch, and Lambda

Documentation explaining workflow and architecture

When deployed in AWS EC2, the dashboard runs live at:

Code
http://<EC2-Public-IP>:5000
Example (temporary): http://18.215.230.44:5000  
Since the sandbox resets, this link may expire.
👉 Permanent reference is provided via screenshots.

📸 Screenshots
Stress Tool Installation

CloudWatch Alarm Trigger

AWS Lambda Automated Response

Flask Dashboard Interface

🚀 Quick Rebuild Checklist
Launch EC2 instance in AWS Academy Sandbox.

Install CloudWatch Agent and configure memory metrics.

Set CloudWatch Alarm at 80% memory usage.

Deploy Lambda function with boto3 to stop EC2 + log to S3.

Run Flask app (python3 app.py) on EC2 port 5000.

Access dashboard via http://<EC2-Public-IP>:5000.

🎯 Skills Demonstrated
AWS Cloud Monitoring (EC2, CloudWatch, Lambda, S3)

Python Automation (boto3, Flask)

Web Dashboard Design (HTML, CSS, Charts)

Cloud Security & Forensic Logging

Professional Documentation & GitHub Portfolio Management
