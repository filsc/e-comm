from flask import current_app as app, render_template

@app.route('/')
def index():
    context = dict()
    return render_template('app/templates/index.html', **context)

