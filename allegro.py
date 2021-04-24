from flask import Flask, render_template, jsonify
import requests
import os
app = Flask(__name__)

def get_repos_dict(username):
    flag = True
    page = 1
    repos_list = []
    star_sum = 0
    while (flag):
        query_url = f"https://api.github.com/users/{username}/repos?page={page}"
        repos = requests.get(query_url).json()
        if len(repos) == 0:
            flag = False
        for repo in repos:
            repos_list.append({"name":repo["name"], "stargazers_count": repo["stargazers_count"]})
            star_sum += repo["stargazers_count"]
        page += 1
    return repos_list, star_sum

@app.route("/list/<username>")
def repo_list(username):
    return jsonify(get_repos_dict(username)[0])

@app.route('/starsum/<username>')
def star_summary(username):
    i = 0
    return jsonify({"star_sum": get_repos_dict(username)[1]})


if __name__ == '__main__':
    app.run(debug=True)