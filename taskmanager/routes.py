from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")

# If statement checking if method from our form is 'POST'.
# If so, it adds a category, created by user, adds to our database.
# Redirects user back to 'categories.hmtl' when category is added.
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")