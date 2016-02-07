from setuptools import setup

setup(name='numparse164',
      version='0.2',
      description='Parse telephone numbers',
      url='http://github.com/binzcodes/numparse164',
      author='Ryan Binns',
      author_email='binz@binz.codes',
      license='GNU',
      packages=['numparse164'],
      install_requires=[
          'phonenumbers',
      ],
      zip_safe=False)