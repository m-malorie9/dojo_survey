from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)   
app.secret_key = 'peanut butter jelly time'

@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/handle_form', methods = ['POST'])
def handle_form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/form_results')


@app.route('/form_results')
def form_results():
    return render_template('form.html', name = session['name'], location = session['location'], language = session['language'], comment = session['comment'])






if __name__ == "__main__":
    app.run(debug=True)