import os
import subprocess
import scrap10
import scrap9
import scrap8
import scrap7
import scrap6
import scrap5
import scrap4
import scrap3
import scrap2
import scrap1

from multiprocessing import Process
from scrap10 import bucle10
from scrap9 import bucle9
from scrap8 import bucle8
from scrap7 import bucle7
from scrap6 import bucle6
from scrap5 import bucle5
from scrap4 import bucle4
from scrap3 import bucle3
from scrap2 import bucle2
from scrap1 import bucle1

exec('scrap10')
exec('scrap9')
exec('scrap8')
exec('scrap7')
exec('scrap6')
exec('scrap5')
exec('scrap4')
exec('scrap3')
exec('scrap2')
exec('scrap1')


if __name__ == '__main__':
    print("corriendo subprocesos...")
    proc = Process(bucle10())
    proc.start()
    proc.join()
    proc = Process(bucle9())
    proc.start()
    proc.join()
    proc = Process(bucle8())
    proc.start()
    proc.join()
    proc = Process(bucle7())
    proc.start()
    proc.join()
    proc = Process(bucle6())
    proc.start()
    proc.join()
    proc = Process(bucle5())
    proc.start()
    proc.join()
    proc = Process(bucle4())
    proc.start()
    proc.join()
    proc = Process(bucle3())
    proc.start()
    proc.join()
    proc = Process(bucle2())
    proc.start()
    proc.join()
    proc = Process(bucle1())
    proc.start()
    proc.join()




