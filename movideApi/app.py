from flask import Flask, request, Response
from contents.asilmedia import asilmedia
from contents.uzmovie import uzmovie
from contents_downloader.asilmedia import asilemdiaDow


app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def home_page():
    return {
        "code":200,
        "message":"sucsess"
    }
    
@app.route('/<string:q>/<int:p>')
def home(q, p):
    dataAsilmedia = asilmedia(q, p)
    return dataAsilmedia

@app.route('/downoad/<string:url>')
def download(url):
    data = asilemdiaDow(url)
    return data




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)