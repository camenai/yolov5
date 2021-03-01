from setuptools import setup, find_packages

setup(
    name='yolo',
    version='0.0.1',
    description='My private package from private github repo',
    url='git+https://github.com/camenai/yolov5.git',
    author='Payam Azad',
    author_email='pazad@cyclomedia.com',
    license='unlicense',
    packages=['yolo', 'yolo.models', 'yolo.utils', 'yolo.utils.aws', 'yolo.models.common', 'yolo.models.expermental',
              'yolo.models.yolo', 'yolo.models.export', 'yolo.utils.datasets', 'yolo.utils.general',
              'yolo.utils.metrics'],
    zip_safe=False
)
