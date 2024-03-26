# Proceedings - Chinese 1997 

#### Chinese Document Retrieval at TREC-6

_Ross Wilkinson_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/csiro.chinese.ps.gz](http://trec.nist.gov/pubs/trec6/papers/csiro.chinese.ps.gz)
??? abstract "Abstract"
	
	In the Chinese language each character represents at least a complete syllable, rather than a letter as in other languages. Many characters are also single syllable words. The total number of characters is therefore quite large and somewhat ill-defined. A literate adult would typically recognise at least 5-6,000 characters. The various modern standards define between 10-12,000 characters, although if early and ancient literature is included the number rises to approximately 100,000. Chinese is agglutinating - there is no space between consecutive characters, except perhaps, at the end of a sentence. Thus to perform retrieval in Chinese, the basis has to be characters unless the text is pre-segmented into words. Segmentation is difficult - not even humans will always agree on correct segmentation, and there has been much research in successful segmentation of Chinese [1].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Wilkinson97.bib) "
	```
	@inproceedings{DBLP:conf/trec/Wilkinson97,
		author = {Ross Wilkinson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Chinese Document Retrieval at {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {25--29},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/csiro.chinese.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Wilkinson97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments on Proximity Based Chinese Text Retrieval in TREC 6

_K. Rajaraman, Kok F. Lai, Y. Changwen_

- :fontawesome-solid-user-group: **Participant:** [ITI-SG](./participants.md#iti-sg)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/itich.ps.gz](http://trec.nist.gov/pubs/trec6/papers/itich.ps.gz)
- :material-file-search: **Runs:** [itich1](./runs.md#itich1) | [itich2](./runs.md#itich2) | [itich3](./runs.md#itich3)

??? abstract "Abstract"
	
	In TREC 6, we participate in the Chinese track and report our experiments on proximity based text retrieval. Our participation this year concentrates on automatic retrieval methods natural for the Chinese language. We index the documents by treating every Chinese character as a single term and store positional information for all terms. During retrieval we employ a proximity operator that uses the positional information in the index, to rank the documents. The operator is defined such that documents are scored in proportion to the proximity of characters as they appear in the query. Since we only use the proximity of characters to compute the score, the algorithm does not strictly require the word boundaries be known a priori. In particular, phrase detection can be derived as a special case of our algorithm by giving maximum score when the characters are immediately adjacent and 0 otherwise. This indexing and retrieval scheme is significantly different from our TREC 5 method. We submit three official runs itich1, itich2 and itich3 for TREC 6. For itich3, we use all phrases from the Description field and compute scores with our proximity operator. The runs itichi and itich2 are obtained through automatic query expansion methods. We dynamically build a 3-gram phrase dictionary from top 20 documents for each query ranked in itich3 and pick phrases to expand from this dictionary using document frequency estimates. The run itich2 is different from itich1 in that the expanded phrases are filtered to remove duplicate and common phrases.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RajaramanLC97.bib) "
	```
	@inproceedings{DBLP:conf/trec/RajaramanLC97,
		author = {K. Rajaraman and Kok F. Lai and Y. Changwen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Experiments on Proximity Based Chinese Text Retrieval in {TREC} 6},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {559--576},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/itich.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RajaramanLC97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Between Terms and Words for European Language IR and Between Words  and Bigrams for Chinese IR

_Jian-Yun Nie, Jean-Pierre Chevallet, Marie-France Bruandet_

- :fontawesome-solid-user-group: **Participant:** [UMontreal](./participants.md#umontreal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/montreal.ps.gz](http://trec.nist.gov/pubs/trec6/papers/montreal.ps.gz)
- :material-file-search: **Runs:** [UdeMbi](./runs.md#udembi) | [UdeMseg](./runs.md#udemseg)

??? abstract "Abstract"
	
	Université de Montréal, together with the MRIM research group of the CLIPS laboratory in IMAG institute, participated in the Cross-Language Retrieval track in TREC6. Université de Montréal also participated in the Chinese track. In this paper, we describe our approches used in our experiments. In the cross-language retrieval track, we compared word-based retrieval and term-based retrieval. In the Chinese track, the approaches using bigrams and words are compared.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NieCB97.bib) "
	```
	@inproceedings{DBLP:conf/trec/NieCB97,
		author = {Jian{-}Yun Nie and Jean{-}Pierre Chevallet and Marie{-}France Bruandet},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Between Terms and Words for European Language {IR} and Between Words and Bigrams for Chinese {IR}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {697--709},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/montreal.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NieCB97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ETH TREC-6: Routing, Chinese, Cross-Language and Spoken Document  Retrieval

_Bojidar Mateev, Eugen Munteanu, Paraic Sheridan, Martin Wechsler, Peter Schäuble_

- :fontawesome-solid-user-group: **Participant:** [ETH](./participants.md#eth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ETH_notebook.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ETH_notebook.ps.gz)
- :material-file-search: **Runs:** [ETHccM](./runs.md#ethccm) | [ETHccA](./runs.md#ethcca)

??? abstract "Abstract"
	
	ETH Zurich's participation in TREC-6 consists of experiments in the main routing task, both manual and automatic runs in the Chinese retrieval track, cross-language retrieval in each of German, French and English as part of the new cross-language retrieval track, and experiments in speech recognition and retrieval under the new spoken document retrieval track. This year our routing experiments focused on the improvement of the feature selection strategy, on query expansion using similarity thesauri, on the grouping of features and on the combination of different retrieval methods. For Chinese retrieval we continued to rely on character bi-grams for indexing instead of attempting to segment and identify individual words, and we introduced a new manually-constructed stopword list consisting of almost 1,000 Chinese words. Experiments in cross-language retrieval focused heavily on our approach using multilingual similarity thesauri but also included several runs using machine translation technol-ogy. Finally, for the spoken document retrieval track our work included the development of a simple speaker-independent phoneme recogniser and some innovations in our probabilistic retrieval functions to compensate for speech recognition errors.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MateevMSWS97.bib) "
	```
	@inproceedings{DBLP:conf/trec/MateevMSWS97,
		author = {Bojidar Mateev and Eugen Munteanu and Paraic Sheridan and Martin Wechsler and Peter Sch{\"{a}}uble},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{ETH} {TREC-6:} Routing, Chinese, Cross-Language and Spoken Document Retrieval},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {623--635},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/ETH\_notebook.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MateevMSWS97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Preliminary Qualitative Analysis of Segmented vs Bigram Indexing in  Chinese

_Mun-Kew Leong, Hong Zhou_

- :fontawesome-solid-user-group: **Participant:** [ISS](./participants.md#iss)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/iss.ps.gz](http://trec.nist.gov/pubs/trec6/papers/iss.ps.gz)
- :material-file-search: **Runs:** [iss97CmD](./runs.md#iss97cmd) | [iss97CbD](./runs.md#iss97cbd) | [iss97CsD](./runs.md#iss97csd)

??? abstract "Abstract"
	
	This paper investigates merging multiple methods of indexing for Chinese IR. Identical queries, differently segmented, are used to retrieve individual lists of documents which are then merged before evaluation. Two simple merge methods are discussed. Results on Chinese TREC queries 1 to 28 show improvement over either one of the indexing schemes by themselves. In addition, we examine the difference in the documents returned by each indexing method, i.e., do different indexing schemes retrieve different documents, or the same documents ranked differently, or something else. While we contrasted bigram based indexing with segmented based indexing, the same methods would apply between any two forms of indexing.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeongZ97.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeongZ97,
		author = {Mun{-}Kew Leong and Hong Zhou},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Preliminary Qualitative Analysis of Segmented vs Bigram Indexing in Chinese},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {551--557},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/iss.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LeongZ97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-6 English and Chinese Retrieval Experiments using PIRCS

_K. L. Kwok, Laszlo Grunfeld, J. H. Xu_

- :fontawesome-solid-user-group: **Participant:** [CUNY](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/queenst6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/queenst6.ps.gz)
- :material-file-search: **Runs:** [pirc7Ca](./runs.md#pirc7ca) | [pirc7Cd](./runs.md#pirc7cd) | [pirc7Ct](./runs.md#pirc7ct)

??? abstract "Abstract"
	
	For Trec-6 ad-hoc experiments, we continue to use two-stage retrieval with pseudo-feedback from top-ranked un-judged documents for both Chinese and English. We perform three types of retrieval characterized by queries formed using title only, description only and all sections of the given topics. For short queries mainly derived from title or description section, query terms are weighted by average term frequency avtf introduced previously. For Chinese, we employ a combination of representation (character, bigram and short-word) strategy, returning the highest average non-interpolated precision that is even better than some manual approaches. In English ad-hoc, we try a document re-ranking strategy for the first stage retrieval based on occurrence of selected query term pairs, so as to have better result in the second stage. Performance for English ad-hoc is also highly competitive for both very short and long queries. In routing, a strategy of combining different methods of query formation and retrieval is used. These include no learning ad-hoc type queries, learning from the more current FBISS documents only, queries learnt from selecting the best set of known relevant documents based on a genetic algorithm, and queries that are trained from a back-propagation neural network with hidden nodes. Average precision results are among the best four. In addition, we also participate in high precision and the filtering track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokGX97.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokGX97,
		author = {K. L. Kwok and Laszlo Grunfeld and J. H. Xu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-6} English and Chinese Retrieval Experiments using {PIRCS}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {207--214},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/queenst6.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KwokGX97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi Chinese Text Retrieval Experiments at TREC-6

_Xiangji Huang, Stephen E. Robertson_

- :fontawesome-solid-user-group: **Participant:** [City](./participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/city_proc_chinese.ps.gz](http://trec.nist.gov/pubs/trec6/papers/city_proc_chinese.ps.gz)
- :material-file-search: **Runs:** [city97c1](./runs.md#city97c1) | [city97c2](./runs.md#city97c2) | [city97c3](./runs.md#city97c3)

??? abstract "Abstract"
	
	A full description of the experimental system and conditions is given in Appendices A and B. Searchers filled in three types of questionnaires. The pre-session questionnaire established the user's experience and profile. In the post search questionnaires, searchers were asked questions regarding the topic, the search and the system used after undertaking each individual search. Finally in the post-session questionnaire, subjects were asked to provide an overview of the experiment. In addition to the questionnaires, searchers noted on a worksheet the different aspects of the topics they encountered whilst they undertook each search. A total of eight subjects completed forty eight searches, that is three searches on each of the two systems, Okapi and ZPrise. The sessions were divided into two rounds of four searchers. Of the two groups who carried out the twenty-four searches on Okapi, Group A used the same interface as in TREC-5, but with incremental query expansion modified (Appendix A.3.2), and Group B searched a slightly different version which allowed the searcher to cancel the relevance feedback process or clear the query (Appendix A.4).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangR97.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangR97,
		author = {Xiangji Huang and Stephen E. Robertson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Okapi Chinese Text Retrieval Experiments at {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {137--142},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/city\_proc\_chinese.ps.gz},
		timestamp = {Wed, 03 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuangR97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MDS TREC6 Report

_Michael Fuller, Marcin Kaszkiel, Chien Leng Ng, Phil Vines, Ross Wilkinson, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [MDS](./participants.md#mds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz](http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz)
- :material-file-search: **Runs:** [mds607](./runs.md#mds607) | [mds608](./runs.md#mds608) | [mds609](./runs.md#mds609)

??? abstract "Abstract"
	
	This year the MDS group has participated in the ad hoc task, the Chinese task, the speech track, and the interactive track. It is our first year of participation in the speech and interactive tracks. We found the participation in both of these tracks of great benefit and interest.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FullerKNVWZ97.bib) "
	```
	@inproceedings{DBLP:conf/trec/FullerKNVWZ97,
		author = {Michael Fuller and Marcin Kaszkiel and Chien Leng Ng and Phil Vines and Ross Wilkinson and Justin Zobel},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{MDS} {TREC6} Report},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {241--257},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FullerKNVWZ97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Passage-Based Refinement (MultiText Experiements for TREC-6)

_Gordon V. Cormack, Charles L. A. Clarke, Christopher R. Palmer, Samuel S. L. To_

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz](http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz)
- :material-file-search: **Runs:** [uwmt6c0](./runs.md#uwmt6c0)

??? abstract "Abstract"
	
	The MultiText system retrieves passages, rather than entire documents, that are likely to be relevant to a particular topic. For all runs, we used the reciprocal of the length of each passage as an estimate of its likely relevance and ranked accordingly. For the manual adhoc task we explored the limits of user interaction by judging some 13,000 documents based on retrieved passages. For the automatic adhoc task we used retrieved passages as a feedback source for new query terms. For the routing task we estimated probability of relevance from passage length and used this estimate to construct a compound (tiered) query which was used to rank the new data using passage length. For the Chinese track we indexed individual characters rather than segmented words or bigrams and used manually constructed queries and passage-length ranking. For the high precision track we performed judgements on passages using an interface similar to that used for the manual adhoc task. The Very Large Collection run was done on a network of four cheap computers using very simple manually constructed queries and passage-length ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackCPT97.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackCPT97,
		author = {Gordon V. Cormack and Charles L. A. Clarke and Christopher R. Palmer and Samuel S. L. To},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Passage-Based Refinement (MultiText Experiements for {TREC-6)}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {303--319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CormackCPT97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY Does Battle With TREC-6

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, Donald Byrd, Russell C. Swan, Jinxi Xu_

- :fontawesome-solid-user-group: **Participant:** [UMass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz)
- :material-file-search: **Runs:** [INQ4ch1](./runs.md#inq4ch1) | [INQ4ch2](./runs.md#inq4ch2)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CIIR) at the University of Massachusetts participated in eight of the ten tracks that were part of the TREC-6 workshop. We started with the two required tracks, ad-hoc and routing, but then included VLC, Filtering, Chinese, Cross-language, SDR, and Interactive. We omitted NLP and High Precision for want of time and energy. With so many tracks involved, it is nearly inevitable that something will go wrong. Despite our best efforts at verifying all aspects of each track-before, during, and after the experiments we once again made mistakes that were minor in scope, but major in consequence. Those mistakes affected our results in Ad-hoc and Routing, as well as the dependent tracks of VLC and Filtering. The details of the mistakes are presented in each track's discussion, along with information comparing the submitted runs to the corrected runs. Unfortunately, those corrected runs are not included in TREC-6 summary information. This remainder of this report covers our approach to each of the tracks as well as some experimental results and analysis. We start with an overview of the major tools that were used across all tracks. The paper is divided into the following sections. The track descriptions are generally broken into approach, results, and analysis sections, though some tracks require a different description.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCCBBSX97.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCCBBSX97,
		author = {James Allan and James P. Callan and W. Bruce Croft and Lisa Ballesteros and Donald Byrd and Russell C. Swan and Jinxi Xu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} Does Battle With {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {169--206},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AllanCCBBSX97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

