import json
import requests
from SensorInfo import get_sensor_name, get_sensor_value, get_sensor_unit

# Request Parameters
host = 'https://sensecap.seeed.cc/openapi/view_latest_telemetry_data'
device_eui = '?device_eui=2CF7F1C0443001A0'
measurement_id = '&measurement_id='
channel_index = '&channel_index=1'
auth = ('AFR6W7WQ0ED3F0WR',
        '573ECB5923794FB991824534BF3C47FED52FA37C05CA49DAAC0C44577F4391A7')

# Sensor parameters
sensorsInfo = ['4097', '4098', '4099', '4101', '4104', '4105', '4113', '4190']
DataExtracted = {}
SensorUnitValue = {}
for sensor_id in sensorsInfo:
    service = host + device_eui + measurement_id + sensor_id + channel_index
    response = requests.get(service, auth=auth)
    if response.status_code == 200:
        sensorName = get_sensor_name(sensor_id)
        DataExtracted[sensorName] = get_sensor_value(
            response.json()['data'])
        SensorUnitValue[sensorName] = get_sensor_unit(sensorName)
    else:
        print(
            f'Request failed with status code {response.status_code}: {response.text}')

print(DataExtracted)
