# Front-keeper
Front-keeper is a basic web interface for passkeeper

This one user interface permit to manage passkeper throught a simple web interface. 

- Home : Frontkeeper home page 
![ScreenShot](https://raw.github.com/kpichardie/front-keeper/master/Screenshots/Home.png)
- Init : Initialize your git passkeeper project 
![ScreenShot](https://raw.github.com/kpichardie/front-keeper/master/Screenshots/Init.png)
- Decrypt : Decrypt files encrypted using passkeeper
![ScreenShot](https://raw.github.com/kpichardie/front-keeper/master/Screenshots/Decrypt.png)
- Encrypt : Encrypt files password
![ScreenShot](https://raw.github.com/kpichardie/front-keeper/master/Screenshots/Encrypt.png)
- List : List all ini password and raw files, allow to remove files
![ScreenShot](https://raw.github.com/kpichardie/front-keeper/master/Screenshots/List.png)
- New : Add new ini password file
![ScreenShot](https://raw.github.com/kpichardie/front-keeper/master/Screenshots/New.png)
- Search : Search a content in your ini files
![ScreenShot](https://raw.github.com/kpichardie/front-keeper/master/Screenshots/Search-1.png)
![ScreenShot](https://raw.github.com/kpichardie/front-keeper/master/Screenshots/Search-2.png)
- Flush : Flush the git history of the changes on your passwords and flush Front-keeper logs
![ScreenShot](https://raw.github.com/kpichardie/front-keeper/master/Screenshots/Flush.png)
- Clean : Remove all files decrypted (used when you decrypt to search password then want to close without to encrypt. It remove all decrypted as you haven't made modification) Could be equivalent to quit

Configuration in settings.py :

PASSKEEPER_PATH : Path of the passkeeper directory (could permit to integrate an initialied one)

PASSKEEPER_ENCRYPT_STATE_FILE : Encryption state file name, if exist then passkeeper password are encrypted.

DISABLE_INIT : Default value is false, when your passkeeper is init no need to init again so you can disable it.

## MANUAL INSTALL 

```
# cd /var/www
apt-get install python-pip git -y
pip install -r https://raw.githubusercontent.com/kpichardie/front-keeper/master/requirements.txt
git clone https://github.com/kpichardie/front-keeper.git
# Change SECRET_KEY for frontkeeper settings in frontkeeper/frontkeeper/settings.py
# use `pwgen -sy 50 1` to generate pass (avoid "'" in key)
```

### Manually Start Server

```/usr/bin/python manage.py runserver 0.0.0.0:8080```

### Supervisor Install

```
apt-get install supervisor -y
cp front-keeper/supervisor-frontkeeper.conf /etc/supervisor/conf.d/frontkeeper.conf
service supervisor restart
```

## Ansible deploy

Please first configure secret_key in ansible/roles/frontkeeper/vars/main.yml

### Without nginx managed 

```ansible-playbook site.yml```

### With nginx managed

```ansible-playbook site.yml -e "manage_nginx=True"```

## NGINX CONFIG EXAMPLE

```
server {
     listen 80;

     server_name frontkeeper.example.com

     keepalive_timeout 5;

     root /var/www/front-keeper/frontkeeper;

     location / {
       # checks for static file, if not found proxy to app
       try_files $uri @proxy_to_app;
     }

     location /static {
       # checks for static file, if not found proxy to app
       autoindex on;    
       root /var/www/front-keeper/frontkeeper/frontkeeper;
     }

     location @proxy_to_app {
       proxy_redirect off;
       proxy_pass http://127.0.0.1:8080;
     }

    access_log /var/log/nginx/access_frontkeeper.log;
    error_log /var/log/nginx/error_frontkeeper.log;
}
```

## DOCKER

### Build image

```
docker build -t frontkeeper .

# Don't forget to change the path of passkeeper in configuration
# Run frontkeeper /usr/bin/python manage.py runserver 0.0.0.0:8080
```
NB : Insure your frontkeeper is encrypted if it's not new one, by default passkeeper consider it's on encrypted state. You can also change it in settings.
