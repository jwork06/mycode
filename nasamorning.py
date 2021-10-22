#!/usr/bin/env python3
import requests

API = "http://api.open-notify.org/iss-now.json" 

def main():
    """Run time code"""

    resp = requests.get(f"{API}") 
    cardsets = resp.json().get("iss_position")
    print(cardsets)      

if __name__ == "__main__":
    main()
