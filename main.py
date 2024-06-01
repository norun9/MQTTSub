import paho.mqtt.client as mqtt
import signal
import sys


def on_connect(client, userdata, flag, rc):
    print("Completed connection to broker")
    client.subscribe("i483/sensors/s2410014/#")


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")


def on_message(client, userdata, msg):
    print(msg.payload.decode())


def signal_handler(sig, frame):
    print('Disconnecting from broker')
    client.disconnect()
    client.loop_stop()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect("150.65.230.59")

client.loop_forever()
