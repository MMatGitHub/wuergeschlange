import os
import protokolliere

def verified_int(i):
    if not isinstance(i, int):
        protokolliere.fehler(f"i: Variable {i} is *not* an integer")
        return None
    return i    
def verified_string(s):
    if not isinstance(s, str):
        protokolliere.fehler(f"i: Variable {s} is *not* a String")
        return None
    return s    
def verified_filepath(fp):
    if not os.path.isfile(fp):
        protokolliere.fehler(f"i: Filepath {fp} is *not* existing!")
        return None
    return fp