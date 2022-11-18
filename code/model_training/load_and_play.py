from stable_baselines3 import PPO
from custom_env import CustomEnv
import os
import time


def simulate():
    for episode in range(MAX_EPISODES):
        done = False
        obs = env.reset()
        while not done:
            random_action = env.action_space.sample()
            obs, reward, done, info = env.step(random_action)
            env.render()
    
    env.close()

if __name__ == "__main__":
    env = CustomEnv()
    MAX_EPISODES = 5
    MAX_TRY = 1000
    model = PPO.load("./models/166808731/1002.zip")
    simulate()