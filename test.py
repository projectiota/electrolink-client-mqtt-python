from electrolinkClient import Electrolink

el = Electrolink('localhost', 1883)

print el.getDeviceInfo()
