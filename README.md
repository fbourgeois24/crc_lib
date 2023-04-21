# Calcul de sommes de controle (CRC) en tout genre

## Importer la bibliothèque : 

```python
import crc_lib
```

## VCS

***2 chiffres de clé de contrôle***

### Méthode de calcul

Pour calculer la clé de contrôle d'un VCS il faut faire un modulo (%) 97 des 10 premiers chiffres.

ATTENTION, cas particulier : si la clé de contrôle = 0 => elle est = 97 (la clé de contrôle ne peut JAMAIS être 0)

Exemple pour le vcs 020343057642

Clé de contrôle = 0203430576 % 97 = 42

### Utilisation de la bibliothèque

Il est possible de calculer une clé de contrôle ou de vérifier une clé existante.

```python
resultat = crc_lib.vcs(data)
```

Si data contient un vcs complet (12 chiffres) la fonction renverra `VRAI` si le vcs est correct et `FAUX` s'il ne l'est pas
Si data contient un vcs sans la clé de contrôle (10 chiffres), la fonction renverra le vcs complet (12 chiffres) avec la clé de contrôle calculée

### BBAN -> IBAN

### Méthode de calcul

Pour transformer un BBAN (12 chiffres) en IBAN (2 lettres et 14 chiffres) il faut ajouter BE si belgique + 2 chiffres.

Les 2 chiffres se calculent comme suit (si les 2 derniers chiffres du BBAN sont représentés par ab): 98 - (abab111400 % 97)

### Utilisation de la bibliothèque

La fonction renvoie les 2 chiffres à ajouter devant le BBAN pour le transformer en IBAN

```python
resultat = crc_lib.bban_iban(data)
```
Data doit contenir le BBAN

### EAN 18
***1 chiffre de clé de contrôle***

### Méthode de calcul

Pour calculer la somme de contrôle d'un ean à 18 chiffres, il faut additionner tous les chiffres (avec un poids différent) et calculer : 10 - (somme % 10).

Le % correspond à l'opération "modulo".

Poids du chiffre: si le rang du chiffre est pair (en commençant à zéro) le chiffre est multiplié par 3 sinon il est pris tel quel.

ATTENTION, cas particulier: si la somme de contrôle = 10 => elle est = 0



Exemple pour l'ean 542501390000184893, nous allons donc calculer le dernier chiffre => 3

|||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|EAN|5|4|2|5|0|1|3|9|0|0|0|0|1|8|4|8|9|
|Rang|0|1|0|1|0|1|0|1|0|1|0|1|0|1|0|1|0|
|Poids|3|1|3|1|3|1|3|1|3|1|3|1|3|1|3|1|3|
|Resultat|15|4|6|5|0|1|9|9|0|0|0|0|3|8|12|8|27|

Somme des résultats = 107

Calcul de la somme de contrôle : 10 - (107 % 10) = 3

La somme de contrôle (dernier chiffre) dans l'EAN ci-dessus est bien 3.

### Utilisation de la bibliothèque

Il est possible de calculer une somme de contrôle ou de vérifier une somme existante.

```python
resultat = crc_lib.ean_18(data)
```

Si data contient un ean complet (18 chiffres) la fonction renverra `VRAI` si l'ean est correct et `FAUX` s'il ne l'est pas
Si data contient un ean sans la somme de contrôle (17 chiffres), la fonction renverra l'ean complet (18 chiffres) avec la somme de contrôle calculée

