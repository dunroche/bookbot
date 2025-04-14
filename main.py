from stats import word_count
from stats import char_count
from stats import sort_data
import sys

if len(sys.argv) < 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)
book_path = sys.argv[1]

file_path =  book_path # "books/frankenstein.txt"
def get_book_text(file_path):
    with open(file_path, "r") as file:
        return file.read()




  

def main():
  get_book_text(book_path) # "books/frankenstein.txt"
  total_words = word_count(book_path) # "books/frankenstein.txt"
  print("\n")
  print("============== BOOKBOT ============\n")
  print(f"Analyzing book found at \"{file_path}\"...\n")
  print("------------ Word Count ------------\n")
  print(f"Found {total_words} total words\n")
  print("-------------Character Count -------------\n")

  sort_data(char_count(book_path)) # "books/frankenstein.txt"

  
  print("================== END ==================")
  
main()
