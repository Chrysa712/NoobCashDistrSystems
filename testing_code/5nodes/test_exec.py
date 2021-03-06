from concurrent.futures import ThreadPoolExecutor
import requests
import json

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def get_function(url):
	requests.get(url)

id_url = {}
id_url[0] = 'http://192.168.0.1:5000'
id_url[1] = 'http://192.168.0.2:5000'
id_url[2] = 'http://192.168.0.3:5000'
id_url[3] = 'http://192.168.0.4:5000'
id_url[4] = 'http://192.168.0.5:5000'


#post_function(url1, message1)

with ThreadPoolExecutor(5) as executor:
    for i in range(5):
        url = id_url[i] + '/test/run'
        executor.submit(get_function, url)

throughput = 0
block_time = 0

for i in range(5):
    response = requests.get(id_url[i] + '/test/results').json()
    throughput += response['throughput']
    block_time += response['block_time']

throughput = throughput / 5
block_time = block_time / 5

f = open("res5_c1_dif4.txt", "x")
f.write(str(throughput) + ' ' + str(block_time))
f.close()