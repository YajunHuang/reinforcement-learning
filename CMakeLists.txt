cmake_minimum_required(VERSION 3.6)
project(reinforcement_learning)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        DavidSilverCourse/1_Intro/README.md
        DavidSilverCourse/2_MDP/README.md
        DavidSilverCourse/3_DP/__init__.py
        DavidSilverCourse/3_DP/policy_evaluation.ipynb
        DavidSilverCourse/3_DP/policy_evaluation.py
        DavidSilverCourse/3_DP/policy_evaluation_solution.ipynb
        DavidSilverCourse/3_DP/policy_iteration.ipynb
        DavidSilverCourse/3_DP/policy_iteration.py
        DavidSilverCourse/3_DP/policy_iteration_solution.ipynb
        DavidSilverCourse/3_DP/README.md
        DavidSilverCourse/3_DP/value_iteration.ipynb
        DavidSilverCourse/3_DP/value_iteration_solution.ipynb
        DavidSilverCourse/lib/envs/__init__.py
        DavidSilverCourse/lib/envs/gridworld.py
        DavidSilverCourse/lib/envs/mygridworld.py
        DavidSilverCourse/lib/__init__.py
        DavidSilverCourse/__init__.py
        DavidSilverCourse/README.md
        CMakeLists.txt
        README.md
        requirements)

add_executable(reinforcement_learning ${SOURCE_FILES})