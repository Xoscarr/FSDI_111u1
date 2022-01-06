from flask import request 
from datetime import datetime

from app import app, db 
from app.database import User 

VERSION = "1.0.0"


@app.get("/version")
def get_version():
    out={}
    out["server_time"] = (
        datetime.now().strftime("%F %H:%M:%S"))
    out["version"] = VERSION
    return out


# @app.post("/users")
# def create_user():
#     user_data = request.json
#     new_id = user.insert(
#         user_data.get("first_name"),
#         user_data.get("last_name"),
#         user_data.get("hobbies")
#     )
#     out = {"new_id": new_id}
#     return out, 201
    

@app.get("/users")
def get_all_users():
    users = User.query.all()
    out_list = []
    for user in users:
        temp = {}
        temp["first_name"] = user.first_name
        temp["last_name"] = user.last_name
        temp["hobbies"] = user.hobbies
        temp["active"] = user.active
        out_list.append(temp)
    return {"users": out_list}
    

# @app.get("/users/<int:pk>")
# def get_single_user(pk):
#     user_record = user.read(pk)
#     out = {"user": user_record}
#     return out 

# @app.put("/users/<int:pk>")
# def put_single_user(pk):
#     user_data = request.json
#     user.update(pk,
#     user_data.get("first_name"),
#     user_data.get("last_name"),
#     user_data.get("hobbies")
#     )

#     return "OK", 204 

# # @app.put()

# @app.delete("/users/<int:pk>")
# def delete_single_user(pk):
#     user.deactivate_user(pk) 

#     return "OK", 200
# @app.delete()
# for update: an HTTP PUT operation with route: /users/<int:pk>
#FOR DEACTIVATE: an HTTP delete operation with route /users/<int:pk>