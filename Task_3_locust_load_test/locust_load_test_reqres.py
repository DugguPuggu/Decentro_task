from locust import HttpUser, constant, task


class MyRequest(HttpUser):
    host = "https://jsonplaceholder.typicode.com"

    @task
    def post_user(self):
        response = self.client.post("/posts", data='''{"title": "hgd", "body": "gbd", "userId": 1}''')
        print(response.status_code)
        print(response.headers)
        print(response.text)
