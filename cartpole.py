import gymnasium as gym
import pygame

env = gym.make("CartPole-v1", render_mode="human")

try:
    observation, info = env.reset()
    running = True

    for episode in range(1, 11):
        steps = 0

        while running:
            # Handle window closing and the Escape key.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            if not running:
                break

            action = env.action_space.sample()
            observation, reward, terminated, truncated, info = env.step(action)
            steps += 1

            if terminated or truncated:
                print(f"Episode {episode}: {steps} steps")
                break

        if not running:
            break

        if episode < 10:
            observation, info = env.reset()

finally:
    env.close()