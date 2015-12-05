import sys


def main():
    promptsFilename = sys.argv[1]
    promptsFile = open(promptsFilename)
    promptsList = promptsFile.read().splitlines()
    promptsFile.close()

    print '#!MLF!#'
    for prompt in promptsList:
        promptWords = prompt.split()
        recordingFilename = promptWords[0]
        print '"*/%s.lab"' % recordingFilename
        for word in promptWords[1:]:
            print word

        print '.'


if __name__ == '__main__':
    main()
