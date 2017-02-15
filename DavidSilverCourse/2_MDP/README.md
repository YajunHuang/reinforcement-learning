# Markov Decision Process

### Review of key ideas

- MDPs are a tool for modeling sequential decision making which is the RL environment, where the environment state is fully observable. i.e. The current state completely characterises the process.

- A _policy \pi_ is a distribution over actions given state s. `\pi(a|s) = P{A_t=a | S_t=s}`. _(i)_ A policy fully defines the behaviour of an agent, _(ii)_ MDP policies depend on the current state (not the history), _(iii)_ policies are stationary (time-independent).

- The return `G_t` of MRP is the total discounted reward from time-step t. `G_t = \sum{k=0}{\inf} \gamma^k R_{t+k+1}`.

- The state-value function `v(s)` of an MDP is the expected return starting from state `s` and then following policy `\pi`. `v_{\pi}(s) = E_{\pi}[G_t | S_t=s]`.

- Bellman Equation makes the value function decomposed into two parts, immediate reward and discounted value of successor state. This points out that value function can be reduced from expectation of infinite time step reward to one step of its successor state value function.

- The optimal state-value function `v_*(s)` is the maximum value function over all policies. `v_*(s) = max_{pi} v_{\pi}(s)`.

- An MDP is 'solved' when we know the optimal value fn. The optimal value function specifies the best possible performance in the MDP.

- The Bellman Optimality Equation differs from Bellman Expectation Equation in value function definition. The optimal value function of a state is related to the optimal value of successor states. It has a __max__ instead of an __expectation__.

- Value functions define an ordering over policies. A policy `p1` is better than `p2` if `v_p1(s) >= v_p2(s)` for all states s. For MDPs, there exist one or more optimal policies that are better than or equal to all other policies.

- A Partially Observable Markov Decision Process is an MDP with hidden states.

### Terms
- MDP
- state/action value function
- policy
- optimal value function
- optimal policy
- Bellman Equation(for MRP)
- Bellman Expectation Equation v.s. Bellman Optimality Equation(for MDP)
- Infinite MDPs
- POMDPs, belief state, ergodic MDP



### Lectures & Readings

__Required:__

- [Reinforcement Learning: An Introduction](https://webdocs.cs.ualberta.ca/~sutton/book/bookdraft2016sep.pdf) - Chapter 3: Finite Markov Decision Processes
- David Silver's RL Course Lecture 2 - Markov Decision Processes ([video](https://www.youtube.com/watch?v=lfHX2hHRMVQ), [slides](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/MDP.pdf))
- [Szepesvari, Algorithms for Reinforcement Learning (Last update: May 18, 2013)](https://sites.ualberta.ca/~szepesva/papers/RLAlgsInMDPs.pdf) - Chapter 2: Markov Decision Processes

__Optional:__
- Introduction to Probability Models - Chapter 4: Markov Chains

### Excercises
