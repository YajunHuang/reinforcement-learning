# encoding=utf8
"""
    created by Yajun Huang on 23/02/2017

run commands:
    cd /path/to/reinforcement-learning
    python -m DavidSilverCourse.lec3_DP.my_implement.value_iteration
"""

import numpy as np
from DavidSilverCourse.lib.envs.mygridworld import GridWorldEnv
from DavidSilverCourse.lec3_DP.my_implement.policy_iteration import get_policy


env = GridWorldEnv()


def value_iteration(env, theta=0.0001, discount_factor=1.0):
    """
    Value Iteration Algorithm.

    Args:
        env: OpenAI environment. env.P represents the transition probabilities of the environment.
        theta: Stopping threshold. If the value of all states changes less than theta
            in one iteration we are done.
        discount_factor: lambda time discount factor.

    Returns:
        A tuple (policy, V) of the optimal policy and the optimal value function.
    """
    V = np.zeros(shape=(env.nS, ))

    while True:
        delta = 0
        for state in range(env.nS):
            max_q = - np.inf
            opt_a = 0
            for action in range(env.nA):
                q = 0
                for trans_prob, next_state, reward, done in env.P[state][action]:
                    # print trans_prob, next_state, reward, done
                    q += trans_prob * (reward + discount_factor * V[next_state])
                if q > max_q:
                    max_q = q
                    opt_a = action
            delta = max(delta, np.abs(V[state] - max_q))
            V[state] = max_q
        if delta < theta:
            break
    policy = get_policy(V, env)
    return policy, V


def main():
    policy, v = value_iteration(env)

    print("Policy Probability Distribution:")
    print(policy)
    print("")

    print("Reshaped Grid Policy (0=up, 1=right, 2=down, 3=left):")
    print(np.reshape(np.argmax(policy, axis=1), env.shape))
    print("")

    print("Value Function:")
    print(v)
    print("")

    print("Reshaped Grid Value Function:")
    print(v.reshape(env.shape))
    print("")


if __name__ == '__main__':
    main()