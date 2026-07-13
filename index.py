import random

class FlyPBirdAI:
    def __init__(self):
        self.gravity = 0.45
        self.jump_force = -7.5
        self.velocity = 0

    def update(self):
        self.velocity += self.gravity

    def jump(self):
        self.velocity = self.jump_force

    def decide(self, bird_y, gap_y, distance):
        """
        bird_y: posição vertical do pássaro
        gap_y: centro da abertura do cano
        distance: distância horizontal até o cano
        """

        # Previsão simples da posição futura
        time = max(distance / 5, 1)
        predicted_y = bird_y + self.velocity * time + 0.5 * self.gravity * time**2

        erro = predicted_y - gap_y

        # Margem dinâmica
        margem = 12 + abs(self.velocity) * 2

        if erro > margem:
            self.jump()
            return True

        return False


# Simulação
ai = FlyPBirdAI()

bird_y = 250
gap_y = 220

for frame in range(60):
    distancia = max(10, 200 - frame * 3)

    ai.update()

    if ai.decide(bird_y, gap_y, distancia):
        print(f"Frame {frame}: PULO")

    bird_y += ai.velocity

    print(
        f"Y={bird_y:.1f} | Vel={ai.velocity:.2f} | Dist={distancia}"
    )
