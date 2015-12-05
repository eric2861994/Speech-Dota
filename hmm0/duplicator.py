import sys


def main():
    # open file
    monophonesFilename = sys.argv[1]
    duplicateFilename = sys.argv[2]

    monophonesList, duplicateText = loadFile(
        monophonesFilename, duplicateFilename)

    for monophone in monophonesList:
        print '~h "%s"' % monophone
        for line in duplicateText:
            print '  %s' % line


def loadFile(monophonesFilename, duplicateFilename):
    # get monophones from file
    monophonesFile = open(monophonesFilename, 'r+')
    monophones = monophonesFile.read().splitlines()
    monophonesFile.close()

    # get duplicate text from file
    duplicateFile = open(duplicateFilename, 'r+')
    duplicateText = duplicateFile.read().splitlines()
    duplicateFile.close()

    return monophones, duplicateText


if __name__ == '__main__':
    main()
