import os
from jinja2 import Environment, FileSystemLoader, PackageLoader

fileNames = ['flask_app/forms.py', 'flask_app/models.py', 'flask_app/views.py', 'flask_app/default_config.py', ]#'flask_app/__init__.py']

PATH = os.path.dirname(os.path.abspath(__file__))

env = Environment(loader=PackageLoader('flask_app', 'flask_app'))

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def createProject():
    name = 'app_name'
    for i in fileNames:
        template = env.get_template(i)
        temp = template.render(flask_app={'name': name})
        print temp
    #newFiles = [fileNames, ]

if __name__ == "__main__":
    createProject()
