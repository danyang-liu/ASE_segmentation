import os
import shutil
import nltk

def get_n_topwords(dir_path, n):
    words_frequences = {}
    n = int(n)
    if os.path.isfile(dir_path):
        filename = dir_path
        filepath = filename
        if os.path.isfile(filepath):
            infile = open(filepath,'r')
            pattern = r"""(?x)                   # set flag to allow verbose regexps
                (?:[A-Z]\.)+           # abbreviations, e.g. U.S.A.
                |\d+(?:\.\d+)?%?       # numbers, incl. currency and percentages
                |\w+(?:[-']\w+)*       # words w/ optional internal hyphens/apostrophe
                |\.\.\.                # ellipsis
                """
            try:
                for line in infile:
                    line_words = nltk.regexp_tokenize(line,pattern)
                    for word in line_words:
                        if word in words_frequences:
                            words_frequences[word] = words_frequences[word] + 1
                        else:
                            words_frequences[word] = 1
            except:
                pass
    else:
        filenames = os.listdir(dir_path)
        for filename in filenames:
            filepath = dir_path+'/'+filename
            if os.path.isfile(filepath):
                infile = open(filepath,'r')
                pattern = r"""(?x)                   # set flag to allow verbose regexps
                    (?:[A-Z]\.)+           # abbreviations, e.g. U.S.A.
                    |\d+(?:\.\d+)?%?       # numbers, incl. currency and percentages
                    |\w+(?:[-']\w+)*       # words w/ optional internal hyphens/apostrophe
                    |\.\.\.                # ellipsis
                    """
                try:
                    for line in infile:
                        line_words = nltk.regexp_tokenize(line,pattern)
                        for word in line_words:
                            if word in words_frequences:
                                words_frequences[word] = words_frequences[word] + 1
                            else:
                                words_frequences[word] = 1
                except:
                    pass
            else:
                dir_path_2 = filepath
                filenames_2 = os.listdir(dir_path_2)
                for filename in filenames_2:
                    filepath = dir_path_2+'/'+filename
                    infile = open(filepath,'r')
                    pattern = r"""(?x)                   # set flag to allow verbose regexps
                        (?:[A-Z]\.)+           # abbreviations, e.g. U.S.A.
                        |\d+(?:\.\d+)?%?       # numbers, incl. currency and percentages
                        |\w+(?:[-']\w+)*       # words w/ optional internal hyphens/apostrophe
                        |\.\.\.                # ellipsis
                        """
                    try:
                        for line in infile:
                            line_words = nltk.regexp_tokenize(line,pattern)
                            for word in line_words:
                                if word in words_frequences:
                                    words_frequences[word] = words_frequences[word] + 1
                                else:
                                    words_frequences[word] = 1
                    except:
                        pass
    sortedwords = sorted(words_frequences.items(), key=lambda d: d[1], reverse=True)
    i=0
    while i < n:
        print(sortedwords[i][0],' ',sortedwords[i][1])
        i = i + 1



if __name__ == '__main__':
    dir = input('Root:')
#    dir='../novel/AB/AC.TheMysteriousAffairatStyles.txt'
    n = input('N:')
    get_n_topwords(dir, n)
    print('finish!')