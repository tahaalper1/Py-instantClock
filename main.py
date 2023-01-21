import time
import os

while True:

    zaman=time.localtime()
    yıl=zaman[0]
    ay=zaman[1]
    gün=zaman[2]
    saat=zaman[3]
    dakika=zaman[4]
    saniye=zaman[5]
    os
    print(f"""
    Tarih : {gün}/{ay}/{yıl}
    Saat  : {saat}:{dakika}:{saniye}""")



