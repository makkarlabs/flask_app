#/bin/bash

echo "Enter a name for your project: "
read appName

mv flask_app $appName
mkdir $appName/logs
touch $appName/logs/error.log

sudo pip install virtualenv
python3 renderProject.py $appName
