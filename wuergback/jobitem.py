import time
import fileio
from typing import List

class Jobitem:
    prg: str = "C:\\Users\\itbc000133\\AppData\\Local\\LOCALHOME\\repos\\no_upstream\\c_ae\\SYS\\portable\\7-ZipPortable\\App\\7-Zip64\\7z.exe"
    geheim: str = fileio.slurp("C:\\Users\\itbc000133\\AppData\\Local\\LOCALHOME\\repos\\upcshare_sec\\mima\\_ssh_geheim_pass\\wuergback.txt")
    quelle: str = "C:\\Temp\\test"
    ziel: str = "C:\\Temp\\backup"
    paketname: str = "testpaketname"
    paketendung: str = ".7z"
    archiv: str ="H:\\_backup\\quelle=RN049932\\cae"
    zeitstempel: str
    multiquellfolder: List[str]

    def __init__(self, quelle, ziel, paketname, multiquellfolder):
        self.quelle = quelle 
        self.ziel = ziel 
        self.paketname = paketname
        self.multiquellfolder = multiquellfolder
        self.zeitstempel=str(time.strftime("%Y.%m.%d_%H-%M-%S", time.localtime()))
        # debug raise NameError (str(paketname))
    def getPrg(self) -> str:
        return self.prg
    
    def getQuelle(self) -> str:
        return self.quelle

    def getZielpaket(self) -> str:
        return self.ziel + "\\" + self.paketname + "_" + self.zeitstempel + self.paketendung

    def getZielpaketfilename(self) -> str:
        return self.paketname + "_" + self.zeitstempel + self.paketendung
    
    def getArchivpaket(self) -> str:
        return self.archiv + "\\" + self.paketname + self.paketendung
    
    def getArchivpaketfilename(self) -> str:
        return self.paketname + self.paketendung