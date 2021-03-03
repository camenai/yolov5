from setuptools import setup, find_packages

setup(
    name='yolov5',
    version='0.0.1',
    description='My private package from private github repo',
    url='git+https://github.com/camenai/yolov5.git',
    author='Payam Azad',
    author_email='pazad@cyclomedia.com',
    license='unlicense',
    packages=['yolo', 'yolo.models', 'yolo.utils', 'yolo.utils.aws'],
    zip_safe=False
)
