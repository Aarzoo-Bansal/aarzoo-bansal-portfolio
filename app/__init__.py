import datetime
import os
from playhouse.shortcuts import model_to_dict
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import Model, CharField, TextField, DateTimeField, MySQLDatabase, SqliteDatabase
from functools import wraps

from app.data import PAGES, EXPERIENCES, PLACES, HOBBIES, EDUCATION

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase(
        'file:memory?mode=memory&cache=shared',
        uri=True
    )
else:
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

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline", pages=PAGES)


# i added the same validaiton logic as my portfolio. This makes it all centralized. So if you add more fields to the form, you can simply add them to the required_fields tuple. And if you ever create a new form, you can reuse this validation logic.
def validate_form(*required_fields):
    """Ensure the given form fields are present and non-empty, else return 400.

    @wraps preserves each view's name so Flask keeps distinct endpoints when
    this is applied to more than one route.
    """

    def decorator(view):
        @wraps(view)
        def wrapper(*args, **kwargs):
            invalid = []

            for field in required_fields:
                value = request.form.get(field, "").strip()

                if not value:
                    invalid.append(field)
                elif field == "email" and (
                    value.count("@") != 1
                    or value.startswith("@")
                    or value.endswith("@")
                ):
                    invalid.append(field)

            if invalid:
                return {"error": f"Invalid {', '.join(invalid)}"}, 400
            return view(*args, **kwargs)

        return wrapper

    return decorator

@app.route('/api/timeline_post', methods=['POST'])
@validate_form('name', 'email', 'content')
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
