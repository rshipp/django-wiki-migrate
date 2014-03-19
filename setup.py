import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

requirements = open(os.path.join(os.path.dirname(__file__),
            'requirements.txt')).read()
requires = requirements.strip().split('\n')

setup(
    name='django-wiki-migrate',
    version='0.1',
    packages=['django_wiki_migrate'],
    include_package_data=True,
    install_requires=requires,
    license='BSD New',
    description='Migrate content from your old wiki to django-wiki.',
    long_description=README,
    url='https://github.com/george2/django-wiki-migrate',
    author='george2',
    author_email='rpubaddr0@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)
