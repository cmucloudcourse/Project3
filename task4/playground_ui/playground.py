from flask import Flask, request

pythonServiceHostName = "http://<ip>";

app = Flask(__name__, static_folder='site', static_url_path='')

@app.route("/", methods=['GET'])
def handle():
    return app.send_static_file("index.html")

@app.route("/python", methods=['GET', 'POST'])
def handlePython():
    if request.method == 'POST':
        code = request.form['code']
        print(code);
        # This should return the stdout and stderr in json format
        # return the exact response fom pyService.py only!
        # Your code should handle 'code' as an argument in both
        # request.form and request.json
        ### BEGIN STUDENT CODE ###
        ### END STUDENT CODE ###
        return ''
    else:
        return app.send_static_file("python.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)
