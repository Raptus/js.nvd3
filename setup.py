from setuptools import setup, find_packages

version = '0.0.1'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='js.nvd3',
      version=version,
      description="Fanstatic package for NVD3.js http://nvd3.org/",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Raptus AG',
      author_email='dev@raptus.com',
      url='https://svn.raptus.com/svn/public/projects/horae/eggs/js.nvd3',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'js.d3',
      ],
      entry_points={
          'fanstatic.libraries': [
              'js.nvd3 = js.nvd3:library',
          ]
      })
