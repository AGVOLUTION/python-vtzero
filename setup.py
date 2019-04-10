import os

from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

os.environ["CC"] = 'clang++'

ext_options = {
    'include_dirs': ['./vendor/vtzero/include', './vendor/protozero/include'],
    'extra_compile_args': ['-O2', '-std=c++14']
}
ext_modules = cythonize([
    Extension('vtzero.tile', ['vtzero/tile.cpp'], **ext_options)
])

setup(
    name='vtzero',
    version='0.0.1',
    description='Python wrapper for vtzero C++ library.',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX',
        'Environment :: Web Environment',
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Scientific/Engineering :: GIS'
    ],
    keywords='mvt mapbox vector tile gis',
    platforms=['POSIX'],
    author='Yohan Boniface',
    author_email='yohan.boniface@data.gouv.fr',
    license='MIT',
    packages=['vtzero'],
    ext_modules=ext_modules,
    provides=['vtzero'],
    include_package_data=True
)