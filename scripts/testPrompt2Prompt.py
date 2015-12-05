import sys


PROMPT_FORMAT = 'S%04d'


def main():
    promptsFilename = sys.argv[1]
    promptsFile = open(promptsFilename)
    promptsList = promptsFile.read().splitlines()
    promptsFile.close()

    start = 751
    for prompt in promptsList:
        promptWords = prompt.split()
        print (PROMPT_FORMAT % start), " ".join(promptWords[2:-1])

        start += 1


if __name__ == '__main__':
    main()
