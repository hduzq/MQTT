import sys
from linkkit import linkkit
import threading
import traceback
import inspect
import time
import logging

# config log
__log_format = '%(asctime)s-%(process)d-%(thread)d - %(name)s:%(module)s:%(funcName)s - %(levelname)s - %(message)s'
logging.basicConfig(format=__log_format)

lk = linkkit.LinkKit(
    host_name="cn-shanghai",
    product_key="i6faViFVrIm",
    device_name="lightTest",
    device_secret="a4ae5c850b4c9c6d2333739dc2baa606")
# lk.config_mqtt(endpoint="iot-cn-6ja******.mqtt.iothub.aliyuncs.com")

lk.enable_logger(logging.DEBUG)


def on_device_dynamic_register(rc, value, userdata):
    if rc == 0:
        print("dynamic register device success, value:" + value)
    else:
        print("dynamic register device fail, message:" + value)


def on_connect(session_flag, rc, userdata):
    print("on_connect:%d,rc:%d" % (session_flag, rc))
    pass


def on_disconnect(rc, userdata):
    print("on_disconnect:rc:%d,userdata:" % rc)


def on_topic_message(topic, payload, qos, userdata):
    print("on_topic_message:" + topic + " payload:" + str(payload) + " qos:" + str(qos))
    pass


def on_subscribe_topic(mid, granted_qos, userdata):
    print("on_subscribe_topic mid:%d, granted_qos:%s" %
          (mid, str(','.join('%s' % it for it in granted_qos))))
    pass


def on_unsubscribe_topic(mid, userdata):
    print("on_unsubscribe_topic mid:%d" % mid)
    pass


def on_publish_topic(mid, userdata):
    print("on_publish_topic mid:%d" % mid)


lk.on_device_dynamic_register = on_device_dynamic_register
lk.on_connect = on_connect
lk.on_disconnect = on_disconnect
lk.on_topic_message = on_topic_message
lk.on_subscribe_topic = on_subscribe_topic
lk.on_unsubscribe_topic = on_unsubscribe_topic
lk.on_publish_topic = on_publish_topic


lk.config_device_info("Eth|03ACDEFF0032|Eth|03ACDEFF0031")
lk.config_mqtt(port=1883, protocol="MQTTv311", transport="TCP",secure="TLS")
lk.connect_async()
lk.start_worker_loop()

while True:
    try:
        msg = input()
    except KeyboardInterrupt:
        sys.exit()
    else:
        if msg == "1":
            lk.disconnect()
        elif msg == "2":
            lk.connect_async()
        elif msg == "3":
            rc, mid = lk.subscribe_topic(lk.to_full_topic("user/get"))
            if rc == 0:
                print("subscribe topic success:%r, mid:%r" % (rc, mid))
            else:
                print("subscribe topic fail:%d" % rc)
        elif msg == "4":
            rc, mid = lk.unsubscribe_topic(lk.to_full_topic("user/get"))
            if rc == 0:
                print("unsubscribe topic success:%r, mid:%r" % (rc, mid))
            else:
                print("unsubscribe topic fail:%d" % rc)
        elif msg == "5":
            rc, mid = lk.publish_topic(lk.to_full_topic("user/update"), "{\"id\":\"1\",\"version\":\"1.0\",\"params\":{\"LightSwitch\":0}}")
            if rc == 0:
                print("publish topic success:%r, mid:%r" % (rc, mid))
            else:
                print("publish topic fail:%d" % rc)
        elif msg == "8":
            ret = lk.dump_user_topics()
            print("user topics:%s", str(ret))
        elif msg == "9":
            lk.destruct()
            print("destructed")
        else:
            sys.exit()