#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Printing dictionary data stored as lists to the screen"""


def main():
    """On this farm there was a..."""

    # this is the data we want to loop across
    # it is a list containing 3 dictionaries
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    for farm in farms:
        print(farm.get("name", "Unknown Farm"), end=":\n") 
        for agri in farm.get("agriculture"):    
            print("  -", agri)     


    question = input("Please choose a farm (NE Farm, W Farm, SE Farm): ")
    if question.lower() == "ne farm":
        for farm in farms.get("name", "NE Farm"):
            for agri in farm.get("agriculture"):
                print(" -", agri)
if __name__ == "__main__":
    main()

