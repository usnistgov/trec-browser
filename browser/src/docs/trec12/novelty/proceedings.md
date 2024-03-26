# Proceedings - Novelty 2003 

#### Overview of the TREC 2003 Novelty Track

_Ian Soboroff, Donna Harman_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/NOVELTY.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec12/papers/NOVELTY.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The novelty track was first introduced in TREC 2002. Given a TREC topic and an ordered list of documents, systems must find the relevant and novel sentences that should be returned to the user from this set. This task integrates aspects of passage retrieval and information filtering. This year, rather than using old TREC topics and documents, we developed fifty new topics specifically for the novelty track. These topics were of two classes: “events” and “opinions”. Additionally, the documents were ordered chronologically, rather than according to a retrieval status value. There were four tasks which provided systems with varying amounts of relevance or novelty information as training data. Fourteen groups participated in the track this year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SoboroffH03.bib) "
	```
	@inproceedings{DBLP:conf/trec/SoboroffH03,
		author = {Ian Soboroff and Donna Harman},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2003 Novelty Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {38--53},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/NOVELTY.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SoboroffH03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### From TREC to DUC to TREC Again

_John M. Conroy, Daniel M. Dunlavy, Dianne P. O'Leary_

- :fontawesome-solid-user-group: **Participant:** [ccs.conroy](./participants.md#ccs.conroy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ccs.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/ccs.novelty.pdf)
- :material-file-search: **Runs:** [ccsumlaqr](./runs.md#ccsumlaqr) | [ccsumrelqr](./runs.md#ccsumrelqr) | [ccsumrelsvd](./runs.md#ccsumrelsvd) | [ccsummeosvd](./runs.md#ccsummeosvd) | [ccsummeoqr](./runs.md#ccsummeoqr) | [ccsum2svdpqr](./runs.md#ccsum2svdpqr) | [ccsumt2svdqr](./runs.md#ccsumt2svdqr) | [ccsumt2pqr](./runs.md#ccsumt2pqr) | [ccsumt2qr](./runs.md#ccsumt2qr) | [ccsum3svdpqr](./runs.md#ccsum3svdpqr) | [ccsum3qr](./runs.md#ccsum3qr) | [ccsum3pqr](./runs.md#ccsum3pqr) | [ccsumt4qr](./runs.md#ccsumt4qr) | [ccsumt4sqr01](./runs.md#ccsumt4sqr01) | [ccsum4spq001](./runs.md#ccsum4spq001) | [ccsumt4pqr](./runs.md#ccsumt4pqr) | [ccsum4svdpqr](./runs.md#ccsum4svdpqr)

??? abstract "Abstract"
	
	The Document Understanding Conference (DUC) uses TREC data as a test bed for algorithms for single and multiple document summarization. For the 2003 DUC task of choosing relevant and novel sentences, we tested a system based on a Hidden Markov Model (HMM). In this work, we use variations of this system on the tasks of the TREC Novelty Track for finding relevant and new sentences. Our complete information retrieval system couples a query handler, a document clusterer, and a summary generator with a convenient user interface. For the TREC tasks, we use only the summarization part of the system, based on an HMM, to find relevant sentences in a document and we use linear algebra techniques to determine the new sentences among these. For the tasks in the 2003 TREC Novelty Track we used a simple preprocessing of the data which consisted of term tokenization and SGML DTD processing. Details of each of these methods are presented in Section 2. The algorithms for choosing relevant sentences were tuned versions of those presented by members of our group in the past DUC evaluations (see [5, 8, 15] for more details). The enhancements to the previous system are detailed in Section 3. Several methods were explored to find a subset of the relevant sentences that had good coverage but low redundancy. In our multi-document summarization system, we used the QR algorithm on term-sentence matrices. For this work, we explored the use of the singular value decomposition as well as two variants of the QR algorithm. These methods are defined in Section 4. The evaluation of these methods is discussed in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ConroyDO03.bib) "
	```
	@inproceedings{DBLP:conf/trec/ConroyDO03,
		author = {John M. Conroy and Daniel M. Dunlavy and Dianne P. O'Leary},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {From {TREC} to {DUC} to {TREC} Again},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {293--302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/ccs.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ConroyDO03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Trec Novelty Track At IRIT-SIG

_Taoufiq Dkaki, Josiane Mothe_

- :fontawesome-solid-user-group: **Participant:** [irit-sig.boughanem](./participants.md#irit-sig.boughanem)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/irit-sig.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/irit-sig.novelty.pdf)
- :material-file-search: **Runs:** [IRITfNegR2](./runs.md#iritfnegr2) | [IRITf2bis](./runs.md#iritf2bis) | [IRITfb1MtmIb](./runs.md#iritfb1mtmib) | [IRITnip2bis](./runs.md#iritnip2bis) | [IRITnb1MtmI4](./runs.md#iritnb1mtmi4) | [Irit1](./runs.md#irit1) | [Irit5q](./runs.md#irit5q) | [IritMtm4](./runs.md#iritmtm4) | [IritMtm5](./runs.md#iritmtm5) | [Irito](./runs.md#irito)

??? abstract "Abstract"
	
	In TREC 2003, IRIT improved the strategy that was introduced in TREC 2002. A sentence is considered as relevant if it matches the topic with a certain level of coverage. This coverage depends on the category of terms used in the texts. Different types of terms have been defined: highly relevant, scarcely relevant, non-relevant and highly non-relevant. With regard to the novelty part, a sentence is considered as novel if its similarity with previously processed sentences and with the n-best-matching sentences does not exceed certain thresholds.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DkakiM03.bib) "
	```
	@inproceedings{DBLP:conf/trec/DkakiM03,
		author = {Taoufiq Dkaki and Josiane Mothe},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Trec Novelty Track At {IRIT-SIG}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {337--342},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/irit-sig.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DkakiM03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Novelty, Genes and Questions at the University of Iowa

_David Eichmann, Padmini Srinivasan, Marc Light, Hudong Wang, Xin Ying Qiu, Robert J. Arens, Aditya Kumar Sehgal_

- :fontawesome-solid-user-group: **Participant:** [uiowa.eichmann](./participants.md#uiowa.eichmann)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uiowa.novelty.genomics.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/uiowa.novelty.genomics.qa.pdf)
- :material-file-search: **Runs:** [UIowa03Nov01](./runs.md#uiowa03nov01) | [UIowa03Nov02](./runs.md#uiowa03nov02) | [UIowa03Nov03](./runs.md#uiowa03nov03) | [UIowa03Nov05](./runs.md#uiowa03nov05) | [UIowa03Nov04](./runs.md#uiowa03nov04) | [UIowa03Nov07](./runs.md#uiowa03nov07) | [UIowa03Nov08](./runs.md#uiowa03nov08) | [UIowa03Nov09](./runs.md#uiowa03nov09) | [UIowa03Nov06](./runs.md#uiowa03nov06) | [UIowa03Nov10](./runs.md#uiowa03nov10) | [UIowa03Nov11](./runs.md#uiowa03nov11) | [UIowa03Nov12](./runs.md#uiowa03nov12) | [UIowa03Nov14](./runs.md#uiowa03nov14) | [UIowa03Nov13](./runs.md#uiowa03nov13)

??? abstract "Abstract"
	
	The University of Iowa participated in the novelty, genomics and question answering tracks of TREC-2003.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannSLWQAS03.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannSLWQAS03,
		author = {David Eichmann and Padmini Srinivasan and Marc Light and Hudong Wang and Xin Ying Qiu and Robert J. Arens and Aditya Kumar Sehgal},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments in Novelty, Genes and Questions at the University of Iowa},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {678--685},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uiowa.novelty.genomics.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannSLWQAS03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NLPR at TREC 2003: Novelty and Robust

_Qianli Jin, Jun Zhao, Bo Xu_

- :fontawesome-solid-user-group: **Participant:** [cas.nlpr](./participants.md#cas.nlpr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.novelty.robust.pdf](http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.novelty.robust.pdf)
- :material-file-search: **Runs:** [NLPR03n1w1](./runs.md#nlpr03n1w1) | [NLPR03n1f1](./runs.md#nlpr03n1f1) | [NLPR03n1f2](./runs.md#nlpr03n1f2) | [NLPR03n1w2](./runs.md#nlpr03n1w2) | [NLPR03n1w3](./runs.md#nlpr03n1w3) | [NLPR03n2d1](./runs.md#nlpr03n2d1) | [NLPR03n2s1](./runs.md#nlpr03n2s1) | [NLPR03n2d2](./runs.md#nlpr03n2d2) | [NLPR03n2d3](./runs.md#nlpr03n2d3) | [NLPR03n2s2](./runs.md#nlpr03n2s2) | [NLPR03n3d1](./runs.md#nlpr03n3d1) | [NLPR03n3s1](./runs.md#nlpr03n3s1) | [NLPR03n3d3](./runs.md#nlpr03n3d3) | [NLPR03n3d2](./runs.md#nlpr03n3d2) | [NLPR03n3s2](./runs.md#nlpr03n3s2) | [NLPR03n4d1](./runs.md#nlpr03n4d1) | [NLPR03n4d2](./runs.md#nlpr03n4d2) | [NLPR03n4s1](./runs.md#nlpr03n4s1) | [NLPR03n4s2](./runs.md#nlpr03n4s2) | [NLPR03n4s3](./runs.md#nlpr03n4s3)

??? abstract "Abstract"
	
	It is the first time that the Chinese Information Processing group of NLPR participates in TREC. Our goal in this year is to test our IR system and get some experience about the TREC evaluation. So, we select two retrieval tasks: Novelty Track and Robust Track. We build a new IR system based on two key technologies: Window-based weighting method and Semantic Tree Model for query expansion. In this paper, the IR system and some new technologies are described first, and then some detail work and results in Novelty and Robust Track are listed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JinZX03.bib) "
	```
	@inproceedings{DBLP:conf/trec/JinZX03,
		author = {Qianli Jin and Jun Zhao and Bo Xu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{NLPR} at {TREC} 2003: Novelty and Robust},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {126--137},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.novelty.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JinZX03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMBC at TREC 12

_Srikanth Kallurkar, Yongmei Shi, R. Scott Cost, Charles K. Nicholas, Akshay Java, Christopher James, Sowjanya Rajavaram, Vishal Shanbhag, Sachin Bhatkar, Drew Ogle_

- :fontawesome-solid-user-group: **Participant:** [umarylandbc.kallurkar](./participants.md#umarylandbc.kallurkar)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/umbc.web.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/umbc.web.novelty.pdf)
- :material-file-search: **Runs:** [umbcrun1](./runs.md#umbcrun1) | [umbcrun2](./runs.md#umbcrun2) | [umbcrun3](./runs.md#umbcrun3) | [umbcnew2](./runs.md#umbcnew2) | [umbcnew3](./runs.md#umbcnew3) | [umbcnew1](./runs.md#umbcnew1)

??? abstract "Abstract"
	
	We present the results of UMBC's participation in the Web and Novelty tracks. We explored various heuristics-based link analysis approaches to the Topic Distillation task. For the novelty task we tried several methods for exploiting semantic information of sentences based on the SVD technique. We used SVD to expand the query and to filter redundant sentences. We also used a clustering algorithm that is also based on SVD.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KallurkarSCNJJRSBO03.bib) "
	```
	@inproceedings{DBLP:conf/trec/KallurkarSCNJJRSBO03,
		author = {Srikanth Kallurkar and Yongmei Shi and R. Scott Cost and Charles K. Nicholas and Akshay Java and Christopher James and Sowjanya Rajavaram and Vishal Shanbhag and Sachin Bhatkar and Drew Ogle},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UMBC} at {TREC} 12},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {699--706},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/umbc.web.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KallurkarSCNJJRSBO03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Use of Metadata for Question Answering and Novelty Tasks

_Kenneth C. Litkowski_

- :fontawesome-solid-user-group: **Participant:** [clresearch](./participants.md#clresearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/clresearch.qa.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/clresearch.qa.novelty.pdf)
- :material-file-search: **Runs:** [clr03n1t](./runs.md#clr03n1t) | [clr03n1n3](./runs.md#clr03n1n3) | [clr03n1n2](./runs.md#clr03n1n2) | [clr03n1d](./runs.md#clr03n1d) | [clr03n2](./runs.md#clr03n2) | [clr03n3f01](./runs.md#clr03n3f01) | [clr03n3f02](./runs.md#clr03n3f02) | [clr03n3f03](./runs.md#clr03n3f03) | [clr03n3f05](./runs.md#clr03n3f05) | [clr03n4](./runs.md#clr03n4) | [clr03n3f04](./runs.md#clr03n3f04)

??? abstract "Abstract"
	
	CL Research's question-answering system for TREC 2003 was modified away from reliance on database technology to the core underlying technology of using massive XML-tagging for processing both questions and documents. This core technology was then extended to participate in the novelty task. This technology provides many opportuinities for experimenting with various approaches to question answering and novelty determination. For the QA track, we submitted one run and our overall main task score was 0.075, with scores of 0.070 for factoid questions, 0.000 for list questions, and 0.160 for definition questions. For the passage task, we submitted two runs, our better score was 0.119 for the factoid questions. These scores were all considerably below the medians for these tasks. We have implemented further routines since our official submission, improving our scores to 0.18 and 0.23 for the exact answer and passages tasks, respectively. For the Novelty track, we submitted four runs for task 1, one run for task 2, five runs for task 3, and one run for task 4; our submissions for tasks 2 and 4 were identical. For task 1, our best run received an F-score of 0.483 for relevant sentences and 0.410 for new sentences. For task 2, our F-score was 0.788 for new sentences. For task 3, our best F-score was 0.558 for relevant sentences and 0.419 for new sentences. For task 4, our F-score was 0.655 for new sentences. On average, our F- scores were somewhat above the medians on all tasks. We describe our system and examine our results from the perspective of exploiting the metadata in the XML tags.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Litkowski03.bib) "
	```
	@inproceedings{DBLP:conf/trec/Litkowski03,
		author = {Kenneth C. Litkowski},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Use of Metadata for Question Answering and Novelty Tasks},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {161--176},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/clresearch.qa.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Litkowski03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Meiji University Web and Novelty Track Experiments at TREC 2003

_Ryosuke Ohgaya, Akiyoshi Shimmura, Tomohiro Takagi, Akiko N. Aizawa_

- :fontawesome-solid-user-group: **Participant:** [meijiu.takagi](./participants.md#meijiu.takagi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/meijiu.web.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/meijiu.web.novelty.pdf)
- :material-file-search: **Runs:** [MeijiHilF11](./runs.md#meijihilf11) | [MeijiHilF12](./runs.md#meijihilf12) | [MeijiHilF13](./runs.md#meijihilf13) | [MeijiHilF14](./runs.md#meijihilf14) | [MeijiHilF15](./runs.md#meijihilf15) | [MeijiHilF21](./runs.md#meijihilf21) | [MeijiHilF22](./runs.md#meijihilf22) | [MeijiHilF23](./runs.md#meijihilf23) | [MeijiHilF24](./runs.md#meijihilf24) | [MeijiHilF31](./runs.md#meijihilf31) | [MeijiHilF32](./runs.md#meijihilf32) | [MeijiHilF33](./runs.md#meijihilf33) | [MeijiHilF34](./runs.md#meijihilf34) | [MeijiHilF41](./runs.md#meijihilf41) | [MeijiHilF42](./runs.md#meijihilf42) | [MeijiHilF43](./runs.md#meijihilf43) | [MeijiHilF44](./runs.md#meijihilf44)

??? abstract "Abstract"
	
	This year we participated in TREC for the first time. We submitted runs for Novelty track and the topic distillation task of Web track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OhgayaSTA03.bib) "
	```
	@inproceedings{DBLP:conf/trec/OhgayaSTA03,
		author = {Ryosuke Ohgaya and Akiyoshi Shimmura and Tomohiro Takagi and Akiko N. Aizawa},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Meiji University Web and Novelty Track Experiments at {TREC} 2003},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {399--407},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/meijiu.web.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OhgayaSTA03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Michigan at TREC 2003

_Jahna Otterbacher, Hong Qi, Ali Hakim, Dragomir R. Radev_

- :fontawesome-solid-user-group: **Participant:** [umich.radev](./participants.md#umich.radev)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/umich.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/umich.novelty.pdf)
- :material-file-search: **Runs:** [umich1](./runs.md#umich1) | [umich5](./runs.md#umich5) | [umich4](./runs.md#umich4) | [umich3](./runs.md#umich3) | [umich2](./runs.md#umich2) | [umich23](./runs.md#umich23) | [umich22](./runs.md#umich22) | [umich21](./runs.md#umich21) | [umich24](./runs.md#umich24) | [umich25](./runs.md#umich25) | [umich32](./runs.md#umich32) | [umich31](./runs.md#umich31) | [umich33](./runs.md#umich33) | [umich34](./runs.md#umich34) | [umich35](./runs.md#umich35) | [umich41](./runs.md#umich41) | [umich43](./runs.md#umich43) | [umich42](./runs.md#umich42) | [umich45](./runs.md#umich45) | [umich44](./runs.md#umich44)

??? abstract "Abstract"
	
	This year the University of Michigan team participated in all four tasks of the Novelty track. Our basic approach for all the tasks involved using our multi-document summarizer, MEAD |1, as well as Maxent 2.1.0 software for training maximum entropy classifiers!. We submitted five runs for each of the four novelty tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OtterbacherQHR03.bib) "
	```
	@inproceedings{DBLP:conf/trec/OtterbacherQHR03,
		author = {Jahna Otterbacher and Hong Qi and Ali Hakim and Dragomir R. Radev},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Michigan at {TREC} 2003},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {732--738},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/umich.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OtterbacherQHR03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Generic Text Summarization Using Wordnet for Novelty and Hard

_Ganesh Ramakrishnan, Kedar Bellare, Chirag Shah, Deepa Paranjpe_

- :fontawesome-solid-user-group: **Participant:** [iitb.ramakrishnan](./participants.md#iitb.ramakrishnan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/iit.novelty.hard2.pdf](http://trec.nist.gov/pubs/trec12/papers/iit.novelty.hard2.pdf)
- :material-file-search: **Runs:** [IITBN1](./runs.md#iitbn1)

??? abstract "Abstract"
	
	This paper presents a Random Walk approach to text summarization using the Wordnet for text representation. For the HARD track, the specified corpus is indexed using a standard indexing engine - lucene and the initial passage set is retrieved by querying the index. The collection of passages is considered to be a document. In Novelty, the documents are as directly supplied by NIST. In either case, the document is used to extract a 'relevant' sub-graph from the wordnet graph. Weights are assigned to each node of this sub-graph using a strategy similar to the Google Page-ranking algorithm. A matrix of sentences against the nodes of the sub-graph is created and principal component analysis is performed to extract the sentences for the summary. Our approach is not specific to any particular genre of documents, such as news articles. We use the semantics in the document rather than using the more common statistical measures like term frequency and inverse-document frequency.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RamakrishnanBSP03.bib) "
	```
	@inproceedings{DBLP:conf/trec/RamakrishnanBSP03,
		author = {Ganesh Ramakrishnan and Kedar Bellare and Chirag Shah and Deepa Paranjpe},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Generic Text Summarization Using Wordnet for Novelty and Hard},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {303--304},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/iit.novelty.hard2.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RamakrishnanBSP03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2003 Novelty and Web Track at ICT

_Jian Sun, Zhe Yang, Wenfeng Pan, Huaping Zhang, Bin Wang, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [cas-ict.bin](./participants.md#cas-ict.bin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.novelty.web.pdf](http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.novelty.web.pdf)
- :material-file-search: **Runs:** [ICT03NOV1BSL](./runs.md#ict03nov1bsl) | [ICT03NOV1SQR](./runs.md#ict03nov1sqr) | [ICT03NOV1XTD](./runs.md#ict03nov1xtd) | [ICT03NOV1DTH](./runs.md#ict03nov1dth) | [ICT03NOV1NAR](./runs.md#ict03nov1nar) | [ICT03NOV2SQR](./runs.md#ict03nov2sqr) | [ICT03NOV2CUR](./runs.md#ict03nov2cur) | [ICT03NOV2PNK](./runs.md#ict03nov2pnk) | [ICT03NOV2LPP](./runs.md#ict03nov2lpp) | [ICT03NOV2LPA](./runs.md#ict03nov2lpa) | [ICT03NOV3KNN](./runs.md#ict03nov3knn) | [ICT03NOV3IKK](./runs.md#ict03nov3ikk) | [ICT03NOV3KNS](./runs.md#ict03nov3kns) | [ICT03NOV3WND](./runs.md#ict03nov3wnd) | [ICT03NOV3WN3](./runs.md#ict03nov3wn3) | [ICT03NOV4SQR](./runs.md#ict03nov4sqr) | [ICT03NOV4WNW](./runs.md#ict03nov4wnw) | [ICT03NOV4OTP](./runs.md#ict03nov4otp) | [ICT03NOV4ALL](./runs.md#ict03nov4all) | [ICT03NOV4LFF](./runs.md#ict03nov4lff)

??? abstract "Abstract"
	
	In this paper, we will present our approaches and experiments on the following two tracks of TREC-2003: Novelty track and Web track. The novelty track can be treated as a binary classification problem: relevant vs. irrelevant sentences, or new vs. non-new. In this way, we applied variants of techniques that have been employed for text categorization. To retrieve the relevant sentences, we compute the similarity between the topic and sentences using vector space model (VSM). In addition, we tried several techniques in an attempt to improve the performance: using narrative field and adopting dynamic threshold for different documents. We also have implemented the KNN algorithm and Winnow algorithm for classifying the sentences into relevant and irrelevant in the novelty task 3. To detect the new sentences, we used Maximum Marginal Relevance (MMR) measure, Winnow algorithm and so on. In addition, we attempted to detect novelty by computing semantic distance between sentences using WordNet. For the Web track, we improved the basic SMART system, and the Lnu-Ltu weighting method was introduced into the system. The improved system has been proved to be effective in last year's task. In addition, we implemented a simple retrieval system using the probability model that is adopted by Okapi. The structure of the paper is as follows: The section 2 reports the approaches and experiments in novelty track. The section 3 describes the experiments in web track. Finally, in section 4, we conclude by summarizing our experiments and presenting the future work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SunYPZWC03.bib) "
	```
	@inproceedings{DBLP:conf/trec/SunYPZWC03,
		author = {Jian Sun and Zhe Yang and Wenfeng Pan and Huaping Zhang and Bin Wang and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2003 Novelty and Web Track at {ICT}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {138--146},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.novelty.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SunYPZWC03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Approach of Information Retrieval with Reference Corpus to Novelty  Detection

_Ming-Feng Tsai, Ming-Hung Hsu, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu.chen](./participants.md#ntu.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ntu.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/ntu.novelty.pdf)
- :material-file-search: **Runs:** [NTU11](./runs.md#ntu11) | [NTU13](./runs.md#ntu13) | [NTU15](./runs.md#ntu15) | [NTU14](./runs.md#ntu14) | [NTU12](./runs.md#ntu12) | [NTU21](./runs.md#ntu21) | [NTU22](./runs.md#ntu22) | [NTU24](./runs.md#ntu24) | [NTU23](./runs.md#ntu23) | [NTU25](./runs.md#ntu25) | [NTU31](./runs.md#ntu31) | [NTU32](./runs.md#ntu32) | [NTU33](./runs.md#ntu33) | [NTU34](./runs.md#ntu34) | [NTU35](./runs.md#ntu35) | [NTU42](./runs.md#ntu42) | [NTU44](./runs.md#ntu44) | [NTU43](./runs.md#ntu43) | [NTU41](./runs.md#ntu41) | [NTU45](./runs.md#ntu45)

??? abstract "Abstract"
	
	According to the results of TREC 2002, we realized the major challenge issue of recognizing relevant sentences is a lack of information used in similarity computation among sentences. In TREC 2003, NTU attempts to find relevant and novel information based on variants of employing information retrieval (IR) system. We call this methodology IR with reference corpus, which can also be considered an information expansion of sentences. A sentence is considered as a query of a reference corpus, and similarity between sentences is measured in terms of the weighting vectors of document lists ranked by IR systems. Basically, we looked for relevant sentences by comparing their results on a certain information retrieval system. Two sentences are regarded as similar if they are related to the similar document lists returned by IR system. In novelty parts, similar analysis is used to compare each relevant sentence with all those that preceded it to find out novelty. An effectively dynamic threshold setting which is based on what percentage of relevant sentences is within a relevant document is presented. In this paper, we paid attention to three points: first, how to use the results of IR system to compare the similarity between sentences; second, how to filter out the redundant sentences; third, how to determine appropriate relevance and novelty threshold.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TsaiHC03.bib) "
	```
	@inproceedings{DBLP:conf/trec/TsaiHC03,
		author = {Ming{-}Feng Tsai and Ming{-}Hung Hsu and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Approach of Information Retrieval with Reference Corpus to Novelty Detection},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {474--479},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/ntu.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TsaiHC03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2003: Novelty, Robust and Web

_Min Zhang, Chuan Lin, Yiqun Liu, Leo Zhao, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [tsinghuau.ma](./participants.md#tsinghuau.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/tsinghuau.novelty.robust.web.pdf](http://trec.nist.gov/pubs/trec12/papers/tsinghuau.novelty.robust.web.pdf)
- :material-file-search: **Runs:** [THUIRnv0311](./runs.md#thuirnv0311) | [THUIRnv0312](./runs.md#thuirnv0312) | [THUIRnv0313](./runs.md#thuirnv0313) | [THUIRnv0314](./runs.md#thuirnv0314) | [THUIRnv0315](./runs.md#thuirnv0315) | [THUIRnv0322](./runs.md#thuirnv0322) | [THUIRnv0332](./runs.md#thuirnv0332) | [THUIRnv0331](./runs.md#thuirnv0331) | [THUIRnv0334](./runs.md#thuirnv0334) | [THUIRnv0333](./runs.md#thuirnv0333) | [THUIRnv0321](./runs.md#thuirnv0321) | [THUIRnv0323](./runs.md#thuirnv0323) | [THUIRnv0342](./runs.md#thuirnv0342) | [THUIRnv0341](./runs.md#thuirnv0341) | [THUIRnv0343](./runs.md#thuirnv0343) | [THUIRnv0344](./runs.md#thuirnv0344) | [THUIRnv0345](./runs.md#thuirnv0345)

??? abstract "Abstract"
	
	This is the second time that Tsinghua University Information Retrieval Group (THUIR) participates in TREC. In this year, we took part in four tracks: novelty, robust, web and HARD, describing in following sections, respectively. A new IR system named TMiner has been built on which all experiments have been performed. In the system, Primary Feature Model (PFM)[1] has been proposed and combined with BM2500 term weighting [2] , which led to encouraging results. Word-pair searching has also been performed and improves system precision. Both approaches are described in robust experiments (section 2), and they were also used in web track experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangLLZM03.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangLLZM03,
		author = {Min Zhang and Chuan Lin and Yiqun Liu and Leo Zhao and Shaoping Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2003: Novelty, Robust and Web},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {556--567},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/tsinghuau.novelty.robust.web.pdf},
		timestamp = {Wed, 16 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhangLLZM03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

