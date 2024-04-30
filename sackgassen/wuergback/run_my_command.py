import subprocess
import protokolliere

def run_cmd(command):
    try:
        result = subprocess.run(["cmd", "/c", command], shell=True, stdout=subprocess.PIPE, text=True, 
                        encoding="cp437")
        if result:
           return result
        else:
            return None
    except UnicodeDecodeError as e:
        protokolliere.err("UnicodeDecodeError occurred.", str(e))