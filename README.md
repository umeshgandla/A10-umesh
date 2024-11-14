# A10-umesh
Assignment: CI/CD Pipeline with Jenkins Master in Docker, Jenkins Slave on EC2, IAM Role-Based Access, Multi-Environment Docker Deployment, and Email Notification

# CI/CD Pipeline with Jenkins and Docker

## Overview
This repository hosts the code and configurations for a comprehensive CI/CD pipeline utilizing Jenkins running in Docker on an AWS EC2 instance (master), with an agent (slave) on another EC2 instance. This setup automates the code checkout, Docker image build, security scanning, testing, and deployment across multiple environments (DEV, STAGING, PROD).

## Tools and Technologies
- **CI/CD**: Jenkins (master in Docker on EC2, slave on another EC2)
- **Containerization**: Docker
- **Source Control**: GitHub (with branch protection and PR-based merging)
- **Container Registry**: Amazon ECR
- **Secrets Management**: AWS Secrets Manager
- **Security Scanning**: Trivy, SonarQube
- **Notifications**: Email (using Jenkins Email Extension Plugin)

## Repository Structure
/ ├── Dockerfile # Dockerfile to build the application image ├── Jenkinsfile # Jenkins pipeline configuration └── app.py # Sample Python application (Replace with your application)

markdown
Copy code

## Getting Started

### Prerequisites
- AWS Account
- Docker installed on your local machine
- Jenkins installed with required plugins

### Initial Setup
1. **Clone the repository:**
git clone https://github.com/<your-username>/<repository-name>.git cd <repository-name>

markdown
Copy code

2. **Create Environment-Specific Branches:**
- `main` for PROD
- `staging` for STAGING
- `dev` for DEV

### Branch Protection Rules
Ensure that you set up branch protection rules to secure the branches:
- Require pull request reviews before merging.
- Require status checks to pass before merging.

## Jenkins Setup
### Launch EC2 Instance for Jenkins Master
- Launch an EC2 instance using Amazon Linux 2 or Ubuntu.
- Install Docker and run Jenkins as a Docker container.

### Configure Jenkins Master and Slave
- Follow the detailed steps in the assignment document to configure Jenkins Master and Slave nodes, install necessary plugins, and set up IAM roles for secure integration with AWS services.

### Configuring the Pipeline
1. **Create a Multi-Branch Pipeline in Jenkins.**
2. **Set up the GitHub webhook for automatic triggers.**

## Running the Pipeline
- Make code changes in the respective branches and create pull requests.
- The pipeline triggers automatically on pull request events, performing build, test, and deployment tasks defined in the `Jenkinsfile`.

## Testing and Validation
- After deploying, access the application using the EC2 IP to verify the deployment across different environments.

## Contributing
Contributions are welcome! Please feel free to submit pull requests.
