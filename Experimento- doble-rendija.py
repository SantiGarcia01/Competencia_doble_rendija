import numpy as np
import math

def sistema_pro(v2, m2, clicks):
    cont = 0
    while cont < clicks:
        result = np.dot(m2, v2)
        v2 = np.transpose(result)
        cont += 1
    return v2

def sistema_cua(v3, m3, clicks):
    cont = 0
    while cont < clicks:
        result = np.dot(m3, v3)
        v3 = np.transpose(result)
        cont += 1
    return v3

def main():

   v2 = np.array ([1,0,0,0,0,0,0,0])
   m2 = np.matrix ([[0,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0], [0,1/3,0,1,0,0,0,0], [0,1/3,0,0,1,0,0,0], [0,1/3,1/3,0,0,1,0,0], [0,0,1/3,0,0,0,1,0], [0,0,1/3,0,0,0,0,1]])
   v3 = np.array([1,0,0,0,0,0,0,0])
   m3 = np.matrix([[0,0,0,0,0,0,0,0],[complex(0, 1/math.sqrt(2)),0,0,0,0,0,0,0],[complex(0, 1/math.sqrt(2)),0,0,0,0,0,0,0], [0,complex(0, -1/math.sqrt(3)),0,1,0,0,0,0], [0,complex(0,1/math.sqrt(3)),0,0,1,0,0,0], [0,complex(0, -1/math.sqrt(3)),complex(0, -1/math.sqrt(3)),0,0,1,0,0], [0,0,complex(0, 1/math.sqrt(3)),0,0,0,1,0], [0,0,complex(0, -1/math.sqrt(3)),0,0,0,0,1]])
   print (sistema_cua(v3, m3, clicks))

main()
