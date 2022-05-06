from flask import Flask,request,render_template

app=Flask(__name__)

app_scope="TEST APP SCOPE"

@app.route("/") #this is decorater
def index():
    var=request.args["test"]
    print(type(var))
    request_scope="TEST REQUEST SCOPE"
    print(request_scope)
    print( "Hello World")
    return "Hello World"
#
# @app.route("/calc")
# def calc():#using arguments
#     number_one=request.args["number_1"]
#     number_two=request.args["number_2"]
#     result=int(number_one)+int(number_two)
#     return f"{result}"

@app.route("/prism")
def calc_volume(): #http://127.0.0.1:5000/calc?number_1=10&number_2=5
    area=request.args["area"]
    height=request.args["height"]
    volume=int(area)*int(height)
    return f"{volume}"



@app.route("/calc/<number_one>/<number_two>")
def calc(number_one,number_two):
    #using parameteres(path parametres) http://127.0.0.1:5000/calc/10/5
    result=int(number_one)+int(number_two)
    #return f"{result}"

    #using dic for response get json type
    response={
        "result":result
    }
    print(type(response))
    return response

#get_user_profile_contact?userid=1 wenuwata
# @app.route("/user/<profile>/<contact>")
# def profile(profile,contact):
#     #using parameteres(path parametres)
#     result=contact
#     return f"{result}"


#get html tag
@app.route("/view")
def view():
    return "<h1>Hello World</h1>"

#get html file
# @app.route("/view_index")
# def view_from_file():
#     response=open("index.html").read()
#     return response
#
# #using render template
# @app.route("/view_index_2")
# def view_from_file_2():
#     return render_template("index.html")


@app.route("/view_index")
def view_from_file():
    name=request.args["name"]
    age=request.args["age"]
    response=open("index.html").read()
    response=response.replace("{{name}}",name)
    response=response.replace("{{age}}",age)
    return response

#using render template
@app.route("/view_index_2")
def view_from_file_2():
    return render_template("index.html")

@app.route("/view_form",methods=["GET","POST"])
def view_form():

    name="Empty"
    age="Empty"

    if request.method=="POST":
        if "name" in request.form:
            name=request.form["name"]
        if "age" in request.form:
            age=request.form["age"]

    return render_template("index.html",name=name,age=age)



print(app_scope)

if __name__=="__main__":
    app.run(debug=True)