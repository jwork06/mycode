#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests

# Define our "base" API
API = "https://api.nasa.gov/DONKI/GST?startDate=2016-01-01&endDate=2016-01-30&api_key=XWFii684Yigi9fhGjdFp53vuUr94g6LbafYdUzFV" # this will never change regardless of the lookup we perform

def main():
    """Run time code"""

    setcode = input("What is date/time of the geomagnetic storm you are trying to lookup? ").lower() # collect user input for MTG card set to lookup

    # create resp, which is our request object
    resp = requests.get(f"{API}linkedEvents?activityID={setcode}")   # this "f" string reads: API + "cards/" + setcode

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    cards = resp.json()

    print(cards)

if __name__ == "__main__":
    main()

