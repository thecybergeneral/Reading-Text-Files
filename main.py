# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content():
    # [assignment] Add your code here
    with open("story.txt") as f:
        for line in f:
          #  print(line)
            #text = line.split()

            return line


print(read_file_content())


def count_words():
    # [assignment] Add your code here

    with open("story.txt") as f:
        for line in f:
            text = line.split()
            counts = dict()
            for x in text:
                if x in counts:
                    counts[x] += 1
                else:
                    counts[x] = 1
    return counts


print(count_words())
