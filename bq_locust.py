from locust import HttpUser, TaskSet, task
import requests
import json
import google.auth
import google.auth.transport.requests
import random


class BigQueryTest(HttpUser):
    host = "https://bigquery.googleapis.com/bigquery"

    @task(1)
    def get_data(self):
        def get_random_user():
            random_user_id = random.randint(1, 100000)
            return random_user_id

        def get_jwt_token():
            credentials, project_id = google.auth.default()

            request = google.auth.transport.requests.Request()
            credentials.refresh(request)
            return credentials.token

        api = f"{self.host}/v2/projects/fs-test-376718/queries"

        token = get_jwt_token()
        headers = {"Authorization": "Bearer " + token}

        user_id = get_random_user()

        data = {
            "query": f"SELECT * FROM fs-test-376718.orders_data.orders WHERE user_id = '{user_id}' ORDER BY timestamp DESC LIMIT 1",
            "timeoutMs": 10000,
            "useLegacySql": False,
        }

        response = self.client.post(api, json=data, headers=headers)
