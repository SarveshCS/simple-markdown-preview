from flask import Flask, render_template, request, redirect, url_for, make_response
import markdown

app = Flask(__name__)

@app.route('/')
def index():
    theme = request.cookies.get('theme', 'light')
    return render_template('home.html', theme=theme)

@app.route('/home')
def home():
    theme = request.cookies.get('theme', 'light')
    return render_template('home.html', theme=theme)

@app.route('/preview', methods=['POST'])
def preview():
    content = request.form['content']
    html_content = markdown.markdown(content)
    return html_content

@app.route('/switch-theme/<theme>')
def switch_theme(theme):
    resp = make_response(redirect(url_for('home')))
    resp.set_cookie('theme', theme)
    return resp

if __name__ == '__main__':
    app.run()