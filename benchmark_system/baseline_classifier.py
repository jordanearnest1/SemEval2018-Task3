from nltk.tokenize import TweetTokenizer


# tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)

training_data = "SemEval2018-T3-train-taskA.txt"


def load_data():
    global training_data
    label_lst = []  ## a list of 1's and 0's
    corpus = []  ## a list of all the words
    word_label_dict = {} ## dict of word:label
    word_label_tuple_lst = [] ## dict of (word, label)
    with open(training_data, "rt", encoding ='utf-8') as data_in:
        for line in data_in:
            if not line.lower().startswith("tweet index"): # discard first line if it contains metadata
                line = line.rstrip() # remove trailing whitespace
                label = int(line.split("\t")[1])
                tweet = line.split("\t")[2]
                label_lst.append(label)
                corpus.append(tweet)
                word_label_dict[tweet]= label
                word_label_tuple_lst.append((tweet, label))

    return corpus, label_lst, word_label_dict, word_label_tuple_lst


def featurize(corpus):   ## doing it with the whole corpus
    tokenized_data = []
    tokenizer = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True).tokenize
    for line in corpus:
        tl = tokenizer(line)
        tokenized_data.append(tl)


#     return tokenized_data


def featurize(word_label_tuple_lst):   ## doing it with the whole corpus
    tokenized_data = []
    tokenized_data_with_class = []
    tokenizer = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True).tokenize
    for line in corpus:
        print(line)
        # tl = tokenizer(line)
        # tokenized_data.append(tl)
        # tokenized_data



#     return tokenized_data


##scikit learns needs a list of data and labels associated with each row



# def classifier(tokenized_data):
#     classifier = nltk.NaiveBayesClassifier.train(tokenized_data)



load = load_data()
print(type(load))

# feature = featurize(word_label_tuple_lst)

print(feature)
# f = featurize(load[0])

# for line in f:
#     print(line)





# for line in load[:10]:
#     print(line)
