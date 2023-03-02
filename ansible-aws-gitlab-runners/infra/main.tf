terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 4.38.0"
    }
  }
}

provider "aws" {
  region = local.region
}


locals {
  name             = "gitlab-runner"
  region           = "eu-central-1"
  vpc_id           = "vpc-0d8d5538112eedd18"
  subnet_id        = "subnet-040da219a6ce27dd5"
  ami              = "ami-0a5b5c0ea66ec560d"
  ssh_user         = "admin"
  key_name         = "mykey"
  private_key_path = "~/.aws/pems/mykey.pem"
}


resource "aws_security_group" "main" {
  name   = "${local.name}-sg"
  vpc_id = local.vpc_id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "main" {
  ami                         = local.ami
  subnet_id                   = local.subnet_id
  instance_type               = "t2.micro"
  associate_public_ip_address = true
  vpc_security_group_ids      = [aws_security_group.main.id]
  key_name                    = local.key_name

  user_data                   = <<EOF
    #!/bin/bash
    touch ~/log.txt
  EOF

  lifecycle {
    ignore_changes = [user_data]
  }
}

resource "null_resource" "main" {
  triggers = {
    always_run = "${timestamp()}"
  }

  provisioner "local-exec" {
    command = "ansible-playbook -i ${aws_instance.main.public_ip}, --private-key ${local.private_key_path} ../playbook.yml"
  }
}

output "runner_ip" {
  value = aws_instance.main.public_ip
}