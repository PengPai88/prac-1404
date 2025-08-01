import warnings
from bs4 import GuessedAtParserWarning

warnings.filterwarnings("ignore", category=GuessedAtParserWarning)

import wikipedia

def main():
    while True:
        title = input("Enter page title: ").strip()
        if not title:
            print("Thank you.")
            break

        try:
            # 禁用autosuggest确保用用户输入的标题搜索
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
            print()
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
            print()
        except wikipedia.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
            print()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print()

if __name__ == "__main__":
    main()
