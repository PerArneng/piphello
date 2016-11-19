from setuptools import setup

setup(name='pip_hello',
      version='0.1',
      description='Hello World From PiP',
      url='https://github.com/PerArneng/piphello',
      author='Per Arneng',
      author_email='per.arneng@scalebit.com',
      license='APACHE 2.0',
      packages=['hello', 'resources'],
      entry_points = {
            'console_scripts': ['pip_hello=hello.hello:main'],
      },
      package_data={
          "resources": [
              "*.txt",
          ],
      },
      include_package_data=True,
      zip_safe=False)