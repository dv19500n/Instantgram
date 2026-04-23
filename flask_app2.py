from flask import Flask, redirect, render_template
import instantgram
app = Flask(__name__)

def listpicturespublic():
    results=instantgram.list_pictures_public()
    return {'results': results}

@app.route('/uploadpicturepublic', methods=['POST'])
def uploadfilepublic():
    return instantgram.upload_picture_public()
