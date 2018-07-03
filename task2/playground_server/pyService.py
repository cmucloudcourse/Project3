from flask import Flask, request
import subprocess
import json

app = Flask(__name__, static_url_path='')

@app.route("/py/eval", methods=['GET', 'POST'])
def handle():
    if request.method == 'POST':

        # Implementation goes here.
        #
        # Both stdout and stderr should be captured.
        # {"stdout": "<output_from_stdout>", "stderr": "<output_from_stderr>"}

        ### BEGIN STUDENT CODE ###
        ### END STUDENT CODE ###
        print "Hello getting the request"
        try:
            content = request.get_json(force=True)
            return executeCommand(command=content['code'])
        except Exception as e:
            json_data = {}
            json_data['stdout'] = ""
            json_data['stderr'] = str(e)
            return json.dumps(json_data)

    else :
        return "Recieved a GET request."


def executeCommand(command):
    json_data = {}
    proc = subprocess.Popen(["python", "-c", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = proc.communicate()
    json_data['stderr'] = stderrdata
    json_data['stdout'] = stdoutdata
    return json.dumps(json_data)

if __name__ == '__main__':
    app.run(threaded=True, debug=True, host="0.0.0.0", port=6000)

