from flask import Flask, render_template, request, url_for,jsonify,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users = all_users)

@app.route('/add', methods = ['POST'])
def add():
    username = request.form['username'].strip()
    if not username:
        return 'please insert your username to continue!'

    new_user = User(name = username)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('users'))

@app.route('/api/users')
def api_users():
    users = User.query.all()
    data = [{"id": user.id, "name": user.name} for user in users]
    return jsonify(data)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
