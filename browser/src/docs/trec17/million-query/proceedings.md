# Proceedings - Million Query 2008 

#### Million Query Track 2008 Overview

_James Allan, Javed A. Aslam, Virgil Pavlu, Evangelos Kanoulas, Ben Carterette_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec17/papers/MQ.OVERVIEW.pdf](https://trec.nist.gov/pubs/trec17/papers/MQ.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The Million Query (1MQ) track ran for the second time in TREC 2008. The track is designed to serve two purposes: first, it is an exploration of ad-hoc retrieval over a large set of queries and a large collection of documents; second, it investigates questions of system evaluation, in particular whether it is better to evaluate using many shallow judgments or fewer thorough judgments. As with the 2007 track [ACA+07], participants ran 10,000 queries against a collection of 25 million documents. The 2008 track differed in the following ways: 1. Queries were assigned to one of four categories. 2. Each query was assigned a target of 8, 16, 32, 64, or 128 judgments. 3. Assessors could judge documents “not relevant but reasonable”. Section 1 describes how the corpus and queries were selected, the query classes, details of the submission formats, and a brief description of each submitted run. Section 2 provides an overview of the judging process, including a sketch of how it alternated between two methods for selecting the small set of documents to be judged. Sections 3.1 and 3.2 provide an overview of those two selection methods, developed at UMass and NEU, respectively. In Section 4 we present statistics collected during the judging process, including the total number of queries judged, how many judgments were served by each approach, and so on, along with the overall results of the track. We present additional results and analysis in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanAPKC08.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanAPKC08,
		author = {James Allan and Javed A. Aslam and Virgil Pavlu and Evangelos Kanoulas and Ben Carterette},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Million Query Track 2008 Overview},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {https://trec.nist.gov/pubs/trec17/papers/MQ.OVERVIEW.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AllanAPKC08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Distributed Multisearch and Resource Selection for the TREC Million  Query Track

_Christopher T. Fallen, Gregory B. Newby, Kylie McCormick_

- :fontawesome-solid-user-group: **Participant:** [ARSC08](./participants.md#arsc08)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/ualaska.mq.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/ualaska.mq.rev.pdf)
- :material-file-search: **Runs:** [lsi150stat](./runs.md#lsi150stat) | [vsmstat](./runs.md#vsmstat) | [vsmstat07](./runs.md#vsmstat07) | [lsi150dyn](./runs.md#lsi150dyn) | [vsmdyn](./runs.md#vsmdyn)

??? abstract "Abstract"
	
	A distributed information retrieval system with resource-selection and result-set merging capability was used to search subsets of the GOV2 document corpus for the 2008 TREC Million Query Track. The GOV2 collection was partitioned into host-name subcollections and distributed to multiple remote machines. The Multisearch demonstration application restricted each search to a fraction of the available sub-collections that was pre-determined by a resource-selection algorithm. Experiment results from topic-by-topic resource selection and aggregate topic resource selection are compared. The sensitivity of Multisearch retrieval performance to variations in the resource selection algorithm is discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FallenNM08.bib) "
	```
	@inproceedings{DBLP:conf/trec/FallenNM08,
		author = {Christopher T. Fallen and Gregory B. Newby and Kylie McCormick},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Distributed Multisearch and Resource Selection for the {TREC} Million Query Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/ualaska.mq.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FallenNM08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

