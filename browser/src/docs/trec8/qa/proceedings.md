# Proceedings - Question Answering 1999 

#### The TREC-8 Question Answering Track Evaluation

_Ellen M. Voorhees, Dawn M. Tice_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/qa8.pdf](http://trec.nist.gov/pubs/trec8/papers/qa8.pdf)
??? abstract "Abstract"
	
	The TREC-8 Question Answering track was the first large-scale evaluation of systems that return answers, as opposed to lists of documents, in response to a question. As a first evaluation, it is important to examine the evaluation methodology itself to understand any limits on the conclusions that can be drawn from the evaluation and possibly to find ways to improve subsequent evaluations. This paper has two main goals: to describe in detail how the evaluation was implemented, and to examine the consequences of the methodology on the comparative performance of the systems participating in the evaluation. The examination uncovered no serious flaws in the methodology, supporting its continued use for question answering evaluation. Nonetheless, redefining the specific task to be performed so that it more closely matches an actual user task does appear warranted.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VoorheesT99.bib) "
	```
	@inproceedings{DBLP:conf/trec/VoorheesT99,
		author = {Ellen M. Voorhees and Dawn M. Tice},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC-8} Question Answering Track Evaluation},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/qa8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VoorheesT99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NTT DATA: Overview of system approach at TREC-8 ad-hoc and question  answering

_Toru Takaki_

- :fontawesome-solid-user-group: **Participant:** [ntt](./participants.md#ntt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-nttdata.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-nttdata.pdf)
- :material-file-search: **Runs:** [nttd8qs1](./runs.md#nttd8qs1) | [nttd8qs2](./runs.md#nttd8qs2) | [nttd8ql1](./runs.md#nttd8ql1) | [nttd8ql4](./runs.md#nttd8ql4)

??? abstract "Abstract"
	
	The question answering (QA) track is first attempt in TREC. We gave priority to the following verification for the QA track: (1) the effectiveness of technique by surface-text-based information in the text and (2) application of the information extraction technique. In our QA track, the following processing was done: (1) decision of answer form by question analysis, (2) passage scoring and selection for detailed analysis of the answer after initial retrieval, and (3) information extraction that look for words or phrases that match the form of the answer. We submitted two results to the answer categories of different strength respectively. A retrieval technique like ad-hoc is effective in a category answered by 250 bytes or less in our evaluation but the question analysis is important for a stricter category answered by 50 bytes or less.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Takaki99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Takaki99,
		author = {Toru Takaki},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{NTT} {DATA:} Overview of system approach at {TREC-8} ad-hoc and question answering},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-nttdata.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Takaki99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Extraction Supported Question Answering

_Rohini K. Srihari, Wei Li_

- :fontawesome-solid-user-group: **Participant:** [cymfony](./participants.md#cymfony)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/cymfony.pdf](http://trec.nist.gov/pubs/trec8/papers/cymfony.pdf)
- :material-file-search: **Runs:** [textract9908](./runs.md#textract9908)

??? abstract "Abstract"
	
	This paper discusses the use of our information extraction (IE) system, Textract, in the question-answering (QA) track of the recently held TREC-8 tests. One of our major objectives is to examine how IE can help IR (Information Retrieval) in applications like QA. Our study shows: (i) IE can provide solid support for QA; (ii) low-level IE like Named Entity tagging is often a necessary component in handling most types of questions; (iii) a robust natural language shallow parser provides a structural basis for handling questions; (iv) high-level domain independent IE, i.e. extraction of multiple relationships and general events, is expected to bring about a breakthrough in QA.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SrihariL99.bib) "
	```
	@inproceedings{DBLP:conf/trec/SrihariL99,
		author = {Rohini K. Srihari and Wei Li},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Information Extraction Supported Question Answering},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/cymfony.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SrihariL99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Xerox TREC-8 Question Answering Track Report

_David A. Hull_

- :fontawesome-solid-user-group: **Participant:** [xerox](./participants.md#xerox)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/xerox-QA.pdf](http://trec.nist.gov/pubs/trec8/papers/xerox-QA.pdf)
- :material-file-search: **Runs:** [xeroxQA8lC](./runs.md#xeroxqa8lc) | [xeroxQA8sC](./runs.md#xeroxqa8sc)

??? abstract "Abstract"
	
	This report describes the Xerox work on the TREC-8 Question Answering Track. We linked together a few basic NLP components (a question parser, a sentence boundary identifier, and a proper noun tagger) with a sentence scoring function and an answer presentation function built specifically for the TREC Q&A task. Our system found the correct 50-byte answer (in the top 5 responses) to 45% of the questions, a quite respectable performance, but with considerable room for improvement. Based on the failure analysis presented in this paper, we can conclude that the system would benefit from having access to a broad range of other NLP technologies, including robust parsing and coreference analysis, or some good heuristic approximations thereof. The system also has a clear need for some semantic resources to help with certain difficult problems, such as finding answers that match the semantic class X in What X? questions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Hull99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Hull99,
		author = {David A. Hull},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Xerox {TREC-8} Question Answering Track Report},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/xerox-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Hull99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### AT&T at TREC-8

_Amit Singhal, Steven P. Abney, Michiel Bacchiani, Michael Collins, Donald Hindle, Fernando C. N. Pereira_

- :fontawesome-solid-user-group: **Participant:** [ATT](./participants.md#att)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/att-trec8.pdf](http://trec.nist.gov/pubs/trec8/papers/att-trec8.pdf)
- :material-file-search: **Runs:** [attqa250e](./runs.md#attqa250e) | [attqa250p](./runs.md#attqa250p) | [attqa50p](./runs.md#attqa50p) | [attqa50e](./runs.md#attqa50e)

??? abstract "Abstract"
	
	In 1999, AT&T participated in the ad-hoc task and the Question Answering (QA), Spoken Document Retrieval (SDR), and Web tracks. Most of our effort for TREC-8 focused on the QA and SDR tracks. Results from SDR track show that our document expansion techniques, presented in [8, 9], are very effective for speech retrieval. The results for question answering are also encouraging. Our system designed in a relatively short period for this task can find the correct answer for about 45% of the user questions. This is specially good given the fact that our system extracts only a short phrase as an answer.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SinghalABCHP99.bib) "
	```
	@inproceedings{DBLP:conf/trec/SinghalABCHP99,
		author = {Amit Singhal and Steven P. Abney and Michiel Bacchiani and Michael Collins and Donald Hindle and Fernando C. N. Pereira},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {AT{\&}T at {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/att-trec8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SinghalABCHP99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SCAI TREC-8 Experiments

_Dong-Ho Shin, Yu-Hwan Kim, Sun Kim, Jae-Hong Eom, Hyung-Joo Shin, Byoung-Tak Zhang_

- :fontawesome-solid-user-group: **Participant:** [seoul](./participants.md#seoul)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps](http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps)
- :material-file-search: **Runs:** [Scai8QnA](./runs.md#scai8qna)

??? abstract "Abstract"
	
	This working note reports our experiences with TREC-8 on four tracks: Ad Hoc, Filtering, Web, and QA. The Ad Hoc retrieval engine, SCAIR, has been used for the Web and QA experiments, and the filtering experiments were based on it's own engine. As a second entry to TREC, we focused this year on exploring possibilities of applying machine learning techniques to TREC tasks. The Ad Hoc track employed a cluster-based retrieval method where the scoring function used cluster information extracted from a collection of precompiled documents. Filtering was based on naive Bayes learning supported by an EM algorithm. In the Web track, we compared the performance of using link information to that of not using the information. In the QA track, some passage extraction techniques have been tested using the baseline SCAIR retrieval engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShinKKESZ99.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShinKKESZ99,
		author = {Dong{-}Ho Shin and Yu{-}Hwan Kim and Sun Kim and Jae{-}Hong Eom and Hyung{-}Joo Shin and Byoung{-}Tak Zhang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{SCAI} {TREC-8} Experiments},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShinKKESZ99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Use of Predictive Annotation for Question Answering in TREC8

_John M. Prager, Dragomir R. Radev, Eric W. Brown, Anni Coden, Valerie Samn_

- :fontawesome-solid-user-group: **Participant:** [ibm-chong](./participants.md#ibm-chong)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/IBMTrec8QA.ps](http://trec.nist.gov/pubs/trec8/papers/IBMTrec8QA.ps)
- :material-file-search: **Runs:** [IBMVS995](./runs.md#ibmvs995) | [IBMVS992](./runs.md#ibmvs992) | [IBMDR992](./runs.md#ibmdr992) | [IBMDR995](./runs.md#ibmdr995)

??? abstract "Abstract"
	
	This paper introduces the technique of Predictive Annota-tion, a methodology for indexing texts for retrieval aimed at answering fact-seeking questions. The essence of the approach can be stated simply: index the answers. This is done by establishing about 20 classes of objects that can be identified in text by shallow parsing, and by annotating and indexing the text with these labels, which we call QA-Tokens. Given a question, its class is identified and the question is modified accordingly to include the appropriate token(s). The search engine is modified to rank and return short passages of text rather than documents. The QA-Tokens are used in later stages of analysis to extract the supposed answers from these returned passages. Fi-nally, all potential answers are ranked using a novel for-mula, which determines which ones among them are most likely to be correct.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PragerRBCS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/PragerRBCS99,
		author = {John M. Prager and Dragomir R. Radev and Eric W. Brown and Anni Coden and Valerie Samn},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The Use of Predictive Annotation for Question Answering in {TREC8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/IBMTrec8QA.ps},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PragerRBCS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CRL's TREC-8 Systems Cross-Lingual IR, and Q&A

_William C. Ogden, James R. Cowie, Yevgeny Ludovik, Hugo Molina-Salgado, Sergei Nirenburg, Nigel Sharples, Svetlana O. Sheremetyeva_

- :fontawesome-solid-user-group: **Participant:** [clresearch](./participants.md#clresearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/crl_proceedings.pdf](http://trec.nist.gov/pubs/trec8/papers/crl_proceedings.pdf)
- :material-file-search: **Runs:** [clr99s](./runs.md#clr99s)

??? abstract "Abstract"
	
	This paper describes the systems used by CRL in the Cross-lingual IR and Q&A tracks. The cross-language experiment was unique in that it was run interactively with a mono-lingual user simulating how a true cross-language system might be used. The methods used in the Q&A system are based on language processing technology developed at CRL for machine translation and information extraction.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OgdenCLMNSS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/OgdenCLMNSS99,
		author = {William C. Ogden and James R. Cowie and Yevgeny Ludovik and Hugo Molina{-}Salgado and Sergei Nirenburg and Nigel Sharples and Svetlana O. Sheremetyeva},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {CRL's {TREC-8} Systems Cross-Lingual IR, and Q{\&}A},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/crl\_proceedings.pdf},
		timestamp = {Thu, 17 Nov 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OgdenCLMNSS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-8 Experiments at Maryland: CLIR, QA and Routing

_Douglas W. Oard, Jianqiang Wang, Dekang Lin, Ian Soboroff_

- :fontawesome-solid-user-group: **Participant:** [umd](./participants.md#umd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf](http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf)
- :material-file-search: **Runs:** [umdqa](./runs.md#umdqa)

??? abstract "Abstract"
	
	The University of Maryland team participated in four aspects of TREC-8: the ad hoc retrieval task, the main task in the cross-language retrieval (CLIR) track, the question answering track, and the routing task in the filtering track. The CLIR method was based on Pirkola's method for Dictionary-based Query Translation, using freely available dictionaries. Broad-coverage parsing and rule-based matching was used for question answering. Routing was performed using Latent Semantic Indexing in profile space.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OardWLS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/OardWLS99,
		author = {Douglas W. Oard and Jianqiang Wang and Dekang Lin and Ian Soboroff},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-8} Experiments at Maryland: CLIR, {QA} and Routing},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OardWLS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Coreference in Question Answering

_Thomas S. Morton_

- :fontawesome-solid-user-group: **Participant:** [ge](./participants.md#ge)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/notebook.pdf](http://trec.nist.gov/pubs/trec8/papers/notebook.pdf)
- :material-file-search: **Runs:** [CRDBASE050](./runs.md#crdbase050) | [CRDBASE250](./runs.md#crdbase250) | [GePenn](./runs.md#gepenn)

??? abstract "Abstract"
	
	In this paper we present an overview of the system used by the GE/Penn team for the the Question Answering Track of TREC-8. Our system uses a simple sentence ranking method which is enhanced by the addition of coreference annotated data as its input. We will present an overview of our initial system and its components. Since this was the first time this track has been run, we made numerous additions to our initial system. We will describe these additions and what motivated them as a series of lessons learned after which the final system used for our submission will be described. Finally we will discuss directions for future research.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Morton99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Morton99,
		author = {Thomas S. Morton},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Using Coreference in Question Answering},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/notebook.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Morton99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LASSO: A Tool for Surfing the Answer Net

_Dan I. Moldovan, Sanda M. Harabagiu, Marius Pasca, Rada Mihalcea, Richard Goodrum, Roxana Girju, Vasile Rus_

- :fontawesome-solid-user-group: **Participant:** [smu](./participants.md#smu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/smu.pdf](http://trec.nist.gov/pubs/trec8/papers/smu.pdf)
- :material-file-search: **Runs:** [SMUNLP1](./runs.md#smunlp1) | [SMUNLP2](./runs.md#smunlp2)

??? abstract "Abstract"
	
	This paper presents the architecture, operation and results obtained with the LASSO system developed in the Natural Language Processing Laboratory at SMU. The system relies on a combination of syntactic and semantic techniques, and lightweight abductive inference to find answers. The search for the answer is based on a novel form of indexing called paragraph in-dexing. A score of 55.5% for short answers and 64.5% for long answers was achieved.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoldovanHPMGR99.bib) "
	```
	@inproceedings{DBLP:conf/trec/MoldovanHPMGR99,
		author = {Dan I. Moldovan and Sanda M. Harabagiu and Marius Pasca and Rada Mihalcea and Richard Goodrum and Roxana Girju and Vasile Rus},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{LASSO:} {A} Tool for Surfing the Answer Net},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/smu.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MoldovanHPMGR99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ask Me Tomorrow: The NRC and University of Ottawa Question Answering  System

_Joel D. Martin, Chris Lankester_

- :fontawesome-solid-user-group: **Participant:** [ottawa](./participants.md#ottawa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/UofO_QA.pdf](http://trec.nist.gov/pubs/trec8/papers/UofO_QA.pdf)
- :material-file-search: **Runs:** [UOandNRC](./runs.md#uoandnrc) | [UOandNRC50](./runs.md#uoandnrc50)

??? abstract "Abstract"
	
	Funny how one extra Perl sort function can make a score of 0.52' on the question answering task look a lot like 0. This paper describes our brute force approach to the question answering task and how we did achieve some success, despite formatting problems with our answer file. This paper also describes how we conducted automatic evaluations using the NIST judgment file on newly proposed answers. A good question says what it is about and constrains the form of the answer. In other words, it specifies the distinguishing context for an answer and partially describes the kind of information that would count as an answer. The question 'Who wrote the Declaration of Independence?' specifies that we are talking about someone who wrote a particular document, instead of engaging in some other action with respect to some other document. In addition, the question describes that we are looking for a 'who' which must be a person, agency, or institution. The process of finding an existing answer to a question means finding part of a document that matches the distinguishing context of the question and then extracting an answer of the right type from nearby. Ideally, the extracted answer would have the right sort of relationship to the context of the question. Since this is our first year at TREC, and we were starting with no existing code, we decided to take a brute force approach to the problem. We divided the task into three phases. Phase I does a very high recall retrieval using the words in the question with the goal of discarding 90% of the document collection. Even with only a tenth of the documents, who wants to read them all? Phase Il does an exhaustive scan of all 200-500 byte windows in the retrieved tenth, looking for strings with high similarity to the original question. This phase also ranks these text windows and adds extra points if an obvious answer type is nearby. Finally, Phase Ill was intended (and did a poor job of it) to extract the best answer of the right answer type from the best outputs from Phase II. In the rest of this notebook paper, we first describe the three phases in more detail and then describe how we evaluated the system. We end with a discussion of the results and ideas for future work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MartinL99.bib) "
	```
	@inproceedings{DBLP:conf/trec/MartinL99,
		author = {Joel D. Martin and Chris Lankester},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Ask Me Tomorrow: The {NRC} and University of Ottawa Question Answering System},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/UofO\_QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MartinL99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question-Answering Using Semantic Relation Triples

_Kenneth C. Litkowski_

- :fontawesome-solid-user-group: **Participant:** [clresearch](./participants.md#clresearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/clresearch.pdf](http://trec.nist.gov/pubs/trec8/papers/clresearch.pdf)
- :material-file-search: **Runs:** [clr99s](./runs.md#clr99s)

??? abstract "Abstract"
	
	This paper describes the development of a prototype system to answer questions by selecting sentences from the documents in which the answers occur. After parsing each sentence in these documents, databases are constructed by extracting relational triples from the parse output. The triples consist of discourse entities, semantic relations, and the governing words to which the entities are bound in the sentence. Database triples are also generated for the questions. Question-answering consists of matching the question database records with the records for the documents. The prototype system was developed specifically to respond to the TREC-8 Q&A track, with an existing parser and some existing capability for analyzing parse output. The system was designed to investigate the viability of using structural information about the sentences in a document to answer questions. The CL Research system achieved an overall score of 0.281 (i.e., on average, providing a sentence containing a correct answer as the fourth selection). The score demonstrates the viability of the approach. Post-hoc analysis suggests that this score understates the performance of the prototype and estimates that a more accurate score is approximately 0.482. This analysis also suggests several further improvements and the potential for investigating other avenues that make use of semantic networks and computational lexicology.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Litkowski99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Litkowski99,
		author = {Kenneth C. Litkowski},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Question-Answering Using Semantic Relation Triples},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/clresearch.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Litkowski99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Description of Preliminary Results to TREC-8 QA Task

_Chuan-Jie Lin, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu](./participants.md#ntu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/NTU_TREC8_QA.pdf](http://trec.nist.gov/pubs/trec8/papers/NTU_TREC8_QA.pdf)
- :material-file-search: **Runs:** [NTU99](./runs.md#ntu99)

??? abstract "Abstract"
	
	Question Answering (QA) becomes a hot research topic in recent years due to the very large virtual database on the Internet. QA is defined to find the exact answer, which can meet the users' need more precisely, from a huge unstructured database. Traditional information retrieval systems cannot afford to resolve this problem. On the one hand, users have to find out the answers by themselves from the documents returned by IR systems. On the other hand, the answers may appear in any documents, even that the document is irrelevant to the question. Two possible approaches, i.e., keyword matching and template extraction, can be considered. Keyword matching postulates that the answering text contains most of the keywords. In other words, it carries enough information relevant to the question. Using templates is some sort of information extraction. The contents of documents are represented as templates. To answer a question, a QA system has to select an appropriate template, then fill the template and finally offer the answer. The major difficulties in this approach are to find general domain templates, and to decide which template can be applied to answer the question. Some other techniques are also useful. For example, to answer the questions 'Who...' and 'When...', the identification of named entities like person names and time/date expressions will help to locate the answer. In our preliminary study, we adopt keyword-matching strategy coupling with expanding the keyword set selected from the question sentence by the synonyms and the morphological forms. We participate in the group 'Sentence or under 250 bytes'. The detail will be presented below.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinC99.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinC99,
		author = {Chuan{-}Jie Lin and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Description of Preliminary Results to {TREC-8} {QA} Task},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/NTU\_TREC8\_QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinC99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Sheffield TREC-8 Q&A System

_Kevin Humphreys, Robert J. Gaizauskas, Mark Hepple, Mark Sanderson_

- :fontawesome-solid-user-group: **Participant:** [sheffield](./participants.md#sheffield)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-ushefqa.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-ushefqa.pdf)
- :material-file-search: **Runs:** [shefinq250](./runs.md#shefinq250) | [shefinq50](./runs.md#shefinq50) | [shefatt50](./runs.md#shefatt50) | [shefatt250](./runs.md#shefatt250)

??? abstract "Abstract"
	
	The system entered by the University of Sheffield in the question answering track of TREC-8 is the result of coupling two existing technologies - information retrieval (IR) and information extraction (IE). In essence the approach is this: the IR system treats the question as a query and returns a set of top ranked documents or passages; the IE system uses NLP techniques to parse the question, analyse the top ranked documents or passages returned by the IR system, and instantiate a query variable in the semantic representation of the question against the semantic representation of the analysed documents or passages. Thus, while the IE system by no means attempts 'full text under-standing', this approach is a relatively deep approach which attempts to work with meaning representations. Since the information retrieval systems we used were not our own (AT&T and UMass) and were used more or less 'off the shelf', this paper concentrates on describing the modifications made to our existing information extraction system to allow it to participate in the Q & A task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HumphreysGHS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HumphreysGHS99,
		author = {Kevin Humphreys and Robert J. Gaizauskas and Mark Hepple and Mark Sanderson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {University of Sheffield {TREC-8} Q{\&}A System},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-ushefqa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HumphreysGHS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The RMIT/CSIRO Ad Hoc, Q&A, Web, Interactive, and Speech Experiments  at TREC 8

_Michael Fuller, Marcin Kaszkiel, Sam Kimberley, Corinna Ng, Ross Wilkinson, Mingfang Wu, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [rmit](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf](http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf)
- :material-file-search: **Runs:** [mds08q1](./runs.md#mds08q1)

??? abstract "Abstract"
	
	We participated in the 250 byte category of the question and answer track, submitting one run, mds08q. Our objective in participating in this track was to determine the appropriateness of applying traditional document retrieval techniques to the retrieval and extraction of small, focused text segments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FullerKKNWWZ99.bib) "
	```
	@inproceedings{DBLP:conf/trec/FullerKKNWWZ99,
		author = {Michael Fuller and Marcin Kaszkiel and Sam Kimberley and Corinna Ng and Ross Wilkinson and Mingfang Wu and Justin Zobel},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {RMIT/CSIRO} Ad Hoc, Q{\&}A, Web, Interactive, and Speech Experiments at {TREC} 8},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FullerKKNWWZ99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QALC - the Question-Answering program of the Language and Cognition  group at LIMSI-CNRS

_Olivier Ferret, Brigitte Grau, Gabriel Illouz, Christian Jacquemin, Nicolas Masson_

- :fontawesome-solid-user-group: **Participant:** [limsi](./participants.md#limsi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/LimsiLC-proceedings-paper.pdf](http://trec.nist.gov/pubs/trec8/papers/LimsiLC-proceedings-paper.pdf)
- :material-file-search: **Runs:** [LimsiLC](./runs.md#limsilc)

??? abstract "Abstract"
	
	In this report we describe the QALC system (the Question-Answering program of the Language and Cognition group at LIMSI-CNRS) which has been involved in the QA-track evaluation at TREC8. The purpose of the Question-Answering track is to find the answers to a set of 200 questions. The answers are text sequences extracted from the volumes 4 and 5 of the TREC collection. All the questions have at least one answer in the collection. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FerretGIJM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/FerretGIJM99,
		author = {Olivier Ferret and Brigitte Grau and Gabriel Illouz and Christian Jacquemin and Nicolas Masson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{QALC} - the Question-Answering program of the Language and Cognition group at {LIMSI-CNRS}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/LimsiLC-proceedings-paper.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FerretGIJM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Filters, Webs and Answers: The University of Iowa TREC-8 Results

_David Eichmann, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [iowa](./participants.md#iowa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf](http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf)
- :material-file-search: **Runs:** [UIowaQA2](./runs.md#uiowaqa2) | [UIowaQA3](./runs.md#uiowaqa3) | [UIowaQA4](./runs.md#uiowaqa4) | [UIowaQA1](./runs.md#uiowaqa1)

??? abstract "Abstract"
	
	The University of Iowa attempted three tracks this year: filtering, question answering, and Web, the latter two new for us this year. All work was based upon that done for TREC-7 [2], with our system adapted for the specifics of the QA and Web tracks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannS99,
		author = {David Eichmann and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Filters, Webs and Answers: The University of Iowa {TREC-8} Results},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fast Automatic Passage Ranking (MultiText Experiments for TREC-8)

_Gordon V. Cormack, Charles L. A. Clarke, D. I. E. Kisman, Christopher R. Palmer_

- :fontawesome-solid-user-group: **Participant:** [waterloo](./participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/waterloo.pdf](http://trec.nist.gov/pubs/trec8/papers/waterloo.pdf)
- :material-file-search: **Runs:** [uwmt8qa1](./runs.md#uwmt8qa1)

??? abstract "Abstract"
	
	TREC-8 represents the fifth year that the MultiText project has participated in TREC |2, 1, 4, 5]. The MultiText project develops and prototypes scalable technologies for parallel information retrieval systems implemented on networks of workstations. Research issues are addressed in the context of this parallel architecture. Issues of concern to the MultiText Project include data distribution, load balancing, fast update, fault tolerance, document structure, relevance ranking, and user interaction. The MultiText system incorporates a unique technique for arbitrary passage retrieval. Since our initial participation in TREC-4 our TREC work has explored variants of this technique. For TREC-8 we focused our efforts on the Web track. In addition, we submitted runs for the Adhoc task (title and title+description) and a run for the Question Answering task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackCKP99.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackCKP99,
		author = {Gordon V. Cormack and Charles L. A. Clarke and D. I. E. Kisman and Christopher R. Palmer},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Fast Automatic Passage Ranking (MultiText Experiments for {TREC-8)}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/waterloo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackCKP99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Sys Called Qanda

_Eric Breck, John D. Burger, Lisa Ferro, David House, Marc Light, Inderjeet Mani_

- :fontawesome-solid-user-group: **Participant:** [mitre](./participants.md#mitre)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/MITRE-TREC8-conference.pdf](http://trec.nist.gov/pubs/trec8/papers/MITRE-TREC8-conference.pdf)
- :material-file-search: **Runs:** [MTR99050](./runs.md#mtr99050) | [MTR99250](./runs.md#mtr99250)

??? abstract "Abstract"
	
	Our question answering system was built with a number of priorities in mind. First, we wanted to experiment with natural language processing (NLP) technologies such as shallow parsing, named entity tagging, and coreference chaining. We felt that the small number of terms in the questions coupled with the short length of the answers would make NLP technologies clearly beneficial, unlike previous experiments with NLP technologies on traditional IR tasks. At a more practical level, we were familiar with and interested in such technologies and thus their use would be relatively straightforward and enjoyable. Second, we wanted to use information retrieval (IR) techniques in hopes of achieving robustness and efficiency. It seemed obvious that many answers would appear in documents and passages laden with terms from the question. Finally, we wanted to experiment with different modules from different sites with differing input and output representation and implementational details. Thus, we needed a multi-process system with a flexible data format. Driven by these priorities, we built Qanda,' a system that combines the finer-grained representations and inference abilities of NLP with IR's robustness and domain independence. In the following, we describe the Qanda system, discuss experimental results for the system, and finally discuss automating the scoring of question answering systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BreckBFHLM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BreckBFHLM99,
		author = {Eric Breck and John D. Burger and Lisa Ferro and David House and Marc Light and Inderjeet Mani},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {A Sys Called Qanda},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/MITRE-TREC8-conference.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BreckBFHLM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY and TREC-8

_James Allan, James P. Callan, Fangfang Feng, Daniella Malin_

- :fontawesome-solid-user-group: **Participant:** [umass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf)
- :material-file-search: **Runs:** [INQ634](./runs.md#inq634) | [INQ635](./runs.md#inq635) | [INQ638](./runs.md#inq638) | [INQ639](./runs.md#inq639)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CIIR) at the University of Massachusetts participated in seven of the tracks: ad-hoc, filtering, spoken document retrieval, small web, large web, question and answer, and the query tracks. We spent significant time working on the filtering track, resulting in substantial performance improvement over TREC-7. For all of the other tracks, we used essentially the same system as used in previous years. In the next section, we describe some of the basic processing that was applied across most of the tracks. We then describe the details for each of the tracks and in some cases present some modest analysis of the effectiveness of our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCFM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCFM99,
		author = {James Allan and James P. Callan and Fangfang Feng and Daniella Malin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} and {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AllanCFM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

