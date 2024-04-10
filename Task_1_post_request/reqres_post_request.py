import json
import jsonpath
import requests

# Api URL
url = 'https://reqres.in/api/users'

# parse the data into json
post_request = json.loads('{"name": "Durga","job": "SDET"}')

# make post request with json input body
response = requests.post(url, post_request)
print(f"The response text is : {response.text}")

status_code = response.status_code

# Way-1 of Validation
assert response.status_code == 201, "The response code is different"

# Way-2 of Validation
if status_code == 201:
    print("The status code is: 201")
else:
    print(f"The response code is coming as :{status_code} ")

# parse response to json format
json_response = json.loads(response.content)

# pick id using json path
# Here jsonpath giving us a List
name = jsonpath.jsonpath(json_response, 'name')
job = jsonpath.jsonpath(json_response, 'job')

# Way-1 of Validation
assert name[0] == "Durga", "Name is different from the expected one"
assert job[0] == "SDET", "Job profiles are not matching"

# Way-2 of Validation
if name[0] == 'Durga' and job[0] == "SDET":
    print(f"The name is : {name[0]} and job is : {job[0]}")
else:
    print(f"Name and job are coming as : {name[0]}, {job[0]}")
