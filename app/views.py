
from app import app

from flask import render_template

@app.route('/')
def home():
    return render_template("/public/index.html")
@app.route('/gallery')
def gallery():
    return render_template("/public/gallery.html")


@app.route('/ourstory')
def ourstory():
    return render_template("/public/ourstory.html")

@app.route('/partners')
def partner():
    return render_template("/public/partners.html")

@app.route('/blog')
def blog():
    return render_template("/public/blog.html")

@app.route('/contact')
def contactus():
    return render_template("/public/contact.html")

@app.route('/blogtitle')
def blogtitle():
    return render_template("/public/blogtitle.html")

@app.route('/faqs')
def faqs():
    return render_template("/public/faqs.html")

@app.route('/garment')
def garment():

    return render_template("/public/garment.html")


@app.route('/policies')
def policies():
    return render_template("/public/policies.html")


@app.route('/our_social')
def our_social():
    return render_template("/public/our_social.html")


@app.route('/dashboard')
def dashboard():
    return render_template("admin/dashboard.html")

@app.route('/Request_callback')
def Request_callback():
    return render_template("public/Request_callback.html")
