""" module """

from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

app.register_blueprint(
    get_swaggerui_blueprint(
        "/swagger",
        "/static/openapi.yml",
        config={
            'app_name': 'Reference Payment'
        }
    ),
    url_prefix="/swagger"
)

if __name__ == '__main__':
    app.run(host="0.0.0.0")


@app.get("/test")
def hello():
    """ endpoint assssssss"""

    return "OK"
