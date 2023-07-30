'''
Jinja2 syntax
{% .... %} - for statements
{{ ... }} = for printing outputs
{# ... #} - for comments
'''

'''
CSS styling way:
Make parent dir: static/css/filename.css
JS way: 
Make subdirectory after static : static/script/filename.js

How to Link CSS in html file:
<link rel='stylesheet' href = "{{url_for('static',filename='css/filename.css')}}">
How to Link JS in html file:
<script type= 'text/javascript' src = '{{url_for('static',filename='script/filename.js')}}'
'''

from flask import Flask,redirect,url_for,request,render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res= ''
    if score>=50:
        res= 'PASS'
    else:
        res= 'FAIL'
    exp = {'score': score, 'res': res}
    return render_template('result.html',result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return f"The person has failed and the marks is {score}"

@app.route('/results/<int:marks>')
def results(marks):
    result = ''
    if marks < 50:
        result = 'fail'
    else:
        result= 'success'
    return redirect(url_for(result,score=marks))

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science+maths+c+datascience)/4
    res = ''
    return redirect(url_for('success',score=total_score))




if __name__ == '__main__':
    app.run(debug=True)

