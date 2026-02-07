from locust import HttpUser, task, between

class MagicPencilReplayUser(HttpUser):
    wait_time = between(40, 80)

    def on_start(self):
        # Open homepage (create session / anonymous user)
        self.client.get("/")

    @task
    def replay_generated_content(self):
        # Simulate rewatching/replaying previously generated content
        self.client.get(
            "/api/content/replay",
            name="Replay_Generated_Content"
        )
