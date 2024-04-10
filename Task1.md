# Task - 1:
- In task 1 I have to test the response received from a POST request using "reqres.in" post APIs.
- Here I used 'https://reqres.in' this base URL and '/api/users' this API endpoint.
- This API takes 2 parameters as payload, one is "name" and the second is "job".
- In response, it gives response code 201, response text "name", "job", "id", and "createdAt".
- For this, I used the "requests", "jsonpath" and "json" modules of Python to interact with the API and its response.

### Payload for the API:
      {
          "name": "morpheus",
          "job": "leader"
      }

### Response from the api:
      # Status code - 201
      {
          "name": "morpheus",
          "job": "leader",
          "id": "344",
          "createdAt": "2024-04-10T15:00:35.515Z"
      }

- To execute this code import all the packages written in the import section and run the file through the IDE. The expected output will come in the console.
