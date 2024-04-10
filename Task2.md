# Task - 2:

- In Task 2 I was given to write an automation test script to verify the API response using ROBOT framework with Python.
- Here I have used "https://jsonplaceholder.typicode.com" dummy API website and the "/posts" endpoint.
- The JSON payloads for this endpoint are "title", "body", and "userId".
- The JSON response it gives has "id", "title", "body", and "userId".
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

- To execute this download the file or copy the content of "robot_framework_post_request.robot" file inside "Task_2_robot_frameword" folder and paste it into a file having ".robot" extension.
- Keep the file in a folder and open a terminal in the folder. The command for execution - robot <file_name>.
