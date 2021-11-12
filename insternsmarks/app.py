from flask import *
from flask.templating import render_template
import sqlite3
app=Flask(__name__)




@app.route('/')
def index():
    connection = sqlite3.connect("intern_detials.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("select * from Int_Info ORDER BY id DESC")
    rows = cursor.fetchall()
    return render_template('index.html',rows=rows)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/contact",methods = ["POST"])
def contacts():
    msg = "msg"

    email=request.form["email"]
    name=request.form['name']

    return (email)


@app.route('/about_us')
def about():
    return render_template('about.html')

@app.route('/add')
def add():
    return render_template('addpost.html')
@app.route('/asdfghjkl')
def addsss():
    return render_template('asdfghjkl.html')

@app.route("/asdfghjkl",methods = ["POST"])
def consssasd():
    ids="Admin@12"
    pas="Password"
    id=request.form["id"]
    passs=request.form["pass"]
    if(id==ids and pas==passs):
        return render_template('addpost.html')
    return render_template('index.html')
@app.route('/deleterecord')
def rem():
    return render_template('remove.html')
@app.route("/deleterecord",methods = ["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("intern_detials.db") as connection:

        cursor = connection.cursor()
        cursor.execute("select * from Int_Info where id=?", (id,))
        rows = cursor.fetchall()
        if not rows == []:

            cursor.execute("delete from Int_info where id = ?",(id,))
            msg = "Student detial successfully deleted"
            return render_template('success_record.html')

        else:
            msg = "can't be deleted"
            return ('not done')
@app.route("/add",methods = ["POST"])
def cons():
    msg = "msg"


    if request.method == "POST":
        try:
            title=request.form["title"]
            subtitle=request.form["subtitle"]
            des=request.form["des"]

            link=request.form["link"]



            with sqlite3.connect("intern_detials.db") as connection:

                cursor = connection.cursor()

                cursor.execute("INSERT into Int_info (title,subtitle,des,link) values (?,?,?,?)",(title,subtitle,des,link))
                connection.commit()
                msg = "Student detials successfully Added"
        except:
            connection = sqlite3.connect("/intern_detials.db")
            connection.rollback()
            msg = "We can not add Student detials to the database"
        finally:
            return render_template("success_record.html",msg = msg)





@app.route('/post/<int:id>')
def post(id):

    connection = sqlite3.connect("intern_detials.db")

    cursor = connection.cursor()
    cursor.execute("select * from Int_info where id=?", (id,))
    rows = cursor.fetchall()
    out = [item for t in rows for item in t]
    print(out[1])
    dict={        'title':out[1],        'subtitle':out[2]    ,    'link':out[4],        'des':out[3]    }
    return render_template('post.html', post=dict)
if __name__=='__main__':
    app.run(debug=True)
