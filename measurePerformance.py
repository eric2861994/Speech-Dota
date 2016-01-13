import sys


class LineType(object):
    PATTERN = 1
    WORD = 2


class Transcript(object):
    def __init__(self):
        self.pattern = ""
        self.words = []

    def setPattern(self, pattern):
        self.pattern = pattern

    def addWord(self, word):
        self.words.append(word)

    def cleanWords(self):
        self.words = self.words[1:-1]


def main():
    # input from arguments
    recognisedFilename = sys.argv[1]
    promptsFilename = sys.argv[2]

    transcriptList = loadTranscript(recognisedFilename)
    for transcript in transcriptList:
        printTranscript(transcript)


def loadTranscript(recognisedFilename):
    # load transcript data
    recognisedFile = open(recognisedFilename, 'r+')
    recognisedData = recognisedFile.read()
    recognisedFile.close()

    lines = recognisedData.splitlines()

    transcriptList = []

    transcript = Transcript()
    lineType = LineType.PATTERN
    idx = 1  # ignore first line because it's useless
    while idx < len(lines):
        if lineType == LineType.PATTERN:
            pattern = lines[idx]
            transcript.setPattern(pattern)

            lineType = LineType.WORD

        elif lineType == LineType.WORD:
            if lines[idx] != '.':
                word = lines[idx].split()[2]
                transcript.addWord(word)

            else:
                transcript.cleanWords()
                transcriptList.append(transcript)
                transcript = Transcript()

                lineType = LineType.PATTERN

        idx += 1

    return transcriptList


def printTranscript(transcript):
    print transcript.pattern
    for word in transcript.words:
        print word


if __name__ == '__main__':
    main()
