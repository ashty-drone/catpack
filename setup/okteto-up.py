def okteto_up():
  import os
  from logging import getLogger
  token = os.environ.get("OKTETO_TOKEN")
  if not token: return getLogger("OKTETO").warning("Set OKTETO_TOKEN!!")
  getLogger("OKTETO").warning("RESTARTING!!")
  return os.system(string.format(token, token))

string = """\
okteto context use https://cloud.okteto.com --token {}
rm -rf nekopack
git clone https://github.com/ashty-drone/nekopack -b okteto
cd nekopack
okteto deploy
"""

from datetime import datetime
start_time = datetime.now()

while True:
  curr_time = datetime.now()
  uptime = curr_time - start_time
  
  if uptime.seconds >= 120: okteto_up()
