import gym
from gym import spaces
import numpy as np
from pygame_2d import PyGame2D

class CustomEnv(gym.Env):
    def __init__(self):
        self.pygame = PyGame2D()
        self.action_space = spaces.Discrete(5)
        self.observation_space = spaces.Box(np.array([0, 0, 0, 0, 0]), np.array([1080, 720, 1080, 720, 360]))

    def reset(self):
        del self.pygame
        self.pygame = PyGame2D()
        obs = np.array(self.pygame.observe())
        return obs

    def step(self, action):
        self.pygame.action(action)
        obs = self.pygame.observe()
        reward = self.pygame.evaluate()
        done = self.pygame.is_done()

        self.render() # It's a hack but it works, renders the env while training.

        return obs, reward, done, {}

    def render(self):
        self.pygame.view() 
