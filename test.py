from iotaLinkClient import IotaLink

il = IotaLink('localhost', 1883)

print il.getDeviceInfo()
