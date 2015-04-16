from distutils.core import setup

readme = file('README.txt')
readme_text = ''
for line in readme:
    readme_text += line

setup(name='Hello SAAO',
      version='0.1',
      url='http://www.saao.ac.za',
      description='Hello World for distribution',
      long_description=readme_text,
      packages=['saaohello', 'saaohello.world'],
      author='Christian Hettlage',
      author_email='hettlage@saao.ac.za',

      )