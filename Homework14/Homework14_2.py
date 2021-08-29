#Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
def stop_words(words: list):
    def search(func):
        def wrapper(arg):
             stopwords: str= func(arg)
             for word in words:
                stopwords = stopwords.replace(word, '*')

             return stopwords
        return wrapper
    return search


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
print(create_slogan("Steve"))
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
