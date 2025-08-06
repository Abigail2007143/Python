from flask import Flask

app=Flask(__name__)

#endpoint, web services 

@app.route("/ver")
def saludar ():
   return"<h1>hola mundo</H1>"