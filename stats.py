

def word_count(text):
    with open(text) as t:
        text = t.read()
        count = 0
        words = text.split()  # Split by whitespace
        for word in words:
            count += 1
        return count

    


def char_count(text):
    with open(text) as t:
        text = t.read()
        counts = {}
        for char in text:
            lower_char = char.lower()
            if lower_char not in counts:
                counts[lower_char] = 1
            else:
                counts[lower_char] += 1
        return counts



        
def sort_data(char_result): 
    sorted_char_list = sorted(char_result.items(), key=lambda item: item[1], reverse=True)
    for k, v in sorted_char_list:
        if k.isalpha():
            print(f"{k}: {v}\n")
    return sorted_char_list      





