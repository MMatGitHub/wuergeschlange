import subprocess
import protokolliere
def check_output(command):
    try:
        process = subprocess.Popen(command, shell=True, encoding="cp437", stdout=subprocess.PIPE)
        
        while True:
            output = process.stdout.readline().strip()
            
            if not output and process.poll() is not None:
                break
                
            if output:
                #print(output, flush=True)
                protokolliere.debug(output)

    except Exception as e:
        raise RuntimeError(f"Failed to execute command '{command}'. Error message: {e}")

def testkommando():
    command = "dir c:\\Windows /s"
    check_output(command)
    
testkommando()


 
 
 
