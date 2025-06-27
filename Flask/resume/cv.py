from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# БД
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cv.db' # 3-ри слеша
db = SQLAlchemy(app)

# Опис моделей
class Skill(db.Model):
    __tablename__ = 'skill'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.Text)
    
    def __repr__(self):
        return f"<Skill - {self.name}>"

    
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/skills")
def skills():
    return render_template('skills.html')

@app.route("/experience")
def experience():
    return render_template('experience.html')

if __name__ == '__main__':
    app.run(debug=True)

"""
Для інсталювання БД та таблиць:
>>> from cv import app, db, Skill # Імпортуємо app, db і модель
>>> app.app_context().push()      # Активуємо контекст Flask
>>> db.create_all()
з'явиться новий каталог "instance" з створенною БД
"""

