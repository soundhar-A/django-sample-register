# import json
# import requests
# from pprint import pprint
#
#
# headers = {
#     "Content-Type":"application/json"
# }
# data = json.dumps({
#     "first_name":"ammu",
#     "last_name":"A",
#     "email":"ammu@gmail.com",
#     "password":"123456",
#     "confirm_password":"123456"
# })
# response = requests.post("http://127.0.0.1:8000/",headers=headers,data=data)
# pprint(response.text)