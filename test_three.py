"""
Analysis of the code below. After your understanding, try to remove the if's clauses without changing their behavior.
"""


def greetings(greeting: str):
    print(greeting)


def say_to(period: str):
    speech: str = ""

    match period:
        case 'M':
            speech = "Morning, have a great day!"
        case 'A':
            speech = "Good Afternoon, see you later!"
        case 'E':
            speech = "Good Evening, how was your day?"
        case 'N':
            speech = "Night, sleep well!"

    # if period == "M":
    #     speech = "Morning, have a great day!"
    # if period == "A":
    #     speech = "Good Afternoon, see you later!"
    # if period == "E":
    #     speech = "Good Evening, how was your day?"
    # if period == "N":
    #     speech = "Night, sleep well!"

    greetings(speech)


if __name__ == "__main__":

    periods = ["M", "A", "E", "N"]
    for g in periods:
        say_to(g)