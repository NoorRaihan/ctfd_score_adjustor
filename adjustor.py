from CTFd.utils.decorators import admins_only
from CTFd.models import Teams, Users, Awards, db
from flask import jsonify, request
import datetime

class ResponseCode:
    ERROR = "000198"
    SUCCESS = "00000"

def load(app):
    @app.route('/api/score/adjust')
    @admins_only
    def manipulate():
        data = request.get_json()
        user_id = data.get("user_id")
        team_id = data.get("team_id")
        points = data.get("points")
        reason = data.get("reason", "Manual adjustment")

        if not points or (not user_id and not team_id):
            return jsonify({"responseCode" : ResponseCode.ERROR, "message": "Missing required fields"}), 400

        if team_id:
            query_id = Teams.query.get(team_id)
            if not query_id:
                return jsonify({"responseCode" : ResponseCode.ERROR, "message": f"{team_id} not exists"}), 404
        else :
            query_id = Users.query.get(user_id)
            if not query_id:
                return jsonify({"responseCode" : ResponseCode.ERROR, "message": f"{user_id} not exists"}), 404

        award = Awards(
            user_id=user_id,
            team_id=team_id,
            name='Score Adjustment',
            description=reason,
            value=points,
            date=datetime.datetime.now(datetime.timezone.utc)
        )
        db.session.add(award)
        db.session.commit()

        return jsonify({"responseCode": ResponseCode.SUCCESS, "message" : "works"})