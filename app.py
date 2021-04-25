from githubapi_handler import Api_handler, UsernameError, APILimitError
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/list/<username>")
def repo_list(username):
    try:
        api = Api_handler(username)
    except UsernameError:
        return jsonify({"Error" : "User not found"})
    except APILimitError:
        return jsonify({"Error" : "API rate limit exceeded"})
    return jsonify(api.get_list())


@app.route('/starsum/<username>')
def star_summary(username):
    try:
        api = Api_handler(username)
    except UsernameError:
        return jsonify({"Error" : "User not found"})
    except APILimitError:
        return jsonify({"Error" : "API rate limit exceeded"})
    return jsonify(api.get_starsum())


if __name__ == '__main__':
    app.run(debug=True)