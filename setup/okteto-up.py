def okteto_up():
  import os
  from logging import getLogger
  getLogger("OKTETO").warning("RESTARTING!!")
  return os.system(string.format(os.environ.get("OKTETO_ACCESS_TOKEN")))

string = """\
okteto context use https://cloud.okteto.com --token {}
rm -rf nekopack
git clone https://github.com/ashty-drone/nekopack -b okteto
cd nekopack
okteto deploy --build
"""

from datetime import datetime
start_time = datetime.now()

while True:
  curr_time = datetime.now()
  uptime = curr_time - start_time
  
  if uptime.seconds >= 5: okteto_up()
