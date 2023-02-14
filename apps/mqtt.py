# encoding: utf-8
import paho.mqtt.client as mqtt

# Client对象构造

MQTTHOST = "iot-06z009y9rnab11u.mqtt.iothub.aliyuncs.com"
MQTTPORT = 1883
mqttClient = mqtt.Client(client_id="i6faViFVrIm.light1|securemode=2,signmethod=hmacsha256,timestamp=1676383979937|")
mqttClient.username_pw_set(username="light1&i6faViFVrIm", password="f0d428467f9fb06467c52f24d11a50491f81c8b4f51684a92682d821ddde29c9")


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
    mqttClient.subscribe("light1/user/update1", 1)
    mqttClient.on_message = on_message_come # 消息到来处理函数


def main():
    on_mqtt_connect()
    # 自定义Topic消息上行
    on_publish("light1/user/test2", "Hello Python!", 1)
    # 系统属性Topic消息上行
    on_publish("/sys/light1/thing/event/property/post", "{\"method\":\"thing.service.property.set\",\"id\":\"i6faViFVrIm.light1|securemode=2,signmethod=hmacsha256,timestamp=1676381859164|\",\"params\":{\"Status\":1},\"version\":\"1.0.0\"}", 1)
    on_subscribe()
    while True:
        pass

if __name__ == '__main__':
    main()