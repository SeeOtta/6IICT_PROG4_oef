import json

""" Volgende info ontbreekt in oefen_mee10.json:
 - De koningin.
 - Het aantal lopers.

"""
def schaak_info(info):
    teller = 0
    for stuk, stuk_info in info.items():
        zin = f"""Er zijn {stuk_info['aantal']} {stuk}. 
                    De engelse naam is {stuk_info['engelse_naam']}. 
                    Ze bewegen {stuk_info['beweging']}"""
        teller+=1
        print(zin)

    if teller < 6:
        raise IndexError("Er zijn te weinig schaak stukken ingegeven")
    if "/" in stuk_info['aantal']:
        raise TypeError("De ingegeven waarde is geen getal")
    
try:      
    fp = open("Leerkracht_Bestanden/6IICT_PROG4_oef/hfst_3/oefeningen/oefen_mee10.json", "r")
    info = json.load(fp)
    schaak_info(info)
except KeyError:
    print("Deze waarde bestaat niet")
except IndexError:
    print("te weinig stukken opgegeven")
except FileNotFoundError:
    print("dit bestand bestaat niet")

else:
    fp.close()