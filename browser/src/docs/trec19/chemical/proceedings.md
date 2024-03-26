# Proceedings - Chemical 2010 

#### TREC-CHEM 2010

_Mihai Lupu, John Tait, Jimmy X. Huang, Jianhan Zhu_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec19/papers/CHEM.OVERVIEW.pdf](https://trec.nist.gov/pubs/trec19/papers/CHEM.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC Chemical IR Track is a domain-specific evaluation campaign working with documents containing specific lexica, including chemical formulas and specific names. The 2010 edition of the track also included supporting material in addition to text: images and structure information files. As in the previous year, we had two tasks: a patent focused prior-art (PA) task and a user-focused Technology Survey task (TS). The data collection includes patent files as well as scientific articles, together with their attachments, if any. Topics and relevance judgments were either automatically or manually created.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LupuTHZ10.bib) "
	```
	@inproceedings{DBLP:conf/trec/LupuTHZ10,
		author = {Mihai Lupu and John Tait and Jimmy X. Huang and Jianhan Zhu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC-CHEM} 2010},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {https://trec.nist.gov/pubs/trec19/papers/CHEM.OVERVIEW.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LupuTHZ10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BiTeM site Report for TREC Chemistry 2010: Impact of Citations Feeback  for Patent Prior Art Search and Chemical Compounds Expansion for Ad  Hoc Retrieval

_Julien Gobeill, Arnaud Gaudinat, Patrick Ruch, Emilie Pasche, Douglas Teodoro, Dina Vishnyakova_

- :fontawesome-solid-user-group: **Participant:** [BiTeM](./participants.md#bitem)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.geneva.chem.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.geneva.chem.rev.pdf)
- :material-file-search: **Runs:** [BiTeM09TSbl](./runs.md#bitem09tsbl) | [BiTeM09TSsqe](./runs.md#bitem09tssqe) | [BiTeM09TSmqe](./runs.md#bitem09tsmqe) | [BiTeM09TSlqe](./runs.md#bitem09tslqe) | [BiTeM10PAx](./runs.md#bitem10pax) | [BiTeM10PAsmx](./runs.md#bitem10pasmx)

??? abstract "Abstract"
	
	For two years, the TREC Chemical Track aims at evaluating participant systems in chemical patent searching. In 2010, it continued with the two tasks from 2009: Prior Art search (PA) and Technology Survey (TS). The BiTeM group participated in both tasks and obtained satisfactory results, relying on a large panel of strategies which were evaluated within the framework of past similar competitions. There are three main conclusions that we draw from this campaign. First of all, regarding a baseline computed by Information Retrieval (IR) only, simplest models achieved the best results for both tasks, such as indexing only titles, abstracts, and claims, and no stemming; however, for the PA task, the performance of this baseline remains low (Mean Average Precision 0.043) compared to last year (MAP 0.067). Further analysis of the query set reveals that description sections were in 2010 twice longer than in 2009, while citations number was stable; having longer queries obviously resulted in a degradation of the signal-to-noise ratio, and in a more complex task for standard IR. Secondly, IPC codes were of no use for the PA task, and even decreased performances, whether they were injected in the index or used for filtering the results. Because this strategy is effective when applied to EPO patents in general domain, further experiments or expertise need to determine if it fails because it is applied to a specific domain, or because the quality of IPC annotations in USPTO patents is insufficient. The last conclusion deals with our re-ranking strategy based on citations feedback for the PA task. Such a strategy led to a dramatic improvement from 0.043 to 0.261 for MAP (+ 507%), and from 0.31 to 0.62 for Recall at 500 (+ 100%). Further analysis shows that our citations feedback strategy achieves to strongly capture the chemical applicants' behaviour, which tends to cite regular patterns of multiple patents massively inter-connected with direct citations. Results of the TS task prove the effectiveness of synonyms expansion driven by chemical entities normalization.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GobeillGRPTV10.bib) "
	```
	@inproceedings{DBLP:conf/trec/GobeillGRPTV10,
		author = {Julien Gobeill and Arnaud Gaudinat and Patrick Ruch and Emilie Pasche and Douglas Teodoro and Dina Vishnyakova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {BiTeM site Report for {TREC} Chemistry 2010: Impact of Citations Feeback for Patent Prior Art Search and Chemical Compounds Expansion for Ad Hoc Retrieval},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.geneva.chem.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GobeillGRPTV10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Prior Art Search in Chemistry Patents Based On Semantic Concepts and  Co-Citation Analysis

_Harsha Gurulingappa, Bernd Müller, Roman Klinger, Heinz-Theodor Mevissen, Martin Hofmann-Apitius, Christoph M. Friedrich, Juliane Fluck_

- :fontawesome-solid-user-group: **Participant:** [Fraunhofer.SCAI](./participants.md#fraunhofer.scai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/fraunhofer-scai.chem.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/fraunhofer-scai.chem.rev.pdf)
- :material-file-search: **Runs:** [SCAI10CIENTP](./runs.md#scai10cientp) | [SCAI10CITENT](./runs.md#scai10citent) | [SCAI10CITNP](./runs.md#scai10citnp) | [SCAI10CITTOK](./runs.md#scai10cittok) | [SCAI10NRMENT](./runs.md#scai10nrment) | [SCAI10NRMNP](./runs.md#scai10nrmnp) | [SCAI10NRMTOK](./runs.md#scai10nrmtok)

??? abstract "Abstract"
	
	Prior Art Search is a task of querying and retrieving the patents in order to uncover any knowledge existing prior to the inventor's question or invention at hand. For addressing this task, we present a contemporary approach that has been evaluated during Trecchem for its ability to adapt to text containing chemistry-based information. The core of the framework is an index of 1.3 million chemistry patents provided as a data set by Trecchem. For the prior art search task, the information of normalized noun phrases, biomedical and chemical entities are added to the full text index. Altogether, 7 runs were submitted for this task that were based on automatic querying with tokens, noun phrases and entities. In addition, the co-citation information was exploited in a systematic way to generate ranked citation sets from the retrieved documents. Querying with noun phrases and entities coupled with co-citation based post-processing performed considerably well with the best MAP score of 0.23.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GurulingappaMKMHFF10.bib) "
	```
	@inproceedings{DBLP:conf/trec/GurulingappaMKMHFF10,
		author = {Harsha Gurulingappa and Bernd M{\"{u}}ller and Roman Klinger and Heinz{-}Theodor Mevissen and Martin Hofmann{-}Apitius and Christoph M. Friedrich and Juliane Fluck},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Prior Art Search in Chemistry Patents Based On Semantic Concepts and Co-Citation Analysis},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/fraunhofer-scai.chem.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GurulingappaMKMHFF10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

