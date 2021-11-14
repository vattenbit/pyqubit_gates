import numpy as np

def mult(a,b):
  return a.dot(b)

#qubits
q0 = [
  [0],
  [1]
]
q0 = np.array(q0)

#not gate
not_gate = [
  [0,1],
  [1,0]
]
not_gate = np.array(not_gate)

#main
result = mult(not_gate,q0)
print("Result: \n{}".format(result))
