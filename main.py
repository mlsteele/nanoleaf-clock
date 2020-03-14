from nanoleaf.nanoleaf import setup
from nanoleaf.nanoleaf import Aurora
import requests
from pprint import pprint
from secrets import ip, port, auth_token

# ips = setup.find_auroras()
# print(ips)

# mac address 00:55:DA:50:A2:58
# token = setup.generate_auth_token(ip)
# print(token)

# my_aurora = Aurora(ip, auth_token)
# my_aurora.on = True
# my_aurora.effect = "Violets Are Blue"

def api_call(method, endpoint, data=None):
  url = f"http://{ip}:{port}/api/v1/{auth_token}/{endpoint}"
  print(f"> {method} {url}")
  print(f"  {data}")
  res = requests.request(method, url, json=data)
  res.raise_for_status()
  if res.text == "":
    return None
  return res.json()

# Takes a map from panel ID to a list of frames.
# Each frame is a list [r, g, b, t].
# Frames other than the first for each panel seem to have no effect.
def anim_data(data):
  # https://forum.nanoleaf.me/docs/openapi#_sh5xwlxaz1pa
  res = f"{len(data)}"
  for (panel_id, frames) in data.items():
    res += f" {panel_id} {len(frames)}"
    for [r, g, b, t] in frames:
      w = 0
      res += f" {r} {g} {b} {w} {t}"
  return res

# pprint(api_call("GET", ""))
# pprint(api_call("GET", "state"))
# print(api_call("GET", "state/on"))
# print(api_call("PUT", "state", {"on": {"value": False}}))

# print(api_call("PUT", "state", {
#   'on': {'value': True},
#   'brightness': {'value': 30},
# }))

# print(api_call("PUT", "identify"))

# pprint(api_call("PUT", "effects", {"write": {"command": "requestAll"}}))

# Set one panel
# pprint(api_call("PUT", "effects", {"write": {
#   "command": "display",
#   "animType": "static",
#   "animData": "1 162 1 255 0 0 0 1",
#   "loop": False,
# }}))

pprint(api_call("PUT", "effects", {"write": {
  "command": "display",
  "animType": "static",
  "animData": anim_data({
    162: [(255, 255, 0, 20)],
  }),
  "loop": False,
}}))
