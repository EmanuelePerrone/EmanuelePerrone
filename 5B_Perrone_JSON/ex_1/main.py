import json
import jsonschema
from jsonschema import validate

def load_schema():
    with open('book.schema.json', 'r') as schema_file:
        return json.load(schema_file)

def load_books():
    with open('books-text-data.json', 'r') as books_file:
        return json.load(books_file)

def validate_books(books, schema):
    for book in books:
        try:
            validate(instance=book, schema=schema)
            print(f"The book '{book['title']}' is valid.")
        except jsonschema.exceptions.ValidationError as e:
            print(f"Validation error in the book '{book['title']}': {e.message}")

def filter_books_by_language(books, language):
    return [book for book in books if book['language'] == language]

def main():
    schema = load_schema()
    books = load_books()

    validate_books(books, schema)

    language = 'it'  
    filtered_books = filter_books_by_language(books, language)
    
    print(f"\nBooks in {language.upper()} language:")
    for book in filtered_books:
        print(f"- {book['title']} by {', '.join(book['authors'])}")

if __name__ == "__main__":
    main()
