from setuptools import setup

setup(
  name = 'domny',
  version = '1.0.0',
  author = 'Danilo Matrangolo Marano',
  author_email = 'danilo.m.marano@gmail.com',
  license = 'LGPLv3',
  url = 'https://github.com/danilommarano/domny',
  description = 'Dominate is a Python library for creating and manipulating HTML documents using an elegant DOM API.',
  long_description = '',
  long_description_content_type = 'text/markdown',
  keywords = 'templating template html htmx python html5',
  python_requires='',
  classifiers = [
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Text Processing :: Markup :: HTML',
  ],
  packages = ['domny'],
  include_package_data = True,   
)