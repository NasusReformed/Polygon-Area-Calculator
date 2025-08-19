import copy
import random

class Hat:
    def __init__(self, **kwargs):
        # Crear la lista de bolas según los colores y cantidades proporcionadas
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        # Verificamos si el número de bolas a extraer es mayor que las bolas disponibles
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()  # Copiar todas las bolas disponibles
            self.contents = []  # Vaciar el contenido del sombrero
            return drawn_balls
        
        # Si hay suficientes bolas para extraer, proceder a sacarlas aleatoriamente
        drawn_balls = []
        for _ in range(num_balls):
            drawn_balls.append(self.contents.pop(random.randrange(len(self.contents))))
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        # Crear una copia del sombrero para no modificar el original
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)

        # Contar la cantidad de cada color en las bolas extraídas
        drawn_count = {}
        for color in drawn:
            drawn_count[color] = drawn_count.get(color, 0) + 1

        # Verificar si las bolas extraídas cumplen con el número esperado de bolas
        success = True
        for color, expected_count in expected_balls.items():
            if drawn_count.get(color, 0) < expected_count:
                success = False
                break

        if success:
            success_count += 1

    # Calcular la probabilidad
    return success_count / num_experiments
hat = Hat(blue=5, red=4, green=2)

# Realizar el experimento con los parámetros deseados
probability = experiment(
    hat=hat,
    expected_balls={'red': 1, 'green': 2},  # Queremos al menos 1 bola roja y 2 bolas verdes
    num_balls_drawn=4,  # Extraemos 4 bolas
    num_experiments=2000  # Realizamos 2000 experimentos
)

print(probability)
