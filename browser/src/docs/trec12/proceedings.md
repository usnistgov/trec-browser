# Proceedings 2003 

## Overview of TREC 2003

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/OVERVIEW.12.pdf](http://trec.nist.gov/pubs/trec12/papers/OVERVIEW.12.pdf)
??? abstract "Abstract"
	
	The twelfth Text REtrieval Conference, TREC 2003, was held at the National Institute of Standards and Technology (NIST) November 18-21, 2003. The conference was co-sponsored by NIST, the US Department of Defense Advanced Research and Development Activity (ARDA), and the Defense Advanced Research Projects Agency (DARPA). TREC 2003 is the latest in a series of workshops designed to foster research on technologies for information retrieval. The workshop series has four goals: to encourage retrieval research based on large test collections; to increase communication among industry, academia, and government by creating an open forum for the ex- change of research ideas; to speed the transfer of technology from research labs into commercial products by demonstrating substantial improvements in retrieval methodologies on real-world problems; and to increase the availability of appropriate evaluation techniques for use by industry and academia, including development of new evaluation techniques more applicable to current systems. TREC 2003 contained six areas of focus called “tracks”. Three of the tracks, novelty, question answering, and web, were continuations of tracks that had run in earlier TRECs. The remaining three tracks, genomics, High-Accuracy-Retrieval-from-Documents (HARD), and robust retrieval, were new tracks in 2003. The retrieval tasks performed in each of the tracks are summarized in Section 3 below. Table 1 lists the 93 groups that participated in TREC 2003. The participating groups come from 22 different countries and include academic, commercial, and government institutions. This paper serves as an introduction to the research described in detail in the remainder of the volume. The next section provides a summary of the retrieval background knowledge that is assumed in the other papers. Section 3 presents a short description of each track—a more complete description of a track can be found in that track's overview paper in the proceedings. The final section looks forward to future TREC conferences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees03.bib)"
	```
	@inproceedings{DBLP:conf/trec/Voorhees03,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of {TREC} 2003},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {1--13},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/OVERVIEW.12.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Genomics 

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

- :fontawesome-solid-user-group: **Participant:** [utokyo.yamamoto](./genomics/participants.md#utokyo.yamamoto)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/utokyo.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/utokyo.genomics.pdf)
- :material-file-search: **Runs:** [aoyama](./genomics/runs.md#aoyama) | [aoyama2](./genomics/runs.md#aoyama2)

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

- :fontawesome-solid-user-group: **Participant:** [ucalberkeley.hearst](./genomics/participants.md#ucalberkeley.hearst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ucal-berkeley.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/ucal-berkeley.genomics.pdf)
- :material-file-search: **Runs:** [biotext0](./genomics/runs.md#biotext0) | [biotext1](./genomics/runs.md#biotext1) | [biotextTask2](./genomics/runs.md#biotexttask2)

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

- :fontawesome-solid-user-group: **Participant:** [dublincityu.blott](./genomics/participants.md#dublincityu.blott)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/dublin-cityu.genomic.ps](http://trec.nist.gov/pubs/trec12/papers/dublin-cityu.genomic.ps)
- :material-file-search: **Runs:** [DcuMesh2](./genomics/runs.md#dcumesh2) | [DcuMesh1](./genomics/runs.md#dcumesh1)

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

- :fontawesome-solid-user-group: **Participant:** [ibm.brown](./genomics/participants.md#ibm.brown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ibm-brown.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/ibm-brown.genomics.pdf)
- :material-file-search: **Runs:** [IBMbt1](./genomics/runs.md#ibmbt1) | [IBMbt2](./genomics/runs.md#ibmbt2) | [IBMbtT2](./genomics/runs.md#ibmbtt2)

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

- :fontawesome-solid-user-group: **Participant:** [cnrc.debruijn](./genomics/participants.md#cnrc.debruijn)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/nrc.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/nrc.genomics.pdf)
- :material-file-search: **Runs:** [nrc1](./genomics/runs.md#nrc1) | [nrc2](./genomics/runs.md#nrc2)

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

- :fontawesome-solid-user-group: **Participant:** [uwales.teahan](./genomics/participants.md#uwales.teahan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ubangor-wales.qa.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/ubangor-wales.qa.genomics.pdf)
- :material-file-search: **Runs:** [uwb2](./genomics/runs.md#uwb2) | [uwb3](./genomics/runs.md#uwb3) | [uwb4](./genomics/runs.md#uwb4)

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

- :fontawesome-solid-user-group: **Participant:** [rutgers.dayanik](./genomics/participants.md#rutgers.dayanik)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/rutgers-dayanik.genomic.pdf](http://trec.nist.gov/pubs/trec12/papers/rutgers-dayanik.genomic.pdf)
- :material-file-search: **Runs:** [dayrutgers2](./genomics/runs.md#dayrutgers2) | [dayrutgers1](./genomics/runs.md#dayrutgers1)

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

- :fontawesome-solid-user-group: **Participant:** [uiowa.eichmann](./genomics/participants.md#uiowa.eichmann)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uiowa.novelty.genomics.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/uiowa.novelty.genomics.qa.pdf)
- :material-file-search: **Runs:** [UIowaGN1](./genomics/runs.md#uiowagn1) | [UIowaSecCan](./genomics/runs.md#uiowaseccan)

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

- :fontawesome-solid-user-group: **Participant:** [calstateu.guillen](./genomics/participants.md#calstateu.guillen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/calstateu.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/calstateu.genomics.pdf)
- :material-file-search: **Runs:** [CSUSM1](./genomics/runs.md#csusm1) | [CSUSM2](./genomics/runs.md#csusm2) | [CSUSMcand](./genomics/runs.md#csusmcand)

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

- :fontawesome-solid-user-group: **Participant:** [ohsu.hersh](./genomics/participants.md#ohsu.hersh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ohsu.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/ohsu.genomics.pdf)
- :material-file-search: **Runs:** [ohsuboost](./genomics/runs.md#ohsuboost)

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

- :fontawesome-solid-user-group: **Participant:** [ntu.chen](./genomics/participants.md#ntu.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ntu.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/ntu.genomics.pdf)
- :material-file-search: **Runs:** [nwe](./genomics/runs.md#nwe) | [we](./genomics/runs.md#we)

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

- :fontawesome-solid-user-group: **Participant:** [axontologic.hull](./genomics/participants.md#axontologic.hull)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/axontologic.genomic.pdf](http://trec.nist.gov/pubs/trec12/papers/axontologic.genomic.pdf)
- :material-file-search: **Runs:** [axon1](./genomics/runs.md#axon1) | [axon2](./genomics/runs.md#axon2)

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

- :fontawesome-solid-user-group: **Participant:** [erasmus.weeber](./genomics/participants.md#erasmus.weeber)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/erasmusu.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/erasmusu.genomics.pdf)
- :material-file-search: **Runs:** [ErasmusMC2](./genomics/runs.md#erasmusmc2) | [ErasmusMC3](./genomics/runs.md#erasmusmc3) | [emc4](./genomics/runs.md#emc4)

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

- :fontawesome-solid-user-group: **Participant:** [nlm.aronson](./genomics/participants.md#nlm.aronson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/nlm.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/nlm.genomics.pdf)
- :material-file-search: **Runs:** [NLMUMDSE](./genomics/runs.md#nlmumdse) | [NLMUMDSRB](./genomics/runs.md#nlmumdsrb) | [NLMUMDLIN](./genomics/runs.md#nlmumdlin)

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

- :fontawesome-solid-user-group: **Participant:** [uedinburgh.webber](./genomics/participants.md#uedinburgh.webber)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uedinburgh.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/uedinburgh.genomics.pdf)
- :material-file-search: **Runs:** [edstanprec](./genomics/runs.md#edstanprec) | [edstanrecall](./genomics/runs.md#edstanrecall) | [EDISTFruns2](./genomics/runs.md#edistfruns2)

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

- :fontawesome-solid-user-group: **Participant:** [utampere.pirkola](./genomics/participants.md#utampere.pirkola)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/utampere.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/utampere.genomics.pdf)
- :material-file-search: **Runs:** [utafil](./genomics/runs.md#utafil) | [utaband](./genomics/runs.md#utaband)

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

- :fontawesome-solid-user-group: **Participant:** [u.hospitalgeneva](./genomics/participants.md#u.hospitalgeneva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/univ-hosp-geneva.genomic.pdf](http://trec.nist.gov/pubs/trec12/papers/univ-hosp-geneva.genomic.pdf)
- :material-file-search: **Runs:** [tg2hug](./genomics/runs.md#tg2hug) | [tgIIhugLASt](./genomics/runs.md#tgiihuglast)

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

- :fontawesome-solid-user-group: **Participant:** [indianau.seki](./genomics/participants.md#indianau.seki)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/indianau.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/indianau.genomics.pdf)
- :material-file-search: **Runs:** [IUB2003](./genomics/runs.md#iub2003)

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

- :fontawesome-solid-user-group: **Participant:** [koreau.kim](./genomics/participants.md#koreau.kim)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/koreau.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/koreau.genomics.pdf)
- :material-file-search: **Runs:** [KUBIOIRNE](./genomics/runs.md#kubioirne) | [KUBIOIRRAW](./genomics/runs.md#kubioirraw)

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

- :fontawesome-solid-user-group: **Participant:** [unybuffalo-cedar](./genomics/participants.md#unybuffalo-cedar)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uny-buffalo.hard.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/uny-buffalo.hard.genomics.pdf)
- :material-file-search: **Runs:** [UBgenomRFB1](./genomics/runs.md#ubgenomrfb1) | [UBgenomeBGNE](./genomics/runs.md#ubgenomebgne) | [UBgenomRFB2](./genomics/runs.md#ubgenomrfb2) | [UBGenT2R1](./genomics/runs.md#ubgent2r1) | [UBGenT2R2](./genomics/runs.md#ubgent2r2) | [UBGenT2BL1](./genomics/runs.md#ubgent2bl1)

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

- :fontawesome-solid-user-group: **Participant:** [nttcom.kazawa](./genomics/participants.md#nttcom.kazawa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ntt.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/ntt.genomics.pdf)
- :material-file-search: **Runs:** [balsc2](./genomics/runs.md#balsc2) | [balsc3](./genomics/runs.md#balsc3) | [balscsec1](./genomics/runs.md#balscsec1)

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

- :fontawesome-solid-user-group: **Participant:** [hummingbird.tomlinson](./genomics/participants.md#hummingbird.tomlinson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/hummingbird.robust.web.genomic.pdf](http://trec.nist.gov/pubs/trec12/papers/hummingbird.robust.web.genomic.pdf)
- :material-file-search: **Runs:** [humG03ns](./genomics/runs.md#humg03ns) | [humG03ns5](./genomics/runs.md#humg03ns5)

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

- :fontawesome-solid-user-group: **Participant:** [tarragon.tong](./genomics/participants.md#tarragon.tong)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/tarragon.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/tarragon.genomics.pdf)
- :material-file-search: **Runs:** [tgnVariant1](./genomics/runs.md#tgnvariant1) | [tgnBaseline](./genomics/runs.md#tgnbaseline)

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

- :fontawesome-solid-user-group: **Participant:** [uwaterloo.cormack](./genomics/participants.md#uwaterloo.cormack)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uwaterloo.genomics.robust.pdf](http://trec.nist.gov/pubs/trec12/papers/uwaterloo.genomics.robust.pdf)
- :material-file-search: **Runs:** [uwmtg03btrf](./genomics/runs.md#uwmtg03btrf) | [uwmtg03atrf](./genomics/runs.md#uwmtg03atrf)

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

- :fontawesome-solid-user-group: **Participant:** [uillinoisuc.zhai](./genomics/participants.md#uillinoisuc.zhai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.robust.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.robust.genomics.pdf)
- :material-file-search: **Runs:** [UIUC03Ga](./genomics/runs.md#uiuc03ga) | [UIUC03Gb](./genomics/runs.md#uiuc03gb)

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

## Web 

#### Overview of the TREC 2003 Web Track

_Nick Craswell, David Hawking, Ross Wilkinson, Mingfang Wu_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/WEB.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec12/papers/WEB.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC 2003 web track consisted of both a non-interactive stream and an interactive stream. Both streams worked with the .GOV test collection. The non-interactive stream continued an investigation into the importance of homepages in Web ranking, via both a Topic Distillation task and a Navigational task. In the topic distillation task, systems were expected to return a list of the homepages of sites relevant to each of a series of broad queries. This differs from previous homepage experiments in that queries may have multiple correct answers. The navigational task required systems to return a particular desired web page as early as possible in the ranking in response to queries. In half of the queries, the target answer was the homepage of a site and the query was derived from the name of the site (Homepage finding) while in the other half, the target answers were not homepages and the queries were derived from the name of the page (Named page finding). The two types of query were arbitrarily mixed and not identified. The interactive stream focused on human participation in a topic distillation task over the .GOV collection. Studies conducted by the two participating groups compared a search engine using au- tomatic topic distillation features with the same engine with those features disabled in order to determine whether the automatic topic distillation features assisted the users in the performance of their tasks and whether humans could achieve better results than the automatic system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellHWW03.bib) "
	```
	@inproceedings{DBLP:conf/trec/CraswellHWW03,
		author = {Nick Craswell and David Hawking and Ross Wilkinson and Mingfang Wu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2003 Web Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {78--92},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/WEB.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CraswellHWW03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 2003 Experiments Using Web Topic-Centric Link  Analysis

_Paricha Ingongngam, Arnon Rungsawang_

- :fontawesome-solid-user-group: **Participant:** [kasetsartu](./web/participants.md#kasetsartu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/kasetsartu.pdf](http://trec.nist.gov/pubs/trec12/papers/kasetsartu.pdf)
- :material-file-search: **Runs:** [KUCONTENT](./web/runs.md#kucontent)

??? abstract "Abstract"
	
	In TREC 2003, our experiments have been concentrated only on the topic distillation task. We first simply apply the term-based technique to the .GOV web collection, and then re-rank the retrieval results using a link analysis algorithm in order to boost the retrieval precision. Our link analysis has been inspired from the original PageRank, but focused on the web topic during the iterative score propagation. We hybridize the term-based retrieval scores with our link analysis approach. From the experiments, the results show that the combination of those scores still provides inadequate precision improvement.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/IngongngamR03.bib) "
	```
	@inproceedings{DBLP:conf/trec/IngongngamR03,
		author = {Paricha Ingongngam and Arnon Rungsawang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Report on the {TREC} 2003 Experiments Using Web Topic-Centric Link Analysis},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {363--367},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/kasetsartu.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/IngongngamR03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fondazione Ugo Bordoni at TREC 2003: Robust and Web Track

_Giambattista Amati, Claudio Carpineto, Giovanni Romano_

- :fontawesome-solid-user-group: **Participant:** [fub.carpineto](./web/participants.md#fub.carpineto)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/fub.robust.web.pdf](http://trec.nist.gov/pubs/trec12/papers/fub.robust.web.pdf)
- :material-file-search: **Runs:** [fub03IneBMt](./web/runs.md#fub03inebmt) | [fub03IneBBt](./web/runs.md#fub03inebbt) | [fub03InLBt](./web/runs.md#fub03inlbt) | [fub03InLBo1t](./web/runs.md#fub03inlbo1t) | [fub03InBMt](./web/runs.md#fub03inbmt)

??? abstract "Abstract"
	
	Our participation in TREC 2003 aims to adapt the use of the DFR (Divergence From Randomness) models with Query Expansion (QE) to the robust track and the topic distillation task of the Web track. We focus on the robust track, where the utilization of QE improves the global performance but hurts the performance on the worst topics. In partic- ular, we study the problem of the selective application of the query expansion. We define two information theory based functions, InfoDFR and InfoQ, predicting respectively the AP (Average Precision) of queries and the AP increment of queries after the application of QE. InfoQ is used to selectively apply QE. We show that the use of InfoQ achieves the same performance comparable of the unexpanded method on the set of the worst topics, but a better performance than full QE on the entire set of topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmatiCR03.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmatiCR03,
		author = {Giambattista Amati and Claudio Carpineto and Giovanni Romano},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Fondazione Ugo Bordoni at {TREC} 2003: Robust and Web Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {234--245},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/fub.robust.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AmatiCR03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Juru at TREC 2003 - Topic Distillation using Query-Sensitive Tuning  and Cohesiveness Filtering

_Einat Amitay, David Carmel, Adam Darlow, Michael Herscovici, Ronny Lempel, Aya Soffer, Reiner Kraft, Jason Y. Zien_

- :fontawesome-solid-user-group: **Participant:** [ibmhaifa.carmel](./web/participants.md#ibmhaifa.carmel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ibm-haifa.web.pdf](http://trec.nist.gov/pubs/trec12/papers/ibm-haifa.web.pdf)
- :material-file-search: **Runs:** [JuruFull](./web/runs.md#jurufull) | [JuruNoAnchor](./web/runs.md#jurunoanchor) | [JuruNoSS](./web/runs.md#jurunoss) | [JuruNoCohes](./web/runs.md#jurunocohes) | [JuruNoQDiff](./web/runs.md#jurunoqdiff)

??? abstract "Abstract"
	
	This is the third year that our group participates in TREC's Web track, the second year in the topic distillation task. Our experiments last year, as well as those of other participants, indicated that sophisticated link-based measures did not significantly improve search results in comparison to standard text-based relevance scoring. We thus focused our experiments this year on improving the ranking algorithms of our core search engine, Juru, and on developing measures that are good indicators of topical pages. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmitayCDHLSKZ03.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmitayCDHLSKZ03,
		author = {Einat Amitay and David Carmel and Adam Darlow and Michael Herscovici and Ronny Lempel and Aya Soffer and Reiner Kraft and Jason Y. Zien},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Juru at {TREC} 2003 - Topic Distillation using Query-Sensitive Tuning and Cohesiveness Filtering},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {276--282},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/ibm-haifa.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AmitayCDHLSKZ03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Robust and Web Retrieval with Document-Centric Integral Impacts

_Vo Ngoc Anh, Alistair Moffat_

- :fontawesome-solid-user-group: **Participant:** [umelbourne.moffat](./web/participants.md#umelbourne.moffat)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/umelbourne.web.pdf](http://trec.nist.gov/pubs/trec12/papers/umelbourne.web.pdf)
- :material-file-search: **Runs:** [MU03np3](./web/runs.md#mu03np3) | [MU03np4](./web/runs.md#mu03np4) | [MU03np5](./web/runs.md#mu03np5) | [MU03td04](./web/runs.md#mu03td04) | [MU03td03](./web/runs.md#mu03td03) | [MU03td05](./web/runs.md#mu03td05) | [MU03td01](./web/runs.md#mu03td01) | [MU03np1](./web/runs.md#mu03np1)

??? abstract "Abstract"
	
	This paper reports the experiments done at The University of Melbourne for the Robust and Web tracks of TREC-2003. We explore the idea of determining the impact of a term locally within the document and in a qualitative manner instead of a quantitative one. The impact of each distinct term in a document or query text is defined to be a small integer. The scalar product of the impact vector for a document and the impact vector for a query is taken to be the similarity score between them, an arrangement that allows very fast query evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnhM03.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnhM03,
		author = {Vo Ngoc Anh and Alistair Moffat},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Robust and Web Retrieval with Document-Centric Integral Impacts},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {726--731},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/umelbourne.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnhM03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT at TREC 2003, Task Classification and Document Structrure  for Known-Item Search

_Steven M. Beitzel, Eric C. Jensen, Rebecca Cathey, Ling Ma, David A. Grossman, Ophir Frieder, Abdur Chowdhury, Greg Pass, Herman Vandermolen_

- :fontawesome-solid-user-group: **Participant:** [iit.grossman](./web/participants.md#iit.grossman)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/iit.web.pdf](http://trec.nist.gov/pubs/trec12/papers/iit.web.pdf)
- :material-file-search: **Runs:** [iit03sau](./web/runs.md#iit03sau) | [iit03sa](./web/runs.md#iit03sa) | [iit03wtaez](./web/runs.md#iit03wtaez) | [iit03wp75](./web/runs.md#iit03wp75) | [iit03su](./web/runs.md#iit03su)

??? abstract "Abstract"
	
	This year's TREC 2003 web task incorporated two retrieval tasks into a single set of experiments for Known-Item retrieval. We hypothesized that not all retrieval tasks should use the same retrieval approach when a single search entry point is used. We applied task classifiers on top of traditional web retrieval approaches. Our traditional retrieval is based on fusion of result sets generated by query runs over independent parts of the document structure. Our task classifiers combine query term analysis with known information resources and URL depth. This approach to task classification shows promise: our classified runs improved overall MRR effectiveness over our traditional retrieval results by ~10%; provided an MRR of .665; ranked 87% of relevant results in the top 10; correctly ranked the #1result 56% of the time. 67% of the queries performed above the average, and 49% above the median.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BeitzelJCMGFCPV03.bib) "
	```
	@inproceedings{DBLP:conf/trec/BeitzelJCMGFCPV03,
		author = {Steven M. Beitzel and Eric C. Jensen and Rebecca Cathey and Ling Ma and David A. Grossman and Ophir Frieder and Abdur Chowdhury and Greg Pass and Herman Vandermolen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IIT} at {TREC} 2003, Task Classification and Document Structrure for Known-Item Search},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {311--320},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/iit.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BeitzelJCMGFCPV03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure at TREC 2003 Web track - Topic Distillation Task

_Mohand Boughanem, Karen Sauvagnat, Cecile Laffaire_

- :fontawesome-solid-user-group: **Participant:** [irit-sig.boughanem](./web/participants.md#irit-sig.boughanem)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/irit-sig.web.pdf](http://trec.nist.gov/pubs/trec12/papers/irit-sig.web.pdf)
- :material-file-search: **Runs:** [Merc1td](./web/runs.md#merc1td) | [Merc1ti](./web/runs.md#merc1ti) | [Merc2tp](./web/runs.md#merc2tp) | [Merc2tm](./web/runs.md#merc2tm)

??? abstract "Abstract"
	
	The tests performed for TREC'2003 web track were focused on the topic distillation part. The aim of our participation is to validate the results we obtained last year and to test the use of term proximity on Mercure model. As last year, ad-hoc methodologies were used to answer the topic distillation task. 4 runs were submitted to NIST this year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoughanemSL03.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoughanemSL03,
		author = {Mohand Boughanem and Karen Sauvagnat and Cecile Laffaire},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Mercure at {TREC} 2003 Web track - Topic Distillation Task},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {343--348},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/irit-sig.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoughanemSL03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC12 Web and Interactive Tracks at CSIRO

_Nick Craswell, David Hawking, Trystan Upstill, Alistair McLean, Ross Wilkinson, Mingfang Wu_

- :fontawesome-solid-user-group: **Participant:** [CSIRO](./web/participants.md#csiro)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/csiro.web.pdf](http://trec.nist.gov/pubs/trec12/papers/csiro.web.pdf)
- :material-file-search: **Runs:** [csiro03td01](./web/runs.md#csiro03td01) | [csiro03td02](./web/runs.md#csiro03td02) | [csiro03td03](./web/runs.md#csiro03td03) | [csiro03td04](./web/runs.md#csiro03td04) | [csiro03td05](./web/runs.md#csiro03td05) | [csiro03ki01](./web/runs.md#csiro03ki01) | [csiro03ki02](./web/runs.md#csiro03ki02) | [csiro03ki03](./web/runs.md#csiro03ki03) | [csiro03ki04](./web/runs.md#csiro03ki04) | [csiro03ki05](./web/runs.md#csiro03ki05)

??? abstract "Abstract"
	
	This year, CSIRO teams participated in all three tasks of the web track; these being: the automatic topic distillation task, the home/named page finding task and the interactive topic distillation task. This paper describes our approaches, experiments and results. The following section describes our experiments in the two automatic tasks, and Section 3 describes our experiment in the interactive task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellHUMWW03.bib) "
	```
	@inproceedings{DBLP:conf/trec/CraswellHUMWW03,
		author = {Nick Craswell and David Hawking and Trystan Upstill and Alistair McLean and Ross Wilkinson and Mingfang Wu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC12} Web and Interactive Tracks at {CSIRO}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {193--203},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/csiro.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CraswellHUMWW03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Non-Functional Prototype at TREC 2003

_Brian D. Davison, Wei Zhang, Josh Miller_

- :fontawesome-solid-user-group: **Participant:** [lehighu.davison](./web/participants.md#lehighu.davison)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/lehighu.web.pdf](http://trec.nist.gov/pubs/trec12/papers/lehighu.web.pdf)
- :material-file-search: **Runs:** [03wume296](./web/runs.md#03wume296) | [03wume298](./web/runs.md#03wume298) | [03wume206](./web/runs.md#03wume206) | [03wume359](./web/runs.md#03wume359)

??? abstract "Abstract"
	
	As a first attempt at participation in the TREC competition, we built a system which produced some preliminary results, but was unable to generate the quality of results that we expected. While we were able to submit four base-line runs, bugs were discovered in the final hours before the deadline making it impossible to submit results using our intended implementation. We have since found additional coding errors, making our submitted results expectedly poor. The size of our index dataset was approximately 3.8GB without compression. We did not use term position information nor any kind of phrasal indexing.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DavisonZM03.bib) "
	```
	@inproceedings{DBLP:conf/trec/DavisonZM03,
		author = {Brian D. Davison and Wei Zhang and Josh Miller},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Non-Functional Prototype at {TREC} 2003},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {383--385},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/lehighu.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DavisonZM03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMBC at TREC 12

_Srikanth Kallurkar, Yongmei Shi, R. Scott Cost, Charles K. Nicholas, Akshay Java, Christopher James, Sowjanya Rajavaram, Vishal Shanbhag, Sachin Bhatkar, Drew Ogle_

- :fontawesome-solid-user-group: **Participant:** [umarylandbc.kallurkar](./web/participants.md#umarylandbc.kallurkar)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/umbc.web.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/umbc.web.novelty.pdf)
- :material-file-search: **Runs:** [C2B](./web/runs.md#c2b) | [C2A](./web/runs.md#c2a)

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

#### Approaches to Robust and Web Retrieval

_Jaap Kamps, Christof Monz, Maarten de Rijke, Börkur Sigurbjörnsson_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.derijke](./web/participants.md#uamsterdam.derijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uamsterdam.web.robust.pdf](http://trec.nist.gov/pubs/trec12/papers/uamsterdam.web.robust.pdf)
- :material-file-search: **Runs:** [UAmsT03WnOWS](./web/runs.md#uamst03wnows) | [UAmsT03WnLM](./web/runs.md#uamst03wnlm) | [UAmsT03WnLn3](./web/runs.md#uamst03wnln3) | [UAmsT03WnLM3](./web/runs.md#uamst03wnlm3) | [UAmsT03WnMSW](./web/runs.md#uamst03wnmsw) | [UAmsT03WtOk3](./web/runs.md#uamst03wtok3) | [UAmsT03WtLM3](./web/runs.md#uamst03wtlm3) | [UAmsT03WtOkI](./web/runs.md#uamst03wtoki) | [UAmsT03WtLMI](./web/runs.md#uamst03wtlmi) | [UAmsT03WtOkC](./web/runs.md#uamst03wtokc)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2003 Robust and Web tracks. For the Robust track, we experimented with the impact of stemming and feedback on the worst scoring topics. Our main finding is the effectiveness of stemming on poorly performing topics, which sheds new light on the role of morphological normalization in information retrieval. For both the home/named page finding and topic distillation tasks of the Web track, we experimented with different document representations and retrieval models. Our main finding is effectiveness of the anchor text index for both tasks, suggesting that compact document representations are a fruitful strategy for scaling-up retrieval systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KampsMRS03.bib) "
	```
	@inproceedings{DBLP:conf/trec/KampsMRS03,
		author = {Jaap Kamps and Christof Monz and Maarten de Rijke and B{\"{o}}rkur Sigurbj{\"{o}}rnsson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Approaches to Robust and Web Retrieval},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {594--599},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uamsterdam.web.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KampsMRS03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Document Structure with IR Tools

_Gregory B. Newby_

- :fontawesome-solid-user-group: **Participant:** [ualaska.newby](./web/participants.md#ualaska.newby)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ualaska.web.pdf](http://trec.nist.gov/pubs/trec12/papers/ualaska.web.pdf)
- :material-file-search: **Runs:** [irttgrep](./web/runs.md#irttgrep) | [irtfgrep](./web/runs.md#irtfgrep)

??? abstract "Abstract"
	
	The IRTools software toolkit was modified for 2003 to utilize a MySQL database for the inverted index. Indexing was for each occurrence of each term in the collection, with HTML structure, location offset, paragraph, and subdocument weight considered. This structure enables some more sophisticated queries than a “bag of words” approach. Post hoc results from the TREC 2002 Named Page Web task are presented, in which a staged fall through approach to topic processing yielded good results, with exact precision of 0.49. The paper also provides an overview of IRTools and its interactive interface, as well as an invitation for IR researchers to get involved with the GridIR standards formation process.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Newby03.bib) "
	```
	@inproceedings{DBLP:conf/trec/Newby03,
		author = {Gregory B. Newby},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Document Structure with {IR} Tools},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {568--577},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/ualaska.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Newby03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Structural Information and the Use of Priors in Mixed Named-Page  and Homepage Finding

_Paul Ogilvie, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [cmu.callan](./web/participants.md#cmu.callan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/cmu-dir.web.pdf](http://trec.nist.gov/pubs/trec12/papers/cmu-dir.web.pdf)
- :material-file-search: **Runs:** [LmrEq](./web/runs.md#lmreq) | [LmrEqUrl](./web/runs.md#lmrequrl) | [LmrEst](./web/runs.md#lmrest) | [LmrEstUrl](./web/runs.md#lmresturl)

??? abstract "Abstract"
	
	This paper presents Carnegie Mellon University's experiments on the mixed named-page and homepage finding task of the TREC 12 Web Track. Our results were strong; we achieved the success using language models estimated from combining information from document text, in-link text, and information present in the structure of the documents. We also present experiments using expectations about posterior distributions to create class-based prior probabilities. We find that priors do provide a large gain for our official runs, but we do further experiments that show the priors do not always help. Some preliminary analysis shows that the prior probabilities are not providing the desired posterior distributions. In cases where applying the priors harm performance, the observed posterior distributions in the rankings are far off of the desired posterior distributions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OgilvieC03.bib) "
	```
	@inproceedings{DBLP:conf/trec/OgilvieC03,
		author = {Paul Ogilvie and Jamie Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Structural Information and the Use of Priors in Mixed Named-Page and Homepage Finding},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {177--184},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/cmu-dir.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OgilvieC03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Meiji University Web and Novelty Track Experiments at TREC 2003

_Ryosuke Ohgaya, Akiyoshi Shimmura, Tomohiro Takagi, Akiko N. Aizawa_

- :fontawesome-solid-user-group: **Participant:** [meijiu.takagi](./web/participants.md#meijiu.takagi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/meijiu.web.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/meijiu.web.novelty.pdf)
- :material-file-search: **Runs:** [meijihilw1](./web/runs.md#meijihilw1) | [meijihilw2](./web/runs.md#meijihilw2) | [meijihilw3](./web/runs.md#meijihilw3) | [meijihilw4](./web/runs.md#meijihilw4) | [meijihilw5](./web/runs.md#meijihilw5)

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

#### University of Glasgow at the Web Track: Dynamic Application of Hyperlink  Analysis using the Query Scope

_Vassilis Plachouras, Iadh Ounis, Cornelis Joost van Rijsbergen, Fidel Cacheda_

- :fontawesome-solid-user-group: **Participant:** [uglasgow.ounis](./web/participants.md#uglasgow.ounis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uglasgow.web.pdf](http://trec.nist.gov/pubs/trec12/papers/uglasgow.web.pdf)
- :material-file-search: **Runs:** [uogki1c](./web/runs.md#uogki1c) | [uogki2ca](./web/runs.md#uogki2ca) | [uogki3cah](./web/runs.md#uogki3cah) | [uogki4cahs](./web/runs.md#uogki4cahs) | [uogtd1c](./web/runs.md#uogtd1c) | [uogtd2ca](./web/runs.md#uogtd2ca) | [uogtd3cas](./web/runs.md#uogtd3cas) | [uogtd4cahs](./web/runs.md#uogtd4cahs) | [uogtd5cass](./web/runs.md#uogtd5cass)

??? abstract "Abstract"
	
	This year, our participation to the Web track aims at combining dynamically evidence from both content and hyperlink analysis. To this end, we introduce a decision mechanism based on the so-called query scope concept. For the topic distillation task, we find that the use of anchor text increases precision significantly over content- only retrieval, a result that contrasts with our TREC11 findings. Using the query scope, we show that a selective application of hyperlink analysis, or URL-based scores, is effective for the more generic queries, improving the overall precision. In fact, our most effective runs use the decision mechanism and outperform significantly the content and anchor text retrieval. For the known item task, we employ the query scope in order to distinguish the named page queries from the home page queries, obtaining results close to the content and anchor text baseline.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PlachourasORC03.bib) "
	```
	@inproceedings{DBLP:conf/trec/PlachourasORC03,
		author = {Vassilis Plachouras and Iadh Ounis and Cornelis Joost van Rijsbergen and Fidel Cacheda},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at the Web Track: Dynamic Application of Hyperlink Analysis using the Query Scope},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {646--652},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uglasgow.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PlachourasORC03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 2003 Experiment: Genomic and Web Searches

_Jacques Savoy, Yves Rasolofo, Laura Perret_

- :fontawesome-solid-user-group: **Participant:** [neuchatelu.savoy](./web/participants.md#neuchatelu.savoy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uneuchatel.genome.web.pdf](http://trec.nist.gov/pubs/trec12/papers/uneuchatel.genome.web.pdf)
- :material-file-search: **Runs:** [UniNEtd5](./web/runs.md#uninetd5) | [UniNEtd1](./web/runs.md#uninetd1) | [UniNEtd2](./web/runs.md#uninetd2) | [UniNEtd3](./web/runs.md#uninetd3) | [UniNEtd4](./web/runs.md#uninetd4) | [UniNEnp1](./web/runs.md#uninenp1) | [UniNEnp2](./web/runs.md#uninenp2) | [UniNEnp3](./web/runs.md#uninenp3) | [UniNEnp4](./web/runs.md#uninenp4) | [UniNEnp5](./web/runs.md#uninenp5)

??? abstract "Abstract"
	
	This year we took part in the genomic information retrieval and information extraction tasks, as well as the named page and topic distillation searches. In carrying out the last two tasks, we made use of link anchor information and document content in order to construct Web page representatives. This type of document representation uses multi-vectors to highlight the importance of both hyperlink and document content.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SavoyRP03.bib) "
	```
	@inproceedings{DBLP:conf/trec/SavoyRP03,
		author = {Jacques Savoy and Yves Rasolofo and Laura Perret},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Report on the {TREC} 2003 Experiment: Genomic and Web Searches},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {739--750},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uneuchatel.genome.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SavoyRP03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Relevance Propagation for Topic Distillation UIUC TREC 2003 Web  Track Experiments

_Azadeh Shakery, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [uillinoisuc.zhai](./web/participants.md#uillinoisuc.zhai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.web.pdf](http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.web.pdf)
- :material-file-search: **Runs:** [UIUC03Wb](./web/runs.md#uiuc03wb) | [UIUC03Wp](./web/runs.md#uiuc03wp) | [UIUC03W2s](./web/runs.md#uiuc03w2s) | [UIUC03Wu1](./web/runs.md#uiuc03wu1) | [UIUC03Wu2](./web/runs.md#uiuc03wu2)

??? abstract "Abstract"
	
	In this paper, we report our experiments on the Web Track TREC-2003. We submitted five runs for the topic distillation task. Our goal was to evaluate the standard language modeling algorithms for topic distillation, as well as to explore the impact of combining link and content information. We proposed a new general relevance propagation model for combining link and content information, and explored a number of specific methods derived from the model. The experiment results show that combining link and content information generally performs better than using only content information, though the amount of improvement is sensitive to the document collection and tuning of parameters.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShakeryZ03.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShakeryZ03,
		author = {Azadeh Shakery and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Relevance Propagation for Topic Distillation {UIUC} {TREC} 2003 Web Track Experiments},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {673--677},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShakeryZ03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Towards a Sense Based Document Representation for Internet Information  Retrieval

_Christopher Stokoe, John Tait_

- :fontawesome-solid-user-group: **Participant:** [usunderland.stokoe](./web/participants.md#usunderland.stokoe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/usunderland.web.pdf](http://trec.nist.gov/pubs/trec12/papers/usunderland.web.pdf)
- :material-file-search: **Runs:** [TBBASE](./web/runs.md#tbbase) | [SBBASE](./web/runs.md#sbbase) | [SBUNIQUE](./web/runs.md#sbunique) | [TBUNIQUE](./web/runs.md#tbunique)

??? abstract "Abstract"
	
	We describe an attempt to use word sense as an alternate text representation within an information retrieval system in order to enhance retrieval effectiveness. A performance comparison between a term and sense based system was carried out indicating increased retrieval effectiveness using a sense based representation. These increases come about by using a retrieval strategy designed to down rank documents containing query terms identified as being used in an infrequent sense.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StokoeT03.bib) "
	```
	@inproceedings{DBLP:conf/trec/StokoeT03,
		author = {Christopher Stokoe and John Tait},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Towards a Sense Based Document Representation for Internet Information Retrieval},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {791--795},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/usunderland.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StokoeT03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2003 Novelty and Web Track at ICT

_Jian Sun, Zhe Yang, Wenfeng Pan, Huaping Zhang, Bin Wang, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [cas-ict.bin](./web/participants.md#cas-ict.bin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.novelty.web.pdf](http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.novelty.web.pdf)
- :material-file-search: **Runs:** [ICTWebTD12A](./web/runs.md#ictwebtd12a) | [ICTWebTD12B](./web/runs.md#ictwebtd12b) | [ICTWebTD12C](./web/runs.md#ictwebtd12c) | [ICTWebKI12A](./web/runs.md#ictwebki12a) | [ICTWebKI12B](./web/runs.md#ictwebki12b) | [ICTWebKI12C](./web/runs.md#ictwebki12c)

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

#### Robust, Web and Genomic Retrieval with Hummingbird SearchServer at  TREC 2003

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird.tomlinson](./web/participants.md#hummingbird.tomlinson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/hummingbird.robust.web.genomic.pdf](http://trec.nist.gov/pubs/trec12/papers/hummingbird.robust.web.genomic.pdf)
- :material-file-search: **Runs:** [humNP03pl](./web/runs.md#humnp03pl) | [humTD03pl](./web/runs.md#humtd03pl) | [humTD03upl](./web/runs.md#humtd03upl) | [humNP03upl](./web/runs.md#humnp03upl) | [humTD03uhpl](./web/runs.md#humtd03uhpl) | [humNP03uhpl](./web/runs.md#humnp03uhpl) | [humNP03l](./web/runs.md#humnp03l) | [humNP03up](./web/runs.md#humnp03up) | [humTD03up](./web/runs.md#humtd03up) | [humTD03l](./web/runs.md#humtd03l)

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

#### Microsoft Research Asia at the Web Track of TREC 2003

_Ji-Rong Wen, Ruihua Song, Deng Cai, Kaihua Zhu, Shipeng Yu, Shaozhi Ye, Wei-Ying Ma_

- :fontawesome-solid-user-group: **Participant:** [microsoftasia.wen](./web/participants.md#microsoftasia.wen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/microsoft-asia.web.pdf](http://trec.nist.gov/pubs/trec12/papers/microsoft-asia.web.pdf)
- :material-file-search: **Runs:** [MSRA1001](./web/runs.md#msra1001) | [MSRA3](./web/runs.md#msra3) | [MSRA4003](./web/runs.md#msra4003) | [MSRA4002](./web/runs.md#msra4002) | [MSRA1002](./web/runs.md#msra1002) | [MSRANP1](./web/runs.md#msranp1) | [MSRANP3](./web/runs.md#msranp3) | [MSRANP2](./web/runs.md#msranp2)

??? abstract "Abstract"
	
	This is the first year that our group participates in the Web track of the TREC conference. Here we report our system and methods on the topic distillation task and the home/ named page finding task. All of our experiments are conducted on a Web search platform we designed and developed from scratch. We originally want to use an existing retrieval system such as Okapi or the full text search mechanism of SQL Server. But we soon find the limitations of such a strategy - these systems cannot fully support some important Web search functions such as link analysis and anchor text, and they also lack of the flexibility to arbitrarily adjust some parameters of add new ranking functions. So we decided to design and implement a research platform to let researchers to test various algorithms or new ideas easily and, also, to conduct the TREC experiments easily. We will introduce the framework of this system in the 'Platform' section. We feel that this year's topic distillation is more close to the real Web search scenarios. The target is to find a list of key resources for a particular (broad) topic and 'key resources' are defined as the entry pages of websites. So, different from the previous years, we think that link analysis may play a positive role on identifying key resources in this year. As a consequence, we focus on using different link analysis techniques to enhance the relevance ranking. In particularly, we propose a novel block-based HITS algorithm to solve the noisy link and topic drifting problems of the classic HITS algorithm. The basic idea is to segment each Web page into multiple semantic blocks using a vision-based page segmentation algorithm we developed before. Then the main steps of the HITS algorithms, such as getting the seeds, expanding the neighbors using inlinks and outlinks, and calculating hub/authority values, can be performed at the block level instead of at the page level. Thus the noisy link and topic drifting problems can be effectively overcome. We will detail these techniques in the 'Page Layout Analysis' and 'Block-based HITS' section. To our understanding, the biggest difference of this year's topic distillation task from last year is that, in general, only one most 'suitable' page for each website should be returned as a top-ranked result. Any other page at the same website should not be included in the results or ranked highly since it is a 'part of a larger site also principally devoted to the topic', despite that the page also 'is principally devoted to the topic'. Therefore, we construct a hierarchical site map for each website by building up the parent-children relationships of Web pages in the GOV dataset. Then we apply a site compression technique to select the most suitable entry pages for websites among the retrieval results and return these entry pages as top-ranked pages. This site compression method has proved to be quite effective to increase the p@10 precision if used appropriately, and will be introduced in the 'Site Compression' section. We totally submitted 5 runs for the topic distillation task and 3 runs for the home/named page finding task. In the 'Experimental results' section, we will introduce these runs and their evaluation results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WenSCZYYM03.bib) "
	```
	@inproceedings{DBLP:conf/trec/WenSCZYYM03,
		author = {Ji{-}Rong Wen and Ruihua Song and Deng Cai and Kaihua Zhu and Shipeng Yu and Shaozhi Ye and Wei{-}Ying Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Research Asia at the Web Track of {TREC} 2003},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {408--417},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/microsoft-asia.web.pdf},
		timestamp = {Wed, 13 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WenSCZYYM03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC-2003 Web Track

_Kiduk Yang, Dan E. Albertson_

- :fontawesome-solid-user-group: **Participant:** [indianau.seki](./web/participants.md#indianau.seki)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/indianau.web.pdf](http://trec.nist.gov/pubs/trec12/papers/indianau.web.pdf)
- :material-file-search: **Runs:** [widittdb1](./web/runs.md#widittdb1) | [widittdb1r1](./web/runs.md#widittdb1r1) | [widittdf1r1](./web/runs.md#widittdf1r1) | [widittdf1r2](./web/runs.md#widittdf1r2) | [widitpfb1](./web/runs.md#widitpfb1) | [widitpff1](./web/runs.md#widitpff1)

??? abstract "Abstract"
	
	[...] In our earlier studies (Yang, 2002a; Yang, 2002b), where we investigated various fusion approaches for ad-hoc retrieval using the WT10g collection, we found that simplistic approach that combine the results of content- and link-based retrieval results did not enhance retrieval performance in general. TREC participants in recent Web track environment, however, found that use of non-textual information such as hyperlinks, document structure, and URL could be beneficial for specific tasks such as topic distillation and named/home page finding tasks. We believe that this is not only due to the change in the retrieval environment (i.e. test collection, retrieval task) but also the result of more dynamic approach to combining multiple sources of evidence than straightforward result merging. Thus, our focus in TREC- 2003 Web track was in exploring fusion strategies that utilize various information sources in a dynamic manner to optimize retrieval for specific search environment. For our experiment, we used the experimental fusion retrieval system called WIDIT to combine content and link information, and then reranked the combined result based on heuristics arrived at from dynamic system tuning process.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangA03.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangA03,
		author = {Kiduk Yang and Dan E. Albertson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC-2003} Web Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {328--336},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/indianau.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangA03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### VT at TREC-2003: The Web Track Report

_Rui Yang, Li Wang, Weiguo Fan, Wensi Xi, Ming Luo, Ye Zhou, Edward A. Fox_

- :fontawesome-solid-user-group: **Participant:** [vatech.xi](./web/participants.md#vatech.xi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/vatech.web.pdf](http://trec.nist.gov/pubs/trec12/papers/vatech.web.pdf)
- :material-file-search: **Runs:** [VTtdgp41](./web/runs.md#vttdgp41) | [VTtdgp52](./web/runs.md#vttdgp52) | [VTtdok4](./web/runs.md#vttdok4) | [VTtdgp33](./web/runs.md#vttdgp33) | [VTtdgp5055](./web/runs.md#vttdgp5055) | [VTnhpok1](./web/runs.md#vtnhpok1) | [VTnhpgp42](./web/runs.md#vtnhpgp42) | [VTnhpgp33](./web/runs.md#vtnhpgp33) | [VTnhpgp55](./web/runs.md#vtnhpgp55) | [VTnhpgpd4](./web/runs.md#vtnhpgpd4)

??? abstract "Abstract"
	
	This year, we participated in the Web Track in addition to the Robust Track. We submitted results on both topic distillation and home page/named page finding tasks. As our time and human resources were limited for taking two tasks simultaneously, in this task we only concentrate on testing our ranking function discovery technique, ARRANGER (Automatic Rendering of RANking functions by GEnetic pRogramming) [Fan 2003a, Fan 2003b], which uses Genetic Programming (GP) to discover the “optimal” ranking functions for various information needs. From Web Track 2002, the training, testing and validation data sets are constructed in the same manner as in Robust Track. Our ARRANGER engine works on those data sets and automatically searches for the “best” ranking functions. The best runs are selected for submission according to their performance on queries in Web track 2002. Our paper is organized as follows. Section 2 states our research objectives. Section 3 describes basic data processing steps. Section 4 summarizes the GP algorithm used in our system and detailed information about how we use GP to find ranking function. Section 5 shows the official submission results in comparison with the other TREC teams.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangWFXLZF03.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangWFXLZF03,
		author = {Rui Yang and Li Wang and Weiguo Fan and Wensi Xi and Ming Luo and Ye Zhou and Edward A. Fox},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{VT} at {TREC-2003:} The Web Track Report},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {837},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/vatech.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangWFXLZF03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2003: Novelty, Robust and Web

_Min Zhang, Chuan Lin, Yiqun Liu, Leo Zhao, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [tsinghuau.ma](./web/participants.md#tsinghuau.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/tsinghuau.novelty.robust.web.pdf](http://trec.nist.gov/pubs/trec12/papers/tsinghuau.novelty.robust.web.pdf)
- :material-file-search: **Runs:** [THUIRpf0301](./web/runs.md#thuirpf0301) | [THUIRpf0302](./web/runs.md#thuirpf0302) | [THUIRpf0303](./web/runs.md#thuirpf0303) | [THUIRpf0304](./web/runs.md#thuirpf0304) | [THUIRpf0305](./web/runs.md#thuirpf0305) | [THUIRtd0301](./web/runs.md#thuirtd0301) | [THUIRtd0303](./web/runs.md#thuirtd0303) | [THUIRtd0304](./web/runs.md#thuirtd0304) | [THUIRtd0305](./web/runs.md#thuirtd0305) | [THUIRtd0302](./web/runs.md#thuirtd0302)

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

## HARD 

#### HARD Track Overview in TREC 2003: High Accuracy Retrieval from  Documents

_James Allan_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/HARD.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec12/papers/HARD.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The effectiveness of ad-hoc retrieval systems appears to have reached a plateau. After several years of 10% gains every year in TREC, improvements dwindled or even stopped. This lack of progress was undoubtedly one of the reasons behind abandoning suspending the ad-hoc TREC after TREC-9. One plausible reason that document retrieval has been unable to improve is that the nature of the task requires that systems adopt “one size fits all” approaches. Given a query, a system will generally do best to return results that are good for an “average” user. Doing otherwise (i.e., targeting the results for a particular type of user) might result in substantial improvements on a query, but it is just as likely (in a TREC environment) to cause horrible degradation. By ignoring the user (or, more accurately, by treating all users identically), systems cannot possibly advance beyond a particular level of accuracy on average for a specific user. The goal of this track is to bring the user out of hiding, making him or her an integral part of both the search process and the evaluation. Systems do not have just a query to chew on, but also have as much information as possible about the person making the request, ranging from biographical data, through information seeking context, to expected type of result. The HARD track is a variant of the ad-hoc retrieval task from the past. It was a “pilot” track in 2003 because of the substantial extension on past evaluation—i.e., it is not clear how best to evaluate some of the aspects of the track, so at least for this year it was intended to be very open ended. HARD is also running as a track of TREC 2004. The HARD 2003 track ran in three phases: baseline, clarifying, and final. In the first phase, sites received and ran topics that were essentially idential to a classic TREC topic: title, description, and narrative fields. In the second phase, sites were able to acquire clarifying information about the topics. They had two means and could use either or both of them: 1. Biographical, contextual, preferred result format, and any information that disambiguates the query was captured when the topics were generated. This metadata about the query was made available for phase two. 2. Sites were permitted to generate a single “clarifying form” that the searcher would answer. For each topic, this form was a Web page that solicited useful information about the query or the searcher (e.g., disambiguating words in the query or finding out more information about what the searcher wants). The assumption was that the “clarification” would be generated automatically, but sites could have opted 0to generate manual clarification questions (can a librarian beat the best IR systems?). None did. In the final phase of the track, sites used all user- and query-information that they acquired to construct a better and more accurate ranked list. That substantially improved (because it is more targeted) list was submitted to NIST for evaluation. Because accurate retrieval could also just be pinpointed retrieval, an extension of the HARD track evaluated passage retrieval, a system's ability to select passages within documents that are relevant. Passage retrieval was an option available to sites, but could be ignored by returning full documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Allan03.bib) "
	```
	@inproceedings{DBLP:conf/trec/Allan03,
		author = {James Allan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{HARD} Track Overview in {TREC} 2003: High Accuracy Retrieval from Documents},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {24--37},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/HARD.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Allan03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Rutgers' HARD and Web Interactive Track Experiments at TREC 2003

_Nicholas J. Belkin, Diane Kelly, Hyuk-Jin Lee, Yuelin Li, Gheorghe Muresan, Muh-Chyun (Morris) Tang, Xiaojun Yuan, Xiao-Min Zhang_

- :fontawesome-solid-user-group: **Participant:** [rutgers.belkin](./hard/participants.md#rutgers.belkin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/rutgersu.hard.web.pdf](http://trec.nist.gov/pubs/trec12/papers/rutgersu.hard.web.pdf)
- :material-file-search: **Runs:** [rutbase1](./hard/runs.md#rutbase1) | [rutbase2](./hard/runs.md#rutbase2) | [Rutmeta](./hard/runs.md#rutmeta)

??? abstract "Abstract"
	
	This year, members of our group, the Information Interaction Laboratory at Rutgers, SCILS, participated in the HARD track, and in the Interactive Sub-track of the Web track. Since there were no points of commonality between the two separate investigations, we describe and present the results and conclusions for each separately.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BelkinKLLMTYZ03.bib) "
	```
	@inproceedings{DBLP:conf/trec/BelkinKLLMTYZ03,
		author = {Nicholas J. Belkin and Diane Kelly and Hyuk{-}Jin Lee and Yuelin Li and Gheorghe Muresan and Muh{-}Chyun (Morris) Tang and Xiaojun Yuan and Xiao{-}Min Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Rutgers' {HARD} and Web Interactive Track Experiments at {TREC} 2003},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {532--543},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/rutgersu.hard.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BelkinKLLMTYZ03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2003 Robust, HARD and QA Track Experiments using PIRCS

_Laszlo Grunfeld, Kui-Lam Kwok, Norbert Dinstl, Peter Deng_

- :fontawesome-solid-user-group: **Participant:** [queensc.kwok](./hard/participants.md#queensc.kwok)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/queens-college.robust.hard.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/queens-college.robust.hard.qa.pdf)
- :material-file-search: **Runs:** [pircHDBt1](./hard/runs.md#pirchdbt1) | [pircHDBtd1](./hard/runs.md#pirchdbtd1) | [pircHDC1t1](./hard/runs.md#pirchdc1t1) | [pircHDC2t2](./hard/runs.md#pirchdc2t2) | [pircHDC2t1](./hard/runs.md#pirchdc2t1) | [pircHDC3td1](./hard/runs.md#pirchdc3td1) | [pircHDC3td2](./hard/runs.md#pirchdc3td2) | [pircHDC1tp](./hard/runs.md#pirchdc1tp) | [pircHDC2tp](./hard/runs.md#pirchdc2tp) | [pircHDC3tdp](./hard/runs.md#pirchdc3tdp)

??? abstract "Abstract"
	
	We participated in the Robust, HARD and part of the QA tracks in TREC2003. For Robust track, a new way of doing ad-hoc retrieval based on web assistance was introduced. For HARD track, we followed the guideline to generate clarification forms for each topic so as to experiment with user feedback and metadata. In QA, we only did the factoid experiment. The approach to QA was similar to what we have used before, except that WWW searching was added as a front-end processing. These experiments are described in Sections 2, 3 and 4 respectively.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrunfeldKDD03.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrunfeldKDD03,
		author = {Laszlo Grunfeld and Kui{-}Lam Kwok and Norbert Dinstl and Peter Deng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2003 Robust, {HARD} and {QA} Track Experiments using {PIRCS}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {510--521},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/queens-college.robust.hard.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrunfeldKDD03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HARD Experiment at Maryland: From Need Negotiation to Automated  HARD Process

_Daqing He, Dina Demner-Fushman_

- :fontawesome-solid-user-group: **Participant:** [umaryland.he](./hard/participants.md#umaryland.he)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/umaryland-he.hard.pdf](http://trec.nist.gov/pubs/trec12/papers/umaryland-he.hard.pdf)
- :material-file-search: **Runs:** [umdbsne2tit](./hard/runs.md#umdbsne2tit) | [UMARIPVR4](./hard/runs.md#umaripvr4) | [UMARIPVR5](./hard/runs.md#umaripvr5) | [UMARIPVR7](./hard/runs.md#umaripvr7) | [UMARIPVR8](./hard/runs.md#umaripvr8)

??? abstract "Abstract"
	
	Our aim of participating in this year's High Accuracy Retrieval from Documents (HARD) track is to explore the possibility of developing an automated HARD retrieval model by leveraging existing models and theories about information need negotiation in information science. The clarification questions we developed are related to four different aspects of search topic, and four different techniques were developed to fully use the information collected from the user through these questions. Our initial analysis of the results indicates that this is a promising approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeD03.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeD03,
		author = {Daqing He and Dina Demner{-}Fushman},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{HARD} Experiment at Maryland: From Need Negotiation to Automated {HARD} Process},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {707--714},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/umaryland-he.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeD03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2003: HARD and QA

_Nasreen Abdul Jaleel, Andrés Corrada-Emmanuel, Qi Li, Xiaoyong Liu, Courtney Wade, James Allan_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./hard/participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/umass-amherst.hard.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/umass-amherst.hard.qa.pdf)
- :material-file-search: **Runs:** [ciirtpsgbas](./hard/runs.md#ciirtpsgbas) | [ciirtbas](./hard/runs.md#ciirtbas) | [ciirtdbas](./hard/runs.md#ciirtdbas) | [ciirtdpsgbas](./hard/runs.md#ciirtdpsgbas) | [ciirtrt](./hard/runs.md#ciirtrt) | [ciirtcftt](./hard/runs.md#ciirtcftt) | [ciirtmda](./hard/runs.md#ciirtmda) | [ciirtp](./hard/runs.md#ciirtp) | [ciirtmdap](./hard/runs.md#ciirtmdap) | [ciirtmdgp](./hard/runs.md#ciirtmdgp)

??? abstract "Abstract"
	
	The Center for Intelligent Information Retrieval (CIIR) at UMass Amherst participated in two tracks for TREC 2003: High Accuracy Retrieval from Documents (HARD) and Question Answering (QA). In the HARD track, we developed document metadata to correspond to query metadata requirements; implemented clarification forms based on query expansion, passage retrieval, and clustering; and retrieved variable length passages deemed most likely to be relevant. This work is discussed at length in Section 1. In the QA track, we focused on retrieving passages that were likely to contain the answer to the question
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JaleelCLLWA03.bib) "
	```
	@inproceedings{DBLP:conf/trec/JaleelCLLWA03,
		author = {Nasreen Abdul Jaleel and Andr{\'{e}}s Corrada{-}Emmanuel and Qi Li and Xiaoyong Liu and Courtney Wade and James Allan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass at {TREC} 2003: {HARD} and {QA}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {715--725},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/umass-amherst.hard.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JaleelCLLWA03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2003: HARD Experiments

_Liang Ma, Wei Tan, Qunxiu Chen, Shaoping Ma, Shuicai Shi, Shibin Xiao, Hongwei Wang, Hongjun Wang_

- :fontawesome-solid-user-group: **Participant:** [tsinghuau.ma](./hard/participants.md#tsinghuau.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/tsinghuau.hard.pdf](http://trec.nist.gov/pubs/trec12/papers/tsinghuau.hard.pdf)
- :material-file-search: **Runs:** [TUCSHardBR1](./hard/runs.md#tucshardbr1) | [TUCSHARD3](./hard/runs.md#tucshard3) | [TUCSHARD1](./hard/runs.md#tucshard1) | [TUCSHARD2](./hard/runs.md#tucshard2)

??? abstract "Abstract"
	
	In this paper, we describe ideas and related experiments of Tsinghua University IR group in TREC-12 HARD Track. In this track, we focus on an automatic delivering mechanism, which combine the existing IR methods and can provide a quick retrieval solution for the practical environment. The final official evaluation show the old ways perform not well, but we think the experiment data will be helpful in evaluating the new ideas developed by other teams.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MaTCMSXWW03.bib) "
	```
	@inproceedings{DBLP:conf/trec/MaTCMSXWW03,
		author = {Liang Ma and Wei Tan and Qunxiu Chen and Shaoping Ma and Shuicai Shi and Shibin Xiao and Hongwei Wang and Hongjun Wang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2003: {HARD} Experiments},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {552--555},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/tsinghuau.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MaTCMSXWW03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Cambridge at TREC-12: HARD track

_Stephen E. Robertson, Hugo Zaragoza, Michael J. Taylor_

- :fontawesome-solid-user-group: **Participant:** [microsoftc.robertson](./hard/participants.md#microsoftc.robertson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/microsoft-cambridge.hard.pdf](http://trec.nist.gov/pubs/trec12/papers/microsoft-cambridge.hard.pdf)
- :material-file-search: **Runs:** [MSRCbase](./hard/runs.md#msrcbase) | [MSRCs1e1p1](./hard/runs.md#msrcs1e1p1) | [MSRCs1e1p1B](./hard/runs.md#msrcs1e1p1b) | [MSRCs1e0p1](./hard/runs.md#msrcs1e0p1) | [MSRCs1e0p0](./hard/runs.md#msrcs1e0p0) | [MSRCs9e1p1](./hard/runs.md#msrcs9e1p1) | [MSRCs2e0p1](./hard/runs.md#msrcs2e0p1) | [MSRCs1e0p0B](./hard/runs.md#msrcs1e0p0b) | [MSRCs1e0p1B](./hard/runs.md#msrcs1e0p1b) | [MSRCs9e1p0](./hard/runs.md#msrcs9e1p0)

??? abstract "Abstract"
	
	We took part in the HARD track, with an active learning method to choose which document snippets to show the user for relevance feedback (compared to baseline feedback using snippets from the top-ranked documents). The active learning method is described, and some prior experiments with the Reuters collection are summarised. We also invited user feedback on phrases chosen from the top retrieved documents, and made some use of the ‘relt' relevant texts provided as part of the metadata. Unfortunately, our results on the HARD task were not good: in most runs, feedback hurt performance, and the active learning feedback hurt more than the baseline feedback. The only runs that improved slightly on the no-feedback runs were a couple of baseline feedback runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonZT03.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonZT03,
		author = {Stephen E. Robertson and Hugo Zaragoza and Michael J. Taylor},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Cambridge at {TREC-12:} {HARD} track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {418--425},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/microsoft-cambridge.hard.pdf},
		timestamp = {Tue, 04 May 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonZT03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Clairvoyance Corporation Experiments in the TREC 2003 High Accuracy  Retrieval from Douments (HARD) Track

_James G. Shanahan, Jeffrey Bennett, David A. Evans, David A. Hull, Jesse Montgomery_

- :fontawesome-solid-user-group: **Participant:** [clairvoyance.evans](./hard/participants.md#clairvoyance.evans)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/clairvoyance.hard.pdf](http://trec.nist.gov/pubs/trec12/papers/clairvoyance.hard.pdf)
- :material-file-search: **Runs:** [CLSTD630](./hard/runs.md#clstd630) | [CLAI1G](./hard/runs.md#clai1g) | [CLAI1NG](./hard/runs.md#clai1ng) | [CLAI2NG](./hard/runs.md#clai2ng) | [CLAI2G](./hard/runs.md#clai2g) | [CLAI2RTNG](./hard/runs.md#clai2rtng) | [CLAI2RTG](./hard/runs.md#clai2rtg) | [CLAI2WRTG](./hard/runs.md#clai2wrtg) | [CLAI2WRTNG](./hard/runs.md#clai2wrtng) | [CLAISTDG](./hard/runs.md#claistdg) | [CLAISTDNG](./hard/runs.md#claistdng) | [CLAISTDRTG](./hard/runs.md#claistdrtg) | [CLAISTDRTNG](./hard/runs.md#claistdrtng) | [CLAISTDWRTNG](./hard/runs.md#claistdwrtng) | [CLAISTDWRTG](./hard/runs.md#claistdwrtg)

??? abstract "Abstract"
	
	The Clairvoyance team participated in the HARD Track, submitting fifteen runs. Our experiments focused primarily on exploiting user feedback through clarification forms for query expansion. We made limited use of the genre and related text metadata. Within the clarification form feedback framework, we explored the cluster hypothesis in the context of relevance feedback. The cluster hypothesis states that closely associated documents tend to be relevant to the same requests [Van Rijsbergen, 1979]. With this in mind we investigated the impact on performance of exploiting user feedback on groups of documents (i.e., organizing the top retrieved documents for a query into intuitive groups through agglomerative clustering or document-centric clustering), as an alternative to a ranked list of titles. This forms the basis for a new blind feedback mechanism (used to expand queries) based upon clusters of documents, as an alternative to blind feedback based upon taking the top N ranked documents, an approach that is commonly used.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShanahanBEHM03.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShanahanBEHM03,
		author = {James G. Shanahan and Jeffrey Bennett and David A. Evans and David A. Hull and Jesse Montgomery},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Clairvoyance Corporation Experiments in the {TREC} 2003 High Accuracy Retrieval from Douments {(HARD)} Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {152--160},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/clairvoyance.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShanahanBEHM03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Active Feedback - UIUC TREC-2003 HARD Experiments

_Xuehua Shen, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [uillinoisuc.zhai](./hard/participants.md#uillinoisuc.zhai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.hard.pdf](http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.hard.pdf)
- :material-file-search: **Runs:** [uiuchard](./hard/runs.md#uiuchard) | [UIHARD1](./hard/runs.md#uihard1) | [UIHARD2](./hard/runs.md#uihard2) | [UIHARD4](./hard/runs.md#uihard4) | [UIHARD3](./hard/runs.md#uihard3)

??? abstract "Abstract"
	
	In this paper, we report our experiments on the HARD (High Accuracy Retrieval from Documents) Track in TREC 2003. We focus on active feedback, i.e., how to intelligently propose questions for relevance feedback in order to maximize accuracy improvement in the second run. We proposed and empirically evaluated three different methods, i.e., top-k, gapped top-k, and k-cluster centroid, to extract a fixed number of text units (e.g. passage or document) for feedback. The results show that presenting the top k documents for user feedback is often not as beneficial for learning as presenting more diversified documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShenZ03.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShenZ03,
		author = {Xuehua Shen and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Active Feedback - {UIUC} {TREC-2003} {HARD} Experiments},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {662--666},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShenZ03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UB at TREC 12: HARD and Genomics Tracks

_Munirathnam Srikanth, Miguel E. Ruiz, Rohini K. Srihari_

- :fontawesome-solid-user-group: **Participant:** [unybuffalo-cedar](./hard/participants.md#unybuffalo-cedar)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uny-buffalo.hard.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/uny-buffalo.hard.genomics.pdf)
- :material-file-search: **Runs:** [ub03ugTcugTD](./hard/runs.md#ub03ugtcugtd) | [ub03cugTD](./hard/runs.md#ub03cugtd) | [ub03sugT](./hard/runs.md#ub03sugt) | [ub03smfugTD](./hard/runs.md#ub03smfugtd)

??? abstract "Abstract"
	
	University at Buffalo (UB) participated in TREC-12 in Genomics and High Accuracy Retrieval from Documents (HARD) tracks. We explored some techniques that combine Information Retrieval and Information Extraction to perform the TREC tasks. We used an Information Extrac tion engine - InfoXtract [3] from Cymfony Inc.1 - to enhance retrieval results. For the Genomics primary task, documents retrieved using a vector space model with relevance feedback are re-weighted based on the biomedical named entities discovered by InfoXtract. For the secondary task, extracted information along with cue words for text snippets that describe functionality is used for generating GeneRIFs for given Gene name and PubMed abstract. A language modeling approach that incorporates keyword and non-keyword features are used for the HARD task. Features extracted by InfoXtract from the HARD corpus are used to rank documents and/or passages as answers to the HARD queries. Cymfony's InfoXtract [3] is a customizable Information Extraction engine that performs syntactic and semantic parsing of a document to identify features like named entities, relationships and events in them. The baseline InfoXtract engine has been trained for the general English and news domain, It can be customized to recognize new named entities like Gene Names and Gene Function. Biomedical Customization of InfoXtract is briefly presented in Section 2.2.
	

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

#### Interactive Search Refinement Techniques for HARD Tasks

_Olga Vechtomova, Eric Lam, Murat Karamuftuoglu_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo.vechtomova](./hard/participants.md#uwaterloo.vechtomova)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uwaterloo-olga.hard.pdf](http://trec.nist.gov/pubs/trec12/papers/uwaterloo-olga.hard.pdf)
- :material-file-search: **Runs:** [UWAThard1](./hard/runs.md#uwathard1) | [UWAThard2](./hard/runs.md#uwathard2) | [UWAThard3](./hard/runs.md#uwathard3)

??? abstract "Abstract"
	
	In our entry to the new HARD track, we have investigated two methods of interactively refining user search formulations. One method consists of asking the user to select a number of sentences that may represent relevant documents, and then using the documents, whose sentences were selected for query expansion. The second method is to show to the user a list of noun phrases, extracted from the initial document set, and then expanding the query with the terms from the phrases selected by the user. The results show that the second method is an effective means of interactive query expansion and yields significant performance improvements.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VechtomovaLK03.bib) "
	```
	@inproceedings{DBLP:conf/trec/VechtomovaLK03,
		author = {Olga Vechtomova and Eric Lam and Murat Karamuftuoglu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Interactive Search Refinement Techniques for {HARD} Tasks},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {820--827},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uwaterloo-olga.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VechtomovaLK03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC12 HARD Track at ISCAS

_Zeng Wu, Lin Du, Le Sun, Shiwei Ye_

- :fontawesome-solid-user-group: **Participant:** [cipc.lin](./hard/participants.md#cipc.lin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.hard.final2.pdf](http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.hard.final2.pdf)
- :material-file-search: **Runs:** [OPEN](./hard/runs.md#open) | [OPEN1](./hard/runs.md#open1)

??? abstract "Abstract"
	
	Statistical model in retrieval has been shown to perform well empirically. Extended Boolean model has been widely used in business system for its easiness to be complemented and not bad results. In this paper, a statistical model and modified Boolean model and natural language processing techniques, shallow query understanding techniques are used and results show that even with very limited training corpus, an appropriate statistical model can greatly improve the performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuDSY03.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuDSY03,
		author = {Zeng Wu and Lin Du and Le Sun and Shiwei Ye},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC12} {HARD} Track at {ISCAS}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {117--125},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.hard.final2.pdf},
		timestamp = {Fri, 21 Aug 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WuDSY03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Robust 

#### Overview of the TREC 2003 Robust Retrieval Track

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ROBUST.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec12/papers/ROBUST.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The robust retrieval track is a new track in TREC 2003. The goal of the track is to improve the consistency of retrieval technology by focusing on poorly performing topics. In addition, the track brings back a classic, ad hoc retrieval task to TREC that provides a natural home for new participants.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees03b.bib) "
	```
	@inproceedings{DBLP:conf/trec/Voorhees03b,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2003 Robust Retrieval Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {69--77},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/ROBUST.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees03b.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fondazione Ugo Bordoni at TREC 2003: Robust and Web Track

_Giambattista Amati, Claudio Carpineto, Giovanni Romano_

- :fontawesome-solid-user-group: **Participant:** [fub.carpineto](./robust/participants.md#fub.carpineto)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/fub.robust.web.pdf](http://trec.nist.gov/pubs/trec12/papers/fub.robust.web.pdf)
- :material-file-search: **Runs:** [fub03IneOLe3](./robust/runs.md#fub03ineole3) | [fub03InB2e3](./robust/runs.md#fub03inb2e3) | [fub03InOLe3](./robust/runs.md#fub03inole3) | [fub03IeOLKe3](./robust/runs.md#fub03ieolke3) | [fub03IneOBu3](./robust/runs.md#fub03ineobu3)

??? abstract "Abstract"
	
	Our participation in TREC 2003 aims to adapt the use of the DFR (Divergence From Randomness) models with Query Expansion (QE) to the robust track and the topic distillation task of the Web track. We focus on the robust track, where the utilization of QE improves the global performance but hurts the performance on the worst topics. In particular, we study the problem of the selective application of the query expansion. We define two information theory based functions, InfoDFR and InfoQ, predicting respectively the AP (Average Precision) of queries and the AP increment of queries after the application of QE. InfoQ is used to selectively apply QE. We show that the use of InfoQ achieves the same performance comparable of the unexpanded method on the set of the worst topics, but a better performance than full QE on the entire set of topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmatiCR03.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmatiCR03,
		author = {Giambattista Amati and Claudio Carpineto and Giovanni Romano},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Fondazione Ugo Bordoni at {TREC} 2003: Robust and Web Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {234--245},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/fub.robust.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AmatiCR03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining First and Second Order Features in the TREC 2003 Robust  Track

_Endre Boros, Paul B. Kantor, David J. Neu_

- :fontawesome-solid-user-group: **Participant:** [rutgers.neu](./robust/participants.md#rutgers.neu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/rutgers-kantor.robust.pdf](http://trec.nist.gov/pubs/trec12/papers/rutgers-kantor.robust.pdf)
- :material-file-search: **Runs:** [rutcor0350](./robust/runs.md#rutcor0350) | [rutcor0325](./robust/runs.md#rutcor0325) | [rutcor0375](./robust/runs.md#rutcor0375) | [rutcor030](./robust/runs.md#rutcor030) | [rutcor03100](./robust/runs.md#rutcor03100)

??? abstract "Abstract"
	
	This year at TREC 2003 we participated in the robust track and investigated the use of very simple retrieval rules based on convex combinations of similarity measures based on first and second order features.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BorosKN03.bib) "
	```
	@inproceedings{DBLP:conf/trec/BorosKN03,
		author = {Endre Boros and Paul B. Kantor and David J. Neu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining First and Second Order Features in the {TREC} 2003 Robust Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {544--546},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/rutgers-kantor.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BorosKN03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2003 Robust, HARD and QA Track Experiments using PIRCS

_Laszlo Grunfeld, Kui-Lam Kwok, Norbert Dinstl, Peter Deng_

- :fontawesome-solid-user-group: **Participant:** [queensc.kwok](./robust/participants.md#queensc.kwok)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/queens-college.robust.hard.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/queens-college.robust.hard.qa.pdf)
- :material-file-search: **Runs:** [pircRBa1](./robust/runs.md#pircrba1) | [pircRBd1](./robust/runs.md#pircrbd1) | [pircRBd2](./robust/runs.md#pircrbd2) | [pircRBd3](./robust/runs.md#pircrbd3) | [pircRBa2](./robust/runs.md#pircrba2)

??? abstract "Abstract"
	
	We participated in the Robust, HARD and part of the QA tracks in TREC2003. For Robust track, a new way of doing ad-hoc retrieval based on web assistance was introduced. For HARD track, we followed the guideline to generate clarification forms for each topic so as to experiment with user feedback and metadata. In QA, we only did the factoid experiment. The approach to QA was similar to what we have used before, except that WWW searching was added as a front-end processing. These experiments are described in Sections 2, 3 and 4 respectively.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrunfeldKDD03.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrunfeldKDD03,
		author = {Laszlo Grunfeld and Kui{-}Lam Kwok and Norbert Dinstl and Peter Deng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2003 Robust, {HARD} and {QA} Track Experiments using {PIRCS}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {510--521},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/queens-college.robust.hard.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrunfeldKDD03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at the Robust Track- A Query-based Model Selection  Approach for the Poorly-Performing Queries

_Ben He, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uglasgow.ounis](./robust/participants.md#uglasgow.ounis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uglasgow.robust.pdf](http://trec.nist.gov/pubs/trec12/papers/uglasgow.robust.pdf)
- :material-file-search: **Runs:** [Sel50QE](./robust/runs.md#sel50qe) | [Sel78QE](./robust/runs.md#sel78qe) | [InexpC2QE](./robust/runs.md#inexpc2qe) | [Sel50](./robust/runs.md#sel50) | [InexpC2](./robust/runs.md#inexpc2)

??? abstract "Abstract"
	
	In this newly introduced Robust Track, we mainly tested a novel query-based approach for the selection of the most appropriate term-weighting model. In our approach, we cluster the queries according to their statistics and associate the best-performing term-weighting model to each cluster. For a given new query, we assign a cluster to the query according to its statistical features, then apply the model associated to the cluster. As shown by the experimental results, our query-based model selection approach does improve the poorly-performing queries compared to a baseline where a unique retrieval model is applied indifferently to all queries. Moreover, it seems that query expansion has detrimental effect on the poorly-performing queries, although it significantly achieves a higher mean average precision over all the 100 queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeO03.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeO03,
		author = {Ben He and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at the Robust Track- {A} Query-based Model Selection Approach for the Poorly-Performing Queries},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {636--645},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uglasgow.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeO03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Océ at TREC 2003

_Pascha Iljin, Roel Brand, Samuel Driessen, Jakob Klok_

- :fontawesome-solid-user-group: **Participant:** [oce.driessen](./robust/participants.md#oce.driessen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/oce.robust.pdf](http://trec.nist.gov/pubs/trec12/papers/oce.robust.pdf)
- :material-file-search: **Runs:** [oce03noXbm](./robust/runs.md#oce03noxbm) | [oce03Xbm](./robust/runs.md#oce03xbm) | [oce03noXpr](./robust/runs.md#oce03noxpr) | [oce03Xpr](./robust/runs.md#oce03xpr) | [oce03noXbmD](./robust/runs.md#oce03noxbmd)

??? abstract "Abstract"
	
	This report describes the work done at Océ Research for the TREC 2003. This first participation consists of ad hoc experiments for the Robust track. We used the BM25 model and our new probabilistic model to rank documents. Knowledge Concepts' Content Enabler semantic network was used for stemming and query expansion. Our main goal was to compare the BM25 model and the probabilistic model implemented with and/or without query expansion. The developed generic probabilistic model does not use global statistics of a document collection to rank documents. The relevance of the document to a given query is calculated using term frequencies of the query terms in the document and the length of the document. Furthermore, some theoretical research has been done. We have constructed a model that uses relevance judgements of previous years. However, we did not implement it due to the time constraints.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/IljinBDK03.bib) "
	```
	@inproceedings{DBLP:conf/trec/IljinBDK03,
		author = {Pascha Iljin and Roel Brand and Samuel Driessen and Jakob Klok},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Oc{\'{e}} at {TREC} 2003},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {496--502},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/oce.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/IljinBDK03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NLPR at TREC 2003: Novelty and Robust

_Qianli Jin, Jun Zhao, Bo Xu_

- :fontawesome-solid-user-group: **Participant:** [cas.nlpr](./robust/participants.md#cas.nlpr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.novelty.robust.pdf](http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.novelty.robust.pdf)
- :material-file-search: **Runs:** [NLPR03vb25](./robust/runs.md#nlpr03vb25) | [NLPR03vb10](./robust/runs.md#nlpr03vb10) | [NLPR03w16](./robust/runs.md#nlpr03w16) | [NLPR03w49](./robust/runs.md#nlpr03w49) | [NLPR03vb50](./robust/runs.md#nlpr03vb50)

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

#### Approaches to Robust and Web Retrieval

_Jaap Kamps, Christof Monz, Maarten de Rijke, Börkur Sigurbjörnsson_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.derijke](./robust/participants.md#uamsterdam.derijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uamsterdam.web.robust.pdf](http://trec.nist.gov/pubs/trec12/papers/uamsterdam.web.robust.pdf)
- :material-file-search: **Runs:** [UAmsT03RFb](./robust/runs.md#uamst03rfb) | [UAmsT03R](./robust/runs.md#uamst03r) | [UAmsT03RStFb](./robust/runs.md#uamst03rstfb) | [UAmsT03RSt](./robust/runs.md#uamst03rst) | [UAmsT03RDesc](./robust/runs.md#uamst03rdesc)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2003 Robust and Web tracks. For the Robust track, we experimented with the impact of stemming and feedback on the worst scoring topics. Our main finding is the effectiveness of stemming on poorly performing topics, which sheds new light on the role of morphological normalization in information retrieval. For both the home/named page finding and topic distillation tasks of the Web track, we experimented with different document representations and retrieval models. Our main finding is effectiveness of the anchor text index for both tasks, suggesting that compact document representations are a fruitful strategy for scaling-up retrieval systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KampsMRS03.bib) "
	```
	@inproceedings{DBLP:conf/trec/KampsMRS03,
		author = {Jaap Kamps and Christof Monz and Maarten de Rijke and B{\"{o}}rkur Sigurbj{\"{o}}rnsson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Approaches to Robust and Web Retrieval},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {594--599},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uamsterdam.web.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KampsMRS03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UIC at TREC-2003: Robust Track

_Shuang Liu, Clement T. Yu_

- :fontawesome-solid-user-group: **Participant:** [uillinois-chicago.yu](./robust/participants.md#uillinois-chicago.yu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uillinois-chicago.robust.pdf](http://trec.nist.gov/pubs/trec12/papers/uillinois-chicago.robust.pdf)
- :material-file-search: **Runs:** [uic0301](./robust/runs.md#uic0301) | [uic0302](./robust/runs.md#uic0302) | [uic0303](./robust/runs.md#uic0303) | [uic0304](./robust/runs.md#uic0304) | [uic0305](./robust/runs.md#uic0305)

??? abstract "Abstract"
	
	In TREC 2003, the Database and Information System Lab (DBIS) at University of Illinois at Chicago (UIC) participate in the robust track, which is a traditional ad hoc retrieval task. The emphasis is based on average effectiveness as well as individual topic effectiveness. Noun phrases in the query are identified and classified into 4 types: proper names, dictionary phrases, simple phrases and complex phrases. A document has a phrase if all content words in a phrase are within a window of a certain size. The window sizes for different types of phrases are different. We consider phrases to be more important than individual terms. As a consequence, documents in response to a query are ranked with matching phrases given a higher priority. WordNet is used to disambiguate word senses and bring in useful synonyms and hyponyms once the correct senses of the words in a query have been identified. The usual pseudo-feedback process is modified so that the documents are also ranked according to phrase and word similarities with phrase matching having a higher priority. Five runs which use either title or title and description have been submitted.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuY03.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuY03,
		author = {Shuang Liu and Clement T. Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UIC} at {TREC-2003:} Robust Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {653--661},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uillinois-chicago.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuY03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Methods for the TREC 2003 Robust Track

_James Mayfield, Paul McNamee_

- :fontawesome-solid-user-group: **Participant:** [jhuapl.mcnamee](./robust/participants.md#jhuapl.mcnamee)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/jhu-apl.robust.pdf](http://trec.nist.gov/pubs/trec12/papers/jhu-apl.robust.pdf)
- :material-file-search: **Runs:** [aplrob03b](./robust/runs.md#aplrob03b) | [aplrob03c](./robust/runs.md#aplrob03c) | [aplrob03d](./robust/runs.md#aplrob03d) | [aplrob03e](./robust/runs.md#aplrob03e) | [aplrob03a](./robust/runs.md#aplrob03a)

??? abstract "Abstract"
	
	The Johns Hopkins University Applied Physics Laboratory (JHU/APL) focused on the Robust Retrieval Track at this year's conference. In the past we have investigated the use of alternate methods for tokenization and applied character n-grams, with success, to tasks in ad hoc, filtering, and cross-language tracks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MayfieldM03.bib) "
	```
	@inproceedings{DBLP:conf/trec/MayfieldM03,
		author = {James Mayfield and Paul McNamee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Methods for the {TREC} 2003 Robust Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {358--362},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/jhu-apl.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MayfieldM03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Robust, Web and Genomic Retrieval with Hummingbird SearchServer at  TREC 2003

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird.tomlinson](./robust/participants.md#hummingbird.tomlinson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/hummingbird.robust.web.genomic.pdf](http://trec.nist.gov/pubs/trec12/papers/hummingbird.robust.web.genomic.pdf)
- :material-file-search: **Runs:** [humR03t](./robust/runs.md#humr03t) | [humR03d](./robust/runs.md#humr03d) | [humR03de](./robust/runs.md#humr03de) | [humR03dc](./robust/runs.md#humr03dc) | [humR03tc](./robust/runs.md#humr03tc)

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

#### Ranking Function Discovery by Genetic Programming for Robust Retrieval

_Li Wang, Weiguo Fan, Rui Yang, Wensi Xi, Ming Luo, Ye Zhou, Edward A. Fox_

- :fontawesome-solid-user-group: **Participant:** [vatech.xi](./robust/participants.md#vatech.xi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/vatech.robust.pdf](http://trec.nist.gov/pubs/trec12/papers/vatech.robust.pdf)
- :material-file-search: **Runs:** [VTcdhgp1](./robust/runs.md#vtcdhgp1) | [VTgpdhgp2](./robust/runs.md#vtgpdhgp2) | [VTcdhgp3](./robust/runs.md#vtcdhgp3) | [VTDokrcgp5](./robust/runs.md#vtdokrcgp5) | [VTgpdhgp4](./robust/runs.md#vtgpdhgp4)

??? abstract "Abstract"
	
	Ranking functions are instrumental for the success of an information retrieval (search engine) system. However nearly all existing ranking functions are manually designed based on experience, observations and probabilistic theories. This paper tested a novel ranking function discovery technique proposed in [Fan 2003a, Fan2003b] - ARRANGER (Automatic geneRation of RANking functions by GEnetic pRogramming), which uses Genetic Programming (GP) to automatically learn the “best” ranking function, for the robust retrieval task. Ranking function discovery is essentially an optimization problem. As the search space here is not a coordinate system, most of the traditional optimization algorithms could not work. However, this ranking discovery problem could be easily tackled by ARRANGER. In our evaluations on 150 queries from the ad-hoc track of TREC 6, 7, and 8, the performance of our system (in average precision) was improved by nearly 16%, after replacing Okapi BM25 function with a function automatically discovered by ARRANGER. By applying pseudo-relevance feedback and ranking fusion on newly discovered functions, we improved the retrieval performance by up to 30%. The results of our experiments showed that our ranking function discovery technique - ARRANGER - is very effective in discovering high-performing ranking functions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangFYXLZF03.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangFYXLZF03,
		author = {Li Wang and Weiguo Fan and Rui Yang and Wensi Xi and Ming Luo and Ye Zhou and Edward A. Fox},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Ranking Function Discovery by Genetic Programming for Robust Retrieval},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {828--836},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/vatech.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangFYXLZF03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Task-Specific Query Expansion (MultiText Experiments for TREC 2003)

_David L. Yeung, Charles L. A. Clarke, Gordon V. Cormack, Thomas R. Lynam, Egidio L. Terra_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo.cormack](./robust/participants.md#uwaterloo.cormack)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uwaterloo.genomics.robust.pdf](http://trec.nist.gov/pubs/trec12/papers/uwaterloo.genomics.robust.pdf)
- :material-file-search: **Runs:** [uwmtCR0](./robust/runs.md#uwmtcr0) | [uwmtCR1](./robust/runs.md#uwmtcr1) | [uwmtCR3](./robust/runs.md#uwmtcr3) | [uwmtCR2](./robust/runs.md#uwmtcr2) | [uwmtCR4](./robust/runs.md#uwmtcr4)

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

- :fontawesome-solid-user-group: **Participant:** [uillinoisuc.zhai](./robust/participants.md#uillinoisuc.zhai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.robust.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.robust.genomics.pdf)
- :material-file-search: **Runs:** [UIUC03Rd1](./robust/runs.md#uiuc03rd1) | [UIUC03Rt1](./robust/runs.md#uiuc03rt1) | [UIUC03Rd2](./robust/runs.md#uiuc03rd2) | [UIUC03Rd3](./robust/runs.md#uiuc03rd3) | [UIUC03Rtd1](./robust/runs.md#uiuc03rtd1)

??? abstract "Abstract"
	
	In this paper, we report our experiments in the TREC 2003 Genomics Track and the Robust Track. A common theme that we explored is the robustness of a basic language modeling retrieval approach. We examine several aspects of robustness, including robustness in handling different types of queries, different types of documents, and op- timizing performance for difficult topics. Our basic re- trieval method is the KL-divergence retrieval model with the two-stage smoothing method plus a mixture model feedback method. In the Genomics IR track, we propose a new method for modeling semi-structured queries using language models, which is shown to be more robust and effective than the regular query model in handling gene queries. In the Robust track, we experimented with two heuristic approaches to improve the robustness in using language models for pseudo feedback.
	

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

#### THUIR at TREC 2003: Novelty, Robust and Web

_Min Zhang, Chuan Lin, Yiqun Liu, Leo Zhao, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [tsinghuau.ma](./robust/participants.md#tsinghuau.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/tsinghuau.novelty.robust.web.pdf](http://trec.nist.gov/pubs/trec12/papers/tsinghuau.novelty.robust.web.pdf)
- :material-file-search: **Runs:** [THUIRr0302](./robust/runs.md#thuirr0302) | [THUIRr0303](./robust/runs.md#thuirr0303) | [THUIRr0304](./robust/runs.md#thuirr0304) | [THUIRr0301](./robust/runs.md#thuirr0301) | [THUIRr0305](./robust/runs.md#thuirr0305)

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

## Question Answering 

#### Overview of the TREC 2003 Question Answering Track

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/QA.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec12/papers/QA.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC 2003 question answering track contained two tasks, the passages task and the main task. In the passages task, systems returned a single text snippet in response to factoid questions; the evaluation metric was the number of snippets that contained a correct answer. The main task contained three separate types of questions, factoid questions, list questions, and definition questions. Each of the questions was tagged as to its type and the different question types were evaluated separately. The final score for a main task run was a combination of the scores for the separate question types. This paper defines the various tasks included in the track and reports the evaluation results. Since the TREC 2003 track was the first time for significant participation in the definition and list subtasks, the paper also examines the reliability of the evaluation for these tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees03a.bib) "
	```
	@inproceedings{DBLP:conf/trec/Voorhees03a,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2003 Question Answering Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {54--68},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/QA.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees03a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### AnswerFinder in TREC 2003

_Diego Mollá Aliod_

- :fontawesome-solid-user-group: **Participant:** [macquarieu.molla](./qa/participants.md#macquarieu.molla)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/macquarieu.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/macquarieu.qa.pdf)
- :material-file-search: **Runs:** [answfind3](./qa/runs.md#answfind3) | [answfind1](./qa/runs.md#answfind1) | [answfind2](./qa/runs.md#answfind2)

??? abstract "Abstract"
	
	In this our first participation in TREC we have focused on the passage task of the question answering track. The main aim of our participation was to test the impact of various types of linguistic information in a simple question answering system. In particular, we have tested various combinations of word overlap, grammatical relations overlap, and overlap of minimal logical forms in the final scoring module of the system. The results indicate a small increase of accuracy with respect to a baseline system based on word overlap. Overall, given the short time available for developing the system, the results are satisfactory and equal or surpass the median.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Aliod03.bib) "
	```
	@inproceedings{DBLP:conf/trec/Aliod03,
		author = {Diego Moll{\'{a}} Aliod},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {AnswerFinder in {TREC} 2003},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {392--398},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/macquarieu.qa.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Aliod03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Hybrid Approach for QA Track Definitional Questions

_Sasha Blair-Goldensohn, Kathleen R. McKeown, Andrew Hazen Schlaikjer_

- :fontawesome-solid-user-group: **Participant:** [ucolorado.ward](./qa/participants.md#ucolorado.ward)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/columbiau.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/columbiau.qa.pdf)
- :material-file-search: **Runs:** [cuaqdef2003](./qa/runs.md#cuaqdef2003)

??? abstract "Abstract"
	
	We present an overview of DefScriber, a system developed at Columbia University that combines knowledge-based and statistical methods to answer definitional questions of the form, “What is X?” We discuss how DefScriber was applied to the definition questions in the TREC 2003 QA track main task. We conclude with an analysis of our system's results on the definition questions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Blair-GoldensohnMS03.bib) "
	```
	@inproceedings{DBLP:conf/trec/Blair-GoldensohnMS03,
		author = {Sasha Blair{-}Goldensohn and Kathleen R. McKeown and Andrew Hazen Schlaikjer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Hybrid Approach for {QA} Track Definitional Questions},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {185--192},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/columbiau.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Blair-GoldensohnMS03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MITRE's Qanda at TREC-12

_John D. Burger_

- :fontawesome-solid-user-group: **Participant:** [mitre.burger](./qa/participants.md#mitre.burger)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/mitre.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/mitre.qa.pdf)
- :material-file-search: **Runs:** [MITRE2003A](./qa/runs.md#mitre2003a)

??? abstract "Abstract"
	
	Qanda is MITRE's TREC-style question answering system. This year, we were able to apply only a small effort to the TREC QA activity, approximately one person-month. As well as some general improvements in Qanda's processing, we made some simple attempts to handle definition and list answers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Burger03.bib) "
	```
	@inproceedings{DBLP:conf/trec/Burger03,
		author = {John D. Burger},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {MITRE's Qanda at {TREC-12}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {436--440},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/mitre.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Burger03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2003 Question Answering Track at CAS-ICT

_Yi Chang, Hongbo Xu, Shuo Bai_

- :fontawesome-solid-user-group: **Participant:** [cas-ict.bin](./qa/participants.md#cas-ict.bin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.qa.final.pdf](http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.qa.final.pdf)
- :material-file-search: **Runs:** [ICTQA2003A](./qa/runs.md#ictqa2003a) | [ICTQA2003B](./qa/runs.md#ictqa2003b) | [ICTQA2003C](./qa/runs.md#ictqa2003c)

??? abstract "Abstract"
	
	In our system, we make use of Chunk information to analyze the question. A multilevel method is fulfilled to retrieve candidate Bi-sentences. As to answer selecting, we proposed a voting method. We figure out the performance of each module of our system, and our study shows that 65.54% information has lost in document retrieval and Bi-sentence retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChangXB03.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChangXB03,
		author = {Yi Chang and Hongbo Xu and Shuo Bai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2003 Question Answering Track at {CAS-ICT}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {147--151},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.qa.final.pdf},
		timestamp = {Thu, 13 Aug 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ChangXB03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Bangor at TREC 2003: Q&A and Genomics Tracks

_Terence Clifton, Alex Colquhoun, William John Teahan_

- :fontawesome-solid-user-group: **Participant:** [uwales.teahan](./qa/participants.md#uwales.teahan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ubangor-wales.qa.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/ubangor-wales.qa.genomics.pdf)
- :material-file-search: **Runs:** [uwbqitekat03](./qa/runs.md#uwbqitekat03)

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

#### Multiple-Engine Question Answering in TextMap

_Abdessamad Echihabi, Ulf Hermjakob, Eduard H. Hovy, Daniel Marcu, Eric Melz, Deepak Ravichandran_

- :fontawesome-solid-user-group: **Participant:** [usc-isi.hermjakob](./qa/participants.md#usc-isi.hermjakob)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/usc-isi.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/usc-isi.qa.pdf)
- :material-file-search: **Runs:** [isi03a](./qa/runs.md#isi03a) | [isi03c](./qa/runs.md#isi03c) | [isi03b](./qa/runs.md#isi03b)

??? abstract "Abstract"
	
	At TREC-2003, TextMap participated in the Main task, which encompassed answering the following types of questions: factoid questions; list questions; definition questions. In this paper, we overview the architecture of the TextMap system and report its performance, as evaluated by the NIST assessors, on each of these tracks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EchihabiHHMMR03.bib) "
	```
	@inproceedings{DBLP:conf/trec/EchihabiHHMMR03,
		author = {Abdessamad Echihabi and Ulf Hermjakob and Eduard H. Hovy and Daniel Marcu and Eric Melz and Deepak Ravichandran},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Multiple-Engine Question Answering in TextMap},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {772--781},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/usc-isi.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EchihabiHHMMR03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Novelty, Genes and Questions at the University of Iowa

_David Eichmann, Padmini Srinivasan, Marc Light, Hudong Wang, Xin Ying Qiu, Robert J. Arens, Aditya Kumar Sehgal_

- :fontawesome-solid-user-group: **Participant:** [uiowa.eichmann](./qa/participants.md#uiowa.eichmann)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uiowa.novelty.genomics.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/uiowa.novelty.genomics.qa.pdf)
- :material-file-search: **Runs:** [UIowaQA0301](./qa/runs.md#uiowaqa0301) | [UIowaQA0302](./qa/runs.md#uiowaqa0302) | [UIowaQA0303](./qa/runs.md#uiowaqa0303)

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

#### The University of Sheffield's TREC 2003 Q&A Experiments

_Robert J. Gaizauskas, Mark A. Greenwood, Mark Hepple, Ian Roberts, Horacio Saggion, Matthew Sargaison_

- :fontawesome-solid-user-group: **Participant:** [usheffield.gaizauskas](./qa/participants.md#usheffield.gaizauskas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/usheffield.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/usheffield.qa.pdf)
- :material-file-search: **Runs:** [shef12simple](./qa/runs.md#shef12simple) | [shef12okapi](./qa/runs.md#shef12okapi) | [shef12madcow](./qa/runs.md#shef12madcow)

??? abstract "Abstract"
	
	The systems entered by the University of Sheffield in the question answering track of previous TRECs have been developments of the system first entered in TREC 8 (Humphreys et al., 1999). Although a range of improvements have been made to the system over the last four years (Scott and Gaizauskas, 2000; Greenwood et al., 2002), none has resulted in a significant performance increase. For this reason it was decided to approach the TREC 2003 evaluation more as a learning experience than as a forum in which to promote a particular approach to QA. We view this as the beginning of a process that will lead to much fuller appreciation of how to build more effective QA systems. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaizauskasGHRSS03.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaizauskasGHRSS03,
		author = {Robert J. Gaizauskas and Mark A. Greenwood and Mark Hepple and Ian Roberts and Horacio Saggion and Matthew Sargaison},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Sheffield's {TREC} 2003 Q{\&}A Experiments},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {782--790},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/usheffield.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GaizauskasGHRSS03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2003 Robust, HARD and QA Track Experiments using PIRCS

_Laszlo Grunfeld, Kui-Lam Kwok, Norbert Dinstl, Peter Deng_

- :fontawesome-solid-user-group: **Participant:** [queensc.kwok](./qa/participants.md#queensc.kwok)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/queens-college.robust.hard.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/queens-college.robust.hard.qa.pdf)
- :material-file-search: **Runs:** [pircsqa1](./qa/runs.md#pircsqa1) | [pircsqa2](./qa/runs.md#pircsqa2) | [pircsqa3](./qa/runs.md#pircsqa3)

??? abstract "Abstract"
	
	We participated in the Robust, HARD and part of the QA tracks in TREC2003. For Robust track, a new way of doing ad-hoc retrieval based on web assistance was introduced. For HARD track, we followed the guideline to generate clarification forms for each topic so as to experiment with user feedback and metadata. In QA, we only did the factoid experiment. The approach to QA was similar to what we have used before, except that WWW searching was added as a front-end processing. These experiments are described in Sections 2, 3 and 4 respectively.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrunfeldKDD03.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrunfeldKDD03,
		author = {Laszlo Grunfeld and Kui{-}Lam Kwok and Norbert Dinstl and Peter Deng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2003 Robust, {HARD} and {QA} Track Experiments using {PIRCS}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {510--521},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/queens-college.robust.hard.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrunfeldKDD03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Answer Mining by Combining Extraction Techniques with Abductive Reasoning

_Sanda M. Harabagiu, Dan I. Moldovan, Christine Clark, Mitchell Bowden, John Williams, Jeremy Bensley_

- :fontawesome-solid-user-group: **Participant:** [lcc.harabagiu](./qa/participants.md#lcc.harabagiu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/lcc.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/lcc.qa.pdf)
- :material-file-search: **Runs:** [LCCmainE03](./qa/runs.md#lccmaine03) | [LCCpass03](./qa/runs.md#lccpass03) | [LCCmainS03](./qa/runs.md#lccmains03)

??? abstract "Abstract"
	
	Language Computer Corporation's Question Answering system combines the strengths of Information Extraction (IE) techniques with the vastness of axiomatic knowledge representations derived from Word-Net for justifying answers that are extracted from the AQUAINT text collection. CICERO LITE, the named entity recognizer employed in LCC's QA system was able to recognize precisely a large set of entities that ranged over an extended set of semantic categories. Similarly, the semantic hierarchy of answer types was also enhanced. To improve the precision of answer min-ing, the QA system also relied on a theorem prover that was able to produce abductive justifications of the answers when it had access to the axiomatic transformations of the WordNet glosses. This combination of techniques was successful and furthermore, produced little difference between the exact extractions and the paragraph extractions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HarabagiuMCBWB03.bib) "
	```
	@inproceedings{DBLP:conf/trec/HarabagiuMCBWB03,
		author = {Sanda M. Harabagiu and Dan I. Moldovan and Christine Clark and Mitchell Bowden and John Williams and Jeremy Bensley},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Answer Mining by Combining Extraction Techniques with Abductive Reasoning},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {375--382},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/lcc.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HarabagiuMCBWB03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2003: HARD and QA

_Nasreen Abdul Jaleel, Andrés Corrada-Emmanuel, Qi Li, Xiaoyong Liu, Courtney Wade, James Allan_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./qa/participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/umass-amherst.hard.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/umass-amherst.hard.qa.pdf)
- :material-file-search: **Runs:** [umassql](./qa/runs.md#umassql)

??? abstract "Abstract"
	
	The Center for Intelligent Information Retrieval (CIIR) at UMass Amherst participated in two tracks for TREC 2003: High Accuracy Retrieval from Documents (HARD) and Question Answering (QA). In the HARD track, we developed document metadata to correspond to query metadata requirements; implemented clarification forms based on query expansion, passage retrieval, and clustering; and retrieved variable length passages deemed most likely to be relevant. This work is discussed at length in Section 1. In the QA track, we focused on retrieving passages that were likely to contain the answer to the question.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JaleelCLLWA03.bib) "
	```
	@inproceedings{DBLP:conf/trec/JaleelCLLWA03,
		author = {Nasreen Abdul Jaleel and Andr{\'{e}}s Corrada{-}Emmanuel and Qi Li and Xiaoyong Liu and Courtney Wade and James Allan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass at {TREC} 2003: {HARD} and {QA}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {715--725},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/umass-amherst.hard.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JaleelCLLWA03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at the TREC 2003 Question Answering  Track

_Valentin Jijkoun, Gilad Mishne, Christof Monz, Maarten de Rijke, Stefan Schlobach, Oren Tsur_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.derijke](./qa/participants.md#uamsterdam.derijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uamsterdam.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/uamsterdam.qa.pdf)
- :material-file-search: **Runs:** [UAmsT03M2](./qa/runs.md#uamst03m2) | [UAmsT03M1](./qa/runs.md#uamst03m1) | [UAmsT03M3](./qa/runs.md#uamst03m3) | [UAmsT03P1](./qa/runs.md#uamst03p1)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2003 Question Answering track. We explain the ideas underlying our approaches to the task, report on our results, provide an error analysis, and give a summary of our findings so far.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JijkounMMRST03.bib) "
	```
	@inproceedings{DBLP:conf/trec/JijkounMMRST03,
		author = {Valentin Jijkoun and Gilad Mishne and Christof Monz and Maarten de Rijke and Stefan Schlobach and Oren Tsur},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Amsterdam at the {TREC} 2003 Question Answering Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {586--593},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uamsterdam.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JijkounMMRST03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Integrating Web-based and Corpus-based Techniques for Question Answering

_Boris Katz, Jimmy Lin, Daniel Loreto, Wesley Hildebrandt, Matthew W. Bilotti, Sue Felshin, Aaron Fernandes, Gregory Marton, Federico Mora_

- :fontawesome-solid-user-group: **Participant:** [mit.lin](./qa/participants.md#mit.lin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/mit.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/mit.qa.pdf)
- :material-file-search: **Runs:** [MITCSAIL03a](./qa/runs.md#mitcsail03a) | [MITCSAIL03b](./qa/runs.md#mitcsail03b) | [MITCSAIL03c](./qa/runs.md#mitcsail03c)

??? abstract "Abstract"
	
	MIT CSAIL's entry in this year's TREC Question Answering track focused on integrating Web-based techniques with more traditional strategies based on document retrieval and named-entity detection. We believe that achieving high performance in the question answering task requires a combination of multiple strategies designed to capitalize on different characteristics of various resources. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KatzLLHBFFMM03.bib) "
	```
	@inproceedings{DBLP:conf/trec/KatzLLHBFFMM03,
		author = {Boris Katz and Jimmy Lin and Daniel Loreto and Wesley Hildebrandt and Matthew W. Bilotti and Sue Felshin and Aaron Fernandes and Gregory Marton and Federico Mora},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Integrating Web-based and Corpus-based Techniques for Question Answering},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {426--435},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/mit.qa.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KatzLLHBFFMM03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ITC-irst at TREC 2003: the DIOGENE QA System

_Milen Kouylekov, Bernardo Magnini, Matteo Negri, Hristo Tanev_

- :fontawesome-solid-user-group: **Participant:** [itcirst.magnini](./qa/participants.md#itcirst.magnini)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/itc-irst.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/itc-irst.qa.pdf)
- :material-file-search: **Runs:** [irstqa2003w](./qa/runs.md#irstqa2003w) | [irstqa2003d](./qa/runs.md#irstqa2003d) | [irstqa2003p](./qa/runs.md#irstqa2003p)

??? abstract "Abstract"
	
	This paper describes a new version of the DIOGENE Question Answering (QA) system developed at ITC-Irst. The recent updates here presented are targeted to the participation to TREC-2003 and meet the specific requirements of this year's QA main task. In particular, extending the backbone already developed for our participation to the last two editions of the QA track, special attention was paid to deal with the principal novelty factors of the new challenge, namely the introduction of the so-called definition and list questions. Moreover, we experimented with a first attempt to integrate parsing as a deeper linguistic analysis technique to find similarities between the syntactic structure of the input questions and the retrieved text passages. The outcome of such experiments, as well as the variations of the system's architecture and the results achieved at TREC-2003 will be presented in the following sections.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KouylekovMNT03.bib) "
	```
	@inproceedings{DBLP:conf/trec/KouylekovMNT03,
		author = {Milen Kouylekov and Bernardo Magnini and Matteo Negri and Hristo Tanev},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {ITC-irst at {TREC} 2003: the {DIOGENE} {QA} System},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {349--357},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/itc-irst.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KouylekovMNT03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QED: The Edinburgh TREC-2003 Question Answering System

_Jochen L. Leidner, Johan Bos, Tiphaine Dalmas, James R. Curran, Stephen Clark, Colin J. Bannard, Bonnie L. Webber, Mark Steedman_

- :fontawesome-solid-user-group: **Participant:** [uedinburgh.leidner](./qa/participants.md#uedinburgh.leidner)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uedinburgh.qa.ps](http://trec.nist.gov/pubs/trec12/papers/uedinburgh.qa.ps)
- :material-file-search: **Runs:** [EdinInf2003C](./qa/runs.md#edininf2003c) | [EdinInf2003B](./qa/runs.md#edininf2003b) | [EdinInf2003A](./qa/runs.md#edininf2003a)

??? abstract "Abstract"
	
	This report describes a new open-domain answer retrieval system developed at the University of Edinburgh and gives results for the TREC-12 question answering track. Phrasal answers are identified by increasingly narrowing down the search space from a large text collection to a single phrase. The system uses document retrieval, query-based passage segmentation and ranking, semantic analysis from a wide-coverage parser, and a unification-like matching procedure to extract potential an-swers. A simple Web-based answer validation stage is also applied. The system is based on the Open Agent Architecture and has a parallel design so that multiple questions can be answered simultaneously on a Beowulf cluster.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeidnerBDCCBWS03.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeidnerBDCCBWS03,
		author = {Jochen L. Leidner and Johan Bos and Tiphaine Dalmas and James R. Curran and Stephen Clark and Colin J. Bannard and Bonnie L. Webber and Mark Steedman},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{QED:} The Edinburgh {TREC-2003} Question Answering System},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {631--635},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uedinburgh.qa.ps},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeidnerBDCCBWS03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Use of Metadata for Question Answering and Novelty Tasks

_Kenneth C. Litkowski_

- :fontawesome-solid-user-group: **Participant:** [clresearch](./qa/participants.md#clresearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/clresearch.qa.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/clresearch.qa.novelty.pdf)
- :material-file-search: **Runs:** [clr03m1](./qa/runs.md#clr03m1) | [clr03p2](./qa/runs.md#clr03p2) | [clr03p1](./qa/runs.md#clr03p1)

??? abstract "Abstract"
	
	CL Research's question-answering system for TREC 2003 was modified away from reliance on database technology to the core underlying technology of using massive XML-tagging for processing both questions and documents. This core technology was then extended to participate in the novelty task. This technology provides many opportuinities for experimenting with various approaches to question answering and novelty determination. For the QA track, we submitted one run and our overall main task score was 0.075, with scores of 0.070 for factoid questions, 0.000 for list questions, and 0.160 for definition questions. For the passage task, we submitted two runs, our better score was 0.119 for the factoid questions. These scores were all considerably below the medians for these tasks. We have implemented further routines since our official submission, improving our scores to 0.18 and 0.23 for the exact answer and passages tasks, respectively. For the Novelty track, we submitted four runs for task 1, one run for task 2, five runs for task 3, and one run for task 4; our submissions for tasks 2 and 4 were identical. For task 1, our best run received an F-score of 0.483 for relevant sentences and 0.410 for new sentences. For task 2, our F-score was 0.788 for new sentences. For task 3, our best F-score was 0.558 for relevant sentences and 0.419 for new sentences. For task 4, our F-score was 0.655 for new sentences. On average, our F-scores were somewhat above the medians on all tasks. We describe our system and examine our results from the perspective of exploiting the metadata in the XML tags.
	

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

#### QA UdG-UPC System at TREC-12

_Marc Massot, Horacio Rodríguez, Daniel Ferrés_

- :fontawesome-solid-user-group: **Participant:** [upc-udg.rodriguez](./qa/participants.md#upc-udg.rodriguez)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/upcudg.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/upcudg.qa.pdf)
- :material-file-search: **Runs:** [UPCUdGsys1](./qa/runs.md#upcudgsys1)

??? abstract "Abstract"
	
	This paper describes a prototype multilingual Q&A system that we have designed to participate in the Q&A Track of TREC-12. The system answer concrete responses, then we participate in the Q&A main task for factoid questions. The main areas of our system are: (1) Inductive Logic Programming to learn the question type, (2) Clustering of Named Entities to improve Information Retrieval and (3) Semantic relations and EuroWordNet synsets to perform a language-independent answer extraction.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MassotRF03.bib) "
	```
	@inproceedings{DBLP:conf/trec/MassotRF03,
		author = {Marc Massot and Horacio Rodr{\'{\i}}guez and Daniel Ferr{\'{e}}s},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{QA} UdG-UPC System at {TREC-12}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {762--771},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/upcudg.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MassotRF03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The JAVELIN Question-Answering System at TREC 2003: A Multi-Strategh  Approach with Dynamic Planning

_Eric Nyberg, Teruko Mitamura, James P. Callan, Jaime G. Carbonell, Robert E. Frederking, Kevyn Collins-Thompson, Laurie Hiyakumoto, Yifen Huang, Curtis Huttenhower, Scott Judy, Jeongwoo Ko, Anna Kupsc, Lucian Vlad Lita, Vasco Pedro, David Svoboda, Benjamin Van Durme_

- :fontawesome-solid-user-group: **Participant:** [cmu_javelin](./qa/participants.md#cmu_javelin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/cmu.javelin.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/cmu.javelin.qa.pdf)
- :material-file-search: **Runs:** [CMUJAV2003](./qa/runs.md#cmujav2003)

??? abstract "Abstract"
	
	The JAVELIN system evaluated at TREC 2003 is an integrated architecture for open-domain question answering. JAVELIN employs a modular approach that addresses individual aspects of the QA task in an abstract manner. The System implements a planner that controls the execution and information flow, as well as a multiple answer seeking strategies used differently depending on the type of question.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NybergMCCFCHHHJKKLPSD03.bib) "
	```
	@inproceedings{DBLP:conf/trec/NybergMCCFCHHHJKKLPSD03,
		author = {Eric Nyberg and Teruko Mitamura and James P. Callan and Jaime G. Carbonell and Robert E. Frederking and Kevyn Collins{-}Thompson and Laurie Hiyakumoto and Yifen Huang and Curtis Huttenhower and Scott Judy and Jeongwoo Ko and Anna Kupsc and Lucian Vlad Lita and Vasco Pedro and David Svoboda and Benjamin Van Durme},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {JAVELIN} Question-Answering System at {TREC} 2003: {A} Multi-Strategh Approach with Dynamic Planning},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/cmu.javelin.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NybergMCCFCHHHJKKLPSD03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Passage Scoring for Question Answering via Bayesian Inference on Lexical  Relations

_Deepa Paranjpe, Ganesh Ramakrishnan, Sumana Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [iitb.ramakrishnan](./qa/participants.md#iitb.ramakrishnan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/iit.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/iit.qa.pdf)
- :material-file-search: **Runs:** [IITBQA](./qa/runs.md#iitbqa) | [IITBQA1](./qa/runs.md#iitbqa1)

??? abstract "Abstract"
	
	Many researchers have used lexical networks and ontologies to mitigate synonymy and polysemy problems in Question Answering (QA), systems coupled with taggers, query classifiers, and answer extractors in complex and ad-hoc ways. We seek to make QA systems reproducible with shared and modest human effort, carefully separating knowledge from algorithms. To this end, we propose an aesthetically “clean” Bayesian inference scheme for exploiting lexical relations for passage-scoring for QA . The factors which contribute to the efficacy of Bayesian Inferencing on lexical relations are soft word sense disambiguation, parameter smoothing which ameliorates the data sparsity problem and estimation of joint probability over words which overcomes the deficiency of naive-bayes-like approaches.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ParanjpeRS03.bib) "
	```
	@inproceedings{DBLP:conf/trec/ParanjpeRS03,
		author = {Deepa Paranjpe and Ganesh Ramakrishnan and Sumana Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Passage Scoring for Question Answering via Bayesian Inference on Lexical Relations},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {305--210},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/iit.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ParanjpeRS03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM's PIQUANT in TREC2003

_John M. Prager, Jennifer Chu-Carroll, Krzysztof Czuba, Christopher A. Welty, Abraham Ittycheriah, Ruchi Mahindru_

- :fontawesome-solid-user-group: **Participant:** [ibm.prager](./qa/participants.md#ibm.prager)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ibm-prager.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/ibm-prager.qa.pdf)
- :material-file-search: **Runs:** [IBM2003a](./qa/runs.md#ibm2003a) | [IBM2003c](./qa/runs.md#ibm2003c) | [IBM2003b](./qa/runs.md#ibm2003b)

??? abstract "Abstract"
	
	For the most part, the system we used for TREC2003 was a smooth evolution of the one we ran in TREC2002 [Chu-Carroll et al, 2003b]. We continued to use our multi-source and multi-agent architecture. For Factoid questions we used all of our previous answering agents with an additional pattern-based agent, an enhanced answer resolution algorithm, and increased coverage of the Cyc sanity checker. We will devote a portion of this paper to performing a post-mortem of our experiences with Cyc this year. For List questions, which we did not attempt previously, we ran our Factoid system with different parameters. For Definition questions we took an entirely new approach, which we call QA-by-Dossier, and which will be the other focus of this paper. While we think that our system performed reasonably well in this subtask, the NIST evaluation results do not reflect this, raising some questions about the Definition subtask specification and evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PragerCCWIM03.bib) "
	```
	@inproceedings{DBLP:conf/trec/PragerCCWIM03,
		author = {John M. Prager and Jennifer Chu{-}Carroll and Krzysztof Czuba and Christopher A. Welty and Abraham Ittycheriah and Ruchi Mahindru},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {IBM's {PIQUANT} in {TREC2003}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {283--292},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/ibm-prager.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PragerCCWIM03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering using the DLT System at TREC 2003

_Richard F. E. Sutcliffe, Igal Gabbay, Michael Mulcahy, Kieran White_

- :fontawesome-solid-user-group: **Participant:** [ulimerick.sutcliffe](./qa/participants.md#ulimerick.sutcliffe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ulimerick.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/ulimerick.qa.pdf)
- :material-file-search: **Runs:** [DLT03QA01](./qa/runs.md#dlt03qa01) | [DLT03QA02](./qa/runs.md#dlt03qa02)

??? abstract "Abstract"
	
	This article outlines our participation in the Question Answering Track of the Text REtrieval Conference organised by the National Institute of Standards and Technology. This was our second year in the track and we hoped to improve our performance relative to 2002. In the next section we outline the general strategy we adopted, the changes relative to last year and the approaches taken to the three question types, namely factoid, list and definition. Following this the individual system components are described in more detail. Thirdly, the runs we submitted are presented together with the results obtained. Finally, conclusions are drawn based on our findings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SutcliffeGMW03.bib) "
	```
	@inproceedings{DBLP:conf/trec/SutcliffeGMW03,
		author = {Richard F. E. Sutcliffe and Igal Gabbay and Michael Mulcahy and Kieran White},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering using the {DLT} System at {TREC} 2003},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {686--698},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/ulimerick.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SutcliffeGMW03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDUQA on TREC2003 QA task

_Lide Wu, Xuanjing Huang, Yaqian Zhou, Yongping Du, Lan You_

- :fontawesome-solid-user-group: **Participant:** [fudanu.lide](./qa/participants.md#fudanu.lide)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/fudanu.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/fudanu.qa.pdf)
- :material-file-search: **Runs:** [FDUT12QA2](./qa/runs.md#fdut12qa2) | [FDUT12QA3](./qa/runs.md#fdut12qa3) | [FDUT12QA1](./qa/runs.md#fdut12qa1)

??? abstract "Abstract"
	
	It is the fourth time that we take part in the QA track. Our system, FDUQA, is based on our previous system (Wu et al, 2002). FDUQA includes an offline part and an online part. We make great efforts on the online part while leaving the offline part unchanged. We have tried many natural language processing techniques, and incorporated many sources of world knowledge, including Web. A novel Query formulation technique has also been put forward. In addition, we've tried another attempt on answer extraction in this year's task. In the second section, we will describe the architecture of our QA system; and give a detailed description on the Query formulation for Web search in the third section; while in the fourth section, we will introduce our new attempt on answer extraction; and we will present our performance in the last section.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHZDY03.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHZDY03,
		author = {Lide Wu and Xuanjing Huang and Yaqian Zhou and Yongping Du and Lan You},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FDUQA} on {TREC2003} {QA} task},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {246--253},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/fudanu.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHZDY03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Questioning Answering By Pattern Matching, Web-Proofing, Semantic  Form Proofing

_Min Wu, Xiaoyu Zheng, Michelle Duan, Ting Liu, Tomek Strzalkowski_

- :fontawesome-solid-user-group: **Participant:** [suny-albany.liu](./qa/participants.md#suny-albany.liu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ualbany-suny.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/ualbany-suny.qa.pdf)
- :material-file-search: **Runs:** [Albany03I2](./qa/runs.md#albany03i2) | [Albany03I3](./qa/runs.md#albany03i3) | [Albany03I4](./qa/runs.md#albany03i4)

??? abstract "Abstract"
	
	In this paper, we introduce the University at Albany's question answering system, ILQUA. It is developed on the following methods: pattern matching over annotated text, web-proofing and semantic form proofing. These methods are currently used in other QA systems, however, we revised them to work together in our QA system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuZDLS03.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuZDLS03,
		author = {Min Wu and Xiaoyu Zheng and Michelle Duan and Ting Liu and Tomek Strzalkowski},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Questioning Answering By Pattern Matching, Web-Proofing, Semantic Form Proofing},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {578--585},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/ualbany-suny.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuZDLS03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2003 QA at BBN: Answering Definitional Questions

_Jinxi Xu, Ana Licuanan, Ralph M. Weischedel_

- :fontawesome-solid-user-group: **Participant:** [bbn.xu](./qa/participants.md#bbn.xu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/bbn.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/bbn.qa.pdf)
- :material-file-search: **Runs:** [BBN2003C](./qa/runs.md#bbn2003c) | [BBN2003A](./qa/runs.md#bbn2003a) | [BBN2003B](./qa/runs.md#bbn2003b)

??? abstract "Abstract"
	
	In TREC 2003, we focused on definitional questions. For factoid and list questions, we simply re-used our TREC 2002 system with some modifications. For definitional QA, we adopted a hybrid approach that combines several complementary technology components. Information retrieval (IR) was used to retrieve from the corpus the relevant documents for each question. Various linguistic and extraction tools were used to analyze the retrieved texts and to extract various types of kernel facts from which the answer to the question is generated. These tools include name finding, parsing, co-reference resolution, proposition extraction, relation extraction and extraction of structured patterns. All text analysis functions except structured pattern extraction were carried out by Serif, a state of the art information extraction engine (Ramshaw, et al, 2001) from BBN. Section 2 summarizes our submission for factoid and list qeustion answering (QA). The rest of the paper focuses on defintional questions. Section 4 concludes this work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuLW03.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuLW03,
		author = {Jinxi Xu and Ana Licuanan and Ralph M. Weischedel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2003 {QA} at {BBN:} Answering Definitional Questions},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {98--106},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/bbn.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuLW03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QUALIFIER In TREC-12 QA Main Task

_Hui Yang, Hang Cui, Mstislav Maslennikov, Long Qiu, Min-Yen Kan, Tat-Seng Chua_

- :fontawesome-solid-user-group: **Participant:** [nus.yang](./qa/participants.md#nus.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/nus-yang.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/nus-yang.qa.pdf)
- :material-file-search: **Runs:** [nusmml03r1](./qa/runs.md#nusmml03r1) | [nusmml03r2](./qa/runs.md#nusmml03r2) | [nusmml03r3](./qa/runs.md#nusmml03r3)

??? abstract "Abstract"
	
	This paper describes a question answering system and its various modules to solve definition, factoid and list questions defined in the TREC12 Main task. In particular, we tackle the factoid QA task by Event-based Question Answering. Each QA event comprises of elements describing different facets like time, location, object, action etc. By analyzing the external knowledge from pre-retrieved TREC documents, Web documents, WordNet and Ontology to discover the QA event structure, we explore the inherent associations among QA elements and then obtain the answers. There are three subsystems working parallel to handle definition, factoid, and list questions separately. We highlight the shared modules, fine-grained named entity recognition, anaphora resolution and canonicalization co-reference resolution, among the three subsystems as well.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangCMQKC03.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangCMQKC03,
		author = {Hui Yang and Hang Cui and Mstislav Maslennikov and Long Qiu and Min{-}Yen Kan and Tat{-}Seng Chua},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{QUALIFIER} In {TREC-12} {QA} Main Task},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {480--488},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/nus-yang.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangCMQKC03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Language Modeling Approach to Passage Question Answering

_Dell Zhang, Wee Sun Lee_

- :fontawesome-solid-user-group: **Participant:** [nus.sun](./qa/participants.md#nus.sun)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/nus-zhang.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/nus-zhang.qa.pdf)
- :material-file-search: **Runs:** [nuslamp03a](./qa/runs.md#nuslamp03a) | [nuslamp03b](./qa/runs.md#nuslamp03b) | [nuslamp03](./qa/runs.md#nuslamp03)

??? abstract "Abstract"
	
	This paper reports our efforts on developing a language modeling approach to passage question answering. In particular, we address the following two problems: (i) generalized language modeling for question classification; (ii) constrained language modeling for passage retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangL03.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangL03,
		author = {Dell Zhang and Wee Sun Lee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Language Modeling Approach to Passage Question Answering},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {489--495},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/nus-zhang.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangL03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Novelty 

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

- :fontawesome-solid-user-group: **Participant:** [ccs.conroy](./novelty/participants.md#ccs.conroy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ccs.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/ccs.novelty.pdf)
- :material-file-search: **Runs:** [ccsumlaqr](./novelty/runs.md#ccsumlaqr) | [ccsumrelqr](./novelty/runs.md#ccsumrelqr) | [ccsumrelsvd](./novelty/runs.md#ccsumrelsvd) | [ccsummeosvd](./novelty/runs.md#ccsummeosvd) | [ccsummeoqr](./novelty/runs.md#ccsummeoqr) | [ccsum2svdpqr](./novelty/runs.md#ccsum2svdpqr) | [ccsumt2svdqr](./novelty/runs.md#ccsumt2svdqr) | [ccsumt2pqr](./novelty/runs.md#ccsumt2pqr) | [ccsumt2qr](./novelty/runs.md#ccsumt2qr) | [ccsum3svdpqr](./novelty/runs.md#ccsum3svdpqr) | [ccsum3qr](./novelty/runs.md#ccsum3qr) | [ccsum3pqr](./novelty/runs.md#ccsum3pqr) | [ccsumt4qr](./novelty/runs.md#ccsumt4qr) | [ccsumt4sqr01](./novelty/runs.md#ccsumt4sqr01) | [ccsum4spq001](./novelty/runs.md#ccsum4spq001) | [ccsumt4pqr](./novelty/runs.md#ccsumt4pqr) | [ccsum4svdpqr](./novelty/runs.md#ccsum4svdpqr)

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

- :fontawesome-solid-user-group: **Participant:** [irit-sig.boughanem](./novelty/participants.md#irit-sig.boughanem)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/irit-sig.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/irit-sig.novelty.pdf)
- :material-file-search: **Runs:** [IRITfNegR2](./novelty/runs.md#iritfnegr2) | [IRITf2bis](./novelty/runs.md#iritf2bis) | [IRITfb1MtmIb](./novelty/runs.md#iritfb1mtmib) | [IRITnip2bis](./novelty/runs.md#iritnip2bis) | [IRITnb1MtmI4](./novelty/runs.md#iritnb1mtmi4) | [Irit1](./novelty/runs.md#irit1) | [Irit5q](./novelty/runs.md#irit5q) | [IritMtm4](./novelty/runs.md#iritmtm4) | [IritMtm5](./novelty/runs.md#iritmtm5) | [Irito](./novelty/runs.md#irito)

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

- :fontawesome-solid-user-group: **Participant:** [uiowa.eichmann](./novelty/participants.md#uiowa.eichmann)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uiowa.novelty.genomics.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/uiowa.novelty.genomics.qa.pdf)
- :material-file-search: **Runs:** [UIowa03Nov01](./novelty/runs.md#uiowa03nov01) | [UIowa03Nov02](./novelty/runs.md#uiowa03nov02) | [UIowa03Nov03](./novelty/runs.md#uiowa03nov03) | [UIowa03Nov05](./novelty/runs.md#uiowa03nov05) | [UIowa03Nov04](./novelty/runs.md#uiowa03nov04) | [UIowa03Nov07](./novelty/runs.md#uiowa03nov07) | [UIowa03Nov08](./novelty/runs.md#uiowa03nov08) | [UIowa03Nov09](./novelty/runs.md#uiowa03nov09) | [UIowa03Nov06](./novelty/runs.md#uiowa03nov06) | [UIowa03Nov10](./novelty/runs.md#uiowa03nov10) | [UIowa03Nov11](./novelty/runs.md#uiowa03nov11) | [UIowa03Nov12](./novelty/runs.md#uiowa03nov12) | [UIowa03Nov14](./novelty/runs.md#uiowa03nov14) | [UIowa03Nov13](./novelty/runs.md#uiowa03nov13)

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

- :fontawesome-solid-user-group: **Participant:** [cas.nlpr](./novelty/participants.md#cas.nlpr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.novelty.robust.pdf](http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.novelty.robust.pdf)
- :material-file-search: **Runs:** [NLPR03n1w1](./novelty/runs.md#nlpr03n1w1) | [NLPR03n1f1](./novelty/runs.md#nlpr03n1f1) | [NLPR03n1f2](./novelty/runs.md#nlpr03n1f2) | [NLPR03n1w2](./novelty/runs.md#nlpr03n1w2) | [NLPR03n1w3](./novelty/runs.md#nlpr03n1w3) | [NLPR03n2d1](./novelty/runs.md#nlpr03n2d1) | [NLPR03n2s1](./novelty/runs.md#nlpr03n2s1) | [NLPR03n2d2](./novelty/runs.md#nlpr03n2d2) | [NLPR03n2d3](./novelty/runs.md#nlpr03n2d3) | [NLPR03n2s2](./novelty/runs.md#nlpr03n2s2) | [NLPR03n3d1](./novelty/runs.md#nlpr03n3d1) | [NLPR03n3s1](./novelty/runs.md#nlpr03n3s1) | [NLPR03n3d3](./novelty/runs.md#nlpr03n3d3) | [NLPR03n3d2](./novelty/runs.md#nlpr03n3d2) | [NLPR03n3s2](./novelty/runs.md#nlpr03n3s2) | [NLPR03n4d1](./novelty/runs.md#nlpr03n4d1) | [NLPR03n4d2](./novelty/runs.md#nlpr03n4d2) | [NLPR03n4s1](./novelty/runs.md#nlpr03n4s1) | [NLPR03n4s2](./novelty/runs.md#nlpr03n4s2) | [NLPR03n4s3](./novelty/runs.md#nlpr03n4s3)

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

- :fontawesome-solid-user-group: **Participant:** [umarylandbc.kallurkar](./novelty/participants.md#umarylandbc.kallurkar)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/umbc.web.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/umbc.web.novelty.pdf)
- :material-file-search: **Runs:** [umbcrun1](./novelty/runs.md#umbcrun1) | [umbcrun2](./novelty/runs.md#umbcrun2) | [umbcrun3](./novelty/runs.md#umbcrun3) | [umbcnew2](./novelty/runs.md#umbcnew2) | [umbcnew3](./novelty/runs.md#umbcnew3) | [umbcnew1](./novelty/runs.md#umbcnew1)

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

- :fontawesome-solid-user-group: **Participant:** [clresearch](./novelty/participants.md#clresearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/clresearch.qa.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/clresearch.qa.novelty.pdf)
- :material-file-search: **Runs:** [clr03n1t](./novelty/runs.md#clr03n1t) | [clr03n1n3](./novelty/runs.md#clr03n1n3) | [clr03n1n2](./novelty/runs.md#clr03n1n2) | [clr03n1d](./novelty/runs.md#clr03n1d) | [clr03n2](./novelty/runs.md#clr03n2) | [clr03n3f01](./novelty/runs.md#clr03n3f01) | [clr03n3f02](./novelty/runs.md#clr03n3f02) | [clr03n3f03](./novelty/runs.md#clr03n3f03) | [clr03n3f05](./novelty/runs.md#clr03n3f05) | [clr03n4](./novelty/runs.md#clr03n4) | [clr03n3f04](./novelty/runs.md#clr03n3f04)

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

- :fontawesome-solid-user-group: **Participant:** [meijiu.takagi](./novelty/participants.md#meijiu.takagi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/meijiu.web.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/meijiu.web.novelty.pdf)
- :material-file-search: **Runs:** [MeijiHilF11](./novelty/runs.md#meijihilf11) | [MeijiHilF12](./novelty/runs.md#meijihilf12) | [MeijiHilF13](./novelty/runs.md#meijihilf13) | [MeijiHilF14](./novelty/runs.md#meijihilf14) | [MeijiHilF15](./novelty/runs.md#meijihilf15) | [MeijiHilF21](./novelty/runs.md#meijihilf21) | [MeijiHilF22](./novelty/runs.md#meijihilf22) | [MeijiHilF23](./novelty/runs.md#meijihilf23) | [MeijiHilF24](./novelty/runs.md#meijihilf24) | [MeijiHilF31](./novelty/runs.md#meijihilf31) | [MeijiHilF32](./novelty/runs.md#meijihilf32) | [MeijiHilF33](./novelty/runs.md#meijihilf33) | [MeijiHilF34](./novelty/runs.md#meijihilf34) | [MeijiHilF41](./novelty/runs.md#meijihilf41) | [MeijiHilF42](./novelty/runs.md#meijihilf42) | [MeijiHilF43](./novelty/runs.md#meijihilf43) | [MeijiHilF44](./novelty/runs.md#meijihilf44)

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

- :fontawesome-solid-user-group: **Participant:** [umich.radev](./novelty/participants.md#umich.radev)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/umich.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/umich.novelty.pdf)
- :material-file-search: **Runs:** [umich1](./novelty/runs.md#umich1) | [umich5](./novelty/runs.md#umich5) | [umich4](./novelty/runs.md#umich4) | [umich3](./novelty/runs.md#umich3) | [umich2](./novelty/runs.md#umich2) | [umich23](./novelty/runs.md#umich23) | [umich22](./novelty/runs.md#umich22) | [umich21](./novelty/runs.md#umich21) | [umich24](./novelty/runs.md#umich24) | [umich25](./novelty/runs.md#umich25) | [umich32](./novelty/runs.md#umich32) | [umich31](./novelty/runs.md#umich31) | [umich33](./novelty/runs.md#umich33) | [umich34](./novelty/runs.md#umich34) | [umich35](./novelty/runs.md#umich35) | [umich41](./novelty/runs.md#umich41) | [umich43](./novelty/runs.md#umich43) | [umich42](./novelty/runs.md#umich42) | [umich45](./novelty/runs.md#umich45) | [umich44](./novelty/runs.md#umich44)

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

- :fontawesome-solid-user-group: **Participant:** [iitb.ramakrishnan](./novelty/participants.md#iitb.ramakrishnan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/iit.novelty.hard2.pdf](http://trec.nist.gov/pubs/trec12/papers/iit.novelty.hard2.pdf)
- :material-file-search: **Runs:** [IITBN1](./novelty/runs.md#iitbn1)

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

- :fontawesome-solid-user-group: **Participant:** [cas-ict.bin](./novelty/participants.md#cas-ict.bin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.novelty.web.pdf](http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.novelty.web.pdf)
- :material-file-search: **Runs:** [ICT03NOV1BSL](./novelty/runs.md#ict03nov1bsl) | [ICT03NOV1SQR](./novelty/runs.md#ict03nov1sqr) | [ICT03NOV1XTD](./novelty/runs.md#ict03nov1xtd) | [ICT03NOV1DTH](./novelty/runs.md#ict03nov1dth) | [ICT03NOV1NAR](./novelty/runs.md#ict03nov1nar) | [ICT03NOV2SQR](./novelty/runs.md#ict03nov2sqr) | [ICT03NOV2CUR](./novelty/runs.md#ict03nov2cur) | [ICT03NOV2PNK](./novelty/runs.md#ict03nov2pnk) | [ICT03NOV2LPP](./novelty/runs.md#ict03nov2lpp) | [ICT03NOV2LPA](./novelty/runs.md#ict03nov2lpa) | [ICT03NOV3KNN](./novelty/runs.md#ict03nov3knn) | [ICT03NOV3IKK](./novelty/runs.md#ict03nov3ikk) | [ICT03NOV3KNS](./novelty/runs.md#ict03nov3kns) | [ICT03NOV3WND](./novelty/runs.md#ict03nov3wnd) | [ICT03NOV3WN3](./novelty/runs.md#ict03nov3wn3) | [ICT03NOV4SQR](./novelty/runs.md#ict03nov4sqr) | [ICT03NOV4WNW](./novelty/runs.md#ict03nov4wnw) | [ICT03NOV4OTP](./novelty/runs.md#ict03nov4otp) | [ICT03NOV4ALL](./novelty/runs.md#ict03nov4all) | [ICT03NOV4LFF](./novelty/runs.md#ict03nov4lff)

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

- :fontawesome-solid-user-group: **Participant:** [ntu.chen](./novelty/participants.md#ntu.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ntu.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/ntu.novelty.pdf)
- :material-file-search: **Runs:** [NTU11](./novelty/runs.md#ntu11) | [NTU13](./novelty/runs.md#ntu13) | [NTU15](./novelty/runs.md#ntu15) | [NTU14](./novelty/runs.md#ntu14) | [NTU12](./novelty/runs.md#ntu12) | [NTU21](./novelty/runs.md#ntu21) | [NTU22](./novelty/runs.md#ntu22) | [NTU24](./novelty/runs.md#ntu24) | [NTU23](./novelty/runs.md#ntu23) | [NTU25](./novelty/runs.md#ntu25) | [NTU31](./novelty/runs.md#ntu31) | [NTU32](./novelty/runs.md#ntu32) | [NTU33](./novelty/runs.md#ntu33) | [NTU34](./novelty/runs.md#ntu34) | [NTU35](./novelty/runs.md#ntu35) | [NTU42](./novelty/runs.md#ntu42) | [NTU44](./novelty/runs.md#ntu44) | [NTU43](./novelty/runs.md#ntu43) | [NTU41](./novelty/runs.md#ntu41) | [NTU45](./novelty/runs.md#ntu45)

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

- :fontawesome-solid-user-group: **Participant:** [tsinghuau.ma](./novelty/participants.md#tsinghuau.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/tsinghuau.novelty.robust.web.pdf](http://trec.nist.gov/pubs/trec12/papers/tsinghuau.novelty.robust.web.pdf)
- :material-file-search: **Runs:** [THUIRnv0311](./novelty/runs.md#thuirnv0311) | [THUIRnv0312](./novelty/runs.md#thuirnv0312) | [THUIRnv0313](./novelty/runs.md#thuirnv0313) | [THUIRnv0314](./novelty/runs.md#thuirnv0314) | [THUIRnv0315](./novelty/runs.md#thuirnv0315) | [THUIRnv0322](./novelty/runs.md#thuirnv0322) | [THUIRnv0332](./novelty/runs.md#thuirnv0332) | [THUIRnv0331](./novelty/runs.md#thuirnv0331) | [THUIRnv0334](./novelty/runs.md#thuirnv0334) | [THUIRnv0333](./novelty/runs.md#thuirnv0333) | [THUIRnv0321](./novelty/runs.md#thuirnv0321) | [THUIRnv0323](./novelty/runs.md#thuirnv0323) | [THUIRnv0342](./novelty/runs.md#thuirnv0342) | [THUIRnv0341](./novelty/runs.md#thuirnv0341) | [THUIRnv0343](./novelty/runs.md#thuirnv0343) | [THUIRnv0344](./novelty/runs.md#thuirnv0344) | [THUIRnv0345](./novelty/runs.md#thuirnv0345)

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

