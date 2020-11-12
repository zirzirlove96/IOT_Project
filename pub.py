import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub")      # MQTT Client 오브젝트 생성
mqttc.connect("broker.hivemq.com", 1883)    # MQTT 서버에 연결
mqttc.publish("hello/world", "Hello World!")  # 'hello/world' 토픽에 "Hello World!"라는 메시지 발행
mqttc.loop(2)       
