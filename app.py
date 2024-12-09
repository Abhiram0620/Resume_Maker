from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/adding', methods=['POST'])
def adding():
    name = request.form.get("first_name") + " " + request.form.get("last_name")
    mobile = request.form.get("mobile_number")
    mobile = "+91 " + mobile[:5] + " " + mobile[5:]
    email = request.form.get("email")
    alinkedin = request.form.get("alinkedin")
    linedin = request.form.get("linkdin")
    agithub = request.form.get("agithub")
    github = request.form.get("github")
    summary = request.form.get("summary")

    if len(alinkedin) != 0 and len(linedin) == 0:
        return render_template("index.html", msg="If you enter anchor then you have to enter URL")

    if len(agithub) != 0 and not github:
        return render_template("index.html", msg1="If you enter anchor then you have to enter URL")
    
    return render_template('resume_template2.html', fullname=name, phone_number=mobile, mail=email, alinkedin=alinkedin, linkedinurl=linedin, agithub=agithub, github=github, summary=summary)

app.route('/gitaddlink',methods=['get','post'])
def gitaddlink():
    #adding new git link input
    return render_template("index.html",gitaddlink=True)

if __name__ == '__main__':
    app.run(debug=True)
