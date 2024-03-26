# Proceedings - Genomics 2003 

#### TREC GENOMICS Track Overview

_William R. Hersh, Ravi Teja Bhupatiraju_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/GENOMICS.OVERVIEW3.pdf](http://trec.nist.gov/pubs/trec12/papers/GENOMICS.OVERVIEW3.pdf)
??? abstract "Abstract"
	
	The first year of TREC Genomics Track featured two tasks: ad hoc retrieval and information extraction. Both tasks centered around the Gene Reference into Function (GeneRIF) resource of the National Library of Medicine, which was used as both pseudorelevance judgments for ad hoc document retrieval as well as target text for information extraction. The track attracted 29 groups who participated in one or both tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershB03.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershB03,
		author = {William R. Hersh and Ravi Teja Bhupatiraju},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} {GENOMICS} Track Overview},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {14--23},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/GENOMICS.OVERVIEW3.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HershB03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Method to Retrieve Papers from MEDLINE: PETER System

_Hiroko Ao, Yasunori Yamamoto, Toshihisa Takagi_

- :fontawesome-solid-user-group: **Participant:** [utokyo.yamamoto](./participants.md#utokyo.yamamoto)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/utokyo.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/utokyo.genomics.pdf)
- :material-file-search: **Runs:** [aoyama](./runs.md#aoyama) | [aoyama2](./runs.md#aoyama2)

??? abstract "Abstract"
	
	We attempted to eliminate non-relevant papers from results of PubMed searches for each topic. The system is called PETER (PubMed Enhancer Toward Efficient Research) and it works as follows. 1. get LocusLink IDs manually. 2. collect information of gene names (AKA synonyms) from public databases. 3. make synonym variations automatically. 4. search papers by PubMed with each synonym. 5. extract titles and abstracts. 6. take another information about synonyms from the extracted titles and abstracts. 7. extract information about abbreviations from the titles and the abstracts. 8. retrieve appropriate papers by using the synonyms and the abbreviations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AoYT03.bib) "
	```
	@inproceedings{DBLP:conf/trec/AoYT03,
		author = {Hiroko Ao and Yasunori Yamamoto and Toshihisa Takagi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Method to Retrieve Papers from {MEDLINE:} {PETER} System},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {806--809},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/utokyo.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AoYT03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BioText Team Report for the TREC 2003 Genomics Track

_Gaurav Bhalotia, Preslav Nakov, Ariel S. Schwartz, Marti A. Hearst_

- :fontawesome-solid-user-group: **Participant:** [ucalberkeley.hearst](./participants.md#ucalberkeley.hearst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ucal-berkeley.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/ucal-berkeley.genomics.pdf)
- :material-file-search: **Runs:** [biotext0](./runs.md#biotext0) | [biotext1](./runs.md#biotext1) | [biotextTask2](./runs.md#biotexttask2)

??? abstract "Abstract"
	
	The BioText project team participated in both tasks of the TREC 2003 genomics track. Key to our approach in the primary task was the use of an organism-name recognition module, a module for recognizing gene name variants, and MeSH descriptors. Text classification improved the results slightly. In the secondary task, the key insight was casting it as a classification problem of choosing between the title and the last sentence of the abstract, although MeSH descriptors helped somewhat in this task as well. These approaches yielded results within the top three groups in both tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BhalotiaNSH03.bib) "
	```
	@inproceedings{DBLP:conf/trec/BhalotiaNSH03,
		author = {Gaurav Bhalotia and Preslav Nakov and Ariel S. Schwartz and Marti A. Hearst},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {BioText Team Report for the {TREC} 2003 Genomics Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {612--621},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/ucal-berkeley.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BhalotiaNSH03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### On the Use of MeSH Headings to Improve Retrieval Effectiveness

_Stephen Blott, Cathal Gurrin, Gareth J. F. Jones, Alan F. Smeaton, Thomas Sødring_

- :fontawesome-solid-user-group: **Participant:** [dublincityu.blott](./participants.md#dublincityu.blott)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/dublin-cityu.genomic.ps](http://trec.nist.gov/pubs/trec12/papers/dublin-cityu.genomic.ps)
- :material-file-search: **Runs:** [DcuMesh2](./runs.md#dcumesh2) | [DcuMesh1](./runs.md#dcumesh1)

??? abstract "Abstract"
	
	Geneticists today spend as much time cataloguing and analysing digital data as they do in wet labs. One of the key problems they face, is that of identifying genes and publications that are relevant to their work or research. This paper describes an approach to retrieval that incorporates structural MeSH heading data into the search process. In particular, we describe a technique using a pseudo-relevance feedback process based on MeSH terms to improve retrieval effectiveness. Experimental results suggest improvements in mean average precision on the order of three percent.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BlottGJSS03.bib) "
	```
	@inproceedings{DBLP:conf/trec/BlottGJSS03,
		author = {Stephen Blott and Cathal Gurrin and Gareth J. F. Jones and Alan F. Smeaton and Thomas S{\o}dring},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {On the Use of MeSH Headings to Improve Retrieval Effectiveness},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {215--224},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/dublin-cityu.genomic.ps},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BlottGJSS03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM Research and the University of Colorado - TREC 2003 Genomics  Track

_Eric W. Brown, Andrew Dolbey, Lawrence Hunter_

- :fontawesome-solid-user-group: **Participant:** [ibm.brown](./participants.md#ibm.brown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ibm-brown.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/ibm-brown.genomics.pdf)
- :material-file-search: **Runs:** [IBMbt1](./runs.md#ibmbt1) | [IBMbt2](./runs.md#ibmbt2) | [IBMbtT2](./runs.md#ibmbtt2)

??? abstract "Abstract"
	
	IBM Research and the University of Colorado collaborated on their submission to the inaugural Genomics track at TREC 2003. IBM Research has extensive experience in natural language processing, text analysis, and large-scale systems [9, 13, 3, 5, 16, 10]. IBM also has numerous research and business activities in the broad areas of bioinformatics and bio-medical information processing [14, 8]. IBM Research is currently developing BioTeKS, a middleware system for text analysis, mining, and information retrieval in the bio-medical domain. The University of Colorado (CU) has been working in the area of bioinformatics and text analysis in the bio-medical domain for a number of years and has made substantial contributions to the field [7, 11, 15, 12]. CU contributed their domain expertise to enhance the BioTeKS system and jointly we designed and evaluated experiments while preparing our track submissions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BrownDH03.bib) "
	```
	@inproceedings{DBLP:conf/trec/BrownDH03,
		author = {Eric W. Brown and Andrew Dolbey and Lawrence Hunter},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IBM} Research and the University of Colorado - {TREC} 2003 Genomics Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {268--275},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/ibm-brown.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BrownDH03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Finiding Gene Function using LitMiner

_Berry de Bruijn, Joel D. Martin_

- :fontawesome-solid-user-group: **Participant:** [cnrc.debruijn](./participants.md#cnrc.debruijn)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/nrc.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/nrc.genomics.pdf)
- :material-file-search: **Runs:** [nrc1](./runs.md#nrc1) | [nrc2](./runs.md#nrc2)

??? abstract "Abstract"
	
	NRC (National Research Council, Canada) submitted 2 sets of results for the primary task in the TREC Genome track. The systems that generated these results were tuned primarily to achieve very high recall (above 90%) and secondarily to minimize the number of documents retrieved. Both submitted sets were the outputs of automatic systems (non-interactive, non-supervised) with a modular architecture. The TREC evaluation confirmed that recall for both submissions was extremely high: 543 out of 566 target documents (0.9594) were returned. In addition, these systems returned far fewer documents than were allowed by the genomic track rules. They returned an average of 196 documents per query across the 50 queries, with a median value of only 100 documents. For the first submission, the system was entirely based on Information Retrieval techniques, tuned to achieve very high recall and fair precision. Averaged precision was 0.3941 for the first submission. This first submission ranked third out of 49 runs submitted by all participants. For the second submission, reranking was done based on the outcome of an information extraction module, tuned towards the task of identifying gene function papers. This module identified 539 documents as highly promising; 121 of these turned out to be target documents, 418 weren't. All in all this caused the averaged precision to drop slightly to 0.3771 - contrary to our expectations. This second submission ranked fifth out of all 49 runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BruijnM03.bib) "
	```
	@inproceedings{DBLP:conf/trec/BruijnM03,
		author = {Berry de Bruijn and Joel D. Martin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Finiding Gene Function using LitMiner},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {451--459},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/nrc.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BruijnM03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Bangor at TREC 2003: Q&A and Genomics Tracks

_Terence Clifton, Alex Colquhoun, William John Teahan_

- :fontawesome-solid-user-group: **Participant:** [uwales.teahan](./participants.md#uwales.teahan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ubangor-wales.qa.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/ubangor-wales.qa.genomics.pdf)
- :material-file-search: **Runs:** [uwb2](./runs.md#uwb2) | [uwb3](./runs.md#uwb3) | [uwb4](./runs.md#uwb4)

??? abstract "Abstract"
	
	This paper describes the participation of the School of Informatics, University of Wales, Bangor at TREC'2003 in the Q&A and Genomics Tracks. The paper is organized into three parts as follows. The first part provides a brief overview of the logic-based framework for Knowledgeable Agents that is currently being developed at Bangor. This was adopted as the basis for implementations used for both Tracks. The second part describes the Q&A system that was developed based on the framework, and the final part describes some experiments that were conducted within the Genomics Track at specifying context using GeneRIFs (for a Q&A system being developed for the BioMedical domain).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CliftonCT03.bib) "
	```
	@inproceedings{DBLP:conf/trec/CliftonCT03,
		author = {Terence Clifton and Alex Colquhoun and William John Teahan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Bangor at {TREC} 2003: Q{\&}A and Genomics Tracks},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {600--611},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/ubangor-wales.qa.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CliftonCT03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Partioning a Graph of Sequences, Structures and Abstracts for Information  Retrieval

_Aynur A. Dayanik, Craig G. Nevill-Manning, Rose Oughtred_

- :fontawesome-solid-user-group: **Participant:** [rutgers.dayanik](./participants.md#rutgers.dayanik)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/rutgers-dayanik.genomic.pdf](http://trec.nist.gov/pubs/trec12/papers/rutgers-dayanik.genomic.pdf)
- :material-file-search: **Runs:** [dayrutgers2](./runs.md#dayrutgers2) | [dayrutgers1](./runs.md#dayrutgers1)

??? abstract "Abstract"
	
	In this paper, we consider the problem of finding the MEDLINE articles that describe functions of particular genes. We describe our experiments using the mg system and the partitioning of a graph of biological sequences, structures and abstracts. We participated in the primary task of the TREC 2003 Genomics Track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DayanikNO03.bib) "
	```
	@inproceedings{DBLP:conf/trec/DayanikNO03,
		author = {Aynur A. Dayanik and Craig G. Nevill{-}Manning and Rose Oughtred},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Partioning a Graph of Sequences, Structures and Abstracts for Information Retrieval},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {522--531},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/rutgers-dayanik.genomic.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DayanikNO03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Novelty, Genes and Questions at the University of Iowa

_David Eichmann, Padmini Srinivasan, Marc Light, Hudong Wang, Xin Ying Qiu, Robert J. Arens, Aditya Kumar Sehgal_

- :fontawesome-solid-user-group: **Participant:** [uiowa.eichmann](./participants.md#uiowa.eichmann)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uiowa.novelty.genomics.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/uiowa.novelty.genomics.qa.pdf)
- :material-file-search: **Runs:** [UIowaGN1](./runs.md#uiowagn1) | [UIowaSecCan](./runs.md#uiowaseccan)

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

#### REGEN: Retrieval and Extraction of Genomics Data

_Rocio Guillén, Tasnim Ferdous_

- :fontawesome-solid-user-group: **Participant:** [calstateu.guillen](./participants.md#calstateu.guillen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/calstateu.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/calstateu.genomics.pdf)
- :material-file-search: **Runs:** [CSUSM1](./runs.md#csusm1) | [CSUSM2](./runs.md#csusm2) | [CSUSMcand](./runs.md#csusmcand)

??? abstract "Abstract"
	
	In this paper we present REGEN (Retrieval and Extraction of GENomics Data) a natural language processing system that retrieves and extracts information from Genomics data. These two tasks are independent of each other in the sense that the retrieved documents are not input to the extraction task. The retrieval task is based on a combination of exact-match and partial-match searching. The extraction task uses syntactic and semantic cues as patterns to generate candidate GENERIFs. We are currently generating just one candidate.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GuillenF03.bib) "
	```
	@inproceedings{DBLP:conf/trec/GuillenF03,
		author = {Rocio Guill{\'{e}}n and Tasnim Ferdous},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{REGEN:} Retrieval and Extraction of Genomics Data},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {107--116},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/calstateu.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GuillenF03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Phrases, Boosting, and Query Expansion Using External Knowledge Resources  for Genomic Information Retrieval

_William R. Hersh, Ravi Teja Bhupatiraju, Susan Price_

- :fontawesome-solid-user-group: **Participant:** [ohsu.hersh](./participants.md#ohsu.hersh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ohsu.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/ohsu.genomics.pdf)
- :material-file-search: **Runs:** [ohsuboost](./runs.md#ohsuboost)

??? abstract "Abstract"
	
	In our TREC Genomics Track work, we focused on domain-specific techniques in attempting to improve retrieval performance beyond a word searching baseline. One set of experiments looked at using phrases based on gene name synonyms with boosting of the canonical name of the gene. Another set assessed query expansion using external knowledge resources.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershBP03.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershBP03,
		author = {William R. Hersh and Ravi Teja Bhupatiraju and Susan Price},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Phrases, Boosting, and Query Expansion Using External Knowledge Resources for Genomic Information Retrieval},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {503--509},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/ohsu.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HershBP03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SVM Approach to GeneRIF Annotation

_Wen-Juan Hou, Chun-Yuan Teng, Chih Lee, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu.chen](./participants.md#ntu.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ntu.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/ntu.genomics.pdf)
- :material-file-search: **Runs:** [nwe](./runs.md#nwe) | [we](./runs.md#we)

??? abstract "Abstract"
	
	In the biological domain, to extract the newly discovered functional features from massive literature is a major challenging issue. To automatically annotate GeneRIF in a new literature is the main goal in this paper. We try to find function words and introducers in the training corpus, and then apply such informative words to annotate the GeneRIF. The experiments showed that 48.15%, 49.78%, 32.31%, and 35.63% for the measure of Classic Dice, Modified unigram Dice, Modified bigram Dice, and Modified bigram Dice phrases. After applying SVM learning mechanism combing new weighting scheme and position information, we get much better performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HouTLC03.bib) "
	```
	@inproceedings{DBLP:conf/trec/HouTLC03,
		author = {Wen{-}Juan Hou and Chun{-}Yuan Teng and Chih Lee and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{SVM} Approach to GeneRIF Annotation},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {468--473},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/ntu.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HouTLC03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Recognizing Gene and Protein Function in MEDLINE Abstracts

_Richard D. Hull, Larry F. Waldman_

- :fontawesome-solid-user-group: **Participant:** [axontologic.hull](./participants.md#axontologic.hull)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/axontologic.genomic.pdf](http://trec.nist.gov/pubs/trec12/papers/axontologic.genomic.pdf)
- :material-file-search: **Runs:** [axon1](./runs.md#axon1) | [axon2](./runs.md#axon2)

??? abstract "Abstract"
	
	Identification of genes and proteins that affect biological function in humans and other organisms is a critical step in the discovery of new medicinal therapies. Automatic recognition of MEDLINE abstracts that describe gene/protein function would be of tremendous benefit to researchers in industry, government, and academia. Our approach uses simple syntax and domain semantics to both identify sentences from MEDLINE abstracts that suggest gene function and to rank those abstracts by a measure of how many appropriate function instances they contain.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HullW03.bib) "
	```
	@inproceedings{DBLP:conf/trec/HullW03,
		author = {Richard D. Hull and Larry F. Waldman},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Recognizing Gene and Protein Function in {MEDLINE} Abstracts},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {93--97},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/axontologic.genomic.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HullW03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Searching for geneRIFs: Concept-Based Query Expansion and Bayes Classification

_Rob Jelier, Martijn J. Schuemie, C. Christiaan van der Eijk, Marc Weeber, Erik M. van Mulligen, Bob J. A. Schijvenaars, Barend Mons, Jan A. Kors_

- :fontawesome-solid-user-group: **Participant:** [erasmus.weeber](./participants.md#erasmus.weeber)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/erasmusu.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/erasmusu.genomics.pdf)
- :material-file-search: **Runs:** [ErasmusMC2](./runs.md#erasmusmc2) | [ErasmusMC3](./runs.md#erasmusmc3) | [emc4](./runs.md#emc4)

??? abstract "Abstract"
	
	The Biosemantics group at the Erasmus MC followed a thesaurus-based approach for the first task of the genomics track. The approach is based on a concept-based indexing engine (Collexis®), suitable for large - cale and high-speed indexing. The thesaurus used for indexing was constructed as a combination of the MESH thesaurus and the gene ontology (GO), with a species-specific gene thesaurus derived from LocusLink gene annotations. Our indexing machinery produces per indexed MEDLINE abstract a list of concepts with an accompanying weight, termed a fingerprint. Searching is done by matching a query fingerprint against fingerprints of all indexed MEDLINE abstracts. Query fingerprints are generated by combining fingerprints of four types. First, a fingerprint containing just the gene concept with all the known gene names and aliases. Second, a combination of MEDLINE fingerprints of all abstracts in which the gene concept was found without ambiguity problems. Third, a generic fingerprint with concepts typical of geneRIFs, when compared to MEDLINE in general. Fourth, a fingerprint containing the concepts of the Gene Ontology (GO) annotation When it comes to identifying a gene name in a text the large number of synonyms and the frequent occurrence of homonymy are problematic. In our approach we attempt to deal with both. Synonymy as found in Locuslink is incorporated in our thesaurus. An attempt was made to reduce the effects of homonymy by expanding the query with fingerprints where the gene name is found unambiguously. Gene specific information, the GO annotation, is included to select for the correct gene, but also to select for abstracts with terms about basic biology. The generic fingerprint is included to select for abstracts with terms about basic biology.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JelierSEWMSMK03.bib) "
	```
	@inproceedings{DBLP:conf/trec/JelierSEWMSMK03,
		author = {Rob Jelier and Martijn J. Schuemie and C. Christiaan van der Eijk and Marc Weeber and Erik M. van Mulligen and Bob J. A. Schijvenaars and Barend Mons and Jan A. Kors},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Searching for geneRIFs: Concept-Based Query Expansion and Bayes Classification},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {225--233},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/erasmusu.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JelierSEWMSMK03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Methods for Accurate Retrieval of MEDLINE Citations in Functional  Genomics

_Mehmet Kayaalp, Alan R. Aronson, Susanne M. Humphrey, Nicholas C. Ide, Lorraine K. Tanabe, Lawrence H. Smith, Dina Demner-Fushman, Russell F. Loane, James G. Mork, Olivier Bodenreider_

- :fontawesome-solid-user-group: **Participant:** [nlm.aronson](./participants.md#nlm.aronson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/nlm.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/nlm.genomics.pdf)
- :material-file-search: **Runs:** [NLMUMDSE](./runs.md#nlmumdse) | [NLMUMDSRB](./runs.md#nlmumdsrb) | [NLMUMDLIN](./runs.md#nlmumdlin)

??? abstract "Abstract"
	
	The lack of discipline and consistency in gene naming poses a formidable challenge to researchers in locating relevant information sources in the genomics literature. The research presented here primarily focuses on how to find the MEDLINEÆ citations that describe functions of particular genes. We developed new methods and extended current techniques that may help researchers to retrieve such citations accurately. We further evaluated several machine learning and optimization algorithms to identify the sentences describing gene functions in given citations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KayaalpAHITSDLMB03.bib) "
	```
	@inproceedings{DBLP:conf/trec/KayaalpAHITSDLMB03,
		author = {Mehmet Kayaalp and Alan R. Aronson and Susanne M. Humphrey and Nicholas C. Ide and Lorraine K. Tanabe and Lawrence H. Smith and Dina Demner{-}Fushman and Russell F. Loane and James G. Mork and Olivier Bodenreider},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Methods for Accurate Retrieval of {MEDLINE} Citations in Functional Genomics},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {441--450},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/nlm.genomics.pdf},
		timestamp = {Thu, 20 Aug 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KayaalpAHITSDLMB03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Edinburgh-Stanford TREC-2003 Genomics Track

_Miles Osborne, Mark Cuminskey, Gail Sinclair, Matthew Smillie, Bonnie L. Webber, Jeffrey T. Chang, Nipun Mehra, Veronica Rotemberg, Russ B. Altman_

- :fontawesome-solid-user-group: **Participant:** [uedinburgh.webber](./participants.md#uedinburgh.webber)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uedinburgh.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/uedinburgh.genomics.pdf)
- :material-file-search: **Runs:** [edstanprec](./runs.md#edstanprec) | [edstanrecall](./runs.md#edstanrecall) | [EDISTFruns2](./runs.md#edistfruns2)

??? abstract "Abstract"
	
	We describe our participation in both tasks in the 2003 TREC Genomics track. For the primary task we concentrated mainly upon query expansion and species-specific document searching. An analysis of the variance of possible retrieval results suggested that the official TREC-supplied test set is only a crude approximation of the true system performance. The secondary task we treated as an extraction problem, using a maximum entropy scorer trained on GeneRIF sentences as positives and other sentences as negatives. While our results were not always equivalent to the actual GeneRIFs, on biological grounds many of them appeared better descriptors than the GeneRIFs themselves.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OsborneCSSWCMRA03.bib) "
	```
	@inproceedings{DBLP:conf/trec/OsborneCSSWCMRA03,
		author = {Miles Osborne and Mark Cuminskey and Gail Sinclair and Matthew Smillie and Bonnie L. Webber and Jeffrey T. Chang and Nipun Mehra and Veronica Rotemberg and Russ B. Altman},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Edinburgh-Stanford {TREC-2003} Genomics Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {622--630},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uedinburgh.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OsborneCSSWCMRA03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2003 Genomics Track Experiments at UTA: Query Expansion with  Predefinded High Frequency Terms

_Ari Pirkola, Erkka Leppänen_

- :fontawesome-solid-user-group: **Participant:** [utampere.pirkola](./participants.md#utampere.pirkola)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/utampere.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/utampere.genomics.pdf)
- :material-file-search: **Runs:** [utafil](./runs.md#utafil) | [utaband](./runs.md#utaband)

??? abstract "Abstract"
	
	We studied the effects of query expansion and query structure on retrieval performance. Two sets of words frequent in relevant documents for Genomics Track's training topics were collected, the first manually and the second automatically. The high frequency words collected and the names of organisms designated in the test topics, were used as expansion keys in gene name queries formed from the final test topics. The results indicated that Boolean structured queries expanded with automatically collected high frequency words and names of organisms performed considerably better than queries containing gene names only as keys. In the Boolean queries the expansion keys were categorized based on the aspects they represent in the documents discussing gene function. All the structured queries performed better than unstructured queries where each key contributed equally to document weights. In the structured queries gene names were assigned more weight than the expansion keys.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PirkolaL03.bib) "
	```
	@inproceedings{DBLP:conf/trec/PirkolaL03,
		author = {Ari Pirkola and Erkka Lepp{\"{a}}nen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2003 Genomics Track Experiments at {UTA:} Query Expansion with Predefinded High Frequency Terms},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {796--805},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/utampere.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PirkolaL03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 2003 Experiment: Genomic Track

_Patrick Ruch, Gilles Cohen, Frédéric Ehrler, Henning Müller, Giovanni Coray, Hatem Ghorbel, Vincenzo Pallotta, Christine Chichester_

- :fontawesome-solid-user-group: **Participant:** [u.hospitalgeneva](./participants.md#u.hospitalgeneva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/univ-hosp-geneva.genomic.pdf](http://trec.nist.gov/pubs/trec12/papers/univ-hosp-geneva.genomic.pdf)
- :material-file-search: **Runs:** [tg2hug](./runs.md#tg2hug) | [tgIIhugLASt](./runs.md#tgiihuglast)

??? abstract "Abstract"
	
	For our first participation to the TREC evaluation campaign, our efforts concentrated on the genomic track. Because we joined the competition at the end of June, we were not able to submit runs for the ad hoc retrieval task (task I), and therefore this report mostly focuses on the information extraction task (task II). Task I. Our approach uses thesaural resources (from the UMLS) together with a variant of the Porter stemmer for string normalization. Gene and Protein Entities (GPE) of the collection (525,938 MedLine citations) were simply marked up by dictionary look up during the indexing in order to avoid erroneous conflation: strings not found in the UMLS Specialist lexicon (augmented with various English lexical resources) were considered as GPE and were moderately overweighted. In the same spirit like other TREC competitors [23] for task I, an overweighting factor was also applied to features belonging to Medical Subject Headings (MeSH) and found in MedLine citations using a MeSH mapping tool [1]. A standard vector space IR engine with tf-idf parameters was used for indexing the Genomic collection: article's titles, MeSH and RN terms, and abstact fields were selected. Best average precisions were obtained with atc.ntn (using the SMART notation) schemes: 16.71 (standard) vs. 17.02 (using UMLS resources and GPE tagging). Studies made after the competition and inspired by results reported by other groups [13][14] confirmed that narrowing the search to those species appearing in the query provides a very effective improvement of the average precision. The species are detected based on their listing in a dictionnary (extracted from the MeSH terminology). The refinement strategy consists in filtering out documents when the targetted species is not found in the abstract. After retrieval, this simple strategy yield to an important improvement of the average precision: from 17.02 up to 35.80. Task II. Our approach is based on argumentative structuring, i.e. classification of textual segments into argumentative classes. We see the task as a question-answering task using always the very same question. We take advantage of a classifier likely to predict the argumentative class of any textual segment with high accuracy (F-score = 85%). We observe that when not taken from the title, GeneRIFs are found -ranked by decreasing order- in: 1) CONCLUSION, 2) PURPOSE, 3) RESULTS, 4) METHODS. After sentence splitting, sentences are classified and ranked according to these four categories. On that basis, a second ranking is made based on the similarity with the title (45% of GeneRIFs; Dice baseline = 50.47%). Then, we compute a combined score for each of these features, setting a Dice-like threshold to decide whether we use the title or the best scored sentence as GeneRIF. Finally, a last step consists in narrowing segment boundaries to shorten the length of the candidate GeneRIF. A set of ad hoc and argumentative filters are applied in order to remove irrelevant pieces at the end/beginning of the selected segment. Examples of phrases that are removed at the beginning are 'in this paper, finally...'. Then, sentence endings (up to 7 words) classified as METHODS (such as 'in contrast to current models', 'by the...') are also removed. Using the complete article instead of the abstract did not result in any improvement. Our best performances are obtained by using 14 (Dice = 52.78%) and 23 (Dice = 52.41%) segments from the abstract, while the reamining originates from the title. The use of argumentative features is encouraging, however more complex features combination will have to be explored in the future.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuchCEMCGPC03.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuchCEMCGPC03,
		author = {Patrick Ruch and Gilles Cohen and Fr{\'{e}}d{\'{e}}ric Ehrler and Henning M{\"{u}}ller and Giovanni Coray and Hatem Ghorbel and Vincenzo Pallotta and Christine Chichester},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Report on the {TREC} 2003 Experiment: Genomic Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {756--761},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/univ-hosp-geneva.genomic.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuchCEMCGPC03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Identifying Gene Function Descriptions by Probability-based Sentence  Selection

_Kazuhiro Seki, Nihar Sheth, Javed Mostafa_

- :fontawesome-solid-user-group: **Participant:** [indianau.seki](./participants.md#indianau.seki)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/indianau.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/indianau.genomics.pdf)
- :material-file-search: **Runs:** [IUB2003](./runs.md#iub2003)

??? abstract "Abstract"
	
	This paper proposes an approach to the secondary task in the TREC Genomics Track. We regard the task as identification of the sentences describing gene functions (i.e., GeneRIFs) and propose a method considering two factors: topicality and relevance. The former refers to the topicality of a sentence and is measured based on location information and word frequencies in the article. The latter refers to the relevance as a GeneRIF based on the vocabulary used in the article. We formalize a probabilistic model combining these features. Our method is evaluated on the test set of 139 MEDLINE abstracts, and the results demonstrate that (a) function words in input could help to identify gene function descriptions and that (b) there is a vocabulary peculiar to GeneRIFs and that (c) location information shows the highest predictive power for this particular task despite its simplicity. Additionally, we examine some alternative methods in comparison with our method.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SekiSM03.bib) "
	```
	@inproceedings{DBLP:conf/trec/SekiSM03,
		author = {Kazuhiro Seki and Nihar Sheth and Javed Mostafa},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Identifying Gene Function Descriptions by Probability-based Sentence Selection},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {321--327},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/indianau.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SekiSM03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Biomedical Text Retrieval System at Korea University

_Young-In Song, Kyoung-Soo Han, Hee-Cheol Seo, Sang-Bum Kim, Hae-Chang Rim_

- :fontawesome-solid-user-group: **Participant:** [koreau.kim](./participants.md#koreau.kim)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/koreau.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/koreau.genomics.pdf)
- :material-file-search: **Runs:** [KUBIOIRNE](./runs.md#kubioirne) | [KUBIOIRRAW](./runs.md#kubioirraw)

??? abstract "Abstract"
	
	In this paper, we describe our retrieval system used for the primary task of genomics track at this year. Our primary goal in this task is to find a proper method for the domain-specific retrieval environment. To achieve the goal, we have tested several techniques such as a phrase indexing strategy, two query weighting methods, and two post-processing methods such as a document filtering method and a documents reranking method. According to the experimental results, query weighting methods and document filtering methods can improve the performance of the retrieval system, but there still remain a room for improvement.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SongHSKR03.bib) "
	```
	@inproceedings{DBLP:conf/trec/SongHSKR03,
		author = {Young{-}In Song and Kyoung{-}Soo Han and Hee{-}Cheol Seo and Sang{-}Bum Kim and Hae{-}Chang Rim},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Biomedical Text Retrieval System at Korea University},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {368--374},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/koreau.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SongHSKR03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UB at TREC 12: HARD and Genomics Tracks

_Munirathnam Srikanth, Miguel E. Ruiz, Rohini K. Srihari_

- :fontawesome-solid-user-group: **Participant:** [unybuffalo-cedar](./participants.md#unybuffalo-cedar)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uny-buffalo.hard.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/uny-buffalo.hard.genomics.pdf)
- :material-file-search: **Runs:** [UBgenomRFB1](./runs.md#ubgenomrfb1) | [UBgenomeBGNE](./runs.md#ubgenomebgne) | [UBgenomRFB2](./runs.md#ubgenomrfb2) | [UBGenT2R1](./runs.md#ubgent2r1) | [UBGenT2R2](./runs.md#ubgent2r2) | [UBGenT2BL1](./runs.md#ubgent2bl1)

??? abstract "Abstract"
	
	University at Buffalo (UB) participated in TREC-12 in Genomics and High Accuracy Retrieval from Documents (HARD) tracks. We explored some techniques that combine Information Retrieval and Information Extraction to perform the TREC tasks. We used an Information Extraction engine - InfoXtract [3] from Cymfony Inc.1 - to enhance retrieval results. For the Genomics primary task, documents retrieved using a vector space model with relevance feedback are reweighted based on the biomedical named entities discovered by InfoXtract. For the secondary task, extracted information along with cue words for text snippets that describe functionality is used for generating GeneRIFs for given Gene name and PubMed abstract. A language modeling approach that incorporates keyword and non-keyword features are used for the HARD task. Features extracted by InfoXtract from the HARD corpus are used to rank documents and/or passages as answers to the HARD queries. Cymfony's InfoXtract [3] is a customizable Information Extraction engine that performs syntactic and semantic parsing of a document to identify features like named entities, relationships and events in them. The baseline InfoXtract engine has been trained for the general English and news domain, It can be customized to recognize new named entities like Gene Names and Gene Function. Biomedical Customization of InfoXtract is briefly presented in Section 2.2.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SrikanthRS03.bib) "
	```
	@inproceedings{DBLP:conf/trec/SrikanthRS03,
		author = {Munirathnam Srikanth and Miguel E. Ruiz and Rohini K. Srihari},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UB} at {TREC} 12: {HARD} and Genomics Tracks},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {751--755},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uny-buffalo.hard.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SrikanthRS03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in TREC 2003 Genomics Track at NTT

_Hirotoshi Taira, Tomonori Izumitani, Tsutomu Hirao, Hideki Isozaki, Hideto Kazawa, Eisaku Maeda_

- :fontawesome-solid-user-group: **Participant:** [nttcom.kazawa](./participants.md#nttcom.kazawa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ntt.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/ntt.genomics.pdf)
- :material-file-search: **Runs:** [balsc2](./runs.md#balsc2) | [balsc3](./runs.md#balsc3) | [balscsec1](./runs.md#balscsec1)

??? abstract "Abstract"
	
	In TREC-2003, we participated in Question Answering and Genomics Tracks. Since the QA system was essentially the same as the past years' systems[1, 2], we describe our results with the Genomics Track in this paper
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TairaIHIKM03.bib) "
	```
	@inproceedings{DBLP:conf/trec/TairaIHIKM03,
		author = {Hirotoshi Taira and Tomonori Izumitani and Tsutomu Hirao and Hideki Isozaki and Hideto Kazawa and Eisaku Maeda},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments in {TREC} 2003 Genomics Track at {NTT}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {460--467},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/ntt.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TairaIHIKM03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Robust, Web and Genomic Retrieval with Hummingbird SearchServer at  TREC 2003

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird.tomlinson](./participants.md#hummingbird.tomlinson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/hummingbird.robust.web.genomic.pdf](http://trec.nist.gov/pubs/trec12/papers/hummingbird.robust.web.genomic.pdf)
- :material-file-search: **Runs:** [humG03ns](./runs.md#humg03ns) | [humG03ns5](./runs.md#humg03ns5)

??? abstract "Abstract"
	
	Hummingbird participated in 4 tasks of TREC 2003: the ad hoc task of the Robust Retrieval Track (find at least one relevant document in the first 10 rows from 1.9GB of news and government data), the navigational task of the Web Track (find the home or named page in 1.2 million pages (18GB) from the .GOV domain), the topic distillation task of the Web Track (find key resources for topics in the first 10 rows from home pages of .GOV), and the primary task of the Genomics Track (find all records focusing on the named gene in 1.1GB of MEDLINE data). In the ad hoc task, SearchServer found a relevant document in the first 10 rows for 48 of the 50 new short (Title-only) topics. In the navigational task, SearchServer returned the home or named page in the first 10 rows for more than 75% of the 300 queries. In the distillation task, a SearchServer run found the most key resources in the first 10 rows of the submitted runs from 23 groups.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson03.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson03,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Robust, Web and Genomic Retrieval with Hummingbird SearchServer at {TREC} 2003},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {254--267},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/hummingbird.robust.web.genomic.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Knowledge-Based Access to the Bio-Medical Literature, Ontologically-Grounded  Experiments for the TREC 2003 Genomics Track

_Richard Tong, John Quackenbush, Mark Snuffin_

- :fontawesome-solid-user-group: **Participant:** [tarragon.tong](./participants.md#tarragon.tong)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/tarragon.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/tarragon.genomics.pdf)
- :material-file-search: **Runs:** [tgnVariant1](./runs.md#tgnvariant1) | [tgnBaseline](./runs.md#tgnbaseline)

??? abstract "Abstract"
	
	The Tarragon Consulting team participated in the primary task of the TREC 2003 Genomics Track. We used a combination of knowledge-engineering and corpus analysis to construct semantic models of the interactions between genes/proteins and other biological entities in the organism, and then used automatic methods to convert these models into evidential queries that could be executed by the K2 search engine from Verity, Inc. The primary goal of our participation in the Genomics Track was to establish a performance baseline using ontologically-grounded techniques that are scalable and implementable using current commercial retrieval technology. The results from both our official submissions and subsequent experiments demonstrate that good performance can be achieved using our approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TongQS03.bib) "
	```
	@inproceedings{DBLP:conf/trec/TongQS03,
		author = {Richard Tong and John Quackenbush and Mark Snuffin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Knowledge-Based Access to the Bio-Medical Literature, Ontologically-Grounded Experiments for the {TREC} 2003 Genomics Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {547--551},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/tarragon.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TongQS03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Task-Specific Query Expansion (MultiText Experiments for TREC 2003)

_David L. Yeung, Charles L. A. Clarke, Gordon V. Cormack, Thomas R. Lynam, Egidio L. Terra_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo.cormack](./participants.md#uwaterloo.cormack)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uwaterloo.genomics.robust.pdf](http://trec.nist.gov/pubs/trec12/papers/uwaterloo.genomics.robust.pdf)
- :material-file-search: **Runs:** [uwmtg03btrf](./runs.md#uwmtg03btrf) | [uwmtg03atrf](./runs.md#uwmtg03atrf)

??? abstract "Abstract"
	
	For TREC 2003 the MultiText Project focused its efforts on the Genomics and Robust tracks. We also submitted passage-retrieval runs for the QA track. For the Genomics Track primary task, we used an amalgamation of retrieval and query expansion techniques, including tiering, term re-writing and pseudo-relevance feedback. For the Robust Track, we examined the impact of pseudo-relevance feedback on retrieval effectiveness under the new robustness measures. All of our TREC runs were generated by the MultiText System, a collection of tools and techniques for information retrieval, question answering and structured text search. The MultiText Project at the University of Waterloo has been developing this system since 1993 and has participated in TREC annually since TREC-4 in 1995. In the next section, we briefly review the retrieval methods used in our TREC 2003 runs. Depending on the track, various combinations of these methods were used to generate our runs. The remaining sections describe our activities for the individual tracks, with the bulk of the report covering our Genomics Track results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YeungCCLT03.bib) "
	```
	@inproceedings{DBLP:conf/trec/YeungCCLT03,
		author = {David L. Yeung and Charles L. A. Clarke and Gordon V. Cormack and Thomas R. Lynam and Egidio L. Terra},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Task-Specific Query Expansion (MultiText Experiments for {TREC} 2003)},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {810--819},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uwaterloo.genomics.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YeungCCLT03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Improving the Robustness of Language Models - UIUC TREC 2003 Robust  and Genomics Experiments

_ChengXiang Zhai, Tao Tao, Hui Fang, Zhidi Shang_

- :fontawesome-solid-user-group: **Participant:** [uillinoisuc.zhai](./participants.md#uillinoisuc.zhai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.robust.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.robust.genomics.pdf)
- :material-file-search: **Runs:** [UIUC03Ga](./runs.md#uiuc03ga) | [UIUC03Gb](./runs.md#uiuc03gb)

??? abstract "Abstract"
	
	In this paper, we report our experiments in the TREC 2003 Genomics Track and the Robust Track. A common theme that we explored is the robustness of a basic language modeling retrieval approach. We examine several aspects of robustness, including robustness in handling different types of queries, different types of documents, and optimizing performance for difficult topics. Our basic retrieval method is the KL-divergence retrieval model with the two-stage smoothing method plus a mixture model feedback method. In the Genomics IR track, we propose a new method for modeling semi-structured queries using language models, which is shown to be more robust and effective than the regular query model in handling gene queries. In the Robust track, we experimented with two heuristic approaches to improve the robustness in using language models for pseudo feedback.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaiTFS03.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaiTFS03,
		author = {ChengXiang Zhai and Tao Tao and Hui Fang and Zhidi Shang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Improving the Robustness of Language Models - {UIUC} {TREC} 2003 Robust and Genomics Experiments},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {667--672},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.robust.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaiTFS03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

