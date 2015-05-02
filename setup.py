from setuptools import setup

setup(name='trackmerge',
      version='0.1.0',
      description='Tool for tracking project release versions with git.',
      url='https://github.com/andrewguy9/trackmerge',
      author='andrew thomson',
      author_email='athomsonguy@gmail.com',
      install_requires = ['docopts'],
      packages=['trackmerge'],
      scripts=['bin/ismerged'],
      zip_safe=False)
