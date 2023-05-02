from locust import HttpUser, task
import requests
import json
import google.auth
import google.auth.transport.requests
import random


class FeatureStoreTest(HttpUser):
    client_adress = "aiplatform.googleapis.com/v1/projects"
    host = f"https://{client_adress}"

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

        LOCATION_ID = "europe-west4"
        PROJECT_ID = "fs-test-376718"
        FEATURESTORE_ID = "orders_predictions_6gwqrq8s"
        ENTITY_TYPE_ID = "user_id"

        api = f"https://{LOCATION_ID}-{self.client_adress}/{PROJECT_ID}/locations/{LOCATION_ID}/featurestores/{FEATURESTORE_ID}/entityTypes/{ENTITY_TYPE_ID}:readFeatureValues"

        token = get_jwt_token()
        headers = {"Authorization": "Bearer " + token}
        user_id = get_random_user()

        data = {
            "entityId": f"{user_id}",
            "featureSelector": {"idMatcher": {"ids": ["*"]}},
        }

        response = self.client.post(api, json=data, headers=headers)
