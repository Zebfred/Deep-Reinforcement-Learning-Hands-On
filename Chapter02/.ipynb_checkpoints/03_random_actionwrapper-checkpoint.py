#import gym
import gymnasium as gym
import random


class RandomActionWrapper(gym.ActionWrapper):
    def __init__(self, env, epsilon=0.9):
        super(RandomActionWrapper, self).__init__(env)
        self.epsilon = epsilon

    def action(self, action):
        if random.random() < self.epsilon:
            print("Random!")
            return self.env.action_space.sample()
        return action


if __name__ == "__main__":
    env = RandomActionWrapper(gym.make("CartPole-v1"))

    obs = env.reset()
    total_reward = 0.0

    while True:
        obs, reward, terminated, truncated, info = env.step(0)
        total_reward += reward
        if terminated:
            break

    print("Reward got: %.2f" % total_reward)
