from setuptools import setup


#REQUIRED_PACKAGES = ['Pillow>=1.0', 'Matplotlib>=2.1', 'Cython>=0.28.1']
REQUIRED_PACKAGES = ['pyqt5','sklearn']


setup(name='AIHubdatashop',
      version='1.0.0',
      description='A print test for PyPI',
      author='',
      author_email='win@163.com',
      url='https://www.python.org/',
      license='MIT',
      keywords='AIHub',
      project_urls={
            #'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
            #'Funding': 'https://donate.pypi.org',
            #'Source': 'https://github.com/pypa/sampleproject/',
            #'Tracker': 'https://github.com/pypa/sampleproject/issues',
      },
      packages=['datashop'],
      install_requires=REQUIRED_PACKAGES,
      python_requires='>=3'
     )