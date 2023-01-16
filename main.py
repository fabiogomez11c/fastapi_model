from fastapi import FastAPI
import tensorflow as tf

app = FastAPI()

model1 = tf.keras.models.load_model('model.h5')
model2 = tf.keras.models.load_model('model.h5')

@app.get("/")
def read_root():
  return {"Hello": "World"}
