# encoding: utf-8
import paho.mqtt.client as mqtt

# Client对象构造
MQTTHOST = "********.iot-as-mqtt.cn-shanghai.aliyuncs.com"
MQTTPORT = 1883
mqttClient = mqtt.Client("pythondevice2|securemode=3,signmethod=hmacsha1|")
mqttClient.username_pw_set("pythondevice2&********", "5D1090BECB4E4AED75BD5208EA420275********")


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
    mqttClient.subscribe("/********/pythondevice2/user/update1", 1)
    mqttClient.on_message = on_message_come # 消息到来处理函数


def main():
    on_mqtt_connect()
    # 自定义Topic消息上行
    on_publish("/********/pythondevice2/user/test2", "Hello Python!", 1)
    # 系统属性Topic消息上行
    on_publish("/sys/********/pythondevice2/thing/event/property/post", "{\"method\":\"thing.service.property.set\",\"id\":\"1745506903\",\"params\":{\"Status\":1},\"version\":\"1.0.0\"}", 1)
    on_subscribe()
    while True:
        pass

if __name__ == '__main__':
    main()