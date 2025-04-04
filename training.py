import random
import numpy as np
import pickle
import json


import nltk
from nltk.stem import WordNetLemmatizer


from tensor import Sequential
from tensor import Dense, Activation, Dropout


lemmatizer = WordNetLemmatizer()


with open('intents.json') as file:
    intents = json.load(file)


words = []
classes = []
documents = []
ignore_words = ['?', '!', '.', ',']


for intent in intents['intents']:
    for pattern in intent['patterns']:
        
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        
        documents.append((word_list, intent['tag']))
        
        if intent['tag'] not in classes:
            classes.append(intent['tag'])


words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))


classes = sorted(list(set(classes)))


print(f"Documents: {len(documents)}")
print(f"Classes: {len(classes)}")
print(f"Words: {len(words)}")


training = []
output_empty = [0] * len(classes)


for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    
    training.append([bag, output_row])


random.shuffle(training)
training = np.array(training)


train_x = list(training[:, 0])
train_y = list(training[:, 1])


model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)


model.save('chatbot_model.h5')


pickle.dump({'words': words, 'classes': classes, 'train_x': train_x, 'train_y': train_y}, open('training_data.pkl', 'wb'))