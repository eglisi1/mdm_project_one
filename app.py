from flask import Flask
import service.logger as logger

app = Flask(__name__)
log = logger.Logger()

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    log.info('Starting Flask app')
    app.run()