# Core
import json
import logging
import logging.config

# Third-party
import requests
from bs4 import BeautifulSoup


logging.config.fileConfig('logging.conf')
logger = logging.getLogger('console')


class GrabData:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get_data(self):
        r'''
            Returns the JSON data we need to return
        '''
        r = requests.get(self.endpoint)
        soup = BeautifulSoup(r.text, "html.parser")

        # Gets all script tags
        all_scripts = soup.find_all('script')

        '''
        Since the data we need is inside a text of a script
            tag, we have to grab the 22th script position and
            see where in between the text to find the JSON we
            need
        '''
        script_with_data = all_scripts[22]
        logger.debug(script_with_data)
        raw_data = script_with_data.get_text()[2638:22314]
        logger.debug(raw_data)
        data = json.loads(raw_data)
        logger.debug(data)
        return data
