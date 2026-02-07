from locust import HttpUser, task, between # type: ignore

class ExplainerUser(HttpUser):
    wait_time = between(1, 3) # type: ignore

    @task
    def submit_prompt(self):
        self.client.post(
            "/api/explain",
            json={
                "prompt": "Explain binary search"
            }
        )
