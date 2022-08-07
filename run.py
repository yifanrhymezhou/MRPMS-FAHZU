from flask import Flask, render_template, redirect, request, flash
from flask_restful import Api, Resource
import json
from package.project_summary import Project_Summaries, Project_Summary
from package.connect import get_db

app = Flask(__name__)
app.config['SECRET_KEY'] ='000'
api = Api(app)

api.add_resource(Project_Summaries, '/project_summaries')
api.add_resource(Project_Summary, '/project_summaries/<int:id>')

@app.route("/dashboard")
def index():
    return render_template('index.html')
@app.route("/", methods=['POST', 'GET'])
def login():
    if request.method=="GET":
        return render_template('login.html')
    id = request.form['id']
    print(id)
    password = request.form['password']
    print(password)
    if request.method=="POST":
        if not id or not password:
            flash('Please enter your username and password.')
        if id and password:
            sql = "SELECT * FROM KY_EMPLOYEE WHERE EMP_ID = '" + id + "' AND PASSWORD = '" + password +"'"
            results = get_db(sql, "cp936", "select")
            print(results)
            if len(results) == 1:
                return redirect('/dashboard')
            else:
                flash('Wrong password or ID. Please try again.')
                return redirect('/')
@app.route("/project_summary")
def project_page():
    return render_template('project_summary.html')
@app.route("/project_delay_summary")
def project_delay_page():
    return render_template('project_delay_summary.html')

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    #particularly for restful api:
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    app.run(debug=True,port=8000)
