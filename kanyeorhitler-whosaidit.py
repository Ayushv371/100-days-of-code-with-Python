import random

# Lists of quotes
kanye_quotes = [
    "I love Jewish people, but I also love Nazis.",
    "I just think that’s what they’re about, is making money - In reference to a jewish family",
    "Nothing in life is promised except death.",
    "If today I stand here as a revolutionary, it is as a revolutionary against the Revolution.",
    "I might have to go back to war. I just might have to",
    "...use you as an example to show the Jewish people that told you to call me that no one can threaten or influence me. I told you this is war.",
    "For 400 years? That sounds like a choice - In reference to slavery"
]

hitler_quotes = [
    "We are a people of different faiths, but we are one.",
    "Who says I am not under the special protection of God?",
    "When a man is starving in the streets, he’s not thinking about bread and water, but of caviar and champagne.",
    "...by defending myself against the Jew, I am fighting for the work of the Lord."
]

remaining_indices = [(0, i) for i in range(len(kanye_quotes))] + [(1, i) for i in range(len(hitler_quotes))]
random.shuffle(remaining_indices)

score = 0
total_questions = len(remaining_indices)

print("Welcome to 'Who Said It?' Quiz!")
print("You have to guess whether a quote is by Kanye West or Adolf Hitler.")
print("Type 'Kanye' or 'Hitler' to answer the questions.\n")

while remaining_indices:
    list_type, idx = remaining_indices.pop(0)

    if list_type == 0:
        quote = kanye_quotes[idx]
        correct_answer = "Kanye"
    else:
        quote = hitler_quotes[idx]
        correct_answer = "Hitler"

    print(f"Who said this? \n'{quote}'")
    user_answer = input("Your answer (Kanye/Hitler): ").strip().capitalize()

    if user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {correct_answer}.")

    print(f"Your current score is: {score}/{total_questions}\n")

print("Quiz Complete!")
print(f"Your final score is: {score}/{total_questions}")
