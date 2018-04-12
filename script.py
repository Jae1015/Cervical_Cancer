from flask import Flask, request
import cPickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

@app.route("/")
def hello():
    
    age = int(request.args.get('age', default = 1, type = int))
    sex_part= int(request.args.get('sex_part', default = -1, type = int))
    f_s_i=int(request.args.get('f_s_i', default = -1, type = int))
    n_o_preg=int(request.args.get('n_o_preg', default = -1, type = int))
    smokes=int(request.args.get('smokes', default = -1, type = int))
    smokes_year=int(request.args.get('smokes_year', default = -1, type = int))
    smokes_pack=int(request.args.get('smokes_pack', default = -1, type = int))
    hormonal_contra=int(request.args.get('hormonal_contra', default = -1, type = int))
    hormonal_year=int(request.args.get('hormonal_year', default = -1, type = int))
    iud=int(request.args.get('iud', default = -1, type = int))
    iud_year=int(request.args.get('iud_year', default = -1, type = int))
    std=int(request.args.get('std', default = -1, type = int))
    std_n=int(request.args.get('std_n', default = -1, type = int))
    std_co=int(request.args.get('std_co', default = -1, type = int))
    std_cer=int(request.args.get('std_cer', default = -1, type = int))
    std_va=int(request.args.get('std_va', default = -1, type = int))
    std_vulvo=int(request.args.get('std_vulvo', default = -1, type = int))
    std_syp=int(request.args.get('std_syp', default = -1, type = int))
    std_pid=int(request.args.get('std_pid', default = -1, type = int))
    std_geni=int(request.args.get('std_geni', default = -1, type = int))    
    std_mollu=int(request.args.get('std_mollu', default = -1, type = int))
    std_aids=int(request.args.get('std_aids', default = -1, type = int))
    std_hiv=int(request.args.get('std_hiv', default = -1, type = int))
    std_hepa=int(request.args.get('std_hepa', default = -1, type = int))
    std_hpv=int(request.args.get('std_hpv', default = -1, type = int))
    no_std=int(request.args.get('no_std', default = -1, type = int))
    f_diag=int(request.args.get('f_diag', default = -1, type = int))
    l_diag=int(request.args.get('l_diag', default = -1, type = int)) 
    dx_cancer=int(request.args.get('dx_cancer', default = -1, type = int))
    dx_cin=int(request.args.get('dx_cin', default = -1, type = int))
    dx_hpv=int(request.args.get('dx_hpv', default = -1, type = int))
    dx=int(request.args.get('dx', default = -1, type = int))

    print(age)
    print(sex_part)
    
    loaded_model = cPickle.load(open("rand_model.sav", 'rb'))
    X_te =[[age,sex_part,f_s_i,n_o_preg,smokes,smokes_year,smokes_pack,hormonal_contra,hormonal_year,iud,iud_year,std,std_n,std_co,std_cer,std_va,std_vulvo,std_syp,std_pid,std_geni,std_mollu,std_aids,std_hiv,std_hepa,std_hpv,no_std,f_diag,l_diag,dx_cancer,dx_cin,dx_hpv,dx]]
    print("####")
    print(X_te)
    print("####")
    
    result = loaded_model.predict(X_te)
    print(np.array2string(result, separator=', '))

    #return np.array2string(result, separator=', ')
    return str(result[0][4])

if (__name__ == "__main__"):
	app.run(port = 5000)

