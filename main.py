import sys
import uvicorn
from enum import Enum
from typing import Optional
from Inference.errors import Error
from Inference.exceptions import ModelNotFound, InvalidModelConfiguration, ApplicationError, ModelNotLoaded, \
	InferenceEngineNotFound, InvalidInputData
from Inference.response import ApiResponse
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form, File, UploadFile, Header, Query
import argparse
from detection import run
from pydantic import BaseModel
from base64 import b64decode, b64encode
import numpy as np
from PIL import Image
import io
import sys
import base64

#####################################################
# 	API Release Information (http://127.0.0.1:5555/docs)
#####################################################
app = FastAPI(version="1.0.0", title='Yolov3 inference Swagger',
			  description="<b>API for performing YOLOv3 inference.</b></br></br>"
						  "<b>Contact the developers:</b></br>"
						  "<b>Yanxi.Lin: <a href='mailto:Yanxi.Lin@advantech.com.tw'>Yanxi.Lin@advantech.com.tw</a></b></br>"
			 )
#####################################################
#	CORS Setting
#####################################################
# app.mount("/public", StaticFiles(directory="/main/public"), name="public")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
	max_age=180,	#	timout (second)
)
#####################################################
#	Define Class Object
#####################################################
error_logging = Error()
#yolov3_model = yolov3(args.num_class, args.anchors)
class ModelName(str, Enum):
    yolov3 = "yolov3"
	

#####################################################
#	Implement multiple interface on Swagger API.
#####################################################
#	Loaded yolov3 model
#####################################################
@app.get('/load/{model_name}', tags=["GET Method"])
async def get_model(model_name: ModelName):
	"""
	Loads all the available models.\n
	Returns all the available models with their respective hashed values.
	"""
	try:
		yolov3_model = run.load_model()
		error_logging.info('request successful;')
		return ApiResponse(success=True, data='yolov3 is loading',)

	except ApplicationError as e:
		error_logging.warning(str(e))
		return ApiResponse(success=False, error=e)

	except Exception as e:
		error_logging.error(str(e))
		return ApiResponse(success=False, error='unexpected server error')


#####################################################
#	Detect an image using yolov3
#####################################################
@app.post('/detect', tags=["POST Method"])
async def predict_image(model_name: ModelName, file: UploadFile = File(...)):

	"""
	Performs a prediction for a specified image using YOLOv3 models.\n
	param model: Model_name 
	Param image: Image file.\n
	Return: Model's Bounding boxes.
	"""
	try:
		image = await file.read()
		image = Image.open(io.BytesIO(image))
		boxes = run.inferenceYoLo(image)
		error_logging.info('request successful;' + str(boxes))
		return boxes

	except ApplicationError as e:
		error_logging.warning(str(e))
		return ApiResponse(success=False, error=e)

	except Exception as e:
		error_logging.error(str(e))
		return ApiResponse(success=False, error='unexpected server error')


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", debug=True)
