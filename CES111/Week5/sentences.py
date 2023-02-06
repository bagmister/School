import random

# main requirments:
#     a.	single	past
#     b.	single	present
#     c.	single	future
#     d.	plural	past
#     e.	plural	present
#     f.	plural	future

def main():
    print()

def get_determiner(quantity):
    # """Return a randomly chosen determiner. A determiner is
    # a word like "the", "a", "one", "some", "many".
    # If quantity is 1, this function will return either "a",
    # "one", or "the". Otherwise this function will return
    # either "some", "many", or "the".

    # Parameter
    #     quantity: an integer.
    #         If quantity is 1, this function will return a
    #         determiner for a single noun. Otherwise this
    #         function will return a determiner for a plural
    #         noun.
    # Return: a randomly chosen determiner.
    # """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    #   """Return a randomly chosen noun.
    # If quantity is 1, this function will
    # return one of these ten single nouns:
    #     "bird", "boy", "car", "cat", "child",
    #     "dog", "girl", "man", "rabbit", "woman"
    # Otherwise, this function will return one of
    # these ten plural nouns:
    #     "birds", "boys", "cars", "cats", "children",
    #     "dogs", "girls", "men", "rabbits", "women"

    # Parameter
    #     quantity: an integer that determines if
    #         the returned noun is single or plural.
    # Return: a randomly chosen noun.
    # """
    if quantity == 1:    
        noun_list = [ "bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    else:
        noun_list = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
    noun_selected = random.choice(noun_list)
    return noun_selected

def get_verb(quantity, tense):
    # """Return a randomly chosen verb. If tense is "past",
    # this function will return one of these ten verbs:
    #     "drank", "ate", "grew", "laughed", "thought",
    #     "ran", "slept", "talked", "walked", "wrote"
    # If tense is "present" and quantity is 1, this
    # function will return one of these ten verbs:
    #     "drinks", "eats", "grows", "laughs", "thinks",
    #     "runs", "sleeps", "talks", "walks", "writes"
    # If tense is "present" and quantity is NOT 1,
    # this function will return one of these ten verbs:
    #     "drink", "eat", "grow", "laugh", "think",
    #     "run", "sleep", "talk", "walk", "write"
    # If tense is "future", this function will return one of
    # these ten verbs:
    #     "will drink", "will eat", "will grow", "will laugh",
    #     "will think", "will run", "will sleep", "will talk",
    #     "will walk", "will write"

    # Parameters
    #     quantity: an integer that determines if the
    #         returned verb is single or plural.
    #     tense: a string that determines the verb conjugation,
    #         either "past", "present" or "future".
    # Return: a randomly chosen verb.
    # """
    if quantity == 1:    
        if tense == "past":
            verb_list = [ "drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
        elif tense == "present":
            verb_list = [ "drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
        elif tense == "future":
            verb_list = [ "will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    else:
        if tense == "past":
            verb_list = [ "drank", "eats", "grew", "laughed", "thoughts","ran", "slept", "talked", "walked", "wrote"]
        elif tense == "present":
            verb_list = [ "drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
        elif tense == "future":
            verb_list = [ "will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    verb_selected = random.choice(verb_list)
    return verb_selected

    main()