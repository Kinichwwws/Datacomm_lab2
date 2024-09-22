from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def time():
    # return (1)
    return {'current_time': datetime.now().isoformat()}
if __name__ == '__main__': app.run(host='0.0.0.0',port=8080, debug=True)


