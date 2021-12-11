import os
import threading
import argparse


def thread_job(book):
    with lock:
        with open(search_dir+'/'+book, 'r') as rf:
            for line in rf:
                if substring in line:
                    print(book+':', line)


parser = argparse.ArgumentParser(description='Search substring')
parser.add_argument('dir', nargs=1, type=str,
                    help='directory to search in')
parser.add_argument('words', nargs='+', type=str,
                    help='words of searched substring')
args = parser.parse_args()
search_dir = args.dir[0]
substring = ' '.join(args.words)

books = os.listdir(search_dir)
lock = threading.Lock()
threads = [threading.Thread(target=thread_job, args=(book, ))
           for book in books]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# C:\Users\Андрей\Desktop>python grep.py ./books not to
# Carroll Lewis. Alices adventures in Wonderland.txt: She said the last word with such sudden violence that Alice quite jumped; but she saw in another moment that it was addressed to the baby, and not to her, so she took courage, and went on again:-
#
# Carroll Lewis. Alices adventures in Wonderland.txt: Alice glanced rather anxiously at the cook, to see if she meant to take the hint; but the cook was busily stirring the soup, and seemed not to be listening, so she went on again: 'Twenty-four hours, I THINK; or is it twelve? I-'
#
# Carroll Lewis. Alices adventures in Wonderland.txt: 'You should learn not to make personal remarks,' Alice said with some severity; 'it's very rude.'
#
# Carroll Lewis. Alices adventures in Wonderland.txt: Alice was rather doubtful whether she ought not to lie down on her face like the three gardeners, but she could not remember every having heard of such a rule at processions; 'and besides, what would be the use of a procession,' thought she, 'if people had all to lie down upon their faces, so that they couldn't see it?' So she stood still where she was, and waited.
#
# Carroll Lewis. Alices adventures in Wonderland.txt: 'I quite agree with you,' said the Duchess; 'and the moral of that is-"Be what you would seem to be"-or if you'd like it put more simply-"Never imagine yourself not to be otherwise than what it might appear to others that what you were or might have been was not otherwise than what you had been would have appeared to them to be otherwise."'
#
# Milne Alan. Winnie the Pooh.txt: "It's like this," he said. "When you go after honey with a balloon, the great thing is not to let the bees know you're coming. Now, if you have a green balloon, they might think you were only part of the tree, and not notice you, and if you have a blue balloon, they might think you were only part of the sky, and not notice you, and the question is: Which is most likely?"
#
# Milne Alan. Winnie the Pooh.txt: "Both," and then, so as not to seem greedy, he added, "But don't bother about the bread, please." And for a long time after that he said nothing... until at last, humming to himself in a rather sticky voice, he got up, shook Rabbit lovingly by the paw, and said that he must be going on.
#
# Milne Alan. Winnie the Pooh.txt: "And I would go in after it," said Pooh excitedly, "only very carefully so as not to hurt myself, and I would get to the Jar of Honey, and I should lick round the edges first of all, pretending that there wasn't any more, you know, and then I should walk away and think about it a little, and then I should come back
#
# Milne Alan. Winnie the Pooh.txt: "Oh!" said Piglet, and tried not to look disappointed. But Pooh went into a corner of the room and said proudly to himself, "Impossible without Me! That
#
# Milne Alan. Winnie the Pooh.txt: 6. But Kanga would have to be looking the other way first, so as not to see
#
# Milne Alan. Winnie the Pooh.txt: "So as not to miss any of it," said Piglet.
#
# The Jungle Book.txt: "They fear me alone. They have good reason," said Kaa. "Chattering, foolish, vain вЂ“ vain, foolish, and chattering вЂ“ are the monkeys. But a man-thing in their hands is in no good luck. They grow tired of the nuts they pick, and throw them down. They carry a branch half a day, meaning to do great things with it, and then they snap it in two. That manling is not to be envied. They called me also вЂ“ 'yellow fish,' was it not?"
