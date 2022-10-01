import json
import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_resource(id=None):
    data={} #you need all records
    if id is not None:
        data={'id':id} # A record with a particular id
    response=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(response.status_code)
    print(response.json())

def create_resource():
    stud_data={'name':'Anand','rollno':201,'marks':88,'address':'Delhi'}
    response=requests.post(BASE_URL+ENDPOINT,data=json.dumps(stud_data))
    print(response.status_code)
    print(response.json())

def update_resource(id):
    stud_data={'id':id,'name':'New user','marks':88,'address':'Unknown place'}
    response=requests.put(BASE_URL+ENDPOINT,data=json.dumps(stud_data))
    print(response.status_code)
    print(response.json())

def delete_resource(id):
    data={'id':id}
    response=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(response.status_code)
    print(response.json())

print("Enter 1--->To retrive the records \n  2--->To create a new record 3--->To update a record \n 4---->To delete a record\n")
print("Enter your choice")
ch=int(input())
if ch==1:
   get_resource()
elif ch==2:
   create_resource()
elif ch==3:
   id=input("Enter id")
   update_resource(id)
elif ch==4:
    id=input("Enter id")
    delete_resource(id)