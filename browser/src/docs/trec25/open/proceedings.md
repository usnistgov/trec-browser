# Proceedings - OpenSearch 2016 

#### Webis at TREC 2016: Tasks, Total Recall, and Open Search Tracks

_Matthias Hagen, Johannes Kiesel, Payam Adineh, Masoud Alahyari, Ehsan Fatehifar, Arefeh Bahrami, Pia Fichtl, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [Webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/Webis-T-TR-O.pdf](http://trec.nist.gov/pubs/trec25/papers/Webis-T-TR-O.pdf)
- :material-file-search: **Runs:** [webis-SSOAR-2](./runs.md#webis-ssoar-2) | [webis-CiteSeerX-2](./runs.md#webis-citeseerx-2)

??? abstract "Abstract"
	
	We give a brief overview of the Webis group's participation in the TREC 2016 Tasks, Total Recall, and Open Search tracks. Our submissions to the Tasks track are similar to our last year's system. In the task understanding subtask of the Tasks track, we use different data sources (ClueWeb12 anchor texts, AOL query log, Wikidata, etc.) and APIs (Google, Bing, etc.) to retrieve suggestions related to a given query. For the task completion and ad-hoc subtask, we combine the results of the Indri search engine for the different related queries identified in the task understanding subtask. Our system for the the Total Recall track also is similar to our last year's idea with some slight changes in the details; we employ a simple SVM baseline with variable batch sizes equipped with a keyqueries step to identify potentially relevant documents. In the Open Search track, we axiomatically re-rank a BM25-ordered result list to come up with a final document ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenKAAFBFS16.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenKAAFBFS16,
		author = {Matthias Hagen and Johannes Kiesel and Payam Adineh and Masoud Alahyari and Ehsan Fatehifar and Arefeh Bahrami and Pia Fichtl and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2016: Tasks, Total Recall, and Open Search Tracks},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/Webis-T-TR-O.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenKAAFBFS16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2016 OpenSearch Track: Search Ranking Based on Clickthrough  Data

_Cheng Li, Zhen Yang, David Lillis_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/BJUT-O.pdf](http://trec.nist.gov/pubs/trec25/papers/BJUT-O.pdf)
- :material-file-search: **Runs:** [BJUT-CiteSeerX-1](./runs.md#bjut-citeseerx-1) | [BJUT-CiteSeerX-2](./runs.md#bjut-citeseerx-2)

??? abstract "Abstract"
	
	In this paper we describe our efforts for the TREC OpenSearch task. Our goal for this year is to evaluate the effectiveness of: (1) a ranking method using information crawled from an authoritative search engine; (2) search ranking based on clickthrough data taken from user feedback; and (3) a unified modeling method that combines knowledge from the web search engine and the users' clickthrough data. Finally, we conduct extensive experiments to evaluate the proposed framework on the TREC 2016 OpenSearch data set, with promising results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiYL16.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiYL16,
		author = {Cheng Li and Zhen Yang and David Lillis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2016 OpenSearch Track: Search Ranking Based on Clickthrough Data},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/BJUT-O.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiYL16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IR-IITBHU at TREC 2016 Open Search Track: Retrieving documents  using Divergence From Randomness model in Terrier

_Mitodru Niyogi, Sukomal Pal_

- :fontawesome-solid-user-group: **Participant:** [IR-IITBHU](./participants.md#ir-iitbhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/IR-IITBHU-O.pdf](http://trec.nist.gov/pubs/trec25/papers/IR-IITBHU-O.pdf)
- :material-file-search: **Runs:** [opensearch_404-CiteSeerX-1](./runs.md#opensearch_404-citeseerx-1) | [opensearch_404-CiteSeerX-2](./runs.md#opensearch_404-citeseerx-2) | [opensearch_404-SSOAR-1](./runs.md#opensearch_404-ssoar-1) | [opensearch_404-SSOAR-2](./runs.md#opensearch_404-ssoar-2)

??? abstract "Abstract"
	
	In our participation at TREC 2016 Open Search Track which focuses on ad-hoc scientifc literature search, we used Terrier, a modular and a scalable Information Retrieval framework as a tool to rank documents. The organizers provided live data as documents, queries and user interactions from real search engine that were available through Living Lab API framework. The data was then converted into TREC format to be used in Terrier. We used Divergence from Randomness (DFR) model, specifically, the Inverse expected document frequency model for randomness, the ratio of two Bernoulli's processes for first normalisation, and normalisation 2 for term frequency normalization with natural logarithm, i.e., In_expC2 model to rank the available documents in response to a set of queries. Altogether we submit 391 runs for sites CiteSeerX and SSOAR to the Open Search Track via the Living Lab API framework. We received an `outcome' of 0.72 for test queries and 0.62 for train queries of site CiteSeerX at the end of Round 3 Test Period where, the 'outcome' is computed as: #wins / (#wins + #losses). A `win' occurs when the participant achieves more clicks on his documents than those of the site and `loss' otherwise. Complete relevance judgments is awaited at the moment. We look forward to getting the users' feedback and work further with them.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NiyogiP16.bib) "
	```
	@inproceedings{DBLP:conf/trec/NiyogiP16,
		author = {Mitodru Niyogi and Sukomal Pal},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IR-IITBHU} at {TREC} 2016 Open Search Track: Retrieving documents using Divergence From Randomness model in Terrier},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/IR-IITBHU-O.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NiyogiP16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Popularity Ranking for Scientific Literature Using the Characteristic  Scores and Scale Method

_Philipp Schaer, Narges Tavakolpoursaleh_

- :fontawesome-solid-user-group: **Participant:** [THKoeln-GESIS](./participants.md#thkoeln-gesis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/THKoeln-GESIS-O.pdf](http://trec.nist.gov/pubs/trec25/papers/THKoeln-GESIS-O.pdf)
- :material-file-search: **Runs:** [Gesis-SSOAR-1](./runs.md#gesis-ssoar-1) | [Gesis-SSOAR-2](./runs.md#gesis-ssoar-2) | [Gesis-CiteSeerX-1](./runs.md#gesis-citeseerx-1) | [Gesis-CiteSeerX-2](./runs.md#gesis-citeseerx-2)

??? abstract "Abstract"
	
	The TREC 2016 OpenSearch track is focused on ad-hoc search for scientific literature. Three scientific search engines and document repositories were part of this living lab-centered evaluation campaign: (1) CiteSeerX, (2) Microsoft Academic Search, and (3) SSOAR - Social Science Open Access Repository. The authors of this paper are also responsible for the implementation of the living lab infrastructure and the LL4IR API that is necessary to include an online system into the OpenSearch evaluation campaign. This work is based on a Master's thesis at University of Bonn [7]. Implementation details can be found there and in the lab's overview paper [1] and from a higher perspective in [6]. In this paper we will present our work on popularity-based relevance ranking within the two systems CiteSeerX and SSOAR. Both offer different types of usage and popularity data. We would like to test a normalization method for these kind of data known as the Characteristic Scores and Scale Method (CSS).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchaerT16.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchaerT16,
		author = {Philipp Schaer and Narges Tavakolpoursaleh},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Popularity Ranking for Scientific Literature Using the Characteristic Scores and Scale Method},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/THKoeln-GESIS-O.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchaerT16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

