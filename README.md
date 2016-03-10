# front-keeper
Front-keeper is a basic web interface for passkeeper

This one user interface permit to manage passkeper throught a simple web interface. 

It include feacture : 

- Init : Initialize your git passkeeper project 
- Decrypt : Decrypt files encrypted using passkeeper
- Encrypt : Encrypt files password
- List : List all ini password files
- New : Add new ini password file
- Search : Search a content in your ini files

Configuration in settings.py :

PASSKEEPER_PATH : Path of the passkeeper directory (could permit to integrate an initialied one)

PASSKEEPER_ENCRYPT_STATE : Default encryption state of passkeeper (True : encrypted, False : decrypted)

-- INSTALL --

#Install prerequisite passkeeper 
apt-get install git python-pip git -y

pip install git+git://github.com/shaftmx/passkeeper -r https://raw.githubusercontent.com/shaftmx/passkeeper/master/requirements.txt --upgrade

#Install Frontkeeper
# cd /var/www

pip install django

git clone https://github.com/kpichardie/front-keeper.git

# Start Server
/usr/bin/python manage.py runserver 0.0.0.0:8080

-- NGINX CONF --

server {
     listen 80;

     server_name frontkeeper.example.com

     keepalive_timeout 5;

     root /var/www/front-keeper/frontkeeper;

     location / {
       # checks for static file, if not found proxy to app
       try_files $uri @proxy_to_app;
     }
     location @proxy_to_app {
       proxy_redirect off;
       proxy_pass http://127.0.0.1:8080;
     }

    access_log /var/log/nginx/access_frontkeeper.log;
    error_log /var/log/nginx/error_frontkeeper.log;
}

-- DOCKER --

# Build image
docker build -t frontkeeper .

# Don't forget to change the path of passkeeper in configuration
# Run frontkeeper /usr/bin/python manage.py runserver 0.0.0.0:8080

NB : Insure your frontkeeper is encrypted if it's not new one, by default passkeeper consider it's on encrypted state. You can also change it in settings.
