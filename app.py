from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__) #Create Flask object app

api = Api(app) #creating api object wrapping app as API

episode_args = reqparse.RequestParser() #creating arguments for the episode 
#adding required arguments 
episode_args.add_argument(name="id", type=int,help="Episode's id", required=True)
episode_args.add_argument(name="name", type=str, help="name of episode", required=True)
episode_args.add_argument(name="listens", type=int, help="Number of listens")
episode_args.add_argument(name="likes", type=int, help="Number of likes")



episodes = {}
class episode(Resource): #Create class episode inheriting from Resource class to handle episode requests
    def get(self, episode_id):
        """"
        Override get method from Resource class for class episode takes in self and episode_id
        """
        args = episode_args.parse_args()
        return {episode_id: args}

    def put(self):
        pass

api.add_resource(episode, "/episode/<int:id>") #adding episode class to resource with an endpoint /episode/<episode_id>

@app.route('/')
def home():
   return "Welcome to my Podcast World!"


if __name__ == "__main__":
    app.run(debug="True")