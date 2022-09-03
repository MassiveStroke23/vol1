from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("fnx_index.html")


@app.route("/home_page", methods=["POST", "GET"])
def home_page_v2():
    a = request.form["Stacking"]
    b = request.form["Material"]
    c = request.form["PlyThickness"]
    print(request.form["Stacking"])
    print(type(request.form["Stacking"]))
    print(request.form["Material"])
    print(request.form["PlyThickness"])
    return render_template("fnx_index.html", stack=a, mat=b, thick=c)


if __name__ == "__main__":
    app.run(debug=True)