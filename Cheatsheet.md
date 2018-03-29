
# Cheatsheet for InfluxDB Lab

This cheatsheet is for your reference. You can **copy & paste** the commands to save time. However, please follow the `Tutorial` and make sure **you know what you are doing** before executing anything.

> Table of Contents

* [InfluxDB installation](#influxdb-installation)
	* [On Mac](#on-mac)
	* [On Windows](#on-windows)
	* [On Linux(*NIX)](#on-linuxnix)
* [InfluxDB client](#influxdb-client)
	* [Basic operations](#basic-operations)
	* [Data insertion](#data-insertion)
	* [Data exploration](#data-exploration)
	* [(Optional) Retention Policy](#optional-retention-policy)
	* [(Optional) Continuous Query](#optional-continuous-query)
* [Grafana](#grafana)
	* [Installation](#installation)
	* [Import panel](#import-dashboard)
	* [Realtime data](#realtime-data)


## InfluxDB installation

InfluxDB will use port `8086` for HTTP APIs, make sure that port isn't being occupied (which is unlikely to happen, since `8086` is not a popular port).

### On Mac

```shell
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew update
brew install influxdb
influxd
```

### On Windows

> Only `x64` arch is supported. Most modern computers should have **Windows 64bit** version installed.

Download and unzip: <https://dl.influxdata.com/influxdb/releases/influxdb-1.5.0_windows_amd64.zip>

Then follow the screenshots on the `Tutorial`. You *don't* need to change configuration file for this lab.

### On Linux(*NIX)

If you are using *NIX, then you may know there are numerous ways to install an application on your platform. Here we just list the easiest solution.

```bash
wget https://dl.influxdata.com/influxdb/releases/influxdb-1.5.1-static_linux_amd64.tar.gz
tar xf influxdb-1.5.1-static_linux_amd64.tar.gz
cd influxdb-1.5.1-1
sudo ./influxd -config influxdb.conf
```

## InfluxDB client

### Start InfluxDB Command Line Interface

On Mac/*NIX:  running  `influx -precision rfc3339` in terminal.
On Windows: double click `influx.exe`.

### Basic operations

```sql
CREATE DATABASE test
SHOW DATABASES
USE test
```

### Data insertion

```sql
INSERT server,region=us_east,host=server_A cpu=0.65,mem=2335
INSERT server,region=us_east,host=server_A cpu=0.53 1521028800000000000
INSERT server,region=us_east cpu=0.43,mem=3532 1521028800000000000
INSERT server,region=us_east,host=server_B cpu=0.33,mem=3323 1521028500000000000

SELECT * FROM server
```

### Data exploration

#### Import air quality data

Download and unzip: <https://github.com/INFSCI-2711-LAB/InfluxDB-Lab/archive/master.zip>

- On Windows
  - Copy `influx.exe` into the `script` folder
  - Execute `import_windows.bat`

- On Mac/*NIX
  - Open terminal and switch to the directory.
  - Execute: `sh scripts/import_mac_linux.sh`

#### Queries

```sql
USE air
SHOW MEASUREMENTS
SHOW TAG KEYS
SHOW FIELD KEYS
```

```sql
SELECT * FROM pm WHERE city = 'Beijing' LIMIT 5

SELECT pm FROM pm WHERE city = 'Shanghai' AND pm > 600

SELECT pm, humidity FROM pm WHERE city = 'Guangzhou' AND time >= '2015-01-01' LIMIT 5

SELECT max(pm), mean(pm) FROM pm GROUP BY city

SELECT mean(pm), mean(precipitation) FROM pm WHERE time >= '2014-01-01' AND time < '2015-01-01' AND city='Beijing' GROUP BY time(7d)
```

### (Optional) Retention Policy

```sql
CREATE DATABASE realtime
USE realtime

CREATE RETENTION POLICY "one_hour" ON "realtime" DURATION 1h REPLICATION 1
SHOW RETENTION POLICIES
```

### (Optional) Continuous Query

```sql
CREATE CONTINUOUS QUERY "cq_one_min" ON "realtime" BEGIN SELECT mean(data_value) INTO realtime.autogen.realtime_mean FROM realtime.one_hour.realtime GROUP BY time(1m) END
SHOW CONTINUOUS QUERIES
```

## Grafana

### Installation

On Mac

```shell
brew update
brew install Grafana
brew services start Grafana
```

On Windows

Download and unzip: <https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana-5.0.4.windows-x64.zip>

Then follow the screenshots on the `Tutorial`.

### Import dashboard

See `Tutorial`.

### Realtime data

```shell
pip install influxdb
python scripts/realtime.py
```

```sql
SELECT "data_value" FROM "realtime" WHERE $timeFilter
```
