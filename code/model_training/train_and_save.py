from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import SubprocVecEnv
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.atari_wrappers import MaxAndSkipEnv
from stable_baselines3.common.vec_env import VecMonitor

from custom_env import CustomEnv
import os
import time
import tensorboard
# tensorboard --logdir=logs

models_dir = f"models/{int(time.time())}/"
logdir = f"logs/{int(time.time())}/"
if not os.path.exists(models_dir):
    os.makedirs(models_dir)
if not os.path.exists(logdir):
    os.makedirs(logdir)

def simulate():
    for episode in range(MAX_EPISODES):
        model.learn(total_timesteps=MAX_TRY, tb_log_name='PPO')
        model.save(f"{models_dir}/{MAX_TRY+episode}")

    env.close()

if __name__ == "__main__":
    env = CustomEnv()
    # env = MaxAndSkipEnv(env, 4)

    MAX_EPISODES = 10
    MAX_TRY = 100000

    # https://www.youtube.com/watch?v=PxoG0A2QoFs&t=1394s
    # num_cpu = 2
    # env = VecMonitor(SubprocVecEnv([CustomEnv() for _ in range(num_cpu)]),"tmp/monitor")
    model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=logdir)


    simulate()