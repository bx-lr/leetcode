import numpy as np
import random


class MultiArmedBandit:
    def __init__(self, num_questions):
        self.num_questions = num_questions
        # estimated success rates for each question
        self.estimated_success_rates = np.zeros(num_questions)
        # Number of times each arm has been pulled
        self.action_counts = np.zeros(num_questions)
        # Exploration weight (higher values prioritize exploration)
        self.exploration_weight = 1.0
        # Number of times each question has been asked
        self.question_attempts = np.zeros(num_questions)
        self.total_successes = []

    def choose_question(self):
        # Calculate exploration bonuses based on failure count
        exploration_bonus = self.exploration_weight / (self.action_counts + 1)
        # Calculate the UCB scores
        # (estimated success rates + exploration bonuses)
        ucb_scores = self.estimated_success_rates + exploration_bonus
        # Choose the question with the lowest UCB score
        print('exploration_bonus', exploration_bonus)
        print('estimated_success_rates', self.estimated_success_rates)
        print('ucb_scores', ucb_scores)
        # randomly prioritize exploration or re-asking the worst question
        decision = random.randint(0, 1)
        if decision:
            chosen_question = np.argmax(ucb_scores)
            print('using argmax')
        else:
            print('using argmin')
            chosen_question = np.argmin(ucb_scores)
        #chosen_question = if random.randint(0,1): np.argmax(ucb_scores) else: np.argmin(ucb_scores)
        print('argmin: ', np.argmax(ucb_scores))
        print('chosen_question:', chosen_question)
        return chosen_question

    def update(self, question, success):
        # Update action counts
        self.action_counts[question] += 1
        # Update estimated success rate for the chosen question
        # (sample average)
        update_value = (success
                        - self.estimated_success_rates[question]
                        ) / self.action_counts[question]
        print('update_value:', update_value)
        self.estimated_success_rates[question] += (
            success - self.estimated_success_rates[question]
            ) / self.action_counts[question]
        print('estimated_success_rates:', self.estimated_success_rates)
        return

if __name__ == '__main__':
    # Number of questions
    num_questions = 10

    # Initialize the bandit for prioritizing failed questions
    bandit = MultiArmedBandit(num_questions)

    # Lists to store rewards and question selections over time
    # True success rates (unknown)
    question_success = np.random.rand(num_questions)
    # Number of times each question has been asked
    question_attempts = np.zeros(num_questions)
    total_successes = []
    # Number of steps
    bandit.num_steps = 1000

    # Run the bandit for a fixed number of time steps
    for step in range(bandit.num_steps):
        # Choose a question based on the UCB policy with exploration bonuses
        chosen_question = bandit.choose_question()
        # Simulate success (1) or failure (0) for the chosen question
        success = np.random.rand() < question_success[chosen_question]
        # Update the bandit with the chosen question and success/failure
        bandit.update(chosen_question, success)
        # Track total successes for each question
        question_attempts[chosen_question] += 1
        total_successes.append(success)

        # Print the results
        print("Success Rates:", bandit.estimated_success_rates)
        print("Question Selection Counts:", bandit.action_counts)
