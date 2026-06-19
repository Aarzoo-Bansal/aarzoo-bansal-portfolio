import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

PAGES = [
    {"name": "Home", "url": "/"},
    {"name": "Experience", "url": "/experience"},
    {"name": "Education", "url": "/education"},
    {"name": "Hobbies", "url": "/hobbies"},
    {"name": "Map", "url": "/map"},
]

@app.route('/')
def index():
    return render_template('index.html', title="Aarzoo Bansal", url=os.getenv("URL"), pages=PAGES)


@app.route('/experience')
def experience():
    return render_template('experience.html', title="Experience", pages=PAGES)


@app.route('/education')
def education():
    return render_template('education.html', title="Education", pages=PAGES)


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", pages=PAGES)


@app.route('/map')
def map():
    return render_template('map.html', title="Map", pages=PAGES)
