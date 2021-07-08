from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import hashlib
from random import randint, shuffle

def hashPass(passIn):
    hashed = hashlib.sha256(str.encode(passIn)).hexdigest()
    return(hashed)

def compareHash(hashIn, passIn):
    retBool = False
    if hashIn == hashlib.sha256(str.encode(passIn)).hexdigest():
        retBool = True
    return retBool

lowerCase = 'abcdefghijklmnopqrstuvwxyz'
upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = "0123456789"

app = Flask(__name__, template_folder="Templates")
app.secret_key = "trishawharton25confirmed"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/krisnubz/Cobellum/Cobellum/User.sqlite3'
app.config['SQLALCHEMY_BINDS'] = {'question' : 'sqlite:////home/krisnubz/Cobellum/Cobellum/Question.sqlite3'}
cau = 0

#ONLY CHANGE BELOW THIS PART!!!
total_players = 25836

db = SQLAlchemy(app)
admin_list = ["kris"]

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    password = db.Column(db.String(50))
    email = db.Column(db.String(50))
    sr = db.Column(db.Integer)
    highestSR = db.Column(db.Integer)
    highestRank = db.Column(db.String(10))
    rank = db.Column(db.String(10))
    flag = db.Column(db.String(50))
    school = db.Column(db.String(50))
    referral = db.Column(db.String(50))
    bit = db.Column(db.Integer)
    friends = db.Column(db.Text)
    requests = db.Column(db.Text)
    correct = db.Column(db.Integer)
    incorrect = db.Column(db.Integer)
    inGame = db.Column(db.Integer)

    def __init__(self, user, passw, em, flg, skl, rcode, ref):
        self.username = user
        self.password = passw
        self.email = em
        self.sr = 0
        self.rank = "Byte"
        self.flag = flg
        self.school = skl
        self.referral = rcode
        if ref == True:
            self.bit = 500
        else:
            self.bit = 0
        self.friends = ""
        self.requests = ""
        self.highestSR = 0
        self.highestRank = "Byte"
        self.correct = 0
        self.incorrect = 0
        self.inGame = 0

class Question(db.Model):
    __bind_key__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500))
    answer = db.Column(db.String(500))
    level = db.Column(db.Integer)
    elo = db.Column(db.Integer)

    def __init__(self, q, a, l, e):
        self.question = q
        self.answer = a
        self.level = int(l)
        self.elo = int(e)

def cce(email):
	first = (email.split("@"))[0]
	back = (email.split("@"))[1]
	return first.lower() + "@" + back

def generateCode():
    while True:
        string = ""
        for x in range(5):
        	if randint(1,3) == 1:
        		string += lowerCase[randint(0,25)]
        	elif randint(1,3) == 2:
        		string += upperCase[randint(0,25)]
        	else:
        		string += numbers[randint(0,9)]
        if not User.query.filter_by(referral=string).first():
            break
    return string

l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
for q in Question.query.all():
    if q.level == 1:
        l1.append(q)
    elif q.level == 2:
        l2.append(q)
    elif q.level == 3:
        l3.append(q)
    elif q.level == 4:
        l4.append(q)
    else:
        l5.append(q)

def generateQuestion(rank):
    if rank == "Byte":
        for x in range(10):
            rand = randint(1,100)
            if rand <= 35:
                s = (l1[randint(0,len(l1)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 35 and rand <= 65:
                s = (l2[randint(0,len(l2)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 65 and rand <= 85:
                s = (l3[randint(0,len(l3)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 85 and rand <= 95:
                s = (l4[randint(0,len(l4)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 95:
                s = (l5[randint(0,len(l5)-1)])
                return [s.question, s.answer, s.level, s.elo]
    if rank == "Kilo":
        for x in range(10):
            rand = randint(1,100)
            if rand <= 25:
                s = (l1[randint(0,len(l1)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 25 and rand <= 60:
                s = (l2[randint(0,len(l2)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 60 and rand <= 85:
                s = (l3[randint(0,len(l3)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 85 and rand <= 95:
                s = (l4[randint(0,len(l4)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 95:
                s = (l5[randint(0,len(l5)-1)])
                return [s.question, s.answer, s.level, s.elo]
    if rank == "Mega":
        for x in range(10):
            rand = randint(1,100)
            if rand <= 18:
                s = (l1[randint(0,len(l1)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 18 and rand <= 43:
                s = (l2[randint(0,len(l2)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 43 and rand <= 83:
                s = (l3[randint(0,len(l3)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 83 and rand <= 93:
                s = (l4[randint(0,len(l4)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 93:
                s = (l5[randint(0,len(l5)-1)])
                return [s.question, s.answer, s.level, s.elo]
    if rank == "Giga":
        for x in range(10):
            rand = randint(1,100)
            if rand <= 10:
                s = (l1[randint(0,len(l1)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 10 and rand <= 30:
                s = (l2[randint(0,len(l2)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 30 and rand <= 70:
                s = (l3[randint(0,len(l3)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 70 and rand <= 90:
                s = (l4[randint(0,len(l4)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 90:
                s = (l5[randint(0,len(l5)-1)])
                return [s.question, s.answer, s.level, s.elo]
    if rank == "Tera":
        for x in range(10):
            rand = randint(1,100)
            if rand <= 5:
                s = (l1[randint(0,len(l1)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 5 and rand <= 20:
                s = (l2[randint(0,len(l2)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 20 and rand <= 55:
                s = (l3[randint(0,len(l3)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 55 and rand <= 85:
                s = (l4[randint(0,len(l4)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 85:
                s = (l5[randint(0,len(l5)-1)])
                return [s.question, s.answer, s.level, s.elo]
    if rank == "Master":
        for x in range(10):
            rand = randint(1,100)
            if rand <= 5:
                s = (l1[randint(0,len(l1)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 5 and rand <= 15:
                s = (l2[randint(0,len(l2)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 15 and rand <= 45:
                s = (l3[randint(0,len(l3)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 45 and rand <= 80:
                s = (l4[randint(0,len(l4)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 80:
                s = (l5[randint(0,len(l5)-1)])
                return [s.question, s.answer, s.level, s.elo]
    if rank == "Grandmaster" or rank == "Top 1" or rank == "Top 2" or rank == "Top 3":
        for x in range(10):
            rand = randint(1,100)
            if rand <= 4:
                s = (l1[randint(0,len(l1)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 4 and rand <= 10:
                s = (l2[randint(0,len(l2)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 10 and rand <= 30:
                s = (l3[randint(0,len(l3)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 30 and rand <= 70:
                s = (l4[randint(0,len(l4)-1)])
                return [s.question, s.answer, s.level, s.elo]
            elif rand > 70:
                s = (l5[randint(0,len(l5)-1)])
                return [s.question, s.answer, s.level, s.elo]

@app.route("/<kazu>")
def webcomic(kazu):
    return render_template("pdf.html", file=kazu)

@app.route("/earlyleave")
def earlyleave():
    updateSR(-20)
    User.query.filter_by(username=session["username"]).first().inGame = 0
    db.session.commit()
    session.pop("num", None)
    session["lose20"] = True
    return redirect(url_for("profile"))

@app.route("/", methods=["GET","POST"])
def default():
    return redirect(url_for("login"))

@app.route("/edit/", methods=["GET","POST"])
def edit():
    if "username" in session:
        if request.method == "POST":
            if "@" not in request.form["email"]:
                return render_template("editprofile.html", user=User.query.filter_by(username=session["username"]), flash=True, warning="Email is not valid.")
            if " " in request.form["password1"]:
                return render_template("editprofile.html", user=User.query.filter_by(username=session["username"]), flash=True, warning="Password cannot contain spaces.")
            if len(request.form["password1"]) < 6 and request.form["password1"] != "":
                return render_template("editprofile.html", user=User.query.filter_by(username=session["username"]), flash=True, warning="Password must be > 6 characters.")
            if (request.form["password1"] != request.form["password2"]) and request.form["password1"] != "":
                return render_template("editprofile.html", user=User.query.filter_by(username=session["username"]), flash=True, warning="Passwords don't match.")
            User.query.filter_by(username=session["username"]).first().email = request.form["email"]
            if request.form["password1"] != "":
                User.query.filter_by(username=session["username"]).first().password = hashPass(request.form["password1"])
            db.session.commit()
            return redirect(url_for("profile"))
        else:
            return render_template("editprofile.html", user=User.query.filter_by(username=session["username"]))
    else:
        return redirect(url_for("login"))

def getPercentage():
    rank = User.query.filter_by(username=session["username"]).first().rank
    elo = User.query.filter_by(username=session["username"]).first().sr
    if rank == "Byte":
        max = 500
    elif rank == "Kilo":
        max = 1000
    elif rank == "Mega":
        max = 1500
    elif rank == "Giga":
        max = 2000
    elif rank == "Tera":
        max = 2500
    elif rank == "Master":
        max = 3000
    else:
        max = sr
    return int(round((elo/max)*100))

@app.route("/play/", methods=["GET","POST"])
def play():
    if "username" in session:
        if request.method == "POST":
            if session["num"] == 10:
                if request.form["submit"] == session["correct"]:
                    session["tally"].append(1)
                    session["test"].append([session["question"],session["Qlevel"],"Correct",request.form["submit"],session["correct"]])
                else:
                    session["tally"].append(-1)
                    session["test"].append([session["question"],session["Qlevel"],"Incorrect",request.form["submit"],session["correct"]])
                session["level"].append(session["Qlevel"])
                session["qsr"].append(session["Qelo"])
                User.query.filter_by(username=session["username"]).first().inGame = 0
                db.session.commit()
                netSR = markTest(session["tally"], session["level"], session["qsr"])
                return render_template("test.html", right=countRight(session["tally"]), nsr=updateSR(netSR), n=session["num"], test=session["test"], changeInSr=netSR, rank=User.query.filter_by(username=session["username"]).first().rank, percentage=getPercentage())
            session["num"] += 1
            session["level"].append(session["Qlevel"])
            session["qsr"].append(session["Qelo"])
            if request.form["submit"] == session["correct"]:
                session["tally"].append(1)
                #title|level|r/w|your answer|correct answer
                session["test"].append([session["question"],session["Qlevel"],"Correct",request.form["submit"],session["correct"]])
            else:
                session["tally"].append(-1)
                session["test"].append([session["question"],session["Qlevel"],"Incorrect",request.form["submit"],session["correct"]])
            q = generateQuestion(User.query.filter_by(username=session["username"]).first().rank)
            session["question"] = q[0]
            session["Qlevel"] = q[2]
            session["Qelo"] = q[3]
            session["correct"] = q[1].split("|")[0]
            split = q[1].split("|")
            shuffle(split)
            return render_template("play.html", test=[q], a=split[0],b=split[1],c=split[2],d=split[3], n=session["num"])
        else:
            if User.query.filter_by(username=session["username"]).first().inGame == 1:
                updateSR(-20)
                session["lose20"] = True
            if "num" in session:
                if session["num"] == 1:
                    User.query.filter_by(username=session["username"]).first().inGame = 1
                    db.session.commit()
            session["qsr"] = []
            session["tally"] = []
            session["level"] = []
            session["test"] = []
            session["num"] = 1
            q = generateQuestion(User.query.filter_by(username=session["username"]).first().rank)
            session["question"] = q[0]
            session["Qlevel"] = q[2]
            session["Qelo"] = q[3]
            session["correct"] = q[1].split("|")[0]
            split = q[1].split("|")
            shuffle(split)
            if "lose20" in session:
                if session["lose20"] == True:
                    session["lose20"] = False
                    session.pop("lose20", None)
                    return render_template("play.html", test=[q], a=split[0],b=split[1],c=split[2],d=split[3], n=session["num"], flash=True)
            return render_template("play.html", test=[q], a=split[0],b=split[1],c=split[2],d=split[3], n=session["num"])
    else:
        return redirect(url_for("login"))

def checkState():
    if User.query.filter_by(username=session["username"]).first().inGame == 1:
        updateSR(-20)
    else:
        User.query.filter_by(username=session["username"]).first().inGame = 1
        db.session.commit()

@app.route("/login/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        if User.query.filter_by(username=request.form["username"].lower()).first():
            if (request.form["username"].lower() == User.query.filter_by(username=request.form["username"].lower()).first().username) and compareHash(User.query.filter_by(username=request.form["username"].lower()).first().password, request.form["password"]):
                if request.form["username"].lower() in admin_list:
                    session["admin"] = True
                global cau
                session["login"] = True
                session["username"] = request.form["username"].lower()
                session["rank"] = User.query.filter_by(username=request.form["username"].lower()).first().rank
                cau += 1
                return redirect(url_for("profile"))
            else:
                return redirect(url_for("login"))
        else:
            return render_template("login.html", error=True)
    else:
        if "login" in session:
            return redirect(url_for("profile"))
        else:
            return render_template("login.html")

@app.route("/register/", methods=["GET", "POST"])
def register():
    if "login" in session:
        return redirect(url_for("profile"))
    if request.method == "POST":
        if request.form["submit"] == "Register":
            if User.query.filter_by(username=request.form["username"].lower()).first():
                return render_template("testregister.html", uerror="already taken")
            if " " in request.form["username"]:
                return render_template("testregister.html", uerror="cannot contain spaces")
            if len(request.form["password"]) < 6:
                return render_template("testregister.html", perror="must be 6 or more characters")
            session["register"] = [request.form["username"].lower(), "None", request.form["password"]]
            return render_template("register2.html")
        else:
            if request.form["select"] == "select a country..." or request.form["school"] == " " or request.form["school"] == "":
                return render_template("register2.html")
            if User.query.filter_by(referral=request.form["referral"]).first():
                User.query.filter_by(referral=request.form["referral"]).first().bit += 500
                db.session.commit()
                valid = True
            else:
                valid = False
            db.session.add(User(session["register"][0], hashPass(session["register"][2]), session["register"][1], request.form["select"], request.form["school"], generateCode(), valid))
            db.session.commit()
            return redirect(url_for("login"))
    else:
        return render_template("testregister.html")

@app.route("/qedit/<sort>", methods=["GET", "POST"])
def qedit(sort):
    if request.method == "POST":
        if request.form["submit"] == "delete":
            db.session.delete(Question.query.filter_by(question=request.form["search"]).first())
            db.session.commit()
            return render_template("question.html", questions = Question.query.filter_by(level=sort))
        else:
            db.session.add(Question(request.form["question"],(request.form["answer1"]+"|"+request.form["answer2"]+"|"+request.form["answer3"]+"|"+request.form["answer4"]),request.form["level"],request.form["elo"]))
            db.session.commit()
            return render_template("question.html", questions = Question.query.filter_by(level=sort))
    else:
        if sort != "all" and sort != "All":
            return render_template("question.html", questions = Question.query.filter_by(level=sort))
        else:
            return render_template("question.html", questions = Question.query.all())

@app.route("/admin/", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        if request.form["submit"] == "change":
            if request.form["cUsername"] != "":
                User.query.filter_by(username=session["currentSearch"]).first().username = request.form["cUsername"]
            if request.form["cPassword"] != "":
                User.query.filter_by(username=session["currentSearch"]).first().password = hashPass(request.form["cPassword"])
            if request.form["cEmail"] != "":
                User.query.filter_by(username=session["currentSearch"]).first().email= request.form["cEmail"]
            if request.form["cSr"] != "":
                User.query.filter_by(username=session["currentSearch"]).first().sr = request.form["cSr"]
            if request.form["cRank"] != "":
                User.query.filter_by(username=session["currentSearch"]).first().rank = request.form["cRank"]
            if request.form["cCountry"] != "":
                User.query.filter_by(username=session["currentSearch"]).first().flag = request.form["cCountry"]
            if request.form["cOrg"] != "":
                User.query.filter_by(username=session["currentSearch"]).first().school = request.form["cOrg"]
            if request.form["cReferral"] != "":
                User.query.filter_by(username=session["currentSearch"]).first().referral = request.form["cReferral"]
            if request.form["cBit"] != "":
                User.query.filter_by(username=session["currentSearch"]).first().bit = request.form["cBit"]
            if request.form["cRequests"] != "":
                if request.form["cRequests"] == "blank":
                    User.query.filter_by(username=session["currentSearch"]).first().requests = ""
                else:
                    User.query.filter_by(username=session["currentSearch"]).first().requests = request.form["cRequests"]
            if request.form["cFriends"] != "":
                if request.form["cFriends"] == "blank":
                    User.query.filter_by(username=session["currentSearch"]).first().friends = ""
                else:
                    User.query.filter_by(username=session["currentSearch"]).first().friends = request.form["cFriends"]
            db.session.commit()
            return render_template("user_search.html", users=User.query.filter_by(username=session["currentSearch"]))
        if request.form["submit"] == "searchuser":
            if not User.query.filter_by(username=request.form["username"]).first():
                return render_template("admin.html", users=User.query.all(), current_active_users=cau)
            session["currentSearch"] = request.form["username"]
            return render_template("user_search.html", users=User.query.filter_by(username=request.form["username"]))
        if request.form["submit"] == "deleteUser":
            db.session.delete(User.query.filter_by(username=request.form["username"]).first())
            db.session.commit()
            return render_template("admin.html", users=User.query.all(), current_active_users=cau)
        if request.form["submit"] == "delete":
            db.session.delete(Question.query.filter_by(question=request.form["search"]).first())
            db.session.commit()
            return render_template("question.html", questions = Question.query.all())
        if request.form["submit"] == "Clear DB":
            return render_template("admin.html", users=User.query.all(), current_active_users=cau)
        elif request.form["submit"] == "goToQuestion":
            return render_template("question.html", questions = Question.query.all())
        else:
            db.session.add(Question(request.form["question"],(request.form["answer1"]+"|"+request.form["answer2"]+"|"+request.form["answer3"]+"|"+request.form["answer4"]),request.form["level"],request.form["elo"]))
            db.session.commit()
            return render_template("question.html", questions = Question.query.all())
    else:
        if "admin" in session:
            return render_template("admin.html", users=User.query.all(), current_active_users=cau)
        else:
             return redirect(url_for("login"))

@app.route("/profile/", methods=["GET", "POST"])
def profile():
    if "username" in session:
        if "lose20" in session:
            if session["lose20"] == True:
                session["lose20"] = False
                session.pop("lose20", None)
                return render_template("profile.html", user_show=User.query.filter_by(username=session["username"]), username="< "+session["username"]+" >", friend="Friends: " + str(countFriends(session["username"])), added=True, acc=findAccuracy(session["username"]), flash=True, edit=True)
        return render_template("profile.html", user_show=User.query.filter_by(username=session["username"]), username="< "+session["username"]+" >", friend="Friends: " + str(countFriends(session["username"])), added=True, acc=findAccuracy(session["username"]), edit=True)
    else:
        return redirect(url_for("login"))

@app.route("/logout/")
def logout():
    if "username" in session:
        if session["username"] in admin_list:
            session.pop("admin", None)
        session.pop("login", None)
        session.pop("rank", None)
        global cau
        cau -= 1
        session.pop("username", None)
    return redirect(url_for("login"))

@app.route("/requests/", methods=["GET", "POST"])
def friendrequests():
    checkLogin()
    return render_template("friendrequest.html", friends=requestList(session["username"]), added=friendList(session["username"]))

@app.route("/home/", methods=["GET", "POST"])
def home():
    if "login" in session:
        if request.method == "POST":
            if request.form["submit"] == "Search":
                session["user_search"] = request.form["username"]
                return redirect(url_for("profilesearch", name=session["user_search"]))
        else:
            if "failsearch" in session:
                if session["failsearch"] == True:
                    session["failsearch"] = False
                    session.pop("failsearch", None)
                    return render_template("hub.html", flash=True, playercount=total_players+User.query.count())
            return render_template("hub.html", playercount=total_players+User.query.count())
    else:
        return redirect(url_for("login"))

@app.route("/profilesearch/<name>", methods=["GET", "POST"])
def profilesearch(name):
    checkLogin()
    if request.method == "POST":
        if "refresh" not in session:
            if not friendAlready(session["username"], name):
                User.query.filter_by(username=name).first().requests += "{}|".format(session["username"])
                db.session.commit()
                session["refresh"] = False
        return render_template("profile.html", user_show=User.query.filter_by(username=name), username="< {} >".format(name), friend="Friends: " + str(countFriends(name)), added=friendAlready(session["username"], name), acc=findAccuracy(name))
    if User.query.filter_by(username=name).first():
        session.pop("refresh", None)
        if "username" in session:
            return render_template("profile.html", user_show=User.query.filter_by(username=name), username="< {} >".format(name), friend="Friends: " + str(countFriends(name)), added=friendAlready(session["username"], name), acc=findAccuracy(name))
    else:
        session["failsearch"] = True
        return redirect(url_for("home"))

@app.route("/leaderboards/")
def leaderboards():
    if "username" in session:
        return render_template("leaderboard.html", users=sortLB())
    else:
        return redirect(url_for("login"))

@app.route("/add/<added>")
def add(added):
    addToFriends(session["username"], added)
    removeFromRequest(session["username"], added)
    return redirect(url_for("friendrequests"))

def checkLogin():
    if "login" in session:
        pass
    else:
        return redirect(url_for("login"))

def friendAlready(checker, checked):
    if checked+"|" in User.query.filter_by(username=checker).first().requests:
        return True
    if checker == checked:
        return True
    user = User.query.filter_by(username=checked).first()
    arr = user.requests.split("|")
    arr2 = user.friends.split("|")
    if checker in arr or checker in arr2:
        return True
    return False

#sort leaderboards
def sortLB():
    ans = []
    for user in User.query.all():
        ans.append([user.username, user.rank, user.flag, user.sr])
    ans.sort(reverse=True,key=lambda x: x[3])
    for x in range(len(ans)):
        ans[x].append(x+1)
    return ans

#get list of names minus the blank for friendrequests()
def requestList(name):
    arr = User.query.filter_by(username=name).first().requests.split("|")
    ans = []
    for x in arr:
        if x != "":
            ans.append([x,User.query.filter_by(username=x).first().rank])
    return ans

def friendList(name):
    arr = User.query.filter_by(username=name).first().friends.split("|")
    ans = []
    for x in arr:
        if x != "":
            ans.append([x,User.query.filter_by(username=x).first().rank])
    return ans

#count friends
def countFriends(name):
    arr = User.query.filter_by(username=name).first().friends.split("|")
    ans = 0
    for x in arr:
        if x != "" and x!= " ":
            ans += 1
    return ans

#remove user from request list
def removeFromRequest(remover, removed):
    arr = User.query.filter_by(username=remover).first().requests.split("|")
    ans = ""
    for x in range(len(arr)):
        if arr[x] != removed and arr[x] != "":
            if x == len(arr)-1:
                ans += arr[x]
            else:
                ans += (arr[x] + "|")
    User.query.filter_by(username=remover).first().requests = ans
    db.session.commit()

#add user to friend list
def addToFriends(adder, added):
    User.query.filter_by(username=adder).first().friends += (added + "|")
    User.query.filter_by(username=added).first().friends += (adder + "|")
    db.session.commit()

#count number of right answers
def countRight(arr):
    ans = 0
    for x in arr:
        if x == 1:
            ans += 1
    return ans

#marking algorithm
def markTest(answer, level, QSR):
    netSR = 0
    Ra = User.query.filter_by(username=session["username"]).first().sr
    for x in range(len(answer)):
        A = answer[x]
        D = level[x]
        if answer[x] == 1:
            User.query.filter_by(username=session["username"]).first().correct += 1
            db.session.commit()
            netSR += A*int(D)
        else:
            User.query.filter_by(username=session["username"]).first().incorrect += 1
            db.session.commit()
            Rq = QSR[x]
            punishConstant = 1 - (1/(1+(10**((Rq-Ra)/500))))
            netSR += (A*(6-D))/punishConstant
    return int(round(netSR))

#updates user SR
def updateSR(netSR):
    currentSR = User.query.filter_by(username=session["username"]).first().sr
    if netSR < -150:
        netSR = -150
    newSR = currentSR + netSR
    if newSR < 0:
        newSR = 0
    User.query.filter_by(username=session["username"]).first().sr = newSR
    if newSR < 500:
        User.query.filter_by(username=session["username"]).first().rank = "Byte"
    elif newSR > 499 and newSR < 1000:
        User.query.filter_by(username=session["username"]).first().rank = "Kilo"
    elif newSR > 999 and newSR < 1500:
        User.query.filter_by(username=session["username"]).first().rank = "Mega"
    elif newSR > 1499 and newSR < 2000:
        User.query.filter_by(username=session["username"]).first().rank = "Giga"
    elif newSR > 1999 and newSR < 2500:
        User.query.filter_by(username=session["username"]).first().rank = "Tera"
    elif newSR < 2499 and newSR > 3000:
        User.query.filter_by(username=session["username"]).first().rank = "Master"
    else:
        arr = sortLB()
        top = 0
        for x in range(3):
            if arr[x][0] == session["username"]:
                top = x+1
                break
        if top == 0:
            User.query.filter_by(username=session["username"]).first().rank = "Grandmater"
        else:
            User.query.filter_by(username=session["username"]).first().rank = "Top {}".format(top)
    db.session.commit()
    if newSR > User.query.filter_by(username=session["username"]).first().highestSR:
        User.query.filter_by(username=session["username"]).first().highestSR = newSR
        User.query.filter_by(username=session["username"]).first().highestRank = findRank(newSR)
        db.session.commit()
    return newSR

def findRank(elo):
    if elo < 500:
        return "Byte"
    elif elo > 499 and elo < 1000:
        return "Kilo"
    elif elo > 999 and elo < 1500:
        return "Mega"
    elif elo > 1499 and elo < 2000:
        return "Giga"
    elif elo > 1999 and elo < 2500:
        return "Tera"
    elif elo < 2499 and elo > 3000:
        return "Master"
    else:
        arr = sortLB()
        top = 0
        for x in range(3):
            if arr[x][0] == session["username"]:
                top = x+1
                break
        if top == 0:
            return "Grandmaster"
        else:
            return "Top {}".format(top)

def findAccuracy(name):
    r = User.query.filter_by(username=name).first().correct
    w = User.query.filter_by(username=name).first().incorrect
    if r == 0 and w == 0:
        return "N/A"
    acc = str(int(round((r/(r+w))*100))) + "%"
    return acc

#if __name__ == "__main__":
#    app.run()
