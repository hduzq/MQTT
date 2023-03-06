# encoding: utf-8
import paho.mqtt.client as mqtt

# Client对象构造

MQTTHOST = "iot-06z009y9rnab11u.mqtt.iothub.aliyuncs.com"
MQTTPORT = 1883
mqttClient = mqtt.Client(client_id="9g55WSBuOZMNtMCJtktx000100|authType=connwl,securemode=-2,_ss=1,ext=3,lan=Python,_v=1.2.5|")
mqttClient.username_pw_set(username="yixingyimi1&i6faWL8wiwH",
                           password="^1^1677597746541^9ffd7c5bcf0c87f")


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
    mqttClient.subscribe("/i6faWL8wiwH/yixingyimi1/user/test1", 1)
    mqttClient.on_message = on_message_come  # 消息到来处理函数


def main():
    on_mqtt_connect()
    # 自定义Topic消息上行
    on_publish("/i6faWL8wiwH/yixingyimi1/user/test1", "Hello Aliyun! This is MQTT client ", 1)
    on_subscribe()
    while True:
        pass


if __name__ == '__main__':
    main()
