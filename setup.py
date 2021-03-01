from setuptools import setup, find_packages

setup(
    name='yolo',
    version='0.0.1',
    description='My private package from private github repo',
    url='git+https://github.com/camenai/yolov5.git',
    author='Payam Azad',
    author_email='pazad@cyclomedia.com',
    license='unlicense',
    packages=find_packages(),
    zip_safe=False
)
