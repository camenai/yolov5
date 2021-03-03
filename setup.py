from setuptools import setup, find_packages

setup(
    name='yolov5',
    version='0.0.1',
    description='My private package from private github repo',
    url='git+https://github.com/camenai/yolov5.git',
    author='Payam Azad',
    author_email='pazad@cyclomedia.com',
    license='unlicense',
    packages=['yolov5', 'yolov5.models', 'yolov5.utils', 'yolov5.utils.aws'],
    zip_safe=False
)
