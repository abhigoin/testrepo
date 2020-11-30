import setuptools

setuptools.setup(
    name="abhishek_package", # Replace with your own username
    version="0.0.1",
    author="Abhishek Sinha",
    author_email="abhigoin@gmail.com",
    description="A small example package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)