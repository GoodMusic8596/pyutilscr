import subprocess

def log(executed_file:str,dump_file_name:str):
	proc = subprocess.Popen(["python3",executed_file],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	f=open(dump_file_name,"w+")
	f.write(proc.communicate(input=None, timeout=None)[0].decode("utf-8"))
	f.close()