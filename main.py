import os

from google.cloud import storage
import tensorflow as tf
from flask import Flask

app = Flask(__name__)

model = tf.keras.models.load_model("gs://mom_seguros_images_car/model_output/ic_v4.7")

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))