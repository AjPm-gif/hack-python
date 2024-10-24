"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    text = "fooziman"
    result = []
    for char in text:
        if char == "o":
            result.append("0")
        elif char == "i":
            result.append("1")
        elif char == "a":
            result.append("@")
        else:
            result.append(char.upper())  # Convertir a mayúscula
    return result