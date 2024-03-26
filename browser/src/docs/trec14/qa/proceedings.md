# Proceedings - Question Answering 2005 

#### Overview of the TREC 2005 Question Answering Track

_Ellen M. Voorhees, Hoa Trang Dang_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/QA.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec14/papers/QA.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC 2005 Question Answering (QA) track contained three tasks: the main question answering task, the document ranking task, and the relationship task. In the main task, question series were used to define a set of targets. Each series was about a single target and contained factoid and list questions. The final question in the series was an “Other” question that asked for additional information about the target that was not covered by previous questions in the series. The main task was the same as the single TREC 2004 QA task, except that targets could also be events; the addition of events and dependencies between questions in a series made the task more difficult and resulted in lower evaluation scores than in 2004. The document ranking task was to return a ranked list of documents for each question from a subset of the questions in the main task, where the documents were thought to contain an answer to the question. In the relationship task, systems were given TREC-like topic statements that ended with a question asking for evidence for a particular relationship.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VoorheesD05.bib) "
	```
	@inproceedings{DBLP:conf/trec/VoorheesD05,
		author = {Ellen M. Voorhees and Hoa Trang Dang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2005 Question Answering Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/QA.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VoorheesD05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploring Document Content with XML to Answer Questions

_Kenneth C. Litkowski_

- :fontawesome-solid-user-group: **Participant:** [clresearch.litkowski](./participants.md#clresearch.litkowski)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/clresearch.pdf](http://trec.nist.gov/pubs/trec14/papers/clresearch.pdf)
- :material-file-search: **Runs:** [clr05](./runs.md#clr05) | [clr05r1](./runs.md#clr05r1) | [clr05r2](./runs.md#clr05r2)

??? abstract "Abstract"
	
	CL Research participated in the question answering track in TREC 2004, submitting runs for the main task, the document relevance task, and the relationship task. The tasks were performed using the Knowledge Management System (KMS), which provides a single interface for question answering, text summarization, information extraction, and document exploration. These tasks are based on creating and exploiting an XML representation of the texts in the AQUAINT collection. Question answering is performed directly within KMS, which answers questions either from the collection or from the Internet projected back onto the collection. For the main task, we submitted one run and our average per-series score was 0.136, with scores of 0.180 for factoid questions, 0.026 for list questions, and 0.152 for “other” questions. For the document ranking task, the average precision was 0.2253 and the R-precision was 0.2405. For the relationship task, we submitted two runs, with scores of 0.276 and 0.216, the first run was the best score on this task. We describe the overall architecture of KMS and how it permits examination of the question-answering task and strategies within TREC, but also in a real-world application in the bioterrorism domain. We also raise some issues concerning the judgments used for evaluating TREC results and their possible relevance in a wider context.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Litkowski05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Litkowski05,
		author = {Kenneth C. Litkowski},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploring Document Content with {XML} to Answer Questions},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/clresearch.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Litkowski05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DalTREC 2005 QA System Jellyfish: Mark-and-Match Approach to Question  Answering

_Tony Abou-Assaleh, Nick Cercone, Jon Doyle, Vlado Keselj, Chris Whidden_

- :fontawesome-solid-user-group: **Participant:** [dalhousieu.keselj](./participants.md#dalhousieu.keselj)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/dalhousieu.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/dalhousieu.qa.pdf)
- :material-file-search: **Runs:** [Dal05s](./runs.md#dal05s) | [Dal05p](./runs.md#dal05p) | [Dal05m](./runs.md#dal05m)

??? abstract "Abstract"
	
	This is the second year that Dalhousie University actively participated in TREC. Three runs were submitted for the Question Answering track. Our results are below the median; however, they're signifantly larger than minimal, the lesson learnt will guide our future development of the system. Our approach was based on a mark-and-match methodology with regular expression rewriting.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Abou-AssalehCDKW05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Abou-AssalehCDKW05,
		author = {Tony Abou{-}Assaleh and Nick Cercone and Jon Doyle and Vlado Keselj and Chris Whidden},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {DalTREC 2005 {QA} System Jellyfish: Mark-and-Match Approach to Question Answering},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/dalhousieu.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Abou-AssalehCDKW05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Towards a Multi-Stream Question Answering-As-XML-Retrieval Strategy

_David Ahn, Sisay Fissaha Adafre, Valentin Jijkoun, Karin Müller, Maarten de Rijke, Erik F. Tjong Kim Sang_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.mueller](./participants.md#uamsterdam.mueller)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uamsterdam.qa.erik.pdf](http://trec.nist.gov/pubs/trec14/papers/uamsterdam.qa.erik.pdf)
- :material-file-search: **Runs:** [uams05all](./runs.md#uams05all) | [uams05rnk](./runs.md#uams05rnk) | [uams05be3](./runs.md#uams05be3) | [uams05s](./runs.md#uams05s) | [uams05l](./runs.md#uams05l)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2005 Question Answering track; our main focus this year was on improving our multi-stream approach to question answering and on making a first step towards a question answering-as-XML retrieval strategy. We provide a detailed account of the ideas underlying our approaches to the QA task, report on our results, and give a summary of our findings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AhnAJMRS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/AhnAJMRS05,
		author = {David Ahn and Sisay Fissaha Adafre and Valentin Jijkoun and Karin M{\"{u}}ller and Maarten de Rijke and Erik F. Tjong Kim Sang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Towards a Multi-Stream Question Answering-As-XML-Retrieval Strategy},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uamsterdam.qa.erik.pdf},
		timestamp = {Tue, 14 Jul 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AhnAJMRS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering with QED at TREC 2005

_Kisuh Ahn, Johan Bos, David Kor, Malvina Nissim, Bonnie L. Webber, James R. Curran_

- :fontawesome-solid-user-group: **Participant:** [uedinburgh.dalmas](./participants.md#uedinburgh.dalmas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uedinburgh-nissim.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/uedinburgh-nissim.qa.pdf)
- :material-file-search: **Runs:** [Edin2005a](./runs.md#edin2005a) | [Edin2005b](./runs.md#edin2005b) | [Edin2005c](./runs.md#edin2005c)

??? abstract "Abstract"
	
	This report describes the system developed by the University of Edinburgh and the University of Sydney for the TREC-2005 question answering evaluation exercise. The backbone of our question-answering platform is QED, a linguistically-principled QA system. We experimented with external sources of knowledge, such as Google and Wikipedia, to enhance the performance of QED, especially for reranking and off-line processing of the corpus. For factoid and list questions we performed significantly above the median accuracy score of all participating systems at TREC 2005.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AhnBKNWC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/AhnBKNWC05,
		author = {Kisuh Ahn and Johan Bos and David Kor and Malvina Nissim and Bonnie L. Webber and James R. Curran},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering with {QED} at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uedinburgh-nissim.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AhnBKNWC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Looking at Limits and Tradeoffs: Sabir Research at TREC 2005

_Chris Buckley_

- :fontawesome-solid-user-group: **Participant:** [sabir.buckley](./participants.md#sabir.buckley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/sabir.tera.robust.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/sabir.tera.robust.qa.pdf)
- :material-file-search: **Runs:** [sab05qa1b](./runs.md#sab05qa1b)

??? abstract "Abstract"
	
	Sabir Research participated in TREC-2005 in the Terabyte, Robust, and document retrieval part of the Question Answering tracks. This writeup focuses on the Robust track, and in particular on a “routing” run that took advantage of relevance judgements for the topics on the old trec V45 collection to construct queries for the new Aquaint collection. The s ¯mart retro tool is described which given a query and the set of relevant documents, con- structs an optimally weighted version of the query. smart_retro is also used to examine the differences in difficulty between the V45 and Aquaint collections (the Aquaint collection is considerably easier). The final part of the paper describes the compression algorithms and tradeoffs that were used in both TREC 2004 and 2005. These were presented in the TREC 2004 speaker session, but never formally written up. The hardware used for all runs was a single commodity PC with a total cost of $1600: $540 for a Dell PC, $520 for four 250 GByte disks, and $500 to bring the memory up to 2.5 GBytes. The information retrieval software used was the research version of SMART 15.0. SMART was originally developed in the early 1960's by Gerard Salton and since then has continued to be a leading research information retrieval tool. It continues to use a statistical vector space model, with stemming, stop words, weighting, inner product similarity function, and ranked retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Buckley05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Buckley05,
		author = {Chris Buckley},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Looking at Limits and Tradeoffs: Sabir Research at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/sabir.tera.robust.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Buckley05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MITRE's Qanda at TREC 14

_John D. Burger, Samuel Bayer_

- :fontawesome-solid-user-group: **Participant:** [mitre.burger](./participants.md#mitre.burger)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/mitre-corp.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/mitre-corp.qa.pdf)
- :material-file-search: **Runs:** [MITRE2005A](./runs.md#mitre2005a) | [MITRE2005B](./runs.md#mitre2005b) | [MITRE2005C](./runs.md#mitre2005c)

??? abstract "Abstract"
	
	Qanda is MITRE's TREC-style question answering system. In recent years, we have been able to apply only a small effort to the TREC QA activity, approximately two person-months this year. (Accordingly, much of this discussion is strikingly similar to prior system descriptions.) We have made some general improvements in Qanda's processing, including genuine question parsing, generalizing answer selection to better handle variant question types like lists and definition questions, and better integration with a maximum entropy answer scorer, both in training and at run time. We have also attempted to better integrate the results of question processing and document retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BurgerB05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BurgerB05,
		author = {John D. Burger and Samuel Bayer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {MITRE's Qanda at {TREC} 14},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/mitre-corp.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BurgerB05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UNT 2005 TREC QA Participation: Using Lemur as IR Search Engine

_Jiangping Chen, Ping Yu, He Ge_

- :fontawesome-solid-user-group: **Participant:** [untexas.chen](./participants.md#untexas.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/unorth-texas.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/unorth-texas.qa.pdf)
- :material-file-search: **Runs:** [UNTQA0503](./runs.md#untqa0503) | [UNTQA0502](./runs.md#untqa0502) | [UNTQA0501](./runs.md#untqa0501)

??? abstract "Abstract"
	
	This paper reports our TREC 2005 QA participation. Our QA system EagleQA developed last year was expanded and modified for this year's QA experiments. Particularly, we used Lemur 4.1 (http://www.lemurproject.org/) as the Information Retrieval (IR) Engine this year to find documents that may contain answers for the test questions from the document collection. Our result shows Lemur did a reasonable job on finding relevant documents. But certainly there is room for further improvement.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenYG05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenYG05,
		author = {Jiangping Chen and Ping Yu and He Ge},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UNT} 2005 {TREC} {QA} Participation: Using Lemur as {IR} Search Engine},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/unorth-texas.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenYG05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM's PIQUANT II in TREC 2005

_Jennifer Chu-Carroll, Pablo Ariel Duboue, John M. Prager, Krzysztof Czuba_

- :fontawesome-solid-user-group: **Participant:** [ibm.prager](./participants.md#ibm.prager)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ibm.tjwatson.qa.prager.pdf](http://trec.nist.gov/pubs/trec14/papers/ibm.tjwatson.qa.prager.pdf)
- :material-file-search: **Runs:** [IBM05C3PD](./runs.md#ibm05c3pd) | [IBM05L3P](./runs.md#ibm05l3p) | [IBM05L1P](./runs.md#ibm05l1p)

??? abstract "Abstract"
	
	This year, the PIQUANT II system we used in the TREC QA track is an improved version over the reengineered system we used in last year's entry [Chu-Carroll et al., 2005]. Our system adopts a multi-agent approach to question answering. In this framework, a question is submitted to multiple agents, each adopting a different question answering strategy and/or consults a different information source to produce a set of answers, which are then combined using a voting scheme to determine the overall system's answer(s) to the question. In our 2005 system, we have made improvements along several dimensions, by improving the performance of select answering agents, by developing two new agents, and finally, by improving our answer resolution algorithm for combining answers from individual agents. In this paper, we describe these improvements and their impact on the factoid, list, and other subtasks in the main task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Chu-CarrollDPC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Chu-CarrollDPC05,
		author = {Jennifer Chu{-}Carroll and Pablo Ariel Duboue and John M. Prager and Krzysztof Czuba},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {IBM's {PIQUANT} {II} in {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ibm.tjwatson.qa.prager.pdf},
		timestamp = {Sat, 21 Jan 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Chu-CarrollDPC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Factoid Question Answering over Unstructured and Structured Web Content

_Silviu Cucerzan, Eugene Agichtein_

- :fontawesome-solid-user-group: **Participant:** [microsoft.brill](./participants.md#microsoft.brill)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/microsoft-res.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/microsoft-res.qa.pdf)
- :material-file-search: **Runs:** [MSRWSQA05](./runs.md#msrwsqa05) | [MSRTQA05](./runs.md#msrtqa05) | [MSRCOMB05](./runs.md#msrcomb05)

??? abstract "Abstract"
	
	We describe our experience with two new, built-from-scratch, web-based question answering systems applied to the TREC 2005 Main Question Answering task, which use complementary models of answering questions over both structured and unstructured content on the Web. Our approaches depart from previous question answering (QA) work in several ways. For unstructured content, we used a web-based system with novel features such as web snippet pattern matching and generic answer type matching using web counts. We also experimented with a new, complementary question answering approach that uses information from the millions of tables and lists that abound on the web. This system attempts to answer factoid questions by guessing relevant rows and fields in matching web tables and integrating the results. We believe a combination of the two approaches holds promise.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CucerzanA05.bib) "
	```
	@inproceedings{DBLP:conf/trec/CucerzanA05,
		author = {Silviu Cucerzan and Eugene Agichtein},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Factoid Question Answering over Unstructured and Structured Web Content},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/microsoft-res.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CucerzanA05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Questions and Relationships at the University of Iowa

_David Eichmann, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [uiowa.eichmann](./participants.md#uiowa.eichmann)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uiowa.geo.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/uiowa.geo.qa.pdf)
- :material-file-search: **Runs:** [UIowaQA0501](./runs.md#uiowaqa0501) | [UIowaQA0502](./runs.md#uiowaqa0502) | [UIowaQA0503](./runs.md#uiowaqa0503) | [UIowa05QAR01](./runs.md#uiowa05qar01)

??? abstract "Abstract"
	
	The University of Iowa participated in the genomics and question answering tracks of TREC-2005. This paper covers only our work in question answering.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannS05,
		author = {David Eichmann and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments in Questions and Relationships at the University of Iowa},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uiowa.geo.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TALP-UPC at TREC 2005: Experiments Using a Voting Scheme Among  Three Heterogeneous QA Systems

_Daniel Ferrés, Samir Kanaan, David Dominguez-Sal, Edgar González, Alicia Ageno, María Fuentes Fort, Horacio Rodríguez, Mihai Surdeanu, Jordi Turmo_

- :fontawesome-solid-user-group: **Participant:** [upc-talp.ferres](./participants.md#upc-talp.ferres)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/upolitecnicade-catalunya.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/upolitecnicade-catalunya.qa.pdf)
- :material-file-search: **Runs:** [talpupc05b](./runs.md#talpupc05b) | [talpupc05c](./runs.md#talpupc05c) | [talpupc05a](./runs.md#talpupc05a)

??? abstract "Abstract"
	
	This paper describes the experiments of the TALP-UPC group for factoid and 'other' (definitional) questions at TREC 2005 Main Question Answering (QA) task. Our current approach for factoid questions is based on a voting scheme among three QA systems: TALP-QA (our previous QA system), Sibyl (a new QA system developed at DAMA-UPC and TALP-UPC), and Aranea (a web-based data-driven approach). For defitional questions, we used two different systems: the TALP-QA Definitional system and LCSUM (a Summarization-based system). Our results for factoid questions indicate that the voting strategy improves the accuracy from 7.5% to 17.1%. While these numbers are low (due to technical problems in the Answer Extraction phase of TALP-QA system) they indicate that voting is a succesful approach for performance boosting of QA systems. The answer to definitional questions is produced by selecting phrases using set of patterns associated with definitions. Its results are 17.2% of F-score in the best configuration of TALP-QA Definitional system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FerresKDGAFRST05.bib) "
	```
	@inproceedings{DBLP:conf/trec/FerresKDGAFRST05,
		author = {Daniel Ferr{\'{e}}s and Samir Kanaan and David Dominguez{-}Sal and Edgar Gonz{\'{a}}lez and Alicia Ageno and Mar{\'{\i}}a Fuentes Fort and Horacio Rodr{\'{\i}}guez and Mihai Surdeanu and Jordi Turmo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TALP-UPC} at {TREC} 2005: Experiments Using a Voting Scheme Among Three Heterogeneous {QA} Systems},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/upolitecnicade-catalunya.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FerresKDGAFRST05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Sheffield's TREC 2005 Q&A Experiments

_Robert J. Gaizauskas, Mark A. Greenwood, Henk Harkema, Mark Hepple, Horacio Saggion, Atheesh Sanka_

- :fontawesome-solid-user-group: **Participant:** [usheffield.gaizauskas](./participants.md#usheffield.gaizauskas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/usheffield.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/usheffield.qa.pdf)
- :material-file-search: **Runs:** [shef05lmg](./runs.md#shef05lmg) | [SHEF05MC](./runs.md#shef05mc) | [SHEF05LC](./runs.md#shef05lc)

??? abstract "Abstract"
	
	Our entries in the TREC 2005 QA evaluation continue experiments carried out as part of TREC 2004. Hence here, as there, we report work on multiple approaches to both the main and document ranking tasks. For query generation and document retrieval we explored two approaches, one based on Lucene 1, the other on MadCow, an in-house boolean search engine. For answer extractrion we have also explored two approaches, one a shallow approach based on semantic typing and question-answer word overlap, the other based on syntactic analysis and logical form matching. As well as continuing independent development of these multiple approaches, we have also concentrated on developing common resources to to be shared between these approaches in order to allow for more principled comparison
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaizauskasGHHSS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaizauskasGHHSS05,
		author = {Robert J. Gaizauskas and Mark A. Greenwood and Henk Harkema and Mark Hepple and Horacio Saggion and Atheesh Sanka},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Sheffield's {TREC} 2005 Q{\&}A Experiments},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/usheffield.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GaizauskasGHHSS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Differential Linguistics at NIST TREC

_Ilya S. Geller_

- :fontawesome-solid-user-group: **Participant:** [lexiclone.geller](./participants.md#lexiclone.geller)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/lexiclone.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/lexiclone.qa.pdf)
- :material-file-search: **Runs:** [lexiclone5](./runs.md#lexiclone5) | [lexicloneB](./runs.md#lexicloneb)

??? abstract "Abstract"
	
	In the course of carrying out NIST TRECs I created and tested a computer program for textual information searches, based on ‘understanding' the meanings of words in texts. The computer using the program ‘understands' not only the abstract, standardized meanings of the words in the text, but the specific, concrete meanings given to those words by the author(s) of the texts. In this article I attempt to bring the language I used to create the algorithm of the program in line with the generally accepted, formalized language of mathematics. (Doing this I must apply the philosophy and metaphysics of Cynicism.)
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Geller05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Geller05,
		author = {Ilya S. Geller},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Differential Linguistics at {NIST} {TREC}},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/lexiclone.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Geller05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering with SEMEX at TREC 2005

_Demetrios G. Glinos_

- :fontawesome-solid-user-group: **Participant:** [ucentralfla.glinos](./participants.md#ucentralfla.glinos)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ucentralfl.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/ucentralfl.qa.pdf)
- :material-file-search: **Runs:** [dggQA05](./runs.md#dggqa05) | [dggQA05X](./runs.md#dggqa05x)

??? abstract "Abstract"
	
	We describe the SEMEX question-answering system and report its performance in the TREC 2005 Question Answering track. Since this was SEMEX's first year participating in the TREC evaluations, implementation teething pains were expected and indeed encountered. Nevertheless, performance against difficult factoid and list questions was supportive of the question answering approach that was implemented.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Glinos05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Glinos05,
		author = {Demetrios G. Glinos},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering with {SEMEX} at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ucentralfl.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Glinos05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Employing Two Question Answering Systems in TREC 2005

_Sanda M. Harabagiu, Dan I. Moldovan, Christine Clark, Mitchell Bowden, Andrew Hickl, Patrick Wang_

- :fontawesome-solid-user-group: **Participant:** [lcc.harabagiu](./participants.md#lcc.harabagiu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/lcc-sanda.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/lcc-sanda.qa.pdf)
- :material-file-search: **Runs:** [lcc05](./runs.md#lcc05) | [lcc05rel1](./runs.md#lcc05rel1) | [lcc05rel2](./runs.md#lcc05rel2)

??? abstract "Abstract"
	
	n 2005, the TREC QA track had two separate tasks: the main task and the relationship task. To participate in TREC 2005 we employed two different QA systems. PowerAnswer-2 was used in the main task, whereas PALANTIR was used for the relationship questions. For the main task, new this year is the use of events as targets in addition to the nominal concepts used last year. Event targets ranged from a nominal event such as “Preakness 1998” to a description of an event as in “Plane clips cable wires in Italian resort”. There were 17 event targets total. Unlike nominal targets, which most often act as the topic of the subsequent questions, events provide a context for the questions. Therefore, targets representing events had questions that asked about participants in the event, about characteristics of the vent and furthermore, had temporal constraints. Also many questions referred to answers of previous questions. To complicate matters, several answers could be candidate for the anaphors used in follow-up questions, but salience mattered. This introduced new complexities for the coreference resolution. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HarabagiuMCBHW05.bib) "
	```
	@inproceedings{DBLP:conf/trec/HarabagiuMCBHW05,
		author = {Sanda M. Harabagiu and Dan I. Moldovan and Christine Clark and Mitchell Bowden and Andrew Hickl and Patrick Wang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Employing Two Question Answering Systems in {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/lcc-sanda.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HarabagiuMCBHW05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Peking University at the TREC 2005 Question and Answering Track

_Jing He, Cheng Chen, Conglei Yao, Ping Yin, Yongjun Bao_

- :fontawesome-solid-user-group: **Participant:** [pekingu.yan](./participants.md#pekingu.yan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/pekingu-he.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/pekingu-he.qa.pdf)
- :material-file-search: **Runs:** [TWQA0501](./runs.md#twqa0501) | [TWQA0502](./runs.md#twqa0502)

??? abstract "Abstract"
	
	This paper describes the architecture and implementation of Tianwang QA system, which can work for the Main task and the Document Ranking task. The system is designed to extract candidate answer snippets from different pipelines, e.g. the high quality search engines' results, the frequently asked question (FAQ) set, and the well-structured web facts, etc..So the system need to process the Web documents, the FAQ corpus and the knowledge base (KB) from the structural web pages, besides analyzing the query, the TREC document retrieval and the answer merging. The external knowledge we made use of, i.e. FAQ and KB, are proved to be effective for our final results. We classify questions with SVM approaches, construct queries in Boolean way, retrieve and rank the passage with span model and extract answers using named entity technologies.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeCYYB05.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeCYYB05,
		author = {Jing He and Cheng Chen and Conglei Yao and Ping Yin and Yongjun Bao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Peking University at the {TREC} 2005 Question and Answering Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/pekingu-he.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeCYYB05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QuALiM at TREC 2005: Web-Question Answering with FrameNet

_Michael Kaisser_

- :fontawesome-solid-user-group: **Participant:** [dfki-saarlandu.kaisser](./participants.md#dfki-saarlandu.kaisser)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/usaarland.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/usaarland.qa.pdf)
- :material-file-search: **Runs:** [mk2005qar1](./runs.md#mk2005qar1) | [mk2005qar2](./runs.md#mk2005qar2)

??? abstract "Abstract"
	
	In this paper I describe my TREC 2005 participation. The system used was-except from one new module-the same as in TREC 2004. In the following I will describe this new module, which uses the annotated Natural Language data collected in the FrameNet project in order to find paraphrases to answer questions. I will furthermore present and discuss the TREC 2005 results and compare them to those achieved in TREC 2004.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Kaisser05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Kaisser05,
		author = {Michael Kaisser},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {QuALiM at {TREC} 2005: Web-Question Answering with FrameNet},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/usaarland.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Kaisser05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### External Knowledge Sources for Question Answering

_Boris Katz, Gregory Marton, Gary C. Borchardt, Alexis Brownell, Sue Felshin, Daniel Loreto, Jesse Louis-Rosenberg, Ben Lu, Federico Mora, Stephan Stiller, Özlem Uzuner, Angela Wilcox_

- :fontawesome-solid-user-group: **Participant:** [mit.katz](./participants.md#mit.katz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/mit-katz.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/mit-katz.qa.pdf)
- :material-file-search: **Runs:** [csail1](./runs.md#csail1) | [csail2](./runs.md#csail2) | [csail3](./runs.md#csail3) | [csail2005m](./runs.md#csail2005m) | [csail2005a](./runs.md#csail2005a)

??? abstract "Abstract"
	
	MIT CSAIL's entries for the TREC Question Answering track (Voorhees, 2005) focused on incorporating external general-knowledge sources into the question answering process. We also explored the effect of document retrieval on factoid question answering, in cooperation with a community focus on document retrieval. For the new relationship task, we present a new passage-retrieval based algorithm emphasizing synonymy, which performed best among automatic systems this year. Our most prominent new external knowledge source is the Wikipedia1, and its most useful component is the synonymy implicit in its subtitles and redirect link structure. Wikipedia is also a large new source of hypernym information. The main task included factoid questions, for which we modified the freely available Web-based Aranea question answering engine; list questions, for which we used hypernym hierarchies to constrain candidate answers; and definitional 'other' questions, for which we combined candidate snippets generated by several previous definition systems using a new novelty-based reranking method inspired by (Allan et al., 2003). [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KatzMBBFLLLMSUW05.bib) "
	```
	@inproceedings{DBLP:conf/trec/KatzMBBFLLLMSUW05,
		author = {Boris Katz and Gregory Marton and Gary C. Borchardt and Alexis Brownell and Sue Felshin and Daniel Loreto and Jesse Louis{-}Rosenberg and Ben Lu and Federico Mora and Stephan Stiller and {\"{O}}zlem Uzuner and Angela Wilcox},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {External Knowledge Sources for Question Answering},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/mit-katz.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KatzMBBFLLLMSUW05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering with Lydia (TREC 2005 QA Track)

_Jae Hong Kil, Levon Lloyd, Steven Skiena_

- :fontawesome-solid-user-group: **Participant:** [suny.skiena](./participants.md#suny.skiena)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/suny-stonybrook.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/suny-stonybrook.qa.pdf)
- :material-file-search: **Runs:** [SUNYSB05qa1](./runs.md#sunysb05qa1) | [SUNYSB05qa2](./runs.md#sunysb05qa2) | [SUNYSB05qa3](./runs.md#sunysb05qa3)

??? abstract "Abstract"
	
	The goal of our participation in TREC 2005 was to determine how effectively our entity recognition/text analysis system, Lydia (http://www.textmap.com) [1-3] could be adapted to question answering. Indeed, our entire QA subsystem consists of only about 2000 additional lines of Perl code. Lydia detects every named entity mentioned in the AQUAINT corpus, and keeps a variety of information on named entities and documents in a relational database. We can collect candidate answers by means of information kept in the database. To produce a response for the main task or a ranked list of documents for the document ranking task, we rank the collected candidate answers or documents using syntactic and statistical analyses. A significant distinction from other question answering systems [4-6] presented earlier at TREC is that we do not use web sources such as Wikipedia and Google to generate candidate answers or answers. Rather, we only use syntactic and statistical features of the test set of questions and corpus provided. Our approach is independent of other sources, and finds answers from the text provided. We describe the design of Lydia and associated algorithms in Section 2, and focus on the design and algorithms of the QA system in Section 3. We then analyze the performance of the QA system in Section 4, and conclude this paper with discussion on future directions in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KilLS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/KilLS05,
		author = {Jae Hong Kil and Levon Lloyd and Steven Skiena},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering with Lydia {(TREC} 2005 {QA} Track)},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/suny-stonybrook.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KilLS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JHU/APL at TREC 2005: QA Retrieval and Robust Tracks

_James Mayfield, Paul McNamee_

- :fontawesome-solid-user-group: **Participant:** [jhu.mayfield](./participants.md#jhu.mayfield)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/jhu-apl.mayfield.qa.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/jhu-apl.mayfield.qa.robust.pdf)
- :material-file-search: **Runs:** [apl05aug](./runs.md#apl05aug) | [apl05w5](./runs.md#apl05w5)

??? abstract "Abstract"
	
	The Johns Hopkins University Applied Physics Laboratory (JHU/APL) focused on the Robust and Question Answering Information Retrieval (QAIR) Tracks at the 2005 TREC conference. For the Robust Track, we attempted to use the difference in retrieval scores between the top retrieved and the 100th document to predict performance; the result was not competitive. For QAIR, we augmented each query with terms that appeared frequently in documents that contained answers to questions from previous question sets; the results showed modest gains from the technique.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MayfieldM05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MayfieldM05,
		author = {James Mayfield and Paul McNamee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{JHU/APL} at {TREC} 2005: {QA} Retrieval and Robust Tracks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/jhu-apl.mayfield.qa.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MayfieldM05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### AnswerFinder at TREC 2005

_Diego Mollá, Menno van Zaanen_

- :fontawesome-solid-user-group: **Participant:** [macquarieu.molla](./participants.md#macquarieu.molla)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/macquarieu.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/macquarieu.qa.pdf)
- :material-file-search: **Runs:** [afrun1](./runs.md#afrun1) | [afrun2](./runs.md#afrun2)

??? abstract "Abstract"
	
	AnswerFinder has been completely redesigned for TREC 2005. The new architecture allows a fast development of question-answering systems for their deployment in the TREC tasks and other applications. The AnswerFinder modules use XML to express the services they provide, and they can be queried with XML for their services. The QA method now incorporates graph-based methods to compute the answerhood of a sentence and pin-point the answer. The system uses a set of graph-based rules that are learnt automatically. Unfortunately the system could not be completed and debugged before the TREC deadline and the runs did not fare well. Currently we are debugging and evaluating the system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MollaZ05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MollaZ05,
		author = {Diego Moll{\'{a}} and Menno van Zaanen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {AnswerFinder at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/macquarieu.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MollaZ05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering Using the DLT System at TREC 2005

_Michael Mulcahy, Kieran White, Igal Gabbay, Aoife O'Gorman, Richard F. E. Sutcliffe_

- :fontawesome-solid-user-group: **Participant:** [ulimerick](./participants.md#ulimerick)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ulimerick.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/ulimerick.qa.pdf)
- :material-file-search: **Runs:** [DLT05QA01](./runs.md#dlt05qa01) | [DLT05QA02](./runs.md#dlt05qa02)

??? abstract "Abstract"
	
	This article summarises our participation in the Question Answering (QA) Track at TREC. Section 2 outlines the architecture of our system. Section 3 describes the changes made for this year. Section 4 summarises the results of our submitted runs while Section 5 presents conclusions and proposes further steps.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MulcahyWGOS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MulcahyWGOS05,
		author = {Michael Mulcahy and Kieran White and Igal Gabbay and Aoife O'Gorman and Richard F. E. Sutcliffe},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering Using the {DLT} System at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ulimerick.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MulcahyWGOS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JAVELIN I and II Systems at TREC 2005

_Eric Nyberg, Robert E. Frederking, Teruko Mitamura, Matthew W. Bilotti, Kerry Hannan, Laurie Hiyakumoto, Jeongwoo Ko, Frank Lin, Lucian Vlad Lita, Vasco Pedro, Andrew Hazen Schlaikjer_

- :fontawesome-solid-user-group: **Participant:** [cmu.nyberg](./participants.md#cmu.nyberg)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/carnegie-mu-javelin.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/carnegie-mu-javelin.qa.pdf)
- :material-file-search: **Runs:** [CMUJAV2005](./runs.md#cmujav2005) | [CMUJAVSEM](./runs.md#cmujavsem) | [CMUJAVSEMMAN](./runs.md#cmujavsemman)

??? abstract "Abstract"
	
	The JAVELIN team at Carnegie Mellon University submitted three question-answering runs for the TREC 2005 evaluation. The JAVELIN I system was used to generate a single submission to the main track, and the JAVELIN II system was used to generate two submissions to the relationship track. In the sections that follow, we separately describe each system and the submission(s) it produced, and conclude with a brief summary.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NybergFMBHHKLLPS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/NybergFMBHHKLLPS05,
		author = {Eric Nyberg and Robert E. Frederking and Teruko Mitamura and Matthew W. Bilotti and Kerry Hannan and Laurie Hiyakumoto and Jeongwoo Ko and Frank Lin and Lucian Vlad Lita and Vasco Pedro and Andrew Hazen Schlaikjer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{JAVELIN} {I} and {II} Systems at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/carnegie-mu-javelin.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NybergFMBHHKLLPS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Building on Redundancy: Factoid Question Answering, Robust Retrieval  and the "Other"

_Dmitri Roussinov, Elena Filatova, Michael Chau, Jose Antonio Robles-Flores_

- :fontawesome-solid-user-group: **Participant:** [arizonau.roussinov](./participants.md#arizonau.roussinov)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/arizonasu.qa.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/arizonasu.qa.robust.pdf)
- :material-file-search: **Runs:** [ASUQA01](./runs.md#asuqa01) | [ASUQA02](./runs.md#asuqa02)

??? abstract "Abstract"
	
	We have explored how redundancy based techniques can be used in improving factoid question answering, definitional questions (“other”), and robust retrieval. For the factoids, we explored the meta approach: we submit the questions to the several open domain question answering systems available on the Web and applied our redundancy-based triangulation algorithm to analyze their outputs in order to identify the most promising answers. Our results support the added value of the meta approach: the performance of the combined system surpassed the underlying performances of its components. To answer definitional (“other”) questions, we were looking for the sentences containing re-occurring pairs of noun entities containing the elements of the target. For robust retrieval, we applied our redundancy based Internet mining technique to identify the concepts (single word terms or phrases) that were highly related to the topic (query) and expanded the queries with them. All our results are above the mean performance in the categories in which we have participated, with one of our robust runs being the best in its category among all 24 participants. Overall, our findings support the hypothesis that using as much as possible textual data, specifically such as mined from the World Wide Web, is extre mely promising.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RoussinovFCR05.bib) "
	```
	@inproceedings{DBLP:conf/trec/RoussinovFCR05,
		author = {Dmitri Roussinov and Elena Filatova and Michael Chau and Jose Antonio Robles{-}Flores},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Building on Redundancy: Factoid Question Answering, Robust Retrieval and the "Other"},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/arizonasu.qa.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RoussinovFCR05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QACTIS-based Question Answering at TREC 2005

_Patrick Schone, Gary M. Ciany, R. Cutts, Paul McNamee, James Mayfield, Thomas Smith_

- :fontawesome-solid-user-group: **Participant:** [nsa.schone](./participants.md#nsa.schone)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/dept-o-defense.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/dept-o-defense.qa.pdf)
- :material-file-search: **Runs:** [QACTIS05v3](./runs.md#qactis05v3) | [QACTIS05v1](./runs.md#qactis05v1) | [QACTIS05v2](./runs.md#qactis05v2)

??? abstract "Abstract"
	
	The QACTIS system is being developed for the eventual purpose of providing a user the capability of multilingual question-answering from multimedia. QACTIS was tested at TREC-2005 as a means of identifying its successes and limitations in answering questions specifically from English newswire text as it moves in the direction of multilingual, multimedia question answering. In this paper, we provide a complete overview of those parts of QACTIS which focus specifically on text question-answering, and we analyze the system's performance at TREC-2005.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchoneCCMMS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchoneCCMMS05,
		author = {Patrick Schone and Gary M. Ciany and R. Cutts and Paul McNamee and James Mayfield and Thomas Smith},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {QACTIS-based Question Answering at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/dept-o-defense.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchoneCCMMS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Syntactic and Semantic Relation Analysis in Question Answering

_Renxu Sun, Jing Jiang, Yee Fan Tan, Hang Cui, Tat-Seng Chua, Min-Yen Kan_

- :fontawesome-solid-user-group: **Participant:** [nus.sun](./participants.md#nus.sun)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/nus.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/nus.qa.pdf)
- :material-file-search: **Runs:** [NUSCHUA1](./runs.md#nuschua1) | [NUSCHUA2](./runs.md#nuschua2) | [NUSCHUA3](./runs.md#nuschua3)

??? abstract "Abstract"
	
	Our participation at TREC this year focuses on integrating dependency and semantic relation analysis of external resources into our existing QA system. In TREC-13, we have proposed the use of dependency relation matching to perform answer extraction for factoid and list questions. The results showed that the technique is effective in answer extraction within the corpus. However, we have also identified some problems and limitations with this technique. First, dependency relation matching does not perform well on short questions, which have only very few key terms. Therefore we need to integrate query expansion and make use of external resources to provide additional contextual information to these short questions. Second, the technique cannot be directly applied to extract answer nuggets from external web pages. As web pages contain much more noise as compared to the corpus, statistical based dependency relation matching tends to make a lot of errors based on our previously trained model on the corpus. Moreover, we do not have sufficient training data to retrain a model on the web. Therefore we propose to use semantic relation analysis to supplement dependency relation analysis to extract answer nuggets for factoid and list questions on the web. Finally, we adopt a soft pattern matching model (Cui et al., 2005) for definition sentence retrieval in the definitional QA task. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SunJTCCK05.bib) "
	```
	@inproceedings{DBLP:conf/trec/SunJTCCK05,
		author = {Renxu Sun and Jing Jiang and Yee Fan Tan and Hang Cui and Tat{-}Seng Chua and Min{-}Yen Kan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Syntactic and Semantic Relation Analysis in Question Answering},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/nus.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SunJTCCK05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Enterprise, QA, Robust and Terabyte Experiments with Hummingbird SearchServer  at TREC 2005

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird.tomlinson](./participants.md#hummingbird.tomlinson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/hummingbird.qa.robust.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/hummingbird.qa.robust.tera.pdf)
- :material-file-search: **Runs:** [humQ05l](./runs.md#humq05l) | [humQ05xl](./runs.md#humq05xl) | [humQ05xle](./runs.md#humq05xle)

??? abstract "Abstract"
	
	Hummingbird participated in 6 tasks of TREC 2005: the email known-item search task of the Enterprise Track, the document ranking task of the Question Answering Track, the ad hoc topic relevance task of the Robust Retrieval Track, and the adhoc, efficiency and named page finding tasks of the Terabyte Track. In the email known-item task, SearchServer found the desired message in the first 10 rows for more than 80% of the 125 queries. In the document ranking task, SearchServer returned an answering document in the first 10 rows for more than 90% of the 50 questions. In the robustness task, SearchServer found a relevant document in the first 10 rows for 88% of the 50 short (title) topics. In the terabyte adhoc and efficiency tasks, SearchServer found a relevant document in the first 10 rows for more than 90% of the 50 title topics. A new retrieval measure, First Relevant Score, is investigated; it is found to more accurately reflect known-item differences than reciprocal rank and to better reflect robustness across topics than the primary measure of the Robust track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson05,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Enterprise, QA, Robust and Terabyte Experiments with Hummingbird SearchServer at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/hummingbird.qa.robust.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2005 Question Answering Experiments at Tokyo Institute of Technology

_Edward W. D. Whittaker, Pierre Chatain, Sadaoki Furui, Dietrich Klakow_

- :fontawesome-solid-user-group: **Participant:** [tokyo-it.whittaker](./participants.md#tokyo-it.whittaker)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/tokyo-inst-tech.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/tokyo-inst-tech.qa.pdf)
- :material-file-search: **Runs:** [asked05a](./runs.md#asked05a) | [asked05b](./runs.md#asked05b) | [asked05c](./runs.md#asked05c)

??? abstract "Abstract"
	
	In this paper we describe Tokyo Institute of Technology's speech group's first attempt at the TREC2005 question answering track which placed us eleventh overall among the best systems of the 30 participants in the track. All our evaluation systems were based on novel, non-linguistic, data-driven approaches to question answering. Our main focus was on the factoid task and we describe in detail one of the new models used in this year's evaluation runs. The list task was treated as a simple extension of the factoid task while the other question task was treated as an automatic summarization problem by important sentence selection. Our best system on the factoid task gave 21.3% correct in first place; our best result on the list task was an average F-score of 0.069 and on the other question task a best average F-score of 0.138.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WhittakerCFK05.bib) "
	```
	@inproceedings{DBLP:conf/trec/WhittakerCFK05,
		author = {Edward W. D. Whittaker and Pierre Chatain and Sadaoki Furui and Dietrich Klakow},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Question Answering Experiments at Tokyo Institute of Technology},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/tokyo-inst-tech.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WhittakerCFK05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ILQUA–An IE-Driven Question Answering System

_Min Wu, Michelle Duan, Samira Shaikh, Sharon G. Small, Tomek Strzalkowski_

- :fontawesome-solid-user-group: **Participant:** [ualbany.min](./participants.md#ualbany.min)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ualbany.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/ualbany.qa.pdf)
- :material-file-search: **Runs:** [ILQUA2](./runs.md#ilqua2) | [ILQUA3](./runs.md#ilqua3) | [ILQUA1](./runs.md#ilqua1)

??? abstract "Abstract"
	
	ILQUA first participated in TREC QA main task in 2003. This year we have made modifications to the system by removing some components with poor performance and enhanced the system with new methods and new components. The newly built ILQUA is an IE-driven QA system. To answer “Factoid” and “List” questions, we apply our answer extraction methods on NE-tagged passages. The answer extraction methods adopted here are surface text pattern matching, n-gram proximity search and syntactic dependency matching. Surface text pattern matching has been applied in some previous TREC QA systems. However, the patterns used in ILQUA are automatically generated by a supervised learning system and represented in a format of regular expressions which can handle up to 4 question terms. N-gram proximity search and syntactic dependency matching are two steps of one component. N-grams of question terms are matched around every named entity in the candidate passages and a list of named entities are generated as answer candidate. These named entities go through a multi-level syntactic dependency matching until a final answer is generated. To answer “Other” questions, we parse the answer sentences of “Other” questions in 2004 main task and built syntactic patterns combined with semantic features. These patterns are applied to the parsed candidate sentences to extract answers of “Other” questions. The evaluation results showed ILQUA has reached an accuracy of 30.9% for factoid questions. ILQUA is an IE-driven QA system without any pre-compiled knowledge base of facts and it doesn't get reference from any other external search engine such as Google. The disadvantage of an IE-driven QA system is that there are some types of questions that can't be answered because the answer in the passages can't be tagged as appropriate NE types. Figure 1 shows the diagram of the ILQUA architecture.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuDSSS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuDSSS05,
		author = {Min Wu and Michelle Duan and Samira Shaikh and Sharon G. Small and Tomek Strzalkowski},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {ILQUA--An IE-Driven Question Answering System},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ualbany.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuDSSS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDUQA on TREC 2005 QA Track

_Lide Wu, Xuanjing Huang, Yaqian Zhou, Zhushuo Zhang, Fen Lin_

- :fontawesome-solid-user-group: **Participant:** [fudan.wu](./participants.md#fudan.wu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/fudanu-wu.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/fudanu-wu.qa.pdf)
- :material-file-search: **Runs:** [FDUQA14B](./runs.md#fduqa14b) | [FDUQA14A](./runs.md#fduqa14a)

??? abstract "Abstract"
	
	In this year's QA Track, we participant in the main and document ranking task and do not take part in the relation task. We put the most effort in factoid and definition questions, and very little on list questions and document ranking task. For factoid questions, we use three QA systems: system 1, system 2 and system 3. System 1 is very similar to our last year's system [Wu et al, 2004] except two main modifications. One is adding an answer validation-feedback scheme. The other is an improved answer projection module. System 2 is a classic QA system that does not use Web. System 3 is a pattern-based system that we used in TREC 2002 evaluation. The main contribution for factoid question is two improvements for Web-based QA system and the system combination. For definition question, we attempt to utilize both the existing definitions in the Web knowledge bases and the automatically generated structured patterns. Effective methods are adopted to make full use of these resources, and they promise high quality response to definition questions. For list questions, we use a pattern-based method to find more answers other than those found in the processing of factoid question. For document ranking task, we only collect the outputs from document searching or answer projection module. In the following, Section 2, 3, 4 will describe our algorithms to factoid, list and definition questions separately. Section 5 will present our results in TREC 2005.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHZZL05.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHZZL05,
		author = {Lide Wu and Xuanjing Huang and Yaqian Zhou and Zhushuo Zhang and Fen Lin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FDUQA} on {TREC} 2005 {QA} Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/fudanu-wu.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHZZL05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Insun05QA on QA Track of TREC 2005

_Yuming Zhao, Zhiming Xu, Yi Guan, Peng Li_

- :fontawesome-solid-user-group: **Participant:** [hit.zhao](./participants.md#hit.zhao)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/harbin-it.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/harbin-it.qa.pdf)
- :material-file-search: **Runs:** [Insun05QA1](./runs.md#insun05qa1)

??? abstract "Abstract"
	
	This is the first time that our group takes part in the QA track. At TREC2005, the system we developed, Insun05QA, participated in the Main Task, which submitted answers to three types of questions: factoid questions, list questions and others questions. And we also submitted the document ranking which our answers are generated from. A new sentence similarity calculating method is used in our Insun05QA system. It can be considered as an extension of vector space model. And our QA system incorporates several useful tools. These tools include WordNet, developed by Princeton University, Minipar by Dekang Lin , and GATE, developed by University of Sheffield. Moreover, external knowledge such as knowledge from Internet is also widely used in our system. Since it is the first time that we take part in QA track and the preparing time is limited, we concentrate on the processing of factoid questions. And the methods we developed to process list and others questions are generated from the method used to process factoid questions. The structure of our Insun05QA system will be describe in Section 2, the details of how we process the factoid, list and others questions will be introduced in Section 3, and our results in TREC2005 will be presented in Section 4.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoXGL05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoXGL05,
		author = {Yuming Zhao and Zhiming Xu and Yi Guan and Peng Li},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Insun05QA on {QA} Track of {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/harbin-it.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoXGL05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

