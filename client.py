import requests
import json
import os
import time

def send_message():
    # We should read the server URL from the environment variable, fallback to localhost for testing
    url = os.getenv("SERVER_URL", "http://localhost:8080")
    message = {"name": "Response from Client!"}
    headers = {"Content-Type": "application/json"}

    while True:  # Loop to send messages repeatedly
        try:
            # Sending POST request to the server
            response = requests.post(url, data=json.dumps(message), headers=headers)
            print(f"Server Response: {response.json()}")
            time.sleep(5)  # Waiting for 5 seconds before sending the next message
        except requests.exceptions.RequestException as e:
            print(f"Failed to connect to server: {e}")
            time.sleep(5)

if __name__ == "__main__":
    send_message()
