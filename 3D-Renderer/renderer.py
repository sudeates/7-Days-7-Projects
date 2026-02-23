import pygame
import math

# Ekran Ayarları
WIDTH, HEIGHT = 800, 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Küpün Köşe Noktaları (X, Y, Z)
points = [
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1],
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1]
]

angle = 0 # Dönüş açısı

while True:
    screen.fill((0, 0, 0)) # Ekranı temizle (Siyah)
    angle += 0.01 # Her karede biraz döndür

    projected_points = []
    for p in points:
        # 1. Döndürme Matematiği (Y ekseni etrafında)
        x = p[0] * math.cos(angle) - p[2] * math.sin(angle)
        z = p[0] * math.sin(angle) + p[2] * math.cos(angle)
        y = p[1]

        # 2. Projeksiyon (3D -> 2D)
        # Z ekseni uzaklaştıkça noktayı küçültüyoruz (Derinlik algısı)
        f = 200 / (z + 4)
        x_2d = x * f + WIDTH // 2
        y_2d = y * f + HEIGHT // 2
        projected_points.append([x_2d, y_2d])

        # Noktaları çiz
        pygame.draw.circle(screen, (0, 255, 0), (int(x_2d), int(y_2d)), 5)

    # 3. Kenarları Birleştir (Küp oluştur)
    for i in range(4):
        pygame.draw.line(screen, (255, 255, 255), projected_points[i], projected_points[(i+1)%4])
        pygame.draw.line(screen, (255, 255, 255), projected_points[i+4], projected_points[((i+1)%4)+4])
        pygame.draw.line(screen, (255, 255, 255), projected_points[i], projected_points[i+4])

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    clock.tick(60)