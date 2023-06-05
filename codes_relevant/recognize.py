from guesslang import Guess

def recognize_programming_language(source_code):
    guess = Guess()
    language = guess.language_name(source_code)
    return language

if __name__ == '__main__':
    source_code = ' #include <stdio.h>\n  int main() {printf("Hello, World!");        return 0;    }'
    print(recognize(source_code))