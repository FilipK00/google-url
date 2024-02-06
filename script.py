from googlesearch import search

def get_first_google_result_url(query):
    try:
        results = search(query, num_results=1)
        first_result = next(results, None)

        if first_result:
            print(f"Pierwszy wynik dla zapytania '{query}':")
            print(first_result)
        else:
            print("Brak wyników dla zapytania.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

search_query = "iFil Group"
get_first_google_result_url(search_query)
