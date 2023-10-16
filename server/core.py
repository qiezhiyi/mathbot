from sanic import Sanic
from sanic_cors import CORS

app = Sanic(__name__)


CORS(app)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
