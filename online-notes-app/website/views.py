from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import null
from .models import Note
from . import db
import json

"""
    Blueprints basically means that it contains a bunch of routes or urls inside of it
"""

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])  # "Decorator"
@login_required
def home():
    if request.method == 'POST':
        data = request.form.get('note')

        if len(data) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=data, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category='success')

            return redirect(url_for('views.home'))

    return render_template('home.html', user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    note_id = note['noteId']
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

# @views.route('/help')
# def help():
#     return "<h1>Fuck you</h1>"
