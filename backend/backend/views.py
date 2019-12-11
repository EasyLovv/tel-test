"""Views implementation."""
from flask import request
from flask_restful import Resource

from backend.app import mongo, config


class Games(Resource):
    """The view to work with all games."""
    def get(self):
        team_name = request.args.get('team_name')
        if team_name:
            return mongo.db.games.find({
                "competitions.competitors.team.name": team_name
            })
        return mongo.db.games.find()


class DirectGame(Resource):
    """The view to work with the direct game /games/{game_id}."""
    def get(self, game_id):
        mongo.db.games.delete_many({})
        return mongo.db.games.find_one({"id": game_id})

    def put(self, game_id):
        if request.headers.get("api_key", default="") != config.API_KEY:
            return {"status": "failed"}, 401
        game_data = request.get_json()
        game_data['id'] = game_id
        resp = mongo.db.games.update({'id': game_id}, game_data, upsert=True)

        if not resp['ok']:
            return {"status": "failed"}, 500

        if resp['updatedExisting']:
            status = 202
        else:
            status = 201

        return {"status": "success"}, status
