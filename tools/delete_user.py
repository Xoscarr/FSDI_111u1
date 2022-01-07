import requests 


from create_user import URL, USER_DATA

def delete_user():
    out = requests.delete(URL+"/1", json=USER_DATA)
    if out.status_code == 200:
        print("Deleted user")
    else: 
        print("something went wrong")

if __name__ == "__main__":
    delete_user()
