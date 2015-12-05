import sys


def main():
    promptsFilename = sys.argv[1]
    promptsFile = open(promptsFilename)
    promptsList = promptsFile.read().splitlines()
    promptsFile.close()

    for prompt in promptsList:
        promptWords = prompt.split()
        recordingFilename = promptWords[0]
        print 'waves/train/{0}.wav mfcc/train/{0}.mfc'\
            .format(recordingFilename)


if __name__ == '__main__':
    main()
