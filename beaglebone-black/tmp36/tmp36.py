import Adafruit_BBIO.ADC as ADC
import plotly.plotly as py
import time

# Fill in the config.json file in this directory with your plotly username,
# plotly API key, and your generated plotly streaming tokens
# Sign up to plotly here: https://plot.ly/ssu
# View your API key and streaming tokens here: https://plot.ly/settings

username = 'workshop'
api_key = 'v6w5xlbx9j'
stream_token = 'unbi52ww8a'
stream_server = 'http://stream.plot.ly'

py.sign_in(username, api_key)

print py.plot([{'x': [], 'y': [], 'type': 'scatter',
              'stream': {'token': stream_token, 'maxpoints': 200}}],
              filename='BBB Streaming Example Values', fileopt='overwrite')

# temperature sensor connected to pin P9_40
sensor_pin = 'P9_40'
ADC.setup()

i = 0
stream = py.Stream(stream_token)
stream.open()

while True:
    reading = ADC.read(sensor_pin)
    millivolts = reading * 1800  # 1.8V reference = 1800 mV
    temp_c = (millivolts - 500) / 10
    temp_f = (temp_c * 9 / 5) + 32
    print('mv=%d C=%d F=%d' % (millivolts, temp_c, temp_f))
    stream.write({'x': i, 'y': temp_c})
    i += 1
    time.sleep(0.05)
