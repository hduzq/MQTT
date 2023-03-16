# encoding: utf-8
import hashlib
import hmac

import paho.mqtt.client as mqtt
import ssl

#设备基本信息，其中random_str仅用于生成唯一的client_id
host_name="cn-shanghai"
product_key="i6faWL8wiwH"
device_name="yixingyimi13"
product_secret="Yr0iF3HIgNkwiaPj"
random_str="Test2"
instance_id="iot-06z009y9rnab11u"

#申请device_token时,client_id username password生成方法
client_id = "%s.%s|random=%s,authType=regnwl,securemode=2,signmethod=hmacsha256,instanceId=%s|" % (
device_name,product_key, random_str, instance_id)
username = "%s&%s" % (device_name, product_key)
password_src ="deviceName%sproductKey%srandom%s" % (device_name, product_key, random_str)
password = hmac.new(product_secret.encode("utf-8"), password_src.encode("utf-8"), hashlib.sha256).hexdigest()

print("clientid:%s \n username:%s \n password:%s"%(client_id,username,password))
# Client对象构造

MQTTHOST = "iot-06z009y9rnab11u.mqtt.iothub.aliyuncs.com"
MQTTPORT = 1883
mqttClient = mqtt.Client(client_id=client_id)
mqttClient.username_pw_set(username=device_name+"&"+product_key,
                           password=password)


#mqtt set tls
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH, cadata="\
-----BEGIN CERTIFICATE-----\n\
MIIDdTCCAl2gAwIBAgILBAAAAAABFUtaw5QwDQYJKoZIhvcNAQEFBQAwVzELMAkG\
A1UEBhMCQkUxGTAXBgNVBAoTEEdsb2JhbFNpZ24gbnYtc2ExEDAOBgNVBAsTB1Jv\
b3QgQ0ExGzAZBgNVBAMTEkdsb2JhbFNpZ24gUm9vdCBDQTAeFw05ODA5MDExMjAw\
MDBaFw0yODAxMjgxMjAwMDBaMFcxCzAJBgNVBAYTAkJFMRkwFwYDVQQKExBHbG9i\
YWxTaWduIG52LXNhMRAwDgYDVQQLEwdSb290IENBMRswGQYDVQQDExJHbG9iYWxT\
aWduIFJvb3QgQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDaDuaZ\
jc6j40+Kfvvxi4Mla+pIH/EqsLmVEQS98GPR4mdmzxzdzxtIK+6NiY6arymAZavp\
xy0Sy6scTHAHoT0KMM0VjU/43dSMUBUc71DuxC73/OlS8pF94G3VNTCOXkNz8kHp\
1Wrjsok6Vjk4bwY8iGlbKk3Fp1S4bInMm/k8yuX9ifUSPJJ4ltbcdG6TRGHRjcdG\
snUOhugZitVtbNV4FpWi6cgKOOvyJBNPc1STE4U6G7weNLWLBYy5d4ux2x8gkasJ\
U26Qzns3dLlwR5EiUWMWea6xrkEmCMgZK9FGqkjWZCrXgzT/LCrBbBlDSgeF59N8\
9iFo7+ryUp9/k5DPAgMBAAGjQjBAMA4GA1UdDwEB/wQEAwIBBjAPBgNVHRMBAf8E\
BTADAQH/MB0GA1UdDgQWBBRge2YaRQ2XyolQL30EzTSo//z9SzANBgkqhkiG9w0B\
AQUFAAOCAQEA1nPnfE920I2/7LqivjTFKDK1fPxsnCwrvQmeU79rXqoRSLblCKOz\
yj1hTdNGCbM+w6DjY1Ub8rrvrTnhQ7k4o+YviiY776BQVvnGCv04zcQLcFGUl5gE\
38NflNUVyRRBnMRddWQVDf9VMOyGj/8N7yy5Y0b2qvzfvGn9LhJIZJrglfCm7ymP\
AbEVtQwdpf5pLGkkeB6zpxxxYu7KyJesF12KwvhHhm4qxFYxldBniYUr+WymXUad\
DKqC5JlR3XC321Y9YeRq4VzW9v493kHMB65jUr9TU/Qr6cf9tveCX4XSQRjbgbME\
HMUfpIBvFSDJ3gyICh3WZlXi/EjJKSZp4A==\n\
-----END CERTIFICATE-----")
mqttClient.tls_set_context(context)

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
    mqttClient.subscribe("/ext/regnwl", 1)
    mqttClient.on_message = on_message_come  # 消息到来处理函数


def main():
    on_subscribe()
    on_mqtt_connect()
    # 自定义Topic消息上行
    #on_publish("/i6faWL8wiwH/yixingyimi1/user/test1", "Hello Aliyun! This is MQTT client ", 1)
    i=0
    while i<5:
        i+=1
        pass


if __name__ == '__main__':
    main()
