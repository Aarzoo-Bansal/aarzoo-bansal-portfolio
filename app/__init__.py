import datetime
import os
from playhouse.shortcuts import model_to_dict
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import Model, CharField, TextField, DateTimeField, MySQLDatabase

from app.data import PAGES, EXPERIENCES, PLACES, HOBBIES, EDUCATION

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                     user=os.getenv("MYSQL_USER"),
                     password=os.getenv("MYSQL_PASSWORD"),
                     host=os.getenv("MYSQL_HOST"),
                     port=3306
                     )

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    create_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/')
def index():
    return render_template('index.html', title="Aarzoo Bansal", url=os.getenv("URL"), pages=PAGES)


@app.route('/experience')
def experience():
    return render_template('experience.html', title="Experience",
                           pages=PAGES, experiences=EXPERIENCES)


@app.route('/education')
def education():
    return render_template('education.html', title="Education",
                           pages=PAGES, education=EDUCATION)


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies",
                           pages=PAGES, hobbies=HOBBIES)


@app.route('/map')
def map():
    return render_template('map.html', title="Map", pages=PAGES, places=PLACES)

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)


@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts' : [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.create_at.desc())
        ]
    }

@app.route('/api/timeline_post/<int:post_id>', methods=['DELETE'])
def delete_time_line_post(post_id):
    rows_deleted = TimelinePost.delete_by_id(post_id)
    if rows_deleted == 0:
        return { 'error': f'Timeline post with id {post_id} not found'}, 404
    return {'message': f'Timeline post {post_id} deleted successfully'}