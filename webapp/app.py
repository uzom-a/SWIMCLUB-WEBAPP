from flask import Flask, session, render_template,request #you need to import session(this is a dict) to allow the global variable

import os
import swimclub
TEMPLATES = "templates/"
app = Flask(__name__)
app.secret_key = "You will never guess"

@app.get("/") #this takes you to the default web page
def index():
    return render_template(#there is no need to specify the templates folder here because the imported function will check that by default.
       "index.html",
       title="Welcome to the Swimclub webapp!!",
       )

def populate_data():
    if "swimmers" not in session: #this ensures previous data does not enter again
     swim_files = os.listdir(swimclub.FOLDER) 
     swim_files.remove(".DS_Store")
     session["swimmers"] = {}
     for file in swim_files: # loop through each file
        name, *_ = swimclub.read_swim_data(file) # read swimmer names from file
        if name not in session["swimmers"]: # check if names are already in the list
           session["swimmers"][name] = []
        session["swimmers"][name].append(file)
    #this function does not need to return anything


@app.get("/swimmers") #this takes you to the swimmers website 
def display_swimmers():
    populate_data()
    return render_template(
        "select.html",
        title="Choose a swimmer",
        select_id="swimmer",
        url="/showfiles",
        data=sorted(session["swimmers"]),
    )
@app.post("/showfiles")#you need this because the select.html uses POST
def display_swimmer_files():
        populate_data()
        name = request.form["swimmer"] #this stores the swimmers name from the select_id key(swimmer)
        return render_template(
            "select.html",
            title="Select an event", 
            url="/showbarchart",
            select_id = "file",#give the <select> tag a name.
            data=session["swimmers"][name],#pass in the data needed for the next drop-down list which in this case is the list of filenames associated with each swimmer
        )

@app.post("/showbarchart")
def show_bar_chart():
    file_id = request.form["file"]#Grab the value of the "file"select_id from the html form
    location = swimclub.produce_bar_chart(file_id, TEMPLATES)#this takes in the filename and changes the location where the data is saved
    return render_template(location.split("\\")[-1])

if __name__ == "__main__":
    app.run(debug=True)