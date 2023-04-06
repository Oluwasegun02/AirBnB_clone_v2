#!/usr/bin/env bash
# Install Nginx if it not already installed
# Create the required folders if they don't already exist
# Create a fake HTML file for testing
# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/
# Change ownership of /data/ to ubuntu user and group
# Update Nginx configuration
# Restart nginx

if [ ! -x /usr/sbin/nginx ]; then
    apt-get update
    apt-get -y install nginx
fi

if [ ! -d "/data/" ]; then
    mkdir /data/
fi

if [ ! -d "/data/web_static/" ]; then
    mkdir /data/web_static/
fi

if [ ! -d "/data/web_static/releases/" ]; then
    mkdir /data/web_static/releases/
fi

if [ ! -d "/data/web_static/shared/" ]; then
    mkdir /data/web_static/shared/
fi

if [ ! -d "/data/web_static/releases/test/" ]; then
    mkdir /data/web_static/releases/test/
fi

echo "<html>
  <head>
  </head>
  <body>
    <h1>Nginx configuration <h1>
    <h2>Segzy say hello Alx <h2>
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
chmod -R 755 /data/
sed -i '/listen 80 default_server;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart

