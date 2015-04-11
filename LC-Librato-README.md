# LendingClub-to-Librato-API-2-API
LendingClub.com to Librato.com Pull and Post
This is a very simple few lines to pull your information out of lendingclub.com using their API.
It then pushes the same data it pulled out over to Librato.com to display in a beautiful dashboard.

A few issues I ran into were the following:
1) URLLIB3 SSL Warnings - https://urllib3.readthedocs.org/en/latest/security.html
    - I implemented the recommended fix to route through pyopenssl
    
2) Requests Issues- https://bugs.launchpad.net/ubuntu/+source/python-pip/+bug/1306991
    - I'm running LinuxMint 17.1 (rebecca); and experienced several issues post installation of requests
    - Purge requests out by going to the directory and removing them as noted above
    - PIP should operate correctly
      - Check to see if requests is on the system still - as somehow mine was still present despite me removing as shown above

3) Required Libraries:
  import time
  import json
  import requests # This may or may not need to be __Installed depending on your system.
  import urllib3.contrib.pyopenssl   #pip install pyopenssl ndg-httpsclient pyasn1 
  import librato # pip install librato-metrics
  
  
Note... no error checking is present... I recommend at least a try/except on the Pull and Push from API to API
