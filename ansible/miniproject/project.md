# Project

Using the resources from this week you are in charge of setting up the development environment for creating a new app. The developers have asked for the following: 
- VPC with 3x public subnets, each with 400+ available IP addresses
- MySQL RDS with configured credentials
- 1x Controller EC2 (has Terraform and ansible installed to set up environment) 
- 1x CI Server EC2 with ports open for HTTP, MySQL, Jenkins and SSH from controller EC2
- 1x Deployment EC2 with public HTTP and MySQL
- CI Server should have Docker, Jenkins, unzip, wget and curl installed
- CI Server needs to add Jenkins to sudo group and add user to Docker group 
- Deployment EC2 should run the app at this repo https://gitlab.com/Reece-Elder/devops-m5-nodeproject/-/tree/main

All of the steps should be done via Ansible and Terraform where possible, limiting the use of the AWS GUI.

