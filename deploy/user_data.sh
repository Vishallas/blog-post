#!/bin/bash
sudo yum -y update
sudo yum -y install ruby
sudo yum -y install wget
cd /home/ec2-user
wget https://aws-codedeploy-ap-south-1.s3.ap-south-1.amazonaws.com/latest/install
sudo chmod +x ./install
sudo ./install auto
sudo yum install -y python-pip
sudo pip install awscli
sudo yum install python

cat <<EOF >> /etc/systemd/system/blog_backend.service
[Unit]
Description=Blog app backend service
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=ec2-user
ExecStart=/usr/bin/python3 /var/www/myapp/app.py

[Install]
WantedBy=multi-user.target
EOF

systemctl start blog_backend.service
systemctl enable blog_backend.service