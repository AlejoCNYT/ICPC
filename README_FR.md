# 🏆 ICPC - Révision de Programmation Compétitive

← [Retour à l'Accueil (Main README)](README.md)

Ce fichier contient la documentation complète en français des solutions de révision pour les problèmes de programmation compétitive selon les normes de l'**ICPC**.

## 🚀 Structure du Dépôt

Voici les détails des solutions de révision actuellement implémentées dans le dépôt :

| Problème / Fichier | Plateforme | Approche / Technique Principale | Langage |
| :--- | :---: | :--- | :---: |
| `uva100_the_3n_plus_1_problem.py` | **UVA 100** | Suite de Collatz optimisée par **Mémorisation** (Memoization) et rétropropagation dynamique. | Python |
| `230B-TPrimes` | **Codeforces 230B** | Théorie des nombres, **Crible d'Ératosthène** et vérification efficace des carrés parfaits de nombres premiers. | Python |
| `223_Rectangle Area` | **LeetCode / UVA 223** | Géométrie algorithmique et calcul d'intersection d'aires bidimensionnelles. | Python |
| `725-Division` | **UVA 725** | Recherche exhaustive (Brute Force), manipulation de chiffres, ensembles (`set`), réduction de l’espace de recherche et formatage de sortie. | Python |
| `binary_search_neighbors.py` | **Binary Search** | Variantes de recherche binaire pour trouver les bornes inférieure et supérieure les plus proches dans un tableau trié et sans doublons. | Python |

## 🧠 Concepts Révisés

* **Optimisation & Programmation Dynamique:** Utilisation de structures de cache (`memo`) pour éviter le recalcul de sous-problèmes chevauchants.
* **Théorie des Nombres:** Exploitation des propriétés des nombres premiers et optimisation de la complexité temporelle dans les boucles de factorisation.
* **Géométrie Computationnelle:** Gestion analytique des coordonnées cartésiennes et de la superposition de régions.
* **Recherche Exhaustive (Brute Force) :** Énumération complète optimisée grâce à un élagage mathématique réduisant efficacement l’espace de recherche.
* **Manipulation des Chiffres :** Vérification de l’unicité et de la couverture complète des chiffres à l’aide d’ensembles (`set`).
* **Variantes de la recherche binaire :** Recherche efficace en `O(log n)` du plus grand élément inférieur à `x` et du plus petit élément supérieur à `x` dans un tableau trié.

## 💻 Instructions d'Exécution

Les solutions sont optimisées pour traiter des flux de données continus via l'entrée standard (`stdin`) jusqu'à la fin du fichier (`EOF`).
