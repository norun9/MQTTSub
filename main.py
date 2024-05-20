import paho.mqtt.client as mqtt


def on_connect(client, userdata, flag, rc):
    print("Completed connection to broker")
    client.subscribe("i483/sensors/s2410014/BMP180/temperature")


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")


def on_message(client, userdata, msg):
    print("Received message" + str(msg.payload) + "on topic" + msg.topic)


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.connect("150.65.230.59", 1883, 60)
    client.loop_forever()
