import os
import platform
from setuptools import setup
from setuptools import find_packages
from setuptools import Extension


extra_compile_args = [
    '-std=c++11',
    '-O3',
    '-Wall',
    '-Wextra',
    '-Wconversion',
    '-fno-strict-aliasing',
    '-fno-rtti',
]

if platform.system() == 'Darwin':
    extra_compile_args += ['-mmacosx-version-min=10.7', '-stdlib=libc++']

arch = os.environ['ARCHITECTURE']


ext_modules = [Extension(
        'rocksdb._rocksdb',
        ['rocksdb/_rocksdb.pyx'],
        include_dirs=[os.path.join(os.getcwd(), '..', 'rocksdb', 'include'),
                      '/usr/include/linux', '/usr/include/c++/12',
                      '/usr/include', '/usr/local/include'],
        extra_compile_args=extra_compile_args,
        extra_objects=['librocksdb.so'],
        language='c++',
        libraries=['snappy', 'bz2', 'z', 'lz4'],
    )]
for e in ext_modules:
    e.cython_directives = {'language_level': '3'}

setup(
    name="python-rocksdb",
    version='0.7.0',
    description="Python bindings for RocksDB",
    keywords='rocksdb',
    author='Ming Hsuan Tu',
    author_email="qrnnis2623891@gmail.com",
    url="https://github.com/twmht/python-rocksdb",
    license='BSD License',
    setup_requires=['setuptools>=25', 'Cython>=0.20,<3.0'],
    install_requires=['setuptools>=25'],
    package_dir={'rocksdb': 'rocksdb'},
    packages=find_packages('rocksdb'),
    ext_modules=ext_modules,
    extras_require={
        "doc": ['sphinx_rtd_theme', 'sphinx'],
    },
    include_package_data=True,
    zip_safe=False,
)
