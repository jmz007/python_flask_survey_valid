from flask import Flask, flash, render_template, request, redirect, session, url_for


app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/', methods=['get'])
def index():
    return render_template('index.html')


@app.route('/formresults', methods=['POST'])
def results():
    
    if len(request.form['name']) < 1:
        flash("Name cannot be blank!")
        error = True

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    if len(request.form['comment']) > 120:
        flash("Comment cannot exceed 120 characters!")
        error = True
    elif len(request.form['comment']) < 1:
        flash('Comment cannot be blank')
        error = True
    else:
        session['comment'] = request.form['comment']
    if error:
        return redirect('/')

    return render_template('formresults.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])

@app.route('/formresults')
def danger():
    print ("user was an asshole")
    return redirect('/')

@app.route('/danger')
def dangerdanger():
    print ("user still an asshole")
    return redirect('/')
    
if __name__=='__main__':
    app.run(debug=True)
