# Task - 3:

- In this task I have to test an API endpoint under load by simulating the load using Locust framework.
- I have used the Locust web UI to test the API under load.
- First I have initialized a session by HttpUser and then run the code in terminal by using locust command.
- The command to run the python file -  locust -f <file_name>.
- Then it will create a session locally at some port and the URL will be visible in the terminal.
- Click on the link to go to the Locust web UI.
- Then we have to select the a) Number of Users
                             b) Number of user per second (Ramp up)
                             c) Under Advance settings - give the time for which you want to execute the test
- In the web UI you can see Charts, Failures, Logs etc to see how stable the API is under load.
- In the console you can see all this after the termination.
- If you are printing some messages it will be shown in the console
- You can manually stop the execution also in the web UI or in console you can press "Ctrl+c". 
