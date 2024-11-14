from flask import Flask

app = Flask(__name__)

@app.route('/')


def hello():
    return "Assignment: CI/CD Pipeline with Jenkins Master in Docker, Jenkins Slave on EC2, IAM Role-Based Access, Multi-Environment Docker Deployment, and Email Notification"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
