from locust import HttpUser, task, between
import uuid

class MagicPencilNewChatUser(HttpUser):
    wait_time = between(40, 80)

    def on_start(self):
        # Open homepage (anonymous session)
        self.client.get("/")

    @task
    def create_new_chat_and_send_prompt(self):
        # Step 1: create a new chat (unique chat each time)
        chat_id = str(uuid.uuid4())

        self.client.post(
            "/api/chat/create",
            json={"chat_id": chat_id},
            name="Create_New_Chat"
        )

        # Step 2: send a prompt in the new chat
        self.client.post(
            "/api/generate",
            json={
                "chat_id": chat_id,
                "prompt": "Explain photosynthesis",
                "mode": "AUTO"
            },
            name="AI_Prompt_New_Chat"
        )
