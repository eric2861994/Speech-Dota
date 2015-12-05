import sys


def main():
    startNumber = int(sys.argv[2])

    # load prompts
    promptsFilename = sys.argv[1]
    promptsFile = open(promptsFilename)
    promptsList = promptsFile.read().splitlines()
    promptsFile.close()

    currentNumber = startNumber
    for prompt in promptsList:
        promptWords = prompt.split()
        print 'S%04d' % currentNumber, ' '.join(promptWords[1:])

        currentNumber += 1


if __name__ == '__main__':
    main()
