from flask import Flask

from config import config

app = Flask(__name__)
app.debug = True
app.config.from_object(config['development'])

from login import login_blue
from file import file_blue

app.register_blueprint(login_blue)
app.register_blueprint(file_blue)

if __name__ == '__main__':
    print(app.url_map)
    app.run()
