'''Calcula el tercer ángulo de un triángulo con los otros dos conocidos.'''
def find_third_angle(angle1, angle2):
    # Calcula el tercer ángulo restando los dos ángulos conocidos de 180 grados
    third_angle = 180 - (angle1 + angle2)
    return third_angle

# Ejemplos de uso
print(find_third_angle(60, 60))  # 60
print(find_third_angle(45, 45))  # 90
print(find_third_angle(30, 90))  # 60
