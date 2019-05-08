# TODO: Copy the code in
#     m1e_mqtt_receiver.py
# as your starting point, pasting its code here.

# Then modify the code so that it receives messages from your
#    m2_tkinter_as_mqtt_sender.py
# module and PRINTS them.

""" A simple example of using MQTT for RECEIVING messages. """

import mqtt_remote_method_calls as com
import time


class DelegateThatReceives(object):
    def __init__(self):
        self.number_of_messages = 0

    def say_it(self, name, message):
        self.number_of_messages = self.number_of_messages + 1
        part1 = "Message {} received from {}:".format(self.number_of_messages,
                                                      name)
        print(part1, message)


def main():
    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")

    my_delegate = DelegateThatReceives()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect(name1, name2)
    time.sleep(1)  # Time to allow the MQTT setup.
    print()

    while True:
        time.sleep(0.01)  # Time to allow message processing


main()
