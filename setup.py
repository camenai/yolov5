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
    zip_safe=False,
    install_requires=[
        'Cython',
        'matplotlib>=3.2.2'
        'numpy>=1.18.5'
        'opencv-python>=4.1.2'
        'Pillow'
        'PyYAML>=5.3.1'
        'scipy>=1.4.1'
        'tensorboard>=2.2'
        'torch>=1.7.0'
        'torchvision>=0.8.1'
        'tqdm>=4.41.0'
    ],
)
