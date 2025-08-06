import subprocess
import json

def analizar_archivo(file_path:str):
    output=subprocess.check_output(["./rust/target/release/reporter"],file_path)
    return json.loads(output)