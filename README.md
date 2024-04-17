# End to End Text-Summarization-Case-Study

## workflows
1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update configuration manager in src/configuration.py
5. Update components
6. Update pipeline
7. Update main.py
8. Update app.py


# How to run?
### STEPS:

Clone the repository

```cmd
https://github.com/Chetand777/Text-Summarization-Case-Study
```

### STEP 01: Create a venv after opening the repo

```cmd
python -m venv summary
```

```cmd
summary\Scripts\activate
```

### STEP 02: Install the requirements
```cmd
pip install -r requirements.txt
```

```cmd
python app.py
```

Now,
```cmd
open up your local host and port
```


```cmd
Author: Chetan D
Email: chetandaddikar31@gmail.com

```

# AWS CI/CD Deployment with Github Actions

## 1. Login to AWS console

## 2. Create IAM user for deployment

    #with specific access

    1. EC2 access: It is vertual machine

    2. ECR: Elatic Container Registry to save your docker image in AWS


    #description: About the deployment

    1. Build the docker image of the source code

    2. Push your docker image to ECR

    3. Launch your EC2

    4. Pull your image from ECR to EC2

    5. Launch your docker image in EC2


    #Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess


## 3. Create ECR repo to store/save docker image
    - Save the URI: 381491967036.dkr.ecr.ap-south-1.amazonaws.com/text-s


## 4. Create EC2 Machine (Ubuntu)


## 5. Open EC2 and install docker in EC2 machine:


    #optional:

    sudo apt-get update -y

    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker


## 6. Configure EC2 as a self hosted runner:

setting>actions>runner>new self hosted runner>choose os>run command one by one


## 7. Set up github secrets

    AWS_ACCESS_KEY_ID

    AWS_SECRET_ACCESS_KEY

    AWS_REGION

    AWS_ECR_LOGIN_URI

    ECR_REPOSITORY_NAME 
