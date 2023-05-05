#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static
if ! dpkg -s nginx >/dev/null 2>&1; then
  sudo apt -y update
  sudo apt -y install nginx
fi
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "<!DOCTYPE HTML>
      <html>
        <head>
        </head>
                <body>
                        Holberton School
                </body>
      </html>" | tee /data/web_static/releases/test/index.html > /dev/null
sudo rm -f /data/web_static/current
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i  '54i \\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
