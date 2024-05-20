import paho.mqtt.client as mqtt
import signal
import sys


def on_connect(client, userdata, flag, rc):
    print("Completed connection to broker")
    # client.subscribe("i483/sensors/s2410014/BMP180/temperature")
    # client.subscribe("i483/sensors/s2410014/BMP180/air_pressure")
    # client.subscribe("i483/sensors/s2410014/SCD41/temperature")
    # client.subscribe("i483/sensors/s2410014/SCD41/co2")
    # client.subscribe("i483/sensors/s2410014/SCD41/humidity")
    client.subscribe("i483/sensors/s2410014/#")


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")


def on_message(client, userdata, msg):
    print("Received message" + str(msg.payload) + "on topic" + msg.topic)


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

client.connect("150.65.230.59", 1883, keepalive=60)

client.loop_forever()
