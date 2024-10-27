import random


PRONOUNS = ["I", "You", "He", "She", "It", "We", "They"]
NAMES = [
    "Todd", "Jane", "John", "Alice", "Bob", "Eve", "Charlie", "Carol", "David",
    "Frank", "Grace", "Hank", "Ivy", "Jack", "Kara", "Liam", "Mona", "Nate",
    "Olivia", "Paul", "Quinn", "Rachel", "Sam", "Tina", "Uma", "Victor",
    "Wendy", "Xander", "Yara", "Zane"
]

TWO_NAMES = [f"{random.choice(NAMES)} and {random.choice(NAMES)}" for _ in range(10)]

PRESENT_SIMPLE_PLUS_S = [
    "run/runs", "jump/jumps", "swim/swims", "write/writes", "read/reads", "sing/sings", "dance/dances", "play/plays",
    "talk/talks", "walk/walks", "drive/drives", "eat/eats", "drink/drinks", "sleep/sleeps", "work/works", "cook/cooks", "clean/cleans"
]

PRESENT_SIMPLE_PLUS_ES = [
    "brush/brushes", "fix/fixes", "watch/watches", "mix/mixes", "kiss/kisses", "pass/passes", "push/pushes", "catch/catches",
    "finish/finishes", "miss/misses", "wish/wishes", "buzz/buzzes", "box/boxes", "match/matches", "wash/washes", "tax/taxes"
]

PRESENT_SIMPLE_PLUS_IES = [
    "study/studies", "try/tries", "fly/flies", "cry/cries", "spy/spies", "apply/applies", "reply/replies", "deny/denies",
    "carry/carries", "hurry/hurries", "marry/marries", "copy/copies", "fry/fries", "multiply/multiplies", "qualify/qualifies",
    "satisfy/satisfies", "vary/varies", "identify/identifies", "magnify/magnifies", "notify/notifies", "occupy/occupies"
]