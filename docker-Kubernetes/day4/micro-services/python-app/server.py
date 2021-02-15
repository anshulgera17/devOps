from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["GET"])
def root():
  return "welcome to python app"


@app.route('/test', methods=["GET"])
def test():
  return "test api inside python app"


@app.route('/ml', methods=["GET"])
def recommend_products():
  return {
    "products": [
      { "id": 1, "title": "product 1", "price": 100 },
      { "id": 2, "title": "product 2", "price": 200 },
      { "id": 3, "title": "product 3", "price": 300 },
    ]
  }


app.run(port=3000, host="0.0.0.0")