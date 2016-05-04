import paho.mqtt.client as mqtt
import json
import Queue

qs = []


class iotaLink():

    def __init__(self, mqttHost, mqttPort):
        self.host = mqttHost
        self.port = mqttPort
        self.authUuid = ''
        self.token = ''
        self.client = None
        self.msgId = 0

        # Define event callbacks
        def on_connect(mosq, obj, rc):
            print("rc: " + str(rc))

        def on_message(mosq, obj, msg):
            print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

            p = json.loads(msg.payload);
            qs[p['id']].put(p)

        def on_publish(mosq, obj, mid):
            print("mid: " + str(mid))

        def on_subscribe(mosq, obj, mid, granted_qos):
            print("Subscribed: " + str(mid) + " " + str(granted_qos))

        def on_log(mosq, obj, level, string):
            print(string)


        self.client = mqtt.Client()

        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.on_publish = on_publish

        self.client.connect(self.host, self.port, 60)

        # Start looping
        self.client.loop_start()


    ###
    # pinMode()
    ###
    def pinMode(self, int pinID, int pinMode):
        """
        {
            "jsonrpc": "2.0",
            "method": "pinMode",
            "params": [<pinId>, <pinMode>],
            "id": <msgId>
        }
        """
        s = {}
        s['jsonrpc'] = '2.0'
        s['method'] = 'pinMode'
        s['params'] = [pinID, pinMode]
        
        # Increment self.msgId to make it unique
        slef.msgId += 1
        msdId = self.msgId
        s['id'] = msgId

        # Create a queue for this message
        qs[msgId] = Queue.Queue()

        payload = json.dumps(s)
        (rc, mid) = self.client.publish(mqttTopic, payload, qos=1)

        # Block on queue waiting for response
        rsp = qs[msgId].get()

        # Delete queue for this message
        qs.del(msgId)

        return rsp.result


    ###
    # digitalWrite()
    ###
    def digitalWrite(self, int pinID, int pinMode):
        """
        {
            "jsonrpc": "2.0",
            "method": "digitalWrite",
            "params": [<pinId>, <value>],
            "id": 4
        }
        """
        s = {}
        s['jsonrpc'] = '2.0'
        s['method'] = 'digitalWrite'
        s['params'] = [pinID, value]
        s['id'] = 4
        payload = json.dumps(s)
        (rc, mid) = self.client.publish(mqttTopic, payload, qos=1)


