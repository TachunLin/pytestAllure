

import yaml


class reader(object):


    def cap_reader(self, deviceName):

        with open("./config/desire_cap.yaml", 'r') as f:
            desired_caps = yaml.load(f.read())
            for key, value in desired_caps.items():
                # print(key)
                if key == deviceName:
                    return desired_caps[key]
                # print(desired_caps['AVD6.0'])

