from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "change-this-secret-key"  # replace in production
app.permanent_session_lifetime = timedelta(minutes=30)


@app.route("/")
def index():
    user = session.get("user")
    return render_template("index.html", user=user)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        # Demo-only authentication: single hardcoded user
        if username == "demo" and password == "securepass":
            session.permanent = True
            session["user"] = username
            flash("Secure cloud tunnel established.", "success")
            return redirect(url_for("dashboard"))

        flash("Invalid credentials. Try demo / securepass.", "error")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    user = session.get("user")
    if not user:
        flash("Please log in to access secure cloud resources.", "error")
        return redirect(url_for("login"))

    return render_template("dashboard.html", user=user)


@app.route("/logout")
def logout():
    session.clear()
    flash("Secure session closed.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
