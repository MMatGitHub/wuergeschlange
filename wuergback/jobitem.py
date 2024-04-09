import time
import geheim
class Jobitem:
    prg: str = "C:\\Users\\itbc000133\\AppData\\Local\\LOCALHOME\\repos\\no_upstream\\c_ae\\SYS\\portable\\7-ZipPortable\\App\\7-Zip64\\7z.exe"
    geheim: str = geheim.get_geheim()
    quelle: str = "C:\\Temp\\test"
    ziel: str = "C:\\Temp\\backup"
    paketname: str = "testpaketname"
    paketendung: str = ".7z"
    archiv: str ="H:\_backup\quelle=RN049932\cae"
    zeitstempel: str = str(time.localtime(time.time()).tm_hour)+"-"+str(time.localtime(time.time()).tm_min)+"-"+str(time.localtime(time.time()).tm_sec)

    def __init__(self, quelle, ziel, paketname):
        self.quelle = quelle 
        self.ziel = ziel 
        self.paketname = paketname
    
    def getPrg(self) -> str:
        return self.prg
    
    def getQuelle(self) -> str:
        return self.quelle

    def getZielpaket(self) -> str:
        return self.ziel + "\\" + self.paketname + "_" + self.zeitstempel + self.paketendung
   
    def getArchivpaket(self) -> str:
        return self.archiv + "\\" + self.paketname + self.paketendung
    
      

