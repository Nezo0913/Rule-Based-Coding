# ==========================================
# Manga Personalization Application
# ==========================================

# Manga database
manga = {
    "Goblin Slayer": ["Fantasy", "Action"],
    "Nisekoi": ["Romance"],
    "Bleach": ["Action"],
    "Ascendance of a Bookworm": ["Fantasy", "Slice-of-Life"],
    "The Hero and the Demon Lord": ["Romance", "Fantasy"],
    "Fate/Stay Night": ["Fantasy", "Action", "Romance"],
    "My Romcom Comedy": ["Romance", "Slice-of-Life"],
    "Grimgar | Ash and Blood": ["Fantasy", "Action"],
    "Cooking with the Emiya Family": ["Slice-of-Life"],
    "A Returner's Magic Should Be Special": ["Fantasy", "Action"],
    "Clannad": ["Romance", "Slice-of-Life"],
    "Spy x Family": ["Slice-of-Life", "Action"]
}

# Available genres
genres = [
    "Fantasy",
    "Slice-of-Life",
    "Action",
    "Romance"
]


# ==========================================
# RULE 1
# Genre Selection -> Manga Selection
# ==========================================

def show_manga_by_genre(selected_genre):
    print("\n==========================================")
    print(f"MANGA IN THE {selected_genre.upper()} GENRE")
    print("==========================================")

    matching_manga = []

    for title, manga_genres in manga.items():
        if selected_genre in manga_genres:
            matching_manga.append(title)

    if len(matching_manga) == 0:
        print("No manga found for this genre.")
    else:
        for number, title in enumerate(matching_manga, start=1):
            print(f"{number}. {title}")

    return matching_manga


# ==========================================
# RULE 2
# Manga Selection -> Similar Manga
# ==========================================

def recommend_manga(selected_manga):
    selected_genres = manga[selected_manga]

    print("\n==========================================")
    print("         MANGA RECOMMENDATIONS")
    print("==========================================")

    print(f"\nYou selected: {selected_manga}")
    print(f"Genres: {', '.join(selected_genres)}")

    recommendations = []

    for title, manga_genres in manga.items():

        # Do not recommend the manga the user already selected
        if title == selected_manga:
            continue

        # Check if the manga shares at least one genre
        shared_genres = set(selected_genres).intersection(manga_genres)

        if shared_genres:
            recommendations.append((title, shared_genres))

    if len(recommendations) == 0:
        print("\nNo similar manga found.")
    else:
        print("\nYou may also like:")

        for number, (title, shared_genres) in enumerate(
            recommendations, start=1
        ):
            print(
                f"{number}. {title} "
                f"({', '.join(shared_genres)})"
            )

    print("\nWould you like to read any of these next?")


# ==========================================
# Display Genres
# ==========================================

def show_genres():
    print("\n==========================================")
    print("             MANGA GENRES")
    print("==========================================")

    for number, genre in enumerate(genres, start=1):
        print(f"{number}. {genre}")


# ==========================================
# Main Application
# ==========================================

def main():

    print("==========================================")
    print("       WELCOME TO THE MANGA APP")
    print("==========================================")

    while True:

        show_genres()

        print("\n0. Exit")

        try:
            genre_choice = int(input("\nChoose a genre: "))

        except ValueError:
            print("\nPlease enter a valid number.")
            continue

        # Exit application
        if genre_choice == 0:
            print("\nThank you for using the Manga App!")
            break

        # Check valid genre selection
        if genre_choice < 1 or genre_choice > len(genres):
            print("\nInvalid genre selection.")
            continue

        # Get selected genre
        selected_genre = genres[genre_choice - 1]

        # RULE 1
        matching_manga = show_manga_by_genre(selected_genre)

        if len(matching_manga) == 0:
            continue

        # Let user choose a manga
        print("\n0. Back to Genres")

        try:
            manga_choice = int(
                input("\nChoose a manga: ")
            )

        except ValueError:
            print("\nPlease enter a valid number.")
            continue

        if manga_choice == 0:
            continue

        if manga_choice < 1 or manga_choice > len(matching_manga):
            print("\nInvalid manga selection.")
            continue

        # Get selected manga
        selected_manga = matching_manga[manga_choice - 1]

        # RULE 2
        recommend_manga(selected_manga)

        input("\nPress Enter to return to the genre menu...")


# ==========================================
# Start Program
# ==========================================

if __name__ == "__main__":
    main()