from influxdb import InfluxDBClient
import threading
import random

interval = 5


def insert_data():
    json_body = [
        {
            "measurement": "realtime",
            "fields": {
                "data_value": random.uniform(0, 10.0)
            }
        }
    ]
    client.write_points(json_body)

def start_timer():
    threading.Timer(interval, start_timer).start()
    insert_data()


client = InfluxDBClient('localhost', 8086, 'root', 'root', 'realtime')
client.create_database('realtime')
client.query('CREATE RETENTION POLICY "one_hour" ON "realtime" DURATION 1h REPLICATION 1 DEFAULT')
client.query('CREATE CONTINUOUS QUERY "cq_one_min" ON "realtime" BEGIN SELECT mean(data_value) INTO realtime.autogen.realtime_mean FROM realtime.one_hour.realtime GROUP BY time(1m) END')
start_timer()