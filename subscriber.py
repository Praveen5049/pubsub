from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
import os
import pandas as pd

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Praveen_Workspace\pathas-proect-84018-49d8a3b60d38.json"

# TODO(developer)
project_id = "pathas-proect-84018"
subscription_id = "student_information_subscriber"
# Number of seconds the subscriber should listen for messages
timeout = 5.0

subscriber = pubsub_v1.SubscriberClient()
# The subscription_path method creates a fully qualified identifier
# in the form projects/{project_id}/subscriptions/{subscription_id}
subscription_path = subscriber.subscription_path(project_id, subscription_id)


def func():
    def callback(message):
        with open('outputFile.csv', 'a') as f:
            f.write(str(message.data, 'utf-8') + "\n")
        message.ack()

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}..\n")

    # Wrap subscriber in a 'with' block to automatically call close() when done.
    with subscriber:
        try:
            # When timeout is not set, result() will block indefinitely,
            # unless an exception is encountered first.
            streaming_pull_future.result(timeout=timeout)
        except TimeoutError:
            streaming_pull_future.cancel()  # Trigger the shutdown.
            streaming_pull_future.result()  # Block until the shutdown is complete.


# if __name__ == '__main__':
#     func()