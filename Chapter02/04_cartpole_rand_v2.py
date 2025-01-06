#import gym
#from gym.wrappers.monitoring.video_recorder import VideoRecorder

import gymnasium as gym


if __name__ == "__main__":
    env = gym.make("CartPole-v1", render_mode="human")
    #env = gym.wrappers.Monitor(env, "recording")

    total_reward = 0.0
    total_steps = 0
    obs, info = env.reset(seed=56)

    while True:
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        total_steps += 1
        if terminated:
            break

    print("Episode done in %d steps, total reward %.2f" % (total_steps, total_reward))
    env.close()
    env.env.close()
