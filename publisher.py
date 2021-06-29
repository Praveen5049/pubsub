"""Publishes multiple messages to a Pub/Sub topic with an error handler."""
from concurrent import futures
from google.cloud import pubsub_v1
from faker import Faker
import uuid
from random import randint
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Praveen_Workspace\pathas-proect-84018-49d8a3b60d38.json"




# TODO(developer)
project_id = "pathas-proect-84018"
topic_id = "student_information_topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)
publish_futures = []

def get_callback(publish_future, data):
    def callback(publish_future):
        try:
            # Wait 60 seconds for the publish call to succeed.
            print(publish_future.result(timeout=60))
        except futures.TimeoutError:
            print(f"Publishing {data} timed out.")

    return callback
def pub():
    for i in range(50):
        myuuid = uuid.uuid4()
        fake = Faker()
        range_start = 10**(10-1)
        range_end = (10**10)-1
        data = ",".join([fake.name(),str(randint(range_start, range_end)),str(myuuid),fake.name(),fake.address(),fake.address()])
        #print(data)
        # When you publish a message, the client returns a future.
        publish_future = publisher.publish(topic_path, data.encode("utf-8"))
        # Non-blocking. Publish failures are handled in the callback function.
        publish_future.add_done_callback(get_callback(publish_future, data))
        publish_futures.append(publish_future)

    # Wait for all the publish futures to resolve before exiting.
    futures.wait(publish_futures, return_when=futures.ALL_COMPLETED)

    #print(f"Published messages with error handler to {topic_path}.")