def is_primitive_root(g, p):    # Check if g is a primitive root modulo p
    for i in range(2, p - 1):
        if pow(g, i, p) == 1:
            return False
    return True

def min_prim(p):    # Find the smallest primitive element in the finite field Fp
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g

p = 28151
primitive_element = min_prim(p)
print(primitive_element)
