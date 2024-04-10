# Task - 2:

- In Task 2 I have given to write a automtion test script to varifyt the API response using ROBOT frame work with python.
- Here i have used "https://jsonplaceholder.typicode.com" dummy API website and "/posts" endpoint.
- The json payloads for this endpoint are "titel", "body", and "userId".
- The json response it gives have "id", "titel", "body", and "userId".
- I validated the status code and the text of the text response of the API using robot framework validations.

### Json payload for this API:
      {
        title: 'foo',
        body: 'bar',
        userId: 1
      }

### Json response from the API:
      {
        id: 101,
        title: 'foo',
        body: 'bar',
        userId: 1
      }

- To execute this download the file or copy the content of "robot_framework_post_request.robot" file inside "Task_2_robot_frameword" folder and paste it in a file having ".robot" extension.
