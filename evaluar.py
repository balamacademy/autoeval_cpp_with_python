import os
import subprocess
import json

from sys import platform
if platform == "linux" or platform == "linux2" or  platform == "darwin":
    EXT = "out"
elif platform == "win32":
    EXT = "exe"

dir_path = r'.'
res = []

conf_file = open('conf_eval.json')
ejercicios = json.load(conf_file)

for file_path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, file_path)):
        if file_path[-3:] == "cpp":
            res.append(file_path)

for program in res:
    conf = ejercicios.get(program, None)
    if conf is not None:
        result = subprocess.run(
            ["g++", program], capture_output=True, text=True
        )    
        if result.stderr:
            conf["salida_obtenida"] = result.stderr
        else:
            p = subprocess.Popen(f"./a.{EXT}", stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            
            if 'inputs' in conf:
                for v in conf['inputs']:
                    p.stdin.write( v.encode() + b'\n' )
            
            outs, errs  = p.communicate()
            conf["salida_obtenida"] = outs.decode('utf-8')
            if errs is not None:
                conf["errors"] = errs.decode('utf-8')          

puntuacion = 0
n_ejercicios = 0
for k in ejercicios:
    n_ejercicios += 1
    print(k)
    print(ejercicios[k]['salida_obtenida'], ejercicios[k]['salida_esperada'], ejercicios[k]['salida_obtenida'] == ejercicios[k]['salida_esperada'])
    puntuacion += 1 if ejercicios[k]['salida_obtenida'] == ejercicios[k]['salida_esperada'] else 0

print(ejercicios)
print(f'{puntuacion}/{n_ejercicios} = {puntuacion/n_ejercicios*100}')