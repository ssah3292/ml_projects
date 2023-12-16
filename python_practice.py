#from src.DimondPricePrediction.logger import logging

# https://www.datacamp.com/tutorial/role-underscore-python

# https://www.dataquest.io/blog/how-to-use-python-data-classes/

"""Usage od ... (ellipsis)"""

#Accessing and slicing multidimensional Arrays/NumPy indexing

import numpy as np
from typing import Callable
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json
from typing import Final


ASTRA_TOKEN_PATH: Final[str] = "ml_practice-token.json"
ASTRA_DB_SECURE_BUNDLE_PATH: Final[str] = "secure-connect-ml-practice.zip"

with open(ASTRA_TOKEN_PATH, "r") as f:
    creds = json.load(f)
    ASTRA_DB_APPLICATION_TOKEN = creds["token"]

"""
    [:, :, :, 0] is same as [ … , 0]
    We should always use colons for accessing the other dimensions i.e. ‘ : ‘.
"""

def ellpisisTest1():
    array=np.random.rand(2,3)
    print(array)
    print(array[..., 1])
    #print(array[Ellipsis, 0])
   

#In type hinting
def ellpisisTest2(name: str)->str:
    return "Hello, " + name

def ellpisisTest3(name: ... )->str:
    print(type(name).__name__)
    if type(name).__name__ == "str":
        return "Hello String, " + name
    else:
        return "Hello Int, " + str(name)
    

def function_name(arg1: int, arg2: int, x:...) -> int:
    ...




def inject(get_next_item: Callable[..., str]) -> None: # Doubt what is the syntax
			...
# Argument type is assumed as type: Any
def foo(x: ...) -> None:
			...


#ellpisisTest1
print(ellpisisTest3(1))



cluster = Cluster(
    cloud={
        "secure_connect_bundle": ASTRA_DB_SECURE_BUNDLE_PATH,
    },
    auth_provider=PlainTextAuthProvider(
        "token",
        ASTRA_DB_APPLICATION_TOKEN,
    ),
)

session = cluster.connect()
row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")




