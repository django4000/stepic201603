#sudo apt-get install nginx
pip install gunicorn
sudo rm /etc/nginx/sites-enabled/default.conf
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default.conf
sudo /etc/init.d/nginx restart
