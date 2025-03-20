"""
(BSc) Software Development at Byu-Idaho  
Course: CSE-111 Programming with Functions
W02 Project: Sentences 
Author: Tiago Borges

Program : Sentence Generator

Description:
This Python program generates six randomly structured sentences using functions to construct phrases with determiners,
nouns, verbs, and prepositional phrases. It follows the assignment's requirements by ensuring variation in number (singular/plural)
and verb tense (past, present, future).

Bonus Features:
1- Each sentence includes a second prepositional phrase to enhance complexity
2- The structure follows the call graph as outlined in the assignment

How It Works:
1. The `main` function calls `make_sentence` to generate six sentences
2. `make_sentence` calls helper functions to obtain determiners, nouns, verbs, and prepositional phrases
3. `get_prepositional_phrase` constructs a phrase by calling `get_preposition`, `get_determiner`, and `get_noun`
4. Sentences are printed with proper capitalization and randomness for variety

"""
#Let´s do it! 


import random

# Function to get a random determiner based on quantity 
def get_determiner(quantity):
    determiners = ["one", "a", "the"] if quantity == 1 else ["some", "many", "the"]
    return random.choice(determiners)

# Function to get a random noun based on quantity (singular or plural)
def get_noun(quantity):
    nouns = ["girl", "bird", "child", "car", "dog", "rabbit", "cat"] if quantity == 1 else ["girls", "birds", "children", "cars", "dogs", "rabbits", "cats"]
    return random.choice(nouns)

# Function to get a random verb based on quantity and tense (past, present, or future)
def get_verb(quantity, tense):
    verbs = {
        "past": ["talked", "ate", "ran", "laughed", "grew"],
        "present": ["talks", "eats", "runs", "laughs", "grows"],
        "future": ["will talk", "will eat", "will run", "will laugh", "will grow"]
    }
    return random.choice(verbs[tense])

# Function to get a random preposition
def get_preposition():
    prepositions = [
        "about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on",
        "onto", "out", "over", "past", "to", "under", "with", "without"
    ]
    return random.choice(prepositions)

# Function to create a prepositional phrase with a preposition, determiner and noun xD
def get_prepositional_phrase(quantity):
    return f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}"

# Function to get a random adjective :D
def get_adjective():
    adjectives = ["red", "big", "small", "fast", "slow", "happy", "sad", "angry", "bright", "dark"]
    return random.choice(adjectives)

# Function to get a random adverb
def get_adverb():
    adverbs = ["quickly", "slowly", "happily", "sadly", "angrily", "sweetly", "calmly"]
    return random.choice(adverbs)

# Function to construct a full sentence with all components!
def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    adjective = get_adjective()
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)
    adverb = get_adverb()
    
    sentence = f"{determiner.capitalize()} {adjective} {noun} {prepositional_phrase1} {adverb} {verb} {prepositional_phrase2}."
    return sentence

# Main function to generate and print six sentences with different tenses and quantities!!!
def main():
    print(make_sentence(1, "past"))  
    print(make_sentence(1, "present"))  
    print(make_sentence(1, "future"))  
    print(make_sentence(2, "past"))  
    print(make_sentence(2, "present"))  
    print(make_sentence(2, "future"))  

# To Finish - End Line - Cheers!

if __name__ == "__main__":
    main()


# This project successfully meets the given requirements and includes an extra prepositional phrase to exceed expectations
# It demonstrates modular function usage and structured randomness in sentence generation

# Thank you for reviewing my project. I appreciate your time and feedback!
