# This run's the earth.py

import earth
import sys
import os

file_name = os.path.basename(sys.argv[0])

class EngineReload(earth.Earth):

    def __init__(self) -> None:
        # Comment out the try methods if in prod
        try:
            planet: earth.Earth = earth.Earth()
        except:
            print(f'{file_name}/[Dev]:  Application not Working')
        else:
            print(f'{file_name}/[Dev]:  Application is Working')

start: EngineReload = EngineReload()