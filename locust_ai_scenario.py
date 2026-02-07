from locust import HttpUser, task, between

class MagicPencilAIScenario(HttpUser):
    wait_time = between(40, 80)

    @task
    def generate_ai_content(self):
        self.client.post(
            "/api/generate",
            json={"prompt": "Explain photosynthesis"},
            name="AI_Generate"
        )
