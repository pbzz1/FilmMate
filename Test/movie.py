from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
api_key = "046cd9a228db2149662380384cae4622"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/signin/')
def signin():
    return render_template('signin.html')

@app.route('/search/')
def search():
    query = request.args.get('query', '')
    if query:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}&language=ko-KR"
        response = requests.get(url)
        data = response.json()
        return render_template('search_results.html', query=query, results=data['results'])
    return render_template('search.html')

@app.route('/search/results/')
def search_results():
    query = request.args.get('query', '')
    return render_template('search_results.html', query=query)

@app.route('/setting/')
def setting():
    return render_template('setting.html')

@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    return render_template('movie_detail.html', movie_id=movie_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
