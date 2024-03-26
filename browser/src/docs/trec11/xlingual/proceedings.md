# Proceedings - Cross-Language 2002 

#### The TREC 2002 Arabic/English CLIR Track

_Douglas W. Oard, Fredric C. Gey_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/OVERVIEW.gey.ps.gz](http://trec.nist.gov/pubs/trec11/papers/OVERVIEW.gey.ps.gz)
??? abstract "Abstract"
	
	Nine teams participated in the TREC-2002 cross-language information retrieval track, which focused on retrieving Arabic language documents based on 50 topics that were originally prepared in English. Arabic translations of the topic descriptions were also made available to facilitate monolingual Arabic runs. This was the second year in which a large Arabic document collection was available. Three new teams joined the evaluation, and the cross-language aspect of the evaluation received more attention this year than in TREC-2001. A set of standard linguistic resources was made available to facilitate cross-system comparisons, and their use as a contrastive condition was encouraged. Unique contributions to the relevance pools were more typical of previous TREC evaluations then the results of TREC-2001 had been for the same document collection, with no run uniquely contributing more than 6% of the known relevant documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OardG02.bib) "
	```
	@inproceedings{DBLP:conf/trec/OardG02,
		author = {Douglas W. Oard and Fredric C. Gey},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {TREC} 2002 Arabic/English {CLIR} Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/OVERVIEW.gey.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OardG02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Named Page Finding and Arabic Retrieval with Hummingbird  SearchServerTM at TREC 2002

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird](./participants.md#hummingbird)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/hummingbird.tomlinson.pdf](http://trec.nist.gov/pubs/trec11/papers/hummingbird.tomlinson.pdf)
- :material-file-search: **Runs:** [humAR02td](./runs.md#humar02td) | [humAR02tde](./runs.md#humar02tde) | [humAR02tdm](./runs.md#humar02tdm) | [humAR02tdne](./runs.md#humar02tdne) | [humAR02te](./runs.md#humar02te)

??? abstract "Abstract"
	
	Hummingbird participated in the named page finding task of the TREC 2002 Web Track (find the named page in 18GB from the .GOV domain) and the monolingual Arabic topic relevance task of the TREC 2002 Cross-Language Track (find all relevant documents in 869MB of Arabic news data). In the named page finding task, SearchServer returned the named page in the first 10 rows for more than 80% of the 150 queries. Searching the full document content produced mean reciprocal rank (MRR) scores more than 20 points higher than just searching particular HTML properties (such as the Title), but enhancing a content search with a little extra weight for HTML properties further increased MRR by 6 points (with standard error of just 2 points). Treating queries as phrases was not found to help significantly (on average), but document length normalization increased MRR by more than 20 points. For Arabic topic relevance, light algorithmic stemming increased mean average precision (MAP) by 5 points, use of Arabic stop words increased MAP by 1 point, and query expansion from blind feedback increased MAP by 3 points.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson02,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments in Named Page Finding and Arabic Retrieval with Hummingbird SearchServerTM at {TREC} 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/hummingbird.tomlinson.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 11 Experiment: Arabic, Named Page and Topic Distillation  Searches

_Jacques Savoy, Yves Rasolofo_

- :fontawesome-solid-user-group: **Participant:** [Neuchatel](./participants.md#neuchatel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uneuchatel.pdf](http://trec.nist.gov/pubs/trec11/papers/uneuchatel.pdf)
- :material-file-search: **Runs:** [UniNE1](./runs.md#unine1) | [UniNE2](./runs.md#unine2) | [UniNE3](./runs.md#unine3) | [UniNE4](./runs.md#unine4)

??? abstract "Abstract"
	
	This year we took part in the Arabic cross-language information retrieval track (for us limited to monolingual Arabic retrieval) and also in both named page and topic distillation searches. In the last two tasks, we made use of link anchor information and document content in order to construct Web page representatives. This document representation uses multi-vectors in order to highlight the importance of both link anchor information and document content.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SavoyR02.bib) "
	```
	@inproceedings{DBLP:conf/trec/SavoyR02,
		author = {Jacques Savoy and Yves Rasolofo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Report on the {TREC} 11 Experiment: Arabic, Named Page and Topic Distillation Searches},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/uneuchatel.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SavoyR02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JHU/APL at TREC 2002: Experiments in Filtering and Arabic Retrieval

_Paul McNamee, Christine D. Piatko, James Mayfield_

- :fontawesome-solid-user-group: **Participant:** [jhu_apl](./participants.md#jhu_apl)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/jhuapl.mcnamee.pdf](http://trec.nist.gov/pubs/trec11/papers/jhuapl.mcnamee.pdf)
- :material-file-search: **Runs:** [apl11ca1](./runs.md#apl11ca1) | [apl11ce1](./runs.md#apl11ce1) | [apl11ce3](./runs.md#apl11ce3) | [apl11ce4](./runs.md#apl11ce4) | [apl11ce2](./runs.md#apl11ce2)

??? abstract "Abstract"
	
	The Johns Hopkins University Applied Physics Laboratory (JHU/APL) participated in two tracks at this year's conference. We participated in the filtering track, again addressing the batch and routing subtasks, as well as the adaptive task for the first time. We also continued experiments in Arabic retrieval, emphasizing language-neutral approaches. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McNameePM02.bib) "
	```
	@inproceedings{DBLP:conf/trec/McNameePM02,
		author = {Paul McNamee and Christine D. Piatko and James Mayfield},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{JHU/APL} at {TREC} 2002: Experiments in Filtering and Arabic Retrieval},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/jhuapl.mcnamee.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McNameePM02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Building an Arabic Stemmer for Information Retrieval

_Aitao Chen, Fredric C. Gey_

- :fontawesome-solid-user-group: **Participant:** [berkeley](./participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ucalberkeley.chen.pdf](http://trec.nist.gov/pubs/trec11/papers/ucalberkeley.chen.pdf)
- :material-file-search: **Runs:** [BKYCL1](./runs.md#bkycl1) | [BKYMON](./runs.md#bkymon) | [BKYCL2](./runs.md#bkycl2) | [BKYCL3](./runs.md#bkycl3)

??? abstract "Abstract"
	
	In TREC 2002 the Berkeley group participated only in the English-Arabic cross-language retrieval (CLIR) track. One Arabic monolingual run and three English-Arabic cross-language runs were submitted. Our approach to the cross-language retrieval was to translate the English topics into Arabic using online English-Arabic machine translation systems. The four official runs are named as BKYMON, BKYCL1, BKYCL2, and BKYCL3. The BKYMON is the Arabic monolingual run, and the other three runs are English-to-Arabic cross-language runs. This paper reports on the construction of an Arabic stoplist and two Arabic stemmers, and the experiments on Arabic monolingual retrieval, English-to-Arabic cross-language retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenG02.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenG02,
		author = {Aitao Chen and Fredric C. Gey},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Building an Arabic Stemmer for Information Retrieval},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/ucalberkeley.chen.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenG02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT at TREC 2002 Linear Combinations Based on Document Structure  and Varied Stemming for Arabic Retrieval

_Abdur Chowdhury, Mohammed Aljlayl, Eric C. Jensen, Steven M. Beitzel, David A. Grossman, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [IIT](./participants.md#iit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/iit.grossman.pdf](http://trec.nist.gov/pubs/trec11/papers/iit.grossman.pdf)
- :material-file-search: **Runs:** [iit02mel](./runs.md#iit02mel) | [iit02mpl](./runs.md#iit02mpl) | [iit02mnl](./runs.md#iit02mnl) | [iit02xma](./runs.md#iit02xma) | [iit02xst](./runs.md#iit02xst)

??? abstract "Abstract"
	
	For TREC 10 we participated in the Named Page Finding Task and the Cross-Lingual Task. In the web track, we explored the use of linear combinations of term collections based on document structure. Our goal was to examine the effects of different term collection statistics based on document structure in respect to known item retrieval. We parsed documents into structural components and built specific term indexes based on that document structure. Each of those indices have their own collection statistics for term weighting based on the type of language used for that structure in the collection. For producing a single ranked list, we examined a weighted linear combination approach to merging results. Our approach to known item retrieval was equal or above the median 58% of the time and 71% above the mean score of submitted runs. In the Arabic track we participated in Arabic Cross-language Information Retrieval (CLIR) and in Arabic monolingual information retrieval. For the monolingual retrieval, we examined the use of two stemming algorithms. The first is a deeper approach, and the second is a pattern-based approach. For the Arabic CLIR, we explored the retrieval effectiveness by using a machine translation (MT) system and translation probabilities obtained from parallel documents collection provided by the United Nations (UN).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChowdhuryAJBGF02.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChowdhuryAJBGF02,
		author = {Abdur Chowdhury and Mohammed Aljlayl and Eric C. Jensen and Steven M. Beitzel and David A. Grossman and Ophir Frieder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IIT} at {TREC} 2002 Linear Combinations Based on Document Structure and Varied Stemming for Arabic Retrieval},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/iit.grossman.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChowdhuryAJBGF02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLIR Experiments at Maryland for TREC 2002: Evidence Combination  for Arabic-English Retrieval

_Kareem Darwish, Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [umd_oard](./participants.md#umd_oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/umd.darwish.pdf](http://trec.nist.gov/pubs/trec11/papers/umd.darwish.pdf)
- :material-file-search: **Runs:** [AutoClirWsum](./runs.md#autoclirwsum) | [AutoClirExp](./runs.md#autoclirexp) | [ManMono](./runs.md#manmono) | [AutoMono](./runs.md#automono) | [AutoClirDoc](./runs.md#autoclirdoc)

??? abstract "Abstract"
	
	The focus of the experiments reported in this paper was techniques for combining evidence for cross-language retrieval, searching Arabic documents using English queries. Evidence from multiple sources of translation knowledge was combined to estimate translation probabilities, and four techniques for estimating query-language term weights from document-language evidence were tried. A new technique that exploits translation probability information was found to outperform a comparable technique in which that information was not used. Comparative results for three variants of Arabic “light” stemming are also presented. A simple variant of an existing stemming algorithm was found to result in significantly better retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DarwishO02.bib) "
	```
	@inproceedings{DBLP:conf/trec/DarwishO02,
		author = {Kareem Darwish and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CLIR} Experiments at Maryland for {TREC} 2002: Evidence Combination for Arabic-English Retrieval},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/umd.darwish.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DarwishO02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Arabic Information Retrieval at IBM

_Martin Franz, J. Scott McCarley_

- :fontawesome-solid-user-group: **Participant:** [ibm-abe](./participants.md#ibm-abe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ibm.franz.pdf](http://trec.nist.gov/pubs/trec11/papers/ibm.franz.pdf)
- :material-file-search: **Runs:** [ibmy02a](./runs.md#ibmy02a) | [ibmy02b](./runs.md#ibmy02b) | [ibmy02c](./runs.md#ibmy02c) | [ibmy02d](./runs.md#ibmy02d)

??? abstract "Abstract"
	
	IBM built two systems for crosslanguage experiments with English queries and Arabic documents. One system approached translation and retrieval as entirely separate tasks: we used a machine translation system to translate the Arabic documents into English, and then did the retrieval with a standard English IR system; the other system incorporated the parameters of a machine translation model directly into an IR scoring formula. A further experiment combined both models. For processing Arabic text, we had access to an innovative Arabic morphological analyzer, whose details will be described elsewhere. We incorporated well-known text normalizations [1] into the Arabic text processing. Our monolingual baseline system was similar to the system we have used in previous ad hoc tracks |3], and consisted of an Okapi |4] first pass followed by LCA-style 5 query expansion, applied to the normalized Arabic stems. Translation model parameters were estimated from the U.N. parallel corpus. The English half was morphologically analyzed (as were the English queries in our submissions); the Arabic half was morphologically analyzed and text normalizations were applied. We built separate translation models relating normalized Arabic morphs to English morphs and relating Arabic words to English morphs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FranzM02.bib) "
	```
	@inproceedings{DBLP:conf/trec/FranzM02,
		author = {Martin Franz and J. Scott McCarley},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Arabic Information Retrieval at {IBM}},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/ibm.franz.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FranzM02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2002 Cross-lingual Retrieval at BBN

_Alexander M. Fraser, Jinxi Xu, Ralph M. Weischedel_

- :fontawesome-solid-user-group: **Participant:** [BBN](./participants.md#bbn)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/bbn.xu.cross.pdf](http://trec.nist.gov/pubs/trec11/papers/bbn.xu.cross.pdf)
- :material-file-search: **Runs:** [BBN11XLA](./runs.md#bbn11xla) | [BBN11XLB](./runs.md#bbn11xlb) | [BBN11XLC](./runs.md#bbn11xlc) | [BBN11XLS](./runs.md#bbn11xls)

??? abstract "Abstract"
	
	We used basically the same retrieval system we used in TREC 2001. Our experiments featured a different method for estimating general English probabilities, two additional Arabic stemmers, a more complex model for lexicon extraction from parallel texts and a slightly different method for query expansion. To our disappointment, these changes did not improve retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FraserXW02.bib) "
	```
	@inproceedings{DBLP:conf/trec/FraserXW02,
		author = {Alexander M. Fraser and Jinxi Xu and Ralph M. Weischedel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2002 Cross-lingual Retrieval at {BBN}},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/bbn.xu.cross.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FraserXW02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2002: Cross Language and Novelty Tracks

_Leah S. Larkey, James Allan, Margaret E. Connell, Alvaro Bolivar, Courtney Wade_

- :fontawesome-solid-user-group: **Participant:** [umass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/umass.wade.pdf](http://trec.nist.gov/pubs/trec11/papers/umass.wade.pdf)
- :material-file-search: **Runs:** [UMassM](./runs.md#umassm) | [UMassX2](./runs.md#umassx2) | [UMassX2n](./runs.md#umassx2n) | [UMassX6](./runs.md#umassx6) | [UMassX6n](./runs.md#umassx6n)

??? abstract "Abstract"
	
	The University of Massachusetts participated in the cross-language and novelty tracks this year. The cross-language submission was characterized by combination of evidence to merge results from two different retrieval engines and a variety of different resources – stemmers, dictionaries, machine translation, and an acronym database. We found that proper names were extremely important in this year's queries. For the novelty track, we applied variants of techniques that have been employed for other problems. In addition, we created additional training data by manually annotating 48 additional topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LarkeyACBW02.bib) "
	```
	@inproceedings{DBLP:conf/trec/LarkeyACBW02,
		author = {Leah S. Larkey and James Allan and Margaret E. Connell and Alvaro Bolivar and Courtney Wade},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass at {TREC} 2002: Cross Language and Novelty Tracks},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/umass.wade.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LarkeyACBW02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

