provider "aws" {
 access_key   = var.access_key
 secret_key   = var.secret_key
 region       = "eu-west-2"
}

resource "aws_vpc" "example_vpc" {
  cidr_block = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "example-vpc"
  }
}

resource "aws_subnet" "example_subnet_1" {
  vpc_id     = aws_vpc.example_vpc.id
  cidr_block = "10.0.1.0/23"

  tags = {
    Name = "example-subnet_1"
  }
}

resource "aws_subnet" "example_subnet_2" {
  vpc_id     = aws_vpc.example_vpc.id
  cidr_block = "10.0.3.0/23"

  tags = {
    Name = "example-subnet_2"
  }
}

resource "aws_subnet" "example_subnet_3" {
  vpc_id     = aws_vpc.example_vpc.id
  cidr_block = "10.0.5.0/23"

  tags = {
    Name = "example-subnet_3"
  }
}

resource "aws_internet_gateway" "example_igw" {
  vpc_id = aws_vpc.example_vpc.id

  tags = {
    Name = "example-igw"
  }
}
 

resource "aws_route_table" "example_rt" {
  vpc_id = aws_vpc.example_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.example_igw.id
  }

  tags = {
    Name = "example-rt"
  }
}

resource "aws_route_table_association" "example_rta_1" {
  subnet_id      = aws_subnet.example_subnet_1.id
  route_table_id = aws_route_table.example_rt.id
}

resource "aws_route_table_association" "example_rta_2" {
  subnet_id      = aws_subnet.example_subnet_2.id
  route_table_id = aws_route_table.example_rt.id
}

resource "aws_route_table_association" "example_rta_3" {
  subnet_id      = aws_subnet.example_subnet_3
  route_table_id = aws_route_table.example_rt.id
}

resource "aws_security_group" "my_sg" {
  vpc_id = aws_vpc.example_vpc.id
  name        = "my_sg"
  description = "Security group for everything"

  ingress { #SSH (port 22)
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

    ingress { #HTTP (port 80)
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress { #MYSQL (port 3306)
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress { #JENKINS (port 8080)
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }


  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "my_sg"
  }
}

resource "aws_db_instance" "mysql_db" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "mysql"
  engine_version       = "5.7" 
  instance_class       = "db.t2.micro"
  username             = "username"
  password             = "password"
  parameter_group_name = "default.mysql5.7"
  skip_final_snapshot  = true

  vpc_security_group_ids = [aws_security_group.my_sg.id]
  db_subnet_group_name   = aws_db_subnet_group.example_subnet_group.name

  tags = {
    Name = "MyMySQLDatabase"
  }
}

resource "aws_db_subnet_group" "example_subnet_group" {
  name       = "my-subnet-group"
  subnet_ids = [aws_subnet.example_subnet_1.id, aws_subnet.example_subnet_2.id, aws_subnet.example_subnet_3.id]

  tags = {
    Name = "My DB Subnet Group"
  }
}


resource "aws_instance" "CI_server_ec2" {
 ami              = var.ami
 instance_type    = "t2.micro"
 key_name         = "mykey"
 subnet_id        = aws_subnet.example_subnet.id
 security_groups  = [aws_security_group.my_sg.id]

 tags = {
  Name = "demo1"
 }
}