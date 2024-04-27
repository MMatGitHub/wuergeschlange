mit = None
algorithmus = None

def do():
   print(f"i: executing algorithmus [{mit}] ...")
   algorithmus(mit)
   return f"i: executed algorithmus [{mit}]" 

def tu(cmdStringNameOfFunctionPointer, name):
   cmdStringNameOfFunctionPointer(name)