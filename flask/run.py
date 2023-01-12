from application import app
from flask_swagger_ui import get_swaggerui_blueprint

if __name__ == "__main__":
    app.run(debug = True, port= 8000)