from githubapi_handler import Api_handler
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def first_page():
    return jsonify({"Error" : "User not specified"})


@app.route("/list/<username>")
def repo_list(username):
    try:
        api = Api_handler(username)
    except Exception as e:
        return jsonify({"Error" : str(e)})
    return jsonify(api.get_list())


@app.route('/starsum/<username>')
def star_summary(username):
    try:
        api = Api_handler(username)
    except Exception as e:
        return jsonify({"Error" : str(e)})
    return jsonify(api.get_starsum())


if __name__ == '__main__':
    app.run()