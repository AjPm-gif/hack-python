"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = ""  # Inicializa result como una cadena vacía
    text = "fooziman"  # Asigna la cadena "fooziman" a text
    for char in text:
        if char == "o":
            result += "0"
        elif char == "i":
            result += "1"
        elif char == "a":
            result += "@"
        else:
            result += char
    return result