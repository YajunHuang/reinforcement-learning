# Introdcution to Reinforcement Learning

### Review of key ideas
- RL is different from Supervised learning since no supervisor(reward), delayed feedback, sequential data(non i.i.d) and
agent's actions affect the subquent data it receives.
- The key components of RL are agent and evrionment which are communicating through action, reword, observation.
- RL is based on the reward hypothesis and doing sequential decision making,
which the goal of agent is to maximise total future reward by standing on Markov states and selecting actions.
This is a Markov Decision Process(MDP) or Partially Observable Markov Decision Process.
- Agents solve sequential decision making by holding one or more of policy, value function and model, so that agent can be categorized as value-based,
policy-based and actor-critic or model-free and model-based.
- Tow fundamental problems of sequential decision making are reinforcement learning and planning.
- RL can be used to solve prediction and control task.

### Terms
- Agent, Environment
- Reward, Action, Observation, State
- Sequential decision making
- MDP & POMDP
- Policy, Value function, Model
- Learning, Planning
- Explortation and Exploitation
- Prediction and Control

### Lectures & Readings

__Required:__

- [Reinforcement Learning: An Introduction](https://webdocs.cs.ualberta.ca/~sutton/book/bookdraft2016sep.pdf) - Chapter 1: The Reinforcement Learning Problem
- David Silver's RL Course Lecture 1 - Introduction to Reinforcement Learning ([video](https://www.youtube.com/watch?v=2pWv7GOvuf0), [slides](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/intro_RL.pdf))
- [OpenAI Gym Tutorial](https://gym.openai.com/docs)

__Optional:__

N/A


### Exercises

- [Work through the OpenAI Gym Tutorial](https://gym.openai.com/docs)