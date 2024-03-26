# Proceedings - HARD 2005 

#### HARD Track Overview in TREC 2005 High Accuracy Retrieval from  Documents

_James Allan_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/HARD.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec14/papers/HARD.OVERVIEW.pdf)
??? abstract "Abstract"
	
	TREC 2005 saw the third year of the High Accuracy Retrieval from Documents (HARD) track. The HARD track explores methods for improving the accuracy of document retrieval systems, with particular attention paid to the start of the ranked list. Although it has done so in a few different ways in the past, budget realities limited the track to “clarification forms” this year. The question investigated was whether highly focused interaction with the searcher be used to improve the accuracy of a system. Participants created “clarification forms” generated in response to a query—and leveraging any information available in the corpus—that were filled out by the searcher. Typical clarification questions might ask whether some titles seem relevant, whether some words or names are on topic, or whether a short passage of text is related. The following summarizes the changes from the HARD track in TREC 2004 [Allan, 2005]: There was no passage retrieval evaluation as part of the track this year. There was no use of metadata this year. The evaluation corpus was the full AQUAINT collection. In HARD 2003 the track used part of AQUAINT plus additional documents. In HARD 2004 it was a collection of news from 2003 collated especially for HARD. The topics were selected from existing TREC topics. The same topics were used by the Robust track [Voorhees, 2006]. The topics had not been judged against the AQUAINT collection, though had been judged against a different collection. There was no notion of “hard relevance” and “soft relevance”, though documents were judged on a trinary scale of not relevant, relevant, or highly relevant. Clarification forms were allowed to be much more complex this year. Corpus and topic development, clarification form processing, and relevance assessments took place at NIST rather than at the Linguistic Data Consortium (LDC). The official evaluation measure of the track was R-precision. The HARD track's Web page may also contain useful pointers, though is not guaranteed to be in place indefinitely. As of early 2006, it was available at http://ciir.cs.umass.edu/research/hard. For TREC 2006, the HARD track is being “rolled into” the Question Answering track. The new aspect of the QA track is called “ciQA” for “complex, interactive Question Answering.” The goal of ciQA is to investigate interactive approaches to cope with complex information needs specified by a templated query.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Allan05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Allan05,
		author = {James Allan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{HARD} Track Overview in {TREC} 2005 High Accuracy Retrieval from Documents},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/HARD.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Allan05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### When Less is More: Relevance Feedback Falls Short and Term Expansion  Succeeds at HARD 2005

_Fernando Diaz, James Allan_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/umass-hard.pdf](http://trec.nist.gov/pubs/trec14/papers/umass-hard.pdf)
- :material-file-search: **Runs:** [MASS1](./runs.md#mass1) | [MASS2](./runs.md#mass2) | [MASSbaseDEE3](./runs.md#massbasedee3) | [MASSbaseTEE3](./runs.md#massbasetee3) | [MASSbaseTRM3](./runs.md#massbasetrm3) | [MASSbaseDRM3](./runs.md#massbasedrm3) | [MASSpsgRM3R](./runs.md#masspsgrm3r) | [MASSpsgRM3](./runs.md#masspsgrm3) | [MASStrmS](./runs.md#masstrms) | [MASStrmR](./runs.md#masstrmr)

??? abstract "Abstract"
	
	We used clarification forms to study passage term feedback. When compared against pseudo-relevance feedback with an extremely large external corpus, we found that passage feedback resulted in a reduction in performance while term feed back significantly improved recall.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DiazA05.bib) "
	```
	@inproceedings{DBLP:conf/trec/DiazA05,
		author = {Fernando Diaz and James Allan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {When Less is More: Relevance Feedback Falls Short and Term Expansion Succeeds at {HARD} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/umass-hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DiazA05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SAIC & University of Virginia at TREC 2005: HARD Track

_Jonathan Michel, Xiangyu Jin, James C. French_

- :fontawesome-solid-user-group: **Participant:** [saic.michel](./participants.md#saic.michel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/saic-hard.pdf](http://trec.nist.gov/pubs/trec14/papers/saic-hard.pdf)
- :material-file-search: **Runs:** [SAICBASE1](./runs.md#saicbase1) | [SAICBASE2](./runs.md#saicbase2) | [SAIC1](./runs.md#saic1) | [SAIC2](./runs.md#saic2) | [SAICFINAL1](./runs.md#saicfinal1) | [SAICFINAL3](./runs.md#saicfinal3) | [SAICFINAL2](./runs.md#saicfinal2) | [SAICFINAL4](./runs.md#saicfinal4) | [SAICFINAL5](./runs.md#saicfinal5) | [SAICFINAL6](./runs.md#saicfinal6)

??? abstract "Abstract"
	
	SAIC (Science Applications International Corporation) and the University of Virginia collaborated to participate in the HARD (High Accuracy Retrieval from Documents) track of TREC 2005. Two clarification forms (CF) and 8 runs were submitted. The main focus of our work is to estimate the impact of incorrect user judgment on relevance feedback performance. The same set of documents are presented to the user to make judgments with different information shown on two CFs. Theoretically speaking if the user could make 100% accurate judgment, CF2 would perform much better than CF1. However, in practice, the user judgment accuracy is about 77.2% for CF1 and 65.4% for CF2. Thus results from feedback based on CF2 actually performs worse than CF1. This indicates possible unfairness when comparing relevance feedback techniques in a purely automatic evaluation environment where the user is assumed to be 'perfect'.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MichelJF05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MichelJF05,
		author = {Jonathan Michel and Xiangyu Jin and James C. French},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{SAIC} {\&} University of Virginia at {TREC} 2005: {HARD} Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/saic-hard.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MichelJF05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Strathclyde at TREC HARD

_Mark Baillie, David Elsweiler, Emma Nicol, Ian Ruthven, Simon O. Sweeney, Murat Yakici, Fabio Crestani, Monica Landoni_

- :fontawesome-solid-user-group: **Participant:** [ustrathclyde.baillie](./participants.md#ustrathclyde.baillie)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ustrathclyde.hard.pdf](http://trec.nist.gov/pubs/trec14/papers/ustrathclyde.hard.pdf)
- :material-file-search: **Runs:** [STRA1](./runs.md#stra1) | [STRA3](./runs.md#stra3) | [STRA2](./runs.md#stra2) | [STRAxreadG](./runs.md#straxreadg) | [STRAxreadA](./runs.md#straxreada) | [STRAxprfb](./runs.md#straxprfb) | [STRAxmtg](./runs.md#straxmtg) | [STRAxqedt](./runs.md#straxqedt) | [STRAxmta](./runs.md#straxmta) | [STRAxqert](./runs.md#straxqert)

??? abstract "Abstract"
	
	The motivation behind the University of Strathclyde's approach to this years HARD track was inspired from previous experiences by other participants, in particular research by [1], [3] and [4]. A running theme throughout these papers was the underlying hypothesis that a user's familiarity in a topic (i.e. their previous experience searching a subject), will form the basis for what type or style of document they will perceive as relevant. In other words, the user's context with regards to their previous search experience will determine what type of document(s) they wish to retrieve.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BaillieENRSYCL05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BaillieENRSYCL05,
		author = {Mark Baillie and David Elsweiler and Emma Nicol and Ian Ruthven and Simon O. Sweeney and Murat Yakici and Fabio Crestani and Monica Landoni},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Strathclyde at {TREC} {HARD}},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ustrathclyde.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BaillieENRSYCL05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Rutgers Information Interaction Lab at TREC 2005: Trying HARD

_Nicholas J. Belkin, Michael J. Cole, Jacek Gwizdka, Yuelin Li, Jingjing Liu, Gheorghe Muresan, Catherine Smith, Arthur R. Taylor, Xiaojun Yuan, Dmitri Roussinov_

- :fontawesome-solid-user-group: **Participant:** [rutgers.belkin](./participants.md#rutgers.belkin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/rutgersu.hard.murensan.pdf](http://trec.nist.gov/pubs/trec14/papers/rutgersu.hard.murensan.pdf)
- :material-file-search: **Runs:** [RUTGBLDR](./runs.md#rutgbldr) | [RUTG2](./runs.md#rutg2) | [RUTG1](./runs.md#rutg1) | [ALLcs0807](./runs.md#allcs0807) | [UG1cs0807](./runs.md#ug1cs0807) | [RUTBE](./runs.md#rutbe) | [RUTIN](./runs.md#rutin) | [LS1cs0807](./runs.md#ls1cs0807) | [AS1cs0807](./runs.md#as1cs0807) | [US1cs0807](./runs.md#us1cs0807) | [RS1cs0807](./runs.md#rs1cs0807) | [BF3cs0807](./runs.md#bf3cs0807) | [WS1cs0807](./runs.md#ws1cs0807) | [BLcs0807](./runs.md#blcs0807)

??? abstract "Abstract"
	
	Within the structure of the TREC 2005 HARD track guidelines, we investigated the following hypotheses: H1: Query expansion using a “clarity”-based approach will increase effectiveness over baseline queries and baseline queries plus pseudo-relevance feedback; H2: Query expansion based on the Web will increase effectiveness over baseline queries and baseline queries plus pseudo-relevance feedback; H3: Query expansion using terms selected by the searcher from those suggested by clarity modeling and/or the web will increase effectiveness over baseline queries, baseline queries plus pseudo-relevance feedback, and queries expanded by all suggested terms; H4: Query expansion using “problem statements” elicited from the searcher will increase effectiveness over baseline queries and baseline queries plus pseudo-relevance feedback; H5: The effectiveness of query expansion using problem statements will be negatively correlated with query “clarity”. H1 and H2 were tested without user intervention; H3 and H4 were tested using two different “clarification forms”; H5 was tested using the results of the H4 clarification form. Baseline queries were generated from the topic titles and descriptions; query expansion was accomplished by adding terms to the baseline queries, with a variety of weights given to the expansion terms, relative to the baseline terms. Preliminary results indicate that H1, H2, H3 and H4 are in part weakly supported, in that performance is increased over baseline, but it is not increased over pseudo-relevance feedback. H5 was not supported. Combining some degree of user interaction (H3) with pseudo-relevance feedback appears to lead to increased performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BelkinCGLLMSTYR05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BelkinCGLLMSTYR05,
		author = {Nicholas J. Belkin and Michael J. Cole and Jacek Gwizdka and Yuelin Li and Jingjing Liu and Gheorghe Muresan and Catherine Smith and Arthur R. Taylor and Xiaojun Yuan and Dmitri Roussinov},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Rutgers Information Interaction Lab at {TREC} 2005: Trying {HARD}},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/rutgersu.hard.murensan.pdf},
		timestamp = {Tue, 31 Jan 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BelkinCGLLMSTYR05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Pitt at TREC 2005: HARD and Enterprise

_Daqing He, Jae-wook Ahn_

- :fontawesome-solid-user-group: **Participant:** [upittsburgh.he](./participants.md#upittsburgh.he)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/upittsburgh.hard.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/upittsburgh.hard.ent.pdf)
- :material-file-search: **Runs:** [PITTBTD](./runs.md#pittbtd) | [PITTBTDN225](./runs.md#pittbtdn225) | [PITT1](./runs.md#pitt1) | [PITT2](./runs.md#pitt2) | [PITTEC2NOB1](./runs.md#pittec2nob1) | [PITTEC1BWWB](./runs.md#pittec1bwwb) | [PITTEC2B225A](./runs.md#pittec2b225a) | [PITTHDCOMB1](./runs.md#pitthdcomb1)

??? abstract "Abstract"
	
	The University of Pittsburgh team participated in two tracks for TREC 2005: the High Accuracy Retrieval from Documents (HARD) track and the Enterprise Retrieval track. The goal of Pitt's HARD study in TREC 2005 was to examine the effectiveness of applying Self Organizing Maps (SOM) as a visual presentation tool and as a clustering tool in the context of HARD tasks, especially its role in clarification form generation. Our experiment results demonstrate that SOM can be used as a clustering tool to generate terms for query expansion based on interactive relevance feedback. It produced significant improvement over the baseline when measured by R-Prec. However, its effectiveness of being a visualization tool for users to make relevance feedback still needs careful examination and further studies. Our goal in this year's enterprise search track was to study the effect of query expansion based on an expansion corpus in retrieving emails from an email corpus. The expansion corpus consisted of the WWW, People and ESW sub-collections of the W3C test collection. The results indicate that query expansion based on the expansion corpus can achieve significant improvement over the no expansion baselines. However, there is no significant difference to the simpler query expansion approach using blind relevance feedback. Interestingly the terms used in these two query expansion approaches are different, with averagely only 6 term overlap among 20 possible terms. Further study is needed for examining the effect of combining these two approaches.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeA05.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeA05,
		author = {Daqing He and Jae{-}wook Ahn},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Pitt at {TREC} 2005: {HARD} and Enterprise},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/upittsburgh.hard.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeA05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of North Carolina's HARD Track Experiment at TREC 2005

_Diane Kelly, Xin Fu_

- :fontawesome-solid-user-group: **Participant:** [unc.kelly](./participants.md#unc.kelly)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/unc-kelly.hard.pdf](http://trec.nist.gov/pubs/trec14/papers/unc-kelly.hard.pdf)
- :material-file-search: **Runs:** [NCARhard05B](./runs.md#ncarhard05b) | [NCAR1](./runs.md#ncar1) | [NCAR2](./runs.md#ncar2) | [NCAR3](./runs.md#ncar3) | [NCARhard05F1](./runs.md#ncarhard05f1) | [NCARhard05F2](./runs.md#ncarhard05f2) | [NCARhard05F3](./runs.md#ncarhard05f3)

??? abstract "Abstract"
	
	In this year's HARD Track, we focused on two aspects related to the elicitation of relevance feedback: the display of document surrogates and features for identifying and selecting terms. We looked at these issues with respect to interactive query expansion (IQE). In typical interactive query expansion scenarios, users mark documents that they find relevant and the system automatically extracts terms from these documents and adds them to users' queries, or suggests potential query terms from these documents and allows users to determine which of these terms are added to their queries. While a large number of studies have been conducted on IQE, results of such studies do not convey a consistent picture of IQE use and effectiveness. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KellyF05.bib) "
	```
	@inproceedings{DBLP:conf/trec/KellyF05,
		author = {Diane Kelly and Xin Fu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of North Carolina's {HARD} Track Experiment at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/unc-kelly.hard.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KellyF05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Meiji University HARD and Robust Track Experiments

_Kazuya Kudo, Kenji Imai, Makoto Hashimoto, Tomohiro Takagi_

- :fontawesome-solid-user-group: **Participant:** [meijiu.kakuta](./participants.md#meijiu.kakuta)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/meijiu.hard.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/meijiu.hard.robust.pdf)
- :material-file-search: **Runs:** [MeijiHilBL1](./runs.md#meijihilbl1) | [MeijiHilBL2](./runs.md#meijihilbl2) | [MEIJ1](./runs.md#meij1) | [MEIJ2](./runs.md#meij2) | [MeijiHilWN](./runs.md#meijihilwn) | [MeijiHilCWE1](./runs.md#meijihilcwe1) | [MeijiHilCWE2](./runs.md#meijihilcwe2) | [MeijiHilRW](./runs.md#meijihilrw) | [MeijiHilRC](./runs.md#meijihilrc) | [MeijiHilRWC](./runs.md#meijihilrwc) | [MeijiHilMrg](./runs.md#meijihilmrg)

??? abstract "Abstract"
	
	We participated in HARD Track and Robust Track at TREC2005. Our main challenge is to deal with expansion of a word by recognition of context. In HARD Track, we handled semantic expansion of a word. In Robust Track, we tried a challenge to new approach of “Document expansion” by context recognition. In this paper, the next section presents HARD Track. Section 3 describes Robust Track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KudoIHT05.bib) "
	```
	@inproceedings{DBLP:conf/trec/KudoIHT05,
		author = {Kazuya Kudo and Kenji Imai and Makoto Hashimoto and Tomohiro Takagi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Meiji University {HARD} and Robust Track Experiments},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/meijiu.hard.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KudoIHT05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Menagerie of Tracks at Maryland: HARD, Enterprise, QA, and Genomics,  Oh My!

_Jimmy Lin, Eileen G. Abels, Dina Demner-Fushman, Douglas W. Oard, Philip Fei Wu, Yejun Wu_

- :fontawesome-solid-user-group: **Participant:** [umaryland.oard](./participants.md#umaryland.oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/umaryland-lin.hard.ent.qa.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/umaryland-lin.hard.ent.qa.geo.pdf)
- :material-file-search: **Runs:** [MARYB1](./runs.md#maryb1) | [MARYB2](./runs.md#maryb2) | [MARYB3](./runs.md#maryb3) | [MARY1](./runs.md#mary1) | [MARY05C1](./runs.md#mary05c1) | [MARY05C2](./runs.md#mary05c2) | [MARY05C3](./runs.md#mary05c3)

??? abstract "Abstract"
	
	This year, the University of Maryland participated in four separate tracks: HARD, enterprise, question answering, and genomics. Our HARD experiments involved a trained intermediary who searched for documents on behalf of the user, created clarification forms manually, and exploited user responses accordingly. The aim was to better understand the nature of single-iteration clarification dialogs and to develop an “ontology of clarifications” that can be leveraged to guide system development. For the enterprise track, we submitted official runs to the Known Item Search and the Discussion Search tasks. Document transformation to normalize dates and version numbers was found to be helpful, but suppression of text quoted from earlier messages and expansion of the indexed terms for a message based on subject line threading proved to not be. For the QA track, we submitted a manual run of “other” questions in an effort to quantify human performance on the task. Our genomics track participation was in collaboration with the National Library of Medicine, and is primarily reported in NLM's overview paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinADOWW05.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinADOWW05,
		author = {Jimmy Lin and Eileen G. Abels and Dina Demner{-}Fushman and Douglas W. Oard and Philip Fei Wu and Yejun Wu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Menagerie of Tracks at Maryland: HARD, Enterprise, QA, and Genomics, Oh My!},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/umaryland-lin.hard.ent.qa.geo.pdf},
		timestamp = {Sat, 29 Jul 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LinADOWW05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NLPR at TREC 2005: HARD Experiments

_Bibo Lv, Jun Zhao_

- :fontawesome-solid-user-group: **Participant:** [cas.nlpr.jzhao](./participants.md#cas.nlpr.jzhao)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-nlpr.hard.pdf](http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-nlpr.hard.pdf)
- :material-file-search: **Runs:** [NLPRB](./runs.md#nlprb) | [CASP1](./runs.md#casp1) | [CASP2](./runs.md#casp2) | [NLPRCF1CF2](./runs.md#nlprcf1cf2) | [NLPRCF1](./runs.md#nlprcf1) | [NLPRCF2](./runs.md#nlprcf2) | [NLPRCF1S1](./runs.md#nlprcf1s1) | [NLPRCF1S2](./runs.md#nlprcf1s2) | [NLPRCF1W](./runs.md#nlprcf1w) | [NLPRCF1S1CF2](./runs.md#nlprcf1s1cf2) | [NLPRCF1S2CF2](./runs.md#nlprcf1s2cf2) | [NLPRCF1WCF2](./runs.md#nlprcf1wcf2)

??? abstract "Abstract"
	
	It is the third time that Chinese Information Processing Group of NLPR takes part in TREC. In the past, we participated in Novelty track and Robust track, in which we had evaluated our two key notions: Window-based Retrieval Algorithm and Result Emerging Strategy [1][2]. This year we focus on investigating the significance of relevance feedback, so HARD track is our best choice. HARD2005 is very different from that in the past two years. Firstly, Metadata is removed from topic description so that the topic description in HARD is the same as that of Robust track. Secondly, passage retrieval is cancelled this year. The paper introduces our work on HARD Track in TREC 2005, mainly (1) we propose a new feature selection method for query expansion in relevance feedback; (2) we adopt some query expansion methods. Our paper is organized as follows. Section 2 introduces our system, a new term selection algorithm for query expansion, and our clarification forms. Section 3 presents our query expansion methods. In section 4 experimental results are given, and finally we conclude our work in section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LvZ05.bib) "
	```
	@inproceedings{DBLP:conf/trec/LvZ05,
		author = {Bibo Lv and Jun Zhao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{NLPR} at {TREC} 2005: {HARD} Experiments},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-nlpr.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LvZ05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Lowlands' TREC Experiments 2005

_Henning Rode, Djoerd Hiemstra, Georgina Ramírez, Thijs Westerveld, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [utwente.rode](./participants.md#utwente.rode)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/lowlands-team.hard.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/lowlands-team.hard.ent.pdf)
- :material-file-search: **Runs:** [TWENbase1](./runs.md#twenbase1) | [TWENbase2](./runs.md#twenbase2) | [TWEN1](./runs.md#twen1) | [TWEN2](./runs.md#twen2) | [TWENblind1](./runs.md#twenblind1) | [TWENall1](./runs.md#twenall1) | [TWENdiff1](./runs.md#twendiff1) | [TWENall2](./runs.md#twenall2) | [TWENdiff2](./runs.md#twendiff2) | [TWENblind2](./runs.md#twenblind2)

??? abstract "Abstract"
	
	This paper describes our participation to the TREC HARD track (High Accuracy Retrieval of Documents) and the TREC Enterprise track. The main goal of our HARD participation is the development and evaluation of so-called query profiles: Short summaries of the retrieved results that enable the user to perform more focused search, for instance by zooming in on a particular time period. The main goal of our Enterprise track participation is to investigate the potential of the structural information for this type of retrieval task. In particular, we study the use of the thread information and the subject and header fields of the email documents. As a secondary and long standing research goal, we aim at developing an information retrieval framework that supports many diverse retrieval applications by means of one simple yet powerful query language (similar to SQL or relational algebra) that hides the implementation details of retrieval approaches from the application developer, while still giving the application developer control over the ranking process. Both the HARD system and the Enterprise system (as well as our TRECVID video retrieval system [14]) are based on MonetDB, an open source database system developed at CWI [1]. The paper is organised as follows. First, we discusses our participation in the HARD track. We define query profiles and discuss the way we generate them in Section 2. Section 3 describes the clarification forms used and Section 4 explains how we refine the queries and rank the results. We end this part by analysing our experimental results in Section 5 and giving some conclusions for this track in Section 6. The second part of the paper discusses our participation in the enterprise track. We start by describing the system and experimental setup in Section 7. Section 8 discusses the approaches taken for each of the subtasks and Section 9 analyses the results. We end by giving some conclusions and future work for this track in Section 10. The final part of the paper describes our future plans for building a so-called parameterised search engine within the Dutch National project MultimediaN.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RodeHRWV05.bib) "
	```
	@inproceedings{DBLP:conf/trec/RodeHRWV05,
		author = {Henning Rode and Djoerd Hiemstra and Georgina Ram{\'{\i}}rez and Thijs Westerveld and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Lowlands' {TREC} Experiments 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/lowlands-team.hard.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RodeHRWV05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Interactive Construction of Query Language Models - UIUC TREC  2005 HARD Track Experiments

_Bin Tan, Atulya Velivelli, Hui Fang, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [uiuc.zhai](./participants.md#uiuc.zhai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.hard.pdf](http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.hard.pdf)
- :material-file-search: **Runs:** [UIUC05Hardb0](./runs.md#uiuc05hardb0) | [UIUC1](./runs.md#uiuc1) | [UIUC2](./runs.md#uiuc2) | [UIUC3](./runs.md#uiuc3) | [UIUChTFB1](./runs.md#uiuchtfb1) | [UIUChTFB3](./runs.md#uiuchtfb3) | [UIUChTFB6](./runs.md#uiuchtfb6) | [UIUChCFB1](./runs.md#uiuchcfb1) | [UIUChCFB3](./runs.md#uiuchcfb3) | [UIUChCFB6](./runs.md#uiuchcfb6)

??? abstract "Abstract"
	
	In the language modeling approach, feedback is often modeled as estimating an improved query model or relevance model based on a set of feedback documents [3, 1]. This is in line with the traditional way of doing relevance feedback - presenting the user with documents or passages for relevance judgment and then extracting terms from the judged documents or passages to improve a query model. Such an indirect way of obtaining help from a user to construct a query model has the drawback that irrelevant terms that occur with relevant ones in the judged content may be erroneously used for query model modification. A more direct way to involve a user in improving the query model is to present some candidate terms to a user and directly ask the user to judge the relevance of each term or specify the probability of each term. This strategy has been discussed in [2], but has not been seriously studied in any existing work. In participating in the TREC 2005 HARD Track task, we explored how to exploit term-based feedback to better involve a user in constructing an improved query model for information retrieval with language models. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TanVFZ05.bib) "
	```
	@inproceedings{DBLP:conf/trec/TanVFZ05,
		author = {Bin Tan and Atulya Velivelli and Hui Fang and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Interactive Construction of Query Language Models - {UIUC} {TREC} 2005 {HARD} Track Experiments},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TanVFZ05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments for HARD and Enterprise Tracks

_Olga Vechtomova, Maheedhar Kolla, Murat Karamuftuoglu_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo.vechtomova](./participants.md#uwaterloo.vechtomova)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uwaterloo-vechtomova.hard.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/uwaterloo-vechtomova.hard.ent.pdf)
- :material-file-search: **Runs:** [UWATbaseT](./runs.md#uwatbaset) | [UWATbaseTD](./runs.md#uwatbasetd) | [UWAT1](./runs.md#uwat1) | [UWAT2](./runs.md#uwat2) | [UWAT3](./runs.md#uwat3) | [UwatHARDexp1](./runs.md#uwathardexp1) | [UwatHARDexp2](./runs.md#uwathardexp2) | [UwatHARDexp3](./runs.md#uwathardexp3) | [UWAThardLC1](./runs.md#uwathardlc1)

??? abstract "Abstract"
	
	The main theme in our participation in this year's HARD track was experimentation with the effect of lexical cohesion on document retrieval. Lexical cohesion is a major characteristic of natural language texts, which is achieved through semantic connectedness between words in text, and expresses continuity between the parts of text [7]. Segments of text which are about the same or similar subjects (topics) have higher lexical cohesion, i.e. share a larger number of words than unrelated segments. We have experimented with two approaches to the selection of query expansion terms based on lexical cohesion: (1) by selecting query expansion terms that form lexical links between the distinct original query terms in the document (section 1.1); and (2) by identifying lexical chains in the document and selecting query expansion terms from the strongest lexical chains (section 1.2).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VechtomovaKK05.bib) "
	```
	@inproceedings{DBLP:conf/trec/VechtomovaKK05,
		author = {Olga Vechtomova and Maheedhar Kolla and Murat Karamuftuoglu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments for {HARD} and Enterprise Tracks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uwaterloo-vechtomova.hard.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VechtomovaKK05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2005: HARD Track

_Miao Wen, Xiangji Huang, Aijun An, Yan Rui Huang_

- :fontawesome-solid-user-group: **Participant:** [yorku.huang](./participants.md#yorku.huang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/yorku-huang.hard.pdf](http://trec.nist.gov/pubs/trec14/papers/yorku-huang.hard.pdf)
- :material-file-search: **Runs:** [york05hb1](./runs.md#york05hb1) | [york05hb2](./runs.md#york05hb2) | [york05hb3](./runs.md#york05hb3) | [YORK1](./runs.md#york1) | [YORK2](./runs.md#york2) | [YORK3](./runs.md#york3) | [YORK4](./runs.md#york4) | [york05ha1](./runs.md#york05ha1) | [york05ha2](./runs.md#york05ha2) | [york05ha3](./runs.md#york05ha3) | [york05ha4](./runs.md#york05ha4) | [york05ha5](./runs.md#york05ha5)

??? abstract "Abstract"
	
	In an IR model, “user”, “query” and “result” are three important components. Traditionally, a query is considered to be independent of the user. IR systems search documents without considering who issues the query and why the query is asked. However, those factors can affect the user's satisfaction about the result. The information about the user, such as the genre preference of the user, occupation of the user, location of the user, which are normally called personalized information, indicate users' preferences to the retrieval result. We demonstrate the effectiveness of a dual indexing technique and a feedback method on the HARD 2005 data set. We also propose a non-content based method to measure user's familiarity to a query. A similarity model is built to utilize the familiarity information and to improve the overall performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WenHAH05.bib) "
	```
	@inproceedings{DBLP:conf/trec/WenHAH05,
		author = {Miao Wen and Xiangji Huang and Aijun An and Yan Rui Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2005: {HARD} Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/yorku-huang.hard.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WenHAH05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC 2005 HARD, Robust, and SPAM Tracks

_Kiduk Yang, Ning Yu, Nicholas George, Aaron Loehrlein, David McCaulay, Hui Zhang, Shahrier Akram, Jue Mei, Ivan Record_

- :fontawesome-solid-user-group: **Participant:** [indianau.yang](./participants.md#indianau.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/indianau-bloom.hard.robust.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/indianau-bloom.hard.robust.spam.pdf)
- :material-file-search: **Runs:** [wdf1t10q1](./runs.md#wdf1t10q1) | [wdf1t3qf2](./runs.md#wdf1t3qf2) | [wdoqdn1d2](./runs.md#wdoqdn1d2) | [wdoqsz1d2](./runs.md#wdoqsz1d2) | [INDI1](./runs.md#indi1) | [INDI2](./runs.md#indi2) | [wf1t10q1RCDX](./runs.md#wf1t10q1rcdx) | [wf1t10q1RODX](./runs.md#wf1t10q1rodx) | [wf2t3qs1RODX](./runs.md#wf2t3qs1rodx) | [wf1t3qdROD10](./runs.md#wf1t3qdrod10) | [wf2t3qs1RCX](./runs.md#wf2t3qs1rcx) | [wf1t3qdRC10](./runs.md#wf1t3qdrc10)

??? abstract "Abstract"
	
	Web Information Discovery Tool (WIDIT) Laboratory at the Indiana University School of Library and Information Science participated in the HARD, Robust, and SPAM tracks in TREC-2005. The basic approach of WIDIT is to combine multiple methods as well as to leverage multiple sources of evidence. Our main strategies for the tracks were: query expansion and fusion optimization for the HARD and Robust tracks; and combination of probabilistic, rule-based, pattern-based, and blacklist email filters for the SPAM track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYGLMZAMR05.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYGLMZAMR05,
		author = {Kiduk Yang and Ning Yu and Nicholas George and Aaron Loehrlein and David McCaulay and Hui Zhang and Shahrier Akram and Jue Mei and Ivan Record},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC} 2005 HARD, Robust, and {SPAM} Tracks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/indianau-bloom.hard.robust.spam.pdf},
		timestamp = {Wed, 29 Jun 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YangYGLMZAMR05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Relevance Feedback by Exploring the Different Feedback Sources and  Collection Structure

_Junlin Zhang, Le Sun, Yuanhua Lv, Wei Zhang_

- :fontawesome-solid-user-group: **Participant:** [cas.zhang](./participants.md#cas.zhang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-zhang.hard.pdf](http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-zhang.hard.pdf)
- :material-file-search: **Runs:** [CASS1](./runs.md#cass1) | [CASS2](./runs.md#cass2) | [cassbase](./runs.md#cassbase) | [cassbasere](./runs.md#cassbasere) | [cassgoogle](./runs.md#cassgoogle) | [casstopdoc](./runs.md#casstopdoc) | [cassself](./runs.md#cassself) | [cassselfre](./runs.md#cassselfre) | [cassallfb](./runs.md#cassallfb) | [cassallre](./runs.md#cassallre) | [cassallfb2](./runs.md#cassallfb2) | [cassallfb2re](./runs.md#cassallfb2re)

??? abstract "Abstract"
	
	In HARD track of HARD 2005, we classify the 50 queries into 7 categories and make use of 3 kinds of feedback sources in various tasks. We find that the different kinds of queries perform differently in feedback tasks and the “CASE “ and “EVENT” queries are more sensitive to the feedback source. We also explore the internal structure of corpus and try to estimate the distribution of relevant documents within sub-collections. The experiments show that this technology is partly effective and the main existing problem is how to predict the distribution more precisely.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangSLZ05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangSLZ05,
		author = {Junlin Zhang and Le Sun and Yuanhua Lv and Wei Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Relevance Feedback by Exploring the Different Feedback Sources and Collection Structure},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-zhang.hard.pdf},
		timestamp = {Fri, 21 Aug 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhangSLZ05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

