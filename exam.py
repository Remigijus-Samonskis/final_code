import logging
from art import art


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.info("Lets play")
class GuessGame:
    def __init__(self, questions: dict, options: list) -> None:
        self.questions = questions
        self.options = options
        self.guesses: list = []
        self.correct_guesses = 0
        self.question_num = 1
    def play_game(self) -> None:
        for item in self.questions:
            print("-------------------------")
            print(item)
            for i in self.options[self.question_num -1]:
                print(i)
            while True:
                try:
                    guess = input("Enter (A, B, or C): ").upper()
                    if guess not in ["A", "B", "C"]:
                        print("-------------------------")
                        raise TypeError("Wrong input. Please enter A, B, or C")
                    break
                except Exception as e:
                    print(e)
            self.guesses.append(guess)
            self.correct_guesses += self.check_answer(self.questions[item], guess)
            self.question_num  +=1
        self.display_score()
    def check_answer(self, answer: str, guess: str) -> int:
        if answer == guess:
            print("CORRECT!")
            return 1
        else:
            print("WRONG!")
            return 0
    def display_score(self) -> None:
        print("-------------------------")
        print("RESULTS")
        print("-------------------------")

        print("Answers: ", end="")
        for i in self.questions:
            print(self.questions[i], end=" ")
        print()

        print("Guesses: ", end="")
        for i in self.guesses:
            print(i, end=" ")
        print()

        score = int((self.correct_guesses / len(self.questions)) * 100)
        print("Your score is: " + str(score) + "%")
    def play_again(self) -> bool:
        response = input("Do you want to play again? (yes or no): ").upper()
      
        if response == "YES":
            self.guesses = []
            self.correct_guesses = 0
            self.question_num = 1
            return True
        else:
            return False
        
questions = {
    "Who many planets have solar system?: ": "A",
    "Is the Earth round: ": "C",
    "Hwo is the Sun?: ": "B",
    "What is Earth satallite?: ": "C"
}

options = [["A. 8 planets", "B. 6 planets", "C. just Mars and Earth"],
           ["A. sometimes", "B. false", "C. true"],
           ["A. planet", "B. star", "C. asteroid"],
           ["A. Mars", "B. international space station", "C. Moon"]]

quiz = GuessGame(questions, options)
quiz.play_game()

while quiz.play_again():
    quiz.play_game()
print("See Ya later!")
art_1 = art("happy")
print(art_1)
	
