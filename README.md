# MDoS-Detection-Response --> https://mdos-detection-response.onrender.com

# 🛡️ REAL-TIME MEMORY DOS DETECTION & AUTOMATED RESPONSE SYSTEM

[![Live Demo] --> (https://img.shields.io/badge/Demo-Live%20on%20Render-brightgreen)](https://mdos-detection-response.onrender.com)

This project demonstrates a cloud-based cybersecurity solution designed to detect and mitigate Memory Denial of Service (M‑DoS) attacks in real time. The system integrates AWS CloudWatch monitoring, Lambda automated response, and a Flask web dashboard for visualization.

## ✨ Project Summary
A cloud-native cybersecurity solution that detects and mitigates M-DoS attacks. This project showcases practical skills in cloud computing, security automation, and web development.

## ⚙️ Key Features
* **Stress Tool Simulation** → Generate artificial memory load for testing.
* **CloudWatch Agent** → Collects memory metrics (`mem_used_percent`) from the EC2 instance.
* **CloudWatch Alarms** → Automatically detects abnormal memory usage (>80%).
* **AWS Lambda Function** → Triggered defense mechanism to stop the instance and log forensic data.
* **S3 Bucket** → Secure storage for forensic logs and attack reports.
* **Flask Dashboard** → A professional web interface to monitor system health and simulate attacks.

## 📁 Repository Structure
```text
MDoS-Detection-Response/
├── project_reference/
│   ├── home.py              # Main Flask Application
│   ├── templates/           # UI Components (dashboard.html)
│   └── requirements.txt     # Python Dependencies
├── Project_Report_MDoS.pdf  # Detailed Technical Documentation
└── screenshots/             # Visual Proof of Implementation

🚀 Updated Setup Instructions Section:
---
## 🚀 Setup Instructions

### 1. Local Preview
To run the dashboard interface on your local machine:
```bash
cd project_reference
pip install -r requirements.txt
python home.py
Access the UI via browser at: http://127.0.0.1:5000

2. AWS Implementation (M-DoS Defense)
EC2 Deployment: The dashboard was successfully hosted on AWS EC2 at http://18.215.230.44:5000 during the simulation.

Stress Installation: Use sudo apt install stress -y to simulate high load.

CloudWatch Configuration: Installed the unified agent to track mem_used_percent.

Automation: Set up a Lambda function using boto3 to automatically stop the instance when the memory alarm is triggered.

🌐 Deployment Notes
This project was originally implemented in the AWS Academy Sandbox.
⚠️ Note: As the AWS sandbox environment is temporary, the backend cloud triggers are illustrative in this repo. The live Render Demo provides a permanent reference for the dashboard's design and functionality.

📸 Project Screenshots

Stress Tool Installation

CloudWatch Alarm Trigger

AWS Lambda Automated Response

Dashboard 

Author: Monika B | Aspiring Software Professional | MCA Student | Cloud & Security Enthusiast | 2026



