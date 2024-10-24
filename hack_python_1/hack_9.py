"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    i = 0
    while i < len(result):
        # Inserta el símbolo "@" en la posición i+1
        result.insert(i + 1, "@")
        # Incrementa el índice i en 2 para considerar el nuevo elemento "@"
        i += 2
    return result  