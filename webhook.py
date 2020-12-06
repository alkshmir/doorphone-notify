import urllib.request, json

def post(message):
    with open('discord_url', 'r') as f:
        url = f.read()
    method = 'POST'
    headers = {"Content-Type": "application/json"}
    
    content = {"content": message}
    json_data = json.dumps(content).encode("utf-8")
    
    request = urllib.request.Request(url, json_data, {"User-Agent":"curl/7.64.1", "Content-Type":"application/json"}, method)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")

if __name__ == "__main__":
    post('discord webhook test')
