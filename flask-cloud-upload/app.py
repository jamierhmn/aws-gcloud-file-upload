from flask import Flask,flash, render_template, request, redirect
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from .aws_upload import upload_file_to_s3
from .gloud_upload import Gcloud_upload_file
import os,glob
app     = Flask(__name__)
app.config.from_pyfile("config.py")

UPLOAD_FOLDER = "uploads"
def allowed_file(filename,storage):
    if(storage=='AWS'):
       return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config["ALLOWED_EXTENSIONS_IMG_MEDIA"]
    elif(storage=='gcloud'):
       return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config["ALLOWED_EXTENSIONS_DOC"]
           
           
           
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_from_UI():
    
    if request.method == 'POST':
        # che   ck if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        print("filename=",file.filename)
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename,"aws"):
           print("file name inside the folder" )
           file.filename = secure_filename(file.filename)
           filepath=os.path.join("./uploads/media/", file.filename)
           print("filepath in uploadfromUI=",filepath)
           output=upload_file_to_s3(filepath,file.filename,app.config["S3_BUCKET"], app.config["S3_SECRET"],app.config["S3_KEY"])
           return str(output)
    
    else:
        return redirect("/")
        
        
#Transfer file from local system  to AWS 
@app.route("/load_media_aws", methods=["POST"])
def upload_local_media_aws():
   files_to_tansfer = glob.glob("./uploads/media/**/*.*",recursive = True)
   print("files to transfer aws =",files_to_tansfer)
   for filepath in files_to_tansfer:
      filename=os.path.basename(filepath)
      print("working on filename=",filename)
      if allowed_file(filename,"aws"):
         #upload to AWS cloud ,method defined in helpers.py
          output=upload_file_to_s3(filepath,filename,app.config["S3_BUCKET"], app.config["S3_SECRET"],app.config["S3_KEY"])  
   #List of file transfer can be           
   return ("sucessfully transfered")     

#Transfer file from local system  to Gcloud 
@app.route("/load_doc_gcloud", methods=["POST"])
def upload_local_doc_gcloud(): 
    files_to_tansfer = glob.glob("./uploads/doc/**/*.*",recursive = True)
    print("files to transfer gcloud =",files_to_tansfer)
    for filepath in files_to_tansfer:
      filename=os.path.basename(filepath)
      
      if allowed_file(filename,"gcloud"):
         #called Gcloud method defined in helpers.py for uploading file
          Gcloud_upload_file(filename)
    return("successful")
    
if __name__ == "__main__":
    app.run()