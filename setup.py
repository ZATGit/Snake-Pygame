try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'A recreation of the Snake arcade game',
    'author':'Zach Trembly',
    'url':'github.com/ZATGit',
    'download_url':'https://github.com/ZATGit/snake_pygame',
    'author_email':'mail@zachtrembly.com',
    'version':'0.1',
    'license':'MIT',
    'install_requires':['pygame'],
    'packages':['snake_pygame'],
    'scripts':[],
    'name':'Snake Pygame'
}

setup(**config)