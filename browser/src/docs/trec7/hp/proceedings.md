# Proceedings - High-Precision 1998 

#### SMART High Precision: TREC 7

_Chris Buckley, Mandar Mitra, Janet A. Walz, Claire Cardie_

- :fontawesome-solid-user-group: **Participant:** [Cornell/Sabir](./participants.md#cornell/sabir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/cornell.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/cornell.pdf.gz)
- :material-file-search: **Runs:** [Cor7HP1](./runs.md#cor7hp1) | [Cor7HP2](./runs.md#cor7hp2) | [Cor7HP3](./runs.md#cor7hp3)

??? abstract "Abstract"
	
	The Smart information retrieval project emphasizes completely automatic approaches to the understanding and retrieval of large quantities of text. We continue our work in TREC 7, concentrating on high precision retrieval. In particular, we present an in-depth analysis of our High-Precision Track results, including offering evaluation approaches and measures for time dependent evaluation. We participated in the Query Track, making initial efforts at analyzing query variability, one of the major obstacles for improving retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleyMWC98.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleyMWC98,
		author = {Chris Buckley and Mandar Mitra and Janet A. Walz and Claire Cardie},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{SMART} High Precision: {TREC} 7},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {230--243},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/cornell.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BuckleyMWC98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Deriving Very Short Queries for High Precision and Recall (MultiText  Experiments for TREC-7)

_Gordon V. Cormack, Christopher R. Palmer, Michael Van Biesbrouck, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/mt7.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/mt7.pdf.gz)
- :material-file-search: **Runs:** [uwmt7h1](./runs.md#uwmt7h1) | [uwmt7h2](./runs.md#uwmt7h2)

??? abstract "Abstract"
	
	The main aim of the MultiText experiments for TREC-7 was to derive very short queries that would yield high precision and recall, using a hybrid of manual and automatic processes. Identical queries were formulated for adhoc and VLC runs. A query set derived automatically from the topic title words, with an average of 2.84 terms per query, achieved a reasonable but unexceptional average precision for the adhoc task and a median precision @20 for the 100 GB VLC task. However, these short queries achieved very fast retrieval times — less than 1 second per query over 100 GB using four inexpensive PCs. Two further query sets were derived using post-processing of the results of interactive searching on the adhoc corpus. Queries comprising a single conjunction, averaging 1.86 terms, achieved high precision on both adhoc and VLC tasks, and achieved faster retrieval times than the title-word queries. Compound queries averaging 6.42 terms achieved precision values competitive with the best runs, and retrieval times of 1.51 seconds per query on the 100 GB VLC corpus.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackPBC98.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackPBC98,
		author = {Gordon V. Cormack and Christopher R. Palmer and Michael Van Biesbrouck and Charles L. A. Clarke},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Deriving Very Short Queries for High Precision and Recall (MultiText Experiments for {TREC-7)}},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {68--79},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/mt7.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CormackPBC98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-7 Ad-Hoc, High Precision and Filtering Experiments using PIRCS

_Kui-Lam Kwok, Laszlo Grunfeld, M. Chan, Norbert Dinstl, Colleen Cool_

- :fontawesome-solid-user-group: **Participant:** [CUNY](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/queens.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/queens.pdf.gz)
- :material-file-search: **Runs:** [pirc8Ha](./runs.md#pirc8ha)

??? abstract "Abstract"
	
	In TREC-7, we participated in the main task of automatic ad-hoc retrieval as well as the high precision and filtering tracks. For ad-hoc, three experiments were done with query types of short (title section of a topic), medium (description section) and long (all sections) lengths. We used a sequence of five methods to handle the short and medium length queries. For long queries we employed a re-ranking method based on evidence from matching query phrases in document windows in both stages of a 2-stage retrieval. Results are well above median. For high precision track, we employed our interactive PIRCS system for the first time. In adaptive filtering, we concentrate on dynamically varying the retrieval status value threshold for deciding selection and during the course of filtering. Query weights were trained but expansion was not done. We also submitted results for batch filtering and standard routing based on methods evolved from previous TREC experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokGCDC98.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokGCDC98,
		author = {Kui{-}Lam Kwok and Laszlo Grunfeld and M. Chan and Norbert Dinstl and Colleen Cool},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-7} Ad-Hoc, High Precision and Filtering Experiments using {PIRCS}},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {287--297},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/queens.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KwokGCDC98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ACSys TREC-7 Experiments

_David Hawking, Nick Craswell, Paul B. Thistlewaite_

- :fontawesome-solid-user-group: **Participant:** [ANU](./participants.md#anu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/acsys.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/acsys.pdf.gz)
- :material-file-search: **Runs:** [acsys7hp](./runs.md#acsys7hp)

??? abstract "Abstract"
	
	Experiments relating to TREC-7 Ad Hoc, HP and VLC tasks are described and results reported. Minor refinements of last year's Ad Hoc methods do not appear to have resulted in worthwile improvements in performance. However, larger benefits were gained from automatic feedback than last year and concept scoring was very beneficial in the Manual Ad Hoc category. In the Automatic Ad Hoc category title-only performance seems to have suffered more severely than long-topic from a number of lexical scanning shortcomings and from an excessive stopword list. The HP track was used to validate the usibility of the combination of PADRE and the Quokka GUI. In the VLC track, the 100 gigabyte collection was indexed in under eight hours and moderately effective queries were processed in less than two seconds.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingCT98a.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingCT98a,
		author = {David Hawking and Nick Craswell and Paul B. Thistlewaite},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {ACSys {TREC-7} Experiments},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {244--257},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/acsys.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HawkingCT98a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

