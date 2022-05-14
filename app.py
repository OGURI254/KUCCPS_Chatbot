from flask import Flask, render_template, request, jsonify 

from chat import get_response

app = Flask(__name__)

def index_get():
    return render_template()
#@app.route("/",methods = ["GET"]) // old method
@app.get("/")
def index_get():
    return render_template("base.html")
"""""
@app.route('/predicts', methods=['GET', 'POST'])
def predicts():
   if request.method == 'POST':
       # do something
   else:
       # show the form
       return render_template('predicts.html')"""""
   

@app.post("/predicts")
def predict():
    text =request.get_json().get("message")
    #im supposed to check if the message is valid
    response =  get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug = True)