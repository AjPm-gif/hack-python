"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    result = result[:-1] + result[-1].upper()  # Reemplaza el último carácter por su versión en mayúscula
    return result