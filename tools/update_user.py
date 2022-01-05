import requests 


from create_user import URL, USER_DATA


def update_user():
    USER_DATA["hobbies"] = "moutain biking"
    out = requests.put(URL+"/1", json=USER_DATA)
    if out.status_code == 204:
        print("test update successful")
    else: 
        print("something went wrong")

if __name__ == "__main__":
    update_user()

