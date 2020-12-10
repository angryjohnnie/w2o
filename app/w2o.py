from flask import Flask, jsonify

#Create a Flask constructor. It takes name of the current module as the argument
app = Flask(__name__)

#Create a route decorator to tell the application, which URL should be called for the #described function and define the function
@app.route('/hello')
def hello():
    return jsonify(app="HelloWorld")

@app.route('/')
def rootresponse():
    return jsonify(
        username="w2oguy",
        email='w2oguy@w2o.com',
        id=12345)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')