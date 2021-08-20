YOLOv3-Swagger
===
Use swagger framework unit tests for yolov3 object detection

* python = 3.6.9
* torch = 1.2.0


# Swagger-ui 
--------------------------------

![alt text](https://github.com/yanxi853600/Yolov3-pytorch/blob/master/git_img/1.PNG)

# 1 . Get Method : 
> [Note] Get the name of your model and confirm if it has been uploaded.

![alt text](https://github.com/yanxi853600/Yolov3-pytorch/blob/master/git_img/2.PNG)


# 2 . Post Method : 
> [Note] Confirm your model name and upload the image file.

![alt text](https://github.com/yanxi853600/Yolov3-pytorch/blob/master/git_img/3.PNG)


> [Note]  Floating lock pass and fail classification of object detection
![alt text](https://github.com/yanxi853600/Yolov3-pytorch/blob/master/images/2f464286-8235-11eb-b54e-c400ad491c49.png)

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

