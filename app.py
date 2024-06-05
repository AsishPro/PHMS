from flask import Flask,render_template,request, session
import numpy as np
import pickle
import data
import onetimepass
import pandas as pd
import psycopg2
import os

from psycopg2 import sql

app = Flask(__name__)    

app.secret_key = 'NOT_A_SECRET'

otp=''


file_path = 'high_accuracy_named.pkl'

with open(file_path, 'rb') as f:
    model = pickle.load(f)
print(model)


print(os.environ.get('pg_host'))
def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('pg_host'),
        user=os.environ.get('pg_user'),
        password=os.environ.get('pg_password'),
        dbname=os.environ.get('pg_database')
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        username = request.form['username']
        password = request.form['pass']

        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            print('Login successful')
            return render_template("home.html")
        else:
            return render_template('login.html',alert=1)
    
    return render_template('login.html')

@app.route('/home',methods=['POST','GET'])
def home():
    return render_template("home.html")

@app.route('/register', methods=["POST", "GET"])
def register():
    global otp
    if request.method == 'POST':
        session['user_details'] = request.form
        # data=session.get('user_details')
        # print(data,'asish')
        # print(data['fname'])
        print(request.form['email'])
        otp = onetimepass.otp_function(request.form['email'])
        print(otp + " updated")
        return render_template("register.html", otp=otp)
    else:
        return render_template("register.html")
    

@app.route('/validate_otp', methods=["POST"])
def validate_otp():
    global otp
    if 'otp' in request.form:
        if request.form['otp'] == otp:
            print("Validation Successful")
            print(request.form['otp'], otp)
            data = session.get('user_details')
            if data:
                conn = get_db_connection()
                cursor = conn.cursor()
                insert = sql.SQL("INSERT INTO users (username, email, password) VALUES (%s, %s, %s);")
                val = (data['fname'], data['email'], data['pass'])
                cursor.execute(insert, val)

                conn.commit()
                cursor.close()
                conn.close()
                print("entry successful")
                return render_template('login.html')
            else:
                return 'User details not found.'
        else:
            return render_template("register.html")
    return render_template("register.html")


@app.route('/predict',methods=["POST","GET"])
def predict():
    if request.method=="POST":
        l=[]
        form_data=request.form
        print(form_data)


        for key,value in form_data.items():
            print(key,value)
            print(data.m[value])
            l.append(data.m[value])
        print(l)
        
        
        while len(l)<17:
            l.append(0)
        
        l=np.reshape(l,(1,-1))

        # l1=[0 for i in range(17)]
        # l1=np.reshape(l,(1,-1))
        # print(model.predict(l1))
        
        result=model.predict(l)
        print(result)

        if l.sum()==0:
            result=[-1]
        
        return render_template("base.html", symptoms=data.sl,prediction=data.disease[result[0]]) 

    return render_template("base.html", symptoms=data.sl) 


@app.route('/medicines_list',methods=["POST","GET"])
def medicines():
    if request.method=="POST":
        selected_disease = request.form.get('disease')
        print(selected_disease)


       
        row=data.medicines[data.medicines['Disease']==selected_disease].values[0][1:]
        medicines=[i for i in row if not pd.isna(i)]    

        #medicines list
        print(medicines)
            

        info=[]
        dosing = []
        precautions=[]
        side_effects=[]
        for medicine in medicines:
            # if medicine=='No Medicine':
                
            desc= data.medicines_desc[(data.medicines_desc['Medicine'] == medicine) & (data.medicines_desc['Disease'] == selected_disease)]['Description'].values[0]

            # print(desc)

            dose = data.med_detailed[(data.med_detailed['Medicine'] == medicine) & (data.med_detailed['Disease'] == selected_disease)]['Dosing'].values[0]

            precaution = data.med_detailed[(data.med_detailed['Medicine'] == medicine) & (data.med_detailed['Disease'] == selected_disease)]['Precautions'].values[0]

            side = data.med_detailed[(data.med_detailed['Medicine'] == medicine) & (data.med_detailed['Disease'] == selected_disease)]['Side Effects'].values[0]

            # print(desc,dose,precaution,side)
            info.append(desc)
            dosing.append(dose)
            precautions.append(precaution)
            side_effects.append(side)

        medicines=list(zip(medicines, info,dosing,precautions,side_effects))

        return render_template("medicines_info.html", medicines_info=medicines) 
    
    return render_template("medicines_final.html", diseases=data.dl[:-1]) 
    

@app.route('/doctors_hosp',methods=["POST","GET"])
def doctors():
    if request.method =="POST":
        selected_disease = request.form.get('disease')
        # print(selected_disease)
        
        category1=data.categories[data.categories['Disease']==selected_disease]['Category1'].values[0]
        category2=data.categories[data.categories['Disease']==selected_disease]['Category2'].values[0]


        doctors1=data.doctor[data.doctor['Category']==category1]['Doctors'].values
        hospitals1=data.doctor[data.doctor['Category']==category1]['Hospitals'].values

        print(doctors1)
        print(hospitals1)
        
        links1=data.doctor[data.doctor['Category']==category1]['Contact'].values


        doctors2=data.doctor[data.doctor['Category']==category2]['Doctors'].values
        hospitals2=data.doctor[data.doctor['Category']==category2]['Hospitals'].values
        links2=data.doctor[data.doctor['Category']==category2]['Contact'].values

       

        return render_template('doctors_hosp.html', selected_disease=selected_disease,doctor_hospitals_links1=zip(doctors1, hospitals1,links1),doctor_hospitals_links2=zip(doctors2, hospitals2,links2),categories=[category1,category2])

    return render_template('doctors_hosp.html',diseases=data.dl[:-1])
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    # app.run(debug=True)
    # ngrok.set_auth_token ("2cp3wE0TnBbGDuwlraaUxGPXqas_6MvUXCiNetc79PehrVRX5")
    # ngrok_tunnel = ngrok.connect(5000)
    # print('Public URL:', ngrok_tunnel.public_url)
    # app.run()