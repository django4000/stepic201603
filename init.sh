ln -s stepic201603/web web
#sudo apt-get install nginx
sudo /etc/init.d/mysql restart
mysql -u root -e "CREATE DATABASE `db` /*!40100 DEFAULT CHARACTER SET utf8 */" 
pip install gunicorn
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/django.conf /etc/gunicorn.d/django.conf
sudo rm /etc/nginx/sites-enabled/default.conf
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default.conf
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/nginx restart
