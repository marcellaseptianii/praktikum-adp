import time
import os
import cowsay 
from termcolor import cprint,colored

teks = "     Happy Eid  🌙    "  # teks scrolling
lebar = 20  
durasi = 20  
jeda = 0.2 

langkah = int(durasi / jeda)

for i in range(langkah):
    mulai = i % len(teks)
    scrolled = (teks + teks)[mulai:mulai+lebar]
    os.system('cls')
    cprint(cowsay.cow(colored(scrolled, 'light_cyan', attrs=['bold'])))
    time.sleep(jeda)
