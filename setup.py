import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hostel_dues_nitc",
    version="1.0.0",
    author="Sandeep",
    author_email="sandeepg.97@gmail.com",
    description="Hostel & Mess dues retriever for NITC students",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sndp487/hostel_dues_nitc",
    packages=setuptools.find_packages(),
    install_requires=["PyPDF2","requests"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
