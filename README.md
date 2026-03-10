Oto Twój workflow i struktura pracy z repozytorium przekształcone na formę bezosobową. Taka forma idealnie nadaje się do dokumentacji projektu (np. w pliku CONTRIBUTING.md lub README.md), ponieważ brzmi jak zestaw obiektywnych zasad.

🎯 Podsumowanie workflow
Tworzenie brancha typu feature.

Praca nad kodem → commit → push.

Tworzenie Pull Request (PR) do gałęzi develop.

Przeprowadzenie testów.

Scalenie (merge) do gałęzi develop.

Stabilizacja kodu i finalny merge do main.

Usunięcie zbędnego brancha feature.

🏗️ Struktura branchy
main – stabilna wersja projektu, gotowa do prezentacji lub wdrożenia.

develop – główna gałąź rozwojowa; miejsce, w którym integrowane są ukończone funkcje.

feature/ – gałęzie funkcjonalne; każda nowa funkcjonalność posiada własny branch.

test_validation – środowisko dedykowane testom automatycznym.

🛠️ Praca nad nową funkcją
1. Utworzenie nowego brancha feature
Stosuje się komendę:
git switch -c feature/nazwa_funkcji

2. Praca nad kodem i wykonywanie commitów
Zmiany są dodawane i zatwierdzane:
git add .
git commit -m "Opis zmian"

3. Wypchnięcie brancha na serwer (GitHub)
git push -u origin feature/nazwa_funkcji

4. Utworzenie Pull Request do gałęzi develop
Jest to jedyne miejsce, w którym następuje scalanie funkcji. Podczas PR weryfikowane są:

poprawność działania kodu,

wyniki testów,

brak konfliktów.

5. Scalenie (merge) do gałęzi develop po akceptacji
develop służy jako punkt styku wszystkich zrealizowanych funkcjonalności.

6. Scalenie develop do main po uzyskaniu stabilności
Do gałęzi main trafia wyłącznie:

stabilny i przetestowany kod,

wersja gotowa do prezentacji.

🧪 Branch test_validation (opcjonalny)
W przypadku korzystania z osobnego środowiska testowego:

nie należy tam scalać gałęzi feature ani develop,

wykorzystuje się go wyłącznie do przeprowadzania testów automatycznych.

🧹 Usuwanie branchy po zakończeniu pracy
Po poprawnym scaleniu funkcji do develop, lokalna i zdalna gałąź feature podlegają usunięciu:

git branch -d feature/nazwa_funkcji
git push origin --delete feature/nazwa_funkcj
