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
def main():
    student1 = Student("John", 5)
    student2 = Student("Joey", 5)
    student3 = Student("Mike", 5)

    # Set scores for student1
    student1.set_score(0, 85)
    student1.set_score(1, 90)
    student1.set_score(2, 92)
    student1.set_score(3, 88)
    student1.set_score(4, 95)

    # Set scores for student2
    student2.set_score(0, 80)
    student2.set_score(1, 82)
    student2.set_score(2, 78)
    student2.set_score(3, 85)
    student2.set_score(4, 90)

    # Equality Test
    print("Equality Test:")
    print("student1 == student2:", student1 == student2)
    print("student1 == student3:", student1 == student3)

    # Less Than Test
    print("\nLess Than Test:")
    print("student1 < student2:", student1 < student2)
    print("student2 < student3:", student2 < student3)

    # Print student info
    print("\nStudent Info:")
    print(student1)
    print(student2)

    # Get average and high score
    print("\nAverage and High Score:")
    print("student1 average:", student1.get_average())
    print("student1 high score:", student1.get_high_score())
    print("student2 average:", student2.get_average())
    print("student2 high score:", student2.get_high_score())


if name == "main":
    main()
