from setuptools import setup

setup(
    name = 'iotaLink',
    packages = ['iotaLink'], # this must be the same as the name above
    version = '0.1',
    description = 'Iota-Link Python client',
    author = 'Drasko DRASKOVIC',
    author_email = 'drasko.draskovic@gmail.com',
    url = 'https://github.com/drasko/iota-link-mqtt-client-python', # use the URL to the github repo
    keywords = ['iot', 'iota', 'mqtt'], # arbitrary keywords
    long_description = """Iota-Link (https://github.com/projectiota) MQTT JSON-RPC Python client""",
    classifiers = [
          "License :: OSI Approved :: Apache-2.0 License",
          "Programming Language :: Python",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Libraries",
    ],
    install_requires = [
        "paho.mqtt.client",
    ],
    license = 'Apache-2.0',
    test_suite = 'examples'
)
