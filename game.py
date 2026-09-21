import pygame, pymunk, math, os

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
bird_raw = pygame.image.load(os.path.join(ASSETS_DIR, "bird.png")).convert_alpha()
pig_raw = pygame.image.load(os.path.join(ASSETS_DIR, "pig.png")).convert_alpha()

space = pymunk.Space()
space.gravity = (0, 900)

floor = pymunk.Segment(space.static_body, (0, 550), (WIDTH, 550), 5)
floor.friction, floor.elasticity = 0.6, 0.3
space.add(floor)

BLOCK_SIZE = (40, 40)
pig_image = pygame.transform.smoothscale(pig_raw, BLOCK_SIZE)
bird_image = pygame.transform.smoothscale(bird_raw, (30, 30))

blocks, projectiles = [], []
for row in range(4):
    for col in range(2):
        body = pymunk.Body(1, pymunk.moment_for_box(1, BLOCK_SIZE))
        body.position = (600 + col * 45, 520 - row * 50)
        shape = pymunk.Poly.create_box(body, BLOCK_SIZE)
        shape.friction, shape.elasticity = 0.5, 0.2
        space.add(body, shape)
        blocks.append(body)

def launch_projectile(pos, impulse):
    body = pymunk.Body(3, pymunk.moment_for_circle(3, 0, 15))
    body.position = pos
    shape = pymunk.Circle(body, 15)
    shape.friction, shape.elasticity = 0.5, 0.6
    space.add(body, shape)
    body.apply_impulse_at_local_point(impulse)
    projectiles.append(body)

launch_origin = (150, 450)
dragging, running = False, True

while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if math.hypot(mouse_pos[0] - launch_origin[0], mouse_pos[1] - launch_origin[1]) < 40:
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and dragging:
            dx, dy = launch_origin[0] - mouse_pos[0], launch_origin[1] - mouse_pos[1]
            launch_projectile(launch_origin, (dx * 15, dy * 15))
            dragging = False

    space.step(1.0 / 60.0)
    screen.fill((30, 30, 35))
    pygame.draw.line(screen, (100, 100, 100), (0, 550), (WIDTH, 550), 5)

    for body in blocks:
        rot = pygame.transform.rotate(pig_image, -math.degrees(body.angle))
        screen.blit(rot, rot.get_rect(center=(round(body.position.x), round(body.position.y))))

    for body in projectiles:
        rot = pygame.transform.rotate(bird_image, -math.degrees(body.angle))
        screen.blit(rot, rot.get_rect(center=(round(body.position.x), round(body.position.y))))

    if dragging:
        pygame.draw.line(screen, (255, 80, 80), launch_origin, mouse_pos, 3)
        pygame.draw.circle(screen, (255, 200, 0), launch_origin, 8)
        screen.blit(bird_image, bird_image.get_rect(center=mouse_pos))
    else:
        screen.blit(bird_image, bird_image.get_rect(center=launch_origin))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()