# encoding: utf-8
import paho.mqtt.client as mqtt

# Client对象构造

MQTTHOST = "iot-06z009y9rnab11u.mqtt.iothub.aliyuncs.com"
MQTTPORT = 1883
mqttClient = mqtt.Client(client_id="i6faViFVrIm.lightTest|securemode=2,signmethod=hmacsha256,timestamp=1676854208595|")
mqttClient.username_pw_set(username="lightTest&i6faViFVrIm",
                           password="565b911af3521ac24715872677e594832cd6845d7ab8d1acbba54cef480d87e9")


# 连接MQTT服务器
def on_mqtt_connect():
    mqttClient.connect(MQTTHOST, MQTTPORT, 60)
    mqttClient.loop_start()


# publish 消息
def on_publish(topic, payload, qos):
    mqttClient.publish(topic, payload, qos)


# 消息处理函数
def on_message_come(lient, userdata, msg):
    print(msg.topic + " " + ":" + str(msg.payload))


# subscribe 消息
def on_subscribe():
    # 订阅监听自定义Topic
    mqttClient.subscribe("/i6faViFVrIm/lightTest/user/test1", 1)
    mqttClient.on_message = on_message_come  # 消息到来处理函数


def main():
    on_mqtt_connect()
    # 自定义Topic消息上行
    on_publish("/i6faViFVrIm/lightTest/user/test1", "Hello Aliyun! This is MQTT client ", 1)
    on_subscribe()
    while True:
        pass


if __name__ == '__main__':
    main()
