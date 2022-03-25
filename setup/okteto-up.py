import os
from sys import exit

token = os.environ.get("OKTETO_TOKEN")
if not token: exit("#"*10 + "\nSet OKTETO_TOKEN!!" + "#"*10)

OKTETO = dict()
  
def okteto_up():
  from logging import getLogger
  getLogger("OKTETO").warning("RESTARTING!!")
  return os.system(string.format(token))

string = """\
okteto context use https://cloud.okteto.com --token {}
rm -rf nekopack
git clone https://github.com/ashty-drone/nekopack -b okteto
cd nekopack
okteto push
"""

from datetime import datetime
start_time = datetime.now()

OKTETO.update({"deployed"}: False})

while not OKTETO["deployed"]:
  curr_time = datetime.now()
  uptime = curr_time - start_time
  if uptime.seconds >= 120: OKTETO.update({"deployed"}: True}); okteto_up()
