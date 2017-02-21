# encoding=utf8

import numpy as np
import pprint
import sys
if "../" not in sys.path:
 sys.path.append("../")
from lib.envs.gridworld import GridWorldEnv

pp = pprint.PrettyPrinter(indent=2)
env = GridWorldEnv


def policy_eval(policy, env, discount_factor=1.0, theta=1e-5):
    """
    Evaluate a policy given an environment and a full description of the environment's dynamics.

    Args:
        policy: [S, A] shaped matrix representing the policy.
        env: OpenAI env. env.P represents the transition probabilities of the environment.
            env.P[s][a] is a (prob, next_state, reward, done) tuple.
        theta: We stop evaluation once our value function change is less than theta for all states.
        discount_factor: lambda discount factor.

    Returns:
        Vector of length env.nS representing the value function.
    """
    V = np.zeros(env.nS)
    while True:
        # TODO: Implement!
        break

    return np.array(V)

random_policy = np.ones([env.nS, env.nA]) / env.nA
v = policy_eval(random_policy, env)

print("Reshaped Grid Value Function:")
print(v.reshape(env.shape))
print("")

# Test: Make sure the evaluated policy is what we expected
expected_v = np.array([0, -14, -20, -22, -14, -18, -20, -20, -20, -20, -18, -14, -22, -20, -14, 0])
np.testing.assert_array_almost_equal(v, expected_v, decimal=2)

