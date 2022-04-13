from flask import Flask, after_this_request, render_template, request, send_file
app = Flask(__name__)
app.secret_key = 'dev'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return "merhaba"
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    