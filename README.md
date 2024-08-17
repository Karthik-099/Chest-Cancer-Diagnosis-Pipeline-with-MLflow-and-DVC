# Chest-Cancer-Diagnosis-Pipeline-with-MLflow-and-DVC
An end-to-end pipeline for chest cancer diagnosis using machine learning. This project employs MLflow for experiment tracking and DVC for data versioning, ensuring efficient data management and reproducibility. Features include data preprocessing, model training, evaluation, and deployment within an MLOps framework.

## Tools and Technologies Used

1. **MLflow**: Used for tracking experiments, logging parameters, metrics, and artifacts to ensure reproducibility.  
   [MLflow Documentation](https://www.mlflow.org/docs/latest/index.html)
2. **DVC (Data Version Control)**: Manages large datasets and tracks changes in data, models, and pipelines over time.  
   [DVC Documentation](https://dvc.org/doc)
3. **GitHub Actions**: Automates workflows for continuous integration and deployment (CI/CD).
4. **Dagshub**: Integrates with GitHub and DVC for easy collaboration, data management, and experiment tracking.
5. **TensorFlow**: Used for building and training machine learning models.  
   [TensorFlow Documentation](https://www.tensorflow.org/learn)
6. **Keras**: A high-level neural networks API used for building and training models, specifically with the VGG16 architecture.  
   [Keras Documentation](https://keras.io/)

## Model Parameters

- **Base Model**: `VGG16`
- **Total Parameters**: `14,764,866`
- **Trainable Parameters**: `50,178`
- **Non-trainable Parameters**: `14,714,688`

This model uses the VGG16 architecture, which is pre-trained on the ImageNet dataset. The total number of parameters indicates the complexity of the model, with a significant portion being non-trainable as they are inherited from the pre-trained VGG16 network.

# AWS-CICD-Deployment-with-Github-Actions

This guide covers the steps to deploy an application using AWS services and GitHub Actions for continuous integration and continuous deployment (CI/CD).

## Prerequisites

1. **Login to AWS Console.**
2. **Create an IAM User for Deployment** with the following specific access:
    - **EC2 Access**: This allows you to manage virtual machines (EC2 instances).
    - **ECR Access**: Elastic Container Registry (ECR) to store your Docker images on AWS.

## Description: About the Deployment

1. **Build the Docker Image** of your source code.
2. **Push the Docker Image to ECR** (Elastic Container Registry).
3. **Launch an EC2 Instance** on AWS.
4. **Pull the Docker Image from ECR** onto the EC2 instance.
5. **Launch the Docker Image on EC2** to deploy your application.

## IAM Policies Required

- **AmazonEC2ContainerRegistryFullAccess**
- **AmazonEC2FullAccess**

## Deployment Steps

1. **Create an ECR Repository** to store your Docker image.
   - Save the repository URI (e.g., `566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken`).

2. **Create an EC2 Instance** (preferably Ubuntu).
   
3. **Install Docker on the EC2 Instance** (optional but recommended):
   - Update and upgrade the package lists:
     ```bash
     sudo apt-get update -y
     sudo apt-get upgrade
     ```
   - Install Docker:
     ```bash
     curl -fsSL https://get.docker.com -o get-docker.sh
     sudo sh get-docker.sh
     sudo usermod -aG docker ubuntu
     newgrp docker
     ```

4. **Configure EC2 as a Self-Hosted Runner** for GitHub Actions:
   - Go to your GitHub repository settings: `Settings > Actions > Runners > New self-hosted runner`.
   - Choose the operating system and run the provided commands on your EC2 instance.

5. **Set Up GitHub Secrets** for Deployment:
   - Go to your GitHub repository and add the following secrets:
     ```plaintext
     AWS_ACCESS_KEY_ID=
     AWS_SECRET_ACCESS_KEY=
     AWS_REGION=us-east-1
     AWS_ECR_LOGIN_URI=566373416292.dkr.ecr.us-east-1.amazonaws.com
     ECR_REPOSITORY_NAME=simple-app
     ```

## Deployed Application

The model has been deployed using Amazon AWS aswell as Render and can be accessed at the following link:

[Chest Cancer Diagnosis Application](https://adenocarcinoma-chest-cancer.onrender.com/)

## Conclusion

Follow the above steps to set up your CI/CD pipeline using AWS and GitHub Actions. This setup allows you to automate the process of building, storing, and deploying your Dockerized applications on AWS. The deployed model is now accessible for use and testing via the provided link.
