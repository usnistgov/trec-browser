# Proceedings 2002 

## Overview of TREC 2002

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/OVERVIEW.11.pdf](http://trec.nist.gov/pubs/trec11/papers/OVERVIEW.11.pdf)
??? abstract "Abstract"
	
	The eleventh Text REtrieval Conference, TREC 2002, was held at the National Institute of Standards and Technology (NIST) November 19–22, 2002. The conference was co-sponsored by NIST, the Information Awareness Office of the Defense Advanced Research Projects Agency (DARPA/IAO), and the US Department of Defense Advanced Research and Development Activity (ARDA). TREC 2002 is the latest in a series of workshops designed to foster research on technologies for information retrieval. The workshop series has four goals: to encourage retrieval research based on large test collections; to increase communication among industry, academia, and government by creating an open forum for the ex- change of research ideas; to speed the transfer of technology from research labs into commercial products by demonstrating substantial improvements in retrieval methodologies on real-world problems; and to increase the availability of appropriate evaluation techniques for use by industry and academia, including development of new evaluation techniques more applicable to current systems. TREC 2002 contained seven areas of focus called “tracks”. These included the Cross-Language Retrieval Track, the Filtering Track, the Interactive Retrieval Track, the Novelty Track, the Question Answering Track, the Video Retrieval Track, and the Web Retrieval Track. This was the first year for the novelty track, which fostered research into detecting redundant information within a relevant document set. The other tracks were run in previous TRECs, though the particular tasks performed in some of the tracks changed for TREC 2002. Table 1 lists the 93 groups that participated in TREC 2002. The participating groups come from 21 different countries and include academic, commercial, and government institutions. This paper serves as an introduction to the research described in detail in the remainder of the volume. The next section provides a summary of the retrieval background knowledge that is assumed in the other papers. Section 3 presents a short description of each track—a more complete description of a track can be found in that track's overview paper in the proceedings. The final section looks forward to future TREC conferences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees02.bib)"
	```
	@inproceedings{DBLP:conf/trec/Voorhees02,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of {TREC} 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/OVERVIEW.11.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Cross-Language 

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

- :fontawesome-solid-user-group: **Participant:** [hummingbird](./xlingual/participants.md#hummingbird)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/hummingbird.tomlinson.pdf](http://trec.nist.gov/pubs/trec11/papers/hummingbird.tomlinson.pdf)
- :material-file-search: **Runs:** [humAR02td](./xlingual/runs.md#humar02td) | [humAR02tde](./xlingual/runs.md#humar02tde) | [humAR02tdm](./xlingual/runs.md#humar02tdm) | [humAR02tdne](./xlingual/runs.md#humar02tdne) | [humAR02te](./xlingual/runs.md#humar02te)

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

- :fontawesome-solid-user-group: **Participant:** [Neuchatel](./xlingual/participants.md#neuchatel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uneuchatel.pdf](http://trec.nist.gov/pubs/trec11/papers/uneuchatel.pdf)
- :material-file-search: **Runs:** [UniNE1](./xlingual/runs.md#unine1) | [UniNE2](./xlingual/runs.md#unine2) | [UniNE3](./xlingual/runs.md#unine3) | [UniNE4](./xlingual/runs.md#unine4)

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

- :fontawesome-solid-user-group: **Participant:** [jhu_apl](./xlingual/participants.md#jhu_apl)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/jhuapl.mcnamee.pdf](http://trec.nist.gov/pubs/trec11/papers/jhuapl.mcnamee.pdf)
- :material-file-search: **Runs:** [apl11ca1](./xlingual/runs.md#apl11ca1) | [apl11ce1](./xlingual/runs.md#apl11ce1) | [apl11ce3](./xlingual/runs.md#apl11ce3) | [apl11ce4](./xlingual/runs.md#apl11ce4) | [apl11ce2](./xlingual/runs.md#apl11ce2)

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

- :fontawesome-solid-user-group: **Participant:** [berkeley](./xlingual/participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ucalberkeley.chen.pdf](http://trec.nist.gov/pubs/trec11/papers/ucalberkeley.chen.pdf)
- :material-file-search: **Runs:** [BKYCL1](./xlingual/runs.md#bkycl1) | [BKYMON](./xlingual/runs.md#bkymon) | [BKYCL2](./xlingual/runs.md#bkycl2) | [BKYCL3](./xlingual/runs.md#bkycl3)

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

- :fontawesome-solid-user-group: **Participant:** [IIT](./xlingual/participants.md#iit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/iit.grossman.pdf](http://trec.nist.gov/pubs/trec11/papers/iit.grossman.pdf)
- :material-file-search: **Runs:** [iit02mel](./xlingual/runs.md#iit02mel) | [iit02mpl](./xlingual/runs.md#iit02mpl) | [iit02mnl](./xlingual/runs.md#iit02mnl) | [iit02xma](./xlingual/runs.md#iit02xma) | [iit02xst](./xlingual/runs.md#iit02xst)

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

- :fontawesome-solid-user-group: **Participant:** [umd_oard](./xlingual/participants.md#umd_oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/umd.darwish.pdf](http://trec.nist.gov/pubs/trec11/papers/umd.darwish.pdf)
- :material-file-search: **Runs:** [AutoClirWsum](./xlingual/runs.md#autoclirwsum) | [AutoClirExp](./xlingual/runs.md#autoclirexp) | [ManMono](./xlingual/runs.md#manmono) | [AutoMono](./xlingual/runs.md#automono) | [AutoClirDoc](./xlingual/runs.md#autoclirdoc)

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

- :fontawesome-solid-user-group: **Participant:** [ibm-abe](./xlingual/participants.md#ibm-abe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ibm.franz.pdf](http://trec.nist.gov/pubs/trec11/papers/ibm.franz.pdf)
- :material-file-search: **Runs:** [ibmy02a](./xlingual/runs.md#ibmy02a) | [ibmy02b](./xlingual/runs.md#ibmy02b) | [ibmy02c](./xlingual/runs.md#ibmy02c) | [ibmy02d](./xlingual/runs.md#ibmy02d)

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

- :fontawesome-solid-user-group: **Participant:** [BBN](./xlingual/participants.md#bbn)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/bbn.xu.cross.pdf](http://trec.nist.gov/pubs/trec11/papers/bbn.xu.cross.pdf)
- :material-file-search: **Runs:** [BBN11XLA](./xlingual/runs.md#bbn11xla) | [BBN11XLB](./xlingual/runs.md#bbn11xlb) | [BBN11XLC](./xlingual/runs.md#bbn11xlc) | [BBN11XLS](./xlingual/runs.md#bbn11xls)

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

- :fontawesome-solid-user-group: **Participant:** [umass](./xlingual/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/umass.wade.pdf](http://trec.nist.gov/pubs/trec11/papers/umass.wade.pdf)
- :material-file-search: **Runs:** [UMassM](./xlingual/runs.md#umassm) | [UMassX2](./xlingual/runs.md#umassx2) | [UMassX2n](./xlingual/runs.md#umassx2n) | [UMassX6](./xlingual/runs.md#umassx6) | [UMassX6n](./xlingual/runs.md#umassx6n)

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

## Web 

#### Overview of the TREC-2002 Web Track

_Nick Craswell, David Hawking_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/WEB.OVER.pdf](http://trec.nist.gov/pubs/trec11/papers/WEB.OVER.pdf)
??? abstract "Abstract"
	
	The TREC-2002 Web Track moved away from non-Web relevance ranking and towards Web-specific tasks on a 1.25 million page crawl “.GOV”. The topic distillation task involved finding pages which were relevant, but also had characteristics which would make them desirable inclusions in a distilled list of key pages. The named page task is a variant of last year's homepage finding task. The task is to find a particular page, but in this year's task the page need not be a home page.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellH02.bib) "
	```
	@inproceedings{DBLP:conf/trec/CraswellH02,
		author = {Nick Craswell and David Hawking},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC-2002} Web Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/WEB.OVER.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CraswellH02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Hierarchical Clustering and Summarisation Approaches for Web  Retrieval: Glasgow at the TREC 2002 Interactive Track

_Richard Osdin, Iadh Ounis, Ryen W. White_

- :fontawesome-solid-user-group: **Participant:** [glasgow](./web/participants.md#glasgow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/glasgow.int.pdf](http://trec.nist.gov/pubs/trec11/papers/glasgow.int.pdf)
- :material-file-search: **Runs:** [uog01ctaialh](./web/runs.md#uog01ctaialh) | [uog02ctadh](./web/runs.md#uog02ctadh) | [uog03ctadqh](./web/runs.md#uog03ctadqh) | [uog04cta2dqh](./web/runs.md#uog04cta2dqh) | [uog05tad](./web/runs.md#uog05tad) | [uog06c](./web/runs.md#uog06c) | [uog07cta](./web/runs.md#uog07cta) | [uog08ctap](./web/runs.md#uog08ctap) | [uog09cta2](./web/runs.md#uog09cta2) | [uog10ctad](./web/runs.md#uog10ctad)

??? abstract "Abstract"
	
	Current search engines are typified as having a lack of precision, coupled with an elongated ranked list style of result presentation. When combined, these factors make relevant data extraction increasingly complex. The main investigation of our participation in the Interactive Track of TREC 2002 is to assess the effectiveness of new visualisation techniques for displaying the results of search engines. Our current system, provisionally named HuddleSearch, uses a newly developed clustering algorithm, which dynamically organises the relevant documents into a traversable hierarchy of general to more-specific cluster categories. We have extended our TREC-10 summarisation tool to also allow the summarisation of multiple documents; whereby a summary paints a caricature of the contents of a cluster, rather than an individual document, thus allowing the user to provisionally judge a cluster's relevance prior to viewing its contents. The interaction between the user and the system is further developed by the aid of an information visualisation tool. Our primary assumption is that the combination of both hierarchical clustering and summarisation tools will aid users in their interaction with the system in the Web context.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OsdinOW02.bib) "
	```
	@inproceedings{DBLP:conf/trec/OsdinOW02,
		author = {Richard Osdin and Iadh Ounis and Ryen W. White},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Hierarchical Clustering and Summarisation Approaches for Web Retrieval: Glasgow at the {TREC} 2002 Interactive Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/glasgow.int.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OsdinOW02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UIC at TREC 2002: Web Track

_Shuang Liu, Clement T. Yu, Wensheng Wu_

- :fontawesome-solid-user-group: **Participant:** [illinois_chicago](./web/participants.md#illinois_chicago)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uillinois.li.pdf](http://trec.nist.gov/pubs/trec11/papers/uillinois.li.pdf)
- :material-file-search: **Runs:** [uic0101](./web/runs.md#uic0101) | [uic0102](./web/runs.md#uic0102) | [uic0103](./web/runs.md#uic0103) | [uicnp01](./web/runs.md#uicnp01) | [uicnp02](./web/runs.md#uicnp02) | [uicnp03](./web/runs.md#uicnp03) | [uic0104](./web/runs.md#uic0104)

??? abstract "Abstract"
	
	This is the first year that members of the Database and Information System Lab (DBIS) at University of Illinois at Chicago (UIC) participate in TREC. We participate in two tasks for the Web track: topic distillation and named page finding. Linkage information among documents as well as content information about documents is used in some of our submitted runs. We utilize the Okapi weighting scheme with some modification for documents and passages retrieval; the proximity of query terms in documents is also utilized for document ranking. The PageRank of a document is combined with the similarity of the document with the query to obtain an overall ranking of documents. A local linkage and URL analysis algorithm is employed for topic distillation. In the named page finding task, we combine the surrogate similarity with the document similarity in one run.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuYW02.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuYW02,
		author = {Shuang Liu and Clement T. Yu and Wensheng Wu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UIC} at {TREC} 2002: Web Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/uillinois.li.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuYW02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2002 Web, Novelty and Filtering Track Experiments using PIRCS

_Kui-Lam Kwok, Peter Deng, Norbert Dinstl, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./web/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/queens.kwok.pdf](http://trec.nist.gov/pubs/trec11/papers/queens.kwok.pdf)
- :material-file-search: **Runs:** [pirc2Wd1](./web/runs.md#pirc2wd1) | [pirc2Wd2](./web/runs.md#pirc2wd2) | [pirc2Wnp1](./web/runs.md#pirc2wnp1) | [pirc2Wnp2](./web/runs.md#pirc2wnp2)

??? abstract "Abstract"
	
	In TREC2002, we participated in three tracks: web, novelty and adaptive filtering. The Web track has two tasks: distillation and named-page retrieval. Distillation is a new utility concept for ranking documents, and needs new design on the output document ranked list after an ad-hoc retrieval from the web (.gov) collection. Novelty track is a new task that involves identifying relevant sentences to a question, and to remove duplicate or non-novel entries in the answer list. The third track is adaptive filtering. We revived a filtering program that was functional at TREC-9 with some added capability. Sections 2, 3, 4 describe our participation in these tracks respectively. Section 5 has our conclusion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokDDC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokDDC02,
		author = {Kui{-}Lam Kwok and Peter Deng and Norbert Dinstl and M. Chan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2002 Web, Novelty and Filtering Track Experiments using {PIRCS}},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/queens.kwok.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokDDC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CARROTT 11 and the TREC 11 Web Track

_R. Scott Cost, Srikanth Kallurkar, Hemali Majithia, Charles K. Nicholas, Yongmei Shi_

- :fontawesome-solid-user-group: **Participant:** [umbc-cost](./web/participants.md#umbc-cost)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/umbc.kallurkar.pdf](http://trec.nist.gov/pubs/trec11/papers/umbc.kallurkar.pdf)
- :material-file-search: **Runs:** [CARROT2A](./web/runs.md#carrot2a) | [CARROT2B](./web/runs.md#carrot2b) | [CARROT2D](./web/runs.md#carrot2d) | [CARROT2C](./web/runs.md#carrot2c) | [CARROT2E](./web/runs.md#carrot2e)

??? abstract "Abstract"
	
	We describe CARROT II, an agent-based architecture for distributed information retrieval and document collection management. CARROT II consists of an arbitrary number of agents, distributed across a variety of platforms and locations. CARROT II agents provide search services over local document collections or information sources. They advertise content-derived metadata that describes their local document store. This metadata is sent to other CARROT II agents which agree to act as brokers for that collection, and every agent in the system has the ability to serve as such a broker. A query can be sent to any CARROT II agent, which can decide to answer the query itself from its local collection, or to send the query on to other agents whose metadata indicate that they would be able to answer the query, or send the query on further. Search results from multiple agents are merged and returned to the user. CARROT II differs from similar systems in that metadata takes the form of an automatically generated, unstructured feature vector, and that any agent in the system can act as a broker, so there is no centralized control. We present experimental results of retrieval performance and effectiveness in a distributed environment. We have evaluated CARROT II in the context of the Web Track of NIST's annual Text Retrieval Conference. Our methodology is described, and results are presented. 
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CostKMNS02.bib) "
	```
	@inproceedings{DBLP:conf/trec/CostKMNS02,
		author = {R. Scott Cost and Srikanth Kallurkar and Hemali Majithia and Charles K. Nicholas and Yongmei Shi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CARROTT} 11 and the {TREC} 11 Web Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/umbc.kallurkar.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CostKMNS02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Filtering, Novelty Detection, and Named-Page Finding

_Kevyn Collins-Thompson, Paul Ogilvie, Yi Zhang, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [cmu_lti](./web/participants.md#cmu_lti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cmu.collins-thompson.pdf](http://trec.nist.gov/pubs/trec11/papers/cmu.collins-thompson.pdf)
- :material-file-search: **Runs:** [LmrAllEq](./web/runs.md#lmralleq) | [LmrAllEst](./web/runs.md#lmrallest) | [LmrNoStruct](./web/runs.md#lmrnostruct) | [LmrDocStruct](./web/runs.md#lmrdocstruct) | [LmrSmall](./web/runs.md#lmrsmall)

??? abstract "Abstract"
	
	In TREC 11, our group participated in the Novelty track, Filtering track, and the Named-Page Finding task of the Web track. This paper describes our approaches, experiments, and results. As the approach for each task is quite different, the paper contains a section for each of the tasks. The following section describes our experiments in adaptive filtering, Section 3 describes named-page finding, and section 4 discusses the Novelty track
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Collins-ThompsonOZC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Collins-ThompsonOZC02,
		author = {Kevyn Collins{-}Thompson and Paul Ogilvie and Yi Zhang and Jamie Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Information Filtering, Novelty Detection, and Named-Page Finding},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cmu.collins-thompson.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Collins-ThompsonOZC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT at TREC 2002 Linear Combinations Based on Document Structure  and Varied Stemming for Arabic Retrieval

_Abdur Chowdhury, Mohammed Aljlayl, Eric C. Jensen, Steven M. Beitzel, David A. Grossman, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [IIT](./web/participants.md#iit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/iit.grossman.pdf](http://trec.nist.gov/pubs/trec11/papers/iit.grossman.pdf)
- :material-file-search: **Runs:** [iit02b](./web/runs.md#iit02b) | [iit02tf](./web/runs.md#iit02tf) | [iit02tfa](./web/runs.md#iit02tfa)

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

#### Homepage Finding and Topic Distillation Using a Common Retrieval Strategy

_Vo Ngoc Anh, Alistair Moffat_

- :fontawesome-solid-user-group: **Participant:** [UMelbourne](./web/participants.md#umelbourne)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/umelbourne.moffat.pdf](http://trec.nist.gov/pubs/trec11/papers/umelbourne.moffat.pdf)
- :material-file-search: **Runs:** [MU106](./web/runs.md#mu106) | [MU307](./web/runs.md#mu307) | [MU208](./web/runs.md#mu208) | [MU609](./web/runs.md#mu609) | [MU80A](./web/runs.md#mu80a) | [MU111](./web/runs.md#mu111) | [MU212](./web/runs.md#mu212) | [MU313](./web/runs.md#mu313) | [MU525](./web/runs.md#mu525) | [MU624](./web/runs.md#mu624)

??? abstract "Abstract"
	
	For the TREC-2002 web track the University of Melbourne experimented with a system designed primarily for topic relevance tasks, and applied it directly to the homepage finding and topic distillation tasks. Our intention was to process queries regardless of their classification, as discriminating information may be unavailable in practice. An integer-valued weighting scheme reported in earlier work was employed, modified to take into account anchor text and many of the metadata fields, but not the URL text, and not the link structure information. Our experiments were carried out using a distributed retrieval system, with data spread across a sixteen node cluster. Indexing and query processing is fast, and the total index size is small.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnhM02.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnhM02,
		author = {Vo Ngoc Anh and Alistair Moffat},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Homepage Finding and Topic Distillation Using a Common Retrieval Strategy},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/umelbourne.moffat.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnhM02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC 2002: Web Track

_Anis Benammar, Mohand Boughanem, Gilles Hubert, Cecile Laffaire, Josiane Mothe_

- :fontawesome-solid-user-group: **Participant:** [irit](./web/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/irit.web.pdf](http://trec.nist.gov/pubs/trec11/papers/irit.web.pdf)
- :material-file-search: **Runs:** [MercureLynx](./web/runs.md#mercurelynx) | [Mercah](./web/runs.md#mercah) | [Mercure](./web/runs.md#mercure)

??? abstract "Abstract"
	
	The tests we performed for TREC'2002 web track focus on the web distillation part. The aim of our participation is to experiment our method for topic distillation combined with a new version of our system Mercure and to validate our system on a large collection of web pages: 18 Go of data. This year, three runs were submitted to NIST.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BenammarBHLM02.bib) "
	```
	@inproceedings{DBLP:conf/trec/BenammarBHLM02,
		author = {Anis Benammar and Mohand Boughanem and Gilles Hubert and Cecile Laffaire and Josiane Mothe},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IRIT} at {TREC} 2002: Web Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/irit.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BenammarBHLM02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LIT at TREC 2002: Web Track

_Nie Yu, Dong-Hong Ji, Lingpeng Yang_

- :fontawesome-solid-user-group: **Participant:** [lit](./web/participants.md#lit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/lit.donghong.pdf](http://trec.nist.gov/pubs/trec11/papers/lit.donghong.pdf)
- :material-file-search: **Runs:** [litlink](./web/runs.md#litlink) | [littext](./web/runs.md#littext)

??? abstract "Abstract"
	
	In Trec-2002, we participated in the Web Trec (named page finding task). There are two kinds of information that can be used while finding the expected page, content information and link information. We exploited both of them. That is to say, our system is content-based and link-based. As to link information, we only used anchor text and connections, and topology between pages is ignored. We submitted two runs. One is based on traditional contented-based retrieval, the other try to combine content-based retrieval and link-based retrieval to get better result.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YuDL02.bib) "
	```
	@inproceedings{DBLP:conf/trec/YuDL02,
		author = {Nie Yu and Dong{-}Hong Ji and Lingpeng Yang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{LIT} at {TREC} 2002: Web Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/lit.donghong.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YuDL02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 11 Experiments at CAS-ICT: Filtering and Web

_Hongbo Xu, Zhifeng Yang, Bin Wang, Bin Liu, Jun Cheng, Yue Liu, Zhe Yang, Xueqi Cheng, Shuo Bai_

- :fontawesome-solid-user-group: **Participant:** [chinese_academy](./web/participants.md#chinese_academy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cas_final.hongbo.pdf](http://trec.nist.gov/pubs/trec11/papers/cas_final.hongbo.pdf)
- :material-file-search: **Runs:** [ictnp4](./web/runs.md#ictnp4) | [ictnp3](./web/runs.md#ictnp3) | [ictnp2](./web/runs.md#ictnp2) | [icttd2](./web/runs.md#icttd2) | [icttd1](./web/runs.md#icttd1) | [icttd3](./web/runs.md#icttd3) | [ictnp7](./web/runs.md#ictnp7) | [ictnp6](./web/runs.md#ictnp6)

??? abstract "Abstract"
	
	CAS-ICT took part in the TREC conference for the second time this year and we undertook two tracks of TREC-11. For filtering track, we have submitted results of all three subtasks. In adaptive filtering, we paid more attention to undetermined documents processing, profile building and adaptation. In batch filtering and routing, a centroid-based classifier is used with preprocessed samples. For Web track, we have submitted results of both two subtasks. Different factors are considered to improve the overall performance of our Web systems. This paper describes our methods in detail.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuYWLCLYCB02.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuYWLCLYCB02,
		author = {Hongbo Xu and Zhifeng Yang and Bin Wang and Bin Liu and Jun Cheng and Yue Liu and Zhe Yang and Xueqi Cheng and Shuo Bai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 11 Experiments at {CAS-ICT:} Filtering and Web},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cas\_final.hongbo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuYWLCLYCB02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC 2002: Filtering, Q&A, Web and Video Tasks

_Lide Wu, Xuanjing Huang, Junyu Niu, Yingju Xia, Zhe Feng, Yaqian Zhou_

- :fontawesome-solid-user-group: **Participant:** [Fudan](./web/participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf](http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf)
- :material-file-search: **Runs:** [fduwt11o1](./web/runs.md#fduwt11o1) | [fduwt11o2](./web/runs.md#fduwt11o2) | [fduwt11t2](./web/runs.md#fduwt11t2) | [fduwt11t1](./web/runs.md#fduwt11t1) | [fduwt11b0](./web/runs.md#fduwt11b0)

??? abstract "Abstract"
	
	This year Fudan University takes part in the TREC conference for the third time. We have participated in four tracks of Filtering, Q&A, Web and Video. For filtering, we only participate in the sub-task of adaptive filtering. A novel method is presented, in which a winnow classifier from the description and narrative fields is constructed, and then utilized to assist our previous adaptive filtering system. A novel approach to confidence sorting, which is based on Maximum Entropy, is proposed in our Question Answering system. The rank of individual answer is determined by several weighted factors, and the confidence score is the product of the exponent of the weights of every factors. The weight of every factor is assigned during the training of previous questions. To return highly relevant key resources for web retrieval, we modified our original search system to make it return higher precision result than before. First, we proposed a novel search algorithm to get a base set of highly relevant documents. Then special post-processing modules are used to expand and re-sort the base set. This year we tried a fast manifold-based approach to face recognition in the Video Search Task. It can be used when there are only few different images of a specific person and runs fast. Experiment shows that applying this step will make the face recognition 5-fold faster and with almost no decreasing of performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHNXFZ02.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHNXFZ02,
		author = {Lide Wu and Xuanjing Huang and Junyu Niu and Yingju Xia and Zhe Feng and Yaqian Zhou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FDU} at {TREC} 2002: Filtering, Q{\&}A, Web and Video Tasks},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHNXFZ02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Named Page Finding and Arabic Retrieval with Hummingbird  SearchServerTM at TREC 2002

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird](./web/participants.md#hummingbird)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/hummingbird.tomlinson.pdf](http://trec.nist.gov/pubs/trec11/papers/hummingbird.tomlinson.pdf)
- :material-file-search: **Runs:** [hum02upd](./web/runs.md#hum02upd) | [hum02pd](./web/runs.md#hum02pd) | [hum02ud](./web/runs.md#hum02ud) | [hum02up](./web/runs.md#hum02up) | [hum02uhp](./web/runs.md#hum02uhp)

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

#### TREC 2002 Web Track "Automated Word Sense Disambiguation for Internet  Information Retrieval"

_Christopher Stokoe, John Tait_

- :fontawesome-solid-user-group: **Participant:** [dgic_stokoe](./web/participants.md#dgic_stokoe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/usunderland.stokoe.pdf](http://trec.nist.gov/pubs/trec11/papers/usunderland.stokoe.pdf)
- :material-file-search: **Runs:** [TDtfidf](./web/runs.md#tdtfidf) | [TDwsdtfidf](./web/runs.md#tdwsdtfidf)

??? abstract "Abstract"
	
	We describe an attempt to use automated word sense disambiguation to improve the performance of an internet information retrieval system. A performance comparison of term frequency verses word sense frequency was carried out, the results of which indicated no significant performance gains from using a sense based retrieval model instead of the traditional TF*IDF.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StokoeT02.bib) "
	```
	@inproceedings{DBLP:conf/trec/StokoeT02,
		author = {Christopher Stokoe and John Tait},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2002 Web Track "Automated Word Sense Disambiguation for Internet Information Retrieval"},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/usunderland.stokoe.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StokoeT02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Web Document Retrieval Using Sentence-Query Similarity

_Eui-Kyu Park, Seong-In Moon, Dong-Yul Ra, Myung-Gil Jang_

- :fontawesome-solid-user-group: **Participant:** [yonsei](./web/participants.md#yonsei)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/yonsei.ra.pdf](http://trec.nist.gov/pubs/trec11/papers/yonsei.ra.pdf)
- :material-file-search: **Runs:** [yenp01](./web/runs.md#yenp01) | [yedi01](./web/runs.md#yedi01) | [yedi01no](./web/runs.md#yedi01no)

??? abstract "Abstract"
	
	For the web document retrieval experiments in our TREC '2002 participation, we used two new methods. One is the use of anchor texts, which has been advocated by many researchers. But the methods used by them is different from our method. The second is the use of sentence-query similarity. It has been known that the use of links for web retrieval did not show impressive improvement in performance [5,6,8,9]. But Bailey, etc. [1] reported that using anchor texts can improve retrieval performance. However, our home page finding experiment done for TREC '2001 showed that it is not the case. The use of anchor texts did not allow any improvement in performance. Our method to use the anchor texts this year is changed a lot from last year and found that it is pretty effective. The major focus of our experiment this year is in the use of sentential information in information retrieval. We obtain similarity values between sentences of a document and the query and use them for computing the retrieval score of the document. The main idea is the following: a sentence in a document that is much relevant to the query can support relevance of the document to the query. We compute the similarity between each sentence in the document and the query. The degree of this similarity is incorporated in calculating the document's score (in addition to the similarity between the document as a whole and the query). It has been found that it does not take too much time for this extra processing. Our experiment showed that including the sentential information in the proposed way can significantly improve retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ParkMRJ02.bib) "
	```
	@inproceedings{DBLP:conf/trec/ParkMRJ02,
		author = {Eui{-}Kyu Park and Seong{-}In Moon and Dong{-}Yul Ra and Myung{-}Gil Jang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Web Document Retrieval Using Sentence-Query Similarity},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/yonsei.ra.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ParkMRJ02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at TREC 2002

_Christof Monz, Jaap Kamps, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [uva](./web/participants.md#uva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uamsterdam.derijke.pdf](http://trec.nist.gov/pubs/trec11/papers/uamsterdam.derijke.pdf)
- :material-file-search: **Runs:** [UAmsT02WnA](./web/runs.md#uamst02wna) | [UAmsT02WnTl](./web/runs.md#uamst02wntl) | [UAmsT02WnTlA](./web/runs.md#uamst02wntla) | [UAmsT02WnTm](./web/runs.md#uamst02wntm) | [UAmsT02WnTmA](./web/runs.md#uamst02wntma) | [UAmsT02WtA](./web/runs.md#uamst02wta) | [UAmsT02WtAcs](./web/runs.md#uamst02wtacs) | [UAmsT02WtAri](./web/runs.md#uamst02wtari) | [UAmsT02WtT](./web/runs.md#uamst02wtt) | [UAmsT02WtTri](./web/runs.md#uamst02wttri)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2002 Novelty, Question answering, and Web tracks. We provide a detailed account of the ideas underlying our approaches to these tasks. All our runs used the FlexIR information retrieval system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MonzKR02.bib) "
	```
	@inproceedings{DBLP:conf/trec/MonzKR02,
		author = {Christof Monz and Jaap Kamps and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Amsterdam at {TREC} 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/uamsterdam.derijke.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MonzKR02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Finding Named Pages via Frequent Anchor Descriptions

_J. Malawong, Arnon Rungsawang_

- :fontawesome-solid-user-group: **Participant:** [kasetsart](./web/participants.md#kasetsart)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/kasetsart.malawong.pdf](http://trec.nist.gov/pubs/trec11/papers/kasetsart.malawong.pdf)
- :material-file-search: **Runs:** [KUHPF0201](./web/runs.md#kuhpf0201)

??? abstract "Abstract"
	
	This article describes about finding documents of interest via frequent anchor descriptions that being derived from the 'gov' web collection. The main idea of our approach is that we consider frequent anchor descriptions as documents. To find out the frequent item sets, we apply the Apri-ori algorithm with a new scoring criterion, called the maximum correspondence. We likewise integrate both retrieval scores calculated from anchor descriptions and title texts of the web pages to identify the resulting named pages, and foundthat these combination scores can boost the precision performance. Concluded from our preliminary experiments, this approach yields a considerable efficiency of named page finding in the aspect that it also highly reduces the document search space.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MalawongR02.bib) "
	```
	@inproceedings{DBLP:conf/trec/MalawongR02,
		author = {J. Malawong and Arnon Rungsawang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Finding Named Pages via Frequent Anchor Descriptions},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/kasetsart.malawong.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MalawongR02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Pliers at Trec 2002

_Andy MacFarlane_

- :fontawesome-solid-user-group: **Participant:** [city-pliers](./web/participants.md#city-pliers)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cityu.pliers.pdf](http://trec.nist.gov/pubs/trec11/papers/cityu.pliers.pdf)
- :material-file-search: **Runs:** [pltr02wt1](./web/runs.md#pltr02wt1) | [pltr02wt2](./web/runs.md#pltr02wt2) | [pltr02wt3](./web/runs.md#pltr02wt3) | [pltr02wt4](./web/runs.md#pltr02wt4) | [pltr02wt5](./web/runs.md#pltr02wt5) | [pltr02wt6](./web/runs.md#pltr02wt6) | [pltr02wt7](./web/runs.md#pltr02wt7) | [pltr02wt8](./web/runs.md#pltr02wt8) | [pltr02wt9](./web/runs.md#pltr02wt9)

??? abstract "Abstract"
	
	We report on our experiments for the TREC 2002 web track for both the topic distillation and named page tasks. We use a very simple method for both tasks which takes the first hit page in the top 10 for a give web site and discards any further pages from that web site (section 2 describes our research aims and objectives in more detail). We also describe indexing results (section 3), give a description of the runs and settings used (section 4), briefly describe our retrieval efficiency results in section 5, and outline our retrieval efficiency results in sections 6 and 7. A conclusion is given in section 8.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacFarlane02.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacFarlane02,
		author = {Andy MacFarlane},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Pliers at Trec 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cityu.pliers.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacFarlane02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 11 Experiment: Arabic, Named Page and Topic Distillation  Searches

_Jacques Savoy, Yves Rasolofo_

- :fontawesome-solid-user-group: **Participant:** [Neuchatel](./web/participants.md#neuchatel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uneuchatel.pdf](http://trec.nist.gov/pubs/trec11/papers/uneuchatel.pdf)
- :material-file-search: **Runs:** [UniNEnp1](./web/runs.md#uninenp1) | [UniNEnp2](./web/runs.md#uninenp2) | [UniNEnp4](./web/runs.md#uninenp4) | [UniNEnp3](./web/runs.md#uninenp3) | [UniNEdi5](./web/runs.md#uninedi5) | [UniNEdi1](./web/runs.md#uninedi1) | [UniNEdi4](./web/runs.md#uninedi4) | [UniNEdi2](./web/runs.md#uninedi2) | [UniNEdi3](./web/runs.md#uninedi3)

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

#### Topic Distillation with Knowledge Agents

_Einat Amitay, David Carmel, Adam Darlow, Ronny Lempel, Aya Soffer_

- :fontawesome-solid-user-group: **Participant:** [IBM-Haifa](./web/participants.md#ibm-haifa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ibm-haifa.pdf](http://trec.nist.gov/pubs/trec11/papers/ibm-haifa.pdf)
- :material-file-search: **Runs:** [ibmHaifaBase](./web/runs.md#ibmhaifabase) | [ibmHaifaAP](./web/runs.md#ibmhaifaap) | [ibmHaifaT10](./web/runs.md#ibmhaifat10) | [ibmHaifaPR](./web/runs.md#ibmhaifapr) | [ibmHaifaT10D](./web/runs.md#ibmhaifat10d)

??? abstract "Abstract"
	
	This is the second year that our group participates in TREC's Web track. Our experiments focused on the Topic distillation task. Our main goal was to experiment with the Knowledge Agent (KA) technology [1], previously developed at our Lab, for this particular task. The knowledge agent approach was designed to enhance Web search results by utilizing domain knowledge. We first describe the generic KA approach and then articulate on the use of this technology in the context of the topic distillation task. We focus mainly on the Knowledge Agent features that were used in this task. The rest of this paper is organized as follows: Section 2 describes KA in general. In Section 3 we describe how KA was used for the topic distillation experiment. Section 4 describes the obtained results. Section 5 concludes.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmitayCDLS02.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmitayCDLS02,
		author = {Einat Amitay and David Carmel and Adam Darlow and Ronny Lempel and Aya Soffer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Topic Distillation with Knowledge Agents},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/ibm-haifa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AmitayCDLS02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Question Answering 

#### Overview of the TREC 2002 Question Answering Track

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/QA11.pdf](http://trec.nist.gov/pubs/trec11/papers/QA11.pdf)
??? abstract "Abstract"
	
	The TREC question answering track is an effort to bring the benefits of large-scale evaluation to bear on the question answering problem. The track contained two tasks in TREC 2002, the main task and the list task. Both tasks required that the answer strings returned by the systems consist of nothing more or less than an answer in contrast to the text snippets containing an answer allowed in previous years. A new evaluation measure in the main task, the confidence-weighted score, tested a system's ability to recognize when it has found a correct answer.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees02a.bib) "
	```
	@inproceedings{DBLP:conf/trec/Voorhees02a,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2002 Question Answering Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/QA11.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees02a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Web Based Pattern Mining and Matching Approach to Question Answering

_Dell Zhang, Wee Sun Lee_

- :fontawesome-solid-user-group: **Participant:** [singapore](./qa/participants.md#singapore)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/nus.web.zhang.pdf](http://trec.nist.gov/pubs/trec11/papers/nus.web.zhang.pdf)
- :material-file-search: **Runs:** [nuslamp2002](./qa/runs.md#nuslamp2002)

??? abstract "Abstract"
	
	We describe herein a Web based pattern mining and matching approach to question answering. For each type of questions, a lot of textual patterns can be learned from the Web automatically, using the TREC QA track data as training examples. These textual patterns are assessed by the concepts of support and confidence, which are borrowed from the data mining community. Given a new unseen question, these textual patterns can be utilized to extract and rank the plausible answers on the Web. The performance of this approach has been evaluated also by the TREC QA track data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangL02.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangL02,
		author = {Dell Zhang and Wee Sun Lee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Web Based Pattern Mining and Matching Approach to Question Answering},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/nus.web.zhang.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangL02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Natural Language Based Reformulation Resource and Wide Exploitation  for Question Answering

_Ulf Hermjakob, Abdessamad Echihabi, Daniel Marcu_

- :fontawesome-solid-user-group: **Participant:** [usc-isi](./qa/participants.md#usc-isi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/usc.hermjakob.pdf](http://trec.nist.gov/pubs/trec11/papers/usc.hermjakob.pdf)
- :material-file-search: **Runs:** [isi02](./qa/runs.md#isi02) | [ilv02t](./qa/runs.md#ilv02t) | [ilv02wt](./qa/runs.md#ilv02wt)

??? abstract "Abstract"
	
	We describe and evaluate how a generalized natural language based reformulation resource in our TextMap question answering system improves web exploitation and answer pinpointing. The reformulation resource, which can be viewed as a clausal extension of WordNet, supports high-precision syntactic and semantic reformulations of questions and other sentences, as well as inferencing and answer generation. The paper shows in some detail how these reformulations can be used to overcome challenges and benefit from the advantages of using the Web.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HermjakobEM02.bib) "
	```
	@inproceedings{DBLP:conf/trec/HermjakobEM02,
		author = {Ulf Hermjakob and Abdessamad Echihabi and Daniel Marcu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Natural Language Based Reformulation Resource and Wide Exploitation for Question Answering},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/usc.hermjakob.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HermjakobEM02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM's Statistical Question Answering System-TREC 11

_Abraham Ittycheriah, Salim Roukos_

- :fontawesome-solid-user-group: **Participant:** [ibm-abe](./qa/participants.md#ibm-abe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ibm.ittycheriah.pdf](http://trec.nist.gov/pubs/trec11/papers/ibm.ittycheriah.pdf)
- :material-file-search: **Runs:** [ibmsqa02a](./qa/runs.md#ibmsqa02a) | [ibmsqa02b](./qa/runs.md#ibmsqa02b) | [ibmsqa02c](./qa/runs.md#ibmsqa02c)

??? abstract "Abstract"
	
	In this paper, we document our efforts to extend our statistical question answering system for TREC-11. We incorporated a web search feature, and novel extensions of statistical machine translation as well as extracting lexical patterns for exact answers from a supervised corpus. Without modification to our base set of thirty-one categories, we were able to achieve a confidence weighted score of 0.455 and an accuracy of 29%. We improved our model on selecting exact answers by insisting on exact answers in the training corpus and this resulted in a 7% gain on TREC-11 but a much larger gain of 46% on TREC-10.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/IttycheriahR02.bib) "
	```
	@inproceedings{DBLP:conf/trec/IttycheriahR02,
		author = {Abraham Ittycheriah and Salim Roukos},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {IBM's Statistical Question Answering System-TREC 11},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/ibm.ittycheriah.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/IttycheriahR02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Machine Learning Approach for QA and Novelty Tracks: NTT System  Description

_Hideto Kazawa, Tsutomu Hirao, Hideki Isozaki, Eisaku Maeda_

- :fontawesome-solid-user-group: **Participant:** [nttcom_kazawa](./qa/participants.md#nttcom_kazawa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/nttcom.pdf](http://trec.nist.gov/pubs/trec11/papers/nttcom.pdf)
- :material-file-search: **Runs:** [nttcs11qam](./qa/runs.md#nttcs11qam)

??? abstract "Abstract"
	
	In one sense, the goals of QA and Novelty tasks are the same: extracting small document parts which are relevant to users' queries. Additionally, the unit of extraction is almost always fixed in both tasks. For QA, an answer is a noun phrase in most cases, and for Novelty, a sentence is recognized as the basic information unit. This observation leads us to the following unified approach to both QA and Novelty tasks: first identify information units in documents, then judge whether each unit is relevant to the query. This two step approach is amenable to machine learning methods because each step can be cast as a classification problem. For example, noun phrase identification can be achieved by classifying each word into the start/middle/end/exterior of a noun phrase; sentence identification by classifying whether each period marks the of a sentence. Additionally, relevance judgment can be regarded as the classification of a pair of query and an information unit into a relevant-pair or non-relevant-pair. In QA and Novelty Tracks at TREC 2002, we studied the feasibility of this two step approach, using Support Vector Machines as the learning algorithm of the classifiers. Since many studies on identifying information units have already been reported, we concentrate on the relevance judgment step in QA and Novelty tasks in this paper
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KazawaHIM02.bib) "
	```
	@inproceedings{DBLP:conf/trec/KazawaHIM02,
		author = {Hideto Kazawa and Tsutomu Hirao and Hideki Isozaki and Eisaku Maeda},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Machine Learning Approach for {QA} and Novelty Tracks: {NTT} System Description},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/nttcom.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KazawaHIM02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Extracting Answers from the Web Using Data Annotation and Knowledge  Mining Techniques

_Jimmy Lin, Aaron Fernandes, Boris Katz, Gregory Marton, Stefanie Tellex_

- :fontawesome-solid-user-group: **Participant:** [mit_lin](./qa/participants.md#mit_lin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/mit.lin.pdf](http://trec.nist.gov/pubs/trec11/papers/mit.lin.pdf)
- :material-file-search: **Runs:** [aranea02a](./qa/runs.md#aranea02a) | [aranea02pc3](./qa/runs.md#aranea02pc3) | [aranea02pbq](./qa/runs.md#aranea02pbq)

??? abstract "Abstract"
	
	Aranea is a question answering system that extracts answers from the World Wide Web using knowledge annotation and knowledge mining techniques. Knowledge annotation, which utilizes semistructured database techniques, is effective for answering large classes of commonly occurring questions. Knowledge mining, which utilizes statistical techniques, can leverage the massive amounts of data available on the Web to overcome many natural language processing challenges. Aranea integrates these two different paradigms of question answering into a single framework. For the TREC evaluation, we also explored the problem of answer projection, or finding supporting documents for our Web-derived answers from the AQUAINT corpus.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinFKMT02.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinFKMT02,
		author = {Jimmy Lin and Aaron Fernandes and Boris Katz and Gregory Marton and Stefanie Tellex},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Extracting Answers from the Web Using Data Annotation and Knowledge Mining Techniques},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/mit.lin.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LinFKMT02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering Using XML-Tagged Documents

_Kenneth C. Litkowski_

- :fontawesome-solid-user-group: **Participant:** [clresearch](./qa/participants.md#clresearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/clresearch.litkowski.pdf](http://trec.nist.gov/pubs/trec11/papers/clresearch.litkowski.pdf)
- :material-file-search: **Runs:** [clr02l1](./qa/runs.md#clr02l1) | [clr02l2](./qa/runs.md#clr02l2) | [clr02l3](./qa/runs.md#clr02l3) | [clr02b2](./qa/runs.md#clr02b2) | [clr02b1](./qa/runs.md#clr02b1)

??? abstract "Abstract"
	
	The official submission for CL Research's question-answering system (DIMAP-QA) for TREC-11 only slightly extends its semantic relation triple (logical form) technology in which documents are fully parsed and databases built around discourse entities. We were unable to complete the planned revision of our system based on a fuller discourse analysis of the texts. We have since implemented many of these changes and can now report preliminary and encouraging results of basing our system on XML markup of texts with syntactic and semantic attributes and use of XML stylesheet functionality (specifically, XPath expressions) to answer questions. The official confidence-weighted score for the main TREC-11 QA task was 0.049, based on processing 20 of the top 50 documents provided by NIST. Our estimated mean reciprocal rank was 0.128 for the exact answers and 0.227 for sentence answers, comparable to our results from previous years. With our revised XML-based system, using a 20 percent sample of the TREC questions, we have an estimated confidence-weighted score of 0.869 and mean reciprocal rank of 0.828. We describe our system and examine the results from XML tagging in terms of question-answering and other applications such as information extraction, text summarization, novelty studies, and investigation of linguistic phenomena.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Litkowski02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Litkowski02,
		author = {Kenneth C. Litkowski},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering Using XML-Tagged Documents},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/clresearch.litkowski.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Litkowski02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Sheffield TREC 2002 Q&A System

_Mark A. Greenwood, Ian Roberts, Robert J. Gaizauskas_

- :fontawesome-solid-user-group: **Participant:** [sheffield](./qa/participants.md#sheffield)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/sheffield.greenwood.pdf](http://trec.nist.gov/pubs/trec11/papers/sheffield.greenwood.pdf)
- :material-file-search: **Runs:** [sheft11lo](./qa/runs.md#sheft11lo) | [sheft11log](./qa/runs.md#sheft11log) | [sheft11mo3](./qa/runs.md#sheft11mo3) | [sheft11mog3](./qa/runs.md#sheft11mog3) | [sheft11mog1](./qa/runs.md#sheft11mog1)

??? abstract "Abstract"
	
	The system entered by the University of Sheffield in the question answering track of TREC 2002 represents a significant development over the Sheffield system entered into TREC-8 [9] and TREC-9 [15], although the underlying architecture remains the same. The essence of the approach is to pass the question to an information retrieval (IR) system which uses it as a query to do passage retrieval against the text collection. The top ranked passages output from the IR system are then passed to a modified information extraction (IE) system. Syntactic and semantic analysis of these passages, along with the question, is carried out to identify the “sought entity” from the question and to score potential matches for this sought entity in each of the retrieved passages. The potential matches are then combined or discarded based on a number of criteria. The highest scoring match is then proposed as the answer to the question
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GreenwoodRG02.bib) "
	```
	@inproceedings{DBLP:conf/trec/GreenwoodRG02,
		author = {Mark A. Greenwood and Ian Roberts and Robert J. Gaizauskas},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Sheffield {TREC} 2002 Q{\&}A System},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/sheffield.greenwood.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GreenwoodRG02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Alicante Experiments at TREC 2002

_José Luis Vicedo González, Fernando Llopis, Antonio Ferrández Rodríguez_

- :fontawesome-solid-user-group: **Participant:** [Alicante](./qa/participants.md#alicante)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ualicante.vicedo.pdf](http://trec.nist.gov/pubs/trec11/papers/ualicante.vicedo.pdf)
- :material-file-search: **Runs:** [ali2002b](./qa/runs.md#ali2002b)

??? abstract "Abstract"
	
	This paper describes the architecture, operation and results obtained with the Question Answering prototype developed in the Department of Language Processing and Information Systems at the University of Alicante. This system is based on our TREC-10 approach where different improvements have been introduced. Main modifications reside on the introduction of a filtering stage into paragraph selection and answer extraction modules that allow the treatment of questions with no answer in the document collection. Moreover, WordNet has been enhanced by adding a collection of gazetteers that includes several types of proper nouns (people, organisations, and places) and a large variety of acronyms, measure and money units.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GonzalezLR02.bib) "
	```
	@inproceedings{DBLP:conf/trec/GonzalezLR02,
		author = {Jos{\'{e}} Luis Vicedo Gonz{\'{a}}lez and Fernando Llopis and Antonio Ferr{\'{a}}ndez Rodr{\'{\i}}guez},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Alicante Experiments at {TREC} 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/ualicante.vicedo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GonzalezLR02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Novel Results and Some Answers - The University of Iowa TREC 11  Results

_David Eichmann, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [uiowa](./qa/participants.md#uiowa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uiowa.eichmann.pdf](http://trec.nist.gov/pubs/trec11/papers/uiowa.eichmann.pdf)
- :material-file-search: **Runs:** [UIowaQA0201](./qa/runs.md#uiowaqa0201) | [UIowaQA0202](./qa/runs.md#uiowaqa0202) | [UIowaQA0203](./qa/runs.md#uiowaqa0203)

??? abstract "Abstract"
	
	The University of Iowa participated in the novelty, adaptive filtering and question answering tracks of TREC-11. The filtering system used was an extension of the one used in TREC-7 [1] and TREC-8 [2]. Question answering was derived from the TREC-10 system. The novelty system was new...
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannS02.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannS02,
		author = {David Eichmann and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Novel Results and Some Answers - The University of Iowa {TREC} 11 Results},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/uiowa.eichmann.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannS02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering: CNLP at the TREC 2002 Question Answering Track

_Anne Diekema, Jiangping Chen, Nancy J. McCracken, Necati Ercan Ozgencil, Mary D. Taffet, Özgür Yilmazel, Elizabeth D. Liddy_

- :fontawesome-solid-user-group: **Participant:** [syracuse](./qa/participants.md#syracuse)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/syracuse.diekema.pdf](http://trec.nist.gov/pubs/trec11/papers/syracuse.diekema.pdf)
- :material-file-search: **Runs:** [SUT11IR1MT](./qa/runs.md#sut11ir1mt) | [SUT11IR1LT](./qa/runs.md#sut11ir1lt) | [SUT11IR1LT2](./qa/runs.md#sut11ir1lt2)

??? abstract "Abstract"
	
	This paper describes the retrieval experiments for the main task and list task of the TREC-2002 question-answering track. The question answering system described automatically finds answers to questions in a large document collection. The system uses a two-stage retrieval approach to answer finding based on matching of named entities, linguistic patterns, keywords, and the use of a new inference module. In answering a question, the system carries out a detailed query analysis that produces a logical query representation, an indication of the question focus, and answer clue words.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DiekemaCMOTYL02.bib) "
	```
	@inproceedings{DBLP:conf/trec/DiekemaCMOTYL02,
		author = {Anne Diekema and Jiangping Chen and Nancy J. McCracken and Necati Ercan Ozgencil and Mary D. Taffet and {\"{O}}zg{\"{u}}r Yilmazel and Elizabeth D. Liddy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering: {CNLP} at the {TREC} 2002 Question Answering Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/syracuse.diekema.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DiekemaCMOTYL02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Statistical Selection of Exact Answers (MultiText Experiments for  TREC 2002)

_Charles L. A. Clarke, Gordon V. Cormack, Graeme Kemkes, M. Laszlo, Thomas R. Lynam, Egidio L. Terra, Philip L. Tilker_

- :fontawesome-solid-user-group: **Participant:** [waterloo](./qa/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uwaterloo.clarke.pdf](http://trec.nist.gov/pubs/trec11/papers/uwaterloo.clarke.pdf)
- :material-file-search: **Runs:** [uwmtB1](./qa/runs.md#uwmtb1) | [uwmtB2](./qa/runs.md#uwmtb2) | [uwmtB3](./qa/runs.md#uwmtb3)

??? abstract "Abstract"
	
	For TREC 2002, the MultiText Group concentrated on the QA track. We also submitted runs for the Web track. Building on the work of previous years, our TREC 2002 QA system takes a statistical approach to answer selection, supported by a lightweight parser that performs question categorization and query genera-tion. Answer candidates are extracted from passages retrieved by an algorithm that identifies short text fragments containing weighted combinations of query terms. If the parser is able to assign one of a predetermined set of question categories to a question, the system employs a finite-state pattern recognizer to extract answer candidates. Otherwise, one- to five-word n-grams from the passages are used. Our system assumes that an answer to every question appears in the TREC corpus, and it produces a NIL result only in a few rare circumstances. Despite the simplicity of the approach, our best QA run returned correct answers to 37% of the questions. Our basic question answering strategy is an extension of the technique we used for both TREC 2000 and 2001 5]. In past years, our system ranked individual terms appearing in retrieved passages and selected 50-byte responses from the passages that included one or more of the highest ranking terms. Since exact answers are required for TREC 2002, much of our effort this year was focused on the extension of this technique to multi-term exact-answer candidates. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeCKLLTT02.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeCKLLTT02,
		author = {Charles L. A. Clarke and Gordon V. Cormack and Graeme Kemkes and M. Laszlo and Thomas R. Lynam and Egidio L. Terra and Philip L. Tilker},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Statistical Selection of Exact Answers (MultiText Experiments for {TREC} 2002)},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/uwaterloo.clarke.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeCKLLTT02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Multi-Strategy and Multi-Source Approach to Question Answering

_Jennifer Chu-Carroll, John M. Prager, Christopher A. Welty, Krzysztof Czuba, David A. Ferrucci_

- :fontawesome-solid-user-group: **Participant:** [ibm_prager](./qa/participants.md#ibm_prager)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ibm.prager.pdf](http://trec.nist.gov/pubs/trec11/papers/ibm.prager.pdf)
- :material-file-search: **Runs:** [IBMPQ](./qa/runs.md#ibmpq) | [IBMPQSQA](./qa/runs.md#ibmpqsqa) | [IBMPQSQACYC](./qa/runs.md#ibmpqsqacyc)

??? abstract "Abstract"
	
	Traditional question answering systems typically employ a single pipeline architecture, consisting roughly of three components: question analysis, search, and answer selection (see e.g., (Clarke et al., 2001a; Hovy et al., 2000; Moldovan et al., 2000; Prager et al., 2000)). The knowledge sources utilized by these systems to date primarily focus on the corpus from which answers are to be retrieved, WordNet, and the Web (see e.g., (Clarke et al., 2001b; Pasca and Harabagiu, 2001; Prager et al., 2001)). More recent research has shown that introducing feedback loops into the traditional pipeline architecture results in a performance gain (Harabagiu et al., 2001). We are interested in improving the performance of QA systems by breaking away from the strict pipeline architecture. In addition, we require an architecture that allows for hybridization at low development cost and facilitates experimentation with different instantiations of system components. Our resulting architecture is one that is modular and easily extensible, and allows for multiple answering agents to address the same question in parallel and for their results to be combined. Our new question answering system, PIQUANT, adopts this flexible architecture. The answering agents currently implemented in PIQUANT vary both in terms of the strategies used and the knowledge sources consulted. For example, an answering agent may employ statistical methods for extracting answers to questions from a large corpus, while another answering agent may transform select natural language questions into logical forms and query structured knowledge sources for answers. In this paper, we first describe the architecture on which PIQUANT is based. We then describe the answering agents currently implemented within the PIQUANT system, and how they were configured for our TREC2002 runs. Finally, we show that significant performance improvement was achieved by our multi-agent architecture by comparing our TREC2002 results against individual answering agent performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Chu-CarrollPWCF02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Chu-CarrollPWCF02,
		author = {Jennifer Chu{-}Carroll and John M. Prager and Christopher A. Welty and Krzysztof Czuba and David A. Ferrucci},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Multi-Strategy and Multi-Source Approach to Question Answering},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/ibm.prager.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Chu-CarrollPWCF02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MITRE's Qanda at TREC-11

_John D. Burger, Lisa Ferro, Warren R. Greiff, John C. Henderson, Scott A. Mardis, Alexander A. Morgan, Marc Light_

- :fontawesome-solid-user-group: **Participant:** [mitre](./qa/participants.md#mitre)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/mitre.burger.pdf](http://trec.nist.gov/pubs/trec11/papers/mitre.burger.pdf)
- :material-file-search: **Runs:** [MITRE2002B](./qa/runs.md#mitre2002b)

??? abstract "Abstract"
	
	Qanda is MITRE's TREC-style question answering system. Since last year's evaluation, principal improvements to the system have been aimed at making it faster and more robust. We discuss the current architecture of the system in Section 1. Some work has gone into better answer formation and ranking, which we discuss in Section 2. After this year's evaluation, we have done a number of ROVER-style system combination experiments using the judged answer strings made available by NIST. We report on some success with this in Section 3. We have also performed a detailed categorization of previous TREC results according to answer type and grammatical category, as well as an analysis of Qanda's own question analysis component—see Section 4 for these analyses.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BurgerFGHMML02.bib) "
	```
	@inproceedings{DBLP:conf/trec/BurgerFGHMML02,
		author = {John D. Burger and Lisa Ferro and Warren R. Greiff and John C. Henderson and Scott A. Mardis and Alexander A. Morgan and Marc Light},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {MITRE's Qanda at {TREC-11}},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/mitre.burger.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BurgerFGHMML02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The YorkQA Prototype Question Answering System

_Marco De Boni, José-Luis Jara-Valencia, Suresh Manandhar_

- :fontawesome-solid-user-group: **Participant:** [york](./qa/participants.md#york)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uyork.deboni.pdf](http://trec.nist.gov/pubs/trec11/papers/uyork.deboni.pdf)
- :material-file-search: **Runs:** [yorkqa01](./qa/runs.md#yorkqa01)

??? abstract "Abstract"
	
	A preliminary analysis of our QA system implemented for TREC-11 is presented, with an initial evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoniJM02.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoniJM02,
		author = {Marco De Boni and Jos{\'{e}}{-}Luis Jara{-}Valencia and Suresh Manandhar},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The YorkQA Prototype Question Answering System},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/uyork.deboni.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoniJM02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Coupling Named Entity Recognition, Vector-Space Model and Knowledge  Bases for TREC 11 Question Answering Track

_Patrice Bellot, Eric Crestan, Marc El-Bèze, Laurent Gillard, Claude de Loupy_

- :fontawesome-solid-user-group: **Participant:** [avignon](./qa/participants.md#avignon)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/lia.sinequa.pdf](http://trec.nist.gov/pubs/trec11/papers/lia.sinequa.pdf)
- :material-file-search: **Runs:** [LIA2002a](./qa/runs.md#lia2002a)

??? abstract "Abstract"
	
	In this paper, we present a question-answering system combining Named Entity Recognition, Vector-Space Model and Knowledge Bases to validate answers candidates. Applying this hybrid approach, for our first participation in the TREC Q&A.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BellotCEGL02.bib) "
	```
	@inproceedings{DBLP:conf/trec/BellotCEGL02,
		author = {Patrice Bellot and Eric Crestan and Marc El{-}B{\`{e}}ze and Laurent Gillard and Claude de Loupy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Coupling Named Entity Recognition, Vector-Space Model and Knowledge Bases for {TREC} 11 Question Answering Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/lia.sinequa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BellotCEGL02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PiQASso 2002

_Giuseppe Attardi, Antonio Cisternino, Francesco Formica, Maria Simi, Alessandro Tommasi_

- :fontawesome-solid-user-group: **Participant:** [Pisa](./qa/participants.md#pisa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/upisa.tommasi.pdf](http://trec.nist.gov/pubs/trec11/papers/upisa.tommasi.pdf)
- :material-file-search: **Runs:** [pqas21](./qa/runs.md#pqas21) | [pqas22](./qa/runs.md#pqas22) | [pqas23](./qa/runs.md#pqas23)

??? abstract "Abstract"
	
	The University of Pisa participated to TREC 2002's QA track with PiQASso, a vertical Q system developed (except for some of the linguistic tools), entirely within our research group at the Computer Science department. The system features a filter-and-loop architecture in which non-promising paragraphs are ruled out basing on features ranging from keyword matching to complex semantic relation matching. The system also exploits the Web in order to get 'hints' at what to look for in the internal collection. This article describes the system in its entire architecture, concentrating on the Web exploita-tion, providing figures of its efficacy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AttardiCFST02.bib) "
	```
	@inproceedings{DBLP:conf/trec/AttardiCFST02,
		author = {Giuseppe Attardi and Antonio Cisternino and Francesco Formica and Maria Simi and Alessandro Tommasi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {PiQASso 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/upisa.tommasi.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AttardiCFST02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mining Knowledge from Repeated Co-Occurrences: DIOGENE at TREC  2002

_Bernardo Magnini, Matteo Negri, Roberto Prevete, Hristo Tanev_

- :fontawesome-solid-user-group: **Participant:** [itc_irst](./qa/participants.md#itc_irst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/itcirst.magnini.pdf](http://trec.nist.gov/pubs/trec11/papers/itcirst.magnini.pdf)
- :material-file-search: **Runs:** [IRST02D1](./qa/runs.md#irst02d1) | [IRST02D2](./qa/runs.md#irst02d2) | [IRST02D3](./qa/runs.md#irst02d3)

??? abstract "Abstract"
	
	This paper presents a new version of the DIOGENE Question Answering (QA) system developed at ITC-Irst. With respect to our first participation to the TREC QA main task (TREC-2001), the system presents both improvements and extensions. On one hand, significant improvements rely on the substitution of basic components (e.g. the search engine and the tool in charge of the named entities recognition) with new modules that enhanced the overall system's performance. On the other hand, an effective extension of DIOGENE is represented by the introduction of a module for the automatic assessment of the candidate answers' quality. All the variations with respect to the first version of the system as well as the results obtained at the TREC-2002 QA main task are presented and discussed in the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MagniniNPT02.bib) "
	```
	@inproceedings{DBLP:conf/trec/MagniniNPT02,
		author = {Bernardo Magnini and Matteo Negri and Roberto Prevete and Hristo Tanev},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Mining Knowledge from Repeated Co-Occurrences: {DIOGENE} at {TREC} 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/itcirst.magnini.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MagniniNPT02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Question Answering System QALC at LIMSI, Experiments in Using  Web and WordNet

_Gaël de Chalendar, Tiphaine Dalmas, Faiïza Elkateb-Gara, Olivier Ferret, Brigitte Grau, Martine Hurault-Plantet, Gabriel Illouz, Laura Monceaux, Isabelle Robba, Anne Vilnat_

- :fontawesome-solid-user-group: **Participant:** [limsi](./qa/participants.md#limsi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/limsi.qa.pdf](http://trec.nist.gov/pubs/trec11/papers/limsi.qa.pdf)
- :material-file-search: **Runs:** [limsiQalir1](./qa/runs.md#limsiqalir1) | [limsiQalir2](./qa/runs.md#limsiqalir2) | [limsiQalir3](./qa/runs.md#limsiqalir3)

??? abstract "Abstract"
	
	The QALC question answering system at LIMSI (Ferret et al, 2001) has been largely modified for the TREC11 evaluation campaign. Architecture now includes the processing of answers retrieved from Web searching, and a number of already existing modules has been re-handled. Indeed, introducing the Web as additional resource with regard to the TREC corpus, brought us to experiment comparison strategies between answers extracted from different corpora. These strategies now make up the final answer selection module. The answer extraction module now takes advantage of using the WordNet semantic data base, whenever the expected answer type is not a named entity. As a result, we draw up a new analysis for these question categories, just as a new formulation of associated answer extraction patterns. We also changed the weighting system of the sentences which are candidate for answer, in order to increase answer reliability. Furthermore, the number of selected sentences is no longer decided before extraction module but inside it according whether the expected answer type is a named entity or not. In the last case, the number of selected sentences is greater than in case of a named entity answer type, so as to take better advantage of the selection made by means of extraction patterns and WordNet. Other modules have been modified: the QALC system now uses a search engine and document selection has been improved through document cutting into paragraphs and selection robustness improvement. Furthermore, named entity recognition module has been significantly modified in order to recognize precisely more of them and decrease ambiguity cases. In this paper, we first present the architecture of the system. Then, we will describe the modified modules, i.e. question analysis, document selection, named entity recognition, sentence weighting and answer extraction. Afterwards, the strategies of final answer selection of the new module will be described. Finally, we will present our results, ending with some concluding remarks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChalendarDEFGHIMRV02.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChalendarDEFGHIMRV02,
		author = {Ga{\"{e}}l de Chalendar and Tiphaine Dalmas and Fai{\"{\i}}za Elkateb{-}Gara and Olivier Ferret and Brigitte Grau and Martine Hurault{-}Plantet and Gabriel Illouz and Laura Monceaux and Isabelle Robba and Anne Vilnat},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Question Answering System {QALC} at LIMSI, Experiments in Using Web and WordNet},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/limsi.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChalendarDEFGHIMRV02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2002 QA at BBN: Answer Selection and Confidence Estimation

_Jinxi Xu, Ana Licuanan, Jonathan May, Scott Miller, Ralph M. Weischedel_

- :fontawesome-solid-user-group: **Participant:** [BBN](./qa/participants.md#bbn)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/bbn.xu.qa.pdf](http://trec.nist.gov/pubs/trec11/papers/bbn.xu.qa.pdf)
- :material-file-search: **Runs:** [BBN2002A](./qa/runs.md#bbn2002a) | [BBN2002B](./qa/runs.md#bbn2002b) | [BBN2002C](./qa/runs.md#bbn2002c)

??? abstract "Abstract"
	
	We focused on two issues: answer selection and confidence estimation. We found that some simple constraints on the candidate answers can improve a pure IR-based technique for answer selection. We also found that a few simple features derived from the question-answer pairs can be used for effective confidence estimation. Our results also confirmed findings by Dumais et al, 2002 that the World-Wide Web is a very useful resource for answering TREC-style factoid questions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuLMMW02.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuLMMW02,
		author = {Jinxi Xu and Ana Licuanan and Jonathan May and Scott Miller and Ralph M. Weischedel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2002 {QA} at {BBN:} Answer Selection and Confidence Estimation},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/bbn.xu.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuLMMW02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Integration of Lexical Knowledge and External Resources for Question  Answering

_Hui Yang, Tat-Seng Chua_

- :fontawesome-solid-user-group: **Participant:** [singapore](./qa/participants.md#singapore)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/nus.pris.yang.pdf](http://trec.nist.gov/pubs/trec11/papers/nus.pris.yang.pdf)
- :material-file-search: **Runs:** [nuslamp2002](./qa/runs.md#nuslamp2002)

??? abstract "Abstract"
	
	For the short, factoid questions in TREC, the query terms we get from the original questions are either too brief or often do not contain most relevant information in the corpus. It will be very difficult to find the answer (especially exact answer) in a large text document collection because of the gap between the query space and the document space. In order to bridge this gap, there is a need to expand the original queries to include the terms in the document space. In this research, we investigate the integration of both the Web and WordNet in performing local context and lexical correlations to bridge the gap. In order to minimize the noise introduced by the external resources, we explore detailed question classes, fine-grained named entities, and successive constraint relaxation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangC02,
		author = {Hui Yang and Tat{-}Seng Chua},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Integration of Lexical Knowledge and External Resources for Question Answering},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/nus.pris.yang.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICT Experiments in TREC 11 QA Main Task

_Hongbo Xu, Hao Zhang, Shuo Bai_

- :fontawesome-solid-user-group: **Participant:** [chinese_academy](./qa/participants.md#chinese_academy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cas_qa.hongbo.pdf](http://trec.nist.gov/pubs/trec11/papers/cas_qa.hongbo.pdf)
- :material-file-search: **Runs:** [ICTQA11a](./qa/runs.md#ictqa11a) | [ICTQA11b](./qa/runs.md#ictqa11b) | [ICTQA11c](./qa/runs.md#ictqa11c)

??? abstract "Abstract"
	
	This is the second time we participate in the TREC-QA track. We put emphasis on candidate passage ranking and answer matching. As to named entity tagging, we applied the latest version of GATE and did some succeeding work aiming at our goal. This paper presents our methods in detail.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuZB02.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuZB02,
		author = {Hongbo Xu and Hao Zhang and Shuo Bai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICT} Experiments in {TREC} 11 {QA} Main Task},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cas\_qa.hongbo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuZB02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC 2002: Filtering, Q&A, Web and Video Tasks

_Lide Wu, Xuanjing Huang, Junyu Niu, Yingju Xia, Zhe Feng, Yaqian Zhou_

- :fontawesome-solid-user-group: **Participant:** [Fudan](./qa/participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf](http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf)
- :material-file-search: **Runs:** [FDUT11QA1](./qa/runs.md#fdut11qa1)

??? abstract "Abstract"
	
	This year Fudan University takes part in the TREC conference for the third time. We have participated in four tracks of Filtering, Q&A, Web and Video. For filtering, we only participate in the sub-task of adaptive filtering. A novel method is presented, in which a winnow classifier from the description and narrative fields is constructed, and then utilized to assist our previous adaptive filtering system. A novel approach to confidence sorting, which is based on Maximum Entropy, is proposed in our Question Answering system. The rank of individual answer is determined by several weighted factors, and the confidence score is the product of the exponent of the weights of every factors. The weight of every factor is assigned during the training of previous questions. To return highly relevant key resources for web retrieval, we modified our original search system to make it return higher precision result than before. First, we proposed a novel search algorithm to get a base set of highly relevant documents. Then special post-processing modules are used to expand and re-sort the base set. This year we tried a fast manifold-based approach to face recognition in the Video Search Task. It can be used when there are only few different images of a specific person and runs fast. Experiment shows that applying this step will make the face recognition 5-fold faster and with almost no decreasing of performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHNXFZ02.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHNXFZ02,
		author = {Lide Wu and Xuanjing Huang and Junyu Niu and Yingju Xia and Zhe Feng and Yaqian Zhou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FDU} at {TREC} 2002: Filtering, Q{\&}A, Web and Video Tasks},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHNXFZ02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering Using the DLT System at TREC 2002

_Richard F. E. Sutcliffe_

- :fontawesome-solid-user-group: **Participant:** [limerick](./qa/participants.md#limerick)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ulimerick.sutcliffe.pdf](http://trec.nist.gov/pubs/trec11/papers/ulimerick.sutcliffe.pdf)
- :material-file-search: **Runs:** [DLT02QA01](./qa/runs.md#dlt02qa01) | [DLT02QA02](./qa/runs.md#dlt02qa02)

??? abstract "Abstract"
	
	This article outlines our participation in the Question Answering Track of the Text REtrieval Conference organised by the National Institute of Standards and Technology. Having not taken part before, our objective was to study the task and build a simple working system capable of answering at least some questions correctly. Only three person weeks was available for the work but this proved sufficient to achieve our goal. The article is structured as follows. Firstly, some preliminaries such as our starting point, tools and strategy are described. After this, the architecture of the Documents and Linguistic Technology Group's DLT system is outlined. Thirdly, the question types analysed by the system are described along with the named entities with which they work. Fourthly, the runs performed are presented together with the results we obtained. Finally, conclusions are drawn based on our findings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Sutcliffe02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Sutcliffe02,
		author = {Richard F. E. Sutcliffe},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering Using the {DLT} System at {TREC} 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/ulimerick.sutcliffe.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Sutcliffe02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Use of Patterns for Detection of Likely Answer Strings: A Systematic  Approach

_Martin M. Soubbotin, Sergei M. Soubbotin_

- :fontawesome-solid-user-group: **Participant:** [insightSoft](./qa/participants.md#insightsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/insightsoftm.sergei.pdf](http://trec.nist.gov/pubs/trec11/papers/insightsoftm.sergei.pdf)
- :material-file-search: **Runs:** [exactanswer](./qa/runs.md#exactanswer)

??? abstract "Abstract"
	
	The paper describes the Question Answering approach applied first at TREC-10 QA track and developed systematically in TREC 2002 experiments. The approach is based on the assumption that answers can be identified by their correspondence to formulas describing the structure of strings carrying certain (generalized) semantics, supposed by the question type. These formulas, or patterns, are like regular expressions but include elements corresponding to predefined lists of terms. Complex patterns can be constructed from blocks corresponding to such semantic entities as persons' or organizations' names, posts, dates, locations, etc. Using various combinations of blocks and intermediate syntactic elements allows to build a great variety of patterns. Exact position of elements corresponding to the 'exact answer' was localized within the structure of each pattern. Each pattern is characterized by a generalized semantics, thus the pattern-matching string must be checked for correlation with the question terms and/or their synonyms/substitutes.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SoubbotinS02.bib) "
	```
	@inproceedings{DBLP:conf/trec/SoubbotinS02,
		author = {Martin M. Soubbotin and Sergei M. Soubbotin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Use of Patterns for Detection of Likely Answer Strings: {A} Systematic Approach},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/insightsoftm.sergei.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SoubbotinS02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question-Answering via Enhanced Understanding of Questions

_Dan Roth, Chad M. Cumby, Xin Li, Paul Morie, Ramya Nagarajan, Nick Rizzolo, Kevin Small, Wen-tau Yih_

- :fontawesome-solid-user-group: **Participant:** [ui_uc](./qa/participants.md#ui_uc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uiuc.roth.pdf](http://trec.nist.gov/pubs/trec11/papers/uiuc.roth.pdf)
- :material-file-search: **Runs:** [UIUC2002](./qa/runs.md#uiuc2002)

??? abstract "Abstract"
	
	We describe a machine learning centered approach to developing an open domain question answering system. The system was developed in the summer of 2002, building upon several existing machine learning based NLP modules developed within a unified framework. Both queries and data were pre-processed and augmented with pos tagging, shallow parsing informa-tion, and some level of semantic categorization (be-yond named entities) using a SNoW based machine learning approach. Given these as input, the system proceeds as an incremental constraint satisfaction process. A machine learning based question analysis module extracts structural and semantic constraints on the answer, including a fine classification of the desired answer type. The system continues in several steps to identify candidate passages and then extracts an answer that best satisfies the constraints. With the available machine learning technologies, the system was developed in six weeks with the goal of identifying some of the key research issues of QA and challenges to it.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RothCLMNRSY02.bib) "
	```
	@inproceedings{DBLP:conf/trec/RothCLMNRSY02,
		author = {Dan Roth and Chad M. Cumby and Xin Li and Paul Morie and Ramya Nagarajan and Nick Rizzolo and Kevin Small and Wen{-}tau Yih},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question-Answering via Enhanced Understanding of Questions},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/uiuc.roth.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RothCLMNRSY02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Michigan at TREC 2002: Question Answering and  Novelty Tracks

_Hong Qi, Jahna Otterbacher, Adam Winkel, Dragomir R. Radev_

- :fontawesome-solid-user-group: **Participant:** [umich](./qa/participants.md#umich)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/umichigan.radev.pdf](http://trec.nist.gov/pubs/trec11/papers/umichigan.radev.pdf)
- :material-file-search: **Runs:** [NSIRGN](./qa/runs.md#nsirgn) | [NSIRG](./qa/runs.md#nsirg) | [NSIRN](./qa/runs.md#nsirn)

??? abstract "Abstract"
	
	The University of Michigan participated in two evaluations this year. In the Question Answering Track, we entered three different versions of our system, NSIR, previously described in |1. For the Novelty Track, we modified our multi-document summarizer, MEAD (www.summarization.com/mead) and submitted five runs with different input parameters.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QiOWR02.bib) "
	```
	@inproceedings{DBLP:conf/trec/QiOWR02,
		author = {Hong Qi and Jahna Otterbacher and Adam Winkel and Dragomir R. Radev},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Michigan at {TREC} 2002: Question Answering and Novelty Tracks},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/umichigan.radev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QiOWR02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Building a Foundation System for Producing Short Answers to Factual  Questions

_Sameer S. Pradhan, Valerie Krugler, Steven Bethard, Wayne H. Ward, Daniel Jurafsky, James H. Martin, Sasha Blair-Goldensohn, Andrew Hazen Schlaikjer, Elena Filatova, Pablo Ariel Duboue, Hong Yu, Rebecca J. Passonneau, Vasileios Hatzivassiloglou, Kathleen R. McKeown, Gabriel Illouz_

- :fontawesome-solid-user-group: **Participant:** [columbia](./qa/participants.md#columbia)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ucolorado.pradhan.pdf](http://trec.nist.gov/pubs/trec11/papers/ucolorado.pradhan.pdf)
- :material-file-search: **Runs:** [2002cuaq1](./qa/runs.md#2002cuaq1) | [2002cuaq2](./qa/runs.md#2002cuaq2)

??? abstract "Abstract"
	
	In this paper we describe question answering research being pursued as a joint project between Columbia University and the University of Colorado at Boulder as part of ARDA's AQUAINT program. As a foundation for targeting complex questions involving opinions, events, and paragraph-length answers, we recently built two systems for answering short factual questions. We submitted results from the two systems to TREC's Q&A track, and the bulk of this paper describes the methods used in building each system and the results obtained. We conclude by discussing current work aiming at combining modules from the two systems in a unified, more accurate system and adding capabilities for producing complex answers in addition to short ones.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PradhanKBWJMBSFDYPHMI02.bib) "
	```
	@inproceedings{DBLP:conf/trec/PradhanKBWJMBSFDYPHMI02,
		author = {Sameer S. Pradhan and Valerie Krugler and Steven Bethard and Wayne H. Ward and Daniel Jurafsky and James H. Martin and Sasha Blair{-}Goldensohn and Andrew Hazen Schlaikjer and Elena Filatova and Pablo Ariel Duboue and Hong Yu and Rebecca J. Passonneau and Vasileios Hatzivassiloglou and Kathleen R. McKeown and Gabriel Illouz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Building a Foundation System for Producing Short Answers to Factual Questions},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/ucolorado.pradhan.pdf},
		timestamp = {Sat, 21 Jan 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PradhanKBWJMBSFDYPHMI02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The QUANTUM Question Answering System at TREC 11

_Luc Plamondon, Guy Lapalme, Leila Kosseim_

- :fontawesome-solid-user-group: **Participant:** [u_montreal](./qa/participants.md#u_montreal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/umontreal.quantum.pdf](http://trec.nist.gov/pubs/trec11/papers/umontreal.quantum.pdf)
- :material-file-search: **Runs:** [UdeMmainNoW](./qa/runs.md#udemmainnow) | [UdeMmainWeb](./qa/runs.md#udemmainweb) | [UdeMlistNoW](./qa/runs.md#udemlistnow)

??? abstract "Abstract"
	
	This year, we participated to the Question Answering task for the second time with the QUANTUM system. We entered 2 runs for the main task (one using the web, the other without) and 1 run for the list task (without the web). We essentially built on last year's experience to enhance the system. The architecture of QUANTUM is mainly the same as last year: it uses patterns that rely on shallow parsing techniques and regular expressions to analyze the question and then select the most appropriate extraction function. This extraction function is then applied to one-paragraph long passages retrieved by Okapi to extract and score candidate answers. Among the novelties we added to QUANTUM this year is a web module that finds exact answers using high-precision reformul tion of the question to anticipate the expected context of the answer.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PlamondonLK02.bib) "
	```
	@inproceedings{DBLP:conf/trec/PlamondonLK02,
		author = {Luc Plamondon and Guy Lapalme and Leila Kosseim},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {QUANTUM} Question Answering System at {TREC} 11},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/umontreal.quantum.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PlamondonLK02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The JAVELIN Question-Answering System at TREC 2002

_Eric Nyberg, Teruko Mitamura, Jaime G. Carbonell, James P. Callan, Kevyn Collins-Thompson, Krzysztof Czuba, Michael Duggan, Laurie Hiyakumoto, N. Hu, Yifen Huang, Jeongwoo Ko, Lucian Vlad Lita, S. Murtagh, Vasco Pedro, David Svoboda_

- :fontawesome-solid-user-group: **Participant:** [cmu_javelin](./qa/participants.md#cmu_javelin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cmu.javelin.pdf](http://trec.nist.gov/pubs/trec11/papers/cmu.javelin.pdf)
- :material-file-search: **Runs:** [CMUJAV000495](./qa/runs.md#cmujav000495) | [CMUJAV000501](./qa/runs.md#cmujav000501)

??? abstract "Abstract"
	
	This paper describes the JAVELIN approach for open-domain question answering (Justification-based Answer Valuation through Language Interpretation), and our participation in the TREC 2002 question-answering track. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NybergMCCCCDHHHKLMPS02.bib) "
	```
	@inproceedings{DBLP:conf/trec/NybergMCCCCDHHHKLMPS02,
		author = {Eric Nyberg and Teruko Mitamura and Jaime G. Carbonell and James P. Callan and Kevyn Collins{-}Thompson and Krzysztof Czuba and Michael Duggan and Laurie Hiyakumoto and N. Hu and Yifen Huang and Jeongwoo Ko and Lucian Vlad Lita and S. Murtagh and Vasco Pedro and David Svoboda},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {JAVELIN} Question-Answering System at {TREC} 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cmu.javelin.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NybergMCCCCDHHHKLMPS02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering Approach Using a WordNet-based Answer Type Taxonomy

_Seung-Hoon Na, In-Su Kang, Sang-Yool Lee, Jong-Hyeok Lee_

- :fontawesome-solid-user-group: **Participant:** [postech_kang](./qa/participants.md#postech_kang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/pohang.seunghoon.pdf](http://trec.nist.gov/pubs/trec11/papers/pohang.seunghoon.pdf)
- :material-file-search: **Runs:** [KLE000](./qa/runs.md#kle000)

??? abstract "Abstract"
	
	In question answering (QA), answer types are semantic categories that questions require. An answer type taxonomy (ATT) is a collection of these answer types. ATT may heavily affect the performance of QA systems, because its broadness and granularity provides coverage and specificity of answer types. Cardie [1] used 13 categories for entity classification, and obtained large performance improvement, compared with the method using no categories. Also, according to Pasca et al. [3], the more categories a system uses, the better performance the system shows. For example, consider two answer type taxonomies, A={PERSON}, and B={PRESIDENT, ENGINEER, SINGER, PERSON}. Given a question “Who was the president of Vichy France?”, we know that the more specific answer type of this question is not PERSON, but PRESIDENT. Thus, if we use ATT B, a set of candidate answers from documents can be reduced to a set of PRESIDENT entities, by excluding the other PERSON entities such as ENGINEER and SINGER. This is not the case with ATT A. However, since ATT A cannot distinguish hypernyms of PERSON, the QA system should consider much more candidate answers. Thus far, most QA systems rely on small-scale ATTs, with the number of semantic categories ranging from 20 to 100. Normally, these ATTs are created from a beginning set of frequently-asked answer types like person, organization, location, number, etc., and then they are incrementally extended to include unexpected answer types from new questions. However, these ad-hoc ATTs may raise the following problems in QA. First, it is nontrivial to manually enlarge a small ATT to a large one, as new answer types appear. Second, ad-hoc ATTs do not allow easy adaptation for processing questions asking new answer types. For such questions, the system needs to modify an existing IE module to classify entities into new answer types. Third, previous ATTs do not have sufficient broadness and granularity, where they are expected characteristics of ATT for open-domain QA. Therefore, at this year's TREC, we have taken a question answering approach that uses WordNet itself as ATT. In other words, our QA system maps an answer type into a concept node called a synset in WordNet. WordNet provides sufficient diversity and density to distinguish specific answer types for most questions. By using such an ontological taxonomy, we do not have the above problems with small ad-hoc ATTs. This paper is organized as follows. Section 2 describes each module of our QA system, and section 3 shows TREC-11 evaluation results, and concluding remarks are given in section 4.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NaKLL02.bib) "
	```
	@inproceedings{DBLP:conf/trec/NaKLL02,
		author = {Seung{-}Hoon Na and In{-}Su Kang and Sang{-}Yool Lee and Jong{-}Hyeok Lee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering Approach Using a WordNet-based Answer Type Taxonomy},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/pohang.seunghoon.pdf},
		timestamp = {Sat, 30 Sep 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NaKLL02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at TREC 2002

_Christof Monz, Jaap Kamps, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [uva](./qa/participants.md#uva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uamsterdam.derijke.pdf](http://trec.nist.gov/pubs/trec11/papers/uamsterdam.derijke.pdf)
- :material-file-search: **Runs:** [UAmsT11qaM1](./qa/runs.md#uamst11qam1) | [UAmsT11qaM2](./qa/runs.md#uamst11qam2) | [UAmsT11qaM3](./qa/runs.md#uamst11qam3)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2002 Novelty, Question answering, and Web tracks. We provide a detailed account of the ideas underlying our approaches to these tasks. All our runs used the FlexIR information retrieval system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MonzKR02.bib) "
	```
	@inproceedings{DBLP:conf/trec/MonzKR02,
		author = {Christof Monz and Jaap Kamps and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Amsterdam at {TREC} 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/uamsterdam.derijke.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MonzKR02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LCC Tools for Question Answering

_Dan I. Moldovan, Sanda M. Harabagiu, Roxana Girju, Paul Morarescu, V. Finley Lacatusu, Adrian Novischi, Adriana Badulescu, Orest Bolohan_

- :fontawesome-solid-user-group: **Participant:** [LCC](./qa/participants.md#lcc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/lcc.moldovan.pdf](http://trec.nist.gov/pubs/trec11/papers/lcc.moldovan.pdf)
- :material-file-search: **Runs:** [LCCmain2002](./qa/runs.md#lccmain2002) | [LCClist2002](./qa/runs.md#lcclist2002)

??? abstract "Abstract"
	
	The increased complexity of the TREC QA questions requires advanced text processing tools that rely on natural language processing and knowledge reasoning. This paper presents the suite of tools that account for the performance of the Power Answer question answering system. It is shown how questions, answers and world knowledge are transformed first in logic representation, followed by a systematic and rigorous logic proof that validly answers questions posed to the QA system. At TREC QA 2002, Power Answer obtained a confidence-weighted score of 0.856, answering correctly 415 out of 500 questions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoldovanHGMLNBB02.bib) "
	```
	@inproceedings{DBLP:conf/trec/MoldovanHGMLNBB02,
		author = {Dan I. Moldovan and Sanda M. Harabagiu and Roxana Girju and Paul Morarescu and V. Finley Lacatusu and Adrian Novischi and Adriana Badulescu and Orest Bolohan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{LCC} Tools for Question Answering},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/lcc.moldovan.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MoldovanHGMLNBB02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Filtering 

#### The TREC 2002 Filtering Track Report

_Stephen E. Robertson, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/OVER.FILTERING.pdf](http://trec.nist.gov/pubs/trec11/papers/OVER.FILTERING.pdf)
??? abstract "Abstract"
	
	The TREC-11 filtering track measures the ability of systems to build persistent user profiles which successfully separate relevant and non-relevant documents in an incoming stream. It consists of three major subtasks: adaptive filtering, batch filtering, and routing. In adaptive filtering, the system begins with only a topic statement and a small number of positive examples, and must learn a better profile from on-line feedback. Batch filtering and routing are more traditional machine learning tasks where the system begins with a large sample of evaluated training documents. This report describes the track, presents some evaluation results, and provides a general commentary on lessons learned from this year's track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonS02.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonS02,
		author = {Stephen E. Robertson and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {TREC} 2002 Filtering Track Report},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/OVER.FILTERING.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonS02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 11 Experiments at NII: The Effects of Virtual Relevant Documents  in Batch Filtering

_Kyung-Soon Lee, Kyo Kageura, Akiko N. Aizawa_

- :fontawesome-solid-user-group: **Participant:** [nii](./filtering/participants.md#nii)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/nii.lee.pdf](http://trec.nist.gov/pubs/trec11/papers/nii.lee.pdf)
- :material-file-search: **Runs:** [kNII11bf1](./filtering/runs.md#knii11bf1) | [kNII11bf2](./filtering/runs.md#knii11bf2)

??? abstract "Abstract"
	
	[...] In TREC-11 batch filtering, we have incorporated prior knowledge called virtual relevant documents to training documents by combining each two relevant documents pair and giving distinct weight for cooccurring terms on assumption that they might be related to the topic. Support vector machine (SVM) was used to learn decision boundary for the artificially enlarged training documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeKA02.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeKA02,
		author = {Kyung{-}Soon Lee and Kyo Kageura and Akiko N. Aizawa},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 11 Experiments at {NII:} The Effects of Virtual Relevant Documents in Batch Filtering},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/nii.lee.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeKA02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2002 Web, Novelty and Filtering Track Experiments using PIRCS

_Kui-Lam Kwok, Peter Deng, Norbert Dinstl, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./filtering/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/queens.kwok.pdf](http://trec.nist.gov/pubs/trec11/papers/queens.kwok.pdf)
- :material-file-search: **Runs:** [pirc2F01](./filtering/runs.md#pirc2f01) | [pirc2F02](./filtering/runs.md#pirc2f02) | [pirc2F03](./filtering/runs.md#pirc2f03) | [pirc2F04](./filtering/runs.md#pirc2f04)

??? abstract "Abstract"
	
	In TREC2002, we participated in three tracks: web, novelty and adaptive filtering. The Web track has two tasks: distillation and named-page retrieval. Distillation is a new utility concept for ranking documents, and needs new design on the output document ranked list after an ad-hoc retrieval from the web (.gov) collection. Novelty track is a new task that involves identifying relevant sentences to a question, and to remove duplicate or non- novel entries in the answer list. The third track is adaptive filtering. We revived a filtering program that was functional at TREC-9 with some added capability. Sections 2, 3, 4 describe our participation in these tracks respectively. Section 5 has our conclusion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokDDC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokDDC02,
		author = {Kui{-}Lam Kwok and Peter Deng and Norbert Dinstl and M. Chan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2002 Web, Novelty and Filtering Track Experiments using {PIRCS}},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/queens.kwok.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokDDC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Incremental Retrieval of Documents Relevant to a Topic

_Caroline Lyon, Bob Dickerson, James A. Malcolm_

- :fontawesome-solid-user-group: **Participant:** [hertfordshire](./filtering/participants.md#hertfordshire)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/hertfordshire.lyon.pdf](http://trec.nist.gov/pubs/trec11/papers/hertfordshire.lyon.pdf)
- :material-file-search: **Runs:** [UHcl1](./filtering/runs.md#uhcl1) | [UHcl2](./filtering/runs.md#uhcl2)

??? abstract "Abstract"
	
	As new participants to TREC, on the Filtering Track, we have started by first investigating two methods of producing document profiles. We begin by looking for 'obvious' profiles that detect closely related documents. This year we have started by looking for: lexically similar cases; semantically similar cases based on a simple combination of keywords.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LyonDM02.bib) "
	```
	@inproceedings{DBLP:conf/trec/LyonDM02,
		author = {Caroline Lyon and Bob Dickerson and James A. Malcolm},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Incremental Retrieval of Documents Relevant to a Topic},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/hertfordshire.lyon.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LyonDM02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLARIT Experiments in Batch Filtering: Term Selection and Threshold  Optimization in IR and SVM Filters

_David A. Evans, James G. Shanahan, Norbert Roma, Jeffrey Bennett, Victor Sheftel, Emilia Stoica, Jesse Montgomery, David A. Hull, Waibhav Tembe_

- :fontawesome-solid-user-group: **Participant:** [clairvoyance](./filtering/participants.md#clairvoyance)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/clairvoyance.evans.pdf](http://trec.nist.gov/pubs/trec11/papers/clairvoyance.evans.pdf)
- :material-file-search: **Runs:** [CCT11BFC](./filtering/runs.md#cct11bfc) | [CCT11BFD](./filtering/runs.md#cct11bfd)

??? abstract "Abstract"
	
	The Clairvoyance team participated in the Filtering Track, submitting two runs in the Batch Filtering category. While we have been exploring the question of both topic modeling and ensemble filter construction (as in our previous TREC filtering experiments [5]), we had one distinct objective this year, to explore the viability of monolithic filters in classification-like tasks. This is appropriate to our work, in part, because monolithic filters are a crucial starting point for ensemble filtering, and it is possible for them to contribute substantially in the ensemble approach. Our primary goal in experiments this year, thus, was to explore two issues in monolithic filter construction: (1) term count selection and (2) filter threshold optimization. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EvansSRBSSMHT02.bib) "
	```
	@inproceedings{DBLP:conf/trec/EvansSRBSSMHT02,
		author = {David A. Evans and James G. Shanahan and Norbert Roma and Jeffrey Bennett and Victor Sheftel and Emilia Stoica and Jesse Montgomery and David A. Hull and Waibhav Tembe},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CLARIT} Experiments in Batch Filtering: Term Selection and Threshold Optimization in {IR} and {SVM} Filters},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/clairvoyance.evans.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EvansSRBSSMHT02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Novel Results and Some Answers - The University of Iowa TREC 11  Results

_David Eichmann, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [uiowa](./filtering/participants.md#uiowa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uiowa.eichmann.pdf](http://trec.nist.gov/pubs/trec11/papers/uiowa.eichmann.pdf)
- :material-file-search: **Runs:** [UIowa02Filt](./filtering/runs.md#uiowa02filt)

??? abstract "Abstract"
	
	The University of Iowa participated in the novelty, adaptive filtering and question answering tracks of TREC-11. The filtering system used was an extension of the one used in TREC-7 [1] and TREC-8 [2]. Question answering was derived from the TREC-10 system. The novelty system was new...
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannS02.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannS02,
		author = {David Eichmann and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Novel Results and Some Answers - The University of Iowa {TREC} 11 Results},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/uiowa.eichmann.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannS02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Filtering, Novelty Detection, and Named-Page Finding

_Kevyn Collins-Thompson, Paul Ogilvie, Yi Zhang, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [cmu_lti](./filtering/participants.md#cmu_lti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cmu.collins-thompson.pdf](http://trec.nist.gov/pubs/trec11/papers/cmu.collins-thompson.pdf)
- :material-file-search: **Runs:** [CMUDIRUDESC](./filtering/runs.md#cmudirudesc) | [CMUDIRFDESC](./filtering/runs.md#cmudirfdesc) | [CMUDIRUml](./filtering/runs.md#cmudiruml) | [CMUDIRFml](./filtering/runs.md#cmudirfml)

??? abstract "Abstract"
	
	In TREC 11, our group participated in the Novelty track, Filtering track, and the Named-Page Finding task of the Web track. This paper describes our approaches, experiments, and results. As the approach for each task is quite different, the paper contains a section for each of the tasks. The following section describes our experiments in adaptive filtering, Section 3 describes named-page finding, and section 4 discusses the Novelty track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Collins-ThompsonOZC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Collins-ThompsonOZC02,
		author = {Kevyn Collins{-}Thompson and Paul Ogilvie and Yi Zhang and Jamie Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Information Filtering, Novelty Detection, and Named-Page Finding},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cmu.collins-thompson.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Collins-ThompsonOZC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Kernel Methods for Document Filtering

_Nicola Cancedda, Cyril Goutte, Jean-Michel Renders, Nicolò Cesa-Bianchi, Alex Conconi, Yaoyong Li, John Shawe-Taylor, Alexei Vinokourov, Thore Graepel, Claudio Gentile_

- :fontawesome-solid-user-group: **Participant:** [kerMIT](./filtering/participants.md#kermit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/kermit.pdf](http://trec.nist.gov/pubs/trec11/papers/kermit.pdf)
- :material-file-search: **Runs:** [KerMITT11af1](./filtering/runs.md#kermitt11af1) | [KerMITT11af2](./filtering/runs.md#kermitt11af2) | [KerMITT11af3](./filtering/runs.md#kermitt11af3) | [KerMITT11af4](./filtering/runs.md#kermitt11af4) | [KerMITT11bf2](./filtering/runs.md#kermitt11bf2) | [KerMITT11rr2](./filtering/runs.md#kermitt11rr2)

??? abstract "Abstract"
	
	This paper describes the algorithms implemented by the KerMIT consortium for its participation in the TREC 2002 Filtering track. The consortium submitted runs for the routing task using a linear SVM, for the batch task using the same SVM in combination with an innovative threshold-selection mechanism, and for the adaptive task using both a second-order perceptron and a combination of SVM and perceptron with uneven margin. Results seem to indicate that these algorithm performed relatively well on the extensive TREC benchmark.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CanceddaGRCCLSVGG02.bib) "
	```
	@inproceedings{DBLP:conf/trec/CanceddaGRCCLSVGG02,
		author = {Nicola Cancedda and Cyril Goutte and Jean{-}Michel Renders and Nicol{\`{o}} Cesa{-}Bianchi and Alex Conconi and Yaoyong Li and John Shawe{-}Taylor and Alexei Vinokourov and Thore Graepel and Claudio Gentile},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Kernel Methods for Document Filtering},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/kermit.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CanceddaGRCCLSVGG02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLIPS at TREC 11: Experiments in Filtering

_Christophe Brouard_

- :fontawesome-solid-user-group: **Participant:** [clips-imag](./filtering/participants.md#clips-imag)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/clips.filter.pdf](http://trec.nist.gov/pubs/trec11/papers/clips.filter.pdf)
- :material-file-search: **Runs:** [reliefst11u](./filtering/runs.md#reliefst11u)

??? abstract "Abstract"
	
	At the TREC9 conference, we presented a new adaptive filtering system called RELIEFS. This system which is based on the idea of resonance, combines for each term t, the relative frequency of relevance knowing t and the relative frequency of t kwowing relevance. On the basis of other experiments, several changes have been made. We improved our threshold adaption, we slightly changed our relevance evaluation function and we gave up the use of conjunctions and thesaurus. The system is now focusing more exclusively on the combination of both reverse frequencies that we believe to represent the fundamental aspects of relevance estimation. This year we used the system in its new version and we tested it on the Reuters corpus. Focusing on the combination of the two frequencies, we varied their relative importance. The results show globally a good effectiveness especially when both frequencies are balanced.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Brouard02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Brouard02,
		author = {Christophe Brouard},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CLIPS} at {TREC} 11: Experiments in Filtering},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/clips.filter.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Brouard02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC 2002: Filtering Track

_Mohand Boughanem, Hamid Tebri, Mohamed Tmar_

- :fontawesome-solid-user-group: **Participant:** [irit](./filtering/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/irit.tebri.pdf](http://trec.nist.gov/pubs/trec11/papers/irit.tebri.pdf)
- :material-file-search: **Runs:** [iritsiga1](./filtering/runs.md#iritsiga1) | [iritsiga2](./filtering/runs.md#iritsiga2) | [iritsigb](./filtering/runs.md#iritsigb) | [iritsigr](./filtering/runs.md#iritsigr)

??? abstract "Abstract"
	
	The experiments we undertaken this year for TREC2002 Filtering track, are focussed on threshold calibration. We proposed a new approach to calibrate the dissemination threshold in an adaptive information filtering. It consists of optimizing a utility function represented by a linearized form of the probability distributions of the scores of the relevant and the non-relevant documents already filtered. The profiles are learned using the same method used last year. It is based on a reinforcement algorithm. We submitted results on three tasks: adaptive, batch and routing.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoughanemTT02.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoughanemTT02,
		author = {Mohand Boughanem and Hamid Tebri and Mohamed Tmar},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IRIT} at {TREC} 2002: Filtering Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/irit.tebri.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoughanemTT02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Incremental Learning for Profile Training in Adaptive Document Filtering

_Liang Ma, Qunxiu Chen, Shaoping Ma, Min Zhang, Lianhong Cai_

- :fontawesome-solid-user-group: **Participant:** [tsinghua](./filtering/participants.md#tsinghua)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/tsinghuau.filtering2.pdf](http://trec.nist.gov/pubs/trec11/papers/tsinghuau.filtering2.pdf)
- :material-file-search: **Runs:** [thuT11af1](./filtering/runs.md#thut11af1) | [thuT11af2](./filtering/runs.md#thut11af2) | [thuT11af3](./filtering/runs.md#thut11af3)

??? abstract "Abstract"
	
	In this paper, we describe our ideas and related experiments in TREC-11 Adaptive Filtering Track. In the track we focused much on a robust way for effective profile training. We developed an incremental learning method which selects pseudo positive documents in less bias from a few initial positive training documents. We also did some experiments with newly emerged information retrieval model, language model-based retrieval mechanism, to evaluate its performance when used in adaptive filtering task. Related experiment results show the incremental learning method can be helpful for profile training, while the new language model perform not well.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MaCMZC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/MaCMZC02,
		author = {Liang Ma and Qunxiu Chen and Shaoping Ma and Min Zhang and Lianhong Cai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Incremental Learning for Profile Training in Adaptive Document Filtering},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/tsinghuau.filtering2.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MaCMZC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 11 Experiments at CAS-ICT: Filtering and Web

_Hongbo Xu, Zhifeng Yang, Bin Wang, Bin Liu, Jun Cheng, Yue Liu, Zhe Yang, Xueqi Cheng, Shuo Bai_

- :fontawesome-solid-user-group: **Participant:** [chinese_academy](./filtering/participants.md#chinese_academy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cas_final.hongbo.pdf](http://trec.nist.gov/pubs/trec11/papers/cas_final.hongbo.pdf)
- :material-file-search: **Runs:** [ICTBatFT11Ua](./filtering/runs.md#ictbatft11ua) | [ICTBatFT11Ub](./filtering/runs.md#ictbatft11ub) | [ICTAdaFT11Ud](./filtering/runs.md#ictadaft11ud) | [ICTAdaFT11Ua](./filtering/runs.md#ictadaft11ua) | [ICTAdaFT11Ub](./filtering/runs.md#ictadaft11ub) | [ICTAdaFT11Uc](./filtering/runs.md#ictadaft11uc) | [ICTRouFT11Ua](./filtering/runs.md#ictrouft11ua) | [ICTRouFT11Ub](./filtering/runs.md#ictrouft11ub)

??? abstract "Abstract"
	
	CAS-ICT took part in the TREC conference for the second time this year and we undertook two tracks of TREC-11. For filtering track, we have submitted results of all three subtasks. In adaptive filtering, we paid more attention to undetermined documents processing, profile building and adaptation. In batch filtering and routing, a centroid-based classifier is used with preprocessed samples. For Web track, we have submitted results of both two subtasks. Different factors are considered to improve the overall performance of our Web systems. This paper describes our methods in detail.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuYWLCLYCB02.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuYWLCLYCB02,
		author = {Hongbo Xu and Zhifeng Yang and Bin Wang and Bin Liu and Jun Cheng and Yue Liu and Zhe Yang and Xueqi Cheng and Shuo Bai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 11 Experiments at {CAS-ICT:} Filtering and Web},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cas\_final.hongbo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuYWLCLYCB02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC 2002: Filtering, Q&A, Web and Video Tasks

_Lide Wu, Xuanjing Huang, Junyu Niu, Yingju Xia, Zhe Feng, Yaqian Zhou_

- :fontawesome-solid-user-group: **Participant:** [Fudan](./filtering/participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf](http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf)
- :material-file-search: **Runs:** [FDUT11AF1](./filtering/runs.md#fdut11af1) | [FDUT11AF2](./filtering/runs.md#fdut11af2)

??? abstract "Abstract"
	
	his year Fudan University takes part in the TREC conference for the third time. We have participated in four tracks of Filtering, Q&A, Web and Video. For filtering, we only participate in the sub-task of adaptive filtering. A novel method is presented, in which a winnow classifier from the description and narrative fields is constructed, and then utilized to assist our previous adaptive filtering system. A novel approach to confidence sorting, which is based on Maximum Entropy, is proposed in our Question Answering system. The rank of individual answer is determined by several weighted factors, and the confidence score is the product of the exponent of the weights of every factors. The weight of every factor is assigned during the training of previous questions. To return highly relevant key resources for web retrieval, we modified our original search system to make it return higher precision result than before. First, we proposed a novel search algorithm to get a base set of highly relevant documents. Then special post-processing modules are used to expand and re-sort the base set. This year we tried a fast manifold-based approach to face recognition in the Video Search Task. It can be used when there are only few different images of a specific person and runs fast. Experiment shows that applying this step will make the face recognition 5-fold faster and with almost no decreasing of performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHNXFZ02.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHNXFZ02,
		author = {Lide Wu and Xuanjing Huang and Junyu Niu and Yingju Xia and Zhe Feng and Yaqian Zhou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FDU} at {TREC} 2002: Filtering, Q{\&}A, Web and Video Tasks},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHNXFZ02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Example Based Text Matching Methodology for Routing Tasks

_Ari Visa, Jarmo Toivonen, Tomi Vesanen, Jarno Mäkinen, Barbro Back, Hannu Vanharanta_

- :fontawesome-solid-user-group: **Participant:** [tampere](./filtering/participants.md#tampere)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/tampere.jarmo.pdf](http://trec.nist.gov/pubs/trec11/papers/tampere.jarmo.pdf)
- :material-file-search: **Runs:** [Visa1T11](./filtering/runs.md#visa1t11) | [Visa2T11](./filtering/runs.md#visa2t11)

??? abstract "Abstract"
	
	We present two variations of a prototype based text matching methodology used in the Routing Sub-Task of TREC 2002 Filtering Track. The methodology examines text on the word level. It is based on word coding and examines the distributions of these codes using document histograms.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VisaTVMBV02.bib) "
	```
	@inproceedings{DBLP:conf/trec/VisaTVMBV02,
		author = {Ari Visa and Jarmo Toivonen and Tomi Vesanen and Jarno M{\"{a}}kinen and Barbro Back and Hannu Vanharanta},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Example Based Text Matching Methodology for Routing Tasks},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/tampere.jarmo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VisaTVMBV02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UB at TREC 11: Batch and Adaptive Filtering

_Munirathnam Srikanth, Xiaoyun Wu, Rohini K. Srihari_

- :fontawesome-solid-user-group: **Participant:** [buffalo_cedar](./filtering/participants.md#buffalo_cedar)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/unybuffalo.pdf](http://trec.nist.gov/pubs/trec11/papers/unybuffalo.pdf)
- :material-file-search: **Runs:** [cedar02bffb0](./filtering/runs.md#cedar02bffb0) | [cedar02afut0](./filtering/runs.md#cedar02afut0) | [cedar02affb0](./filtering/runs.md#cedar02affb0) | [cedar02bfut0](./filtering/runs.md#cedar02bfut0)

??? abstract "Abstract"
	
	This is the first time we participated in TREC filtering track. We submitted four runs: two for adaptive filtering, and two for batching filtering. And these runs come from two separate efforts with very different approaches. One effort treats the filtering problems as standard text categorization problems and solves them using Support Vector Machines (SVM). The second effort is a Language Modeling approach to information filtering. Among other things we wanted to use filtering tasks as large scale test cases for two separate frameworks we have been working on for information retrieval. Significant time was spent on putting the components together and limited time on pre-submission performance evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SrikanthWS02.bib) "
	```
	@inproceedings{DBLP:conf/trec/SrikanthWS02,
		author = {Munirathnam Srikanth and Xiaoyun Wu and Rohini K. Srihari},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UB} at {TREC} 11: Batch and Adaptive Filtering},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/unybuffalo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SrikanthWS02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Cambridge at TREC 2002: Filtering Track

_Stephen E. Robertson, Steve Walker, Hugo Zaragoza, Ralf Herbrich_

- :fontawesome-solid-user-group: **Participant:** [microsoft_cambridge](./filtering/participants.md#microsoft_cambridge)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cambridge.corrected.pdf](http://trec.nist.gov/pubs/trec11/papers/cambridge.corrected.pdf)
- :material-file-search: **Runs:** [ok11aflu](./filtering/runs.md#ok11aflu) | [ok11afsu](./filtering/runs.md#ok11afsu) | [ok11afsb](./filtering/runs.md#ok11afsb) | [ok11aflb](./filtering/runs.md#ok11aflb) | [msPUMs](./filtering/runs.md#mspums) | [msPUMb](./filtering/runs.md#mspumb)

??? abstract "Abstract"
	
	Six runs were submitted for the Adaptive Filtering track, four on the adaptive filtering task (ok11af??), and two on the routing task (msPUM?). The adaptive filtering system has been somewhat modified from the one used for TREC–10, largely for efficiency and flexibility reasons; the basic filtering algorithms remain similar to those used in recent TRECs. For the routing task, a completely new system based on perceptrons with uneven margins was used.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonWZH02.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonWZH02,
		author = {Stephen E. Robertson and Steve Walker and Hugo Zaragoza and Ralf Herbrich},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Cambridge at {TREC} 2002: Filtering Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cambridge.corrected.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonWZH02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Classifier Stacking and Voting for Text Filtering

_Rada Mihalcea_

- :fontawesome-solid-user-group: **Participant:** [north_texas](./filtering/participants.md#north_texas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/untexas.mihalcea.pdf](http://trec.nist.gov/pubs/trec11/papers/untexas.mihalcea.pdf)
- :material-file-search: **Runs:** [UNTextCatSU](./filtering/runs.md#untextcatsu) | [UNTextCatF](./filtering/runs.md#untextcatf) | [UNTextCatR](./filtering/runs.md#untextcatr) | [UNTextCatR1](./filtering/runs.md#untextcatr1)

??? abstract "Abstract"
	
	This paper summarizes the approach and the results of the TextCat system participating in the Filtering track in the Text Retrieval Conference 2002. The system relies primarily on statistical methods, and was designed with the main purpose of having a backbone system in which we can further integrate semantic components, and evaluate their relative performance as compared to traditional statistical approaches. The system is therefore simple, and is based on techniques for keywords extraction, and various classifier combinations including stacking and voting. TextCat participated in the Batch and Routing tasks. In the Batch task, it achieved a score of 39.02% normalized utility, and 26.37% F-measure respectively, averaged over all topics. The averaged uninterpolated precision for our best routing submission was 14.16%.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Mihalcea02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Mihalcea02,
		author = {Rada Mihalcea},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Classifier Stacking and Voting for Text Filtering},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/untexas.mihalcea.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Mihalcea02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JHU/APL at TREC 2002: Experiments in Filtering and Arabic Retrieval

_Paul McNamee, Christine D. Piatko, James Mayfield_

- :fontawesome-solid-user-group: **Participant:** [jhu_apl](./filtering/participants.md#jhu_apl)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/jhuapl.mcnamee.pdf](http://trec.nist.gov/pubs/trec11/papers/jhuapl.mcnamee.pdf)
- :material-file-search: **Runs:** [apl11Fah1](./filtering/runs.md#apl11fah1) | [apl11Fah2](./filtering/runs.md#apl11fah2) | [apl11Faq1](./filtering/runs.md#apl11faq1) | [apl11Faq2](./filtering/runs.md#apl11faq2) | [apl11FbF](./filtering/runs.md#apl11fbf) | [apl11FbSU](./filtering/runs.md#apl11fbsu) | [apl11Frm](./filtering/runs.md#apl11frm) | [apl11Frsvm](./filtering/runs.md#apl11frsvm)

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

#### Rutgers Filtering Work at TREC 2002: Adaptive and Batch

_Andrei Anghelescu, Endre Boros, David D. Lewis, Vladimir Menkov, David J. Neu, Paul B. Kantor_

- :fontawesome-solid-user-group: **Participant:** [rutgers-kantor](./filtering/participants.md#rutgers-kantor)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/rutgers.kantor.pdf](http://trec.nist.gov/pubs/trec11/papers/rutgers.kantor.pdf)
- :material-file-search: **Runs:** [dimacs11a30Q](./filtering/runs.md#dimacs11a30q) | [dimacs11aAPQ](./filtering/runs.md#dimacs11aapq) | [dimacs11b001](./filtering/runs.md#dimacs11b001) | [dimacs11aP1Q](./filtering/runs.md#dimacs11ap1q)

??? abstract "Abstract"
	
	This year at TREC 2002 we participated in the adaptive filtering sub-task of the filtering track with some models for training a Rocchio classifier. Results were poorer than average on the utility type measures. Using simple feature selection produced better than average results on an F-type measure. The key to our approach was the use of pseudo-judgments, and an approach to threshold updating. We also participated in the batch filtering sub-task of the filtering track and investigated the use of rank based feature selection techniques in conjunction with a very simple classification rule.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnghelescuBLMNK02.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnghelescuBLMNK02,
		author = {Andrei Anghelescu and Endre Boros and David D. Lewis and Vladimir Menkov and David J. Neu and Paul B. Kantor},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Rutgers Filtering Work at {TREC} 2002: Adaptive and Batch},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/rutgers.kantor.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnghelescuBLMNK02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Novelty 

#### Overview of the TREC 2002 Novelty Track

_Donna Harman_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/NOVELTY.OVER.pdf](http://trec.nist.gov/pubs/trec11/papers/NOVELTY.OVER.pdf)
??? abstract "Abstract"
	
	The novelty track was a new track in TREC-11. The basic task was as follows: given a TREC topic and an ordered list of relevant documents (ordered by relevance ranking), find the relevant and 'novel' sentences that should be returned to the user from this set. There were 13 groups that participated in this new task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Harman02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Harman02,
		author = {Donna Harman},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2002 Novelty Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/NOVELTY.OVER.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Harman02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Machine Learning Approach for QA and Novelty Tracks: NTT System  Description

_Hideto Kazawa, Tsutomu Hirao, Hideki Isozaki, Eisaku Maeda_

- :fontawesome-solid-user-group: **Participant:** [nttcom_kazawa](./novelty/participants.md#nttcom_kazawa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/nttcom.pdf](http://trec.nist.gov/pubs/trec11/papers/nttcom.pdf)
- :material-file-search: **Runs:** [nttcslabnvp](./novelty/runs.md#nttcslabnvp) | [nttcslabnvr2](./novelty/runs.md#nttcslabnvr2)

??? abstract "Abstract"
	
	In one sense, the goals of QA and Novelty tasks are the same: extracting small document parts which are relevant to users' queries. Additionally, the unit of extraction is almost always fixed in both tasks. For QA, an answer is a noun phrase in most cases, and for Novelty, a sentence is recognized as the basic information unit. This observation leads us to the following unified approach to both QA and Novelty tasks: first identify information units in documents, then judge whether each unit is relevant to the query. This two step approach is amenable to machine learning methods because each step can be cast as a classification problem. For example, noun phrase identification can be achieved by classifying each word into the start/middle/end/exterior of a noun phrase; sentence identification by classifying whether each period marks the of a sentence. Additionally, relevance judgment can be regarded as the classification of a pair of query and an information unit into a relevant-pair or non-relevant-pair. In QA and Novelty Tracks at TREC 2002, we studied the feasibility of this two step approach, using Support Vector Machines as the learning algorithm of the classifiers. Since many studies on identifying information units have already been reported, we concentrate on the relevance judgment step in QA and Novelty tasks in this paper
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KazawaHIM02.bib) "
	```
	@inproceedings{DBLP:conf/trec/KazawaHIM02,
		author = {Hideto Kazawa and Tsutomu Hirao and Hideki Isozaki and Eisaku Maeda},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Machine Learning Approach for {QA} and Novelty Tracks: {NTT} System Description},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/nttcom.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KazawaHIM02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2002 Web, Novelty and Filtering Track Experiments using PIRCS

_Kui-Lam Kwok, Peter Deng, Norbert Dinstl, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./novelty/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/queens.kwok.pdf](http://trec.nist.gov/pubs/trec11/papers/queens.kwok.pdf)
- :material-file-search: **Runs:** [pircs2N01](./novelty/runs.md#pircs2n01) | [pircs2N02](./novelty/runs.md#pircs2n02) | [pircs2N03](./novelty/runs.md#pircs2n03) | [pircs2N04](./novelty/runs.md#pircs2n04) | [pircs2N05](./novelty/runs.md#pircs2n05)

??? abstract "Abstract"
	
	In TREC2002, we participated in three tracks: web, novelty and adaptive filtering. The Web track has two tasks: distillation and named-page retrieval. Distillation is a new utility concept for ranking documents, and needs new design on the output document ranked list after an ad-hoc retrieval from the web (.gov) collection. Novelty track is a new task that involves identifying relevant sentences to a question, and to remove duplicate or non-novel entries in the answer list. The third track is adaptive filtering. We revived a filtering program that was functional at TREC-9 with some added capability. Sections 2, 3, 4 describe our participation in these tracks respectively. Section 5 has our conclusion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokDDC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokDDC02,
		author = {Kui{-}Lam Kwok and Peter Deng and Norbert Dinstl and M. Chan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2002 Web, Novelty and Filtering Track Experiments using {PIRCS}},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/queens.kwok.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokDDC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Filtering, Novelty Detection, and Named-Page Finding

_Kevyn Collins-Thompson, Paul Ogilvie, Yi Zhang, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [cmu_lti](./novelty/participants.md#cmu_lti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cmu.collins-thompson.pdf](http://trec.nist.gov/pubs/trec11/papers/cmu.collins-thompson.pdf)
- :material-file-search: **Runs:** [cmu02t300rCv](./novelty/runs.md#cmu02t300rcv) | [cmu02t300rCw](./novelty/runs.md#cmu02t300rcw) | [cmu02t300rCb](./novelty/runs.md#cmu02t300rcb) | [cmu02t300rBw](./novelty/runs.md#cmu02t300rbw) | [cmu02t300rAs](./novelty/runs.md#cmu02t300ras)

??? abstract "Abstract"
	
	In TREC 11, our group participated in the Novelty track, Filtering track, and the Named-Page Finding task of the Web track. This paper describes our approaches, experiments, and results. As the approach for each task is quite different, the paper contains a section for each of the tasks. The following section describes our experiments in adaptive filtering, Section 3 describes named-page finding, and section 4 discusses the Novelty track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Collins-ThompsonOZC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Collins-ThompsonOZC02,
		author = {Kevyn Collins{-}Thompson and Paul Ogilvie and Yi Zhang and Jamie Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Information Filtering, Novelty Detection, and Named-Page Finding},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cmu.collins-thompson.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Collins-ThompsonOZC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Novelty Track at IRIT-SIG

_Taoufiq Dkaki, Josiane Mothe, Jérôme Augé_

- :fontawesome-solid-user-group: **Participant:** [irit](./novelty/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/irit.novelty.pdf](http://trec.nist.gov/pubs/trec11/papers/irit.novelty.pdf)
- :material-file-search: **Runs:** [dumbrun](./novelty/runs.md#dumbrun)

??? abstract "Abstract"
	
	IRIT developed a new strategy in order to detect the relevant sentences that we did not try in a more general context of document retrieval but did try previously and partially in document categorization. In our approach a sentence is considered as relevant if it matches the topic with a certain level of coverage. This level of coverage depends on the category of the terms used in the texts. Three types of terms have been defined: highly relevant, lowly relevant and no relevant. With regard to the novelty part, a sentence is considered as novel when its levels of coverage with the previously processed sentences and with the best-matching sentences do not exceed certain thresholds.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DkakiMA02.bib) "
	```
	@inproceedings{DBLP:conf/trec/DkakiMA02,
		author = {Taoufiq Dkaki and Josiane Mothe and J{\'{e}}r{\^{o}}me Aug{\'{e}}},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Novelty Track at {IRIT-SIG}},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/irit.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DkakiMA02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THU TREC 2002: Novelty Track Experiments

_Min Zhang, Ruihua Song, Chuan Lin, Shaoping Ma, Zhe Jiang, Yijiang Jin, Yiqun Liu, Le Zhao_

- :fontawesome-solid-user-group: **Participant:** [tsinghua](./novelty/participants.md#tsinghua)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/tsinghuau.novelty2.pdf](http://trec.nist.gov/pubs/trec11/papers/tsinghuau.novelty2.pdf)
- :material-file-search: **Runs:** [thunv1](./novelty/runs.md#thunv1) | [thunv2](./novelty/runs.md#thunv2) | [thunv3](./novelty/runs.md#thunv3) | [thunv4](./novelty/runs.md#thunv4) | [thunv5](./novelty/runs.md#thunv5)

??? abstract "Abstract"
	
	This is the first time that Tsinghua University took part in TREC. In this year's novelty track, our basic idea is to find the key factor that help people find relevant and new information on a set of documents with noise. We paid attention to three points: 1. how to get full information from a short sentence; 2. how to complement hidden well-known knowledge to the sentences; 3. how to make the determination of duplication. Accordingly, expansion-based technologies are the key points. Studies of expansion technologies have been performed on three levels: efficient query expansion based on thesaurus and statistics, replacement-based document expansion, and term-expansion-related duplication elimination strategy based on overlapping measurement. Besides, two issues have been studied: finding key information in topics, and dynamic result selection. A new IR system has been developed for the task. In the system, four weighting strategies have been implemented: ltn.lnu [1], BM2500[2], FUB1 [3], FUB2 [3]. It provides both similarity and overlapping measurements, based on term expansion. Comparisons can be made on sentence-to-sentence or sentence-to-pool level.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangSLMJJLZ02.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangSLMJJLZ02,
		author = {Min Zhang and Ruihua Song and Chuan Lin and Shaoping Ma and Zhe Jiang and Yijiang Jin and Yiqun Liu and Le Zhao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THU} {TREC} 2002: Novelty Track Experiments},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/tsinghuau.novelty2.pdf},
		timestamp = {Wed, 16 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhangSLMJJLZ02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Some Similarity Computation Methods in Novelty Detection

_Ming-Feng Tsai, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [NTU](./novelty/participants.md#ntu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ntu.feng.final2.pdf](http://trec.nist.gov/pubs/trec11/papers/ntu.feng.final2.pdf)
- :material-file-search: **Runs:** [ntu1](./novelty/runs.md#ntu1) | [ntu2](./novelty/runs.md#ntu2) | [ntu3](./novelty/runs.md#ntu3)

??? abstract "Abstract"
	
	In the novelty task, the amount of information of a sentence that can be used in similarity computation is the major challenging issue. Some sort of information expansion methods was introduced to tackle this problem. Our approach to relevance identification was to expand the information of a sentence with the context of this sentence using a sliding window method. The similarity was measured by the number of words of a topic description that match the sentences within a window. Besides, WordNet was employed to relax word match operation to inexact match. In the novelty detection part, we first applied a coherent text segmentation algorithm to partition the sentences extracted from the relevance identification part into several coherent segments denoting sub-topics. Then we compute the similarity of each sentence with each segment. A sentence was in terms of a sentence-segment similarity vector. Two sentences are regarded as similar if they are related to the same sub-topics. In this way, the redundant sentences were filtered out.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TsaiC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/TsaiC02,
		author = {Ming{-}Feng Tsai and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Some Similarity Computation Methods in Novelty Detection},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/ntu.feng.final2.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TsaiC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Novelty Detection at Columbia University

_Barry Schiffman_

- :fontawesome-solid-user-group: **Participant:** [columbia_novelty](./novelty/participants.md#columbia_novelty)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/columbia.schiffman.pdf](http://trec.nist.gov/pubs/trec11/papers/columbia.schiffman.pdf)
- :material-file-search: **Runs:** [novcolcl35](./novelty/runs.md#novcolcl35) | [novcolclfx](./novelty/runs.md#novcolclfx) | [novcolmerg](./novelty/runs.md#novcolmerg) | [novcolsent](./novelty/runs.md#novcolsent) | [novcolcl85](./novelty/runs.md#novcolcl85)

??? abstract "Abstract"
	
	This paper describes the method we used for the Novelty Track for the 2002 Text Retrieval Conference (TREC). We tried to adapt tools we are developing for a task closely related to the novelty part of the this track. The system we are building will scan a stream of documents and present to the user only the new information it finds. For the 'relevance' part of the TREC, we decided to test the applicability of some of these tools. Since information retrieval is not a focus of our research, we thought it would be more interesting to use something new rather than try to hurriedly catch up. The results were far from satisfactory, but it is clear from the overall results that novelty detection remains a difficult and unsolved problem.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Schiffman02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Schiffman02,
		author = {Barry Schiffman},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments in Novelty Detection at Columbia University},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/columbia.schiffman.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Schiffman02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Michigan at TREC 2002: Question Answering and  Novelty Tracks

_Hong Qi, Jahna Otterbacher, Adam Winkel, Dragomir R. Radev_

- :fontawesome-solid-user-group: **Participant:** [umich](./novelty/participants.md#umich)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/umichigan.radev.pdf](http://trec.nist.gov/pubs/trec11/papers/umichigan.radev.pdf)
- :material-file-search: **Runs:** [umich1](./novelty/runs.md#umich1) | [UMICH4](./novelty/runs.md#umich4) | [UMich3](./novelty/runs.md#umich3) | [UMich5](./novelty/runs.md#umich5) | [UMIch2](./novelty/runs.md#umich2)

??? abstract "Abstract"
	
	The University of Michigan participated in two evaluations this year. In the Question Answering Track, we entered three different versions of our system, NSIR, previously described in (1. For the Novelty Track, we modified our multi-document summarizer, MEAD (www.summarization.com/mead) and submitted five runs with different input parameters.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QiOWR02.bib) "
	```
	@inproceedings{DBLP:conf/trec/QiOWR02,
		author = {Hong Qi and Jahna Otterbacher and Adam Winkel and Dragomir R. Radev},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Michigan at {TREC} 2002: Question Answering and Novelty Tracks},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/umichigan.radev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QiOWR02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Crude Cut at Query Expansion

_Philip Rennert_

- :fontawesome-solid-user-group: **Participant:** [streamsage](./novelty/participants.md#streamsage)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/streamsage.rennert.pdf](http://trec.nist.gov/pubs/trec11/papers/streamsage.rennert.pdf)
- :material-file-search: **Runs:** [ss1](./novelty/runs.md#ss1)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Rennert02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Rennert02,
		author = {Philip Rennert},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Crude Cut at Query Expansion},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/streamsage.rennert.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Rennert02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at TREC 2002

_Christof Monz, Jaap Kamps, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [uva](./novelty/participants.md#uva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uamsterdam.derijke.pdf](http://trec.nist.gov/pubs/trec11/papers/uamsterdam.derijke.pdf)
- :material-file-search: **Runs:** [UAmsT11ntste](./novelty/runs.md#uamst11ntste) | [UAmsT11ntlem](./novelty/runs.md#uamst11ntlem) | [UAmsT11ntcom](./novelty/runs.md#uamst11ntcom)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2002 Novelty, Question answering, and Web tracks. We provide a detailed account of the ideas underlying our approaches to these tasks. All our runs used the FlexIR information retrieval system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MonzKR02.bib) "
	```
	@inproceedings{DBLP:conf/trec/MonzKR02,
		author = {Christof Monz and Jaap Kamps and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Amsterdam at {TREC} 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/uamsterdam.derijke.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MonzKR02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2002: Cross Language and Novelty Tracks

_Leah S. Larkey, James Allan, Margaret E. Connell, Alvaro Bolivar, Courtney Wade_

- :fontawesome-solid-user-group: **Participant:** [umass](./novelty/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/umass.wade.pdf](http://trec.nist.gov/pubs/trec11/papers/umass.wade.pdf)
- :material-file-search: **Runs:** [CIIR02tfkl](./novelty/runs.md#ciir02tfkl) | [CIIR02tfnew](./novelty/runs.md#ciir02tfnew)

??? abstract "Abstract"
	
	The University of Massachusetts participated in the cross-language and novelty tracks this year. The cross-language submission was characterized by combination of evidence to merge results from two different retrieval engines and a variety of different resources - stemmers, dictionaries, machine translation, and an acronym database. We found that proper names were extremely important in this year's queries. For the novelty track, we applied variants of techniques that have been employed for other problems. In addition, we created additional training data by manually annotating 48 additional topics.
	

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

## Interactive 

#### TREC 2002 Interactive Track Report

_William R. Hersh_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/INTERACTIVE.OHSU.pdf](http://trec.nist.gov/pubs/trec11/papers/INTERACTIVE.OHSU.pdf)
??? abstract "Abstract"
	
	For TREC 2002, the Interactive Track completed the two-year cycle of observational studies begun in TREC 2001 and followed now by more controlled laboratory experiments focusing on question answering using Web data. Six research groups participated this year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Hersh02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Hersh02,
		author = {William R. Hersh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2002 Interactive Track Report},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/INTERACTIVE.OHSU.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Hersh02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at the Web Track of TREC 2002

_Vassilis Plachouras, Iadh Ounis, Gianni Amati, C. J. van Rijsbergen_

- :fontawesome-solid-user-group: **Participant:** [glasgow](./interactive/participants.md#glasgow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/glasgow.web.pdf](http://trec.nist.gov/pubs/trec11/papers/glasgow.web.pdf)

??? abstract "Abstract"
	
	The aim of our participation in the topic distillation and the named page finding tasks of the Web track is the evaluation of a well-founded modular probabilistic framework for Web Information Retrieval, which integrates content and link analyses. The link analysis component of the framework employs a new probabilistic approach, called the Absorbing Model, for calculating a measure of popularity for documents induced from the Web graph. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PlachourasOAR02.bib) "
	```
	@inproceedings{DBLP:conf/trec/PlachourasOAR02,
		author = {Vassilis Plachouras and Iadh Ounis and Gianni Amati and C. J. van Rijsbergen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at the Web Track of {TREC} 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/glasgow.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PlachourasOAR02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### More Statistical Power Needed: The OHSU TREC 2002 Interactive  Track Experiments

_William R. Hersh, Susan Moy, Dale Kraemer, Lynetta Sacherek, Daniel Olson_

- :fontawesome-solid-user-group: **Participant:** [OHSU](./interactive/participants.md#ohsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ohsu.pdf](http://trec.nist.gov/pubs/trec11/papers/ohsu.pdf)
- :material-file-search: **Runs:** [IOHSU](./interactive/runs.md#iohsu)

??? abstract "Abstract"
	
	The original goal for the Oregon Health & Science University (OHSU) TREC 2002 Interactive Track experiments was to perform some preliminary experiments comparing searching on tablet devices versus ordinary personal computers. Unfortunately, the vendor who had promised the devices we planned to use was unable to deliver them in time for the experiments. We therefore shifted our experimental focus to assessing user factors found in previous experiments to be associated with success, with a particular desire to assess the role of spatial visualization. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershMKSO02.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershMKSO02,
		author = {William R. Hersh and Susan Moy and Dale Kraemer and Lynetta Sacherek and Daniel Olson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {More Statistical Power Needed: The {OHSU} {TREC} 2002 Interactive Track Experiments},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/ohsu.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HershMKSO02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Rutgers Interactive Track at TREC 2002

_Nicholas J. Belkin, Diane Kelly, G. Kim, Ja-Young Kim, Hyuk-Jin Lee, Gheorghe Muresan, Muh-Chyun (Morris) Tang, Xiaojun Yuan, Colleen Cool_

- :fontawesome-solid-user-group: **Participant:** [rutgers_belkin](./interactive/participants.md#rutgers_belkin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/rutgers.belkin.pdf](http://trec.nist.gov/pubs/trec11/papers/rutgers.belkin.pdf)
- :material-file-search: **Runs:** [IRutgers](./interactive/runs.md#irutgers)

??? abstract "Abstract"
	
	Two important results came out of our investigations in the TREC 2001 Interactive Track (Belkin, et al., 2002). One was that the greater the amount of interaction that searchers engaged in, the lower their satisfaction with the results of the search. We understood this to mean that interaction effort was inversely related to search satisfaction, and therefore, that making interaction more effective would lead to increased search satisfaction. The second was that performance in the searching task increased with query length. We conjectured that this was due, at least in part, to the subjects having searched using a best-match search engine (Excite1 ), as well as longer queries being better able to express the information problem. These two findings became the basis for our systems and experiments in the TREC 2002 Interactive Track. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BelkinKKKLMTYC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/BelkinKKKLMTYC02,
		author = {Nicholas J. Belkin and Diane Kelly and G. Kim and Ja{-}Young Kim and Hyuk{-}Jin Lee and Gheorghe Muresan and Muh{-}Chyun (Morris) Tang and Xiaojun Yuan and Colleen Cool},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Rutgers Interactive Track at {TREC} 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/rutgers.belkin.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BelkinKKKLMTYC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Augmenting and Limiting Search Queries

_Elaine G. Toms, Luanne Freund, Cara Li_

- :fontawesome-solid-user-group: **Participant:** [toronto](./interactive/participants.md#toronto)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/utoronto.toms.pdf](http://trec.nist.gov/pubs/trec11/papers/utoronto.toms.pdf)
- :material-file-search: **Runs:** [IToronto](./interactive/runs.md#itoronto)

??? abstract "Abstract"
	
	Web queries tend to be significantly shorter and less complex than queries used in earlier types of information systems (Jansen & Pooch, 2000; Lawrence & Giles, 1999; Spink et al, 2001). Yet, there is general belief that enriched queries and query reformulation will lead to improved results (Belkin et al, 2001). In our research we are examining the sorts of tools that could assist with the creation of enriched queries and in turn improve the search process and the user's search experience. In the work reported here we assessed the use of two types of tools: one to assist the user in targeting and, thus, restricting the query, and a second one to assist in augmenting the query. We speculated that certain types of tools are more useful for certain types of information tasks. In particular we targeted the standard informational request in which a suitable response could be culled from many different Web pages, and secondly, the ‘know-item' task, in which a specific Website exists to solve the problem. We anticipated that the tool to enable query augmentation would be more useful for informational tasks, as it would encourage amplification of the query to contain many more words and phrases that represent the information task. On the other hand, ‘know-item' searches suffer when the exact title or some exact content is not known in advance and the limiter would enable more focussed searches. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TomsFL02.bib) "
	```
	@inproceedings{DBLP:conf/trec/TomsFL02,
		author = {Elaine G. Toms and Luanne Freund and Cara Li},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Augmenting and Limiting Search Queries},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/utoronto.toms.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TomsFL02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 11 Web and Interactive Tracks at CSIRO

_Nick Craswell, David Hawking, Ross Wilkinson, Mingfang Wu, James A. Thom, Trystan Upstill_

- :fontawesome-solid-user-group: **Participant:** [CSIRO](./interactive/participants.md#csiro)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/csiro.craswell.pdf](http://trec.nist.gov/pubs/trec11/papers/csiro.craswell.pdf)
- :material-file-search: **Runs:** [Icsiro](./interactive/runs.md#icsiro)

??? abstract "Abstract"
	
	This year, the CSIRO teams participated and completed runs in two tracks: web and interactive. Our web track participation was a preliminary exploration of forms of evidence which might be useful for named page finding and topic distillation. For this reason, we made heavy use of evidence other than page content in our runs. In the interactive track, we continue to focus on answer organization issues, aiming to investigate the usefulness of the knowledge about “organizational structure” in organizing and delivering the retrieved documents. For the collection of the US government (.gov domain) web documents, we used their level two domain labels and their corresponding organization names to categorize the retrieved documents. For example, documents from the 'nih.gov' domain will be put into the 'National Institutes of Health (nih)' category. We compared this delivery method with the traditional ranked list. The preliminary results indicate that subjects achieved a significantly better performance with the category interface at the end of fifteen minutes search, however, there is no significant difference between the two methods during the first five or ten minutes. The experiment result also shows that the category interface assisted subjects answer the more complex topics as time increases.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellHWWTU02.bib) "
	```
	@inproceedings{DBLP:conf/trec/CraswellHWWTU02,
		author = {Nick Craswell and David Hawking and Ross Wilkinson and Mingfang Wu and James A. Thom and Trystan Upstill},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 11 Web and Interactive Tracks at {CSIRO}},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/csiro.craswell.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CraswellHWWTU02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Video 

#### The TREC-2002 Video Track Report

_Alan F. Smeaton, Paul Over_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/VIDEO.OVER.pdf](http://trec.nist.gov/pubs/trec11/papers/VIDEO.OVER.pdf)
??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmeatonO02.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmeatonO02,
		author = {Alan F. Smeaton and Paul Over},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {TREC-2002} Video Track Report},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/VIDEO.OVER.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmeatonO02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC 2002: Filtering, Q&A, Web and Video Tasks

_Lide Wu, Xuanjing Huang, Junyu Niu, Yingju Xia, Zhe Feng, Yaqian Zhou_

- :fontawesome-solid-user-group: **Participant:** [Fudan](./video/participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf](http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf)
- :material-file-search: **Runs:** [VFudan](./video/runs.md#vfudan)

??? abstract "Abstract"
	
	This year Fudan University takes part in the TREC conference for the third time. We have participated in four tracks of Filtering, Q&A, Web and Video. For filtering, we only participate in the sub-task of adaptive filtering. A novel method is presented, in which a winnow classifier from the description and narrative fields is constructed, and then utilized to assist our previous adaptive filtering system. A novel approach to confidence sorting, which is based on Maximum Entropy, is proposed in our Question Answering system. The rank of individual answer is determined by several weighted factors, and the confidence score is the product of the exponent of the weights of every factors. The weight of every factor is assigned during the training of previous questions. To return highly relevant key resources for web retrieval, we modified our original search system to make it return higher precision result than before. First, we proposed a novel search algorithm to get a base set of highly relevant documents. Then special post-processing modules are used to expand and re-sort the base set. This year we tried a fast manifold-based approach to face recognition in the Video Search Task. It can be used when there are only few different images of a specific person and runs fast. Experiment shows that applying this step will make the face recognition 5-fold faster and with almost no decreasing of performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHNXFZ02.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHNXFZ02,
		author = {Lide Wu and Xuanjing Huang and Junyu Niu and Yingju Xia and Zhe Feng and Yaqian Zhou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FDU} at {TREC} 2002: Filtering, Q{\&}A, Web and Video Tasks},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHNXFZ02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Video Indexing and Retrieval at UMD

_Christian Wolf, David S. Doermann, Mika Rautiainen_

- :fontawesome-solid-user-group: **Participant:** [umd_oard](./video/participants.md#umd_oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/umd.doermann.pdf](http://trec.nist.gov/pubs/trec11/papers/umd.doermann.pdf)
- :material-file-search: **Runs:** [VUMD](./video/runs.md#vumd)

??? abstract "Abstract"
	
	Our team from the University of Maryland and INSA de Lyon participated in the feature extraction evaluation with overlay text features and in the search evaluation with a query retrieval and browsing system. For search we developed a weighted query mechanism by integrating 1) text (OCR and speech recognition) content using full text and n-grams through the MG system, 2) color correlogram indexing of image and video shots reported last year in TREC, and 3) ranked versions of the extracted binary features. A command line version of the interface allows users to formulate simple queries, store them and use weighted combinations of the simple queries to generate compound queries. One novel component of our interactive approach is the ability for the users to formulate dynamic queries previously developed for database applications at Maryland. The interactive interface treats each video clip as visual object in a multi-dimensional space, and each ”feature” of that clip is mapped to one dimension. The user can visualize any two dimensions by placing any two features on the horizontal and vertical axis with additional dimensions visualized by adding attributes to each object.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WolfDR02.bib) "
	```
	@inproceedings{DBLP:conf/trec/WolfDR02,
		author = {Christian Wolf and David S. Doermann and Mika Rautiainen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Video Indexing and Retrieval at {UMD}},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/umd.doermann.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WolfDR02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CWI at the TREC 2002 Video Track

_Thijs Westerveld, Arjen P. de Vries, Alex van Ballegooij_

- :fontawesome-solid-user-group: **Participant:** [cwi](./video/participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cwi.westerveld.pdf](http://trec.nist.gov/pubs/trec11/papers/cwi.westerveld.pdf)
- :material-file-search: **Runs:** [VCWI](./video/runs.md#vcwi)

??? abstract "Abstract"
	
	We present a probabilistic model for the retrieval of multimodal documents. The model is based on Bayesian decision theory and combines models for text based search with models for visual search. The textual model, applied to the LIMSI transcripts, is based on the language modelling approach to text retrieval. The visual model, a mixture of Gaussian densities, describes keyframes selected from shots. Both models have proved successful on media specific retrieval tasks. Our contribution is the combination of both techniques in a unified model, ranking shots on ASR-data and visual features simultaneously. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WesterveldVB02.bib) "
	```
	@inproceedings{DBLP:conf/trec/WesterveldVB02,
		author = {Thijs Westerveld and Arjen P. de Vries and Alex van Ballegooij},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CWI} at the {TREC} 2002 Video Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cwi.westerveld.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WesterveldVB02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC Feature Extraction by Active Learning

_Jeroen Vendrig, Ioannis Patras, Cees Snoek, Marcel Worring, Jurgen den Hartog, Stephan Raaijmakers, Jeroen van Rest, David A. van Leeuwen_

- :fontawesome-solid-user-group: **Participant:** [amsterdam_isis](./video/participants.md#amsterdam_isis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/mediamill.vendrig.pdf](http://trec.nist.gov/pubs/trec11/papers/mediamill.vendrig.pdf)
- :material-file-search: **Runs:** [Vworring](./video/runs.md#vworring)

??? abstract "Abstract"
	
	[...] We present a system which interactively learns user-defined semantic concepts for a specific collection from a domain expert. For each concept, the domain expert builds a model by feeding visual evidence to the system in the form of examples, without knowledge about the underlying classifier and descriptors. We employ a large set of multimedia descriptors for use in a Maximum Entropy classifier. The space for example selection is determined by the output of the incrementally improved model. The system is evaluated against the TREC 2002 feature extraction collection. The user information consists of the ten semantic concepts defined for the feature extraction task. As our system is based on visual evidence, we focus on visual content of videos. That is, we focus on the features outdoors, indoors, face, people, cityscape, landscape, text overlay and monologue. The classification of the audio features (speech and instrumental sound) is provided independently and is described briefly in section 2.2. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VendrigPSWHRRL02.bib) "
	```
	@inproceedings{DBLP:conf/trec/VendrigPSWHRRL02,
		author = {Jeroen Vendrig and Ioannis Patras and Cees Snoek and Marcel Worring and Jurgen den Hartog and Stephan Raaijmakers and Jeroen van Rest and David A. van Leeuwen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} Feature Extraction by Active Learning},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/mediamill.vendrig.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VendrigPSWHRRL02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Semantic Feature Extraction using Mpeg Macro-block Classification

_Fabrice Souvannavong, Bernard Mérialdo, Benoit Huet_

- :fontawesome-solid-user-group: **Participant:** [eurecom](./video/participants.md#eurecom)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/eurecom.fabrice.pdf](http://trec.nist.gov/pubs/trec11/papers/eurecom.fabrice.pdf)
- :material-file-search: **Runs:** [Veurecom](./video/runs.md#veurecom)

??? abstract "Abstract"
	
	In this paper, we present some first results in the extraction of semantic features from video sequences. Our approach is based on the classification of Mpeg DCT macro-blocks. Although it is clear that using macro-blocks imposes severe restrictions on the analysis accuracy of the image, it has the advantage of avoiding the complete decoding of the Mpeg stream. Our objective is to evaluate the quality of the Semantic Feature Extraction that can be obtained with this direct approach, to serve as a comparative baseline with more elaborate approaches.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SouvannavongMH02.bib) "
	```
	@inproceedings{DBLP:conf/trec/SouvannavongMH02,
		author = {Fabrice Souvannavong and Bernard M{\'{e}}rialdo and Benoit Huet},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Semantic Feature Extraction using Mpeg Macro-block Classification},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/eurecom.fabrice.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SouvannavongMH02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2002 Video Track Experiments at MediaTeam Oulu and VTT

_Mika Rautiainen, Dmitri Vorobiev, Kai Noponen, Pertti Alvar Väyrynen, Matti Hosio, Esa Matinmikko, Timo Ojala, Tapio Seppänen, Jani Penttilä, Satu-Marja Mäkelä, Johannes Peltola_

- :fontawesome-solid-user-group: **Participant:** [oulu](./video/participants.md#oulu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uoulu.rautiainen.pdf](http://trec.nist.gov/pubs/trec11/papers/uoulu.rautiainen.pdf)
- :material-file-search: **Runs:** [VOulu](./video/runs.md#voulu)

??? abstract "Abstract"
	
	In TREC 2002 Video Track MediaTeam Oulu and VTT Technical Research Centre of Finland participated jointly in semantic feature extraction, manual search and interactive search tasks. In the semantic feature extraction task, we sent results for semantic categories of cityscape, landscape, people, speech and instrumental sound. Spatio-temporal correlation of oriented gradient occurrences was used with example shots to detect shots containing people, cityscape or landscape. The audio signal features consisted of various statistical measurements and were used to detect shots containing speech or instrumental sound. Our video browsing and retrieval system, VIRE, was used for manual and interactive search tasks. Our system offers two techniques for video retrieval: 1. Multi-modal indexing based on self-organizing feature maps with semantic filtering. 2. An interactive navigating tool that combines two inter-shot properties, temporal coherency and metric similarities, into a view where database shots are presented in a lattice structure. We tested our interactive navigating tool with eight persons to obtain results for 25 pre-defined search topics. In this paper we give an overview of the approaches and a summary of the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RautiainenVNVHMOSPMP02.bib) "
	```
	@inproceedings{DBLP:conf/trec/RautiainenVNVHMOSPMP02,
		author = {Mika Rautiainen and Dmitri Vorobiev and Kai Noponen and Pertti Alvar V{\"{a}}yrynen and Matti Hosio and Esa Matinmikko and Timo Ojala and Tapio Sepp{\"{a}}nen and Jani Penttil{\"{a}} and Satu{-}Marja M{\"{a}}kel{\"{a}} and Johannes Peltola},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2002 Video Track Experiments at MediaTeam Oulu and {VTT}},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/uoulu.rautiainen.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RautiainenVNVHMOSPMP02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLIPS at TREC 11: Experiments in Video Retrieval

_Georges Quénot, Daniel Moraru, Laurent Besacier, Philippe Mulhem_

- :fontawesome-solid-user-group: **Participant:** [clips-imag](./video/participants.md#clips-imag)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/clips.video.pdf](http://trec.nist.gov/pubs/trec11/papers/clips.video.pdf)
- :material-file-search: **Runs:** [Vclips](./video/runs.md#vclips)

??? abstract "Abstract"
	
	This pap er presents the systems used by CLIPS-IMAG to p erform the Shot Boundary Detection (SBD) task, the Feature Extraction (FE) and the Search (S) task of the Video track of the TREC-11 conference. Results obtained for the TREC-11 evaluation are presented.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QuenotMBM02.bib) "
	```
	@inproceedings{DBLP:conf/trec/QuenotMBM02,
		author = {Georges Qu{\'{e}}not and Daniel Moraru and Laurent Besacier and Philippe Mulhem},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CLIPS} at {TREC} 11: Experiments in Video Retrieval},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/clips.video.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QuenotMBM02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Video Retrieval Using Global Features in Keyframes

_Marcus Jerome Pickering, Daniel Heesch, Stefan M. Rüger, Robert J. O'Callaghan, David R. Bull_

- :fontawesome-solid-user-group: **Participant:** [imperial](./video/participants.md#imperial)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/imperial.pickering.pdf](http://trec.nist.gov/pubs/trec11/papers/imperial.pickering.pdf)
- :material-file-search: **Runs:** [VImperial](./video/runs.md#vimperial)

??? abstract "Abstract"
	
	We describe our experiments for the shot-boundary detection and search tasks for the TREC-11 video track. Our shot-boundary detection scheme is based on a multi-timescale detection algorithm in which colour histogram differences are examined over a range of frames. Our search efforts are based on a system which brings together a number of global features encompassing colour, texture and text features derived from speech recognition transcripts into a unique relevance feedback system. 
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PickeringHROB02.bib) "
	```
	@inproceedings{DBLP:conf/trec/PickeringHROB02,
		author = {Marcus Jerome Pickering and Daniel Heesch and Stefan M. R{\"{u}}ger and Robert J. O'Callaghan and David R. Bull},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Video Retrieval Using Global Features in Keyframes},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/imperial.pickering.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PickeringHROB02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Automatic Shot Boundary Detection and Classification of Indoor and  Outdoor Scenes

_Andrea Miene, Thorsten Hermes, George T. Ioannidis, R. Fathi, Otthein Herzog_

- :fontawesome-solid-user-group: **Participant:** [ubremen](./video/participants.md#ubremen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ubremen.miene.pdf](http://trec.nist.gov/pubs/trec11/papers/ubremen.miene.pdf)
- :material-file-search: **Runs:** [VBremen](./video/runs.md#vbremen)

??? abstract "Abstract"
	
	This paper describes our contribution to the TREC 2002 video analysis track. We participated in the shot detection task and in the feature extraction task (features indoors and outdoors). The shot detection approach is based on histogram differences and uses adaptive thresholds. Multiple detected shot boundaries that follow each other within a short temporal interval are grouped together and classified as a gradual change beginning with the first and ending with the last shot boundary in the interval. For the feature extraction task we examined whether it is possible to classify indoor and outdoor shots by their color distribution. In order to analyze the color distribution we use first order statistical features. The shots are classified into indoor and outdoor shots using a neural net.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MieneHIFH02.bib) "
	```
	@inproceedings{DBLP:conf/trec/MieneHIFH02,
		author = {Andrea Miene and Thorsten Hermes and George T. Ioannidis and R. Fathi and Otthein Herzog},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Automatic Shot Boundary Detection and Classification of Indoor and Outdoor Scenes},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/ubremen.miene.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MieneHIFH02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM Research TREC 2002 Video Retrieval System

_Bill Adams, Giridharan Iyengar, Chalapathy Neti, Harriet J. Nock, Arnon Amir, Haim H. Permuter, Savitha Srinivasan, Chitra Dorai, Alejandro Jaimes, Christian A. Lang, Ching-Yung Lin, Apostol Natsev, Milind R. Naphade, John R. Smith, Belle L. Tseng, Sugata Ghosal, Raghavendra Singh, T. V. Ashwin, DongQing Zhang_

- :fontawesome-solid-user-group: **Participant:** [ibm-video](./video/participants.md#ibm-video)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ibm.smith.vid.pdf](http://trec.nist.gov/pubs/trec11/papers/ibm.smith.vid.pdf)
- :material-file-search: **Runs:** [VIBM](./video/runs.md#vibm)

??? abstract "Abstract"
	
	In this paper, we describe the IBM Research system for analysis, indexing, and retrieval of video, which was applied to the TREC-2002 video retrieval benchmark. The system explores novel methods for fully-automatic content analysis, shot boundary detection, multi-modal feature extraction, statistical modeling for semantic concept detection, and speech recognition and indexing. The system supports querying based on automatically extracted features, models, and speech information. Additional interactive methods for querying include multiple-example and relevance feedback searching, cluster, concept, and storyboard browsing, and iterative fusion based on user-selected aggregation and combination functions. The system was applied to all four of the tasks of the video retrieval benchmark including shot boundary detection, concept detection, concept exchange, and search. We describe the approaches for each of the tasks and discuss some of the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AdamsINNAPSDJLLNNSTGSAZ02.bib) "
	```
	@inproceedings{DBLP:conf/trec/AdamsINNAPSDJLLNNSTGSAZ02,
		author = {Bill Adams and Giridharan Iyengar and Chalapathy Neti and Harriet J. Nock and Arnon Amir and Haim H. Permuter and Savitha Srinivasan and Chitra Dorai and Alejandro Jaimes and Christian A. Lang and Ching{-}Yung Lin and Apostol Natsev and Milind R. Naphade and John R. Smith and Belle L. Tseng and Sugata Ghosal and Raghavendra Singh and T. V. Ashwin and DongQing Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IBM} Research {TREC} 2002 Video Retrieval System},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/ibm.smith.vid.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AdamsINNAPSDJLLNNSTGSAZ02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Video Searching and Browsing Using Viewfinder

_Dan E. Albertson, Javed Mostafa, John Fieber_

- :fontawesome-solid-user-group: **Participant:** [indiana](./video/participants.md#indiana)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/indianau.albertson.pdf](http://trec.nist.gov/pubs/trec11/papers/indianau.albertson.pdf)
- :material-file-search: **Runs:** [VIndiana](./video/runs.md#vindiana)

??? abstract "Abstract"
	
	Several researchers consisting of students and faculty from the School of Library and Information Science at Indiana University developed a video retrieval system named ViewFinder for the purpose of providing access to video content for a project named the Cultural digital Library Indexing Our Heritage (CLIOH) at Indiana University Purdue University at Indianapolis (IUPUI). For our role in the Text Retrieval Conference (TREC) and its video track, we took the existing system, made notable modifications, and applied it to the video data provided by the conference. After conducting 1 interactive search run, we generated our search results and submitted them to TREC where human judges determined the relevancy of each returned shot and assigned an averaged precision ranking for each topic. From these results we were capable of drawing conclusions of the current system, and how to make ViewFinder more productive in future versions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlbertsonMF02.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlbertsonMF02,
		author = {Dan E. Albertson and Javed Mostafa and John Fieber},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Video Searching and Browsing Using Viewfinder},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/indianau.albertson.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlbertsonMF02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Dublin City University Video Track Experiments for TREC 2002

_Paul Browne, Csaba Czirjek, Cathal Gurrin, Roman Jarina, Hyowon Lee, Seán Marlow, Kieran McDonald, Noel Murphy, Noel E. O'Connor, Alan F. Smeaton, Jiamin Ye_

- :fontawesome-solid-user-group: **Participant:** [dublin](./video/participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/dublincu.smeaton.pdf](http://trec.nist.gov/pubs/trec11/papers/dublincu.smeaton.pdf)
- :material-file-search: **Runs:** [VDublin](./video/runs.md#vdublin)

??? abstract "Abstract"
	
	Dublin City University participated in the Feature Extraction task and the Search task of the TREC-2002 Video Track. In the Feature Extraction task, we submitted 3 features: Face, Speech, and Music. In the Search task, we developed an interactive video retrieval system, which incorporated the 40 hours of the video search test collection and supported user searching using our own feature extraction data along with the donated feature data and ASR transcript from other Video Track groups. This video retrieval system allows a user to specify a query based on the 10 features and ASR transcript, and the query result is a ranked list of videos that can be further browsed at the shot level. To evaluate the usefulness of the feature-based query, we have developed a second system interface that provides only ASR transcript-based querying, and we conducted an experiment with 12 test users to compare these 2 systems. Results were submitted to NIST and we are currently conducting further analysis of user performance with these 2 systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BrowneCGJLMMMOSY02.bib) "
	```
	@inproceedings{DBLP:conf/trec/BrowneCGJLMMMOSY02,
		author = {Paul Browne and Csaba Czirjek and Cathal Gurrin and Roman Jarina and Hyowon Lee and Se{\'{a}}n Marlow and Kieran McDonald and Noel Murphy and Noel E. O'Connor and Alan F. Smeaton and Jiamin Ye},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Dublin City University Video Track Experiments for {TREC} 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/dublincu.smeaton.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BrowneCGJLMMMOSY02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Temporal Multi-Resolution Framework for Shot Boundary Detection and  Keyframe Extraction

_A. Chandrashekhara, HuaMin Feng, Tat-Seng Chua_

- :fontawesome-solid-user-group: **Participant:** [singapre_hui](./video/participants.md#singapre_hui)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/nus.video.pdf](http://trec.nist.gov/pubs/trec11/papers/nus.video.pdf)
- :material-file-search: **Runs:** [VNUS](./video/runs.md#vnus)

??? abstract "Abstract"
	
	Video shot boundary detection and keyframe extraction is an important step in many video-processing applications. We observe that video shot boundary is a multi-resolution edge phenomenon in the feature space. In this experiment, we expanded our previous temporal multi-resolution analysis (TMRA) work by introducing the new feature vector based on motion, incorporating functions to detect flash and camera/object motion, and selecting automatic thresholds for noise elimination based on the type of video. The framework is used to extract meaningful keyframes. Experiments show that our new system can detect and characterize both the abrupt (CUT) and gradual (GT) transitions effectively. It has good accuracy for both the detection of transitions as well as their boundaries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChandrashekharaFC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChandrashekharaFC02,
		author = {A. Chandrashekhara and HuaMin Feng and Tat{-}Seng Chua},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Temporal Multi-Resolution Framework for Shot Boundary Detection and Keyframe Extraction},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/nus.video.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChandrashekharaFC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Video Classification and Retrieval with the Informedia Digital Video  Library System

_Alexander G. Hauptmann, Rong Yan, Yanjun Qi, Rong Jin, Michael G. Christel, Mark Derthick, Ming-Yu Chen, Robert V. Baron, Wei-Hao Lin, Tobun D. Ng_

- :fontawesome-solid-user-group: **Participant:** [cmu-Hauptmann-video](./video/participants.md#cmu-hauptmann-video)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cmu.hauptmann.pdf](http://trec.nist.gov/pubs/trec11/papers/cmu.hauptmann.pdf)
- :material-file-search: **Runs:** [VCMU](./video/runs.md#vcmu)

??? abstract "Abstract"
	
	This paper is organized in three parts. The first part details some of the lower level shot classification work, the second part describes the ‘manual' retrieval systems while the last section details the interactive retrieval system for the Carnegie Mellon University TREC Video Retrieval Track runs. The description of the data can be found elsewhere in the proceedings of the 2002 TREC conference video track overview
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HauptmannYQJCDCBLN02.bib) "
	```
	@inproceedings{DBLP:conf/trec/HauptmannYQJCDCBLN02,
		author = {Alexander G. Hauptmann and Rong Yan and Yanjun Qi and Rong Jin and Michael G. Christel and Mark Derthick and Ming{-}Yu Chen and Robert V. Baron and Wei{-}Hao Lin and Tobun D. Ng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Video Classification and Retrieval with the Informedia Digital Video Library System},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cmu.hauptmann.pdf},
		timestamp = {Thu, 16 Dec 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HauptmannYQJCDCBLN02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Shot Boundary Detection Using the Moving Query Window

_Seyed M. M. Tahaghoghi, James A. Thom, Hugh E. Williams_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./video/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/rmit.ps.gz](http://trec.nist.gov/pubs/trec11/papers/rmit.ps.gz)
- :material-file-search: **Runs:** [VRMIT](./video/runs.md#vrmit)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TahaghoghiTW02.bib) "
	```
	@inproceedings{DBLP:conf/trec/TahaghoghiTW02,
		author = {Seyed M. M. Tahaghoghi and James A. Thom and Hugh E. Williams},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Shot Boundary Detection Using the Moving Query Window},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/rmit.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TahaghoghiTW02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

