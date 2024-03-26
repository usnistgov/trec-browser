# Proceedings - Spoken Document Retrieval 1997 

#### TREC-6 1997 Spoken Document Retrieval Track Overview and Results

_John S. Garofolo, Ellen M. Voorhees, Vincent M. Stanford, Karen Sparck Jones_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/sdr97.ps.gz](http://trec.nist.gov/pubs/trec6/papers/sdr97.ps.gz)
??? abstract "Abstract"
	
	This paper describes the 1997 TREC-6 Spoken Document Retrieval (SDR) Track which implemented a first evaluation of retrieval of broadcast news excerpts using a combination of automatic speech recognition and information retrieval technologies. The motivations behind the SDR Track and background regarding its development and implementation are discussed. The SDR evaluation collection and topics are described and summaries and analyses of the results of the track are presented. Finally, plans for future SDR tracks are described. Since this was the first implementation of an evaluation of SDR, the evaluation itself as well as the evaluated technology should be considered experimental. The results of the first SDR Track were very encouraging and showed us that SDR could be successfully implemented and evaluated. However, the results of the SDR Track should be considered preliminary since the 50-hour spoken document collection used was very small for retrieval experiments (even though it was considered extremely large for speech recognition purposes.) Nonetheless, with thirteen groups participating in the TREC-6 SDR Track, a considerable amount of experience was gained in implementing and evaluating the SDR task. This experience will greatly benefit the next 1998 TREC-7 SDR Track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GarofoloVSJ97.bib) "
	```
	@inproceedings{DBLP:conf/trec/GarofoloVSJ97,
		author = {John S. Garofolo and Ellen M. Voorhees and Vincent M. Stanford and Karen Sparck Jones},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-6} 1997 Spoken Document Retrieval Track Overview and Results},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {83--91},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/sdr97.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GarofoloVSJ97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad hoc Retrieval Using Thresholds, WSTs for French Mono-lingual Retrieval,  Document-at-a-Glance for High Precision and Triphone Windows for Spoken  Documents

_Alan F. Smeaton, Fergus Kelledy, Gerard Quinn_

- :fontawesome-solid-user-group: **Participant:** [Dublin](./participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz](http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz)
- :material-file-search: **Runs:** [DCU97QSDRB1](./runs.md#dcu97qsdrb1) | [DCU97QSDRB2](./runs.md#dcu97qsdrb2) | [DCU97QSDRR1](./runs.md#dcu97qsdrr1) | [DCU97QSDRR2](./runs.md#dcu97qsdrr2)

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

#### AT&T at TREC-6: SDR Track

_Amit Singhal, John Choi, Donald Hindle, Fernando C. N. Pereira_

- :fontawesome-solid-user-group: **Participant:** [ATT](./participants.md#att)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/att.speech.ps.gz](http://trec.nist.gov/pubs/trec6/papers/att.speech.ps.gz)
- :material-file-search: **Runs:** [att97sB1](./runs.md#att97sb1) | [att97sR1](./runs.md#att97sr1) | [att97sS1](./runs.md#att97ss1) | [att97sS2](./runs.md#att97ss2)

??? abstract "Abstract"
	
	In the spoken document retrieval track, we study how higher word-recall-recognizing many of the spoken words affects the retrieval effectiveness for speech documents, given that high word-recall comes at a cost of low word-precision-recognizing many words that were not actually spoken. We hypothesize that information retrieval algorithms would benefit from a higher word-recall and are robust against poor word-precision. Start-up difficulties with recognition for this task kept us from doing an systematic study of the effect of varying levels of word-recall and word-precision on retrieval effectiveness from speech. We simulated a high word-recall and a poor word-precision system by merging the output of several recognizers. Experiments suggest that having higher word-recall does improve the retrieval effectiveness from speech.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SinghalCHP97.bib) "
	```
	@inproceedings{DBLP:conf/trec/SinghalCHP97,
		author = {Amit Singhal and John Choi and Donald Hindle and Fernando C. N. Pereira},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {AT{\&}T at {TREC-6:} {SDR} Track},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {227--232},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/att.speech.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SinghalCHP97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Spoken Document Retrieval at CMU

_Matthew Siegler, Michael J. Witbrock, Seán Slattery, Kristie Seymore, R. E. Jones, Alexander G. Hauptmann_

- :fontawesome-solid-user-group: **Participant:** [CMU](./participants.md#cmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/cmu.trecSDR97-report.ps.gz](http://trec.nist.gov/pubs/trec6/papers/cmu.trecSDR97-report.ps.gz)
- :material-file-search: **Runs:** [CMUref](./runs.md#cmuref) | [CMUibm](./runs.md#cmuibm) | [CMUcmu](./runs.md#cmucmu)

??? abstract "Abstract"
	
	We describe our submission to the TREC-6 Spoken Document Retrieval (SDR) track and the speech recognition and the information retrieval engines. We present SDR evaluation results and a brief analysis. A few developments and experiments are also described in detail including: Vocabulary size experiments, which assess the effect of words missing from the speech recognition vocabulary. For our 51,000-word vocabulary the effect was minimal. Speech recognition using a stemmed language model, where the model statistics of words containing the same root are combined. Stemmed language models did not improve speech recognition or information retrieval. Merging the IBM and CMU speech recognition data. Combining the results of two independent recognition systems slightly boosted information retrieval results. Confidence annotations that estimate of the correctness of each recognized word. Confidence annotations did not appear to improve retrieval. N-best lists where the top recognizer hypotheses are used for information retrieval. Using the top 50 hypotheses dramatically improved performance in the test set. Effects of corpus size on the SDR task. As more documents are added to the task, the gap between perfect retrieval and retrieving spoken documents gets larger. This makes it clear that the size of the current TREC SDR track corpus is too small for obtaining meaningful results. While we have done preliminary experiments with these approaches, most of them were not part of our submission, since their impact on the IR performance on the actual TREC SDR training corpus was too marginal for reliable experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SieglerWSSJH97.bib) "
	```
	@inproceedings{DBLP:conf/trec/SieglerWSSJH97,
		author = {Matthew Siegler and Michael J. Witbrock and Se{\'{a}}n Slattery and Kristie Seymore and R. E. Jones and Alexander G. Hauptmann},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Experiments in Spoken Document Retrieval at {CMU}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {291--302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/cmu.trecSDR97-report.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SieglerWSSJH97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Text Retrieval via Semantic Forests

_Patrick Schone, Jeffrey L. Townsend, Thomas H. Crystal, Calvin Olano_

- :fontawesome-solid-user-group: **Participant:** [NSA](./participants.md#nsa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/nsa-rev.ps.gz](http://trec.nist.gov/pubs/trec6/papers/nsa-rev.ps.gz)
- :material-file-search: **Runs:** [nsasglt1](./runs.md#nsasglt1) | [nsasgsr1](./runs.md#nsasgsr1)

??? abstract "Abstract"
	
	We approached our first participation in TREC with an interest in performing retrieval on the output of automatic speech-to-text (speech recognition) systems and a background in performing topic-labeling on such output. Our primary thrust, therefore, was to participate in the SDR track. In conformance with the rules, we also participated in the Ad Hoc text-retrieval task, to create a baseline for comparing our converted topic-labeling system with other approaches to IR and to assess the effect of speech-transcription errors. A second thrust was to explore rapid prototyping of an IR system, given the existing topic-labeling software. Our IR system makes use of software called Semantic Forests which is based on an algorithm originally developed for labeling topics in text and transcribed speech (Schone & Nelson, ICASSP 96). Topic-labelling is not an IR task, so Semantic Forests was adapted for use in TREC over an eight-week period for the Ad Hoc task, with an additional two weeks for SDR. In what follows, we describe our system as well as experiments, timings, results, and future directions with these techniques.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchoneTCO97.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchoneTCO97,
		author = {Patrick Schone and Jeffrey L. Townsend and Thomas H. Crystal and Calvin Olano},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Text Retrieval via Semantic Forests},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {761--773},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/nsa-rev.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SchoneTCO97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ETH TREC-6: Routing, Chinese, Cross-Language and Spoken Document  Retrieval

_Bojidar Mateev, Eugen Munteanu, Paraic Sheridan, Martin Wechsler, Peter Schäuble_

- :fontawesome-solid-user-group: **Participant:** [ETH](./participants.md#eth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ETH_notebook.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ETH_notebook.ps.gz)
- :material-file-search: **Runs:** [ETHS1](./runs.md#eths1) | [ETHB1](./runs.md#ethb1) | [ETHR1](./runs.md#ethr1) | [ETHS2](./runs.md#eths2) | [ETHB2](./runs.md#ethb2)

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

#### MDS TREC6 Report

_Michael Fuller, Marcin Kaszkiel, Chien Leng Ng, Phil Vines, Ross Wilkinson, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [MDS](./participants.md#mds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz](http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz)
- :material-file-search: **Runs:** [mds612](./runs.md#mds612) | [mds613](./runs.md#mds613) | [mds614](./runs.md#mds614) | [mds615](./runs.md#mds615)

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

#### Short Queries, Natural Language and Spoken Document Retrieval: Experiments  at Glasgow University

_Fabio Crestani, Mark Sanderson, Marcos Theophylactou, Mounia Lalmas_

- :fontawesome-solid-user-group: **Participant:** [Glasgow](./participants.md#glasgow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/glasgow.ps.gz](http://trec.nist.gov/pubs/trec6/papers/glasgow.ps.gz)
- :material-file-search: **Runs:** [gla6B1](./runs.md#gla6b1) | [gla6R1](./runs.md#gla6r1) | [gla6S1](./runs.md#gla6s1) | [gla6S2](./runs.md#gla6s2)

??? abstract "Abstract"
	
	This paper contains a description of the methodology and results of the three TREC submissions made by the Glasgow IR group (glair). In addition to submitting to the ad hoc task, submissions were also made to NLP track and to the SDR speech 'pre-track'. Results from our submissions reveal that some of our approaches have performed poorly (i.e. ad hoc and NLP track), but we have also had success particularly in the speech track through use of transcript merging. We also highlight and discuss a seemingly unusual result where retrieval based on the very short versions of the TREC ad hoc queries produced better retrieval effectiveness than retrieval based on more 'normal' length queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CrestaniSTL97.bib) "
	```
	@inproceedings{DBLP:conf/trec/CrestaniSTL97,
		author = {Fabio Crestani and Mark Sanderson and Marcos Theophylactou and Mounia Lalmas},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Short Queries, Natural Language and Spoken Document Retrieval: Experiments at Glasgow University},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {667--686},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/glasgow.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CrestaniSTL97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY Does Battle With TREC-6

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, Donald Byrd, Russell C. Swan, Jinxi Xu_

- :fontawesome-solid-user-group: **Participant:** [UMass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz)
- :material-file-search: **Runs:** [INQ4sdd](./runs.md#inq4sdd) | [INQ4sds](./runs.md#inq4sds) | [INQ4sdl](./runs.md#inq4sdl)

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

#### The THISL Spoken Document Retrieval System

_Dave Abberley, Steve Renals, Gary D. Cook, Anthony J. Robinson_

- :fontawesome-solid-user-group: **Participant:** [Sheffield](./participants.md#sheffield)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/sheffield.ps.gz](http://trec.nist.gov/pubs/trec6/papers/sheffield.ps.gz)
- :material-file-search: **Runs:** [THISLB1](./runs.md#thislb1) | [THISLB2](./runs.md#thislb2) | [THISLR1](./runs.md#thislr1) | [THISLR2](./runs.md#thislr2) | [THISLS1](./runs.md#thisls1) | [THISLS2](./runs.md#thisls2)

??? abstract "Abstract"
	
	The THISL spoken document retrieval system is based on the ABBOT Large Vocabulary Continuous Speech Recognition (LVCSR) system developed by Cambridge University, Sheffield University and SoftSound, and uses PRISE (NIST) for indexing and retrieval. We participated in full SDR mode. Our approach was to transcribe the spoken documents at the word level using ABBOT, indexing the resulting text transcriptions using PRISE. The LVCSR system uses a recurrent network-based acoustic model (with no adaptation to different conditions) trained on the 50 hour Broadcast News training set, a 65,000 word vocabulary and a trigram language model derived from Broadcast News text. Words in queries which were out-of-vocabulary (OOV) were word spotted at query time (utilizing the posterior phone probabilities output by the acoustic model), added to the transcriptions of the relevant documents and the collection was then re-indexed. We generated pronunciations at run-time for OOV words using the Festival TTS system (University of Edinburgh). Our key aims in this evaluation were to produce a complete system for the SDR task, to investigate the effect of a word error rate of 30-50% on retrieval performance and to investigate the integration of LVCSR and word spotting in a retrieval task. To achieve this we performed four basic experiments indexing on: transcribed text; IBM (baseline recognizer) SRT files; ABBOT SRT files; and ABBOT SRT files combined with word spotting of OOV words in the query. This evaluation provided a stress test for our LVCSR system. In particular we developed our decoding algorithm and software to operate in a more 'online mode'. The result of this was the ability to decode arbitrarily long passages without segmentation into 'utterances'. When indexing, acoustic model computation required around 3.5 x real time on a Sun Ultra 1/170, and lexical search required around 2.5 x real time. At query time the word spotting component ran in about 0.25 × real time per document per query.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbberleyRCR97.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbberleyRCR97,
		author = {Dave Abberley and Steve Renals and Gary D. Cook and Anthony J. Robinson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {THISL} Spoken Document Retrieval System},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {747--752},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/sheffield.ps.gz},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AbberleyRCR97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

