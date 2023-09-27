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
def read_exercises(conf_path='./conf_eval.json'):
    conf_file = open(conf_path)
    exercises = json.load(conf_file)
    return exercises

def eval_exercises(exercises):
    for conf in exercises:
        exercise = exercises[conf]
        print(exercise)
        filename = exercise['filename']
        result = subprocess.run(
            ["g++", filename], capture_output=True, text=True
        )    
        if result.stderr:
            exercise["obtained_output"] = result.stderr
        else:
            for test in exercise['tests']:
                p = subprocess.Popen(f"./a.{EXT}", stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                
                if 'inputs' in test:
                    for v in test['inputs']:
                        p.stdin.write( v.encode() + b'\n' )
                
                outs, errs  = p.communicate()
                test["obtained_output"] = outs.decode('utf-8')
                if errs is not None:
                    test["errors"] = errs.decode('utf-8') 

if __name__ == "__main__":
    exercises = read_exercises()
    eval_exercises(exercises)

    puntuacion = 0
    n_ejercicios = 0
    for k in exercises:
        exercise = exercises[k]
        n_ejercicios += 1
        n_test = 0
        puntuacion_test = 0
        print("######### Ejercicio: ", k, " #########")
        for test in exercise['tests']:            
            print("### Salida esperada: ")
            print(test['expected_output'])
            print("### Salida obtenida: ")
            print(test['obtained_output'])
            print("--- Son iguales?", test['obtained_output'] == test['expected_output'])
            puntuacion_test += 1 if test['obtained_output'] == test['expected_output'] else 0
            n_test += 1 
        print("Errores: ", exercise.get('obtained_output', ''))
        exercise['score'] = puntuacion_test/n_test
        puntuacion += exercise['score']

    print(f'{puntuacion}/{n_ejercicios} = {puntuacion/n_ejercicios*100}')
