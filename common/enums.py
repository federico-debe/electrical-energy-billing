from enum import Enum


class ConsumerType(Enum):
    RESIDENTIAL_DOMESTIC = 0  
    DOMESTIC_NO_RESIDENTIAL = 1
    BT_PUBLIC_LIGHTING = 2 
    BT_PUBLIC_CHARGING_INFRASTRUCTURES_FOR_ELECTRIC_VEHICLES = 3
    BT_OTHER = 4 # Low Voltage Other Uses
    MT_PUBLIC_LIGHTING = 5
    MT_OTHER = 6 # Medium Voltage               
    AT = 7 # High Voltage
    ATT = 8 

class ShiftType(Enum):
    '''time slots for energy consumption'''
    F1 = 'F1'
    F2 = 'F2'
    F3 = 'F3'

class ConcessionsType(Enum):
    NO_CONCESSIONS = 0 # nessuna agevolazione
    ASOS1 = 1
    ASOS2 = 2
    ASOS3 = 3
    VALR = 4 # agevolazione per imprese energivore

