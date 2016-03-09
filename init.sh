#sudo apt-get install nginx
sudo rm /etc/nginx/sites-enabled/default.conf
sudo ln -s web/etc/nginx.conf  /etc/nginx/sites-enabled/default.conf
sudo /etc/init.d/nginx restart
