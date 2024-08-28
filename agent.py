import os, http.client

def io():
  proxy,port = "io","80"
  try:
    agent = os.environ["AGENT"]
    parts = agent.split(':')  
    proxy = parts[0]
    if len(parts) > 1:
      port = parts[1]
  except:
    None
  return http.client.HTTPConnection(proxy,port)
