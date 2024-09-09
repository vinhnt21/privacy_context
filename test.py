import spacy


context = '''
Daniel Lee donated $100 to Charity Organization on 2023-1 1-08.
Sophia Kim received a salary payment of $4,000 from Employer Corp on 2023-12-01.
David Kim invested $5,000 in a mutual fund managed by W ealth Management Group on 2023-07-12.
Emily Chen paid her monthly rent of $1,500 to Landlord Properties on 2023-08-01.
Sarah Lee purchased a new laptop for $1,200 using her credit card on 2023-05-20.
Global Exports Inc received a payment of €50,000 from Euro Importers Ltd on 2023-06-30.
Michael Rodriguez sold 100 shares of T echCo stock for $20 per share on 2023-09-18.
Olivia Davis bought a new car for $30,000 from Car Dealership Inc on 2023-10-25.
'''

question = "How much did Sophia Kim received?"

# Load a pre-trained NER model (e.g., en_core_web_sm)
nlp = spacy.load('en_core_web_sm')

# Process a text
text = context + question
doc = nlp(text)
# Extract and print named entities
words_list = [(entity.text, entity.label_) for entity in doc.ents]
print(words_list)
