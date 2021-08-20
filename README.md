YOLOv3-Swagger
===
Use swagger framework unit tests for yolov3 object detection

* python = 3.6.9
* torch = 1.2.0


# Swagger-ui 
--------------------------------

![alt text](https://dev.azure.com/SE-Develop/6c9779dc-21a0-4509-ae29-f440d2e5d1db/_apis/git/repositories/1e3b088c-a5f0-4abc-90d2-40f2674d839c/items?path=%2Fgit_img%2F1.PNG&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0)

# 1 . Get Method : 
> [Note] Get the name of your model and confirm if it has been uploaded.

![alt text](https://dev.azure.com/SE-Develop/6c9779dc-21a0-4509-ae29-f440d2e5d1db/_apis/git/repositories/1e3b088c-a5f0-4abc-90d2-40f2674d839c/items?path=%2Fgit_img%2F2.PNG&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0)


# 2 . Post Method : 
> [Note] Confirm your model name and upload the image file.

![alt text](https://dev.azure.com/SE-Develop/6c9779dc-21a0-4509-ae29-f440d2e5d1db/_apis/git/repositories/1e3b088c-a5f0-4abc-90d2-40f2674d839c/items?path=%2Fgit_img%2F3.PNG&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0)


> [Note]  Floating lock pass and fail classification of object detection
![alt text](https://dev.azure.com/SE-Develop/6c9779dc-21a0-4509-ae29-f440d2e5d1db/_apis/git/repositories/1e3b088c-a5f0-4abc-90d2-40f2674d839c/items?path=%2Fimages%2F7214ebba-8235-11eb-a959-c400ad491c49.png&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0)

# Installation
--------------------------------

### Clone and install requirements
```
git clone 
cd Yolov3-Swagger/
pip install -r requirements.txt
```

### Run the server:
```
cd Yolov3-Swagger/
uvicorn main:app --port [5050]
```
> Go to http://127.0.0.1:5050/docs


 # Folder Structure 
---------------------------------


    $ Yolov3-Swagger
    $ |── detection
    $ |     └── cfg
    $ |     └── darknet
    $ |     └── data
    $ |     └── utils
    $ |     └── weights
    $ |     └── run.py
    $ |── git_img
    $ |── images
    $ |── inference
    $ |     └── base_error.py
    $ |     └── errors.py
    $ |     └── exceptions.py
    $ |     └── response.py
    $ |── logs
    $ |── main.py
    $ |── README.md
    $ |── requirements.txt

