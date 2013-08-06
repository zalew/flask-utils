import os
from setuptools import setup, find_packages
from flask_utils import VERSION, DEV_STATUS

setup(
    name='flask-utils',
    version='.'.join(map(str, VERSION)),
    description='Various Flask utilities.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    keywords='flask utils',
    author='Jakub Zalewski',
    author_email='zalew7@gmail.com',
    url='https://bitbucket.org/zalew/flask-utils',
    license='MIT license',
    packages=find_packages(),
    zip_safe=False,
    package_data = {
        'flask_utils': [],
    },
    classifiers=[
        'Development Status :: %s' % DEV_STATUS,
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
	'Programming Language :: Python :: 2',
        'Framework :: Flask',
    ],
    install_requires=[
        'flask',
	'jinja2',
    ],    
)
