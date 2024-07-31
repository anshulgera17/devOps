# AWS Learning

## AWS questions

- What is VPC1 ?
- What is difference between public and private subnet ?
- What is reserved instance ?
- What is difference between spot instance and reserved instance ?
- What is cloud formation ?
- Have you used Route 53 ?
- What is the best feature of AWS which you like ?

## EC2 (Elastic Compute Cloud)
- What is Amazon EC2?
- Explanation of EC2 as a service that provides resizable compute capacity in the cloud.
- How do you create and launch an EC2 instance?
- Steps involved in creating and launching an EC2 instance using the AWS Management Console or CLI.
- What are the different instance types in EC2?
- Explanation of various instance types such as General Purpose, Compute Optimized, Memory Optimized, Storage Optimized, and Accelerated Computing.
- What are the security groups and how do they work in EC2?
- Details on how security groups act as virtual firewalls to control inbound and outbound traffic for EC2 instances.
- Explain the concept of Elastic IPs.
- How Elastic IP addresses are static IPv4 addresses designed for dynamic cloud computing.
- How can you resize an EC2 instance?
- Steps to stop the instance, change its instance type, and restart it.
- What is an EBS volume and how do you attach it to an EC2 instance?
- Explanation of Elastic Block Store (EBS) and the process of attaching and detaching EBS volumes.
- What is an AMI and how do you create one?
- Details on Amazon Machine Images (AMIs) and the process of creating a custom AMI.

## S3 (Simple Storage Service)

- What is Amazon S3?
- Explanation of S3 as an object storage service that offers scalability, data availability, security, and performance.
- How do you create an S3 bucket?
- Steps to create an S3 bucket using the AWS Management Console or CLI.
- What are the different storage classes in S3?
- Explanation of storage classes such as Standard, Intelligent-Tiering, Standard-IA, One Zone-IA, Glacier, and Glacier Deep Archive.
- How does versioning work in S3?
- Details on enabling versioning to keep multiple versions of an object in the same bucket.
- What is an S3 lifecycle policy?
- How to manage your objects so that they are stored cost-effectively throughout their lifecycle.
- How do you secure data in S3?
- Methods like bucket policies, IAM policies, ACLs, and enabling encryption.
- What is S3 Transfer Acceleration?
- Explanation of S3 Transfer Acceleration and how it speeds up content transfer to and from S3 buckets.

## RDS (Relational Database Service)

- What is Amazon RDS?
- Explanation of RDS as a managed relational database service that supports various database engines.
- How do you create an RDS instance?
- Steps to create an RDS instance using the AWS Management Console or CLI.
- What are the different database engines supported by RDS?
- Supported engines like MySQL, PostgreSQL, MariaDB, Oracle, and SQL Server.
- How do you secure an RDS instance?
- Methods like using security groups, subnet groups, and enabling encryption.
- What is RDS Multi-AZ deployment?
- Explanation of Multi-AZ deployments for high availability and automated failover.
- How do you backup and restore an RDS instance?
- Details on automated backups, manual snapshots, and restoring from a backup.

## IAM (Identity and Access Management)

- What is AWS IAM?
- Explanation of IAM as a web service for securely controlling access to AWS services.
- How do you create an IAM user?
- Steps to create an IAM user using the AWS Management Console or CLI.
- What are IAM roles and how do they differ from users?
- Explanation of IAM roles as entities that AWS resources can assume to access other resources.
- What are IAM policies and how do you create one?
- Details on creating and attaching JSON policy documents to users, groups, or roles.
- What is the principle of least privilege and how do you implement it in IAM?
- Explanation of granting the minimum required permissions to users or roles.
- What are IAM groups and how do they work?
- How to use groups to manage permissions for multiple users.

## VPC (Virtual Private Cloud)

- What is Amazon VPC?
- Explanation of VPC as a service to launch AWS resources in a virtual network.
- How do you create a VPC?
- Steps to create a VPC using the AWS Management Console or CLI.
- What are subnets and how do they work in VPC?
- Details on dividing a VPC into public and private subnets.
- What is a route table and how do you configure it?
- Explanation of route tables to manage network traffic within a VPC.
- What is a NAT gateway and how does it differ from an Internet gateway?
- NAT gateway for private subnet internet access and Internet gateway for public subnet access.
- How do you secure a VPC?
- Using security groups, network ACLs, and VPC peering for securing network traffic.

## CloudFormation

- What is AWS CloudFormation?
- Explanation of CloudFormation as a service for provisioning and managing AWS infrastructure as code.
- How do you create a CloudFormation stack?
- Steps to create a stack using a CloudFormation template.
- What are CloudFormation templates and what do they contain?
- Details on the structure of templates, including resources, parameters, mappings, conditions, and outputs.
- How do you update a CloudFormation stack?
- Methods to update a stack using change sets or direct updates.
- What is a nested stack in CloudFormation?
- Explanation of using nested stacks to manage complex infrastructure.

## Load Balancers

- What is an Elastic Load Balancer (ELB)?
- Explanation of ELB as a service to distribute incoming application traffic across multiple targets.
- What are the different types of load balancers in AWS?
- Details on Application Load Balancer (ALB), Network Load Balancer (NLB), and Classic Load Balancer (CLB).
- How do you configure an Application Load Balancer?
- Steps to set up an ALB, including target groups, listeners, and rules.
- What are target groups and how do they work with load balancers?
- Explanation of target groups for routing requests to one or more registered targets.
- How does health checking work in ELB?
- Details on configuring health checks to ensure traffic is only routed to healthy targets.
- What is the difference between ALB and NLB?
- Comparison of ALB for HTTP/HTTPS traffic and NLB for TCP/UDP traffic.


- 130 mins , 65 questions and $ 150 USD.
- Reliability - 34 %
- Performance efficiency - 24 %
- Security - 26 %
- Cost optimization - 10 %
- Operational Excellence -  6 %

<br>

- AWS well architected framework
- Operational excellence
- Reliability
- Security
- Performance efficiency
- Cost optimization

<br>

- IAM: Users, Groups, Roles, Policies
- Root, administrator, power users
- STS - IAM (security token service)
- STS API Calls
- AssumeRole
- AssumeRoleWithWebIdentiy
- AssumeRoleWithSAML
- GetFederationToken
- GetSessionToken
- Custom Identity Provider
- LDAP/Active Directory
- OpenIDConnect for connecting login from - facebook, google….
