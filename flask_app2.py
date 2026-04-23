from flask import Flask, redirect, render_template
import instantgram
app = Flask(__name__)

@app.route('/listpictures')
def listpictures():
    results=instantgram.list_pictures()
    return {'results': results}

@app.route('/uploadpicture', methods=['POST'])
def uploadfile():
    return instantgram.upload_picture()