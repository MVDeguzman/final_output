import time
import sys

def transition_effect():
    # Simple transition effect using a dot

    sys.stdout.flush()
    time.sleep(0.3)  # Pause for 0.3 seconds between words

def display_lyrics_word_by_word():
    lyrics = [
        "At baby, ako'y mag-aabang",
        "At dadalhin ka sa nakaraan",
        "Sa nakaraan",
        "",
        "Malayo man ako sa 'yo, sinta",
        "Uwi ka na",
        "Kahit saan pang lugar, ipagdarasal",
        "Makita ka lang",
        "",
        "Oh, nasa'n ka ba, mahal?",
        "Hinahanap ka na ng puso ko",
        "",
        "Baby, ikaw lang talaga",
        "Ang nami-miss ko sa tuwi-tuwina",
        "Sa tuwi-tuwina"
    ]
    
    for line in lyrics:
        words = line.split()  # Split the line into words
        for word in words:
            sys.stdout.write(word + ' ')
            sys.stdout.flush()
            transition_effect()  # Show transition effect after each word
        print()  # Move to the next line after finishing the current one
        time.sleep(1)  # Pause before showing the next line

# Call the function to display the lyrics word by word with transitions
display_lyrics_word_by_word()