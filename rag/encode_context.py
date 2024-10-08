from langchain_core.prompts import ChatPromptTemplate
from rag.rag_services import *


def detect_words(context: str, question: str) -> str:
    system_prompt = '''
    Task: Find all words that contain detail information in the context and question 
    such as name, number, date, location, etc. Then return the list of these words and its type.
    Instructions:
    * Analyze the context & question.
    * Find all words that contain detail information.
    * Return the list of these words.
    
    Your answer is only the list of words without any additional information, and must be strictly in the format:
    [('word1', 'type1'), ('word2', 'type2'), ...]
    
    
    Sample Output:
    [('Mary', 'name'), ('Peter', 'name'), ('15,000', 'number'), ('EUR', 'currency'), ('HSBC', 'bank'), ('London', 'location'), ('ABC Company', 'company'), ('Switzerland', 'location'), ('July 15, 2023', 'date')]
    
    
    Context: {context}
    Question: {question}
    '''

    prompt = ChatPromptTemplate.from_template(system_prompt)

    chain = prompt | local_llm

    words_list_str = chain.invoke({'context': context, 'question': question}).content
    return words_list_str


def make_context_abstract(context, question, words_list):
    """

    :param context: is the context that the user wants to ask
    :param question: is the question that the user wants to ask
    :param words_list: [(word1, type1), (word2, type2), ...]
    :return:
        context and question with the sensitive information replaced by placeholders
        if type is name, replace by [name]
        if type is number, replace by [number]
        ...
        if more than name, replace by [name1], [name2], ...
        ...
    """
    context_abstract = context
    question_abstract = question

    # Replace the sensitive information with placeholders
    for i, (word, word_type) in enumerate(words_list):
        placeholder = f"[{word_type}{i + 1}]"  # Generate a unique placeholder for each word type
        context_abstract = context_abstract.replace(word, placeholder)
        question_abstract = question_abstract.replace(word, placeholder)

    return context_abstract, question_abstract


def get_words_list(context: str, question: str) -> list:
    doc = nlp(context + question)
    words_list = [(entity.text, entity.label_) for entity in doc.ents]
    return words_list


def send_to_cloud_model(encoded_context: str, encoded_question: str) -> str:
    system_prompt = '''
    Your task is answer the question based on the encoded context and question. You can use the provided encoded context 
    and question to generate the answer. Please make sure to respect the privacy of the data and not reveal any 
    sensitive information.
    
    Encode Context: {encoded_context}
    Encode Question: {encoded_question}
    
    Return: The answer to the question based on the encoded context and question.
    '''

    prompt = ChatPromptTemplate.from_template(system_prompt)

    chain = prompt | llm

    return chain.invoke({'encoded_context': encoded_context, 'encoded_question': encoded_question}).content


def decode_answer(abstract_answer, words_list):
    for i, (word, word_type) in enumerate(words_list):
        placeholder = f"[{word_type}{i + 1}]"
        abstract_answer = abstract_answer.replace(placeholder, word)
    return abstract_answer
