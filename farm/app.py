from flask import Flask, render_template, request, redirect, url_for, session,jsonify
from chat import get_response
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
  
  
app = Flask(__name__)
  
  
app.secret_key = 'xyzsdfg'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'user-system'
  
mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/fertilizer")
def fertilizer():
    return render_template("fertilizer.html")

@app.route("/Seeds")
def seeds():
    return render_template("Seeds.html")

@app.route("/Programs")
def programs():
    return render_template("Programs.html")

@app.route("/panel")
def panel():
    return render_template("panel.html")

  

@app.route('/farmerlogin', methods =['GET', 'POST'])
def farmerlogin():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM farmer WHERE email = %s AND password = %s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('Farmer/farmerhome.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('Farmer/login.html', mesage = mesage)
  

  
@app.route('/farmerregister', methods =['GET', 'POST'])
def farmerregister():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM farmer WHERE email = %s', (email, ))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not userName or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO farmer VALUES (NULL, %s, %s, %s)', (userName, email, password, ))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('Farmer/register.html', mesage = mesage)


@app.route('/sellerlogin', methods =['GET', 'POST'])
def sellerlogin():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM seller WHERE email = %s AND password = %s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('seller/sellerhome.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('seller/login.html', mesage = mesage)
  

  
@app.route('/sellerregister', methods =['GET', 'POST'])
def sellerregister():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM seller WHERE email = %s', (email, ))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not userName or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO seller VALUES (NULL, %s, %s, %s)', (userName, email, password, ))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('seller/register.html', mesage = mesage)

@app.route('/adminlogin', methods =['GET', 'POST'])
def adminlogin():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('admin/adminhome.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('admin/login.html', mesage = mesage)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('index'))


@app.route('/farmerhome')
def farmerhome():
    return render_template('Farmer/farmerhome.html')


@app.route('/farmerpost', methods =['GET', 'POST'])
def farmerpost():
    mesage = ''
    if 'userid' in session:
        if request.method == 'POST' :       
            CropName = request.form['CropName']
            quantity = request.form['quantity']
            contact = request.form['contact']
            remarks = request.form['remarks']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            if not re.match(r'^\d{10}$', contact):
                mesage = 'Invalid phone number !'
            
            elif(quantity<= r'0'):
                mesage = 'Quantity cannot be zero!'

            elif(remarks.strip() == ""):
                mesage="Enter your name and address"
            
            else:
                cursor.execute('INSERT INTO farmerproduct (CropName, quantity, contact, remarks, userid) VALUES (%s, %s, %s, %s,%s)', (CropName,quantity,contact,remarks,session['userid']))
                mysql.connection.commit()
                mesage = 'You have successfully posted !'
        return render_template('Farmer/farmerpost.html', mesage = mesage)
    else:
        return render_template('Farmer/login.html')



@app.route('/fpostlist')
def fpostlist():
    posts=''
    if 'userid' in session:
        id = session['userid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(r'SELECT CropName, quantity, contact, remarks FROM farmerproduct WHERE userid = %s', (id,))
        posts = cursor.fetchall()
        print(posts)
        return render_template('Farmer/fpostlist.html', posts = posts)
    else:
        return render_template('Farmer/login.html', posts = posts)


@app.route('/forderlist')
def forderlist():
    posts=''
    if 'userid' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT CropName, quantity, contact, remarks FROM sellerpost')
        posts = cursor.fetchall()
        print(posts)
        return render_template('Farmer/forderlist.html', posts = posts)
    else:
        return render_template('Farmer/login.html', posts = posts)
        

@app.route('/complaint', methods =['GET', 'POST'])
def complaint():
    mesage = ''
    if 'userid' in session:
        if request.method == 'POST' :       
            fcomplain = request.form['fcomplain']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            if(fcomplain.strip() == ""):
                mesage='Please enter your queires and complains'

            else:
                cursor.execute('INSERT INTO complaint (fcomplain, userid) VALUES (%s,%s)', (fcomplain,session['userid']))
                mysql.connection.commit()
                mesage = 'You have successfully posted !'
        else :
            mesage = 'Please fill out the form !'
        return render_template('Farmer/complaint.html', mesage = mesage)

@app.route('/fcomplaintlist')
def fcomplaintlist():
    posts=''
    if 'userid' in session:
        id = session['userid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(r'SELECT fcomplain FROM complaint WHERE userid = %s', (id,))
        posts = cursor.fetchall()
        print(posts)
        return render_template('Farmer/fcomplaintlist.html', posts = posts)
    else:
        return render_template('Farmer/login.html', posts = posts)
        

@app.route('/fnotification')
def fnotification():
   posts=''
   if 'userid' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT adminpost FROM adminpost')
        posts = cursor.fetchall()
        print(posts)
        return render_template('Farmer/fnotification.html', posts = posts)
   else:
        return render_template('Farmer/login.html', posts = posts)
        
    

@app.route('/adminhome')
def adminhome():
    return render_template('admin/adminhome.html')


@app.route('/apost', methods =['GET', 'POST'])
def apost():
    mesage = ''
    if 'userid' in session:
        if request.method == 'POST' :       
            adminpost = request.form['adminpost']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            if(adminpost.strip() == ""):
                mesage='Please enter your queires and complains'
            else:
                cursor.execute('INSERT INTO adminpost (adminpost, userid) VALUES (%s,%s)', (adminpost,session['userid']))
                mysql.connection.commit()
                mesage = 'You have successfully posted !'
        else :
            mesage = 'Please fill out the form !'
        return render_template('admin/apost.html', mesage = mesage)
    else:
        return render_template('admin/login.html', mesage = mesage)


@app.route('/fqueries')
def fqueries():
   posts=''
   if 'userid' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT fcomplain FROM complaint')
        posts = cursor.fetchall()
        print(posts)
        return render_template('admin/fqueries.html', posts = posts)
   else:
        return render_template('admin/login.html', posts = posts)
   
@app.route('/squeries')
def squeries():
   posts=''
   if 'userid' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT scomplain FROM sellercomplaint')
        posts = cursor.fetchall()
        print(posts)
        return render_template('admin/squeries.html', posts = posts)
   else:
        return render_template('admin/login.html', posts = posts)
   
@app.route('/apostlist')
def apostlist():
    posts=''
    if 'userid' in session:
        id = session['userid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(r'SELECT adminpost FROM adminpost WHERE userid = %s', (id,))
        posts = cursor.fetchall()
        print(posts)
        return render_template('admin/apostlist.html', posts = posts)
    else:
        return render_template('admin/login.html', posts = posts)






@app.route('/sellerhome')
def sellerhome():
    return render_template('seller/sellerhome.html')

@app.route('/orderpost',methods =['GET', 'POST'] )
def orderpost():
    mesage = ''
    if 'userid' in session:
        if request.method == 'POST' :       
            CropName = request.form['CropName']
            quantity = request.form['quantity']
            contact = request.form['contact']
            remarks = request.form['remarks']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            if not re.match(r'^\d{10}$', contact):
                mesage = 'Invalid phone number !'
            
            elif(quantity<= r'0'):
                mesage = 'Quantity cannot be zero!'

            elif(remarks.strip() == ""):
                mesage="Enter your name and address"

            else:
                cursor.execute('INSERT INTO sellerpost (CropName, quantity, contact, remarks, userid) VALUES (%s, %s, %s, %s,%s)', (CropName,quantity,contact,remarks,session['userid']))
                mysql.connection.commit()
                mesage = 'You have successfully posted !'
        return render_template('seller/orderpost.html', mesage = mesage)
    else:
        return render_template('seller/login.html')

    
    
    
@app.route('/sorderlist')
def sorderlist():
    if 'userid' in session:
        id = session['userid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(r'SELECT CropName, quantity, contact, remarks FROM sellerpost WHERE userid = %s', (id,))
        posts = cursor.fetchall()
        print(posts)
        return render_template('seller/sorderlist.html', posts = posts)
    else:
        return render_template('seller/login.html')


@app.route('/spostlist')
def spostlist():
   posts=''
   if 'userid' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT CropName, quantity, contact, remarks FROM farmerproduct')
        posts = cursor.fetchall()
        print(posts)
        return render_template('seller/spostlist.html', posts = posts)
   else:
        return render_template('seller/login.html', posts = posts)
   
@app.route('/scomplaint',methods =['GET', 'POST'] )
def scomplaint():
    mesage = ''
    if 'userid' in session:
        if request.method == 'POST' :       
            scomplain = request.form['scomplain']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            if(scomplain.strip() == ""):
                mesage="Enter your name and address"
            else:
                cursor.execute('INSERT INTO sellercomplaint (scomplain, userid) VALUES (%s,%s)', (scomplain,session['userid']))
                mysql.connection.commit()
                mesage = 'You have successfully posted !'
        else :
            mesage = 'Please fill out the form !'
        return render_template('seller/scomplaint.html', mesage = mesage)
    else:
        return render_template('seller/login.html')

        


@app.route('/scomplaintlist')
def scomplaintlist():
    if 'userid' in session:
        id = session['userid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(r'SELECT scomplain FROM sellercomplaint WHERE userid = %s', (id,))
        posts = cursor.fetchall()
        print(posts)
        return render_template('seller/scomplaintlist.html', posts = posts)
    else:
        return render_template('seller/login.html')


@app.route('/snotification')
def snotification():
   posts=''
   if 'userid' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT adminpost FROM adminpost')
        posts = cursor.fetchall()
        print(posts)
        return render_template('seller/snotification.html', posts = posts)
   else:
        return render_template('seller/login.html', posts = posts)






@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

    
if __name__ == "__main__":
    app.run(debug=True)