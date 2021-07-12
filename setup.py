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
        # todo
        #  This is copied from the requirements.txt,
        #  which is usually not what you want to do
        #  We might be able to refine this later.

        # base ----------------------------------------
        'Cython',
        'matplotlib>=3.2.2',
        'numpy>=1.18.5',
        'opencv-python>=4.1.2',
        'Pillow',
        'PyYAML>=5.3.1',
        'scipy>=1.4.1',
        'tensorboard>=2.2',
        'torch>=1.7.0',
        'torchvision>=0.8.1',
        'tqdm>=4.41.0',

        # logging -------------------------------------
        'wandb',

        # plotting ------------------------------------
        'seaborn>=0.11.0',
        'pandas',

        # export --------------------------------------
        # coremltools>=4.1
        # onnx>=1.8.1
        # scikit-learn==0.19.2  # for coreml quantization

        # extras --------------------------------------
        'thop',  # FLOPS computation
        'pycocotools>=2.0',  # COCO mAP
    ],
)
