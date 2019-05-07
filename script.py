
import argparse
import pandas as pd
import numpy as np
parser = argparse.ArgumentParser()
parser.add_argument("--OwnerID",nargs='?',help="Enter the OwnerID",default=1546,type=int)

def get_pet_names(owner):
    owners = pd.read_csv('owners.csv')
    pets = pd.read_csv('pets.csv')
    pets['pet_name']=pets.Name
    pets = pets.drop(columns='Name')
    df = pd.merge(pets,owners,on='OwnerID')
    return df[df.OwnerID==owner]['pet_name'] 
    


if __name__=='__main__':
    
    args = parser.parse_args()
    OwnerID = args.OwnerID
    print(get_pet_names(OwnerID))

