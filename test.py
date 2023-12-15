text = 'Zoos können gut für die Bildung sein, weil Menschen dort Tiere sehen können, die sie sonst nie sehen würden. Manche sagen, Zoos helfen beim Schutz von Tieren, die in der Wildnis bedroht sind. Aber Tiere in Zoos leben nicht in ihrer natürlichen Umgebung und das kann für sie stressig sein. Es ist wichtig, dass Zoos gute Bedingungen für die Tiere haben. Die Frage, ob Zoos moralisch vertretbar sind, hängt davon ab, wie sie die Tiere behandeln.'
# i want to know how many words is in the text

# 1. split the text into words
words = text.split(' ')
# 2. count the words
number_of_words = len(words)
# 3. print the result
print(number_of_words)