# Proceedings - Question Answering 2007 

#### Overview of the TREC 2007 Question Answering Track

_Hoa Trang Dang, Diane Kelly, Jimmy Lin_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/QA.OVERVIEW16.pdf](http://trec.nist.gov/pubs/trec16/papers/QA.OVERVIEW16.pdf)
??? abstract "Abstract"
	
	The TREC 2007 question answering (QA) track contained two tasks: the main task consisting of series of factoid, list, and “Other” questions organized around a set of targets, and the complex, interactive question answering (ciQA) task. The main task differed from previous years in that the document collection comprised blogs in addition to newswire documents, requiring systems to process diverse genres of unstructured text. The evaluation of factoid and list responses distinguished between answers that were globally correct (with respect to the document collection), and those that were only locally correct (with respect to the supporting document but not to the overall document collection). The ciQA task provided a framework for participants to investigate interaction in the context of complex information needs. Standing in for surrogate users, assessors interacted with QA systems live over the Web; this setup allowed participants to experiment with more complex interfaces but also revealed limitations in the ciQA design for evaluation of interactive systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DangKL07.bib) "
	```
	@inproceedings{DBLP:conf/trec/DangKL07,
		author = {Hoa Trang Dang and Diane Kelly and Jimmy Lin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2007 Question Answering Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/QA.OVERVIEW16.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DangKL07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Persuasive, Authorative and Topical Answers for Complex Question Answering

_Leif Azzopardi, Mark Baillie, Ian Ruthven_

- :fontawesome-solid-user-group: **Participant:** [ustrathclyde.ruthven](./participants.md#ustrathclyde.ruthven)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ustrathclyde.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ustrathclyde.qa.final.pdf)
- :material-file-search: **Runs:** [sicka](./runs.md#sicka) | [strath](./runs.md#strath) | [strath2](./runs.md#strath2) | [sicka2](./runs.md#sicka2)

??? abstract "Abstract"
	
	The ciqa track investigates the role of interaction in answering complex questions: questions that relate two or more entities by some specified relationship. As in the ciqa 2006, our interest in ciqa 2007 was on contextual factors that may affect how answers are assessed. In ciqa 2006 we investigated factors such as topical knowledge or confidence in assessing answers through direct questioning - asking the ciqa assessors to directly estimate values for such variables using ordinal or categorical scales. In ciqa 2006 we found many useful relationships between personal contextual variables and how assessors judged answers. This year we were keen to follow this line of investigation, following a more specific research question: how do contextual variables affect the judgement of different types of information surrogate. We created information surrogates (answers) which contained similar amounts of information but presented the information in different ways; either as neutral, topically related information (topical answers), information that was presented in such a way as to entice the read (persuasive answers), or information that was presented as coming from a named authority (authorative answers). Separately, we gathered contextual information on the assessors' preferences for such answers through the use of HTML interaction forms. Our results show differences in how assessors reacted to these different information surrogates in terms of highly they were to judge the answer as good and how likely they were to read the document containing the answer.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AzzopardiBR07.bib) "
	```
	@inproceedings{DBLP:conf/trec/AzzopardiBR07,
		author = {Leif Azzopardi and Mark Baillie and Ian Ruthven},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Persuasive, Authorative and Topical Answers for Complex Question Answering},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ustrathclyde.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AzzopardiBR07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Drexel at TREC 2007: Question Answering

_Protima Banerjee, Hyoil Han_

- :fontawesome-solid-user-group: **Participant:** [drexelu.han](./participants.md#drexelu.han)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/drexelu.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/drexelu.qa.final.pdf)
- :material-file-search: **Runs:** [DrexelRun1](./runs.md#drexelrun1) | [DrexelRun2](./runs.md#drexelrun2) | [DrexelRun3](./runs.md#drexelrun3)

??? abstract "Abstract"
	
	The TREC Question Answering Track presented several distinct challenges to participants in 2007. Participants were asked to create a system which discovers the answers to factoid and list questions about people, entities, organizations and events, given both blog and newswire text data sources. In addition, participants were asked to expose interesting information nuggets which exist in the data collection, which were not uncovered by the factoid or list questions. This year is the first time the Intelligent Information Processing group at Drexel has participated in the TREC Question Answering Track. As such, our goal was the development of a Question Answering system framework to which future enhancements could be made, and the construction of simple components to populate the framework. The results of our system this year were not significant; our primary accomplishment was the establishment of a baseline system which can be improved upon in 2008 and going forward.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BanerjeeH07.bib) "
	```
	@inproceedings{DBLP:conf/trec/BanerjeeH07,
		author = {Protima Banerjee and Hyoil Han},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Drexel at {TREC} 2007: Question Answering},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/drexelu.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BanerjeeH07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Intellexer Question Answering

_Aliaksei Bondarionok, Anatoly Bobkov, Liudmila Sudanova, Pavel Mazur, Tatsiana Samuseva_

- :fontawesome-solid-user-group: **Participant:** [effectivesoft](./participants.md#effectivesoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/effectivesoft.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/effectivesoft.qa.final.pdf)
- :material-file-search: **Runs:** [Intellexer7A](./runs.md#intellexer7a) | [Intellexer7B](./runs.md#intellexer7b) | [Intellexer7C](./runs.md#intellexer7c)

??? abstract "Abstract"
	
	This is a short description of Intellexer QA system used in QA track 2007. The paper is divided into the following sections that describe modules of the system and certain steps of processing.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BondarionokBSMS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/BondarionokBSMS07,
		author = {Aliaksei Bondarionok and Anatoly Bobkov and Liudmila Sudanova and Pavel Mazur and Tatsiana Samuseva},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Intellexer Question Answering},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/effectivesoft.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BondarionokBSMS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Pronto QA System at TREC 2007: Harvesting Hyponyms, Using  Nominalisation Patterns, and Computing Answer Cardinality

_Johan Bos, Edoardo Guzzetti, James R. Curran_

- :fontawesome-solid-user-group: **Participant:** [uroma.bos](./participants.md#uroma.bos)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/urome.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/urome.qa.final.pdf)
- :material-file-search: **Runs:** [pronto07run1](./runs.md#pronto07run1) | [pronto07run2](./runs.md#pronto07run2) | [pronto07run3](./runs.md#pronto07run3)

??? abstract "Abstract"
	
	The backbone of the Pronto QA system is linguistically-principled: Combinatory Categorial Grammar is used to generate syntactic analyses of questions and potential answer snippets, and Discourse Representation Theory is employed as semantic formalism to match the meanings of questions and answers. The key idea of the Pronto system is to use semantics to prune answer candidates, thereby exploiting lexical resources such as WordNet and NomLex to facilitate the selection of answers. The system performed well at TREC-2007 on factoid-questions with an answer accuracy of 22%, a score higher than the median accuracy score of all participating systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BosGC07.bib) "
	```
	@inproceedings{DBLP:conf/trec/BosGC07,
		author = {Johan Bos and Edoardo Guzzetti and James R. Curran},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Pronto {QA} System at {TREC} 2007: Harvesting Hyponyms, Using Nominalisation Patterns, and Computing Answer Cardinality},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/urome.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BosGC07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Lethbridge's Participation in TREC 2007 QA Track

_Yllias Chali, Shafiq R. Joty_

- :fontawesome-solid-user-group: **Participant:** [ulethbridge.chali](./participants.md#ulethbridge.chali)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ulethbridge.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ulethbridge.qa.final.pdf)
- :material-file-search: **Runs:** [UofL](./runs.md#uofl)

??? abstract "Abstract"
	
	Question Answering (QA) is retrieving answers to natural language questions from a collection of documents rather than retrieving relevant documents containing the keywords of the query which is performed by search engines. What a user usually wants is often a precise answer to a question. For example, given the question “Who won the nobel prize in peace in 2006?” what a user really wants is the answer “Dr. Muhammad Yunus”, in stead of reading through lots of documents that contain the words “win”, “nobel”,“prize”, “peace” and “2006” etc. This means that question answering systems will possibly be integral to the next generation of search engines. The Text Retrieval Conference, TREC1 QA track is the major large-scale evaluation environment for open-domain question answering systems. The questions in the TREC-2007 QA track are clustered by target, which is the overall theme or topic of the questions. The track has three types of questions: 1. factoid that require only one correct response, 2. list that require a non redundant list of correct responses and 3. other questions that require a non redundant list of facts about the target that has not already been discovered by a previous answer. We took the approach of designing a question answering system that is based on document tagging and question classification. Question classification extracts useful information (i.e. answer type) from the question about how to answer the question. Document tagging extracts useful information from the documents, which will be used in finding the answer to the question. We used different available tools to tag the documents. Our system classifies the questions using manually developed rules.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChaliJ07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChaliJ07,
		author = {Yllias Chali and Shafiq R. Joty},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Lethbridge's Participation in {TREC} 2007 {QA} Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ulethbridge.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChaliJ07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering with LCC's CHAUCER-2 at TREC 2007

_Andrew Hickl, Kirk Roberts, Bryan Rink, Jeremy Bensley, Tobias Jungen, Ying Shi, John Williams_

- :fontawesome-solid-user-group: **Participant:** [lcc.chaucer](./participants.md#lcc.chaucer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/lcc-hickl.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/lcc-hickl.qa.final.pdf)
- :material-file-search: **Runs:** [LCCFerret](./runs.md#lccferret)

??? abstract "Abstract"
	
	In TREC 2007, Language Computer Corporation explored how a new, semantically-rich framework for information retrieval could be used to boost the overall performance of the answer extraction and answer selection components featured in its CHAUCER-2 automatic question-answering (Q/A) system. By replacing the traditional keyword-based retrieval system used in (?) with a new indexing and retrieval engine capable of retrieving documents or passages based on the distribution of named entities or semantic dependencies, we were able to dramatically enhance CHAUCER-2's overall accuracy, while significantly reducing the number of of candidate answers that were considered by its Answer Ranking and Answer Validation modules.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HicklRRBJSW07.bib) "
	```
	@inproceedings{DBLP:conf/trec/HicklRRBJSW07,
		author = {Andrew Hickl and Kirk Roberts and Bryan Rink and Jeremy Bensley and Tobias Jungen and Ying Shi and John Williams},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering with LCC's {CHAUCER-2} at {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/lcc-hickl.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HicklRRBJSW07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at the TREC 2007 QA Track

_Katja Hofmann, Valentin Jijkoun, Mahboob Alam Khalid, Joris van Rantwijk, Erik F. Tjong Kim Sang_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.deRijke](./participants.md#uamsterdam.derijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uamsterdam-hofmann.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uamsterdam-hofmann.qa.final.pdf)
- :material-file-search: **Runs:** [uams07main](./runs.md#uams07main) | [uams07atch](./runs.md#uams07atch) | [uams07nwrr](./runs.md#uams07nwrr)

??? abstract "Abstract"
	
	In our participation in the TREC 2007 Question Answering (QA) track, we focused on three tasks. First, we processed the new blog corpus and converted it to formats which could be used by our QA system. Second, we rewrote the module interface code in Java in order to improve the maintainability of the system. And third, we added a new table stream which has learned associations between question properties and properties of candidate answers. In the three runs we submitted to the competition, we experimented with answer type checking and web re-ranking. In follow-up experiments we were able to further evaluate the contribution of these two factors, and to evaluate our new table lookup stream and combinations of streams.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HofmannJKRS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/HofmannJKRS07,
		author = {Katja Hofmann and Valentin Jijkoun and Mahboob Alam Khalid and Joris van Rantwijk and Erik F. Tjong Kim Sang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Amsterdam at the {TREC} 2007 {QA} Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uamsterdam-hofmann.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HofmannJKRS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CSAIL at TREC 2007 Question Answering

_Boris Katz, Sue Felshin, Gregory Marton, Federico Mora, Yuan Kui Shen, Gabriel Zaccak, Ammar Ammar, Eric Eisner, Asli Turgut, Linda Brown Westrick_

- :fontawesome-solid-user-group: **Participant:** [mit-csail.katz](./participants.md#mit-csail.katz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/mit.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/mit.qa.final.pdf)
- :material-file-search: **Runs:** [csail1](./runs.md#csail1) | [csail2](./runs.md#csail2) | [csail3](./runs.md#csail3)

??? abstract "Abstract"
	
	MIT CSAIL's entries for the TREC 2007 question answering track built on our systems of previous years, updating them for the new corpora. Our greatest efforts went into the system that handles the 'other' questions, looking for new descriptive information about the topic. We noticed in our experiments with Nuggeteer (Marton and Radul, 2006)1 that some of the parameters made a big difference in the results, and decided to restructure our scoring to be able to tune its parameters. This represents the first such use of the Nuggeteer software that we are aware of, and yielded excellent results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KatzFMMSZAETW07.bib) "
	```
	@inproceedings{DBLP:conf/trec/KatzFMMSZAETW07,
		author = {Boris Katz and Sue Felshin and Gregory Marton and Federico Mora and Yuan Kui Shen and Gabriel Zaccak and Ammar Ammar and Eric Eisner and Asli Turgut and Linda Brown Westrick},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CSAIL} at {TREC} 2007 Question Answering},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/mit.qa.final.pdf},
		timestamp = {Sun, 10 May 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KatzFMMSZAETW07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Interactions to Improve Translation Dictionaries: UNC, Yahoo!  and ciQA

_Diane Kelly, Xin Fu, Vanessa Murdock_

- :fontawesome-solid-user-group: **Participant:** [unorth-carolina.kelly](./participants.md#unorth-carolina.kelly)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/unc-yahoo.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/unc-yahoo.qa.final.pdf)
- :material-file-search: **Runs:** [UNCYA1](./runs.md#uncya1) | [UNCYA2](./runs.md#uncya2) | [UNCYABL30](./runs.md#uncyabl30) | [UNCYAEX1](./runs.md#uncyaex1) | [UNCYAEX2](./runs.md#uncyaex2)

??? abstract "Abstract"
	
	Sentence retrieval is an important step in many question-answering (QA) technologies. However, characteristics of sentences and of the question-answering task itself often make it difficult to apply document retrieval techniques to sentence retrieval. The use of translation dictionaries offers one potentially useful approach to sentence retrieval, but training such dictionaries using QA corpora often introduces noise that can negatively impact retrieval performance. In this study, we experiment with using data elicited from assessors during interactions as training data for a translation dictionary. We employ two different interactions that elicit two types of data: data about assessors' topics and data about retrieved sentences. Results show that using sentence-level relevance feedback to adjust the translation dictionary improved retrieval for about half the topics, but harmed it for the other half.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KellyFM07.bib) "
	```
	@inproceedings{DBLP:conf/trec/KellyFM07,
		author = {Diane Kelly and Xin Fu and Vanessa Murdock},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Interactions to Improve Translation Dictionaries: UNC, Yahoo! and ciQA},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/unc-yahoo.qa.final.pdf},
		timestamp = {Mon, 26 Apr 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KellyFM07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Testing an Entity Ranking Function for English Factoid QA

_Kui-Lam Kwok, Norbert Dinstl_

- :fontawesome-solid-user-group: **Participant:** [queens-college-cuny.kwok](./participants.md#queens-college-cuny.kwok)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/queens.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/queens.qa.final.pdf)
- :material-file-search: **Runs:** [pircs07qa2](./runs.md#pircs07qa2) | [pircs07qa1](./runs.md#pircs07qa1) | [pircs07qa3](./runs.md#pircs07qa3)

??? abstract "Abstract"
	
	Much progress has been made in the English question-answering task since it was initiated in TREC-8 and our last participation in TREC-2001. QA is a complex semantics-oriented task, and it is necessary that much linguistic processing, auxiliary resources, and learning steps are needed to come up with adequate performance to the task [1]. Chinese language factoid QA was first introduced during NTCIR-5 and -6 [2,3] and in which we participated. Because Chinese QA was new with little training data and Chinese linguistic tools and resources were not as readily available as in English, we employed a simple answer ranking technique that depends only on surface term usage statistics in questions and document sentences [4,5]. The outcome has been surprisingly satisfactory, achieving results ~80% of the best [2,3]. We were curious how this approach may perform for English factoid questions, comparing with median result for example. The program was modified to support English in this TREC-2007 QA task. As in Chinese, we made little use of linguistic tools or training data, and no auxiliary resources. It can form a basis result from which more sophisticated tools may enhance. The Sections 2-5 describes our question classification, document processing and retrieval, entity extraction and answer ranker respectively. Section 6 shows our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokD07.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokD07,
		author = {Kui{-}Lam Kwok and Norbert Dinstl},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Testing an Entity Ranking Function for English Factoid {QA}},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/queens.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokD07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Complex Interactive Question Answering Enhanced with Wikipedia

_Ian MacKinnon, Olga Vechtomova_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo-olga](./participants.md#uwaterloo-olga)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uwaterloo-vechtomova.qa.pdf](http://trec.nist.gov/pubs/trec16/papers/uwaterloo-vechtomova.qa.pdf)
- :material-file-search: **Runs:** [UWinitBASE](./runs.md#uwinitbase) | [UWinitWIKI](./runs.md#uwinitwiki) | [UWfinWIKI](./runs.md#uwfinwiki) | [UWfinLINK](./runs.md#uwfinlink) | [UWfinalWIKI](./runs.md#uwfinalwiki) | [UWfinalMAN](./runs.md#uwfinalman)

??? abstract "Abstract"
	
	In ciQA, templates are used with several bracketed items we call ”facets” which are the basis of information being sought. This information is returned in the form of nuggets. Due to the concepts being sought having multiple terms to describe them, it becomes difficult to determine which sentences in the AQUAINT-2 news articles contain the query terms being sought, as they may be represented in the parent document by a variety of different phrases still making reference to the query term. For example, if the term ”John McCain” were being sought, it might appear in an article, however, the sentence which is the vital nugget may simply contain ”Senator McCain”; an imperfect match. Traditional query expansion[5] of facets would introduce new terms which are related but do not necessarily mean the same as the original facet. This does not always help the problem of query terms appearing in relevant documents but not relevant sentences within documents, it only introduces related terms which cannot be considered synonymous with the facet being retrieved. In this year's TREC, we hope to overcome some of this problem by looking for synonyms for facets using Wikipedia. Many of the ciQA facets are proper nouns and most thesauri, such as WordNet, do not contain entries for these. Thus, a new manner of finding synonyms must be found. In recent years, several new approaches have been proposed to use Wikipedia as a source of lexical information[2, 7], as it can be downloaded in its entirety, and contains relatively high quality articles[3].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacKinnonV07.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacKinnonV07,
		author = {Ian MacKinnon and Olga Vechtomova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Complex Interactive Question Answering Enhanced with Wikipedia},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uwaterloo-vechtomova.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacKinnonV07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2007 ciQA Task: University of Maryland

_Nitin Madnani, Jimmy Lin, Bonnie J. Dorr_

- :fontawesome-solid-user-group: **Participant:** [umd-collegepark.oard](./participants.md#umd-collegepark.oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/umd.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/umd.qa.final.pdf)
- :material-file-search: **Runs:** [UMD07MMRa](./runs.md#umd07mmra) | [UMD07MMRaURL](./runs.md#umd07mmraurl) | [UMD07iMASCa](./runs.md#umd07imasca) | [UMD07iMASCaU](./runs.md#umd07imascau) | [UMD07MMRb](./runs.md#umd07mmrb) | [UMD07iMASCb](./runs.md#umd07imascb)

??? abstract "Abstract"
	
	Information needs are complex, evolving, and difficult to express or capture (Taylor, 1962), a fact that is often overlooked by modern information retrieval systems. TREC, through the HARD track, has been attempting to introduce elements of interaction into large-scale evaluations in order to achieve high accuracy document retrieval (Allan, 2005). Previous research has shown that well-constructed clarification questions can yield a better understanding of users' information needs and thereby improve retrieval performance (Lin et al., 2006). Interactive question answering has recently become a focus of research in the context of complex QA. The topics in the ciQA task are substantially different from factoid questions in that the information needs are complex, multi-faceted, and often not well defined or expressed. To investigate the role of interaction in complex QA, we experimented with two approaches. The first approach relied on Maximum Marginal Relevance (MMR) and is described in Section 2. The second approach employed the Multiple Alternative Sentence Compressions (MASC) framework (Zajic, 2007; Madnani et al., 2007), described in Section 3. Section 4 presents official results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MadnaniLD07.bib) "
	```
	@inproceedings{DBLP:conf/trec/MadnaniLD07,
		author = {Nitin Madnani and Jimmy Lin and Bonnie J. Dorr},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2007 ciQA Task: University of Maryland},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/umd.qa.final.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MadnaniLD07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Lymba's PowerAnswer 4 in TREC 2007

_Dan I. Moldovan, Christine Clark, Moldovan Bowden_

- :fontawesome-solid-user-group: **Participant:** [lymba.clark](./participants.md#lymba.clark)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/lymba.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/lymba.qa.final.pdf)
- :material-file-search: **Runs:** [LymbaPA07](./runs.md#lymbapa07)

??? abstract "Abstract"
	
	This paper reports on Lymba Corporation's (a spinoff of Language Computer Corporation) participation in the TREC 2007 Question Answering track. An overview of the Power-Answer 4 question answering system and a discussion of new features added to meet the challenges of this year's evaluation are detailed. Special attention was given to methods for incorporating blogs into the searchable collection, methods for improving answer precision, both statistical and knowledge driven, new mechanisms for recognizing named entities, events, and time expressions, and updated pattern-driven approaches to answer definition questions. Lymba's results in the evaluation are presented at the end of the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoldovanCB07.bib) "
	```
	@inproceedings{DBLP:conf/trec/MoldovanCB07,
		author = {Dan I. Moldovan and Christine Clark and Moldovan Bowden},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Lymba's PowerAnswer 4 in {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/lymba.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MoldovanCB07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDUQA on TREC 2007 QA Track

_Xipeng Qiu, Bo Li, Chao Shen, Lide Wu, Xuanjing Huang, Yaqian Zhou_

- :fontawesome-solid-user-group: **Participant:** [fudanu.wu](./participants.md#fudanu.wu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/fudan.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/fudan.qa.final.pdf)
- :material-file-search: **Runs:** [FDUQAT16A](./runs.md#fduqat16a) | [FDUQAT16B](./runs.md#fduqat16b) | [FDUQAT16C](./runs.md#fduqat16c)

??? abstract "Abstract"
	
	In this year's QA track, we only participant in the main task[Dang 2006]. There are two changes in this year. One change is that time dependent questions are added, and the other is that the corpus is consisted by two collections with different qualities. Therefore, we need add some time limitation in answer filter and merge the answers from two different datasets. The preprocess step is same as our system in TREC QA 2006[Zhou et al. 2006]. We firstly index the documents for fast retrieval. The search engine used in our system is Lucene, an open source document retrieval system. We build four different indexing files. The first two are indexed based on the whole document and the single paragraph of original articles respectively. The rest two are indexed based on the whole document and single paragraph of the morphed articles. Before analyzing question, we process the questions with our question series anaphora resolution. Our modifications mainly are done for factoid questions and definition questions. For list questions, we used the system in TREC 2006[Zhou et al. 2006]. The only modification is that we used a natural paragraph as a unit to index instead of three sentences. For factoid questions, we added query expansion and time filter to our system. For definition questions, we integrate the language model and syntactic features to rank the candidate sentences, and remove the redundancies on sub-sentence level. The rest of the paper is arranged as follows. Section 2, 3 describe our system of factoid and definition questions respectively. Section 4 presents our results in TREC 2007. At last, we give our conclusions in section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QiuLSWHZ07.bib) "
	```
	@inproceedings{DBLP:conf/trec/QiuLSWHZ07,
		author = {Xipeng Qiu and Bo Li and Chao Shen and Lide Wu and Xuanjing Huang and Yaqian Zhou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FDUQA} on {TREC} 2007 {QA} Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/fudan.qa.final.pdf},
		timestamp = {Thu, 23 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QiuLSWHZ07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Concordia University at the TREC 2007 QA Track

_Majid Razmara, Andrew Fee, Leila Kosseim_

- :fontawesome-solid-user-group: **Participant:** [concordiau.kosseim](./participants.md#concordiau.kosseim)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/concordiau.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/concordiau.qa.final.pdf)
- :material-file-search: **Runs:** [QASCU1](./runs.md#qascu1) | [QASCU2](./runs.md#qascu2) | [QASCU3](./runs.md#qascu3)

??? abstract "Abstract"
	
	In this paper, we describe the system we used for the trec-2007 Question Answering Track. For factoid questions our redundancy-based approach using a modified version of aranea was enhanced further. Our list question answerer uses a clustering method to group the candidate answers that co-occur together. It also uses the target and question keywords as spies to pinpoint the right cluster of candidates. To answer other types of questions, our system extracts from Wikipedia articles a list of interest-marking terms and uses them to extract and score sentences from the aquaint-2 and blog document collections using various interest-marking triggers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RazmaraFK07.bib) "
	```
	@inproceedings{DBLP:conf/trec/RazmaraFK07,
		author = {Majid Razmara and Andrew Fee and Leila Kosseim},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Concordia University at the {TREC} 2007 {QA} Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/concordiau.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RazmaraFK07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IITD-IBMIRL System for Question Answering Using Pattern Matching,  Semantic Type and Semantic Category Recognition

_Ashish Kumar Saxena, Ganesh Viswanath Sambhu, Saroj Kaushik, L. Venkata Subramaniam_

- :fontawesome-solid-user-group: **Participant:** [iit-delhi.saxena](./participants.md#iit-delhi.saxena)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/iit-delhi-ibm-india.qa.pdf](http://trec.nist.gov/pubs/trec16/papers/iit-delhi-ibm-india.qa.pdf)
- :material-file-search: **Runs:** [IITDIBM2007F](./runs.md#iitdibm2007f) | [IITDIBM2007S](./runs.md#iitdibm2007s) | [IITDIBM2007T](./runs.md#iitdibm2007t)

??? abstract "Abstract"
	
	A Question Answering (QA) system aims to return exact answers to natural language questions. While today information retrieval techniques are quite successful at locating within large collections of documents those that are relevant to a user's query, QA techniques that extract the exact answer from these retrieved documents still do not obtain very good accuracies. We approached the TREC 2007 Question Answering task as a semantics based question to answer matching problem. Given a question we aimed to extract the relevant semantic entities in it so that we can pin-point the answer. In this paper we show that our technique obtains reasonable accuracy compared to other systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SaxenaSKS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SaxenaSKS07,
		author = {Ashish Kumar Saxena and Ganesh Viswanath Sambhu and Saroj Kaushik and L. Venkata Subramaniam},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IITD-IBMIRL} System for Question Answering Using Pattern Matching, Semantic Type and Semantic Category Recognition},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/iit-delhi-ibm-india.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SaxenaSKS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Semantic Extensions of the Ephyra QA System for TREC 2007

_Nico Schlaefer, Jeongwoo Ko, Justin Betteridge, Manas A. Pathak, Eric Nyberg, Guido Sautter_

- :fontawesome-solid-user-group: **Participant:** [ukarlsruhe-cmu.schlaefer](./participants.md#ukarlsruhe-cmu.schlaefer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/cmu-ukarlsruhe.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/cmu-ukarlsruhe.qa.final.pdf)
- :material-file-search: **Runs:** [Ephyra1](./runs.md#ephyra1) | [Ephyra2](./runs.md#ephyra2) | [Ephyra3](./runs.md#ephyra3)

??? abstract "Abstract"
	
	We describe recent extensions to the Ephyra question answering (QA) system and their evaluation in the TREC 2007 QA track. Existing syntactic answer extraction approaches for factoid and list questions have been complemented with a high-accuracy semantic approach that generates a semantic representation of the question and extracts answer candidates from similar semantic structures in the corpus. Candidates found by different answer extractors are combined and ranked by a statistical framework that integrates a variety of answer validation techniques and similarity measures to estimate a probability for each candidate. A novel answer type classifier combines a statistical model and hand-coded rules to predict the answer type based on syntactic and semantic features of the question. Our approach for the 'other' questions uses Wikipedia and Google to judge the relevance of answer candidates found in the corpora.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchlaeferKBPNS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchlaeferKBPNS07,
		author = {Nico Schlaefer and Jeongwoo Ko and Justin Betteridge and Manas A. Pathak and Eric Nyberg and Guido Sautter},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Semantic Extensions of the Ephyra {QA} System for {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/cmu-ukarlsruhe.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchlaeferKBPNS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Alyssa System at TREC QA 2007: Do We Need Blog06?

_Dan Shen, Michael Wiegand, Andreas Merkel, Stefan Kazalski, Sabine Hunsicker, Jochen L. Leidner, Dietrich Klakow_

- :fontawesome-solid-user-group: **Participant:** [saarlandu.shen](./participants.md#saarlandu.shen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/saarlandu.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/saarlandu.qa.final.pdf)
- :material-file-search: **Runs:** [lsv2007a](./runs.md#lsv2007a) | [lsv2007b](./runs.md#lsv2007b) | [lsv2007c](./runs.md#lsv2007c)

??? abstract "Abstract"
	
	We describe the participation of the Saarland University LSV group in the DARPA/NIST TREC 2007 Q&A track with the Alyssa system, using an approach that combines cascaded language-model based information retrieval (LMIR) with data-driven learning methods for answer extraction and ranking. To test the robustness of this approach that was previously proven on news data also across document collections of varying levels of subjectivity, we test the hypothesis that the answer accuracy over factoid questions does not decrease significantly if blog data is added. Our results show that on the contrary, the method remains competitive on larger datasets with mixed content, such as the union of the AQUAINT 2 (news) and BLOG 06 (blog) corpora (Macdonald and Ounis, 2006). We also present evaluation results on an unofficial set of questions manually generated from BLOG 06 documents, which were created at LSV.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShenWMKHLK07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShenWMKHLK07,
		author = {Dan Shen and Michael Wiegand and Andreas Merkel and Stefan Kazalski and Sabine Hunsicker and Jochen L. Leidner and Dietrich Klakow},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Alyssa System at {TREC} {QA} 2007: Do We Need Blog06?},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/saarlandu.qa.final.pdf},
		timestamp = {Mon, 17 Apr 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ShenWMKHLK07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass Complex Interactive Question Answering (ciQA) 2007: Human Performance  as Question Answerers

_Mark D. Smucker, James Allan, Blagovest Dachev_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/umass.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/umass.qa.final.pdf)
- :material-file-search: **Runs:** [UMassBaseAut](./runs.md#umassbaseaut) | [UMass1](./runs.md#umass1) | [UMass2](./runs.md#umass2) | [UMassIntA](./runs.md#umassinta) | [UMassIntM](./runs.md#umassintm)

??? abstract "Abstract"
	
	Every day, people widely use information retrieval (IR) systems to answer their questions. We utilized the TREC 2007 complex, interactive question answering (ciQA) track to measure the performance of humans using an interactive IR system to answer questions. Using our IR system, assessors searched for relevant documents and recorded answers to their questions. We submitted the assessors' answers without modification as one of our runs. For our other submission, one of the authors used our IR system for an unlimited time and recorded answers to the questions. We found that human performance using an interactive IR system for question answering is variable but that interactive IR systems offer the potential for superior question answering performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmuckerAD07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmuckerAD07,
		author = {Mark D. Smucker and James Allan and Blagovest Dachev},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass Complex Interactive Question Answering (ciQA) 2007: Human Performance as Question Answerers},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/umass.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmuckerAD07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FSC at TREC

_Stephen Taylor, Orlando Montalvo-Huhn, Nikhil Kartha_

- :fontawesome-solid-user-group: **Participant:** [fitchburg-state.taylor](./participants.md#fitchburg-state.taylor)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/fitchburg.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/fitchburg.qa.final.pdf)
- :material-file-search: **Runs:** [eduFsc04](./runs.md#edufsc04) | [eduFsc05](./runs.md#edufsc05)

??? abstract "Abstract"
	
	This is the rst time that Fitchburg State College has entered the competition and the rst project that the students had worked on of this sort. We decided that we would split our time between building an infrastructure and on speci c techniques for information processing, and to use the project to help us understand the problem better for subsequent years. Because of the time we needed to research and understand the problem and when we started we had a real time constraint. We decided to do some fast prototyping and use simple information processing techniques to test the basic infrastructure. To allow for easier insertion of more complex methods we decided on a layered approach to the information processing. A three layer approach seemed to make the most sense. The rst layer would nd the document that may have the answer. The second would try to nd the sentence that answered the question. And the third would try to extract the answer from the sentence. We wanted to try a number of di erent approaches to processing information at each layer. However because of lack of time, we only got a chance to try a few. We spent much of time experimenting with the document retrieval portion. Even when you nd a method, you need time to play with the parameters with the weight multiplier and any number of tweaks. Unfortunately, we didn't get much time to do that.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TaylorMK07.bib) "
	```
	@inproceedings{DBLP:conf/trec/TaylorMK07,
		author = {Stephen Taylor and Orlando Montalvo{-}Huhn and Nikhil Kartha},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FSC} at {TREC}},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/fitchburg.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TaylorMK07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2007 Question Answering Experiments at Tokyo Institute of Technology

_Edward W. D. Whittaker, Matthias H. Heie, Josef R. Novak, Sadaoki Furui_

- :fontawesome-solid-user-group: **Participant:** [tokyo-inst-tech.whittaker](./participants.md#tokyo-inst-tech.whittaker)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/tokyo-it.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/tokyo-it.qa.final.pdf)
- :material-file-search: **Runs:** [asked07a](./runs.md#asked07a) | [asked07b](./runs.md#asked07b) | [asked07c](./runs.md#asked07c)

??? abstract "Abstract"
	
	In this paper we describe Tokyo Institute of Technology's attempt at the TREC2007 question answering (QA) track. Keeping the same theoretical QA model as for the TREC2006 task, this year we once again focused on the factoid QA task, while investigating a new method for sentence retrieval. We deviated from our earlier approach of using web data, and instead relied solely on the supplied news wire and blog data. Our factoid and list score fell significantly from last year, while we achieved a higher other question score compared to TREC2006, using sentence retrieval rather than last year's summarization method.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WhittakerHNF07.bib) "
	```
	@inproceedings{DBLP:conf/trec/WhittakerHNF07,
		author = {Edward W. D. Whittaker and Matthias H. Heie and Josef R. Novak and Sadaoki Furui},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2007 Question Answering Experiments at Tokyo Institute of Technology},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/tokyo-it.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WhittakerHNF07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UAlbany's ILQUA at TREC 2007

_Min Wu, Song Chen, Yu Zhan, Tomek Strzalkowski_

- :fontawesome-solid-user-group: **Participant:** [suny-albany.wu](./participants.md#suny-albany.wu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ualbany-suny.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ualbany-suny.qa.final.pdf)
- :material-file-search: **Runs:** [ILQUA1](./runs.md#ilqua1) | [ILQUA2](./runs.md#ilqua2)

??? abstract "Abstract"
	
	TREC2007 QA track introduced a combined collection of 175GB BLOG data and 2.5GB newswire data. This introduced an additional challenge for an automatic QA system to processes data in different formats without sacrificing the accuracy. In ILQUA we added a data preprocessing component to filter out noisy blog data. ILQUA has been built as an IE-driven QA system; it extracts answers from documents annotated with named entity tags. Answer extraction methods applied are surface text pattern matching, n-gram proximity search and syntactic dependency matching. The answer patterns used in ILQUA are automatically summarized by a supervised learning system and represented in form of regular expressions which contain multiple question terms. In addition to surface text pattern matching, we also adopt N-gram proximity search and syntactic dependency matching. N-grams of question terms are matched around every named entity in the candidate passages and a list of named entities are extracted as answer candidate. These named entities then go through a multi-level syntactic dependency matching component until a final answer is chosen. This year, we modified the component that tackles “Other” questions and applied different method in the two runs we submitted. One method utilized representative words and syntactic patterns, while the other method utilized representative words from TREC data and web data. Figure 1 gives an illustration of components, data flow and control flow of ILQUA. The following sections give detailed discussion of each component of the system, evaluation results, conclusion and future work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuSZS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuSZS07,
		author = {Min Wu and Song Chen and Yu Zhan and Tomek Strzalkowski},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UAlbany's {ILQUA} at {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ualbany-suny.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuSZS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2007 ciQA Track at RMIT and CSIRO

_Mingfang Wu, Andrew Turpin, Falk Scholer, Yohannes Tsegay, Ross Wilkinson_

- :fontawesome-solid-user-group: **Participant:** [rmitu.scholer](./participants.md#rmitu.scholer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/rmit-csiro.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/rmit-csiro.qa.final.pdf)
- :material-file-search: **Runs:** [rmitrun1](./runs.md#rmitrun1) | [rmitrun2](./runs.md#rmitrun2) | [rmitrun3](./runs.md#rmitrun3) | [rmitrun4](./runs.md#rmitrun4) | [rmitrun5](./runs.md#rmitrun5) | [rmitrun6](./runs.md#rmitrun6)

??? abstract "Abstract"
	
	As part of our participation in the 2007 CiQA track, the RMIT and CSIRO team investigated the following three research questions: 1. What contextual words are helpful in improving answer quality? 2. Given two answer lists of different quality, which list would a user prefer? 3. Would a user's preference choice be correlated with her own relevance judgement of an individual list? To explore these questions, we submitted: Four system runs with various query formulation strategies; Two interactive runs, with one interface for the preference choice, and the other one for the relevance judgement of each answer sentence from an answer list.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuTSTW07.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuTSTW07,
		author = {Mingfang Wu and Andrew Turpin and Falk Scholer and Yohannes Tsegay and Ross Wilkinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2007 ciQA Track at {RMIT} and {CSIRO}},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/rmit-csiro.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuTSTW07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Michigan State University at the 2007 TREC ciQA Task

_Chen Zhang, Matthew Gerber, Tyler Baldwin, Steve Emelander, Joyce Yue Chai, Rong Jin_

- :fontawesome-solid-user-group: **Participant:** [mich-stateu.cha](./participants.md#mich-stateu.cha)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/michiganu.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/michiganu.qa.final.pdf)

??? abstract "Abstract"
	
	This is our first participation in the ciQA task. Instead of exploring conversation strategies in question answering [3, 4], we decided to focus on simple interaction strategies using relevance feedback. In our view, the ciQA task is not designed to evaluate user initiative interaction strategies. Since NIST assessors act as users, the motivation to take an initiative is lacking. It is not clear how to encourage the assessors to take the initiative (e.g., by asking additional questions) during the interaction process. We feel in such a setting, relevance feedback or any kind of system initiative interaction strategies seem more appropriate. Therefore, we have focused on variations of relevance feedback in this year's evaluation. For the initial runs, our two submissions were based on two distinct approaches, a heuristic approach and a machine learning approach. Since only two interactive runs can be submitted for evaluation, we decided to focus on one aspect of variation. The only difference between the two interactive and final run systems is how the feedback is solicited and incorporated. Since there are many parameters inherent in the evaluation that affect the outcome of the final runs, only varying one parameter will hopefully allow us to make some preliminary observations about how feedback solicitation can affect final performance. Although manual runs were allowed in this evaluation, all of our runs were created automatically. The following steps were taken during the evaluation. For each topic, the system first generated a query based on its question template and narrative and used this query to retrieve relevant documents. The retrieved documents were then segmented into sentences, which were further ranked and put together as the initial run results. The interactive web pages were generated based on the results from the initial runs. These pages were accessed by NIST assessors. Feedback from assessors was used to create the final run results. In the following sections, we describe in detail the steps taken to create our initial runs and final runs. We also discuss what we have learned from this exercise.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangGBECJ07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangGBECJ07,
		author = {Chen Zhang and Matthew Gerber and Tyler Baldwin and Steve Emelander and Joyce Yue Chai and Rong Jin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Michigan State University at the 2007 {TREC} ciQA Task},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/michiganu.qa.final.pdf},
		timestamp = {Wed, 05 Jan 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangGBECJ07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

