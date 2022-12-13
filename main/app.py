from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__, static_folder="static")


@app.route('/static/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico')


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        data = request.get_json()
        return data.get('text')
    if request.method == 'GET':
        return render_template('test.html')
