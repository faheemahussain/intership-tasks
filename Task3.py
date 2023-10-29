import random
import time

def generate_random_text():
    # Define a list of sample texts for typing practice.
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Simplicity is the ultimate sophistication.",
        "Practice makes perfect.",
        "Type to learn, learn to type.",
    ]
    return random.choice(texts)

def calculate_wpm(input_text, elapsed_time):
    words = input_text.split()
    num_words = len(words)
    time_in_minutes = elapsed_time / 60
    wpm = num_words / time_in_minutes
    return round(wpm, 2)

def typing_speed_test():
    text_to_type = generate_random_text()
    print("Type the following text:")
    print(text_to_type)

    input_text = input("Start typing: ")
    start_time = time.time()

    if input_text == text_to_type:
        end_time = time.time()
        elapsed_time = end_time - start_time
        wpm = calculate_wpm(text_to_type, elapsed_time)
        print(f"Your typing speed: {wpm} WPM")
    else:
        print("Text doesn't match. Try again.")

if __name__ == "__main__":
    typing_speed_test()
