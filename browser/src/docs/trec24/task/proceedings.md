# Proceedings - Tasks 2015 

#### Overview of the TREC 2015 Tasks Track

_Emine Yilmaz, Manisha Verma, Rishabh Mehrotra, Evangelos Kanoulas, Ben Carterette, Nick Craswell_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/Overview-T.pdf](http://trec.nist.gov/pubs/trec24/papers/Overview-T.pdf)
??? abstract "Abstract"
	
	Research in Information Retrieval has traditionally focused on serving the best results for a single query, ignoring the reasons (or the task) that might have motivated the user to submit that query. Often times search engines are used to complete complex tasks (information needs); achieving these tasks with current search engines requires users to issue multiple queries. For example, booking travel to a location such as London could require the user to submit various queries such as flights to London, hotels in London, points of interest around London, etc. Standard evaluation mechanisms focus on evaluating the quality of a retrieval system in terms of the relevance of the results retrieved, completely ignoring the fact that user satisfaction mainly depends on the usefullness of the system in helping the user complete the actual task that led the user issue the query. The TREC 2015 Tasks Track is an attempt in devising mechanisms for evaluating quality of retrieval systems in terms of (1) how well they can understand the underlying task that led the user submit a query, and (2) how useful they are for helping users complete their tasks. In this overview, we first summarise the three categories of evaluation mechanisms used in the track and briefly describe the corpus, topics, and tasks that comprise the test collections. We then give an overview of the runs submitted to the Tasks Track and present evaluation results and analysis.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YilmazVMKCC15.bib) "
	```
	@inproceedings{DBLP:conf/trec/YilmazVMKCC15,
		author = {Emine Yilmaz and Manisha Verma and Rishabh Mehrotra and Evangelos Kanoulas and Ben Carterette and Nick Craswell},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2015 Tasks Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/Overview-T.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YilmazVMKCC15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mining Tasks from the Web Anchor Text Graph: MSR Notebook Paper  for the TREC 2015 Tasks Track

_Paul N. Bennett, Ryen W. White_

- :fontawesome-solid-user-group: **Participant:** [MSRTasks](./participants.md#msrtasks)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/MSRTasks-T.pdf](http://trec.nist.gov/pubs/trec24/papers/MSRTasks-T.pdf)
- :material-file-search: **Runs:** [MSRTasksQUrun3](./runs.md#msrtasksqurun3)

??? abstract "Abstract"
	
	Users may have a variety of tasks that give rise to issuing a particular query. The goal of the Tasks Track at TREC 2015 was to identify all aspects or subtasks of a user's task as well as the documents relevant to the entire task. This was broken into two parts: (1) Task Understanding which judged relevance of key phrases or queries to the original query (relative to a likely task that would have given rise to both); (2) Task Completion which performed document retrieval and measured usefulness to any task a user with the query might be peforming through either a completion measure that uses both relevance and usefulness criteria or more simply through an ad hoc retrieval measure of relevance alone. We submitted a run in the Task Understanding track. In particular, since the anchor text graph has proven useful in the general realm of query reformulation [2], we sought to quantify the value of extracting key phrases from anchor text in the broader setting of the task understanding track. Given a query, our approach considers a simple method for identifying a relevant and diverse set of key phrases related to the possible tasks that might have given rise to the query. In particular, given the effectiveness of sessions for producing query suggestions as well as the fact that sessions tend to be both topically coherent and cohesive with respect to a task, we investigated the effectiveness of mining session co-occurrence data. For a search engine log, session boundaries can be defined in the typical way but to operate over the anchor text graph, we need some notion of a “session”. We adopt the suggestion of Dang & Croft [2] and treat different links pointing to the same document as belonging to the same “session”. The basic assumption is that the anchor text of two links pointing to the same document are related via the common reference. Note that this assumption is based on the destination URL of the link being the same. Given a query, we then find matching seed candidates (link text from the web graph or queries over search logs) and expand to related candidate key phrases via this session assumption. The final ranking is based on a combination of  session count and the similarity of a link to the query. Additionally we perform several types of filtering that prevent over-expanding the set of related queries. We refer to the method as “having coverage” if the method was able to find a matching seed - since this is a necessary step to producing any candidates based on co-occurrence. Empirical results demonstrate generally good performance for the method when it finds a matching seed. In particular, of the 34 topics judged for the Query Understanding track, our method had coverage 62% of the time (21 topics). When the method has coverage, the suggested key phrases are above the mean performance (by nearly every measure reported) 2/3 times and the best performer 1/3 times. Given it's simplicity and availability to nearly all participants as well as the fact that coverage can be detected before submission, it is a promsing candidate for future investigation in the track. We now describe the method and results more fully before summarizing.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BennettW15.bib) "
	```
	@inproceedings{DBLP:conf/trec/BennettW15,
		author = {Paul N. Bennett and Ryen W. White},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Mining Tasks from the Web Anchor Text Graph: {MSR} Notebook Paper for the {TREC} 2015 Tasks Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/MSRTasks-T.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BennettW15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2015: Tasks and Total Recall Tracks

_Matthias Hagen, Steve Göring, Magdalena Keil, Olaoluwa Anifowose, Amir Othman, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [Webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/Webis-TTR.pdf](http://trec.nist.gov/pubs/trec24/papers/Webis-TTR.pdf)
- :material-file-search: **Runs:** [webis1](./runs.md#webis1) | [webisC1](./runs.md#webisc1) | [webisC2](./runs.md#webisc2) | [webisC3](./runs.md#webisc3) | [webisA1](./runs.md#webisa1) | [webisA2](./runs.md#webisa2) | [webisA3](./runs.md#webisa3)

??? abstract "Abstract"
	
	In this paper we give a brief overview of the Webis group's participation in the TREC 2015 Tasks and Total Recall tracks. In the task understanding subtask of the Tasks track, we use dierent data sources (AOL query log, Freebase, etc.) and APIs (Google, Bing, etc.) to retrieve topics related to a given query. All sources are combined in our SQuare system. The task completion subtask is based on combining the results of our ChatNoir 2 for the dierent topics identified in the task understanding subtask. Finally, for the ad-hoc subtask (similar to the previous years' Web tracks), we use an axiomatic re-ranking approach of the search results obtained from ChatNoir 2. In the Total Recall track, we employ a simple SVM baseline with variable batch sizes equipped with a keyqueries step to identify potentially relevant documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenGKAOS15.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenGKAOS15,
		author = {Matthias Hagen and Steve G{\"{o}}ring and Magdalena Keil and Olaoluwa Anifowose and Amir Othman and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2015: Tasks and Total Recall Tracks},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/Webis-TTR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenGKAOS15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

