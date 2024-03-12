from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Jakarta, Indonesia',
    'salary':'Rp10.000.000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Bogor, Indonesia',
    'salary':'Rp10.000.000'
  },
  {
    'id':3,
    'title':'Front-End Engineer',
    'location':'Remote',
  },
  {
    'id':4,
    'title':'Back-End Engineer',
    'location':'San Fransisco, USA',
    'salary':'$120,000'
  },
]

@app.route("/")
def index():
  return render_template("home.html", jobs=JOBS, company_name="Fierynx")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)