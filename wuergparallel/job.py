mit = None
algorithmus = None
import protokolliere
def do():
   protokolliere.info(f"i: executing algorithmus [{mit}] ...")
   algorithmus(mit)
   return f"i: executed algorithmus [{mit}]" 

def tu(cmdStringNameOfFunctionPointer, name):
   cmdStringNameOfFunctionPointer(name)