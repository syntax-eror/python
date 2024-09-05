#/usr/bin/env python3

from tenable.io import TenableIO
from pprint import pprint
import getpass, re

accessKey = getpass.getpass("Enter access key: ")
secretKey = getpass.getpass("Enter secret key: ")

tio = TenableIO(accessKey, secretKey)

#get gropuIDs from API request or going into Tenable web portal and navigating to Settings > Sensors > Groups and selecting the group. Group ID will be the end of URL
winWSGroupID = <integerhere>
winServerGroupID = <integerhere>

for agent in tio.agents.list():
    try:
        unassignedGroup = agent['groups'] #check if groups field is populated
    except: #if groups field is blank, agent is not assigned to a group
        if agent['platform'] == "WINDOWS":
            agentName = agent['name']
            agentNameSearch = re.search("WS", agentName)
            if agentNameSearch:
                tio.agent_groups.add_agent(winWSGroupID, agent['id'])
                print("Agent", agentName, "added to Windows Workstations group")
            else:
                print("Windows agent", agentName , "not added, check if it's a server")
                
input("Press <ENTER> to exit")
