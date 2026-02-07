from locust import HttpUser, task, between

class MagicPencilPromptUser(HttpUser):
    # User thinks/reads for 45–90 seconds
    wait_time = between(45, 90)

    def on_start(self):
        # Step 1: open homepage (public, creates session/cookies)
        self.client.get("/")

    @task
    def send_prompt(self):
        # Step 2: send an AI prompt (adjust endpoint if needed)
        self.client.post(
            "/api/generate",
            json={
                "prompt": "Explain photosynthesis in simple terms",
                "mode": "AUTO"
            },
            name="AI_Prompt"
        )
