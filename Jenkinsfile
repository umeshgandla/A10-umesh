pipeline {
    agent { label 'slave-agent' }

    environment {
        ECR_REPO = '866934333672.dkr.ecr.ap-northeast-1.amazonaws.com/ume-repo'          // Replace with your actual ECR URL
        IMAGE_NAME = 'flask-app'
        TAG = "${env.BRANCH_NAME}-${env.BUILD_ID}"
        PORT = "${env.BRANCH_NAME == 'dev' ? '5001' : env.BRANCH_NAME == 'staging' ? '5002' : '5003'}"
        CONTAINER_NAME = "${IMAGE_NAME}-${env.BRANCH_NAME}"
        TRIVY_REPORT = 'trivy-report.txt' // Defining the Trivy report file name
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: "${env.BRANCH_NAME}", url: 'https://github.com/umeshgandla/A10-umesh.git' // Replace with your GitHub repository URL
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build an image tagged with the branch name and build ID
                    sh "docker build -t ${env.ECR_REPO}:${env.TAG} ."
                }
            }
        }

       stage('Trivy Security Scan') {
            steps {
                script {
                    // Run Trivy scan on the branch-specific image and save the report
                    sh "trivy image --format template --template '@trivy/templates/default.tpl' -o ${TRIVY_REPORT} ${ECR_REPO}:${TAG}"
                }
            }
            post {
                always {
                    // Send an email with the Trivy report attached
                    mail(
                        to: 'umesh0019@gmail.com', // Replace with the recipient's email
                        subject: "Trivy Scan Report - ${env.BRANCH_NAME}",
                        body: "Hello,\n\nAttached is the Trivy scan report for the Docker image '${env.IMAGE_NAME}:${env.TAG}'.\n\nBest regards,\nJenkins",
                        attachmentsPattern: "${TRIVY_REPORT}"
                    )
                }
            }
        }

        stage('Push to ECR') {
            steps {
                // Log in to ECR using the instance profile attached to the EC2 instance
                sh "aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin ${env.ECR_REPO}"
                
                // Push the Docker image to ECR with the branch-specific tag
                sh "docker push ${env.ECR_REPO}:${env.TAG}"
            }
        }

        stage('Cleanup Previous Containers') {
            steps {
                script {
                    // Stop and remove any container with the same name for the current branch
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"
                    sh "fuser -k ${PORT}/tcp || true" // Free up the designated port
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run the Docker container for testing with the branch-specific port
                    sh "docker run -d --name ${CONTAINER_NAME} -p ${PORT}:5000 ${ECR_REPO}:${TAG}"
                    sh 'sleep 5' // Wait for the container to start

                    // Test if the Flask app is responding on the designated port
                    sh "curl -f http://localhost:${PORT} || exit 1"

                    // Stop and remove the test container after testing
                    sh "docker stop ${CONTAINER_NAME}"
                    sh "docker rm ${CONTAINER_NAME}"
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'  // Only deploy if we're on the main branch
            }
            steps {
                script {
                    // Deploy the main branch container to production on port 80
                    sh """
                    docker pull ${ECR_REPO}:${TAG}
                    docker stop ${IMAGE_NAME} || true
                    docker rm ${IMAGE_NAME} || true
                    docker run -d --name ${IMAGE_NAME} -p 80:5000 ${ECR_REPO}:${TAG}
                    """
                }
            }
        }
    }

    post {
        a
