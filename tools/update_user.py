import requests 
from random import choice 

UPDATED_USER ={
    "first_name":"Angel",
    "last_name": "Garcia",
    "hobbies": choice(
        [
            "Golf",
            "Tennis",
            "Soccer",
            "Skateboarding",
            "Football",
            "Coding"
        ]
     )
}


URL = "http://127.0.0.1:5000/users/1"


def update_user():
    out = requests.put(URL, json=UPDATED_USER)
    if out.status_code == 200:
        print("Update Successful.")
    else:
        print("Update failed.")
        
if __name__ == "__main__":
    update_user()

#     USER_DATA["hobbies"] = "moutain biking"
#     out = requests.put(URL+"/1", json=USER_DATA)
#     if out.status_code == 204:
#         print("test update successful")
#     else: 
#         print("something went wrong")

# if __name__ == "__main__":
#     update_user()

