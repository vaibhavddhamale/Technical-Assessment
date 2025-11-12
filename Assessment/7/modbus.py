from pymodbus.client import ModbusSerialClient
from paho.mqtt import client as mqtt
import json, time

modbus = ModbusSerialClient(port='/dev/ttyUSB0', baudrate=9600, timeout=2)
mqttc = mqtt.Client("modbus_gateway")
mqttc.connect("broker.hivemq.com", 1883)
mqttc.loop_start()

while True:
    r = modbus.read_holding_registers(0, 3, unit=1)
    if not r.isError():
        data = {"device":"PLC01","regs":r.registers}
        mqttc.publish("factory/data", json.dumps(data))
        print("Sent:", data)
    time.sleep(5)
