#sudo apt-get install nginx
pip install gunicorn
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo rm /etc/nginx/sites-enabled/default.conf
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default.conf
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/nginx restart
