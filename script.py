from flask import Flask, request
importcPickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

@app.route("/")
def hello():
    
    age = int(request.args.get('age', default = 1, type = int))
    sex_part= int(request.args.get('number_of_sexual_partners', default = 0, type = int))
    f_s_i=int(request.args.get('first_sexual_intercourse', default = 0, type = int))
    n_o_preg=int(request.args.get('number_of_pregnancies', default = 0, type = int))
    smokes=int(request.args.get('smokes', default = 0, type = int))
    smokes_year=int(request.args.get('smokes_year', default = 0, type = int))
    smokes_pack=int(request.args.get('smokes_year_pack', default = 0, type = int))
    hormonal_contra=int(request.args.get('hormonal_contraceptives', default = 0, type = int))
    hormonal_year=int(request.args.get('hormonal_contraceptives_year', default = 0, type = int))
    iud=int(request.args.get('iud', default = 0, type = int))
    iud_year=int(request.args.get('iud_year', default = 0, type = int))
    std=int(request.args.get('std', default = 0, type = int))
    std_n=int(request.args.get('std_number', default = 0, type = int))
    std_co=int(request.args.get('std_condylomatosis', default = 0, type = int))
    std_cer=int(request.args.get('std_cervical_condylomatosis', default = 0, type = int))
    std_va=int(request.args.get('std_vaginal_condylomatosis', default = 0, type = int))
    std_vulvo=int(request.args.get('std_vulvo_perineal_condylomatosis', default = 0, type = int))
    std_syp=int(request.args.get('std_syphilis', default = 0, type = int))
    std_pid=int(request.args.get('std_pid', default = 0, type = int))
    std_geni=int(request.args.get('std_genital_herpes', default = 0, type = int))    
    std_mollu=int(request.args.get('std_molluscum_contagiosum', default = 0, type = int))
    std_aids=int(request.args.get('std_aids', default = 0, type = int))
    std_hiv=int(request.args.get('std_hiv', default = 0, type = int))
    std_hepa=int(request.args.get('std_hepatitisb', default = 0, type = int))
    std_hpv=int(request.args.get('std_hpv', default = 0, type = int))
    no_std=int(request.args.get('number_std', default = 0, type = int))
    f_diag=int(request.args.get('time_first_diagnose', default = 0, type = int))
    last_diag=int(request.args.get('time_last_diagnose', default = 0, type = int)) 
    dx_cancer=int(request.args.get('dx_cancer', default = 0, type = int))
    dx_cin=int(request.args.get('dx_cin', default = 0, type = int))
    dx_hpv=int(request.args.get('dx_hpv', default = 0, type = int))
    dx=int(request.args.get('dx', default = 0, type = int))

    print(age)
    print(sex_part)
    loaded_model = cPickle.load(open("rand_model.sav", 'rb'))
    X_te = [[age, number_sexual_partners,18.0,1.0,0.0,0.0,0.0,1.0,0.25,0.0,0.0,1.0,2.0,1.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1,2.0,2.0,0,0,0,0]]
    result = loaded_model.predict(X_te)
    print(np.array2string(result, separator=', '))
    return np.array2string(result, separator=', ')
    #return result

if (__name__ == "__main__"):
	app.run(port = 5000)
