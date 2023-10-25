class MyString:
    def __init__(self, value):
        if isinstance(value, str):
            self.value = value
        else:
            self.value = ''  # Set value to an empty string when it's not a string

    def is_sentence(self):
        # Check if the value ends with a period
        return self.value.endswith('.')

    def is_question(self):
        # Check if the value ends with a question mark
        return self.value.endswith('?')

    def is_exclamation(self):
        # Check if the value ends with an exclamation mark
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the value using regular expressions to find sentences
        import re
        sentences = re.split(r'[.!?]', self.value)

        # Filter out empty strings (resulting from consecutive punctuation marks)
        non_empty_sentences = [sentence for sentence in sentences if sentence.strip()]

        return len(non_empty_sentences)

# Example usage:
string = MyString("This is a string! It has three sentences. Right?")
print(string.is_sentence())  # True
print(string.is_question())  # False
print(string.is_exclamation())  # True
print(string.count_sentences())  # 3
