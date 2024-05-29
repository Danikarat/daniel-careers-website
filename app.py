from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
  {
  "id" : 1,
  "title" : "Data Analyst",
  "location" : "Accra, Ghana",
  "salary" : "GHc. 12,000"
  },
  {
    "id" : 2,
    "title" : "Data Annotator",
    "location" : "Accra, Ghana",
    "salary" : "GHc. 5,000"
  },
  {
    "id" : 3,
    "title" : "Cybersecurity Analyst",
    "location" : "Hybrid",
    "salary" : "GHc. 15,000"
  },
  {
    "id" : 4,
    "title" : "Ethical Hacker",
    "location" : "Remote",
    "salary" : "GHc. 17,000"
  }


]





@app.route('/')
def hello_world():
  return render_template('home.html',
                         jobs= JOBS,
                        )
@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


print("__name__")
if __name__ =="__main__":
  app.run(host = '0.0.0.0', debug=True)