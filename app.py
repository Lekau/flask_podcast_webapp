from flask import Flask
from flask_restful import Api, Resource 

app = Flask(__name__) #Create Flask object app

api = Api(app) #creating api object wrapping app as API

class helloWorld(Resource): #Create class helloWorld inheriting from Resource class
    def get(self): #Override get method from Resource class for class helloWorld
        hello = {"Method":"Hello Lekau, you have just handled a GET request!"} #Create dict to return when get request is made
        return hello 

    def post(self):
        post_data = {"method":"Hello Lekau, you have just handled a POST request!"}
        return post_data

api.add_resource(helloWorld, "/hello") #adding helloWorld class to resource with an endpoint /hello

@app.route('/')
def hello_world():
   return "Hello World!"


if __name__ == "__main__":
    app.run(debug="True")