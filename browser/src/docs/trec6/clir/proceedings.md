# Proceedings - Cross-Language 1997 

#### Cross-Language Information Retrieval (CLIR) Track Overview

_Peter Schäuble, Paraic Sheridan_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/clir_track_US.ps.gz](http://trec.nist.gov/pubs/trec6/papers/clir_track_US.ps.gz)
??? abstract "Abstract"
	
	Cross-Language Information Retrieval (CLIR) was a new task in the TREC-6 evaluation. In contrast to the multilingual track included in previous TREC evaluations, which was concerned with information retrieval in Spanish or Chi-nese, the cross-language retrieval track focuses on the retrieval situation where the documents are written in a language which is different than the language used to specify the queries. The TREC-6 track used documents in English, French and German and queries in English, French, German, Spanish and Dutch. There are many applications or scenarios in which a user of a retrieval system may be interested in finding information written in a language other than the user's native or preferred language. In some applications, a user may want to discover all possible relevant information in a multilingual textbase, irrespective of the language of the relevant information. This may be the case when searching certain collections of legal or patent information for example. In other cases a user may even have some language comprehension ability in the languages of the documents (passive vocabulary) but may not have a sufficiently rich active vocabulary in the document languages to confidently specify queries in those languages. In this case a cross-language search which permits the user to specify native language queries but retrieves documents in their original language is useful. Cross-language retrieval also has the added advantage of requiring only one query to a multi-lingual text collection, rather than having a user submit individual queries in each of the languages of interest. Situations where a retrieval system user is faced with the task of querying a multilingual document collection are becoming increasingly common. These range across document collections made up of documents from local offices of multinational companies, collections composed of documents from different regions of multilingual countries such as Switzerland or Canada, or the document collections of large organisations such as the United Nations or European Com-mission. It is however, the global information infrastructure of the internet that has been largely responsible for the growing awareness of a need for cross-language information retrieval systems. This has in turn led to a growing body of research into the problems of cross-language retrieval and the development of several different approaches for CLIR.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchaubleS97.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchaubleS97,
		author = {Peter Sch{\"{a}}uble and Paraic Sheridan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Cross-Language Information Retrieval {(CLIR)} Track Overview},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {31--43},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/clir\_track\_US.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SchaubleS97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad hoc Retrieval Using Thresholds, WSTs for French Mono-lingual Retrieval,  Document-at-a-Glance for High Precision and Triphone Windows for Spoken  Documents

_Alan F. Smeaton, Fergus Kelledy, Gerard Quinn_

- :fontawesome-solid-user-group: **Participant:** [Dublin](./participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz](http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz)
- :material-file-search: **Runs:** [DCU97Fv1](./runs.md#dcu97fv1) | [DCU97Fv2](./runs.md#dcu97fv2)

??? abstract "Abstract"
	
	This paper describes work done by a team from Dublin City University as part of TREC-6. In this TREC exercise we completed series of runs in 4 categories. The first was the mainline ad hoc retrieval task in which we repeated our entry for TREC-5, without modification. This is based on applying various thresholds to processing a query including query term and posting list thresholds, in order to improve retrieval efficiency. As our previous work has shown, this can be done without any loss in retrieval effectiveness. Our second set of submitted runs were as part of the cross-lingual retrieval track where we ran French topics against French texts, effectively mono-lingual retrieval. What is novel about our approach is that it is based upon matching word shape tokens derived from character shape codes, rather than matching word stems or base forms. This technique is useful for retrieving from scanned document images rather than full texts and is something we are currently refining for English texts (and English queries). With those other experiments we have obtained surprisingly effective retrieval and this venture in TREC-6 was to see how effective WST-based retrieval could be for French. The third series of experiments we submitted were based on the high precision track in which we used a graphical representation of a ranked list of documents and the positional occurrences of search terms within those top-ranked documents, relative to each other. Our final experiments were as part of the spoken document retrieval track in which we removed the tags used for story bounds, turned transcripts and topics into a phonetic representation using a phoneme dictionary and we then retrieved story identifiers based on a triphone match between topic and fixed-width windows of triphones in the transcripts. We also applied a weighting function to triphones as they occurred in story 'windows' based on their offset within those windows.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmeatonKQ97.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmeatonKQ97,
		author = {Alan F. Smeaton and Fergus Kelledy and Gerard Quinn},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Ad hoc Retrieval Using Thresholds, WSTs for French Mono-lingual Retrieval, Document-at-a-Glance for High Precision and Triphone Windows for Spoken Documents},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {461--475},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SmeatonKQ97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Automatic 3-Language Cross-Language Information Retrieval with Latent  Semantic Indexing

_Bob Rehder, Michael L. Littman, Susan T. Dumais, Thomas K. Landauer_

- :fontawesome-solid-user-group: **Participant:** [Duke](./participants.md#duke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/lsi.ps.gz](http://trec.nist.gov/pubs/trec6/papers/lsi.ps.gz)
- :material-file-search: **Runs:** [97lsiSEE](./runs.md#97lsisee) | [97lsiSFF](./runs.md#97lsisff) | [97lsiSGG](./runs.md#97lsisgg) | [97lsiLEE](./runs.md#97lsilee) | [97lsiLFF](./runs.md#97lsilff) | [97lsiLGG](./runs.md#97lsilgg) | [97lsiSGE](./runs.md#97lsisge) | [97lsiSGF](./runs.md#97lsisgf) | [97lsiLGE](./runs.md#97lsilge) | [97lsiLGF](./runs.md#97lsilgf) | [97lsiSFE](./runs.md#97lsisfe) | [97lsiSFG](./runs.md#97lsisfg) | [97lsiLFE](./runs.md#97lsilfe) | [97lsiLFG](./runs.md#97lsilfg) | [97lsiSEG](./runs.md#97lsiseg) | [97lsiSEF](./runs.md#97lsisef) | [97lsiLEG](./runs.md#97lsileg) | [97lsiLEF](./runs.md#97lsilef)

??? abstract "Abstract"
	
	This paper describes cross-language information-retrieval experiments carried out for TREC-6. Our retrieval method, cross-language latent semantic indexing (CL-LSI), is completely automatic and we were able to use it to create a 3-way English-French-German IR system. This study extends our previous work in terms of the large size of training and testing corpora, the use of low-quality training data, the evaluation using relevance judg-ments, and the number of languages analyzed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RehderLDL97.bib) "
	```
	@inproceedings{DBLP:conf/trec/RehderLDL97,
		author = {Bob Rehder and Michael L. Littman and Susan T. Dumais and Thomas K. Landauer},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Automatic 3-Language Cross-Language Information Retrieval with Latent Semantic Indexing},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {233--239},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/lsi.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RehderLDL97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Document Translation for Cross-Language Text Retrieval at the University  of Maryland

_Douglas W. Oard, Paul G. Hackett_

- :fontawesome-solid-user-group: **Participant:** [UMd](./participants.md#umd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/umd.ps.gz](http://trec.nist.gov/pubs/trec6/papers/umd.ps.gz)
- :material-file-search: **Runs:** [umcpxeg1](./runs.md#umcpxeg1) | [umcpxeg2](./runs.md#umcpxeg2) | [umcpxeg3](./runs.md#umcpxeg3) | [umcpxge1](./runs.md#umcpxge1) | [umcpxge2](./runs.md#umcpxge2) | [umcpxge3](./runs.md#umcpxge3) | [umcpxgg1](./runs.md#umcpxgg1) | [umcpxgg2](./runs.md#umcpxgg2) | [umcpxgg3](./runs.md#umcpxgg3) | [umcpxgg4](./runs.md#umcpxgg4) | [umcpxgg5](./runs.md#umcpxgg5) | [umcpxgg6](./runs.md#umcpxgg6)

??? abstract "Abstract"
	
	The University of Maryland participated in three TREC-6 tasks: ad hoc retrieval, cross-language retrieval, and spoken document retrieval. The principal focus of the work was evaluation of a cross-language text retrieval technique based on fully automatic machine translation. The results show that approaches based on document translation can be approximately as effective as approaches based on query translation, but that additional work will be needed to develop a solid basis for choosing between the two in specific applications. Ad hoc and spoken document retrieval results are also presented.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OardH97.bib) "
	```
	@inproceedings{DBLP:conf/trec/OardH97,
		author = {Douglas W. Oard and Paul G. Hackett},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Document Translation for Cross-Language Text Retrieval at the University of Maryland},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {687--696},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/umd.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/OardH97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Between Terms and Words for European Language IR and Between Words  and Bigrams for Chinese IR

_Jian-Yun Nie, Jean-Pierre Chevallet, Marie-France Bruandet_

- :fontawesome-solid-user-group: **Participant:** [UMontreal](./participants.md#umontreal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/montreal.ps.gz](http://trec.nist.gov/pubs/trec6/papers/montreal.ps.gz)
- :material-file-search: **Runs:** [CLIPS1](./runs.md#clips1) | [CLIPS2](./runs.md#clips2) | [CLIPS3](./runs.md#clips3)

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
- :material-file-search: **Runs:** [ETHdd1](./runs.md#ethdd1) | [ETHde1](./runs.md#ethde1) | [ETHde2](./runs.md#ethde2) | [ETHde3](./runs.md#ethde3) | [ETHdf1](./runs.md#ethdf1) | [ETHdf2](./runs.md#ethdf2) | [ETHed1](./runs.md#ethed1) | [ETHed2](./runs.md#ethed2) | [ETHed3](./runs.md#ethed3) | [ETHed4](./runs.md#ethed4) | [ETHee1](./runs.md#ethee1) | [ETHfd1](./runs.md#ethfd1) | [ETHfd2](./runs.md#ethfd2) | [ETHff1](./runs.md#ethff1)

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

#### Cross Language Retrieval with the Twenty-One system

_Wessel Kraaij, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [TNO](./participants.md#tno)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/twentyone.ps.gz](http://trec.nist.gov/pubs/trec6/papers/twentyone.ps.gz)
- :material-file-search: **Runs:** [TNOde1](./runs.md#tnode1) | [TNOde2](./runs.md#tnode2) | [TNOdeMT1](./runs.md#tnodemt1) | [TNOee](./runs.md#tnoee) | [TNOfe1](./runs.md#tnofe1) | [TNOfe2](./runs.md#tnofe2) | [TNOnle1](./runs.md#tnonle1) | [TNOnle2](./runs.md#tnonle2) | [TNOde3](./runs.md#tnode3) | [TNOde4](./runs.md#tnode4) | [TNOde5](./runs.md#tnode5) | [TNOde6](./runs.md#tnode6) | [TNOfe3](./runs.md#tnofe3) | [TNOfe4](./runs.md#tnofe4) | [TNOfe5](./runs.md#tnofe5) | [TNOfe6](./runs.md#tnofe6) | [TNOnle3](./runs.md#tnonle3) | [TNOnle4](./runs.md#tnonle4) | [TNOnle5](./runs.md#tnonle5) | [TNOnle6](./runs.md#tnonle6)

??? abstract "Abstract"
	
	The EU project Twenty-One will support cross language queries in a multilingual document base. A prototype version of the Twenty-One system has been subjected to the Cross Language track tests in order to set baseline performances. The runs were based on query translation using dictionaries and corpus based disambiguation methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KraaijH97.bib) "
	```
	@inproceedings{DBLP:conf/trec/KraaijH97,
		author = {Wessel Kraaij and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Cross Language Retrieval with the Twenty-One system},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {753--760},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/twentyone.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KraaijH97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Phrase Discovery for English and Cross-language Retrieval at TREC  6

_Fredric C. Gey, Aitao Chen_

- :fontawesome-solid-user-group: **Participant:** [Berkeley](./participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/brkly.ps.gz](http://trec.nist.gov/pubs/trec6/papers/brkly.ps.gz)
- :material-file-search: **Runs:** [BrklyG2GA](./runs.md#brklyg2ga) | [BrklyE2GA](./runs.md#brklye2ga) | [BrklyE2GM](./runs.md#brklye2gm)

??? abstract "Abstract"
	
	Berkeley's experiments in TREC-6 center around phrase discovery in topics and documents. The technique of ranking bigram term pairs by their expected mutual information value was utilized for English phrase discovery as well as Chinese seg-mentation. This differentiates our phrase-finding method from the mechanistic one of using all bigrams which appear at least 25 times in the collection. Phrase finding presents an interesting interaction with stop words and stop word processing. English phrase discovery proved very important in a dictionary-based English to German cross language run. Our participation in the filtering track was marked with an interesting strictly Boolean retrieval as well as some experimentation with maximum utility thresholds on probabilistically ranked retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GeyC97.bib) "
	```
	@inproceedings{DBLP:conf/trec/GeyC97,
		author = {Fredric C. Gey and Aitao Chen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Phrase Discovery for English and Cross-language Retrieval at {TREC} 6},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {637--647},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/brkly.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GeyC97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Xerox TREC-6 Site Report: Cross Language Text Retrieval

_Éric Gaussier, Gregory Grefenstette, David A. Hull, B. Maximilian Schulze_

- :fontawesome-solid-user-group: **Participant:** [Xerox](./participants.md#xerox)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/xrce-trec6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/xrce-trec6.ps.gz)
- :material-file-search: **Runs:** [XRCECLE2EA](./runs.md#xrcecle2ea) | [XRCECLE2EM](./runs.md#xrcecle2em) | [XRCECLF2FM](./runs.md#xrceclf2fm) | [XRCECLF2FA](./runs.md#xrceclf2fa) | [XRCECLF2EA](./runs.md#xrceclf2ea) | [XRCECLF2EM](./runs.md#xrceclf2em) | [XRCECLE2FM](./runs.md#xrcecle2fm) | [XRCECLE2FA](./runs.md#xrcecle2fa)

??? abstract "Abstract"
	
	Xerox participated in the Cross Language Information Retrieval (CLIR) track of TREC-6. This track examines the problem of retrieving documents written in one language using queries written in another language. Our approach is to use a bilingual dictionary at query time to construct a target language version of the original query. We concentrate our experiments this year on manual query construction based on a weighted boolean model and on an automatic method for the translation of multi-word units. We also introduce a new derivational stemming algorithm whose word classes are generated automatically from a monolingual lexicon. We present our results on the 22 TREC-6 CLIR topics which have been assessed and briefly discuss the problems inherent in the cross-language IR task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaussierGHS97.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaussierGHS97,
		author = {{\'{E}}ric Gaussier and Gregory Grefenstette and David A. Hull and B. Maximilian Schulze},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Xerox {TREC-6} Site Report: Cross Language Text Retrieval},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {775--788},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/xrce-trec6.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GaussierGHS97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Free Resources And Advanced Alignment For Cross-Language Text Retrieval

_Mark W. Davis, William C. Ogden_

- :fontawesome-solid-user-group: **Participant:** [NMSU-D](./participants.md#nmsu-d)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/nmsu-clir.ps.gz](http://trec.nist.gov/pubs/trec6/papers/nmsu-clir.ps.gz)
- :material-file-search: **Runs:** [clcrl1](./runs.md#clcrl1) | [clcrl2](./runs.md#clcrl2) | [clcrl3](./runs.md#clcrl3) | [clcrl4](./runs.md#clcrl4)

??? abstract "Abstract"
	
	For the Cross-Language Text Retrieval Track in TREC 6, NMSU experimented with a new approach to deriving translation equivalents from parallel text databases, and also investigated performing automatic, dictionary-based translation of query terms by using a dictionary that could be queried remotely via the World Wide Web. The new approach to building bilingual translation lexicons involved aligning parallel texts at the sentence level, and then performing further alignments at the sub-sentence level. The process initially chooses alignment anchors based on N-gram matches between cognate terms. Term and phrase matching is then performed between the anchor points by finding the most direct path from one anchor to the next, penalizing larger steps over runs of terms. The collected term translations are then used as equivalents for a query translation process and the translated query is then submitted to a monolingual retrieval engine. The results are compared against the performance of a monolingual French-French retrieval system, and against a translated query formed from a very high-quality bilingual dictionary accessed directly over the World Wide Web. A combined approach is also presented that uses terminology from both the dictionary and, where the dictionary lacks coverage, supplements the query translation using terms from a parallel text database.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DavisO97.bib) "
	```
	@inproceedings{DBLP:conf/trec/DavisO97,
		author = {Mark W. Davis and William C. Ogden},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Free Resources And Advanced Alignment For Cross-Language Text Retrieval},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {385--395},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/nmsu-clir.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DavisO97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Clustering and SuperConcepts Within SMART: TREC 6

_Chris Buckley, Mandar Mitra, Janet A. Walz, Claire Cardie_

- :fontawesome-solid-user-group: **Participant:** [Cornell](./participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/cornell.ps.gz](http://trec.nist.gov/pubs/trec6/papers/cornell.ps.gz)
- :material-file-search: **Runs:** [Cor6FFsc](./runs.md#cor6ffsc) | [Cor6EFexp](./runs.md#cor6efexp) | [Cor6EFent](./runs.md#cor6efent) | [Cor6ETGsc](./runs.md#cor6etgsc) | [Cor6EEsc](./runs.md#cor6eesc)

??? abstract "Abstract"
	
	The Smart information retrieval project emphasizes completely automatic approaches to the understanding and retrieval of large quantities of text. We continue our work in TREC 6, performing runs in the routing, ad-hoc, and foreign language environments, including cross-lingual runs. The major focus this year is on trying to maintain the balance of the query - attempting to ensure the various aspects of the original query are appropriately addressed, especially while adding expansion terms. Exactly the same procedure is used for foreign language environments as for English; our tenet is that good information retrieval techniques are more powerful than linguistic knowledge. We also give an interesting cross-lingual run, assuming that French and English are closely enough related so that a query in one language can be run directly on a collection in the other language by just 'correcting' the spelling of the query words. This is quite successful for most queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleyMWC97.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleyMWC97,
		author = {Chris Buckley and Mandar Mitra and Janet A. Walz and Claire Cardie},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Using Clustering and SuperConcepts Within {SMART:} {TREC} 6},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {107--124},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/cornell.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BuckleyMWC97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure at TREC6

_Mohand Boughanem, Chantal Soulé-Dupuy_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/irit.ps.gz](http://trec.nist.gov/pubs/trec6/papers/irit.ps.gz)
- :material-file-search: **Runs:** [MercureFFs](./runs.md#mercureffs) | [MercureFFl](./runs.md#mercureffl)

??? abstract "Abstract"
	
	We continue our work in trec performing runs in adhoc, routing and part of the cross language track. The major investigations this year are the weight schemes modification to take into account the document length. We also experiment the high precision procedure in automatic adhoc environment by tuning the term weight parameters.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoughanemS97.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoughanemS97,
		author = {Mohand Boughanem and Chantal Soul{\'{e}}{-}Dupuy},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Mercure at {TREC6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {321--328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/irit.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BoughanemS97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY Does Battle With TREC-6

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, Donald Byrd, Russell C. Swan, Jinxi Xu_

- :fontawesome-solid-user-group: **Participant:** [UMass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz)
- :material-file-search: **Runs:** [INQ4xl1](./runs.md#inq4xl1) | [INQ4xl2](./runs.md#inq4xl2)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CIR) at the University of Massachusetts participated in eight of the ten tracks that were part of the TREC-6 workshop. We started with the two required tracks, ad-hoc and routing, but then included VLC, Filtering, Chinese, Cross-language, SDR, and Interactive. We omitted NLP and High Precision for want of time and energy. With so many tracks involved, it is nearly inevitable that something will go wrong. Despite our best efforts at verifying all aspects of each track-before, during, and after the experiments we once again made mistakes that were minor in scope, but major in consequence. Those mistakes affected our results in Ad-hoc and Routing, as well as the dependent tracks of VLC and Filtering. The details of the mistakes are presented in each track's discussion, along with information comparing the submitted runs to the corrected runs. Unfortunately, those corrected runs are not included in TREC-6 summary information. This remainder of this report covers our approach to each of the tracks as well as some experimental results and analysis. We start with an overview of the major tools that were used across all tracks. The paper is divided into the following sections. The track descriptions are generally broken into approach, results, and analysis sections, though some tracks require a different description.
	

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

