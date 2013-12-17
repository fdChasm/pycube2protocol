import setuptools

packages = [
    'cube2protocol',
    'cube2protocol.sauerbraten',
    'cube2protocol.sauerbraten.collect',
]

setuptools.setup(
    name="pycube2protocol",
    version="0.1",
    packages=packages,
    package_dir={'' : 'src'},
    install_requires=['pycube2common'],
    author="Chasm",
    author_email="fd.chasm@gmail.com",
    url="https://github.com/fdChasm/pycube2protocol",
    license="MIT",
    description="Collection of Python tools for reading and writing data streams for games built with the cube 2 engine.",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English"
    ],
)
