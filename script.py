from flask import Flask
import cPickle
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

@app.route("/")
def hello():
	loaded_model = cPickle.load(open("rand_model.sav", 'rb'))
	result = loaded_model.predict(X_te)
	print(result)


if (__name__ == "__main__"):
	app.run(port = 5000)
