from flask import Flask,request,render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route("/user/<id>",methods=['GET'])
def user(id):
    return "id is:"+id

@app.route("/query_user",methods=['GET'])
def queryUser():
    return "query_user,id is:"+request.args.get('id')
