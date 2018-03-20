from flask import Flask, request
import _pickle as cPickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

@app.route("/")
def hello():
    
    age = int(request.args.get('age', default = 1, type = int))
    number_sexual_partners = int(request.args.get('number_of_sexual_partners', default = 1, type = int))
    
    print(age)
    print(number_sexual_partners)
    loaded_model = cPickle.load(open("rand_model.sav", 'rb'))
    X_te = [[age, number_sexual_partners,18.0,1.0,0.0,0.0,0.0,1.0,0.25,0.0,0.0,1.0,2.0,1.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1,2.0,2.0,0,0,0,0]]
    result = loaded_model.predict(X_te)
    print(np.array2string(result, separator=', '))
    return np.array2string(result, separator=', ')
    #return result

if (__name__ == "__main__"):
	app.run(port = 5000)
