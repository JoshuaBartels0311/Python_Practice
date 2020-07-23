
cd /home/student/mycode/
mkdir iftest2/
vim iftest2/ipstatic.py

#!/usr/bin/env python3
ipchk = "192.168.0.1"

# a string tests as True
if ipchk:
   print("Looks like the IP address was set: " + ipchk)


chmod u+x iftest2/ipstatic.py

./iftest2/ipstatic.py

vim iftest2/ipask.py


#!/usr/bin/env python3
ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true
if ipchk:
   print("Looks like the IP address was set: " + ipchk) # indented under if

./iftest2/ipask.py

vim iftest2/ipask.py

#!/usr/bin/env python3
ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true
if ipchk:
   print("Looks like the IP address was set: " + ipchk) # indented under if
else:    # if data is NOT provided
   print("You did not provide input.") # indented under else

,/iftest2/ipask.py

vim iftest2/ipask2.py

#!/usr/bin/env python3
ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# if user set IP of gateway
if ipchk == "192.168.70.1":
   print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk: # if any data is provided, this will test true
   print("Looks like the IP address was set: " + ipchk) # indented under if
else: # if data is NOT provided
   print("You did not provide input.") # indented under else

./iftest2/ipask2.py

