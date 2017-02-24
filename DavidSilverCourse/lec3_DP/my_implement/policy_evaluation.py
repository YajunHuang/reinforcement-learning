# encoding=utf8
"""
run commands:
    cd /path/to/reinforcement-learning
    python -m DavidSilverCourse.3_DP.policy_evaluation
"""
import numpy as np
import pprint
import sys
from DavidSilverCourse.lib.envs.mygridworld import GridWorldEnv

pp = pprint.PrettyPrinter(indent=2)
env = GridWorldEnv()


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
    next_V = np.zeros_like(V)       # using synchronous backups, so we need two value functions for old and new.
    # in MDP, we assume that transition probabilities, and reward functions are given.
    P = env.P
    # observation = env.reset()     # we do not need observation in MDP, as we have the env knowledge.
    # env.render()
    while True:
        # TODO: Implement!
        delta = 0
        # sweeping state-value functions for all states in a iteration.
        for state in range(env.nS):
            # According to the formula:
            # v_state = sum_{a in A} pi(a|s) * (P(s, a) + discount_factor * sum_{next_s in S}P(s, next_s, a)V(next_s))))
            # each state, perform the full back backup
            v_state = 0.0
            # For each state, look at the possible next actions
            for action, action_prob in enumerate(policy[state]):
                # print state, action, action_prob
                # For each action, look at each possible next transition state
                for trans_prob, next_state, reward, done in P[state][action]:    # done is useless as we update all states
                    # print state, action, action_prob, next_state, trans_prob, reward
                    v_state += action_prob * trans_prob * (reward + discount_factor * V[next_state])
            next_V[state] = v_state
            delta = max(delta, np.abs(v_state - V[state]))
        if delta < theta:
            break
        V = next_V.copy()
    return np.array(V)


def main():
    random_policy = np.ones([env.nS, env.nA]) / env.nA
    v = policy_eval(random_policy, env)

    print("Reshaped Grid Value Function:")
    print(v.reshape(env.shape))
    print("")

    # Test: Make sure the evaluated policy is what we expected
    expected_v = np.array([0, -14, -20, -22, -14, -18, -20, -20, -20, -20, -18, -14, -22, -20, -14, 0])
    np.testing.assert_array_almost_equal(v, expected_v, decimal=2)


if __name__ == '__main__':
    main()
