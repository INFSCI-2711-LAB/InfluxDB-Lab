
## InfluxDB-Lab

This repo contains all the contents for the INFSCI 2711 Lab on InfluxDB.

### Preparation before Class

 - We are experiencing some network connectivity problems on some domains (e.g. pip install site) with the university's WIFI recently. So, please take five minutes to install the required softwares at home on your laptop with the following commands.
 - **All systems**: install the Python package with command
	 - `pip install influxdb` **(this is the most important one)**
 - **Mac OS**: run these commands in your terminal
	 - `
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
`
	- `brew update`
	- `brew install influxdb`
	- `brew install Grafana`

 - **Windows**: download the following files
	 - https://dl.influxdata.com/influxdb/releases/influxdb-1.5.0_windows_amd64.zip
	 - https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana-5.0.4.windows-x64.zip

### Cheatsheet
 - A [cheatsheet](CHEATSHEET.md) is provided for your reference. It includes all the commands you'll be needing during the lab.
