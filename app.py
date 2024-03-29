from flask import Flask,jsonify,render_template, request
from flaskext.mysql import MySQL




app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'flaskapp'
app.config['MYSQL_DATABASE_PORT']=3306

mysql = MySQL(app)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        #print (app.config)
        details = request.form
        name = details['Name']
        color = details['FavColor']
        animal = details['CatDog']
        print(app.config)
        print (name)
        cursor = mysql.get_db().cursor()
        cursor.execute("INSERT INTO Data(Name,Favorite_Color,CatOrDog)  VALUES (%s, %s, %s)", (name, color, animal))
        mysql.get_db().commit()
        cursor.close()
        return render_template('success.html')
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)