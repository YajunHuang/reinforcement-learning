"""
run commands:
    cd /path/to/reinforcement-learning
    python -m DavidSilverCourse.lec3_DP.my_implement.policy_iteration
"""

import numpy as np

from DavidSilverCourse.lec3_DP.my_implement.policy_evaluation import policy_eval
from DavidSilverCourse.lib.envs.mygridworld import GridWorldEnv

env = GridWorldEnv()
P = env.P


def get_policy(V, env):
    """
    Obtain the policy based on value functions of states
    :param V: state-value functions of states.
    :param env: The OpenAI gym environment.
    :return: the stochastic policy
    """
    policy = np.zeros(shape=(env.nS, env.nA))

    for state in range(env.nS):
        if V[state] == 0:
            continue
        next_states = np.zeros(shape=(env.nA,), dtype=np.int) - 1
        next_state_vs = np.zeros(shape=(env.nA,)) - np.inf
        for action in range(env.nA):
            for trans_prob, next_state, reward, done in P[state][action]:
                next_states[action] = next_state
                next_state_vs[action] = V[next_state]
        max_next_v = np.amax(next_state_vs)

        greedy_actions = np.argwhere(np.around(next_state_vs, decimals=2) == np.around(max_next_v, decimals=2)).flatten()
        # print state, max_next_v, greedy_actions, greedy_actions, policy[state][greedy_actions], next_states, next_state_vs
        policy[state][greedy_actions] = 1.0 / greedy_actions.shape[0]
        # print state, policy[state]
    return policy


def policy_improvement(env):
    """
    Policy Improvement Algorithm. Iteratively evaluates and improves a policy
    until an optimal policy is found.
    :param env: state-value functions of states.
    :return: A tuple (policy, V).
        policy is the optimal policy, a matrix of shape [S, A] where each state s
        contains a valid probability distribution over actions.
        V is the value function for the optimal policy.
    """
    policy = np.ones(shape=(env.nS, env.nA)) / env.nA
    V = policy_eval(policy, env)

    while True:
        greedy_policy = get_policy(V, env)
        print greedy_policy
        if np.array_equal(policy, greedy_policy):
            return policy, V
        else:
            V = policy_eval(greedy_policy, env)
            # V = next_V
            policy = greedy_policy

    # print policy


def main():
    policy, v = policy_improvement(env)
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
