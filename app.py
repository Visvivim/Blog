from flask import Flask ,render_template,request,redirect,url_for

app = Flask(__name__)


#@app.route('/')

if __name__ == '__mian__':
    app.run(debug=True,host='0.0.0.0',port=8000)