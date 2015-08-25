from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='sft',
      version='0.1',
      description='Parameterized fft supporting custom weights',
      long_description=readme(),
      classifiers=[
        'Programming Language :: Python :: 3.4',
        'Topic :: Signal Processing :: fft',
      ],
      keywords='fft radioGIS dft',
      url='http://github.com/98789/sft',
      author='Jesús Muñoz',
      author_email='jmunoz@radioGIS.uis.edu.co',
      packages=['sft'],
      include_package_data=True,
      zip_safe=False)
