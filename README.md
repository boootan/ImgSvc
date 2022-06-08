# RESTImgSvc
## By Sonny Tan
- sonnythemantan@csu.fullerton.edu

REST image service to return image based on ID number/other key.

Based on application that will provide ID number of image to lookup, as well as a SHA-1 hash of the ID Number concatenated with an API key that is shared between the application and the endpoint on the image repository.

This service is intended to run on a web server such as IIS or Apache in order to ensure availability for a production environment. 

Can point to mapped drive on server, Dropbox, wherever image repository exists. Easier to configure if image repo is Windows/Linux filesystem.

IIS Configuration Documentation: https://medium.com/@bilalbayasut/deploying-python-web-app-flask-in-windows-server-iis-using-fastcgi-6c1873ae0ad8

# Testing
Flask has a built in development HTTP listener, it will run on the port of your choice (usually 5000 or 8000) in order to do testing. I have included a random key generator (keygen.py) and hash computer (hashcomputer.py) that you can edit to include your ID and key, and compute the hash to make the GET request.
The request will look something like https://college.domain/img?IdNumber=123456789&hash={hash}

REQUIRED: Generic image to display if picture not found: generic.jpg


# Tools Used
- Python (Flask, hashlib)
- Apache WebServer/Microsoft Internet Information Services
