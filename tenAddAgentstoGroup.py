#/usr/bin/env python3

accessKey = ' '
secretKey = ' '

from tenable.io import TenableIO
from pprint import pprint
import re

tio = TenableIO(accessKey, secretKey)

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