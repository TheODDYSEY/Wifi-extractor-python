import subprocess
import os
import re
from collections import namedtuple
import configparser

def get_windows_saved_ssid():
    # gets all the saved profiles in the PC
    output = subprocess.check_output("netsh wlan show profiles").decode()
    ssids = []
    profiles = re.findall(r"All User Profile\s(.*)",output)
    for profile in profiles:
        # for each SSID ,remove spaces and colon
        ssid = profile.strip().strip(":").strip()
        # add to the list
        ssids.append(ssid)
    return ssids    