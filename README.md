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

# Kafka Setup on your EC2 machine

Once the EC2 machine is up and running, we need to install Kafka on that machine. So, we will be performing the following activities:

1. Get the compressed version of Kafka on your EC2 instance

    wget https://downloads.apache.org/kafka/3.3.1/kafka_2.12-3.3.1.tgz

2. Un-compress the Kafka files:

    tar -xvf kafka_2.12-3.3.1.tgz

In order to run Kafka, we need to install Java on your remote machine. In order to do that perform the following commands:

1. sudo yum install java-1.8.0-openjdk
2. java -version

Once Java is installed, we need to navigate to the kafka folder and then start the zookeeper service.

1. cd kafka_2.12-3.3.1

