import os
from sys import exit
from subprocess import run
from logging import getLogger

token = os.environ.get("OKTETO_TOKEN")
if not token: exit("#"*25 + "\nSet OKTETO_TOKEN!!\n" + "#"*25)
  
def okteto_up():
  with open("okteto.sh", "w+") as f: f.write(string.format(token))
  getLogger("OKTETO").warning("RESTARTING!!")
  run(["sh", "okteto.sh"])
  os.remove("okteto.sh")

string = """\
okteto context use https://cloud.okteto.com --token {}
rm -rf nekopack
git clone https://github.com/ashty-drone/nekopack.git -b okteto
cd nekopack
okteto deploy
"""

while True:
  from datetime import datetime
  start_time = datetime.now()

  while True:
    curr_time = datetime.now()
    uptime = curr_time - start_time
    if uptime.seconds >= 84600: break
  
  okteto_up()
