# Proceedings - Tasks 2016 

#### Overview of the TREC Tasks Track 2016

_Manisha Verma, Emine Yilmaz, Rishabh Mehrotra, Evangelos Kanoulas, Ben Carterette, Nick Craswell, Peter Bailey_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/Overview-T.pdf](http://trec.nist.gov/pubs/trec25/papers/Overview-T.pdf)
??? abstract "Abstract"
	
	Research in Information Retrieval has traditionally focused on serving the best results for a single query, ignoring the reasons (or the task) that might have motivated the user to submit that query. Often times search engines are used to complete complex tasks (information needs); achieving these tasks with current search engines requires users to issue multiple queries. For example, booking travel to a location such as London could require the user to submit various queries such as flights to London, hotels in London, points of interest around London etc. Standard evaluation mechanisms focus on evaluating the quality of a retrieval system in terms of the relevance of the results retrieved, completely ignoring the fact that user satisfaction mainly depends on the usefulness of the system in helping the user complete the actual task that led the user issue the query. Similar to Tasks Track 2015 [1], Tasks Track 2016 is an attempt investigate quality of retrieval systems in terms of (1) how well they can understand the underlying task that led the user submit a query, and (2) how useful they are for helping users complete their tasks. In this overview, we first summarise the three categories of evaluation mechanisms used in the track and briefly describe the corpus, topics, and tasks that comprise the test collections. We then give an overview of the runs submitted to the Tasks Track and present evaluation results and analysis.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VermaYMKCCB16.bib) "
	```
	@inproceedings{DBLP:conf/trec/VermaYMKCCB16,
		author = {Manisha Verma and Emine Yilmaz and Rishabh Mehrotra and Evangelos Kanoulas and Ben Carterette and Nick Craswell and Peter Bailey},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} Tasks Track 2016},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/Overview-T.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VermaYMKCCB16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Stavanger at the TREC 2016 Tasks Track

_Darío Garigliotti, Krisztian Balog_

- :fontawesome-solid-user-group: **Participant:** [UiS](./participants.md#uis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/UiS-T.pdf](http://trec.nist.gov/pubs/trec25/papers/UiS-T.pdf)
- :material-file-search: **Runs:** [UiS_4](./runs.md#uis_4) | [UiS_8](./runs.md#uis_8) | [UiS_9](./runs.md#uis_9)

??? abstract "Abstract"
	
	This paper describes our participation in the Task understanding task of the Tasks track at TREC 2016. We introduce a general probabilistic framework in which we combine query suggestions from web search engines with keyphrases generated from top ranked documents. We achieved top performance among all submitted systems, on both official evaluation metrics, which attests the effectiveness of our approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GarigliottiB16.bib) "
	```
	@inproceedings{DBLP:conf/trec/GarigliottiB16,
		author = {Dar{\'{\i}}o Garigliotti and Krisztian Balog},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {The University of Stavanger at the {TREC} 2016 Tasks Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/UiS-T.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GarigliottiB16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2016: Tasks, Total Recall, and Open Search Tracks

_Matthias Hagen, Johannes Kiesel, Payam Adineh, Masoud Alahyari, Ehsan Fatehifar, Arefeh Bahrami, Pia Fichtl, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [Webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/Webis-T-TR-O.pdf](http://trec.nist.gov/pubs/trec25/papers/Webis-T-TR-O.pdf)
- :material-file-search: **Runs:** [webisA1](./runs.md#webisa1) | [webisA2](./runs.md#webisa2) | [webisA3](./runs.md#webisa3) | [webisC1](./runs.md#webisc1) | [webisC2](./runs.md#webisc2) | [webisC3](./runs.md#webisc3) | [webis1](./runs.md#webis1) | [webis2](./runs.md#webis2) | [webis3](./runs.md#webis3)

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

