from flask import Flask,render_template,request
import pickle
app = Flask(__name__)
model = pickle.load(open("phone_.pkl", "rb"))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        battery_power=int(request.form['battery_power'])
        blue=int(request.form['blue'])
        clock_speed=float(request.form['clock_speed'])
        fc=int(request.form['fc'])
        four_g=int(request.form['four_g'])
        int_memory=int(request.form['int_memory'])
        m_dep=float(request.form['m_dep'])
        mobile_wt=int(request.form['mobile_wt'])
        n_cores=int(request.form['n_cores'])
        pc=int(request.form['pc'])
        px_height=int(request.form['px_height'])
        px_width=int(request.form['px_width'])
        ram=int(request.form['ram'])
        sc_h=int(request.form['sc_h'])
        sc_w=int(request.form['sc_w'])
        three_g=int(request.form['three_g'])
        touch_screen=int(request.form['touch_screen'])
        wifi=int(request.form['wifi'])
        dual_sim=int(request.form['dual_sim'])
        output=model.predict([[battery_power,blue,clock_speed,dual_sim,fc,four_g,int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_h,sc_w,three_g,touch_screen,wifi]])
        if output == 0:
            val = "LOW COST"
        elif output==1:
            val = "MEDIUM COST"
        elif output==2:
            val = "HIGH COST"
        else:
            val="VERY HIGH COST"
        return render_template('index.html', prediction_text='The value of the PHONE is  {}'.format(val))
    else:
        return render_template('index.html')	
if __name__ == "__main__":
    app.run() 				
        
        