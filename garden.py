import spacy

nlp = spacy.load("en_core_web_sm")

garden_path_1 = "The man who hunts ducks out on weekends."
garden_path_2 = "I know the words to that song about the Queen don't rhyme."
garden_path_3 = "Helen is expecting tomorrow to be a bad day."
garden_path_4 = "After the young Londoner had visited his parents prepared to celebrate their anniversary."
garden_path_5 = "The cotton clothing is usually made of grows in Mississippi."

# store garden path sentences in a list.
garden_path_sentences = [garden_path_1, garden_path_2, garden_path_3, garden_path_4, garden_path_5]

# tokenize each garden path sentence.
for sentence in garden_path_sentences:
    doc = nlp(sentence)
    print(f"\nTokens:")
    for token in doc:
        print(token)

print("\nNamed Entity Recognition:")

# NER performed on each sentence.
for sentence in garden_path_sentences:
    doc = nlp(sentence)
    for ent in doc.ents:
        print(ent.text, ent.label_)

"""
'Helen' has been categorised as a GPE.
This entity type refers to geopolitical entities i.e. cities, states, countries. 
This was not expected as PERSON would be the expected entity for 'Helen' in this sentence.
However, Helen is also a city in Georgia, USA. 
This is likely the reason for this classification. 

'a bad day' has been categorised as a DATE.
This entity type refers to absolute and relative dates or periods. 
A bad day is an absolute period regardless of the adjective 'bad'. 
This entity type is expected and appropriate. 
"""
