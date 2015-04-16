from setuptools import setup

readme = file('README.txt')
readme_text = ''
for line in readme:
    readme_text += line

setup(name='HelloSAAO',
      version='0.2',
      url='http://www.saao.ac.za',
      description='Hello World for distribution',
      long_description=readme_text,
      packages=['saaohello', 'saaohello.world'],
      install_requires=['numpy'],
      author='Christian Hettlage',
      author_email='hettlage@saao.ac.za')
