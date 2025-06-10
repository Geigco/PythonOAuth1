import http.client
import time

#Supply 
consumer_key = "ChangeThisToYourKey"
consumer_secret = "ChangeThisToYourSecret"

timestamp = str(int(time.time()))
nonce = str(int(time.time() * 1000));
callback_uri = "oob"
signare_method = "PLAINTEXT"
version = "1.0"


print(f"Timestamp: {timestamp}")
print(f"Nonce: {nonce}")

conn = http.client.HTTPSConnection("lrs.adlnet.gov")
payload = f'oauth_consumer_key={consumer_key}&oauth_callback={callback_uri}&oauth_signature_method={signare_method}&oauth_signature={consumer_secret}%26&oauth_nonce={nonce}&oauth_timestamp={timestamp}&oauth_version={version}'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
  #'Cookie': 'csrftoken=CIT2PhXRe6B8MONugXxgTcQ5DrYHXPjG7KeOHizVJ476JMCGdaUVAMeni5ui44Vf'
}
conn.request("POST", "/xAPI/OAuth/initiate", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))