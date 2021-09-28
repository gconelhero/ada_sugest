from flask import Flask
from flask import request, jsonify, redirect
import engine

#Create APP Object
app = Flask(__name__)

#Start Debugger, See an error of a malformed code Save File And DEBUG(console)
app.config["DEBUG"] = True

body_dict = ""

@app.route('/', methods=['GET'])
def home():
    return "<h1>OpenAI Project</h1><h3>This is a prototype...</h3><p>By Rambo and Nambo Fucker's Eq.</p>"

@app.route('/body_dict/new', methods=['GET'])
def newLists():
    return """<html><body><h1>Add New List</h1>
    <form method="POST" enctype="multipart/form-data" action="/body_dict/insert">
    <input name="titles" type="text" placeholder="Add New Titles">
    <input type="submit" value="Add"></form></body></html>"""

@app.route('/body_dict/insert', methods=['GET', 'POST'])
def insertList():
    global body_dict
    body_dict = ""
    user = request.form['titles']
    body_dict += user
    
    if body_dict != "":
        href_response = engine.title(body_dict)
        print(href_response)
        
        if len(href_response) > 1:
            href_response = ' , '.join(href_response)
        elif len(href_response) == 1:
            href_response = href_response[0]
        elif href_response == []:
            href_response = "SORRY... NOT RESULT...TRY AGAIN"
    
    return href_response

@app.route('/body_dict/all', methods=['GET'])
def bodyDict():
    return body_dict

app.run(host='0.0.0.0', port='5000')
