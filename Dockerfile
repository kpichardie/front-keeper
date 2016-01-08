from debian:latest

run apt-get update && apt-get install -y \
    git python-pip python-virtualenv python-dev 
    run pip install django
    run git clone https://github.com/kpichardie/front-keeper.git

