#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
conf="\\\\n\tadd_header X-Served-By $HOSTNAME;"
sudo sed -i "15i $conf" /etc/nginx/nginx.conf
sudo mkdir -p /data/web_static/shared /data/web_static/releases/test
index="<html>\\n  <head>\\n  </head>\\n  <body>\\n    Holberton School\\n  </body>\\n</html>"
echo -e "$index" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '37i\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
