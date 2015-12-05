import os


ORIGINAL = "%d.wav"
RENAMED = "S%04d.wav"


def main():
    for counter in range(1, 201):
        original = ORIGINAL % counter
        renamed = RENAMED % (750 + counter)
        os.rename(original, renamed)


if __name__ == '__main__':
    main()
