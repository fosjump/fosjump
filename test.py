import yaml
from markdown import markdown
from jinja2 import Environment, Template, FileSystemLoader
from time import sleep
import os

def renderIndex():
    f = open('projects.yml')
    dataMap = yaml.safe_load(f)
    f.close()

    templateLoader = FileSystemLoader( searchpath="." )
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_template("index.base.html")
    rendered = template.render(links=dataMap, landing=True)

    result = open('output/index.html', 'w')
    result.write(rendered)
    result.close()


def renderContrib():
    f = open('contribute.md')
    contribute = f.read()
    contribute = markdown(contribute)
    f.close()

    templateLoader = FileSystemLoader(searchpath=".")
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_template("contrib.base.html")
    rendered = template.render(markdown=contribute)

    result = open('output/contrib.html', 'w')
    result.write(rendered)
    result.close()


def renderOther():
    f = open('other.yml')
    other = yaml.safe_load(f)
    f.close()

    templateLoader = FileSystemLoader(searchpath=".")
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_template("other.base.html")
    rendered = template.render(otherData=other)

    result = open('output/other.html', 'w')
    result.write(rendered)
    result.close()


if __name__ == "__main__":
    os.system("cp projectImages/* output/images/projects/")
    while(1):
        renderIndex()
        renderContrib()
        renderOther()
        sleep(5)

# Might wanna add a simple http server
