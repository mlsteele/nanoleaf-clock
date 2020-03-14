import requests
from pprint import pprint
import time
from secrets import ip, port, auth_token

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
def anim_data(data):
  # https://forum.nanoleaf.me/docs/openapi#_sh5xwlxaz1pa
  res = f"{len(data)}"
  for (panel_id, frames) in data.items():
    res += f" {panel_id} {len(frames)}"
    for [r, g, b, t] in frames:
      w = 0
      res += f" {r} {g} {b} {w} {t}"
  return res

def get_panel_ids():
  return [panel['panelId'] for panel in api_call("GET", "panelLayout/layout")['positionData']]

# panel_ids_raw = get_panel_ids()
panel_ids_raw = [251, 126, 87, 209, 8, 203, 48, 122, 162, 191]
panel_ids_reorder = [10, 1, 2, 9, 3, 4, 5, 6, 8, 7]
panel_ids = [x[0] for x in sorted(zip(panel_ids_raw, panel_ids_reorder), key=lambda x: x[1])]

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

# pprint(api_call("PUT", "effects", {"write": {
#   "command": "display",
#   "animType": "custom",
#   "animData": anim_data({
#     162: [(255, 255, 255, 5), (255, 0, 0, 10)],
#   }),
#   "loop": True,
# }}))

print(panel_ids)
for panel_id in panel_ids:
  api_call("PUT", "effects", {"write": {
    "command": "display",
    "animType": "custom",
    "animData": anim_data({
      panel_id: [(255, 255, 255, 2), (255, 0, 0, 4)],
    }),
    "loop": True,
  }})
  time.sleep(1)
  api_call("PUT", "effects", {"write": {
    "command": "display",
    "animType": "custom",
    "animData": anim_data({
      panel_id: [(0, 0, 0, 5)],
    }),
    "loop": False,
  }})
