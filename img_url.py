import cloudinary
import cloudinary.uploader
import cloudinary.api

from fastapi import FastAPI, File, UploadFile

# Import the CloudinaryImage and CloudinaryVideo methods for the simplified syntax used in this guide
from cloudinary import CloudinaryImage

app = FastAPI()

cloudinary.config(
  cloud_name = "dbv678kfe",
  api_key = "318863461112866",
  api_secret = "wBPt_7gFaUYnphtcgVCAVXBhx4c",
  secure = True
)


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile=File(...)):

    # uploading file to cloudinary server
    upload_result = cloudinary.uploader.upload(file.file)

    # Return the URL of the uploaded image
   

    return {"img_url": upload_result["secure_url"]}