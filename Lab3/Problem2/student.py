import random

class Student:
    def __init__(self, name, num_scores):
        """Initializes a student with a name and a list of scores, all initially set to 0."""
        self.name = name
        self.scores = [0] * num_scores

    def get_name(self):
        """Returns the student's name."""
        return self.name

    def set_score(self, index, score):
        """Sets the score at the given index (0-based)."""
        self.scores[index] = score

    def get_score(self, index):
        """Returns the score at the given index (0-based)."""
        return self.scores[index]

    def get_average(self):
        """Returns the average of the student's scores."""
        return sum(self.scores) / len(self.scores)

    def get_high_score(self):
        """Returns the highest score of the student."""
        return max(self.scores)

    def __str__(self):
        """Returns a string representation of the student."""
        scores_str = " ".join(str(score) for score in self.scores)
        return f"Name: {self.name}\nScores: {scores_str}"

    def __eq__(self, other):
        """Returns True if two students have the same name."""
        return self.name == other.name

    def __lt__(self, other):
        """Returns True if the current student's name comes before the other student's name."""
        return self.name < other.name

    def __ge__(self, other):
        """Returns True if the current student's name comes after or is equal to the other student's name."""
        return self.name >= other.name

def main():
    students =
    [
        Student("Ken", 5),
        Student("John", 5),
        Student("Alice", 5),
        Student("Bob", 5),
        Student("Emma", 5)
    ]

    random.shuffle(students)
    students.sort()

    for student in students:
        print(student)
        print()

if _name_ == "_main_":
    main()
