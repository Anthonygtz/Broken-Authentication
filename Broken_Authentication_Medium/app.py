from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USERNAME = "The_living_Tribunal-2022"
PASSWORD = "Sh@mb@11@"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    error_message = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('admin_panel'))
        elif username == USERNAME:
            error_message = "Invalid credentials. "
        elif password == PASSWORD:
            error_message = "Invalid credentials. "
        else:
            error_message = "Invalid credentials."

    return render_template("login.html", error_message=error_message)

@app.route("/admin-panel/")
def admin_panel():
    return render_template("admin_panel.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)