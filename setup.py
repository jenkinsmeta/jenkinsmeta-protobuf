from setuptools import setup

setup(name='jenkinsmeta_pb2',
      version='0.0.1',
      description='Protocol (based on protobuf2) for Jenkinsmeta',
      url='https://github.com/jenkinsmeta/jenkinsmeta-protobuf.git',
      author='Maciej Kasprzyk',
      author_email='mkasprzyk@szy.fr',
      license='MIT',
      packages=['jenkinsmeta_pb2'],
      install_requires = ['protobuf==2.6.1'],
      zip_safe=False)
