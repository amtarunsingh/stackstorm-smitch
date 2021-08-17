import sys
import json 
import dns
import requests

from st2common.runners.base_action import Action

class SmitchPlugAction(Action):
    def run(self, xApiKey, userId, deviceId, powerStatus):

        header = {
            'Accept': 'application/json',
            'x-api-key': xApiKey
        }
        url = 'https://app.api.developer.mysmitch.com/v1/app/job/device'
        myobj = {
            "user_id": userId,
            "commands": [
                {
                    "device_id": deviceId,
                    "device_settings": {
                        "power_status": powerStatus
                    }
                }
            ]
        }

        plug = requests.post(url, data = myobj, headers = header)
        return(plug.status_code, plug)