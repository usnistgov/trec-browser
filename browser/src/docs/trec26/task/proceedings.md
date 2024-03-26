# Proceedings - Tasks 2017 

#### TREC 2017 Tasks Track Overview

_Evangelos Kanoulas, Emine Yilmaz, Rishabh Mehrotra, Ben Carterette, Nick Craswell, Peter Bailey_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Overview-T.pdf](https://trec.nist.gov/pubs/trec26/papers/Overview-T.pdf)
??? abstract "Abstract"
	
	Research in Information Retrieval has traditionally focused on serving the best results for a single query, ignoring the reasons (or the task) that might have motivated the user to submit that query. Often times search engines are used to complete complex tasks; achieving these tasks with current search engines requires users to issue multiple queries. For example, booking travel to a location such as London could require the user to submit various queries such as flights to London, hotels in London, points of interest around London, etc. Standard evaluation mechanisms focus on evaluating the quality of a retrieval system in terms of the topical relevance of the results retrieved, completely ignoring the fact that user satisfaction mainly depends on the usefulness of the system in helping the user complete the actual task that led the user issue the query. The TREC Tasks Track is an attempt in devising mechanisms for evaluating quality of retrieval systems in terms of (1) how well they can understand the underlying task that led the user submit a query, and (2) how useful they are for helping users complete their tasks. A number of application areas, beyond task-based retrieval, could benefit from such an evaluation framework and the constructed test collections, including, but not limited to, digital assistants tasks, query suggestions, session-based retrieval, exploratory search, entity-based search. In this paper, we first summarize the three categories of evaluation mechanisms used in the track and briefly describe the corpus, topics, and tasks that comprise the test collection. We then give an overview of the runs submitted to the 2017 Tasks Track and present the evaluation results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KanoulasYMCCB17.bib) "
	```
	@inproceedings{DBLP:conf/trec/KanoulasYMCCB17,
		author = {Evangelos Kanoulas and Emine Yilmaz and Rishabh Mehrotra and Ben Carterette and Nick Craswell and Peter Bailey},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2017 Tasks Track Overview},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/Overview-T.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KanoulasYMCCB17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Siena's Tasks Track System

_Emily Barranca, Sharon Gower Small_

- :fontawesome-solid-user-group: **Participant:** [SienaCLTeam](./participants.md#sienaclteam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/SienaCLTeam-T.pdf](https://trec.nist.gov/pubs/trec26/papers/SienaCLTeam-T.pdf)
- :material-file-search: **Runs:** [SienaCLTeamRun1](./runs.md#sienaclteamrun1) | [SienaCLTeamRun2](./runs.md#sienaclteamrun2)

??? abstract "Abstract"
	
	This paper discusses our development of Siena's Tasks Track System (STTS) and its participation in the Tasks Track of the 2017 Text Retrieval Conference (TREC). The purpose of this track is to try to understand the underlying task a user might be trying to complete when searching a specific query. The Task Understanding portion of this task aimed to find a list of up to 100 keywords and phrases that might be related to a user's task given the example query. In the first year of our work in this track we submitted two fairly simple runs. In the first run, we used the jsoup library to run these queries through Google and processed the first five documents resulting from the search. We automatically extracted keywords and phrases that appeared commonly across the documents. In the second run we utilized Wordnet to generate new words and phrases to augment the query. These two methods, the Wordnet approach and the Google approach were submitted as two separate runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BarrancaS17.bib) "
	```
	@inproceedings{DBLP:conf/trec/BarrancaS17,
		author = {Emily Barranca and Sharon Gower Small},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Siena's Tasks Track System},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/SienaCLTeam-T.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BarrancaS17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2017: Tasks Track

_Lupu Li, Guangyuan Zhang, Zhen Yang_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./participants.md#bjut)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/BJUT-T.pdf](https://trec.nist.gov/pubs/trec26/papers/BJUT-T.pdf)
- :material-file-search: **Runs:** [BJUT_1](./runs.md#bjut_1) | [BJUT_2](./runs.md#bjut_2)

??? abstract "Abstract"
	
	We generally evaluate the quality of task based information retrieval system from two aspects: task understanding and task completion. To evaluate the quality of task understanding, we need a list of sub-tasks that provide a complete coverage of tasks for each query. Finding a way to get a list like that for every query is our target. So, this paper explored the viable approach to achieve it and analyzed experimental results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiZY17.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiZY17,
		author = {Lupu Li and Guangyuan Zhang and Zhen Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2017: Tasks Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/BJUT-T.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiZY17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

