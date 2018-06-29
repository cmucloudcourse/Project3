from flask import Flask, request
import requests,json

flag = True
app = Flask(__name__, static_folder='site', static_url_path='')

@app.route("/", methods=['GET'])
def handle():
    return app.send_static_file("index.html")

@app.route("/python", methods=['GET', 'POST'])
def handlePython():
    if request.method == 'POST':
        payload = {}
        if request.json :
            print "Request contains JSON data"
            code = request.get_json(force=True)
            print code
            payload=code
        else :
            print "Request contains form data"
            code = request.form['code']
            payload['code'] = code

        print "Converted Payload JSON is "+json.dumps(payload)
        res = fwdreq(json.dumps(payload))
        # This should return the stdout and stderr in json format
        # return the exact response fom pyService.py only!
        # Your code should handle 'code' as an argument in both
        # request.form and request.json
        ### BEGIN STUDENT CODE ###
        ### END STUDENT CODE ###

        return res
    else:
        return app.send_static_file("python.html")

def fwdreq(command):
    global  flag
    if flag:
        pythonServiceHostName = "http://playground-task3-service:80"
        print "sending request to GCP "+pythonServiceHostName;
        flag = False
    else :
        pythonServiceHostName = "http://azure-task3-service:80"
        print "Sending request to azure "
        flag = True
    r = requests.post(pythonServiceHostName+"/py/eval", command)
    # print r.text
    print "Results ::::: This is the result json"
    print r.json()
    return r.text

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)
