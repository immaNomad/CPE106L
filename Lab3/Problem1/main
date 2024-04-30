class Student:
    def __init__(self, name, num_scores):
        # Initialize a student with name and number of scores.
        self.name = name
        self.scores = [0] * num_scores

    def get_name(self):
        # Return the student's name.
        return self.name

    def set_score(self, index, score):
        # Set the score at the given index, counting from 0.
        self.scores[index] = score

    def get_score(self, index):
        # Return the score at the given index, counting from 0.
        return self.scores[index]

    def get_average(self):
        # Return the average score.
        if len(self.scores) > 0:
            return sum(self.scores) / len(self.scores)
        return 0

    def get_high_score(self):
        # Return the highest score.
        if len(self.scores) > 0:
            return max(self.scores)
        return None

    def __str__(self):
        # Return the string representation of the student.
        scores_str = " ".join(str(score) for score in self.scores)
        return f"Name: {self.name}\nScores: {scores_str}"

    def __eq__(self, other):
        # Check if two students have the same name.
        if isinstance(other, Student):
            return self.name == other.name
        return False

    def __lt__(self, other):
        # Compare students based on their names.
        if isinstance(other, Student):
            return self.name < other.name
        return False
