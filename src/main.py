from flask import render_template, request, redirect, url_for
from application.models import Item, ItemSchema
from application.config import app, db, mm


@app.route('/')
def index():
    incomplete = Item.query.filter_by(complete=False).all()
    complete = Item.query.filter_by(complete=True).all()
  
    return render_template('index.html', incomplete=incomplete, complete=complete)

@app.route('/add', methods=['POST'])
def add():
    item = Item(text=request.form['todoitem'], quantity=1, complete=False)
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):
    item = Item.query.filter_by(id=int(id)).first()
    item.complete = True
    db.session.commit()
    return redirect(url_for('index'))
