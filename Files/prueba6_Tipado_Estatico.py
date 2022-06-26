from typing import Dict,List,Tuple

def suma(a:int,b:int) -> int:
    return a+b

print(type(suma("1","2")))


positives:List[int]=[1,2,3,4,5]

users: Dict[str,int]={"argentina":1,
                      "mexico":10,}


coordinatestype=List[Dict[str,Tuple[int,int]]]

coordinates:coordinatestype=[{"coor1":(1,2),"coor2":(3,5)},
                     {"coord1":(0,1),"coord2":(2,5)}]


print(users)


