# Proceedings 2009 

## Relevance Feedback 

#### FUB at TREC 2009 Relevance Feedback Track: Diversifying Feedback  Documents (Extended Abstract)

_Andrea Bernardini, Claudio Carpineto, Edgardo Ambrosi_

- :fontawesome-solid-user-group: **Participant:** [FUB](./relfdbk/participants.md#fub)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/fub.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/fub.RF.pdf)
- :material-file-search: **Runs:** [fub.1](./relfdbk/runs.md#fub.1) | [FUB9RF.fub.1](./relfdbk/runs.md#fub9rf.fub.1) | [FUB9RF.CMU.1](./relfdbk/runs.md#fub9rf.cmu.1) | [FUB9RF.QUT.1](./relfdbk/runs.md#fub9rf.qut.1) | [FUB9RF.twen.2](./relfdbk/runs.md#fub9rf.twen.2) | [FUB9RF.ilps.2](./relfdbk/runs.md#fub9rf.ilps.2) | [FUB9RF.PRIS.1](./relfdbk/runs.md#fub9rf.pris.1) | [FUB9RF.UMas.1](./relfdbk/runs.md#fub9rf.umas.1) | [FUB9RF.base](./relfdbk/runs.md#fub9rf.base)

??? abstract "Abstract"
	
	The focus of our participation was optimal selection and use of diverse feedback documents. Assuming that the query has a topical structure and that the user is interested only in some query topics and assuming also that only a small amount of feedback information will be made available, the goal was to select topic representatives to be used as feedback documents and then exploit the feedback information to bias the set of results towards the topics of interest. Our method consists of the following steps. The selection of topic representatives was performed by running a first-pass retrieval on the original query and extracting the most novel and relevant documents from the obtained results. Such documents were returned for manual evaluation and the provided feedback was given as an input to an improved version of the relevance feedback system that we developed at TREC 2008 Relevance Feedback track. As this system was designed for explicitly dealing with both positive and negative relevance feedback, we reckoned that in principle it would be able to use the diverse topic representatives to filter out the highly-ranked documents belonging to the unwanted topics in an effective manner. Unfortunately, due to resource and time limitations, we were not able to fully implement and test the method outlined above. We had to make a number of approximations and simplifications that did not allow us to evaluate its true potential for improving relevance feedback. Likewise, we could not test our main hypothesis that this method is suitable for dealing with multi-topic queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BernardiniCA09.bib) "
	```
	@inproceedings{DBLP:conf/trec/BernardiniCA09,
		author = {Andrea Bernardini and Claudio Carpineto and Edgardo Ambrosi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FUB} at {TREC} 2009 Relevance Feedback Track: Diversifying Feedback Documents (Extended Abstract)},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/fub.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BernardiniCA09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Padua at TREC 2009: Relevance Feedback Track

_Emanuele Di Buccio, Massimo Melucci_

- :fontawesome-solid-user-group: **Participant:** [UPD](./relfdbk/participants.md#upd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/upadua.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/upadua.RF.pdf)
- :material-file-search: **Runs:** [UPD.1](./relfdbk/runs.md#upd.1) | [UPD9RF.base](./relfdbk/runs.md#upd9rf.base) | [UPD9RF.CMU.1](./relfdbk/runs.md#upd9rf.cmu.1) | [UPD9RF.PRIS.1](./relfdbk/runs.md#upd9rf.pris.1) | [UPD9RF.QUT.1](./relfdbk/runs.md#upd9rf.qut.1) | [UPD9RF.UMas.1](./relfdbk/runs.md#upd9rf.umas.1) | [UPD9RF.UPD.1](./relfdbk/runs.md#upd9rf.upd.1) | [UPD9RF.hit2.1](./relfdbk/runs.md#upd9rf.hit2.1) | [UPD9RF.ilps.2](./relfdbk/runs.md#upd9rf.ilps.2)

??? abstract "Abstract"
	
	In the Relevance Feedback (RF) task the user is directly involved in the search process: given an initial set of results, he specifies if they are relevant or not to the achievement of his information goal. In the TREC 2009 RF track the first five documents retrieved by the baseline systems were judged by the assessors and then used as evidence for the RF algorithms to be tested. The specific algorithm we tested is mainly based on a geometric framework which allows the latent semantic associations of terms in the feedback documents to be modeled as a vector subspace; the documents of the collection represented as vectors of TF·IDF weights were re-ranked according to their distance from the subspace. The adopted geometric framework was used in past works as a basis for Implicit Relevance Feedback (IRF) and Pseudo Relevance Feedback (PRF) algorithms; the participation to the RF track allows us to make some preliminary investigations on the effectiveness of the adopted framework when it is exploited to support explicit RF on much larger test collections, thus complementing the work carried out for the other RF strategies.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuccioM09.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuccioM09,
		author = {Emanuele Di Buccio and Massimo Melucci},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Padua at {TREC} 2009: Relevance Feedback Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/upadua.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuccioM09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Minimal Test Collections for Relevance Feedback

_Ben Carterette, Praveen Chandar, Aparna Kailasam, Divya Muppaneni, Sree Lekha Thota_

- :fontawesome-solid-user-group: **Participant:** [UDel](./relfdbk/participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.RF.pdf)
- :material-file-search: **Runs:** [udel.1](./relfdbk/runs.md#udel.1) | [udel.2](./relfdbk/runs.md#udel.2) | [udel2.SIEL.1](./relfdbk/runs.md#udel2.siel.1) | [udel2.Sab.1](./relfdbk/runs.md#udel2.sab.1) | [udel2.UCSC.1](./relfdbk/runs.md#udel2.ucsc.1) | [udel2.WatS.1](./relfdbk/runs.md#udel2.wats.1) | [udel2.fub.1](./relfdbk/runs.md#udel2.fub.1) | [udel2.twen.1](./relfdbk/runs.md#udel2.twen.1) | [udel2.udel.1](./relfdbk/runs.md#udel2.udel.1) | [udel2.udel.2](./relfdbk/runs.md#udel2.udel.2) | [udel2.base](./relfdbk/runs.md#udel2.base)

??? abstract "Abstract"
	
	The Information Retrieval Lab at the University of Delaware participated in the Relevance Feedback track at TREC 2009. We used only the Category B subset of the ClueWeb collection; our preprocessing and indexing steps are described in our paper on ad hoc and diversity runs [10]. The second year of the Relevance Feedback track focused on selection of documents for feedback. Our hypothesis is that documents that are good at distinguishing systems in terms of their effectiveness by mean average precision will also be good documents for relevance feedback. Thus we have applied the document selection algorithm MTC (Minimal Test Collections) developed by Carterette et al. [6, 4, 9, 5] that is used in the Million Query Track [2, 1, 8] for selecting documents to be judged to find the right ranking of systems. Our approach can therefore be described as “MTC for Relevance Feedback”.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CarteretteCKMT09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CarteretteCKMT09,
		author = {Ben Carterette and Praveen Chandar and Aparna Kailasam and Divya Muppaneni and Sree Lekha Thota},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Minimal Test Collections for Relevance Feedback},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CarteretteCKMT09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass Amherst and UT Austin @ the TREC 2009 Relevance Feedback  Track

_Marc-Allen Cartright, Jangwon Seo, Matthew Lease_

- :fontawesome-solid-user-group: **Participant:** [UMass](./relfdbk/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/umass-amhearst.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/umass-amhearst.RF.pdf)
- :material-file-search: **Runs:** [UMas.1](./relfdbk/runs.md#umas.1) | [UMas.2](./relfdbk/runs.md#umas.2) | [UMa9RF.base](./relfdbk/runs.md#uma9rf.base) | [UMa9RF.PRIS.1](./relfdbk/runs.md#uma9rf.pris.1) | [UMa9RF.UCSC.2](./relfdbk/runs.md#uma9rf.ucsc.2) | [UMa9RF.UMas.1](./relfdbk/runs.md#uma9rf.umas.1) | [UMa9RF.UMas.2](./relfdbk/runs.md#uma9rf.umas.2) | [UMa9RF.YUIR.2](./relfdbk/runs.md#uma9rf.yuir.2) | [UMa9RF.ilps.1](./relfdbk/runs.md#uma9rf.ilps.1) | [UMa9RF.ugTr.1](./relfdbk/runs.md#uma9rf.ugtr.1)

??? abstract "Abstract"
	
	We present a new supervised method for estimating term-based retrieval models and apply it to weight expansion terms from relevance feedback. While previous work on supervised feedback [Cao et al., 2008] demonstrated significantly improved retrieval accuracy over standard unsupervised approaches [Lavrenko and Croft, 2001, Zhai and Lafferty, 2001], feedback terms were assumed to be independent in order to reduce training time. In contrast, we adapt the AdaRank learning algorithm [Xu and Li, 2007] to simultaneously estimate parameterization of all feedback terms. While not evaluated here, the method can be more generally applied for joint estimation of both query and feedback terms. To apply our method to a large web collection, we also investigate use of sampling to reduce feature extraction time while maintaining robust learning.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CartrightSL09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CartrightSL09,
		author = {Marc{-}Allen Cartright and Jangwon Seo and Matthew Lease},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass Amherst and {UT} Austin @ the {TREC} 2009 Relevance Feedback Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/umass-amhearst.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CartrightSL09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Machine Learning for Information Retrieval: TREC 2009 Web, Relevance  Feedback and Legal Tracks

_Gordon V. Cormack, Mona Mojdeh_

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./relfdbk/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf](http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf)
- :material-file-search: **Runs:** [WAT2.base](./relfdbk/runs.md#wat2.base) | [WAT2.CMIC.2](./relfdbk/runs.md#wat2.cmic.2) | [WAT2.MSRC.2](./relfdbk/runs.md#wat2.msrc.2) | [WAT2.UCSC.1](./relfdbk/runs.md#wat2.ucsc.1) | [WAT2.UPD.1](./relfdbk/runs.md#wat2.upd.1) | [WAT2.WatS.2](./relfdbk/runs.md#wat2.wats.2) | [WAT2.YUIR.1](./relfdbk/runs.md#wat2.yuir.1) | [WAT2.hit2.2](./relfdbk/runs.md#wat2.hit2.2) | [WAT2.udel.1](./relfdbk/runs.md#wat2.udel.1)

??? abstract "Abstract"
	
	For the TREC 2009, we exhaustively classified every document in each corpus, using machine learning methods that had previously been shown to work well for email spam [9, 3]. We treated each document as a sequence of bytes, with no tokenization or parsing of tags or meta-information. This approach was used exclusively for the adhoc web, diversity and relevance feedback tasks, as well as to the batch legal task: the ClueWeb09 and Tobacco collections were processed end-to-end and never indexed. We did the interactive legal task in two phases: first, we used interactive search and judging to find a large and diverse set of training examples; then we used active learning process, similar to what we used for the other tasks, to find find more relevant documents. Finally, we fitted a censored (i.e. truncated) mixed normal distribution to estimate recall and the cutoff to optimize F1, the principal effectiveness measure.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackM09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackM09,
		author = {Gordon V. Cormack and Mona Mojdeh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Machine Learning for Information Retrieval: {TREC} 2009 Web, Relevance Feedback and Legal Tracks},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackM09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Research at TREC 2009: Web and Relevance Feedback Track

_Nick Craswell, Dennis Fetterly, Marc Najork, Stephen Robertson, Emine Yilmaz_

- :fontawesome-solid-user-group: **Participant:** [msrc](./relfdbk/participants.md#msrc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/microsoft.WEB.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/microsoft.WEB.RF.pdf)
- :material-file-search: **Runs:** [MSRC.2](./relfdbk/runs.md#msrc.2) | [MSRC.1](./relfdbk/runs.md#msrc.1) | [MSRC.CMU.1](./relfdbk/runs.md#msrc.cmu.1)

??? abstract "Abstract"
	
	We took part in the Web and Relevance Feedback tracks, using the ClueWeb09 corpus. To process the corpus, we developed a parallel processing pipeline which avoids the generation of an inverted file. We describe the components of the parallel architecture and the pipeline and how we ran the TREC experiments, and we present effectiveness results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellFNRY09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CraswellFNRY09,
		author = {Nick Craswell and Dennis Fetterly and Marc Najork and Stephen Robertson and Emine Yilmaz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Research at {TREC} 2009: Web and Relevance Feedback Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/microsoft.WEB.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CraswellFNRY09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CMIC@TREC 2009: Relevance Feedback Track

_Kareem Darwish, Ahmed El-Deeb_

- :fontawesome-solid-user-group: **Participant:** [CMIC](./relfdbk/participants.md#cmic)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/cmic.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/cmic.RF.pdf)
- :material-file-search: **Runs:** [CMIC.1](./relfdbk/runs.md#cmic.1) | [CMIC.2](./relfdbk/runs.md#cmic.2) | [CMIC.base](./relfdbk/runs.md#cmic.base) | [CMIC.CMIC.1](./relfdbk/runs.md#cmic.cmic.1) | [CMIC.CMIC.2](./relfdbk/runs.md#cmic.cmic.2) | [CMIC.MSRC.1](./relfdbk/runs.md#cmic.msrc.1) | [CMIC.UMas.2](./relfdbk/runs.md#cmic.umas.2) | [CMIC.ilps.1](./relfdbk/runs.md#cmic.ilps.1) | [CMIC.udel.1](./relfdbk/runs.md#cmic.udel.1) | [CMIC.udel.2](./relfdbk/runs.md#cmic.udel.2) | [CMIC.ugTr.2](./relfdbk/runs.md#cmic.ugtr.2)

??? abstract "Abstract"
	
	This paper describes CMIC's submissions to the TREC'09 relevance feedback track. In the phase 1 runs we submitted, we experimented with two different techniques to produce 5 documents to be judged by the user in the initial feedback step, namely using knowledge bases and clustering. Both techniques attempt to topically diversify these 5 documents as much as possible in an effort to maximize the probability that they contain at least 1 relevant document. The basic premise is that if a query has n diverse interpretations, then diversifying results and picking the top 5 most likely interpretations would maximize the probability that a user would be interested in at least one interpretation. In phase 2 runs, which involved the use of the feedback attained from phase 1 judgments, we attempted to use positive and negative judgments in weighing the terms to be used for subsequent feedback. 
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DarwishE09.bib) "
	```
	@inproceedings{DBLP:conf/trec/DarwishE09,
		author = {Kareem Darwish and Ahmed El{-}Deeb},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {CMIC@TREC 2009: Relevance Feedback Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/cmic.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DarwishE09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Pairwise Document Classification for Relevance Feedback

_Jonathan L. Elsas, Pinar Donmez, Jamie Callan, Jaime G. Carbonell_

- :fontawesome-solid-user-group: **Participant:** [CMU_LIRA](./relfdbk/participants.md#cmu_lira)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/cmu.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/cmu.RF.pdf)
- :material-file-search: **Runs:** [CMU.1](./relfdbk/runs.md#cmu.1) | [CMU.base](./relfdbk/runs.md#cmu.base) | [CMU.CMIC.1](./relfdbk/runs.md#cmu.cmic.1) | [CMU.CMIC.2](./relfdbk/runs.md#cmu.cmic.2) | [CMU.CMU.1](./relfdbk/runs.md#cmu.cmu.1) | [CMU.FDU.1](./relfdbk/runs.md#cmu.fdu.1) | [CMU.MSRC.1](./relfdbk/runs.md#cmu.msrc.1) | [CMU.UMas.2](./relfdbk/runs.md#cmu.umas.2) | [CMU.YUIR.2](./relfdbk/runs.md#cmu.yuir.2)

??? abstract "Abstract"
	
	In this paper we present Carnegie Mellon University's submission to the TREC 2009 Relevance Feedback Track. In this submission we take a classification approach on document pairs to using relevance feedback information. We explore using textual and non-textual document-pair features to classify unjudged documents as relevant or non-relevant, and use this prediction to re-rank a baseline document retrieval. These features include co-citation measures, URL similarities, as well as features often used in machine learning systems for document ranking such as the difference in scores assigned by the baseline retrieval system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ElsasDCC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ElsasDCC09,
		author = {Jonathan L. Elsas and Pinar Donmez and Jamie Callan and Jaime G. Carbonell},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Pairwise Document Classification for Relevance Feedback},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/cmu.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ElsasDCC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Twente @ TREC 2009: Indexing Half a Million Web Pages

_Claudia Hauff, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [utwente](./relfdbk/participants.md#utwente)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/utwente.WEB.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/utwente.WEB.RF.pdf)
- :material-file-search: **Runs:** [twen.1](./relfdbk/runs.md#twen.1) | [twen.2](./relfdbk/runs.md#twen.2) | [twen.base](./relfdbk/runs.md#twen.base) | [twen.FDU.1](./relfdbk/runs.md#twen.fdu.1) | [twen.ilps.1](./relfdbk/runs.md#twen.ilps.1) | [twen.UCSC.2](./relfdbk/runs.md#twen.ucsc.2) | [twen.twen.1](./relfdbk/runs.md#twen.twen.1) | [twen.YUIR.2](./relfdbk/runs.md#twen.yuir.2) | [twen.ugTr.1](./relfdbk/runs.md#twen.ugtr.1) | [twen.twen.2](./relfdbk/runs.md#twen.twen.2)

??? abstract "Abstract"
	
	The University of Twente participated in three tasks of TREC 2009: the adhoc task, the diversity task and the relevance feedback task. All experiments are performed on the English part of ClueWeb09. We describe our approach to tuning our retrieval system in absence of training data in Section 3. We describe the use of categories and a query log for diversifying search results in Section 4. Section 5 describes preliminary results for the relevance feedback task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HauffH09.bib) "
	```
	@inproceedings{DBLP:conf/trec/HauffH09,
		author = {Claudia Hauff and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Twente @ {TREC} 2009: Indexing Half a Million Web Pages},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/utwente.WEB.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HauffH09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at 2009 Relevance Feedback Track: Experiments in Language Model  for Relevance Feedback

_Si Li, Xinsheng Li, Hao Zhang, Sanyuan Gao, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [buptpris___2009](./relfdbk/participants.md#buptpris___2009)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/pris.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/pris.RF.pdf)
- :material-file-search: **Runs:** [PRIS.1](./relfdbk/runs.md#pris.1) | [PRIS.base](./relfdbk/runs.md#pris.base) | [PRIS.ilps.1](./relfdbk/runs.md#pris.ilps.1) | [PRIS.PRIS.1](./relfdbk/runs.md#pris.pris.1) | [PRIS.Sab.1](./relfdbk/runs.md#pris.sab.1) | [PRIS.SIEL.1](./relfdbk/runs.md#pris.siel.1) | [PRIS.UCSC.1](./relfdbk/runs.md#pris.ucsc.1) | [PRIS.hit2.2](./relfdbk/runs.md#pris.hit2.2) | [PRIS.twen.1](./relfdbk/runs.md#pris.twen.1)

??? abstract "Abstract"
	
	This paper describes BUPT (pris) participation in Relevance Feedback Track 2009. The track has two phrases. In the first phrase, 5 documents are submitted based on the results of the k-means. In the second phrase, language model is used to relevance feedback for query expansion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiLZGCG09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiLZGCG09,
		author = {Si Li and Xinsheng Li and Hao Zhang and Sanyuan Gao and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at 2009 Relevance Feedback Track: Experiments in Language Model for Relevance Feedback},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/pris.RF.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiLZGCG09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mining Specific and General Features in Both Positive and Negative  Relevance Feedback

_Yuefeng Li, Xiaohui Tao, Abdulmohsen Algarni, Sheng-Tang Wu_

- :fontawesome-solid-user-group: **Participant:** [QUT_ED_Lab](./relfdbk/participants.md#qut_ed_lab)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/queenslandu.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/queenslandu.RF.pdf)
- :material-file-search: **Runs:** [QUT.1](./relfdbk/runs.md#qut.1) | [QUT.base](./relfdbk/runs.md#qut.base) | [QUT.CMIC.1](./relfdbk/runs.md#qut.cmic.1) | [QUT.MSRC.2](./relfdbk/runs.md#qut.msrc.2) | [QUT.QUT.1](./relfdbk/runs.md#qut.qut.1) | [QUT.SIEL.1](./relfdbk/runs.md#qut.siel.1) | [QUT.UPD.1](./relfdbk/runs.md#qut.upd.1) | [QUT.WatS.1](./relfdbk/runs.md#qut.wats.1) | [QUT.YUIR.2](./relfdbk/runs.md#qut.yuir.2) | [QUT.hit2.1](./relfdbk/runs.md#qut.hit2.1)

??? abstract "Abstract"
	
	User relevance feedback is usually utilized by Web systems to interpret user information needs and retrieve effective results for users. However, how to discover useful knowledge in user relevance feedback and how to wisely use the discovery knowledge are two critical problems. In TREC 2009, we participated in the Relevance Feedback Track and experimented a model consisting of two innovative stages: one for subject-based query expansion to extract pseudo-relevance feedback; one for relevance feature discovery to find useful patterns and terms in relevance judgements to rank documents. In this paper, the detailed description of our model is given, as well as the related discussions for the experimental results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiTAW09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiTAW09,
		author = {Yuefeng Li and Xiaohui Tao and Abdulmohsen Algarni and Sheng{-}Tang Wu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Mining Specific and General Features in Both Positive and Negative Relevance Feedback},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/queenslandu.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiTAW09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2009: Experiments with Terrier

_Richard McCreadie, Craig Macdonald, Iadh Ounis, Jie Peng, Rodrygo L. T. Santos_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./relfdbk/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf)
- :material-file-search: **Runs:** [ugTr.1](./relfdbk/runs.md#ugtr.1) | [ugTr.2](./relfdbk/runs.md#ugtr.2) | [ugTr.base](./relfdbk/runs.md#ugtr.base) | [ugTr.CMU.1](./relfdbk/runs.md#ugtr.cmu.1) | [ugTr.hit2.1](./relfdbk/runs.md#ugtr.hit2.1) | [ugTr.ilps.2](./relfdbk/runs.md#ugtr.ilps.2) | [ugTr.ugTr.1](./relfdbk/runs.md#ugtr.ugtr.1) | [ugTr.ugTr.2](./relfdbk/runs.md#ugtr.ugtr.2) | [ugTr.UMas.1](./relfdbk/runs.md#ugtr.umas.1) | [ugTr.UPD.1](./relfdbk/runs.md#ugtr.upd.1) | [ugTr.YUIR.1](./relfdbk/runs.md#ugtr.yuir.1)

??? abstract "Abstract"
	
	In TREC 2009, we extend our Voting Model for the faceted blog distillation, top stories identification, and related entity finding tasks. Moreover, we experiment with our novel xQuAD framework for search result diversification. Besides fostering our research in multiple directions, by participating in such a wide portfolio of tracks, we further develop the indexing and retrieval capabilities of our Terrier Information Retrieval platform, to effectively and efficiently cope with a new generation of large-scale test collections.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieMOPS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieMOPS09,
		author = {Richard McCreadie and Craig Macdonald and Iadh Ounis and Jie Peng and Rodrygo L. T. Santos},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2009: Experiments with Terrier},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieMOPS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Topical Diversity and Relevance Feedback

_Edgar Meij, Jiyin He, Wouter Weerkamp, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [UAms](./relfdbk/participants.md#uams)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.RF.pdf)
- :material-file-search: **Runs:** [ilps.2](./relfdbk/runs.md#ilps.2) | [ilps.1](./relfdbk/runs.md#ilps.1) | [IlpsRF.base](./relfdbk/runs.md#ilpsrf.base) | [IlpsRF.QUT.1](./relfdbk/runs.md#ilpsrf.qut.1) | [IlpsRF.Sab.1](./relfdbk/runs.md#ilpsrf.sab.1) | [IlpsRF.WatS.1](./relfdbk/runs.md#ilpsrf.wats.1) | [IlpsRF.fub.1](./relfdbk/runs.md#ilpsrf.fub.1) | [IlpsRF.ilps.1](./relfdbk/runs.md#ilpsrf.ilps.1) | [IlpsRF.ilps.2](./relfdbk/runs.md#ilpsrf.ilps.2) | [IlpsRF.twen.1](./relfdbk/runs.md#ilpsrf.twen.1) | [IlpsRF.twen.2](./relfdbk/runs.md#ilpsrf.twen.2)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdam's Intelligent Systems Lab in the relevance feedback track at TREC 2009. Our main conclusion for the relevance feedback track is that a topical diversity approach provides good feedback documents. Further, we find that our relevance feedback algorithm seems to help most when there are sufficient relevant documents available.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MeijHWR09.bib) "
	```
	@inproceedings{DBLP:conf/trec/MeijHWR09,
		author = {Edgar Meij and Jiyin He and Wouter Weerkamp and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Topical Diversity and Relevance Feedback},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MeijHWR09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments with ClueWeb09: Relevance Feedback and Web Tracks

_Mark D. Smucker, Charles L. A. Clarke, Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./relfdbk/participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.RF.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.RF.WEB.pdf)
- :material-file-search: **Runs:** [WatS.1](./relfdbk/runs.md#wats.1) | [WatS.2](./relfdbk/runs.md#wats.2) | [WatS.base](./relfdbk/runs.md#wats.base) | [WatS.SIEL.1](./relfdbk/runs.md#wats.siel.1) | [WatS.Sab.1](./relfdbk/runs.md#wats.sab.1) | [WatS.UCSC.1](./relfdbk/runs.md#wats.ucsc.1) | [WatS.WatS.1](./relfdbk/runs.md#wats.wats.1) | [WatS.WatS.2](./relfdbk/runs.md#wats.wats.2) | [WatS.fub.1](./relfdbk/runs.md#wats.fub.1) | [WatS.twen.1](./relfdbk/runs.md#wats.twen.1) | [WatS.twen.2](./relfdbk/runs.md#wats.twen.2)

??? abstract "Abstract"
	
	In this paper, we report on our TREC experiments with the ClueWeb09 document collection. We participated in the relevance feedback and web tracks. While our phase 1 relevance feedback run's performance was good, our other relevance feedback and web track submissions' performances were lacking. We suspect this performance difference is caused by the Category B document subset of the ClueWeb09 collection having a higher prior probability of relevance than the rest of the collection. Future work will involve a more detailed error analysis of our experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmuckerCC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmuckerCC09,
		author = {Mark D. Smucker and Charles L. A. Clarke and Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments with ClueWeb09: Relevance Feedback and Web Tracks},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.RF.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmuckerCC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Relevance Feedback Based on Constrained Clustering: FDU at TREC  09

_Bingqing Wang, Xuanjing Huang_

- :fontawesome-solid-user-group: **Participant:** [FDU_MEDLAB](./relfdbk/participants.md#fdu_medlab)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/fudanu.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/fudanu.RF.pdf)
- :material-file-search: **Runs:** [FDU.1](./relfdbk/runs.md#fdu.1) | [FDURFN.base](./relfdbk/runs.md#fdurfn.base) | [FDURFN.PRIS.1](./relfdbk/runs.md#fdurfn.pris.1) | [FDURFN.QUT.1](./relfdbk/runs.md#fdurfn.qut.1) | [FDURFN.UMas.1](./relfdbk/runs.md#fdurfn.umas.1) | [FDURFN.fub.1](./relfdbk/runs.md#fdurfn.fub.1) | [FDURFN.twen.2](./relfdbk/runs.md#fdurfn.twen.2) | [FDURFN.WatS.1](./relfdbk/runs.md#fdurfn.wats.1) | [FDURFN.FDU.1](./relfdbk/runs.md#fdurfn.fdu.1)

??? abstract "Abstract"
	
	We introduce our participation of the TREC Relevance Feedback(RF) TRACK in 2009. The RF09 TRACK is focused on the explicit relevant feedback, where a few relevant and irrelevant documents are available to each query. Our system is implemented under the framework of probabilistic language model. We apply the constrained clustering on the top returned documents and extract the expanded words to reform the query. We also extract the named entities from the explicit relevant documents to expand the query. The experiment was conducted on the ClueWeb09 TREC Category B, which is a new and huge test collection for the TREC TRACKs. The evaluation result shows the performance of the constrained clustering.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangH09.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangH09,
		author = {Bingqing Wang and Xuanjing Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Relevance Feedback Based on Constrained Clustering: {FDU} at {TREC} 09},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/fudanu.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangH09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2009: Relevance Feedback Track

_Zheng Ye, Xiangji Huang, Ben He, Hongfei Lin_

- :fontawesome-solid-user-group: **Participant:** [york09](./relfdbk/participants.md#york09)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/yorku.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/yorku.RF.pdf)
- :material-file-search: **Runs:** [YUIR.1](./relfdbk/runs.md#yuir.1) | [YUIR.2](./relfdbk/runs.md#yuir.2) | [YUIR.base](./relfdbk/runs.md#yuir.base) | [YUIR.YUIR.1](./relfdbk/runs.md#yuir.yuir.1) | [YUIR.ugTr.1](./relfdbk/runs.md#yuir.ugtr.1) | [YUIR.UMas.2](./relfdbk/runs.md#yuir.umas.2) | [YUIR.FDU.1](./relfdbk/runs.md#yuir.fdu.1) | [YUIR.YUIR.2](./relfdbk/runs.md#yuir.yuir.2) | [YUIR.CMIC.1](./relfdbk/runs.md#yuir.cmic.1) | [YUIR.UCSC.2](./relfdbk/runs.md#yuir.ucsc.2)

??? abstract "Abstract"
	
	We describe a series of experiments conducted in our participation in the Relevance Feedback Track. We evaluate two traditional weighting models (BM25 and DFR) for the phase 1 task, which are widely used in text retrieval domain. We also evaluate a statistics-based feedback model and our proposed feedback model for the phase 2 task. Currently, we are waiting for the overview paper to facilitate further analyses.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YeHHYL09.bib) "
	```
	@inproceedings{DBLP:conf/trec/YeHHYL09,
		author = {Zheng Ye and Xiangji Huang and Ben He and Hongfei Lin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2009: Relevance Feedback Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/yorku.RF.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YeHHYL09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCSC at Relevance Feedback Track

_Lanbo Zhang, Jadiel de Arma, Kai Yu_

- :fontawesome-solid-user-group: **Participant:** [UCSCIRKM](./relfdbk/participants.md#ucscirkm)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uc-santa.cruz.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/uc-santa.cruz.RF.pdf)
- :material-file-search: **Runs:** [UCSC.1](./relfdbk/runs.md#ucsc.1) | [UCSC.2](./relfdbk/runs.md#ucsc.2) | [UCSC.base](./relfdbk/runs.md#ucsc.base) | [UCSC.CMIC.1](./relfdbk/runs.md#ucsc.cmic.1) | [UCSC.FDU.1](./relfdbk/runs.md#ucsc.fdu.1) | [UCSC.UMas.2](./relfdbk/runs.md#ucsc.umas.2) | [UCSC.ugTr.2](./relfdbk/runs.md#ucsc.ugtr.2) | [UCSC.udel.2](./relfdbk/runs.md#ucsc.udel.2) | [UCSC.UCSC.2](./relfdbk/runs.md#ucsc.ucsc.2) | [UCSC.UCSC.1](./relfdbk/runs.md#ucsc.ucsc.1) | [UCSC.MSRC.1](./relfdbk/runs.md#ucsc.msrc.1)

??? abstract "Abstract"
	
	The relevance feedback track in TREC 2009 focuses on two sub tasks: actively selecting good documents for users to provide relevance feedback and retrieving documents based on user relevance feedback. For the first task, we tried a clustering based method and the Transductive Experimental Design (TED) method proposed by Yu et al. [5]. For clustering based method, we use the K-means algorithm to cluster the top retrieved documents and choose the most representative document of each cluster. The TED method aims to find documents that are hard-to-predict and representative of the unlabeled documents. For the second task, we did query expansion based on a relevance model learned on the relevant documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangAY09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangAY09,
		author = {Lanbo Zhang and Jadiel de Arma and Kai Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UCSC} at Relevance Feedback Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uc-santa.cruz.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangAY09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Chemical 

#### Overview of the TREC 2009 Chemical IR Track

_Mihai Lupu, Florina Piroi, Xiangji Huang, Jianhan Zhu, John Tait_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/CHEM09.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec18/papers/CHEM09.OVERVIEW.pdf)
??? abstract "Abstract"
	
	TREC 2009 was the first year of the Chemical IR Track, which focuses on evaluation of search techniques for discovery of digitally stored information on chemical patents and academic journal articles. The track included two tasks: Prior Art (PA) and Technical Survey (TS) tasks. This paper describes how we designed the two tasks and presents the official results of eight participating groups.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LupuPHZT09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LupuPHZT09,
		author = {Mihai Lupu and Florina Piroi and Xiangji Huang and Jianhan Zhu and John Tait},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2009 Chemical {IR} Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/CHEM09.OVERVIEW.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LupuPHZT09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Strategies for Effective Chemical Information Retrieval

_Suleyman Cetintas, Luo Si_

- :fontawesome-solid-user-group: **Participant:** [Purdue_Si](./chemical/participants.md#purdue_si)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/purdue.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/purdue.CHEM.pdf)
- :material-file-search: **Runs:** [purdueTS09r1](./chemical/runs.md#purduets09r1) | [purduePA09r1](./chemical/runs.md#purduepa09r1) | [purduePA09r2](./chemical/runs.md#purduepa09r2)

??? abstract "Abstract"
	
	We participated in the technology survey and prior art search subtasks of the TREC 2009 Chemical IR Track. This paper describes the methods developed for these two tasks. For the technology survey task, we propose a method that constructs highly structured queries to do retrieval on different fields of chemical patents and documents in a weighted way. The proposed method i) enriches these structured queries with synonyms of the chemicals that have been identified, and ii) uses simple entity recognition to extract information for increasing or decreasing weights of some terms and to filter out documents from the ranked list. For prior art search task; we propose an automated query generation method that uses all title words, and selects sets of terms from the claims, abstract and description fields of query patents to transform a query patent into a search query. From the selected terms, chemical entities are extracted and synonyms for the identified chemical entities are included from PubChem. Then structured queries are formed to do retrieval over different fields of documents with different weights. Furthermore a post-processing step is also proposed that i) filters out some of the retrieved documents from the ranked list because of date constraints and ii) utilizes the IPC similarities between query patent and its retrieved patents to re-rank the retrieved documents. Empirical results demonstrate the effectiveness of these methods in both tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CetintasS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CetintasS09,
		author = {Suleyman Cetintas and Luo Si},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Strategies for Effective Chemical Information Retrieval},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/purdue.CHEM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CetintasS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 2009 Experiments: Chemical IR Track

_Julien Gobeill, Douglas Teodoro, Emilie Pasche, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [BITEM](./chemical/participants.md#bitem)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/bitem.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/bitem.CHEM.pdf)
- :material-file-search: **Runs:** [BiTeM09](./chemical/runs.md#bitem09) | [BiTeM09po](./chemical/runs.md#bitem09po) | [BiTeM09qe](./chemical/runs.md#bitem09qe) | [BiTeM09qepo](./chemical/runs.md#bitem09qepo) | [BiTeM09comb](./chemical/runs.md#bitem09comb) | [BiTeM09ipc1](./chemical/runs.md#bitem09ipc1) | [BiTeM09ipc3](./chemical/runs.md#bitem09ipc3) | [BiTeM09ipc5](./chemical/runs.md#bitem09ipc5) | [BiTeM09ipc3b](./chemical/runs.md#bitem09ipc3b) | [BiTeM09PAbl](./chemical/runs.md#bitem09pabl) | [BiTeM09PAcit](./chemical/runs.md#bitem09pacit) | [BiTeM09PAcl](./chemical/runs.md#bitem09pacl) | [BiTeM09PAqe](./chemical/runs.md#bitem09paqe) | [BiTeM09PAcba](./chemical/runs.md#bitem09pacba) | [BiTeM09PAcbb](./chemical/runs.md#bitem09pacbb)

??? abstract "Abstract"
	
	The goal of the first TREC Chemical track was to retrieve documents relevant to a given patent query, within a large collection of patents in chemistry. Regarding this objective, for the Prior Art subtask, our runs performed significantly better that runs submitted by other participating teams. Baseline retrieval methods achieved relatively poor performances (Mean Average Precision = 0.067). Query expansion, driven my chemical named entity recognition resulted in some modest improvement (+2 to 3%). Filtering based on IPC codes did not result in any significant improvement. A re-ranking strategy, based on claims only improved MAP by about 3%. The most effective gain was obtained by using patent citation patterns. Somehow similar to feed-back but restricted to citations, we used patents cited in the retrieved patents in order to boost the retrieval status value of the baseline run. This strategy led to a remarkable improvement (MAP 0.18, +168 %). Nevertheless, as official topics were sampled from the collection disregarding their creation date, our strategy happened to exploit citations of patents which were patented after the topic itself. From a user perspective, such a setting is questionable. We think that future TREC-CHEM competitions should address this issue by using patents filed as recently as possible.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GobeillTPR09.bib) "
	```
	@inproceedings{DBLP:conf/trec/GobeillTPR09,
		author = {Julien Gobeill and Douglas Teodoro and Emilie Pasche and Patrick Ruch},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Report on the {TREC} 2009 Experiments: Chemical {IR} Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/bitem.CHEM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GobeillTPR09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Patent Retrieval in Chemistry Based on Semantically Tagged Named Entities

_Harsha Gurulingappa, Bernd Müller, Roman Klinger, Heinz-Theodor Mevissen, Martin Hofmann-Apitius, Juliane Fluck, Christoph M. Friedrich_

- :fontawesome-solid-user-group: **Participant:** [NERCHEM116](./chemical/participants.md#nerchem116)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/scai.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/scai.CHEM.pdf)
- :material-file-search: **Runs:** [SCAI09TSNP](./chemical/runs.md#scai09tsnp) | [SCAI09TSMAN](./chemical/runs.md#scai09tsman) | [SCAI09TSPM](./chemical/runs.md#scai09tspm) | [SCAI09PAt2a](./chemical/runs.md#scai09pat2a) | [SCAI09PAf2a](./chemical/runs.md#scai09paf2a) | [SCAI09PAt2b](./chemical/runs.md#scai09pat2b) | [SCAI09PAf2b](./chemical/runs.md#scai09paf2b) | [SCAI09PAt2c](./chemical/runs.md#scai09pat2c) | [SCAI09PAf2c](./chemical/runs.md#scai09paf2c) | [SCAI09PAt2d](./chemical/runs.md#scai09pat2d) | [SCAI09PAf2d](./chemical/runs.md#scai09paf2d) | [SCAI09PAt2e](./chemical/runs.md#scai09pat2e) | [SCAI09PAf2e](./chemical/runs.md#scai09paf2e) | [SCAI09PAt1a](./chemical/runs.md#scai09pat1a) | [SCAI09PAf1a](./chemical/runs.md#scai09paf1a) | [SCAI09PAt1b](./chemical/runs.md#scai09pat1b) | [SCAI09PAf1b](./chemical/runs.md#scai09paf1b) | [SCAI09PAt1c](./chemical/runs.md#scai09pat1c) | [SCAI09PAf1c](./chemical/runs.md#scai09paf1c) | [SCAI09PAt1d](./chemical/runs.md#scai09pat1d) | [SCAI09PAf1d](./chemical/runs.md#scai09paf1d) | [SCAI09PAt1e](./chemical/runs.md#scai09pat1e) | [SCAI09PAf1e](./chemical/runs.md#scai09paf1e) | [SCAI09PAt3a](./chemical/runs.md#scai09pat3a) | [SCAI09PAf3a](./chemical/runs.md#scai09paf3a) | [SCAI09PAt3b](./chemical/runs.md#scai09pat3b) | [SCAI09PAf3b](./chemical/runs.md#scai09paf3b) | [SCAI09PAt3c](./chemical/runs.md#scai09pat3c) | [SCAI09PAf3c](./chemical/runs.md#scai09paf3c) | [SCAI09PAt3d](./chemical/runs.md#scai09pat3d) | [SCAI09PAf3d](./chemical/runs.md#scai09paf3d) | [SCAI09PAt3e](./chemical/runs.md#scai09pat3e) | [SCAI09PAf3e](./chemical/runs.md#scai09paf3e) | [SCAI09PAt4a](./chemical/runs.md#scai09pat4a) | [SCAI09PAf4a](./chemical/runs.md#scai09paf4a) | [SCAI09PAt4c](./chemical/runs.md#scai09pat4c) | [SCAI09PAf4c](./chemical/runs.md#scai09paf4c) | [SCAI09PAt4b](./chemical/runs.md#scai09pat4b) | [SCAI09PAf4b](./chemical/runs.md#scai09paf4b)

??? abstract "Abstract"
	
	This paper reports on the work that has been conducted by Fraunhofer SCAI for Trec Chemistry (Trec-Chem) track 2009. The team of Fraunhofer SCAI participated in two tasks, namely Technology Survey and Prior Art Search. The core of the framework is an index of 1.2 million chemical patents provided as a data set by Trec. For the technology survey, three runs were submitted based on semantic dictionaries and noun phrases. For the prior art search task, several fields were introduced into the index that contained normalized noun phrases, biomedical as well as chemical entities. Altogether, 36 runs were submitted for this task that were based on automatic querying with tokens, noun phrases and entities along with different search strategies.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GurulingappaMKMHFF09.bib) "
	```
	@inproceedings{DBLP:conf/trec/GurulingappaMKMHFF09,
		author = {Harsha Gurulingappa and Bernd M{\"{u}}ller and Roman Klinger and Heinz{-}Theodor Mevissen and Martin Hofmann{-}Apitius and Juliane Fluck and Christoph M. Friedrich},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Patent Retrieval in Chemistry Based on Semantically Tagged Named Entities},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/scai.CHEM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GurulingappaMKMHFF09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2009: Chemical IR Track

_Song Jin, Zheng Ye, Hongfei Lin_

- :fontawesome-solid-user-group: **Participant:** [DUTIR](./chemical/participants.md#dutir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/dalianu.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/dalianu.CHEM.pdf)
- :material-file-search: **Runs:** [DUT09TSRun1](./chemical/runs.md#dut09tsrun1) | [DUT09TSRun2](./chemical/runs.md#dut09tsrun2) | [DUT09TSRun3](./chemical/runs.md#dut09tsrun3) | [DUT09TSRun4](./chemical/runs.md#dut09tsrun4) | [DUT09TSRun6](./chemical/runs.md#dut09tsrun6) | [DUTIR09BM25F](./chemical/runs.md#dutir09bm25f) | [DUTIRRun1](./chemical/runs.md#dutirrun1) | [DUTIRRun2](./chemical/runs.md#dutirrun2) | [DUTIRRun3](./chemical/runs.md#dutirrun3)

??? abstract "Abstract"
	
	This paper presents the DUTIR submission to TREC 2009 Chemical IR Track. This track included two tasks: Prior Art (PA) and Technical Survey (TS) tasks. We present a series of experiments on two text retrieval models, BM25 and Language Model for IR (LMIR). For Prior Art task, we focused on formulating the queries from the query patents and date filtering. Moreover, some traditional search techniques are used for Technical Survey task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JinYL09.bib) "
	```
	@inproceedings{DBLP:conf/trec/JinYL09,
		author = {Song Jin and Zheng Ye and Hongfei Lin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2009: Chemical {IR} Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/dalianu.CHEM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JinYL09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC Blog and TREC Chem: A View from the Corn Fields

_Yelena Mejova, Viet Ha-Thuc, Steven Foster, Christopher G. Harris, Robert J. Arens, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [IowaS](./chemical/participants.md#iowas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uiowa.BLOG.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/uiowa.BLOG.CHEM.pdf)
- :material-file-search: **Runs:** [UIowaS09PA1](./chemical/runs.md#uiowas09pa1) | [UIowaS09PA2](./chemical/runs.md#uiowas09pa2) | [UIowaS09PA3](./chemical/runs.md#uiowas09pa3)

??? abstract "Abstract"
	
	The University of Iowa Team, participated in the blog track and the chemistry track of TREC-2009. This is our first year participating in the blog track as well as the chemistry track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MejovaHFHAS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/MejovaHFHAS09,
		author = {Yelena Mejova and Viet Ha{-}Thuc and Steven Foster and Christopher G. Harris and Robert J. Arens and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} Blog and {TREC} Chem: {A} View from the Corn Fields},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uiowa.BLOG.CHEM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MejovaHFHAS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC Chemical IR Track 2009: A Distributed Dimensional Indexing  Model for Chemical Patent Search

_Jay Urbain, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [msoe](./chemical/participants.md#msoe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/milwaukee.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/milwaukee.CHEM.pdf)
- :material-file-search: **Runs:** [msoe09TSx1](./chemical/runs.md#msoe09tsx1) | [msoe09TSx2](./chemical/runs.md#msoe09tsx2) | [msoe09TSx3](./chemical/runs.md#msoe09tsx3) | [msoe09TSx4](./chemical/runs.md#msoe09tsx4) | [msoe09TSx5](./chemical/runs.md#msoe09tsx5) | [msoe09TSx1ta](./chemical/runs.md#msoe09tsx1ta) | [msoe09TSx2ta](./chemical/runs.md#msoe09tsx2ta) | [msoe09TSx3ta](./chemical/runs.md#msoe09tsx3ta) | [msoe09TSx4ta](./chemical/runs.md#msoe09tsx4ta) | [msoe09TSx5ta](./chemical/runs.md#msoe09tsx5ta)

??? abstract "Abstract"
	
	For the TREC-2009 Chemical IR Track, we explore development of a distributed information retrieval system based on a dimensional data model. The indexing model supports named entity identification and aggregation of term statistics at multiple levels of patent structure including individual words, sentences, claims, descriptions, abstracts, and titles. The system was deployed across 15 Amazon Web Services (AWS) Elastic Cloud Compute (EC2) instances and 15 Elastic Block Storage (EBS) database shards to support efficient indexing and query processing of the relatively large index generated from indexing each individual word (sans stop words) in the 100G+ collection of chemical patent documents. The query processing algorithm for technology survey search and prior art search uses information extraction techniques and locally aggregated term statistics to help disambiguate candidate entities and terms in context. Query processing for prior art search automatically generates a structured query based on the relative distinctiveness of individual terms and candidate entity phrases from the query patent's claims, abstract, and title sections. For both the technology survey and prior art search, we evaluated several probabilistic retrieval functions for integrating statistics of retrieved named entities with term statistics at multiple levels of document structure to identify relevant patents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/UrbainF09.bib) "
	```
	@inproceedings{DBLP:conf/trec/UrbainF09,
		author = {Jay Urbain and Ophir Frieder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} Chemical {IR} Track 2009: {A} Distributed Dimensional Indexing Model for Chemical Patent Search},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/milwaukee.CHEM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/UrbainF09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Formulating Simple Structured Queries Using Temporal and Distributional  Cues in Patents

_Le Zhao, James P. Callan_

- :fontawesome-solid-user-group: **Participant:** [CMU_LIRA](./chemical/participants.md#cmu_lira)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/cmu.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/cmu.CHEM.pdf)
- :material-file-search: **Runs:** [CMU09Chmtcd](./chemical/runs.md#cmu09chmtcd) | [CMU09Chmtcdd](./chemical/runs.md#cmu09chmtcdd)

??? abstract "Abstract"
	
	Patent prior art retrieval aims to find related publications, especially patents, which may invalidate the patent. The task exhibits its own characteristic because of the possible use of a whole patent as a query. This work focuses on the use of date fields and content fields of the query patent to formulate effective structured queries. Retrieval is performed on the collection of patents which also share the same structure as the query patent, mainly priority dates, application date, publication date and content fields. Unsurprisingly, results show that filtering using date information improves retrieval significantly. However, results also show that a careful choice of the date filter is important, given the multiple date fields existent in a patent. The actual ranking query is constructed based on word distributions of title, claims and content fields of the query patent. The overall MAP of this citation finding task is still in the lower 0.1 range. An error analysis focusing on the lower performing topics finds that the citation finding task (given publication recommend citations, which is a very similar setup as this year's prior art evaluation) can be very different from the prior art task (finding patents that invalidates the query patent). It raises the concern that just the citations included in query patents can be a biased and incomplete set of relevance judgements for the prior art task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoC09,
		author = {Le Zhao and James P. Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Formulating Simple Structured Queries Using Temporal and Distributional Cues in Patents},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/cmu.CHEM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2009: Chemical Track

_Jiashu Zhao, Xiangji Huang, Zheng Ye, Jianhan Zhu_

- :fontawesome-solid-user-group: **Participant:** [york09](./chemical/participants.md#york09)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/yorku.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/yorku.CHEM.pdf)
- :material-file-search: **Runs:** [york09ca03](./chemical/runs.md#york09ca03) | [york09ca04](./chemical/runs.md#york09ca04) | [york09ca05](./chemical/runs.md#york09ca05) | [york09ca06](./chemical/runs.md#york09ca06) | [york09ca02](./chemical/runs.md#york09ca02) | [york09ca07](./chemical/runs.md#york09ca07) | [york09ca08](./chemical/runs.md#york09ca08) | [york09caPA01](./chemical/runs.md#york09capa01) | [york09caPA03](./chemical/runs.md#york09capa03)

??? abstract "Abstract"
	
	Our chemical experiments mainly focus on addressing three major problems in two chemical information retrieval tasks, Technology Survey (TS) task and Prior Art (PA) task. The three problems are: (1) how to deal with chemical terminology synonyms? (2) how to deal with chemical terminology abbreviation? (3) how to deal with long queries in Prior Art (PA) task? In particular, we propose a query expansion algorithm for TS task and a keyword-selection algorithm for PA task. The Mean Average Precision (MAP) for our TS task run “york09ca07” using Algorithm 1 was 0.2519 and for our PA task run “york09caPA01” using Algorithm 2 was 0.0566. The evaluation results show that both algorithms are effective for improving retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoHYYZ09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoHYYZ09,
		author = {Jiashu Zhao and Xiangji Huang and Zheng Ye and Jianhan Zhu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2009: Chemical Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/yorku.CHEM.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoHYYZ09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Legal 

#### Overview of the TREC 2009 Legal Track

_Bruce Hedin, Stephen Tomlinson, Jason R. Baron, Douglas W. Oard_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/LEGAL09.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec18/papers/LEGAL09.OVERVIEW.pdf)
??? abstract "Abstract"
	
	TREC 2009 was the fourth year of the Legal Track, which focuses on evaluation of search technology for “discovery” (i.e., responsive review) of electronically stored information in litigation and regulatory settings. The track included two tasks: an Interactive task (in which real users could iteratively refine their queries and/or engage in multi-pass relevance feedback) and a Batch task (two-pass search in a controlled setting with some relevant and nonrelevant documents manually marked after the first pass). This paper describes the design of the two tasks and presents the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HedinTBO09.bib) "
	```
	@inproceedings{DBLP:conf/trec/HedinTBO09,
		author = {Bruce Hedin and Stephen Tomlinson and Jason R. Baron and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2009 Legal Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/LEGAL09.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HedinTBO09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Machine Learning for Information Retrieval: TREC 2009 Web, Relevance  Feedback and Legal Tracks

_Gordon V. Cormack, Mona Mojdeh_

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./legal/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf](http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf)
- :material-file-search: **Runs:** [watrrf](./legal/runs.md#watrrf) | [watstack](./legal/runs.md#watstack) | [watlogistic](./legal/runs.md#watlogistic) | [watlint](./legal/runs.md#watlint)

??? abstract "Abstract"
	
	For the TREC 2009, we exhaustively classified every document in each corpus, using machine learning methods that had previously been shown to work well for email spam [9, 3]. We treated each document as a sequence of bytes, with no tokenization or parsing of tags or meta-information. This approach was used exclusively for the adhoc web, diversity and relevance feedback tasks, as well as to the batch legal task: the ClueWeb09 and Tobacco collections were processed end-to-end and never indexed. We did the interactive legal task in two phases: first, we used interactive search and judging to find a large and diverse set of training examples; then we used active learning process, similar to what we used for the other tasks, to find find more relevant documents. Finally, we fitted a censored (i.e. truncated) mixed normal distribution to estimate recall and the cutoff to optimize F1, the principal effectiveness measure.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackM09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackM09,
		author = {Gordon V. Cormack and Mona Mojdeh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Machine Learning for Information Retrieval: {TREC} 2009 Web, Relevance Feedback and Legal Tracks},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackM09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Backstop LLP and Cleary Gottlied Steen & Hamilton LLP at TREC  Legal Track 2009

_Bruce Ellis Fein, Brian Merrell, F. Eli Nelson_

- :fontawesome-solid-user-group: **Participant:** [Cleary_Backstop](./legal/participants.md#cleary_backstop)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/backstop.LEGAL.pdf](http://trec.nist.gov/pubs/trec18/papers/backstop.LEGAL.pdf)
- :material-file-search: **Runs:** [CGSHBCK2](./legal/runs.md#cgshbck2) | [CGSHBCK](./legal/runs.md#cgshbck) | [CGSHBCK1](./legal/runs.md#cgshbck1)

??? abstract "Abstract"
	
	This paper presents the results of the collaborative entry of Backstop LLP and Cleary Gottlieb Steen & Hamilton LLP in the Legal Track of the 2009 Text Retrieval Conference (TREC) sponsored by the National Institute for Standards and Technology (NIST). The Legal Track served as a truncated replication of a document review of almost one million documents. Backstop software, assisted by attorney document review of less than one-tenth of one percent of the overall document set, classified the documents and achieved a combined accuracy rate (“F1 score”) of approximately 80%.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FeinMN09.bib) "
	```
	@inproceedings{DBLP:conf/trec/FeinMN09,
		author = {Bruce Ellis Fein and Brian Merrell and F. Eli Nelson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Backstop {LLP} and Cleary Gottlied Steen {\&} Hamilton {LLP} at {TREC} Legal Track 2009},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/backstop.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FeinMN09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Sparse Matrix Factorization: Applications to Latent Semantic Indexing

_Erin Moulding, Raymond J. Spiteri, April Kontostathis_

- :fontawesome-solid-user-group: **Participant:** [URSINUS](./legal/participants.md#ursinus)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ursinus.LEGAL.pdf](http://trec.nist.gov/pubs/trec18/papers/ursinus.LEGAL.pdf)
- :material-file-search: **Runs:** [ucedlsi](./legal/runs.md#ucedlsi) | [uclsi](./legal/runs.md#uclsi) | [ucscra](./legal/runs.md#ucscra)

??? abstract "Abstract"
	
	This article describes the use of Latent Semantic Indexing (LSI) and some of its variants for the TREC Legal batch task. Both folding-in and Essential Dimensions of LSI (EDLSI) ap- peared as if they might be successful for recall-focused retrieval on a collection of this size. Furthermore, we developed a new LSI technique, one which replaces the Singular Value Decomposition (SVD) with another technique for matrix factorization, the sparse column-row approximation (SCRA). We were able to conclude that all three LSI techniques have similar performance. Although our 2009 results showed significant improvement when compared to our 2008 results, the use of a better method for selection of the parameter K, which is the ranking that results in the best balance between precision and recall, appears to have provided the most benefit.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MouldingSK09.bib) "
	```
	@inproceedings{DBLP:conf/trec/MouldingSK09,
		author = {Erin Moulding and Raymond J. Spiteri and April Kontostathis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Sparse Matrix Factorization: Applications to Latent Semantic Indexing},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ursinus.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MouldingSK09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Clearwell Systems at TREC 2009 Legal Interactive

_Venkat Rangan, Maojin Jiang_

- :fontawesome-solid-user-group: **Participant:** [Clearwell09](./legal/participants.md#clearwell09)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/clearwell09.legal.pdf](http://trec.nist.gov/pubs/trec18/papers/clearwell09.legal.pdf)
- :material-file-search: **Runs:** [Clearwell09i](./legal/runs.md#clearwell09i) | [clearwell01](./legal/runs.md#clearwell01)

??? abstract "Abstract"
	
	The TREC Legal Track 2009 features an Interactive Task that is designed to replicate real-world challenges in producing a collection of responsive documents from a large collection of documents. The task required us to produce responsive documents from any of the seven topics, which are production requests. Clearwell Systems incorporated novel methods for producing a responsive collection using a combination of automated sampling, evaluation of the samples, and using the samples as input into a blind relevance feedback engine. The algorithms applied use an automatic correlation covariance matrix for automatic evaluation of the samples and, using the correlation coefficient, determine whether the process of blind feedback converges to a highly correlated set of responsive documents. The number of iterations of sampling, the K-value for blind feedback, along with the final convergence threshold are monitored. The F-measure results of this are compared across the three different Interactive Topics that Clearwell participated in, for discussions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RanganJ09.bib) "
	```
	@inproceedings{DBLP:conf/trec/RanganJ09,
		author = {Venkat Rangan and Maojin Jiang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Clearwell Systems at {TREC} 2009 Legal Interactive},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/clearwell09.legal.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RanganJ09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### EQUIVIO at TREC 2009 Legal Interactive

_Tal Sterenzy_

- :fontawesome-solid-user-group: **Participant:** [Equivio](./legal/participants.md#equivio)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/equivio.LEGAL.pdf](http://trec.nist.gov/pubs/trec18/papers/equivio.LEGAL.pdf)
- :material-file-search: **Runs:** [Equivio207R1](./legal/runs.md#equivio207r1) | [Equivio205R1](./legal/runs.md#equivio205r1)

??? abstract "Abstract"
	
	Equivio participated in two runs under the legal interactive track: topics 205 and 207. The runs utilized the Equivio>Relevance product. Equivio>Relevance is an expert-guided system which enables automated prioritization of documents and keywords. Based on initial input from a lead attorney, Equivio>Relevance uses statistical and self-learning techniques to calculate graduated relevance scores for each document in the data collection. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Sterenzy09.bib) "
	```
	@inproceedings{DBLP:conf/trec/Sterenzy09,
		author = {Tal Sterenzy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{EQUIVIO} at {TREC} 2009 Legal Interactive},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/equivio.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Sterenzy09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments with the Negotiated Boolean Queries of the TREC 2009  Legal Track

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [ot](./legal/participants.md#ot)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/open-text.LEGAL.pdf](http://trec.nist.gov/pubs/trec18/papers/open-text.LEGAL.pdf)
- :material-file-search: **Runs:** [otL09rvl](./legal/runs.md#otl09rvl) | [otL09F](./legal/runs.md#otl09f) | [otL09frwF](./legal/runs.md#otl09frwf)

??? abstract "Abstract"
	
	For our participation in the Batch Task of the TREC 2009 Legal Track, we produced several retrieval sets to compare experimental Boolean, vector, fusion and relevance feedback techniques for e-Discovery requests. In this paper, we have reported not just the mean scores of the experimental approaches but also the largest per-topic impacts of the techniques for several measures. The experimental automatic relevance feedback technique was found to attain a statistically significant gain over the reference Boolean result in both the mean Precision@B and F1@K measures.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson09.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson09,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments with the Negotiated Boolean Queries of the {TREC} 2009 Legal Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/open-text.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ZL Technologies at TREC 2009 Legal Interactive: Comparing Exclusionary  and Investigative Approaches for Electronic Discovery Using the TREC  Enron Corpus

_John Wang, Cameron Coles, Rob Elliot, Sofia Andrianakou_

- :fontawesome-solid-user-group: **Participant:** [ZLTech](./legal/participants.md#zltech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/zlti.legal.pdf](http://trec.nist.gov/pubs/trec18/papers/zlti.legal.pdf)
- :material-file-search: **Runs:** [CompCustIT09](./legal/runs.md#compcustit09) | [CompEntrIT09](./legal/runs.md#compentrit09)

??? abstract "Abstract"
	
	Organizations responding to requests to produce electronically stored information (ESI) for litigation today often conduct information retrieval with a limited amount of data that has first been culled by custodian mailboxes, date ranges, or other factors chosen semi-arbitrarily based on legal negotiations or other exogenous factors. The culling process does not necessarily take into account the composition of the data set; and may, in fact, impede the expediency and cost-effectiveness of the eDiscovery process as ESI not initially identified may need to be collected later in the eDiscovery process. This exclusionary eDiscovery approach has been recommended by search and information retrieval technology providers in the past, in part, based on the state of technology available at the time; however, the technology now exists to perform an inclusive, content-based, investigative eDiscovery across a large document collection without the introduction of semi- arbitrary exclusion factors. In this paper, we investigate whether limited document retrieval based on custodian email mailboxes results in lower recall and produces fewer responsive documents than a broader, inclusive search process that covers all potential custodians. In order to compare the two approaches, we designed an experiment with two independent teams conducting electronic discovery using the different approaches. We found that searching across the entire data set resulted in finding significantly more responsive documents and more initial custodians than implementing an approach that relies on custodian-based culling. Specifically, investigative eDiscovery found 516% more relevant documents and 1825% more initial custodians in our study. Based on these results, we believe organizations that employ an exclusionary, culling-based methodology may require subsequent collections, risk under production and sanctions during litigation, and will ultimately expend more resources in responding to eDiscovery production requests with a less comprehensive result.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangCEA09.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangCEA09,
		author = {John Wang and Cameron Coles and Rob Elliot and Sofia Andrianakou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ZL} Technologies at {TREC} 2009 Legal Interactive: Comparing Exclusionary and Investigative Approaches for Electronic Discovery Using the {TREC} Enron Corpus},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/zlti.legal.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangCEA09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2009 at the University of Buffalo: Interactive Legal E-Discovery  With Enron Emails

_Jianqiang Wang, Ying Sun, Paul Thompson_

- :fontawesome-solid-user-group: **Participant:** [SUNY_Buffalo](./legal/participants.md#suny_buffalo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ubuffalo.LEGAL.pdf](http://trec.nist.gov/pubs/trec18/papers/ubuffalo.LEGAL.pdf)
- :material-file-search: **Runs:** [buffalo](./legal/runs.md#buffalo)

??? abstract "Abstract"
	
	For the TREC 2009, the team from University at Buffalo, the State University of New York participated in the Legal E-Discovery track, working on the interactive search task. We explored indexing and searching at both the record level and the document level with the Enron email collection. We studied the usefulness of fielded search and document presentation features such as clustering documents based on email threads. For query formulation for the selected search topic, we combined a precision-oriented Specific Query method that a recall-oriented Generic Query method. Future evaluation of the effectiveness of these query techniques is still needed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangST09.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangST09,
		author = {Jianqiang Wang and Ying Sun and Paul Thompson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2009 at the University of Buffalo: Interactive Legal E-Discovery With Enron Emails},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ubuffalo.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangST09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Model for Understanding Collaborative Information Behavior in E-Discovery

_Zhen Yue, Daqing He_

- :fontawesome-solid-user-group: **Participant:** [pitt_sis](./legal/participants.md#pitt_sis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/pitt_sis.legal.pdf](http://trec.nist.gov/pubs/trec18/papers/pitt_sis.legal.pdf)
- :material-file-search: **Runs:** [pittsis09](./legal/runs.md#pittsis09)

??? abstract "Abstract"
	
	The University of Pittsburgh team participated in the interactive task of Legal Track in TREC 2009. We designed an experiment to investigate into the collaborative information behavior (CIB) of the group of people working on e-discovery tasks provided by Legal Track in TREC 2009. Through the studies, we proposed a model for understanding CIB in e-discovery.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YueH09.bib) "
	```
	@inproceedings{DBLP:conf/trec/YueH09,
		author = {Zhen Yue and Daqing He},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Model for Understanding Collaborative Information Behavior in E-Discovery},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/pitt\_sis.legal.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YueH09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Web 

#### Overview of the TREC 2009 Web Track

_Charles L. A. Clarke, Nick Craswell, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/WEB09.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec18/papers/WEB09.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC Web Track explores and evaluates Web retrieval technologies. Currently, the Web Track conducts experiments using the new billion-page ClueWeb09 collection1. The TREC 2009 track is the successor to the Terabyte Retrieval Track, which ran from 2004 to 2006, and to the older Web Track, which ran from 1999 to 2003. The TREC 2009 Web Track includes both a traditional adhoc retrieval task and a new diversity task. The goal of this diversity task is to return a ranked list of pages that together provide complete coverage for a query, while avoiding excessive redundancy in the result list. For example, given the query “windows”, a system might return the Windows update page first, followed by the Microsoft home page, and then a news article discussing the release of Windows 7. Mixed in these results might be pages providing product information on doors and windows for homes and businesses. The track used the new ClueWeb09 dataset as its document collection. The full collection consists of roughly 1 billion web pages, comprising approximately 25TB of uncompressed data (5TB compressed) in multiple languages. The dataset was crawled from the Web during January and February 2009. For groups who were unable to work with this full “Category A” dataset, the track accepted runs over the smaller ClueWeb09 “Category B” dataset, a subset of about 50 million English-language pages. Topics for the track were created from the logs of a commercial search engine, with the aid of tools developed at Microsoft Research. Given a target query, these tools extracted and analyzed groups of related queries, using co-clicks and other information, to identify clusters of queries that highlight different aspects and interpretations of the target query. These clusters were employed by NIST for topic development. Each resulting topic is structured as a representative set of subtopics, each related to a different user need. Documents were judged with respect to the subtopics, as well as with respect to the topic as a whole. For each subtopic, NIST assessors made a binary judgment as to whether or not the document satisfies the information need associated with the subtopic. These topics were used for both the adhoc task and the diversity task. For both tasks, partici- pants executed the original target queries over the ClueWeb09 collection. The tasks differ primarily in their evaluation measures. The adhoc task uses an estimate of mean average precision, based on overall topical relevance [3]. The diversity task uses newer measures, based on the subtopics, which explicitly consider novelty in the result list (intent aware precision [1] and alpha-nDCG [4]) A total of 26 groups submitted runs to the track, with many groups participating in both tasks. Table 1 summarizes the participation of these groups. About half the groups worked with the full collection. A few groups submitted runs over both the full (Category A) collection and the Category B collection. This report provides an overview of the track, including topic development, evaluation measures, and results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeCS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeCS09,
		author = {Charles L. A. Clarke and Nick Craswell and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2009 Web Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/WEB09.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeCS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Web Track 2009 Diversity Track

_Wenjing Bi, Xiaoming Yu, Yue Liu, Feng Guan, Zeying Peng, Hongbo Xu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./web/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ictnet.WEB-DIV.pdf](http://trec.nist.gov/pubs/trec18/papers/ictnet.WEB-DIV.pdf)
- :material-file-search: **Runs:** [ICTNETDivR1](./web/runs.md#ictnetdivr1) | [ICTNETDivR3](./web/runs.md#ictnetdivr3) | [ICTNETADRun3](./web/runs.md#ictnetadrun3) | [ICTNETDivR2](./web/runs.md#ictnetdivr2) | [ICTNETADRun4](./web/runs.md#ictnetadrun4) | [ICTNETADRun5](./web/runs.md#ictnetadrun5)

??? abstract "Abstract"
	
	We (ICTNET team) participated in Web Track of TREC2009, and in this paper, we summarize our work on Diversity task of Web Track, which is new in this year. The goal of the diversity task is to return a ranked list of pages that together provide complete coverage for a query, while avoiding excessive redundancy in the result list. For this task, we cluster the results of ad hoc task, and rerank the results depend on subtopics docs covers. Besides, we introduce two methods which tried to find the implicit subtopic by using the docs returned from commerce search engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BiYLGPXC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/BiYLGPXC09,
		author = {Wenjing Bi and Xiaoming Yu and Yue Liu and Feng Guan and Zeying Peng and Hongbo Xu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Web Track 2009 Diversity Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ictnet.WEB-DIV.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BiYLGPXC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad Hoc and Diversity Retrieval at the University of Delaware

_Praveen Chandar, Aparna Kailasam, Divya Muppaneni, Sree Lekha Thota, Ben Carterette_

- :fontawesome-solid-user-group: **Participant:** [UDel](./web/participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.WEB.MQ.pdf](http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.WEB.MQ.pdf)
- :material-file-search: **Runs:** [udelIndDMRM](./web/runs.md#udelinddmrm) | [udelIndDRSP](./web/runs.md#udelinddrsp) | [udelSimPrune](./web/runs.md#udelsimprune) | [udelFMWG](./web/runs.md#udelfmwg) | [udelIndDRPR](./web/runs.md#udelinddrpr) | [udelFMRM](./web/runs.md#udelfmrm)

??? abstract "Abstract"
	
	This is the report on the University of Delaware Information Retrieval Lab's participation in the TREC 2009 Web and Million Query tracks. Our report on the Relevance Feedback track is in a separate document [3].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChandarKMTC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChandarKMTC09,
		author = {Praveen Chandar and Aparna Kailasam and Divya Muppaneni and Sree Lekha Thota and Ben Carterette},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Ad Hoc and Diversity Retrieval at the University of Delaware},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.WEB.MQ.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChandarKMTC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Machine Learning for Information Retrieval: TREC 2009 Web, Relevance  Feedback and Legal Tracks

_Gordon V. Cormack, Mona Mojdeh_

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./web/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf](http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf)
- :material-file-search: **Runs:** [watd1](./web/runs.md#watd1) | [watd3](./web/runs.md#watd3) | [watd5](./web/runs.md#watd5) | [watwp](./web/runs.md#watwp) | [watrrfw](./web/runs.md#watrrfw) | [uwgym](./web/runs.md#uwgym) | [watprf](./web/runs.md#watprf)

??? abstract "Abstract"
	
	For the TREC 2009, we exhaustively classified every document in each corpus, using machine learning methods that had previously been shown to work well for email spam [9, 3]. We treated each document as a sequence of bytes, with no tokenization or parsing of tags or meta-information. This approach was used exclusively for the adhoc web, diversity and relevance feedback tasks, as well as to the batch legal task: the ClueWeb09 and Tobacco collections were processed end-to-end and never indexed. We did the interactive legal task in two phases: first, we used interactive search and judging to find a large and diverse set of training examples; then we used active learning process, similar to what we used for the other tasks, to find find more relevant documents. Finally, we fitted a censored (i.e. truncated) mixed normal distribution to estimate recall and the cutoff to optimize F1, the principal effectiveness measure.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackM09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackM09,
		author = {Gordon V. Cormack and Mona Mojdeh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Machine Learning for Information Retrieval: {TREC} 2009 Web, Relevance Feedback and Legal Tracks},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackM09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Research at TREC 2009: Web and Relevance Feedback Track

_Nick Craswell, Dennis Fetterly, Marc Najork, Stephen Robertson, Emine Yilmaz_

- :fontawesome-solid-user-group: **Participant:** [msrc](./web/participants.md#msrc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/microsoft.WEB.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/microsoft.WEB.RF.pdf)
- :material-file-search: **Runs:** [MS1](./web/runs.md#ms1) | [MS2](./web/runs.md#ms2) | [MSDiv2](./web/runs.md#msdiv2) | [MSDiv1](./web/runs.md#msdiv1) | [MSDiv3](./web/runs.md#msdiv3)

??? abstract "Abstract"
	
	We took part in the Web and Relevance Feedback tracks, using the ClueWeb09 corpus. To process the corpus, we developed a parallel processing pipeline which avoids the generation of an inverted file. We describe the components of the parallel architecture and the pipeline and how we ran the TREC experiments, and we present effectiveness results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellFNRY09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CraswellFNRY09,
		author = {Nick Craswell and Dennis Fetterly and Marc Najork and Stephen Robertson and Emine Yilmaz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Research at {TREC} 2009: Web and Relevance Feedback Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/microsoft.WEB.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CraswellFNRY09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRRA at TREC 2009: Index Term Weighting Based on Divergence From  Independence Model

_Bekir Taner Dinçer, Ilker Kocabas, Bahar Karaoglan_

- :fontawesome-solid-user-group: **Participant:** [IRRA](./web/participants.md#irra)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/muglau.WEB.MQ.pdf](http://trec.nist.gov/pubs/trec18/papers/muglau.WEB.MQ.pdf)
- :material-file-search: **Runs:** [irra1a](./web/runs.md#irra1a) | [irra2a](./web/runs.md#irra2a) | [irra3a](./web/runs.md#irra3a) | [irra1d](./web/runs.md#irra1d) | [irra2d](./web/runs.md#irra2d) | [irra3d](./web/runs.md#irra3d)

??? abstract "Abstract"
	
	IRRA (IR-Ra) group participated in the 2009 Web track (both adhoc task and diversity task) and the Million Query track. In this year, the major concern is to examine the effectiveness of a novel, nonparametric index term weighting model, divergence from independence (DFI). The notion of independence, which is the notion behind the well-known statistical exploratory data analysis technique called the correspondence analysis (Greenacre, 1984; Jambu, 1991), can be adapted to the index term weighting problem. In this respect, it can be thought of as a qualitative description of the importance of terms for documents, in which they appear, importance in the sense of contribution to the information contents of documents relative to other terms. According to the independence notion, if the ratios of the frequencies of two different terms are the same across documents, they are independent from documents. For example, each Web page contains a pair of “html” and a pair of “body” tags, so that the ratio of frequencies of these tags is the same across all Web pages, indicating that the “html” and “body” tags are independent from Web pages. They are used by design, irrespective of the information contents of Web pages. On the other hand, some tags, such as “image”, “table”, which are also independent from Web pages, may occur less or more in some pages than the expected frequencies suggested by the independence model; so, their associated frequency ratios may not be the same for all Web pages. However, it is reasonable to expect that, if the pages are not about the tags' usage, such as a “HTML Handbook”, frequencies of those tags should not be significantly different from their expected frequencies: they should be close to the expectation, i.e., in a parametric point of view, their observed frequencies on individual documents should be attributed to chance fluctuation. Although this tag example is helpful in exemplifying the use of independence notion, it is obvious that the tags are artificial, and so, governed by some rules completely different from the rules of a spoken language. Nonetheless, some words, like the ones in a common “stopwords list”, appear in documents, not because of their contribution to the information contents of documents, but because of the grammatical rules. On this account, such words can be modeled as if they were tags, because they are independent from documents in the same manner. Their observed frequencies in individual documents is expected to fluctuate around their frequencies expected under independence, as in the case of tags. Content bearing words are, therefore, the words whose frequencies highly diverge from the frequencies expected under independence. The results of the TREC experiments about IRRA runs show that the independence notion promises a natural basis for quantifying the categorical relationships between the terms and the documents. The TERRIER retrieval platform (Ounis et al., 2007) is used to index and search the ClueWeb09-T09B1 data set, a subset of about 50 million Web pages in English (TREC 2009 “Category B” data set). During indexing and searching, terms are stemmed and a particular set of stop words2 are eliminated.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DincerKK09.bib) "
	```
	@inproceedings{DBLP:conf/trec/DincerKK09,
		author = {Bekir Taner Din{\c{c}}er and Ilker Kocabas and Bahar Karaoglan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IRRA} at {TREC} 2009: Index Term Weighting Based on Divergence From Independence Model},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/muglau.WEB.MQ.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DincerKK09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Research Asia at the Web Track of TREC 2009

_Zhicheng Dou, Kun Chen, Ruihua Song, Yunxiao Ma, Shuming Shi, Ji-Rong Wen_

- :fontawesome-solid-user-group: **Participant:** [MSRAsia](./web/participants.md#msrasia)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/microsoft-asia.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/microsoft-asia.WEB.pdf)
- :material-file-search: **Runs:** [MSRANORM](./web/runs.md#msranorm) | [MSRAAF](./web/runs.md#msraaf) | [MSRAC](./web/runs.md#msrac) | [MSRABASE](./web/runs.md#msrabase) | [MSRACS](./web/runs.md#msracs) | [MSRAACSF](./web/runs.md#msraacsf)

??? abstract "Abstract"
	
	In TREC 2009, we participate in the Web track, and focus on the diversity task. We propose to diversify web search results by first mining subtopics, and then rank results based on mined subtopics. We propose a model to diversify search results by considering both relevance of documents and richness of mined subtopics. Our experimental results show that the model improves diversity of search results in terms of α-NDCG, and combining subtopics from multiple data sources helps further improve result diversity.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DouCSMSW09.bib) "
	```
	@inproceedings{DBLP:conf/trec/DouCSMSW09,
		author = {Zhicheng Dou and Kun Chen and Ruihua Song and Yunxiao Ma and Shuming Shi and Ji{-}Rong Wen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Research Asia at the Web Track of {TREC} 2009},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/microsoft-asia.WEB.pdf},
		timestamp = {Tue, 01 Dec 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DouCSMSW09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT University at TREC 2009: Web Track

_Steven Garcia_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./web/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/rmit.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/rmit.WEB.pdf)
- :material-file-search: **Runs:** [RmitLm](./web/runs.md#rmitlm) | [RmitOkapi](./web/runs.md#rmitokapi) | [RmitDiv](./web/runs.md#rmitdiv)

??? abstract "Abstract"
	
	RMIT participated in the 2009 Web Track tasks. Our submissions utilised the Zettair search engine1 to index and search the Category B subset of the ClueWeb collection used by the Web Track. The Web Track was composed of two tasks, a traditional adhoc retrieval task, and a new diversity task where participants attempted to retrieve documents covering a range of sub topics for each query. Sub topics were not provided with the queries. Our experiments utilised the well known measures Okapi BM25 and language modeling with Dirichlet smoothing for the adhoc task. For the diversity task we attempted to improve the diversity of query results by minimising the number of documents returned for a single domain.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Garcia09.bib) "
	```
	@inproceedings{DBLP:conf/trec/Garcia09,
		author = {Steven Garcia},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} University at {TREC} 2009: Web Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/rmit.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Garcia09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Web Track 2009 Ad-hoc Task

_Feng Guan, Xiaoming Yu, Zeying Peng, Hongbo Xu, Yue Liu, Linhai Song, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./web/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ictnet.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/ictnet.WEB.pdf)
- :material-file-search: **Runs:** [ICTNETDivR1](./web/runs.md#ictnetdivr1) | [ICTNETDivR3](./web/runs.md#ictnetdivr3) | [ICTNETADRun3](./web/runs.md#ictnetadrun3) | [ICTNETDivR2](./web/runs.md#ictnetdivr2) | [ICTNETADRun4](./web/runs.md#ictnetadrun4) | [ICTNETADRun5](./web/runs.md#ictnetadrun5)

??? abstract "Abstract"
	
	This paper is about the work done for ad-hoc task of TREC 2009 Web Track. We introduce three methods for this task, including two improved BM25 models and query expansion. The results of these models indicate that both minimum window and query expansion could improve BM25 model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GuanYPXLSC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/GuanYPXLSC09,
		author = {Feng Guan and Xiaoming Yu and Zeying Peng and Hongbo Xu and Yue Liu and Linhai Song and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Web Track 2009 Ad-hoc Task},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ictnet.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GuanYPXLSC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Twente @ TREC 2009: Indexing Half a Million Web Pages

_Claudia Hauff, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [utwente](./web/participants.md#utwente)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/utwente.WEB.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/utwente.WEB.RF.pdf)
- :material-file-search: **Runs:** [twCSrs9N](./web/runs.md#twcsrs9n) | [twCSrsR](./web/runs.md#twcsrsr) | [twJ48rsU](./web/runs.md#twj48rsu) | [twCSodpRNB](./web/runs.md#twcsodprnb) | [twCSodpRBB](./web/runs.md#twcsodprbb)

??? abstract "Abstract"
	
	The University of Twente participated in three tasks of TREC 2009: the adhoc task, the diversity task and the relevance feedback task. All experiments are performed on the English part of ClueWeb09. We describe our approach to tuning our retrieval system in absence of training data in Section 3. We describe the use of categories and a query log for diversifying search results in Section 4. Section 5 describes preliminary results for the relevance feedback task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HauffH09.bib) "
	```
	@inproceedings{DBLP:conf/trec/HauffH09,
		author = {Claudia Hauff and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Twente @ {TREC} 2009: Indexing Half a Million Web Pages},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/utwente.WEB.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HauffH09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Heuristic Ranking and Diversification of Web Documents

_Jiyin He, Krisztian Balog, Katja Hofmann, Edgar Meij, Maarten de Rijke, Manos Tsagkias, Wouter Weerkamp_

- :fontawesome-solid-user-group: **Participant:** [UAms](./web/participants.md#uams)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.WEB.pdf)
- :material-file-search: **Runs:** [uvaee](./web/runs.md#uvaee) | [uvamrf](./web/runs.md#uvamrf) | [uvamrftop](./web/runs.md#uvamrftop) | [uvaaol](./web/runs.md#uvaaol) | [spc](./web/runs.md#spc) | [tm](./web/runs.md#tm)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdam's Intelligent Systems Lab in the web track at TREC 2009. We participated in the adhoc and diversity task. We find that spam is an important issue in the ad hoc task and that Wikipedia-based heuristic optimization approaches help to boost the retrieval performance, which is assumed to potentially reduce spam in the top ranked results. As for the diversity task, we explored different methods. Clustering and a topic model-based approach have a similar performance and both are relatively better than a query log based approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeBHMRTW09.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeBHMRTW09,
		author = {Jiyin He and Krisztian Balog and Katja Hofmann and Edgar Meij and Maarten de Rijke and Manos Tsagkias and Wouter Weerkamp},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Heuristic Ranking and Diversification of Web Documents},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeBHMRTW09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Result Diversity and Entity Ranking Experiments: Anchors, Links, Text  and Wikipedia

_Rianne Kaptein, Marijn Koolen, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [Amsterdam](./web/participants.md#amsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uamsterdam-kamps.ENT.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uamsterdam-kamps.ENT.WEB.pdf)
- :material-file-search: **Runs:** [UamsAwebQE10](./web/runs.md#uamsawebqe10) | [UamsDancTFb1](./web/runs.md#uamsdanctfb1) | [UamsDwebLFou](./web/runs.md#uamsdweblfou) | [UamsDwQE10TF](./web/runs.md#uamsdwqe10tf) | [UamsAw7an3](./web/runs.md#uamsaw7an3)

??? abstract "Abstract"
	
	In this paper, we document our efforts in participating to the TREC 2009 Entity Ranking and Web Tracks. We had multiple aims: For the Web Track's Adhoc task we experiment with document text and anchor text representation, and the use of the link structure. For the Web Track's Diversity task we experiment with using a top down sliding window that, given the top ranked documents, chooses as the next ranked document the one that has the most unique terms or links. We test our sliding window method on a standard document text index and an index of propagated anchor texts. We also experiment with extreme query expansions by taking the top n results of the initial ranking as multi-faceted aspects of the topic to construct n relevance models to obtain n sets of results. A final diverse set of results is obtained by merging the n results lists. For the Entity Ranking Track, we also explore the effectiveness of the anchor text representation, look at the co-citation graph, and experiment with using Wikipedia as a pivot. Our main findings can be summarized as follows: Anchor text is very effective for diversity. It gives high early precision and the results cover more relevant sub-topics than the document text index. Our baseline runs have low diversity, which limits the possible impact of the sliding window approach. New link information seems more effective for diversifying text-based search results than the amount of unique terms added by a document. In the entity ranking task, anchor text finds few primary pages , but it does retrieve a large number of relevant pages. Using Wikipedia as a pivot results in large gains of P10 and NDCG when only primary pages are considered. Although the links between the Wikipedia entities and pages in the Clueweb collection are sparse, the precision of the existing links is very high.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KapteinKK09.bib) "
	```
	@inproceedings{DBLP:conf/trec/KapteinKK09,
		author = {Rianne Kaptein and Marijn Koolen and Jaap Kamps},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Result Diversity and Entity Ranking Experiments: Anchors, Links, Text and Wikipedia},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uamsterdam-kamps.ENT.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KapteinKK09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2009 Web Track: Finding Relevant and Diverse Results  for Large Scale Web Search

_Zhichao Li, Fei Chen, Qianli Xing, Junwei Miao, Yufei Xue, Tong Zhu, Bo Zhou, Rongwei Cen, Yiqun Liu, Min Zhang, Yijiang Jin, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [THUIR](./web/participants.md#thuir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/tsinghuau.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/tsinghuau.WEB.pdf)
- :material-file-search: **Runs:** [THUIR09An](./web/runs.md#thuir09an) | [THUIR09TxAn](./web/runs.md#thuir09txan) | [THUIR09LuTA](./web/runs.md#thuir09luta) | [THUIR09QeDiv](./web/runs.md#thuir09qediv) | [THUIR09FuClu](./web/runs.md#thuir09fuclu) | [THUIR09AbClu](./web/runs.md#thuir09abclu)

??? abstract "Abstract"
	
	This is the 8th year that IR group of Tsinghua University (THUIR) participates in TREC. This year we focus on Web track, which contains two tasks, namely ad hoc and diversity. On ad hoc task, we improved the efficiency of our distributed retrieval system TMiner to handle terabytes of Web data. Then three studies have been done, namely page quality estimation, ranking feature analysis, and model comparison. On diversity task, we proposed several new approaches on searching strategy, user intention detection, and duplication elimination. To mine user‟s intention, we proposed and compared two different strategies, namely „searching + content-based diversity‟ which is a kind of result clustering, and „user based diverse intention prediction + searching‟ which is in the branch of query expansion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiCXMXZZCLZJM09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiCXMXZZCLZJM09,
		author = {Zhichao Li and Fei Chen and Qianli Xing and Junwei Miao and Yufei Xue and Tong Zhu and Bo Zhou and Rongwei Cen and Yiqun Liu and Min Zhang and Yijiang Jin and Shaoping Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2009 Web Track: Finding Relevant and Diverse Results for Large Scale Web Search},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/tsinghuau.WEB.pdf},
		timestamp = {Wed, 16 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LiCXMXZZCLZJM09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCD SIFT in the TREC 2009 Web Track

_David Lillis, Fergus Toolan, Ling Lin, Rem W. Collier, John Dunnion_

- :fontawesome-solid-user-group: **Participant:** [CSIUCD](./web/participants.md#csiucd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ucollege-dublin.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/ucollege-dublin.WEB.pdf)
- :material-file-search: **Runs:** [UCDSIFTslide](./web/runs.md#ucdsiftslide) | [UCDSIFTinter](./web/runs.md#ucdsiftinter) | [UCDSIFTprob](./web/runs.md#ucdsiftprob) | [UCDSIFTdiv](./web/runs.md#ucdsiftdiv)

??? abstract "Abstract"
	
	The SIFT (SIFT Information Fusion Techniques) group in UCD is dedicated to researching Data Fusion in Information Retrieval. This area of research involves the merging of multiple sets of results into a single result set that is presented to the user. As a means of evaluating the effectiveness of this work, the group entered Category B of the TREC 2009 Web Track. This paper discusses the strategies and experiments employed by the UCD SIFT group in entering the TREC Web Track 2009. This involved the use of freely-available Information Retrieval tools to provide inputs to the data fusion process, with the aim of contrasting with more sophisticated systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LillisTLCD09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LillisTLCD09,
		author = {David Lillis and Fergus Toolan and Ling Lin and Rem W. Collier and John Dunnion},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UCD} {SIFT} in the {TREC} 2009 Web Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ucollege-dublin.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LillisTLCD09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Of Ivory and Smurfs: Loxodontan MapReduce Experiments for Web Search

_Jimmy Lin, Tamer Elsayed, Lidan Wang, Donald Metzler_

- :fontawesome-solid-user-group: **Participant:** [UMD](./web/participants.md#umd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/umd-yahoo.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/umd-yahoo.WEB.pdf)
- :material-file-search: **Runs:** [UMHOObm25GS](./web/runs.md#umhoobm25gs) | [UMHOObm25IF](./web/runs.md#umhoobm25if) | [UMHOObm25B](./web/runs.md#umhoobm25b) | [UMHOOsd](./web/runs.md#umhoosd) | [UMHOOsdp](./web/runs.md#umhoosdp) | [UMHOOqlB](./web/runs.md#umhooqlb) | [UMHOOqlGS](./web/runs.md#umhooqlgs) | [UMHOOqlIF](./web/runs.md#umhooqlif)

??? abstract "Abstract"
	
	This paper describes Ivory, an attempt to build a distributed retrieval system around the open-source Hadoop implementation of MapReduce. We focus on three noteworthy aspects of our work: a retrieval architecture built directly on the Hadoop Distributed File System (HDFS), a scalable MapReduce algorithm for inverted indexing, and webpage classification to enhance retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinEWM09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinEWM09,
		author = {Jimmy Lin and Tamer Elsayed and Lidan Wang and Donald Metzler},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Of Ivory and Smurfs: Loxodontan MapReduce Experiments for Web Search},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/umd-yahoo.WEB.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LinEWM09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2009: Experiments with Terrier

_Richard McCreadie, Craig Macdonald, Iadh Ounis, Jie Peng, Rodrygo L. T. Santos_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./web/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf)
- :material-file-search: **Runs:** [uogTrdphP](./web/runs.md#uogtrdphp) | [uogTrdphCEwP](./web/runs.md#uogtrdphcewp) | [uogTrdphA](./web/runs.md#uogtrdpha) | [uogTrDYScdA](./web/runs.md#uogtrdyscda) | [uogTrDYCcsB](./web/runs.md#uogtrdyccsb) | [uogTrDPCQcdB](./web/runs.md#uogtrdpcqcdb)

??? abstract "Abstract"
	
	In TREC 2009, we extend our Voting Model for the faceted blog distillation, top stories identification, and related entity finding tasks. Moreover, we experiment with our novel xQuAD framework for search result diversification. Besides fostering our research in mul- tiple directions, by participating in such a wide portfolio of tracks, we further develop the indexing and retrieval capabilities of our Terrier Information Retrieval platform, to effectively and efficiently cope with a new generation of large-scale test collections.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieMOPS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieMOPS09,
		author = {Richard McCreadie and Craig Macdonald and Iadh Ounis and Jie Peng and Rodrygo L. T. Santos},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2009: Experiments with Terrier},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieMOPS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Lucene for n-grams using the CLUEWeb Collection

_Gregory B. Newby, Christopher T. Fallen, Kylie McCormick_

- :fontawesome-solid-user-group: **Participant:** [ARSC09](./web/participants.md#arsc09)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/arsc.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/arsc.WEB.pdf)
- :material-file-search: **Runs:** [arsc09web](./web/runs.md#arsc09web)

??? abstract "Abstract"
	
	The ARSC team made modifications to the Apache Lucene engine to accommodate “go words,” taken from the Google Gigaword vocabulary of n-grams. Indexing the Category “B” subset of the ClueWeb collection was accomplished by a divide and conquer method, working across the separate ClueWeb subsets for 1, 2 and 3-grams.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NewbyFM09.bib) "
	```
	@inproceedings{DBLP:conf/trec/NewbyFM09,
		author = {Gregory B. Newby and Christopher T. Fallen and Kylie McCormick},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Lucene for n-grams using the CLUEWeb Collection},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/arsc.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NewbyFM09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Northeastern University in the TREC 2009 Web Track

_Shahzad Rajput, Evangelos Kanoulas, Virgiliu Pavlu, Javed A. Aslam_

- :fontawesome-solid-user-group: **Participant:** [NEU](./web/participants.md#neu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/northeasternu.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/northeasternu.WEB.pdf)
- :material-file-search: **Runs:** [NeuLMWebBase](./web/runs.md#neulmwebbase) | [NeuLMWeb600](./web/runs.md#neulmweb600) | [NeuLMWeb300](./web/runs.md#neulmweb300) | [NeuDiv1](./web/runs.md#neudiv1) | [NeuRRWeb300](./web/runs.md#neurrweb300) | [NeuDivW75](./web/runs.md#neudivw75)

??? abstract "Abstract"
	
	In a typical retrieval scenario a user poses a query to a retrieval system in order to satisfy an information need generated during some task the user is undertaking. Retrieval systems access an underline collection of searchable material and rank them according to some definition of relevance of the material to the users request and returns this ranked list to the user. In the case of web search where typical users express their information needs by 2-3 keywords submitted queries often time have ambiguous meanings, representing more than one information need. Given a query, a good retrieval system should be able to satisfy all possible users by ranking documents in a way that their content covers as many information needs as possible. The primary goal of our Web Track submission is to explore whether named entity tags can be utilized to diversify the returned ranked list of documents. Our hypothesis is that each information need could be represented by a certain named entity tag (or certain combination of them). For instance, in Table 1 one can see the example query taken from the Web Track web page. The query is “physical therapists”. The subtopics that correspond to this query are listed in the left column of the table. To illustrate our hypothesis, next to each subtopic, in bold, we have manually identified a possible combination of entity tags that could represent each subtopic/information need. Further, each document relevant to the original query could also be represented by a set of named entity tags. Instead of attempting to diversify documents based on the distance of their language models over text, we explored whether it is possible to diversify them according to the distance of their language model over entity tags. Entity tags could allow a further abstraction of documents avoiding issues like language mismatch. Our methodology highly depended on two assumptions: (1) retrieval methods based on a bug-of-words representation can retrieve many relevant documents in the top 2,000 positions, and (2) the relevant documents would be diverse enough at the first place. Then using our methodology we could abstract the representation of those documents and diversify the list based on their tag distributions. A second goal of our Web Track submission was to develop a simple spam filter. By analyzing a small subset of the documents, selected at random from the top 2,000 documents ranked by Indri language model per query over the new ClueWeb09 collection (category B) 1, we observed that 44.5% of them were spam. A large subset of the spam documents were those that contained query terms way too many times. For this purpose, we decided to develop a simple spam filter to remove these documents from the ranked list.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RajputKPA09.bib) "
	```
	@inproceedings{DBLP:conf/trec/RajputKPA09,
		author = {Shahzad Rajput and Evangelos Kanoulas and Virgiliu Pavlu and Javed A. Aslam},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Northeastern University in the {TREC} 2009 Web Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/northeasternu.WEB.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RajputKPA09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PARADISE Based Search Engine at TREC 2009 Web Track

_Dongdong Shan, Dongsheng Zhao, Jing He, Hongfei Yan_

- :fontawesome-solid-user-group: **Participant:** [pku2009](./web/participants.md#pku2009)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/pekingu.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/pekingu.WEB.pdf)
- :material-file-search: **Runs:** [pkuSewmTp](./web/runs.md#pkusewmtp) | [pkuStruct](./web/runs.md#pkustruct) | [pkuLink](./web/runs.md#pkulink)

??? abstract "Abstract"
	
	In this paper, we introduce the PARADISE search engine in TREC09 Web track. PARADISE is the abbreviation for Platform for Applying, Research and Developing Intelligent Search Engine, which is a search engine platform developed by SEWM group, Peking University. The system is designed to support both English and Chinese information retrieval. This system preprocessed and indexed the five hundred million web pages for this year's Web Track. In the preprocessing stage, the templates were removed, the encoding were identified and unified, and the anchor texts and InLink information are extracted with the mapreduce framework (using Hadoop in this system). In retrieval, our runs used an extension of BM25. This model distinguishes terms from different fields and integrated both term counts and position information. Furthermore, some web based features are also considered.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShanZHY09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShanZHY09,
		author = {Dongdong Shan and Dongsheng Zhao and Jing He and Hongfei Yan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PARADISE} Based Search Engine at {TREC} 2009 Web Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/pekingu.WEB.pdf},
		timestamp = {Mon, 15 May 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ShanZHY09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments with ClueWeb09: Relevance Feedback and Web Tracks

_Mark D. Smucker, Charles L. A. Clarke, Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./web/participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.RF.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.RF.WEB.pdf)
- :material-file-search: **Runs:** [WatSklq](./web/runs.md#watsklq) | [WatSklfu](./web/runs.md#watsklfu) | [WatSklfb](./web/runs.md#watsklfb) | [WatSdmrm3](./web/runs.md#watsdmrm3) | [WatSql](./web/runs.md#watsql) | [WatSdmrm3we](./web/runs.md#watsdmrm3we)

??? abstract "Abstract"
	
	In this paper, we report on our TREC experiments with the ClueWeb09 document collection. We participated in the relevance feedback and web tracks. While our phase 1 relevance feedback run's performance was good, our other relevance feedback and web track submissions' performances were lacking. We suspect this performance difference is caused by the Category B document subset of the ClueWeb09 collection having a higher prior probability of relevance than the rest of the collection. Future work will involve a more detailed error analysis of our experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmuckerCC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmuckerCC09,
		author = {Mark D. Smucker and Charles L. A. Clarke and Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments with ClueWeb09: Relevance Feedback and Web Tracks},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.RF.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmuckerCC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Diversifying Search Results with Popular Subtopics

_Dawei Yin, Zhenzhen Xue, Xiaoguang Qi, Brian D. Davison_

- :fontawesome-solid-user-group: **Participant:** [LU_WUME](./web/participants.md#lu_wume)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/lehighu.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/lehighu.WEB.pdf)
- :material-file-search: **Runs:** [wume1](./web/runs.md#wume1) | [wume2](./web/runs.md#wume2)

??? abstract "Abstract"
	
	This paper describes the method we use in the diversity task of web track in TREC 2009. The problem we aim to solve is the diversification of search results for ambiguous web queries. We present a model based on knowledge of the diversity of query subtopics to generate a diversified ranking for retrieved documents. We expand the original query into several related queries, assuming that query expansions expose subtopics of the original query. Moreover, each query expansion is given a weight which reflects the likelihood of the interpretation (the fraction of users who issued this query given the general query topic). We issue all those expanded queries including the original query to a standard BM25 search engine, then re-rank the retrieved documents to generate the final ranking. Our method can detect possible subtopics of a given query and provide a reasonable ranking that satisfies both relevancy and diversity metrics. The TREC evaluations show our method is effective on the diversity task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YinXQD09.bib) "
	```
	@inproceedings{DBLP:conf/trec/YinXQD09,
		author = {Dawei Yin and Zhenzhen Xue and Xiaoguang Qi and Brian D. Davison},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Diversifying Search Results with Popular Subtopics},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/lehighu.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YinXQD09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Axiomatic Approaches to Information Retrieval–University of Delaware  at TREC 2009 Million Query and Web Tracks

_Wei Zheng, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [EceUdel](./web/participants.md#eceudel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.MQ.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.MQ.WEB.pdf)
- :material-file-search: **Runs:** [UDWAxQEWeb](./web/runs.md#udwaxqeweb) | [UDWAxQE](./web/runs.md#udwaxqe) | [UDWAxBL](./web/runs.md#udwaxbl)

??? abstract "Abstract"
	
	We report our experiments in TREC 2009 Million Query track and Adhoc task of Web track. Our goal is to evaluate the effectiveness of axiomatic retrieval models on the large data collection. Axiomatic approaches to information retrieval have been recently proposed and studied. The basic idea is to search for retrieval functions that can satisfy all the reasonable retrieval constraints. Previous studies showed that the derived basic axiomatic retrieval functions are less sensitive to the parameters than the other state of the art retrieval functions with comparable optimal performance. In this paper, we focus on evaluating the effectiveness of the basic axiomatic retrieval functions as well as the semantic term matching based query expansion strategy. Experiment results of the two tracks demonstrate the effectiveness of the axiomatic retrieval models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengF09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengF09,
		author = {Wei Zheng and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Axiomatic Approaches to Information Retrieval--University of Delaware at {TREC} 2009 Million Query and Web Tracks},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.MQ.WEB.pdf},
		timestamp = {Tue, 20 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengF09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Million Query 

#### Million Query Track 2009 Overview

_Ben Carterette, Virgiliu Pavlu, Hui Fang, Evangelos Kanoulas_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/MQ09OVERVIEW.pdf](http://trec.nist.gov/pubs/trec18/papers/MQ09OVERVIEW.pdf)
??? abstract "Abstract"
	
	The Million Query Track ran for the third time in 2009. The track is designed to serve two purposes: first, it is an exploration of ad hoc retrieval over a large set of queries and a large collection of documents; second, it investigates questions of system evaluation, in particular whether it is better to evaluate using many queries judged shallowly or fewer queries judged thoroughly. Fundamentally, the Million Query tracks (2007-2009) are ad-hoc tasks, only using complex but very efficient evaluation methodologies that allow human assessment effort to be spread on up to 20 times more queries than previous ad-hoc tasks. We estimate metrics like Average Precision fairly well and produce system ranking that (with high confidence) match the true ranking that would be obtained with complete judgments. We can answer budget related questions like how many queries versus how many assessments per query give an optimal strategy; a variance analysis is possible due to the large number of queries involved. While we have confidence we can evaluate participating runs well, an important question is whether the assessments produced by the evaluation process can be reused (together with the collection and the topics) for a new search strategy—that is, one that did not participate in the assessment done by NIST. To answer this, we designed a reusability study which concludes that a variant of participating track systems may be evaluated with reasonably high confidence using the MQ data, while a complete new system cannot. The 2009 track quadrupled the number of queries of previous years from 10,000 to 40,000. In addition, this year saw the introduction of a number of new threads to the basic framework established in the 2007 and 2008 tracks: Queries were classified by the task they represented as well as by their apparent difficulty; Participating sites could choose to do increasing numbers of queries, depending on time and resources available to them; We designed and implemented a novel in situ reusability study. Section 1 describes the tasks for participants. Section 2 provides an overview of the test collection that will result from the track. Section 3 briefly describes the document selection and evaluation methods. Section 4 summarizes the submitted runs. In Section 5 we summarize evaluation results from the task, and Section 6 provides deeper analysis into the results. For TREC 2009, Million Query, Relevance Feedback, and Web track ad-hoc task judging was conducted simultaneously using MQ track methods. A number of compromises had to be made to accomplish this; a note about the usability of the resulting data is included in Section 3.3
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CarterettePFK09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CarterettePFK09,
		author = {Ben Carterette and Virgiliu Pavlu and Hui Fang and Evangelos Kanoulas},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Million Query Track 2009 Overview},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/MQ09OVERVIEW.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CarterettePFK09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad Hoc and Diversity Retrieval at the University of Delaware

_Praveen Chandar, Aparna Kailasam, Divya Muppaneni, Sree Lekha Thota, Ben Carterette_

- :fontawesome-solid-user-group: **Participant:** [UDel](./million-query/participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.WEB.MQ.pdf](http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.WEB.MQ.pdf)
- :material-file-search: **Runs:** [udelIndDM](./million-query/runs.md#udelinddm) | [udelIndri](./million-query/runs.md#udelindri) | [udelIndRM](./million-query/runs.md#udelindrm) | [udelIndSP](./million-query/runs.md#udelindsp) | [udelIndPR](./million-query/runs.md#udelindpr)

??? abstract "Abstract"
	
	This is the report on the University of Delaware Information Retrieval Lab's participation in the TREC 2009 Web and Million Query tracks. Our report on the Relevance Feedback track is in a separate document [3].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChandarKMTC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChandarKMTC09,
		author = {Praveen Chandar and Aparna Kailasam and Divya Muppaneni and Sree Lekha Thota and Ben Carterette},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Ad Hoc and Diversity Retrieval at the University of Delaware},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.WEB.MQ.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChandarKMTC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRRA at TREC 2009: Index Term Weighting Based on Divergence From  Independence Model

_Bekir Taner Dinçer, Ilker Kocabas, Bahar Karaoglan_

- :fontawesome-solid-user-group: **Participant:** [IRRA](./million-query/participants.md#irra)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/muglau.WEB.MQ.pdf](http://trec.nist.gov/pubs/trec18/papers/muglau.WEB.MQ.pdf)
- :material-file-search: **Runs:** [irra1mqd](./million-query/runs.md#irra1mqd) | [irra2mqa](./million-query/runs.md#irra2mqa) | [irra2mqd](./million-query/runs.md#irra2mqd) | [irra1mqa](./million-query/runs.md#irra1mqa) | [irra3mqd](./million-query/runs.md#irra3mqd)

??? abstract "Abstract"
	
	IRRA (IR-Ra) group participated in the 2009 Web track (both adhoc task and diversity task) and the Million Query track. In this year, the major concern is to examine the effectiveness of a novel, nonparametric index term weighting model, divergence from independence (DFI). The notion of independence, which is the notion behind the well-known statistical exploratory data analysis technique called the correspondence analysis (Greenacre, 1984; Jambu, 1991), can be adapted to the index term weighting problem. In this respect, it can be thought of as a qualitative description of the importance of terms for documents, in which they appear, importance in the sense of contribution to the information contents of documents relative to other terms. According to the independence notion, if the ratios of the frequencies of two different terms are the same across documents, they are independent from documents. For example, each Web page contains a pair of “html” and a pair of “body” tags, so that the ratio of frequencies of these tags is the same across all Web pages, indicating that the “html” and “body” tags are independent from Web pages. They are used by design, irrespective of the information contents of Web pages. On the other hand, some tags, such as “image”, “table”, which are also independent from Web pages, may occur less or more in some pages than the expected frequencies suggested by the independence model; so, their associated frequency ratios may not be the same for all Web pages. However, it is reasonable to expect that, if the pages are not about the tags' usage, such as a “HTML Handbook”, frequencies of those tags should not be significantly different from their expected frequencies: they should be close to the expectation, i.e., in a parametric point of view, their observed frequencies on individual documents should be attributed to chance fluctuation. Although this tag example is helpful in exemplifying the use of independence notion, it is obvious that the tags are artificial, and so, governed by some rules completely different from the rules of a spoken language. Nonetheless, some words, like the ones in a common “stopwords list”, appear in documents, not because of their contribution to the information contents of documents, but because of the grammatical rules. On this account, such words can be modeled as if they were tags, because they are independent from documents in the same manner. Their observed frequencies in individual documents is expected to fluctuate around their frequencies expected under independence, as in the case of tags. Content bearing words are, therefore, the words whose frequencies highly diverge from the frequencies expected under independence. The results of the TREC experiments about IRRA runs show that the independence notion promises a natural basis for quantifying the categorical relationships between the terms and the documents. The TERRIER retrieval platform (Ounis et al., 2007) is used to index and search the ClueWeb09-T09B1 data set, a subset of about 50 million Web pages in English (TREC 2009 “Category B” data set). During indexing and searching, terms are stemmed and a particular set of stop words2 are eliminated.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DincerKK09.bib) "
	```
	@inproceedings{DBLP:conf/trec/DincerKK09,
		author = {Bekir Taner Din{\c{c}}er and Ilker Kocabas and Bahar Karaoglan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IRRA} at {TREC} 2009: Index Term Weighting Based on Divergence From Independence Model},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/muglau.WEB.MQ.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DincerKK09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Northeastern University in TREC 2009 Million Query Track

_Evangelos Kanoulas, Keshi Dai, Virgiliu Pavlu, Stefan Savev, Javed A. Aslam_

- :fontawesome-solid-user-group: **Participant:** [NEU](./million-query/participants.md#neu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/northeasternu.MQ.pdf](http://trec.nist.gov/pubs/trec18/papers/northeasternu.MQ.pdf)
- :material-file-search: **Runs:** [NeuSvmBase](./million-query/runs.md#neusvmbase) | [NeuSvmHE](./million-query/runs.md#neusvmhe) | [NeuSvmPR](./million-query/runs.md#neusvmpr) | [NeuSvmPRHE](./million-query/runs.md#neusvmprhe) | [NeuSvmStefan](./million-query/runs.md#neusvmstefan)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KanoulasDPSA09.bib) "
	```
	@inproceedings{DBLP:conf/trec/KanoulasDPSA09,
		author = {Evangelos Kanoulas and Keshi Dai and Virgiliu Pavlu and Stefan Savev and Javed A. Aslam},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Northeastern University in {TREC} 2009 Million Query Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/northeasternu.MQ.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KanoulasDPSA09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Study of Term Proximity and Document Weighting Normalization in  Pseudo Relevance Feedback–UIUC at TREC 2009 Million Query Track

_Yuanhua Lv, Jing He, V. G. Vinod Vydiswaran, Kavita Ganesan, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [UIUC](./million-query/participants.md#uiuc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uiuc.MQ.pdf](http://trec.nist.gov/pubs/trec18/papers/uiuc.MQ.pdf)
- :material-file-search: **Runs:** [uiuc09KL](./million-query/runs.md#uiuc09kl) | [uiuc09RegQL](./million-query/runs.md#uiuc09regql) | [uiuc09GProx](./million-query/runs.md#uiuc09gprox) | [uiuc09MProx](./million-query/runs.md#uiuc09mprox) | [uiuc09Adpt](./million-query/runs.md#uiuc09adpt)

??? abstract "Abstract"
	
	In this paper, we report our experiments in the TREC 2009 Million Query Track. Our first line of study is on proximity-based feedback, in which we propose a positional relevance model (PRM) to exploit term proximity evidence so as to assign more weights to expansion words that are closer to query words in feedback documents. The second line of study is to improve the weighting of feedback documents in the relevance model by using a regression-based method to approximate the probability of relevance (and thus the name RegRM). In the third line of study, we test a supervised approach for query classification. Besides, we also evaluate a selective pseudo feedback strategy which stops pseudo feedback for precision-oriented queries and only uses it for recall-oriented ones. The proposed PRM has shown clear improvements over the relevance model for pseudo feedback, suggesting that capturing the term proximity heuristic appropriately could lead to a better feedback model. RegRM performs as well as relevance model, but no noticeable improvement is observed. Unfortunately, the proposed query classification methods appear to not work well. The results also show that the proposed selective pseudo feedback may not work well, since precision-oriented queries can also benefit from pseudo feedback, though not as much as recall-oriented queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LvHVGZ09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LvHVGZ09,
		author = {Yuanhua Lv and Jing He and V. G. Vinod Vydiswaran and Kavita Ganesan and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Study of Term Proximity and Document Weighting Normalization in Pseudo Relevance Feedback--UIUC at {TREC} 2009 Million Query Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uiuc.MQ.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LvHVGZ09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2009: Experiments with Terrier

_Richard McCreadie, Craig Macdonald, Iadh Ounis, Jie Peng, Rodrygo L. T. Santos_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./million-query/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf)
- :material-file-search: **Runs:** [uogTRMQdph40](./million-query/runs.md#uogtrmqdph40) | [uogTRMQdpA10](./million-query/runs.md#uogtrmqdpa10)

??? abstract "Abstract"
	
	In TREC 2009, we extend our Voting Model for the faceted blog distillation, top stories identification, and related entity finding tasks. Moreover, we experiment with our novel xQuAD framework for search result diversification. Besides fostering our research in multiple directions, by participating in such a wide portfolio of tracks, we further develop the indexing and retrieval capabilities of our Terrier Information Retrieval platform, to effectively and efficiently cope with a new generation of large-scale test collections.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieMOPS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieMOPS09,
		author = {Richard McCreadie and Craig Macdonald and Iadh Ounis and Jie Peng and Rodrygo L. T. Santos},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2009: Experiments with Terrier},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieMOPS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIIT Hyderabad at Million Query Track TREC 2009

_Prashant Ullegaddi, Sudip Datta, Vinay Pande, Kushal S. Dave, Vasudeva Varma_

- :fontawesome-solid-user-group: **Participant:** [SIEL](./million-query/participants.md#siel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/iiit-hyderabad.MQ.pdf](http://trec.nist.gov/pubs/trec18/papers/iiit-hyderabad.MQ.pdf)
- :material-file-search: **Runs:** [iiithAuthPN](./million-query/runs.md#iiithauthpn) | [iiithAuEQ](./million-query/runs.md#iiithaueq) | [iiithExpQry](./million-query/runs.md#iiithexpqry)

??? abstract "Abstract"
	
	This was our maiden attempt at Million Query track, TREC 2009. We submitted three runs for ad-hoc retrieval task in Million Query track. We explored ad-hoc retrieval of web pages using Hadoop—a distributed infrastructure. To enhance recall, we expanded the queries using WordNet and also by combining the query with all possible subsets of tokens present in the query. To prevent query drift we experimented on giving selective boosts to different steps of expansion including giving higher boosts to sub-queries containing named entities as opposed to those that did not. In fact, this run achieved highest precision among our other runs. Using simple statistics we identified authoritative domains such as wikipedia.org, answers.com, etc and attempted to boost hits from them, while preventing them from overly biasing the results. An attempt to query classification was also made.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/UllegaddiDPDV09.bib) "
	```
	@inproceedings{DBLP:conf/trec/UllegaddiDPDV09,
		author = {Prashant Ullegaddi and Sudip Datta and Vinay Pande and Kushal S. Dave and Vasudeva Varma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IIIT} Hyderabad at Million Query Track {TREC} 2009},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/iiit-hyderabad.MQ.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/UllegaddiDPDV09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Axiomatic Approaches to Information Retrieval–University of Delaware  at TREC 2009 Million Query and Web Tracks

_Wei Zheng, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [EceUdel](./million-query/participants.md#eceudel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.MQ.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.MQ.WEB.pdf)
- :material-file-search: **Runs:** [UDMQAxQEWeb](./million-query/runs.md#udmqaxqeweb) | [UDMQAxQE](./million-query/runs.md#udmqaxqe) | [UDMQAxBL](./million-query/runs.md#udmqaxbl) | [UDMQAxQEWP](./million-query/runs.md#udmqaxqewp) | [UDMQAxBLlink](./million-query/runs.md#udmqaxbllink)

??? abstract "Abstract"
	
	We report our experiments in TREC 2009 Million Query track and Adhoc task of Web track. Our goal is to evaluate the effectiveness of axiomatic retrieval models on the large data collection. Axiomatic approaches to information retrieval have been recently proposed and studied. The basic idea is to search for retrieval functions that can satisfy all the reasonable retrieval constraints. Previous studies showed that the derived basic axiomatic retrieval functions are less sensitive to the parameters than the other state of the art retrieval functions with comparable optimal performance. In this paper, we focus on evaluating the effectiveness of the basic axiomatic retrieval functions as well as the semantic term matching based query expansion strategy. Experiment results of the two tracks demonstrate the effectiveness of the axiomatic retrieval models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengF09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengF09,
		author = {Wei Zheng and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Axiomatic Approaches to Information Retrieval--University of Delaware at {TREC} 2009 Million Query and Web Tracks},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.MQ.WEB.pdf},
		timestamp = {Tue, 20 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengF09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Blog 

#### Overview of the TREC 2009 Blog Track

_Craig Macdonald, Iadh Ounis, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/BLOG09.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec18/papers/BLOG09.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The Blog track explores the information seeking behaviour in the blogosphere. Thus far, since its inception in 2006 [9], the Blog track addressed two main search tasks based on the analysis of a commercial blog search engine: the opinion-finding task (i.e. “What do people think about X?”) and the blog distillation task (i.e. “Find me a blog with a principal, recurring interest in X.”). In TREC 2009, the Blog track has been markedly revamped with the use of a new and larger sample of the blogosphere, called Blogs08, which has a 13-month timespan covering a period ranging from 14th January 2008 to 10th February 2009, and the introduction of two new search tasks, addressing more refined and typical search scenarios on the blogosphere: Faceted blog distillation: A more refined version of the blog distillation task, addressing the quality aspect of the retrieved blogs. Top stories identification: A task that addresses news-related issues on the blogosphere. Most of the efforts of the organisers in the Blog track 2009 have been spent on defining the new search tasks, on building a suitable infrastructure to support the investigation of the introduced search tasks, and on establishing an appropriate methodology to evaluate the effectiveness of the submitted runs. The remainder of this paper is structured as follows. Section 2 describes the newly created Blogs08 collection. Section 3 describes the new faceted blog distillation task, and discusses the main obtained results by the participating groups. Section 4 describes the top stories identification task, and summarises the results of the runs and the main effective approaches deployed by the participating groups. Concluding remarks are provided in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacdonaldOS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacdonaldOS09,
		author = {Craig Macdonald and Iadh Ounis and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2009 Blog Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/BLOG09.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacdonaldOS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BRAT: A Random Walk Through the Semantic Spaces of the Blogosphere

_Adil El Ghali, Yann Vigile Hoareau_

- :fontawesome-solid-user-group: **Participant:** [shakwat](./blog/participants.md#shakwat)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uparis.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/uparis.BLOG.pdf)
- :material-file-search: **Runs:** [ri2049rw3](./blog/runs.md#ri2049rw3) | [ri1025rw2b](./blog/runs.md#ri1025rw2b) | [ri1025rw5h2b](./blog/runs.md#ri1025rw5h2b) | [ri1025rw5432](./blog/runs.md#ri1025rw5432)

??? abstract "Abstract"
	
	Semantic spaces, such as the Latent Semantic Analysis (LSA), Hyperspace Ana- log to Language (HAL) or Random Indexing (RI), offer convenient methods to represent semantic relations between words and concepts, abstracted from a distribution of documents. The distribution of documents determines the local co-occurrence pattern between words all over the corpus and, then, determines the semantic abstracted from the local distribution. Such methods are sensitive to the statistical properties on the distribution of words over documents. For instance, the semantic on the word table abstracted from a scientific corpus or a general corpus may be different. In the first case, since table may occur in the context of table of correlation or table of results, it would be considered to be associated to the word correlation whereas in the second case, because it may co-occur with kitchen or living-room, it would rather be considered as similar to chair. Nevertheless, the formal relation bearing the properties of the distribution of word's co-occurence and the final semantic produced by Semantic space methods have not been described until now. In the case of a mixed “scientific and general” corpus, what makes that the semantic of table became more similar to chair than Speerman and vice-versa? We approached the Top-stories task of the Blog-Track'09 using a system named Blogosphere Random Analysis using Texts (BRAT) composed of two layers. The first layer distributes and represents blogs posts' in different semantic spaces built using Random Indexing. The second layer is an algorithm of retrieval that have the aim of navigate in the semantic space via a ramdom walk. BRAT have been constructed under two main working hypothesis that we considered important for dealing with the semantic of the blogosphere: the notion of semantic identity and the notion of semantic pollution. The article is organized as follows. In a first part, we shortly overview the methods and properties of semantic spaces models. The notions of semantic identity and semantic pollution are described in general together with their practical implication within the Top-stories task. In the second part, the BRAT system is described. The third part gives an overview of the performances of BRAT for the Top-stories task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GhaliH09.bib) "
	```
	@inproceedings{DBLP:conf/trec/GhaliH09,
		author = {Adil El Ghali and Yann Vigile Hoareau},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{BRAT:} {A} Random Walk Through the Semantic Spaces of the Blogosphere},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uparis.BLOG.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GhaliH09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BIT at TREC 2009 Faceted Blog Distillation Task

_Peng Jiang, Qing Yang, Chunxia Zhang, Zhendong Niu_

- :fontawesome-solid-user-group: **Participant:** [BIT](./blog/participants.md#bit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/bit.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/bit.BLOG.pdf)
- :material-file-search: **Runs:** [BIT09PH](./blog/runs.md#bit09ph) | [BIT09P](./blog/runs.md#bit09p)

??? abstract "Abstract"
	
	This Paper presents the work done for the TREC 2009 faceted blog distillation task of blog track. In our approach, we use a mixture of language models based on global representation. Our model can be regarded as a combination of topic relevance model and faceted relevance model. By pseudo-relevance feedback method, we can estimate the above two models from topic relevance feedback documents and facet relevance feedback documents respectively. Experimental results on TREC blogs08 collection show the effectiveness of our proposed approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangYZN09.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangYZN09,
		author = {Peng Jiang and Qing Yang and Chunxia Zhang and Zhendong Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{BIT} at {TREC} 2009 Faceted Blog Distillation Task},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/bit.BLOG.pdf},
		timestamp = {Fri, 04 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JiangYZN09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Lugano at TREC 2009 Blog Track

_Mostafa Keikha, Mark James Carman, Robert Gwadera, Shima Gerani, Ilya Markov, Giacomo Inches, Az Azrinudin Alidin, Fabio Crestani_

- :fontawesome-solid-user-group: **Participant:** [USI](./blog/participants.md#usi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ulugano.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/ulugano.BLOG.pdf)
- :material-file-search: **Runs:** [OWA](./blog/runs.md#owa) | [regularized](./blog/runs.md#regularized) | [combined](./blog/runs.md#combined) | [runtag](./blog/runs.md#runtag) | [RegLDM](./blog/runs.md#regldm)

??? abstract "Abstract"
	
	We report on the University of Lugano's participation in the Blog track of TREC 2009. In particular we describe our system for performing blog distillation, faceted search and top stories identification.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KeikhaCGGMIAC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/KeikhaCGGMIAC09,
		author = {Mostafa Keikha and Mark James Carman and Robert Gwadera and Shima Gerani and Ilya Markov and Giacomo Inches and Az Azrinudin Alidin and Fabio Crestani},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Lugano at {TREC} 2009 Blog Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ulugano.BLOG.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KeikhaCGGMIAC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### POSTECH at TREC 2009 Blog Track: Top Stories Identification

_Yeha Lee, Hun-Young Jung, Woosang Song, Jong-Hyeok Lee_

- :fontawesome-solid-user-group: **Participant:** [POSTECH_KLE](./blog/participants.md#postech_kle)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/postech-kle.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/postech-kle.BLOG.pdf)
- :material-file-search: **Runs:** [KLEFeedPrior](./blog/runs.md#klefeedprior) | [KLEFeed](./blog/runs.md#klefeed) | [KLEClusPrior](./blog/runs.md#kleclusprior) | [KLECluster](./blog/runs.md#klecluster)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2009 Blog Track. Our system consists of the query likelihood component and the news headline prior component, based on the language model framework. For the query likelihood, we propose several approaches to estimate the query language model and the news headline language model. We also suggest two approaches to choose the 10 supporting relevant posts: Feed-Based Selection and Cluster-Based Selection. Furthermore, we propose two criteria to estimate the news headline prior for a given day. Experimental results show that using the prior significantly improves the performance of the task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeJSL09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeJSL09,
		author = {Yeha Lee and Hun{-}Young Jung and Woosang Song and Jong{-}Hyeok Lee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{POSTECH} at {TREC} 2009 Blog Track: Top Stories Identification},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/postech-kle.BLOG.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeJSL09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Facet Classification of Blogs: Know-Center at the TREC 2009 Blog  Distillation Task

_Elisabeth Lex, Michael Granitzer, Andreas Juffinger_

- :fontawesome-solid-user-group: **Participant:** [knowcenter](./blog/participants.md#knowcenter)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/know-center.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/know-center.BLOG.pdf)
- :material-file-search: **Runs:** [nounfull](./blog/runs.md#nounfull) | [punctfull](./blog/runs.md#punctfull) | [sentence](./blog/runs.md#sentence)

??? abstract "Abstract"
	
	In this paper, we outline our experiments carried out at the TREC 2009 Blog Distillation Task. Our system is based on a plain text index extracted from the XML feeds of the TREC Blogs08 dataset. This index was used to retrieve candidate blogs for the given topics. The resulting blogs were classified using a Support Vector Machine that was trained on a manually labelled subset of the TREC Blogs08 dataset. Our experiments included three runs on different features: firstly on nouns, secondly on stylometric properties, and thirdly on punctuation statistics. The facet identification based on our approach was successful, although a significant number of candidate blogs were not retrieved at all.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LexGJ09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LexGJ09,
		author = {Elisabeth Lex and Michael Granitzer and Andreas Juffinger},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Facet Classification of Blogs: Know-Center at the {TREC} 2009 Blog Distillation Task},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/know-center.BLOG.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LexGJ09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Study of Faceted Blog Distillation–PRIS at TREC 2009 Blog Track

_Si Li, Huiji Gao, Hao Sun, Fei Chen, Oupeng Feng, Sanyuan Gao, Hao Zhang, Xinsheng Li, Caili Tan, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [buptpris___2009](./blog/participants.md#buptpris___2009)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/pris.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/pris.BLOG.pdf)
- :material-file-search: **Runs:** [prisb](./blog/runs.md#prisb) | [pris](./blog/runs.md#pris)

??? abstract "Abstract"
	
	This paper describes BUPT (pris) participation in faceted blog distillation task at Blog Track 2009. The system adopts a two-stage strategy in faceted blog distillation task. In the first stage, the system carries out a basic topic relevance retrieval to get the top k blogs for each query. In the second stage, different models are designed to judge the facets and ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiGSCFGZLTXCG09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiGSCFGZLTXCG09,
		author = {Si Li and Huiji Gao and Hao Sun and Fei Chen and Oupeng Feng and Sanyuan Gao and Hao Zhang and Xinsheng Li and Caili Tan and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Study of Faceted Blog Distillation--PRIS at {TREC} 2009 Blog Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/pris.BLOG.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiGSCFGZLTXCG09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2009: Experiments with Terrier

_Richard McCreadie, Craig Macdonald, Iadh Ounis, Jie Peng, Rodrygo L. T. Santos_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./blog/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf)
- :material-file-search: **Runs:** [uogTrTSbmmr](./blog/runs.md#uogtrtsbmmr) | [uogTrTSemmrs](./blog/runs.md#uogtrtsemmrs) | [uogTrTSwtime](./blog/runs.md#uogtrtswtime) | [uogTrTStimes](./blog/runs.md#uogtrtstimes) | [uogTrFBNclas](./blog/runs.md#uogtrfbnclas) | [uogTrFBMclas](./blog/runs.md#uogtrfbmclas) | [uogTrFBAlr](./blog/runs.md#uogtrfbalr) | [uogTrFBHlr](./blog/runs.md#uogtrfbhlr)

??? abstract "Abstract"
	
	In TREC 2009, we extend our Voting Model for the faceted blog distillation, top stories identification, and related entity finding tasks. Moreover, we experiment with our novel xQuAD framework for search result diversification. Besides fostering our research in multiple directions, by participating in such a wide portfolio of tracks, we further develop the indexing and retrieval capabilities of our Terrier Information Retrieval platform, to effectively and efficiently cope with a new generation of large-scale test collections.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieMOPS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieMOPS09,
		author = {Richard McCreadie and Craig Macdonald and Iadh Ounis and Jie Peng and Rodrygo L. T. Santos},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2009: Experiments with Terrier},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieMOPS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC Blog and TREC Chem: A View from the Corn Fields

_Yelena Mejova, Viet Ha-Thuc, Steven Foster, Christopher G. Harris, Robert J. Arens, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [IowaS](./blog/participants.md#iowas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uiowa.BLOG.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/uiowa.BLOG.CHEM.pdf)
- :material-file-search: **Runs:** [IowaSBT0901](./blog/runs.md#iowasbt0901) | [IowaSBT0902](./blog/runs.md#iowasbt0902) | [IowaSBT0903](./blog/runs.md#iowasbt0903) | [IowaSBT0904](./blog/runs.md#iowasbt0904) | [IowaSBD0901](./blog/runs.md#iowasbd0901) | [IowaSBD0902](./blog/runs.md#iowasbd0902)

??? abstract "Abstract"
	
	The University of Iowa Team, participated in the blog track and the chemistry track of TREC-2009. This is our first year participating in the blog track as well as the chemistry track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MejovaHFHAS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/MejovaHFHAS09,
		author = {Yelena Mejova and Viet Ha{-}Thuc and Steven Foster and Christopher G. Harris and Robert J. Arens and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} Blog and {TREC} Chem: {A} View from the Corn Fields},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uiowa.BLOG.CHEM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MejovaHFHAS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FEUP at TREC 2009 Blog Track: Temporal Evidence in the Faceted  Blog Distillation Task

_Sérgio Nunes, Cristina Ribeiro, Gabriel David_

- :fontawesome-solid-user-group: **Participant:** [FEUP](./blog/participants.md#feup)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/feup.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/feup.BLOG.pdf)
- :material-file-search: **Runs:** [FEUPirlab1](./blog/runs.md#feupirlab1) | [FEUPirlab2](./blog/runs.md#feupirlab2) | [FEUPirlab3](./blog/runs.md#feupirlab3) | [FEUPirlab4](./blog/runs.md#feupirlab4)

??? abstract "Abstract"
	
	This paper describes the participation of FEUP, from the University of Porto, in the TREC 2009 Blog Track. FEUP participated in the faceted blog distillation task with work focused on the use of temporal features available in the new TREC Blogs08 collection. The approach presented in this paper uses the temporal information available in most individual posts to amplify (or reduce) each post's score. Blog scores, and subsequent ranks, are obtained by combining individual posts' scores. While preparing the runs, no endeavors were made to identify a priori any temporal differences between the three distinct facets.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NunesRD09.bib) "
	```
	@inproceedings{DBLP:conf/trec/NunesRD09,
		author = {S{\'{e}}rgio Nunes and Cristina Ribeiro and Gabriel David},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FEUP} at {TREC} 2009 Blog Track: Temporal Evidence in the Faceted Blog Distillation Task},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/feup.BLOG.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NunesRD09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### From Blogs to News: Identifying Hot Topics in the Blogosphere

_Wouter Weerkamp, Manos Tsagkias, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [UAms](./blog/participants.md#uams)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.BLOG.pdf)
- :material-file-search: **Runs:** [IlpsTSExP](./blog/runs.md#ilpstsexp) | [IlpsTSExT](./blog/runs.md#ilpstsext) | [IlpsTSHlP](./blog/runs.md#ilpstshlp) | [IlpsTSHlT](./blog/runs.md#ilpstshlt) | [IlpsBDm2T](./blog/runs.md#ilpsbdm2t) | [IlpsBDmxT](./blog/runs.md#ilpsbdmxt) | [IlpsBDmxfT](./blog/runs.md#ilpsbdmxft) | [IlpsBDm1T](./blog/runs.md#ilpsbdm1t)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdam's ILPS group in the blog track at TREC 2009. We focus on the top stories identification task, and take an approach that does not require the headlines of top stories to be known beforehand. We explore the feasibility of a so-called blogs to news approach: given a date and a set of blog posts, identify the main topics for that date. This approach is more general than just finding top stories, but it can still be applied to the task of headline ranking. Results show that this general approach, applied to the task at hand, is among the top performing approaches in this year's TREC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WeerkampTR09.bib) "
	```
	@inproceedings{DBLP:conf/trec/WeerkampTR09,
		author = {Wouter Weerkamp and Manos Tsagkias and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {From Blogs to News: Identifying Hot Topics in the Blogosphere},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.BLOG.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WeerkampTR09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Blog Track TREC 2009

_Xueke Xu, Yue Liu, Hongbo Xu, Xiaoming Yu, Linhai Song, Feng Guan, Zeying Peng, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./blog/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ictnet.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/ictnet.BLOG.pdf)
- :material-file-search: **Runs:** [ICTNETTSRun3](./blog/runs.md#ictnettsrun3) | [ICTNETTSRun2](./blog/runs.md#ictnettsrun2) | [ICTNETTSRun4](./blog/runs.md#ictnettsrun4) | [ICTNETTSRun1](./blog/runs.md#ictnettsrun1) | [ICTNETBDRUN3](./blog/runs.md#ictnetbdrun3) | [ICTNETBDRUN2](./blog/runs.md#ictnetbdrun2) | [ICTNETBDRUN1](./blog/runs.md#ictnetbdrun1) | [ICTNETBDRUN4](./blog/runs.md#ictnetbdrun4)

??? abstract "Abstract"
	
	This paper describes our participation in blog track of TREC2009. All runs are submitted for both two task, namely Top stories identification task and faceted blog distillation task. The “FirteX” platform was used to index and retrieval posts. As for top stories identification task, to identify important headlines, we measure the importance of headline by accumulating the BM25 relevance score with posts on the query day. We propose a graph-based iterative approach and a sub-topic detecting based approach respectively to identify diverse blog posts. As for faceted blog distillation task: we adopt a very straightforward approach and measure the topical relevance by only exploiting top ad-hoc 10000 posts. To identify facet inclination, we either train centroid classifier or compute facet inclination weights of terms to compute facet inclination score and rerank feed by combining relevance score and facet inclination score.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuLXYSGPC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuLXYSGPC09,
		author = {Xueke Xu and Yue Liu and Hongbo Xu and Xiaoming Yu and Linhai Song and Feng Guan and Zeying Peng and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Blog Track {TREC} 2009},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ictnet.BLOG.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuLXYSGPC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Entity 

#### Overview of the TREC 2009 Entity Track

_Krisztian Balog, Arjen P. de Vries, Pavel Serdyukov, Paul Thomas, Thijs Westerveld_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ENT09.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec18/papers/ENT09.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The goal of the entity track is to perform entity-oriented search tasks on the World Wide Web. Many user information needs would be better answered by specific entities instead of just any type of documents. The track defines entities as “typed search results,” “things,” represented by their homepages on the web. Searching for entities thus corresponds to ranking these homepages. The track thereby investigates a problem quite similar to the QA list task. In this pilot year, we limited the track's scope to searches for instances of the organizations, people, and product entity types.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BalogVSTW09.bib) "
	```
	@inproceedings{DBLP:conf/trec/BalogVSTW09,
		author = {Krisztian Balog and Arjen P. de Vries and Pavel Serdyukov and Paul Thomas and Thijs Westerveld},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2009 Entity Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ENT09.OVERVIEW.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BalogVSTW09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Related Entity Finding Based on Co-Occurance

_Marc Bron, Krisztian Balog, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [UAms](./entity/participants.md#uams)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.ENT.pdf)
- :material-file-search: **Runs:** [ilpsEntem](./entity/runs.md#ilpsentem) | [ilpsEntBL](./entity/runs.md#ilpsentbl) | [ilpsEntcr](./entity/runs.md#ilpsentcr) | [ilpsEntcf](./entity/runs.md#ilpsentcf)

??? abstract "Abstract"
	
	We report on experiments for the Related Entity Finding task in which we focus on only using Wikipedia as a target corpus in which to identify (related) entitities. Our approach is based on co-occurrences between the source entity and potential target entities. We observe improvements in performance when a context-independent co-occurrence model is combined with context-dependent co-occurrence models in which we stress the importance of the expected relation between source and target entity. Applying type filtering yields further improvements results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BronBR09.bib) "
	```
	@inproceedings{DBLP:conf/trec/BronBR09,
		author = {Marc Bron and Krisztian Balog and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Related Entity Finding Based on Co-Occurance},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.ENT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BronBR09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Entity Retrieval with Hierarchical Relevance Model, Exploiting the  Structure of Tables and Learning Homepage Classifiers

_Yi Fang, Luo Si, Zhengtao Yu, Yantuan Xian, Yangbo Xu_

- :fontawesome-solid-user-group: **Participant:** [Purdue_Si](./entity/participants.md#purdue_si)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/purdue.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/purdue.ENT.pdf)
- :material-file-search: **Runs:** [KMR2PU](./entity/runs.md#kmr2pu) | [KMR1PU](./entity/runs.md#kmr1pu) | [KMR3PU](./entity/runs.md#kmr3pu)

??? abstract "Abstract"
	
	This paper gives an overview of our work done for the TREC 2009 Entity track. We propose a hierarchical relevance retrieval model for entity ranking. In this model, three levels of relevance are examined which are document, passage and entity, respectively. The final ranking score is a linear combination of the relevance scores from the three levels. Furthermore, we exploit the structure of tables and lists to identify the target entities from them by making a joint decision on all the entities with the same attribute. To find entity homepages, we train logistic regression models for each type of entities. A set of templates and filtering rules are also used to identify target entities. The key lessons that we learned by participating this year's Entity track include: 1) our special treatment of table and list data is well rewarding; 2) The high accuracy of homepage finding is crucial in this track; 3) Wikipedia can serve as a valuable knowledge resource for different aspects of the related entity finding task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FangSYXX09.bib) "
	```
	@inproceedings{DBLP:conf/trec/FangSYXX09,
		author = {Yi Fang and Luo Si and Zhengtao Yu and Yantuan Xian and Yangbo Xu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Entity Retrieval with Hierarchical Relevance Model, Exploiting the Structure of Tables and Learning Homepage Classifiers},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/purdue.ENT.pdf},
		timestamp = {Tue, 17 May 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FangSYXX09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Result Diversity and Entity Ranking Experiments: Anchors, Links, Text  and Wikipedia

_Rianne Kaptein, Marijn Koolen, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [Amsterdam](./entity/participants.md#amsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uamsterdam-kamps.ENT.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uamsterdam-kamps.ENT.WEB.pdf)
- :material-file-search: **Runs:** [basewikirun](./entity/runs.md#basewikirun) | [UAmsER09Co](./entity/runs.md#uamser09co) | [UAmsER09Ab1](./entity/runs.md#uamser09ab1) | [wikiruncats](./entity/runs.md#wikiruncats)

??? abstract "Abstract"
	
	In this paper, we document our efforts in participating to the TREC 2009 Entity Ranking and Web Tracks. We had multiple aims: For the Web Track's Adhoc task we experiment with document text and anchor text representation, and the use of the link structure. For the Web Track's Diversity task we experiment with using a top down sliding window that, given the top ranked documents, chooses as the next ranked document the one that has the most unique terms or links. We test our sliding window method on a standard document text index and an index of propagated anchor texts. We also experiment with extreme query expansions by taking the top n results of the initial ranking as multi-faceted aspects of the topic to construct n relevance models to obtain n sets of results. A final diverse set of results is obtained by merging the n results lists. For the Entity Ranking Track, we also explore the effectiveness of the anchor text representation, look at the co-citation graph, and experiment with using Wikipedia as a pivot. Our main findings can be summarized as follows: Anchor text is very effective for diversity. It gives high early precision and the results cover more relevant sub-topics than the document text index. Our baseline runs have low diversity, which limits the possible impact of the sliding window approach. New link information seems more effective for diversifying text-based search results than the amount of unique terms added by a document. In the entity ranking task, anchor text finds few primary pages , but it does retrieve a large number of relevant pages. Using Wikipedia as a pivot results in large gains of P10 and NDCG when only primary pages are considered. Although the links between the Wikipedia entities and pages in the Clueweb collection are sparse, the precision of the existing links is very high.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KapteinKK09.bib) "
	```
	@inproceedings{DBLP:conf/trec/KapteinKK09,
		author = {Rianne Kaptein and Marijn Koolen and Jaap Kamps},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Result Diversity and Entity Ranking Experiments: Anchors, Links, Text and Wikipedia},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uamsterdam-kamps.ENT.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KapteinKK09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2009: Experiments with Terrier

_Richard McCreadie, Craig Macdonald, Iadh Ounis, Jie Peng, Rodrygo L. T. Santos_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./entity/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf)
- :material-file-search: **Runs:** [uogTrEbl](./entity/runs.md#uogtrebl) | [uogTrEc3](./entity/runs.md#uogtrec3) | [uogTrEpr](./entity/runs.md#uogtrepr) | [uogTrEdi](./entity/runs.md#uogtredi)

??? abstract "Abstract"
	
	In TREC 2009, we extend our Voting Model for the faceted blog distillation, top stories identification, and related entity finding tasks. Moreover, we experiment with our novel xQuAD framework for search result diversification. Besides fostering our research in multiple directions, by participating in such a wide portfolio of tracks, we further develop the indexing and retrieval capabilities of our Terrier Information Retrieval platform, to effectively and efficiently cope with a new generation of large-scale test collections.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieMOPS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieMOPS09,
		author = {Richard McCreadie and Craig Macdonald and Iadh Ounis and Jie Peng and Rodrygo L. T. Santos},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2009: Experiments with Terrier},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieMOPS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Journey in Entity Related Retrieval for TREC 2009

_Jagadish Pamarthi, GuangXu Zhou, Coskun Bayrak_

- :fontawesome-solid-user-group: **Participant:** [UALR_CB](./entity/participants.md#ualr_cb)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uarkansas-lr.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/uarkansas-lr.ENT.pdf)
- :material-file-search: **Runs:** [UALRCB09r4](./entity/runs.md#ualrcb09r4) | [UALRCB09r1](./entity/runs.md#ualrcb09r1) | [UALRCB09r2](./entity/runs.md#ualrcb09r2) | [UALRCB09r3](./entity/runs.md#ualrcb09r3)

??? abstract "Abstract"
	
	The focus of this paper is to present the results obtained as a result of performing entity information retrieval, namely the home pages of products, organizations and persons. The preliminary results, based on the Indri Search Engine, of this study and experimentation were presented at the Entity Track in TREC 2009. Indri Search Engine is an efficient and effective open source tool, which is operated by indri query language in any windows or UNIX based platform. Indri is based on the inference network framework and supports structured queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PamarthiZB09.bib) "
	```
	@inproceedings{DBLP:conf/trec/PamarthiZB09,
		author = {Jagadish Pamarthi and GuangXu Zhou and Coskun Bayrak},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Journey in Entity Related Retrieval for {TREC} 2009},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uarkansas-lr.ENT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PamarthiZB09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Delft University at the TREC 2009 Entity Track: Ranking Wikipedia  Entities

_Pavel Serdyukov, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [tudelft](./entity/participants.md#tudelft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/delft.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/delft.ENT.pdf)
- :material-file-search: **Runs:** [tudpw](./entity/runs.md#tudpw) | [tudpwkntop](./entity/runs.md#tudpwkntop) | [tudwtop](./entity/runs.md#tudwtop) | [tudwebtop](./entity/runs.md#tudwebtop)

??? abstract "Abstract"
	
	This paper describes the details of our participation in Entity track of the TREC 2009.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SerdyukovV09.bib) "
	```
	@inproceedings{DBLP:conf/trec/SerdyukovV09,
		author = {Pavel Serdyukov and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Delft University at the {TREC} 2009 Entity Track: Ranking Wikipedia Entities},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/delft.ENT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SerdyukovV09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Finding Related Entities by Retrieving Relations: UIUC at TREC  2009 Entity Track

_V. G. Vinod Vydiswaran, Kavita Ganesan, Yuanhua Lv, Jing He, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [UIUC](./entity/participants.md#uiuc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uiuc.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/uiuc.ENT.pdf)
- :material-file-search: **Runs:** [UIqryForm](./entity/runs.md#uiqryform) | [UIqryForm3](./entity/runs.md#uiqryform3) | [UIauto](./entity/runs.md#uiauto)

??? abstract "Abstract"
	
	Our goal in participating in the TREC 2009 Entity Track was to study whether relation extraction techniques can help in improving accuracy of the entity finding task. Finding related entities is informational in nature and we wanted to explore if inducing structure on the queries helps satisfy this information need. The research outlook we took was to study techniques that retrieve relations between two entities from a large corpus, and from those, find the most relevant entities that participate in the given relation with another given entity. Instead of aiming at retrieving pages about specific entities, we tried to address the problem of directly finding the entities from the text. Our experimental results show that we were able to find many related entities using relation-based extraction, and ranking entities based on further evidence from the text helps to a certain extent.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VydiswaranGLHZ09.bib) "
	```
	@inproceedings{DBLP:conf/trec/VydiswaranGLHZ09,
		author = {V. G. Vinod Vydiswaran and Kavita Ganesan and Yuanhua Lv and Jing He and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Finding Related Entities by Retrieving Relations: {UIUC} at {TREC} 2009 Entity Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uiuc.ENT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VydiswaranGLHZ09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BUPT at TREC 2009: Entity Track

_Zhanyi Wang, Dong-xin Liu, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [buptpris___2009](./entity/participants.md#buptpris___2009)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/bupt.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/bupt.ENT.pdf)
- :material-file-search: **Runs:** [PRIS1](./entity/runs.md#pris1) | [PRIS2](./entity/runs.md#pris2) | [PRIS3](./entity/runs.md#pris3) | [PRIS4](./entity/runs.md#pris4)

??? abstract "Abstract"
	
	This report introduces the work of BUPT (PRIS) in Entity Track in TREC2009. The task and data are both new this year. In our work, an improved two-stage retrieval model is proposed according to the task. The first stage is document retrieval, in order to get the similarity of the query and documents. The second stage is to find the relationship between documents and entities. We also focus on entity extraction in the second stage and the final ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangLXCG09.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangLXCG09,
		author = {Zhanyi Wang and Dong{-}xin Liu and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{BUPT} at {TREC} 2009: Entity Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/bupt.ENT.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangLXCG09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NiCT at TREC 2009: Employing Three Models for Entity Ranking Track

_Youzheng Wu, Hideki Kashioka_

- :fontawesome-solid-user-group: **Participant:** [NiCT](./entity/participants.md#nict)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/nict.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/nict.ENT.pdf)
- :material-file-search: **Runs:** [NiCTm2](./entity/runs.md#nictm2) | [NiCTm1](./entity/runs.md#nictm1) | [NiCTm3](./entity/runs.md#nictm3) | [NiCTm4](./entity/runs.md#nictm4)

??? abstract "Abstract"
	
	This paper describes experiments carried out at NiCT for the TREC 2009 Entity Ranking track. Our main study is to develop an effective approach to rank entities via measuring the “similarities” between supporting snippets of entities and input query. Three models are implemented to this end. 1) The DLM regards entity ranking as a task of calculating the probabilities of generating input query given supporting snippets of entities via language model. 2) The RSVM ranks entities via a supervised Ranking SVM. 3) The CSVM, an unsupervised model, ranks entities according to the probabilities of input query belonging to topics represented by entities and their supporting snippets via SVM classifier. The evaluation shows that the DLM is the best on P@10, while the RSVM outperforms the others on nDCG.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuK09.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuK09,
		author = {Youzheng Wu and Hideki Kashioka},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {NiCT at {TREC} 2009: Employing Three Models for Entity Ranking Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/nict.ENT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuK09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments on Related Entity Finding Track at TREC 2009

_Qing Yang, Peng Jiang, Chunxia Zhang, Zhendong Niu_

- :fontawesome-solid-user-group: **Participant:** [BIT](./entity/participants.md#bit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/bit.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/bit.ENT.pdf)
- :material-file-search: **Runs:** [BITDLDE09Run](./entity/runs.md#bitdlde09run)

??? abstract "Abstract"
	
	Our goal in participating in the TREC 2009 Entity Track is to study whether QA list technique can help improve accuracy of the entity finding task. Also, we take a looking for homepage finding to identify homepages of an entity by training a maximum entropy classifier and a logistic regression models for three types of entity respectively.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangJZN09.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangJZN09,
		author = {Qing Yang and Peng Jiang and Chunxia Zhang and Zhendong Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments on Related Entity Finding Track at {TREC} 2009},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/bit.ENT.pdf},
		timestamp = {Fri, 04 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YangJZN09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Novel Framework for Related Entities Finding: ICTNET at TREC  2009 Entity Track

_Haijun Zhai, Xueqi Cheng, Jiafeng Guo, Hongbo Xu, Yue Liu_

- :fontawesome-solid-user-group: **Participant:** [CAS_ICT_IR](./entity/participants.md#cas_ict_ir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ictnet.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/ictnet.ENT.pdf)
- :material-file-search: **Runs:** [ICTZHRun1](./entity/runs.md#ictzhrun1)

??? abstract "Abstract"
	
	This paper addresses the problem of related entity finding, which was proposed in trec 2009. The overall aim of related entity finding (REF) is to perform entity-related search on Web data, which address common information needs that are not that well modeled as ad hoc document search. In this paper, a novel framework was proposed based on a probabilistic model for related entity finding in a Web collection. This model consists of two parts. One is the probability indicating the relation between the source entity and the candidate entities. The other is the probability indicating the relevance between the candidate entities and the topic. Using ClueWeb09 dataset, the experimental evaluations show the effectiveness of our REF framework.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaiCGXL09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaiCGXL09,
		author = {Haijun Zhai and Xueqi Cheng and Jiafeng Guo and Hongbo Xu and Yue Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Novel Framework for Related Entities Finding: {ICTNET} at {TREC} 2009 Entity Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ictnet.ENT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaiCGXL09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UDEL/SMU at TREC 2009 Entity Track

_Wei Zheng, Swapna Gottipati, Jing Jiang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [EceUdel](./entity/participants.md#eceudel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.ENT.pdf)
- :material-file-search: **Runs:** [UdSmuTP](./entity/runs.md#udsmutp) | [UdSmuTU](./entity/runs.md#udsmutu) | [UdSmuCM50](./entity/runs.md#udsmucm50) | [UdSmuCM](./entity/runs.md#udsmucm)

??? abstract "Abstract"
	
	We report our methods and experiment results from the collaborative participation of the InfoLab group from University of Delaware and the school of Information Systems from Singapore Management University in the TREC 2009 Entity track. Our general goal is to study how we may apply language modeling approaches and natural language processing techniques to the task. Specifically, we proposed to find supporting information based on segment retrieval, to extract entities using Stanford NER tagger, and to rank entities based on a previously proposed probabilistic framework for expert finding.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengGJF09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengGJF09,
		author = {Wei Zheng and Swapna Gottipati and Jing Jiang and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UDEL/SMU} at {TREC} 2009 Entity Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.ENT.pdf},
		timestamp = {Tue, 20 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengGJF09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

