import requests
import time

# Client URL
CLIENT_URL = 'http://127.0.0.1:8080'

# Timer duration in seconds
TIMER_DURATION = 60


def send_status_to_client(status):
    try:
        # Send an HTTP POST request to the client with the device status
        response = requests.post(CLIENT_URL, data=status)
        response.raise_for_status()  # Raise an exception for any HTTP error status
        print("Status sent to client.")
    except requests.RequestException as e:
        # Handle request exceptions (e.g., connection error)
        print(f"Error sending status to client: {e}")


if __name__ == "__main__":
    # Continuously send status to client and then wait specified time
    try:
        while True:
            send_status_to_client("connected")
            time.sleep(TIMER_DURATION)
    # if a keyboard interrupt occurs then the status updates end
    except KeyboardInterrupt:
        print("User ended status updates.")


