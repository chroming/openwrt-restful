# openwrt-restful

A tiny restful api service for openwrt.

## Usage

### openwrt:

`pip install requirements.txt`
`python run.py`

### client:

`requests.get("http://192.168.1.1/ss/status")`

 `requests.post("http://192.168.1.1/ss/gfw", data={"url":"google.com"})`
 
