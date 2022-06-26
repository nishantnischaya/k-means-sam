import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='kmeans_sam',  
     version='0.1',
     scripts=['kmeans_sam'] ,
     author="Nishant Nischaya",
     author_email="nishantnischaya@gmail.com",
     description="A package for creating subclusters of KMeansSam clusters and merging them with great flexibilty",
     long_description=long_description,
    long_description_content_type="text/markdown",
     url="https://github.com/nishantnischaya/k-means-sams",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )