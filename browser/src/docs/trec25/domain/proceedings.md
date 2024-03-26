# Proceedings - Dynamic Domain 2016 

#### TREC 2016 Dynamic Domain Track Overview

_Grace Hui Yang, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/Overview-DD.pdf](http://trec.nist.gov/pubs/trec25/papers/Overview-DD.pdf)
??? abstract "Abstract"
	
	The main goal of TREC dynamic domain track is to explore and evaluate systems for interactive information retrieval, which reflects real-world search scenarios. Due to the importance of learning from user interactions, this track has been held for the second year. The name of the track contains two parts. “Dynamic” means that the search system dynamically adapts the provided ranking to the user through interactions. “Domain” stems from the fact that the search task in the track is on the domains of special interests, which tend to bring information needs that would not be met within a single interaction. The task is inspired by interested groups in government, including the DARPA Memex program. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangS16.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangS16,
		author = {Grace Hui Yang and Ian Soboroff},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2016 Dynamic Domain Track Overview},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/Overview-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangS16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT @ TREC 2016 Dynamic Domain Track: Exploiting Passage Representation  for Retrieval and Relevance Feedback

_Ameer Albahem, Damiano Spina, Lawrence Cavedon, Falk Scholer_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/RMIT-DD.pdf](http://trec.nist.gov/pubs/trec25/papers/RMIT-DD.pdf)
- :material-file-search: **Runs:** [rmit_lm_nqe](./runs.md#rmit_lm_nqe) | [rmit_oracle.lm.1000](./runs.md#rmit_oracle.lm.1000) | [rmit_lm_psg.max](./runs.md#rmit_lm_psg.max) | [rmit_lm_rocchio.Rp.NRd.10](./runs.md#rmit_lm_rocchio.rp.nrd.10)

??? abstract "Abstract"
	
	The TREC Dynamic Domain search task addresses search scenarios where users engage interactively with search systems to tackle domain specific information needs. In our participation, we focused on utilizing passage-based representations in document retrieval and user feedback processing. In addition, we submitted a baseline retrieval method and a manual run that considers only relevant documents in the top 1000 retrieved documents. Results show that the passage based representation is inferior to the baseline method but differences are not statistically significant in terms of the Cube Test and the Average Cube Test metrics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlbahemSCS16.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlbahemSCS16,
		author = {Ameer Albahem and Damiano Spina and Lawrence Cavedon and Falk Scholer},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{RMIT} @ {TREC} 2016 Dynamic Domain Track: Exploiting Passage Representation for Retrieval and Relevance Feedback},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/RMIT-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlbahemSCS16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Evaluation of a Feedback Algorithm inspired by Quantum Detection for  Dynamic Search Tasks

_Emanuele Di Buccio, Massimo Melucci_

- :fontawesome-solid-user-group: **Participant:** [UPD_IA](./participants.md#upd_ia)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/UPD_IA-DD.pdf](http://trec.nist.gov/pubs/trec25/papers/UPD_IA-DD.pdf)
- :material-file-search: **Runs:** [UPD_IA_BiQBFi](./runs.md#upd_ia_biqbfi) | [UPD_IA_BiQBDiJ](./runs.md#upd_ia_biqbdij)

??? abstract "Abstract"
	
	In this paper we investigate the effectiveness of Relevance Feedback algorithms inspired by Quantum Detection in the context of the Dynamic Domain track. Documents and queries are represented as vectors; the query vector is projected into the subspace spanned by the eigenvector which maximizes the distance between the distribution of quantum probability of relevance and the distribution of quantum probability of non-relevance. When relevant documents are present in the feedback set, the algorithm performs Explicit RF exploiting evidence gathered from relevant passages; if all the documents in the top retrieved are judged as non-relevant, Pseudo RF is performed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuccioM16.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuccioM16,
		author = {Emanuele Di Buccio and Massimo Melucci},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Evaluation of a Feedback Algorithm inspired by Quantum Detection for Dynamic Search Tasks},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/UPD\_IA-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuccioM16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Laval University at TREC Dynamic Domain 2016: Subtopic extraction  focused on Named Entities

_Robin Joganah, Richard Khoury, Luc Lamontagne_

- :fontawesome-solid-user-group: **Participant:** [LavalLakehead](./participants.md#lavallakehead)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/LavalLakehead-DD.pdf](http://trec.nist.gov/pubs/trec25/papers/LavalLakehead-DD.pdf)
- :material-file-search: **Runs:** [UL_BM25](./runs.md#ul_bm25) | [UL_LDA_200](./runs.md#ul_lda_200) | [UL_LDA_NE](./runs.md#ul_lda_ne) | [UL_LDA_Psum](./runs.md#ul_lda_psum) | [UL_Kmeans](./runs.md#ul_kmeans)

??? abstract "Abstract"
	
	This paper describes the results submitted by Laval University to the TREC 2016 Dynamic Domain track. We submitted five runs. For this year we decided to focus around Named Entities to interpret the subtopics. Named Entities are one of the two types of queries we identified in this challenge, the other being queries about concepts. We describe in this paper our experiments to determine if targeting this type of query with a specific pipeline can lead to a global improvement of the system by taking into account the specificity of the queries
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JoganahKL16.bib) "
	```
	@inproceedings{DBLP:conf/trec/JoganahKL16,
		author = {Robin Joganah and Richard Khoury and Luc Lamontagne},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Laval University at {TREC} Dynamic Domain 2016: Subtopic extraction focused on Named Entities},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/LavalLakehead-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JoganahKL16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UFMG at the TREC 2016 Dynamic Domain track

_Felipe Moraes, Rodrygo L. T. Santos, Nivio Ziviani_

- :fontawesome-solid-user-group: **Participant:** [ufmg](./participants.md#ufmg)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/ufmg-DD.pdf](http://trec.nist.gov/pubs/trec25/papers/ufmg-DD.pdf)
- :material-file-search: **Runs:** [ufmgHS2](./runs.md#ufmghs2) | [ufmgXS2](./runs.md#ufmgxs2) | [ufmgHM2](./runs.md#ufmghm2) | [ufmgXM2](./runs.md#ufmgxm2) | [ufmgHM3](./runs.md#ufmghm3)

??? abstract "Abstract"
	
	In TREC 2016, we focus on tackling the challenges posed by the Dynamic Domain (DD) track. The goal of the TREC DD track is to support research in dynamic, exploratory search within a complex domain. To this end, our participation investigates the suitability of multiple diversification approaches for dynamic information retrieval. In particular, based on fine-grained real-time feedback obtained from a simulated user, we apply diversification strategies that make use of single-source as well multi-source information for mining flat or hierarchical query aspects.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoraesSZZ16.bib) "
	```
	@inproceedings{DBLP:conf/trec/MoraesSZZ16,
		author = {Felipe Moraes and Rodrygo L. T. Santos and Nivio Ziviani},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UFMG} at the {TREC} 2016 Dynamic Domain track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/ufmg-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MoraesSZZ16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Investigation of Basic Retrieval Models for the Dynamic Domain  Task

_Razieh Rahimi, Grace Hui Yang_

- :fontawesome-solid-user-group: **Participant:** [georgetown](./participants.md#georgetown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/georgetown-DD.pdf](http://trec.nist.gov/pubs/trec25/papers/georgetown-DD.pdf)
- :material-file-search: **Runs:** [FirstIterBaseline](./runs.md#firstiterbaseline) | [SecondIterationBaseline](./runs.md#seconditerationbaseline) | [FifthIterBaseline](./runs.md#fifthiterbaseline) | [TenthIterBaseline](./runs.md#tenthiterbaseline)

??? abstract "Abstract"
	
	TREC dynamic domain is a new challenging task, which aims to simultaneously optimize the performance of retrieval and the number of iterations to accomplish the search task in a session-based search environment with a more sophisticated feedback information from the user. As a first step towards developing an effective search systems for this task, we investigate the characteristics of the newly created dataset for this task, and performance of basic well-known retrieval models for it. Our investigation demonstrates that the query sets contain multiple difficult queries, where initial results may provide very limited evidence for improvement in subsequent iterations. The new setting of the task and characteristics of dataset stress the need for more comprehensive metrics of performance evaluation, in terms of result diversity as an example.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RahimiY16.bib) "
	```
	@inproceedings{DBLP:conf/trec/RahimiY16,
		author = {Razieh Rahimi and Grace Hui Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {An Investigation of Basic Retrieval Models for the Dynamic Domain Task},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/georgetown-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RahimiY16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

