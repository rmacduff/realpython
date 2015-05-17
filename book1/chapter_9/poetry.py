import random

nouns = ['fossil', 'horse', 'aardvark', 'judge', 'chef', 'mango', 'extrovert', 'gorilla']
verbs = ['kicks', 'jingles', 'bounces', 'slurps', 'meows', 'explodes', 'curdles']
adjectives = ['furry', 'balding', 'incredulous', 'fragrant', 'exuberant', 'glistening']
prepositions = ['against', 'after', 'into', 'beneath', 'upon', 'for', 'in', 'like', 'over', 'within']
adverbs = ['curiously', 'extravagantly', 'tantalizingly', 'furiously', 'sensuously']
words = [nouns, verbs, adjectives, prepositions, adverbs]

def choose_rand_words(words, qty):
    rand_words = []
    while len(rand_words) < qty:
        word = random.choice(words) 
        if word not in rand_words:
            rand_words.append(word)
    return rand_words

def make_poem(words):
    nouns = choose_rand_words(words[0], 3)
    verbs = choose_rand_words(words[1], 3)
    adjectives = choose_rand_words(words[2], 3)
    prepositions = choose_rand_words(words[3], 2)
    adverbs = choose_rand_words(words[4], 1)
    
    if adjectives[0][0] in ['a', 'e', 'i', 'o', 'u']:
        article_a = 'An'
    else:
        article_a = 'A'

    print "{} {} {}".format(article_a, \
                           adjectives[0], \
                           nouns[0]
                          )
    print ""
    print "{} {} {} {} {} the {} {}".format(article_a, \
                                             adjectives[0], \
                                             nouns[0], \
                                             verbs[0], \
                                             prepositions[0], \
                                             adjectives[1], \
                                             nouns[1]
                                            )
    print "{}, the {} {}".format(adverbs[0], \
                                 nouns[0], \
                                 verbs[1]
                                )
    print "the {} {} {} a {} {}".format(nouns[1], \
                                        verbs[2], \
                                        prepositions[1], \
                                        adjectives[2], \
                                        nouns[2]
                                       )

if __name__ == '__main__':
    make_poem(words)
