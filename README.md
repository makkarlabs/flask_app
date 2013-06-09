Sample Flask App
================

This uses flask-security, SQLAlchemy, reCaptcha, bcrypt a few more libraries.
We usually use a mysql database.

Steps : 
-------

1. Clone this repo, remove the .git files using the following command so that you can push your new project to a different repo.
```rm -rf `find ./ -type d -name .git` ```

2. Change the name, requirements, config according to your needs and start your new project!

3. To install the requirements do 
``` pip install -r requirements.txt```

4. To run the app locally, do
``` python runserver.py ```


5. To deploy on server we reccommend using 'uWSGI' and 'nginx'

Happy Coding!
Team MakkarLabs
makkarlabs.in
