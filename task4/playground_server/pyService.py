from flask import Flask, request

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

if __name__ == '__main__':
    app.run(threaded=True, debug=True, host="0.0.0.0", port=6000)
