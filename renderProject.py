import sys
from jinja2 import Environment, FileSystemLoader

appName = 'flask_app'
fileNames = ['__init__.py', 'forms.py', 'models.py', 'views.py', 'default_config.py']


def fileWrite(appName, fileName):
    env = Environment(loader=FileSystemLoader(appName))
    template = env.get_template(fileName)
    output = template.render(flask_app={'name': appName})
    with open(appName + '/' + fileName, 'wb') as f:
        f.write(bytes(output, 'UTF-8'))

#    print(output)

if __name__ == "__main__":
    appName = sys.argv[1]
    for i in fileNames:
        fileWrite(appName, i)
