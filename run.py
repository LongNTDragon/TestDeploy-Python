import json
import os

from flask import Flask, jsonify, render_template, request, url_for
from api.expert_controller import expert01, expert02, expert03, expert04, expert05
from api.parent_controller import parent01, parent03, parent04

app = Flask(__name__)
TMP_PATH = os.path.join(app.root_path, "static", "cache", "")


@app.template_filter("css")
def static_file_filter_css(filename):
    return url_for("static", filename=f"css/{filename}")


@app.template_filter("font")
def static_file_filter_font(filename):
    return url_for("static", filename=f"assets/fonts/{filename}")


@app.template_filter("img")
def static_file_filter_img(filename):
    return url_for("static", filename=f"assets/images/{filename}")


@app.template_filter("img_2x")
def static_file_filter_img_2x(filename):
    name = filename.split(".")[0]
    type = filename.split(".")[1]
    return url_for("static", filename=f"assets/images/{name}@2x.{type}")


@app.template_filter("img_3x")
def static_file_filter_img_3x(filename):
    name = filename.split(".")[0]
    type = filename.split(".")[1]
    return url_for("static", filename=f"assets/images/{name}@3x.{type}")


@app.route('/submit_data', methods=["POST"])
def submit_data():
    data = request.json
    with open(f"{TMP_PATH}{data['header']}", "w") as file:
        json.dump(data, file)
    return jsonify({"status": "success",
                    "message": "Data received and stored in session"})


@app.route('/<string:x>')
def show_template(x):
    if os.path.isfile(f"{TMP_PATH}{x}"):
        with open(f"{TMP_PATH}{x}", "r") as file:
            data = json.load(file)
    else:
        return "No data found", 400

    return render_template(f"{x}.html", **data)

@app.route('/')
def show_home():
    return render_template(f"index.html")

@app.route("/expert_01", methods=['POST'])
def reportExpert01():
    return expert01()

@app.route("/expert_02", methods=['POST'])
def reportExpert02():
    return expert02()

@app.route("/expert_03", methods=['POST'])
def reportExpert03():
    return expert03()

@app.route("/expert_04", methods=['POST'])
def reportExpert04():
    return expert04()

@app.route("/expert_05", methods=['POST'])
def reportExpert05():
    return expert05()

@app.route("/parent_01", methods=['POST'])
def reportParent01():
    return parent01()

@app.route("/parent_03", methods=['POST'])
def reportParent03():
    return parent03()

@app.route("/parent_04", methods=['POST'])
def reportParent04():
    return parent04()

if __name__ == '__main__':
    app.run(port=8888, debug=True)
