from flask import Flask,render_template,request
import md5decr

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        #print(form_data)
        #print(request.form)
        a=form_data
        hash=a['Field1_name']
        decr=md5decr.tr(hash)

        ttr='''
        <center>

        <p><b> This is a look-up tool for typical unsalted MD5 cryptographic hashes. <br>The database currently contains 1.1+ trillion passwords. </p>

        <form action="/data/" method = "POST">
            <p>MD5 Hash <br><input type = "text" name = "Field1_name" /></p>
            <p><input type = "submit" value = "Submit" /></p>
        </form>
        '''
        return(ttr+decr)







app.run(host='localhost', port=5000, debug=True)
#app.run(host='localhost', port=80, debug=True)
