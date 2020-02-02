from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask import jsonify, request
import os
import microphoneTranscript
import driver

import wget

from flask import send_from_directory

import urllib.request

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.getcwd()

THE_URL = ""
voiceOut = ""

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif',
                      'mp4', 'mp3', 'mkv'}

app = Flask(__name__)
Bootstrap(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("home.html")
    #urllib.request.urlopen("http://127.0.0.1:5000/upload")
    
@app.route('/loading')
def loading():

    time_stamp_array = driver.get_timestamps( voiceOut )
    header = "We found " + str(len(time_stamp_array)) + " instances of " + voiceOut
    return render_template("end.html", array = time_stamp_array, video_url = THE_URL, header = header)

@app.route('/mic')
def recording_link():
    voice_command = microphoneTranscript.listen_mic()

    #voiceOut = voice_command
    #urllib.request.urlopen("http://127.0.0.1:5000/loading")
    #return render_template("test.html")

    time_stamp_array = driver.get_timestamps( voice_command )
    header = "We found " + str(len(time_stamp_array)) + " instances of " + voice_command
    return render_template("end.html", array = time_stamp_array, video_url = THE_URL, header = header)

@app.route('/boot')
def bootstrap():
    print("Bootstrap test")
    return render_template("test.html")

##@app.route('/upload')
##def upload_file():
##   return render_template('upload.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/getValues')
def downloadURL():
    url = request.args.get('url')


    THE_URL = url

    print("SUCESS: " + THE_URL)

    file_name = wget.download(url)

    driver.upload_file( file_name )

    print("file name: ", file_name)
    
    return render_template("test.html")
    


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
##    return '''
##    <!doctype html>
##    <title>Upload new File</title>
##    <h1>Upload new File</h1>
##    <form method=post enctype=multipart/form-data>
##      <input type=file name=file>
##      <input type=submit value=Upload>
##    </form>
##    '''
    return render_template('home.html')

@app.route('/uploads/<filename>', methods=['GET', 'POST'])
def uploaded_file(filename):
    print("filename: ", filename)
    url = os.getcwd() + '/' + filename
    print("ur: ", url)
    app.config['UPLOAD_FOLDER']
    #return send_from_directory(app.config['UPLOAD_FOLDER'],
                               #filename)
    #return render_template('playing.html', video_url=url)
    return render_template('playing.html')


##@app.route('/uploads/<filename>')
##def uploaded_file(filename):
##    print(filename)
##    print( app.config['UPLOAD_FOLDER'],
##    filename )
##    return render_template('home.html')



##@app.route('/uploads/<filename>')
##def uploaded_file(filename):
##    return render_template('playing.html')


    
if __name__=="__main__":
##    app.run(host=os.getenv('IP', '0.0.0.0'), 
##            port=int(os.getenv('PORT', 4444)))

    app.run()
