#! /bin/bash
cd /var/www/myapp
pip install -r requirements.txt

systemctl restart blog_backend