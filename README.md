# METRICS 3D

Celem projektu jest implementacja miar podobieństwa dla zbioru struktur przestrzennych,
przy zalozeniu identycznosci sekwencyjnej struktur.

Zaimplementowane miary
RMSD, INF (WC, nWC, stacking, all), P-value, DI i Clash Score

Metryki opisano w artykule: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2743038/

- Program umozliwia obliczenie powyzszych miar po podaniu na wejsciu plikow PDB.
- Program umozliwia obliczenie miar dla fragmentow struktur ograniczonych sfera o podanym promieniu i atomie C1'
- Base pair zostaja pobrane z serwera dla istniejacych zwiazkow, uzytkownik ma jednak mozliwosc podania na wejsciu rezultatu z programu MCAnnotate.

# Instrukcja uzycia

- Stworzenie obiektu fasady Metric3D.
```
metric = Metrics3D()
```
- Fasada umożliwia wywołanie następujących funkcji:
```
- rmsd
- clash_score
- inf (z mozliwoscia filtrowania all pairs, all (pairs + stacking), stacking, wc (pary Watson Crick), nWc (pary nie-Watson Crick), stacking
- di
- p_value
```
- Parametry:
```
- pdb_file: ścieżka do pliku pdb
- first_pdb_path: ścieżka do pliku pdb
- second_pdb_path: ścieżka do pliku pdb
- residue_seq_id: numer residuum w którym będzie wyszukany atom C1'
- first_mcannotate_path:
- second_mcannotate_path:
```


# Use cases

Przyklady uzycia zostaly umieszczone w katalogu examples

+ RMSDExample
```
metric.rmsd('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent')
```
+ PvalueExample
```
metric.p_value('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent', residue_seq_id=56, radius=100)
```
+ InfExample
```
metric.inf('pdb/pdb4tna.ent', 'pdb/pdb6tna.ent', 'base_pair_mcannotate/4tna', 'base_pair_mcannotate/6tna', bp_type="nWc")
```
+ DIExample
```
metric.di('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent')
```
+ ClashScoreExample
```
metric.clash_score('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent')
```
#####