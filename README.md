# METRICS 3D

Celem projektu jest implementacja miar podobieństwa dla zbioru struktur przestrzennych,
przy zalozeniu identycznosci sekwencyjnej struktur.

Zaimplementowane miary
RMSD, INF (WC, nWC, stacking, all), P-value, DI i Clash Score

Metryki opisano w artykule: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2743038/

- Program umozliwia obliczenie powyzszych miar po podaniu na wejsciu plikow PDB.
- Program umozliwia obliczenie miar dla fragmentow struktur ograniczonych sfera o podanym promieniu i srodku
- Base pair zostaja pobrane z serwera dla istniejacych zwiazkow, uzytkownik ma jednak mozliwosc podania na wejsciu rezultatu z programu MCAnnotate.

# Instrukcja uzycia

1.
2.
3.
4.
+
+
+


# Use cases

Przyklady uzycia zostaly umieszczone w katalogu examples

+ RMSDExample

+ PvalueExample
Obliczanie pvalue dla zwiazkow 4TNA i 4TRA, oraz 1EHZ i 1EVV
```
metric.p_value('pdb/pdb4tna.ent', 'pdb/pdb4tra.ent')

metric.p_value('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent')
```
+ InfExample

+ DIExample

+ ClashScoreExample

#####