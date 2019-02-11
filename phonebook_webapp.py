from flask import Flask, render_template, request
import os
import engine

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("pages/index.html")

@app.route('/home')
def home():
    return render_template("pages/index.html")

@app.route('/findperson', methods=['GET','POST'])
def find_person():
    if request.method == 'GET':
        return render_template("pages/findperson.html")
    elif request.method == 'POST':
        surname = request.form.get('name_p')
        option = request.form.get('loc_select')
        if option == 'city':
            city = request.form.get('loc_p')
            postcode = None
        elif option == 'postcode':
            postcode = request.form.get('loc_p')
            city = None
        search = engine.main_p(surname, postcode, city)
        return render_template('pages/findperson.html', search=search)

    else:
        return "Sorry something went wrong with the request"

@app.route('/findbusiness', methods=['GET','POST'])
def find_business():
    if request.method == 'GET':
        return render_template('pages/findbusiness.html')
    elif request.method == 'POST':
        biz_identity = request.form.get('name_type_select_b')
        biz_loc = request.form.get('loc_select')
        print(biz_identity, biz_loc)

        if biz_identity == 'biz_name':
            biz_name = request.form.get('name_type_b')
            biz_type = None
            print(biz_identity, biz_loc)
        elif biz_identity == 'biz_type':
            biz_type = request.form.get('name_type_b')
            biz_name = None
        if biz_loc == 'city':
            city = request.form.get('loc_b')
            postcode = None
            print(biz_identity, biz_loc)
        elif biz_loc == 'postcode':
            postcode = request.form.get('loc_b') 
            city = None
        # unassigned = if v is None for v in [biz_name, biz_type, postcode, city]
        # vars for vars in list(biz_name, biz_type, postcode, city)
        search = engine.main_b(biz_name, biz_type, postcode, city)
        return render_template('pages/findbusiness.html', search=search)
    else:
        return "Sorry something went wrong with the request"

if __name__ == "__main__":
    app.run()