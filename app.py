from flask import Flask
from flask import json
import logging
import time

app = Flask(__name__)


@app.route("/")
def hello():
	app.logger.info('Main request status!')
    return "Hello World!"

@app.route("/status")
def healthchesk():
	response = app.response_class(
		response = json.dumps({"result": "OK - healthy"}),
		status = 200,
		mimetype = 'application/json'
		)
	app.logger.info('status request success')
	return response

@app.route("/metrics")
def metrics():
	response = app.response_class(
		response = json.dumps({"status":"success","data": {"UserCount": 140, "UserCountActive": 23}}),
		status = 200,
		mimetype = 'application/json'
		)
	#logging.info({{"time":time.now}}, {{ "name":"metrics"}} "endpoint was reached")
	app.logger.info('Metrics request success')
	return response



if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')

