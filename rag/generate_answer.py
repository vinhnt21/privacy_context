import ast

from rag.encode_context import *
from rag.index_docs import get_context


def get_answer(question: str) -> str:
    print("Question:", question)
    print("Getting context...")
    context = get_context(question)
    print("Context:", context)
    print("Encoding context and question...")
    word_list_str = detect_words(context, question)
    print("Words list:", word_list_str)
    words_list = ast.literal_eval(word_list_str)
    context_abstract, question_abstract = make_context_abstract(context, question, words_list)
    print("Encoded context:", context_abstract)
    print("Encoded question:", question_abstract)
    abstract_answer = send_to_cloud_model(context_abstract, question_abstract)
    print("Abstract answer:", abstract_answer)
    decoded_answer = decode_answer(abstract_answer, words_list)
    print("Decoded answer:", decoded_answer)
    return decoded_answer
