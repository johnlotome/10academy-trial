from flask import Flask,render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    title = 'Home'
    return render_template('home.html',title=title)

@app.route('/about',methods=['GET'])
def about():
    return "<h1>About Page</h1>"

if __name__=='__main__':
    app.run(host='localhost',port=3333,debug=True)