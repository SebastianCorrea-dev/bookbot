from stats import count_characters
from stats import print_count
import sys
def main():
    if len(sys.argv) == 1:
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        print_count(count_characters(file_path), file_path)
    
main()