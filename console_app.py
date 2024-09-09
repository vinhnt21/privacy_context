from rag.generate_answer import get_answer

if __name__ == '__main__':
    while True:
        print("=" * 50)
        question = input("Enter your question: ")
        if question == "exit":
            break
        answer = get_answer(question)
        print("=" * 20)
        print("Answer:", answer)
