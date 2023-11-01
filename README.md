# realtime-DataIngestion
This repository uses AWS cloud services and Big Data technologies to process data in real time and archive data in data lake storage 

# AWS setup

We created a free-tier account on AWS. Then performed the following activities:

1. Launched a new EC2 instance
2. While creating a new instance, we generated a new key-pair value so that we can extract a .pem file and connect to the machine through local.
3. Once the instance is up and running and the .pen file is saved on your local machine, open your terminal and navigate to the folder where your .pem file is.
4. Copy the ssh command from your AWS account and run it on your terminal (assuming you are on the same .pem file location).
5. For Mac user, there might be a permission denied error. So before executing the ssh command, execute the following command:
        chmod 400 <name of the .pem file>
