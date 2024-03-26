# Proceedings - LiveQA 2016 

#### Overview of the TREC 2016 LiveQA Track

_Eugene Agichtein, David Carmel, Dan Pelleg, Yuval Pinter, Donna Harman_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec25/papers/Overview-QA.pdf](https://trec.nist.gov/pubs/trec25/papers/Overview-QA.pdf)
??? abstract "Abstract"
	
	The LiveQA track, now in its second year, is focused on real-time question answering for real-user questions. During the test period, real user questions are drawn from those newly submitted on a popular community question answering site, Yahoo Answers (YA), that have not yet been answered. These questions are sent to the participating systems, who provide an answer in real time. Returned answers are judged by the NIST assessors on a 4-level Likert scale. The most challenging aspects of this task are that the questions can be on any one of many popular topics, are informally stated, and are often complex and at least partly subjective. Furthermore, the participant systems must return an answer in under 60 seconds, which places additional, and realistic, constraints on the kind of processing that a system can do. In addition to the main real-time question answering task, this year we introduced a pilot task aimed at identifying the question intent. As human questions submitted on forums and CQA sites are verbose in nature and contain many redundant or unnecessary terms, participants were challenged to identify the signi cant parts of the question. The main theme of the question is marked by the systems by specifying a list of spans that capture its main intent. This automatic 'summary' of the question was evaluated by measuring its ROUGE-and METEOR-based similarity to a succinct rephrase of the question, manually provided by NIST assessors.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AgichteinCPPH16.bib) "
	```
	@inproceedings{DBLP:conf/trec/AgichteinCPPH16,
		author = {Eugene Agichtein and David Carmel and Dan Pelleg and Yuval Pinter and Donna Harman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2016 LiveQA Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {https://trec.nist.gov/pubs/trec25/papers/Overview-QA.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AgichteinCPPH16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ECNU at 2016 LiveQA Track: A Parameter Sharing Long Short Term  Memory Model for Learning Question Similarity

_Weijie An, Mengfei Shi, Xin Ouyang, Yan Yang, Qinmin Hu, Liang He_

- :fontawesome-solid-user-group: **Participant:** [ECNU](./participants.md#ecnu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/ECNU-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/ECNU-QA.pdf)
- :material-file-search: **Runs:** [ECNU](./runs.md#ecnu)

??? abstract "Abstract"
	
	In this paper, we present our system which is evaluated in the TREC 2016 LiveQA Challenge. Same as the last year, the TREC 2016 LiveQA track focuses on “live” question answering for the real-user questions from Yahoo! Answer. In this year, we first apply a parameter sharing Long Short Term Memory(LSTM) network to learn a high embedding of question representation. Then we combine the question representation with the key words information to strengthen the representation of semantic-similar questions, followed by calculating the question similarity with a simple metric function. Our approach outperforms the average score of all submitted runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnSOYHH16.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnSOYHH16,
		author = {Weijie An and Mengfei Shi and Xin Ouyang and Yan Yang and Qinmin Hu and Liang He},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ECNU} at 2016 LiveQA Track: {A} Parameter Sharing Long Short Term Memory Model for Learning Question Similarity},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/ECNU-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnSOYHH16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Texas Rio Grande Valley TREC LiveQA 2016: Using Topic  Modeling to Answer Complex Questions

_Josue Balandrano Coronel_

- :fontawesome-solid-user-group: **Participant:** [JBC-TREC2016](./participants.md#jbc-trec2016)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/JBC-TREC2016-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/JBC-TREC2016-QA.pdf)
- :material-file-search: **Runs:** [UTRGV](./runs.md#utrgv)

??? abstract "Abstract"
	
	This paper describes the system submitted to the TREC 2016 LiveQA track. This year, the TREC 2016 LiveQA track consists of implementing a web service to answer user-submitted questions. The newest unanswered question from Yahoo! Answers will be posted to the web service, a question every minute for 24 hours. The implementation described in this paper uses natural language processing (NLP) to extract keywords from the question given as input. A web search together with a Yahoo! Answer search is used to select candidate answers. A latent dirichlet allocation (LDA) model is trained in order to compute a topic distribution of the different candidate answers. Finally, the Jensen-Shannon distance is used as similarity measure between the candidate answers and the question given as input. This implementation performed better than the average scores.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Coronel16.bib) "
	```
	@inproceedings{DBLP:conf/trec/Coronel16,
		author = {Josue Balandrano Coronel},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Texas Rio Grande Valley {TREC} LiveQA 2016: Using Topic Modeling to Answer Complex Questions},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/JBC-TREC2016-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Coronel16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Open Domain Real-Time Question Answering Based on Semantic and Syntactic  Question Similarity

_Vivek V. Datla, Sadid A. Hasan, Joey Liu, Yassine Benajiba, Kathy Lee, Ashequl Qadir, Aaditya Prakash, Oladimeji Farri_

- :fontawesome-solid-user-group: **Participant:** [prna](./participants.md#prna)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/prna-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/prna-QA.pdf)
- :material-file-search: **Runs:** [prna](./runs.md#prna)

??? abstract "Abstract"
	
	In this paper, we describe our system and results of our participation in the Live-QA track of the Text Retrieval Conference(TREC) 2016. The Live-QA task involves real user questions, extracted from the stream of most recent questions submitted to the Yahoo Answers (YA) site, which have not yet been answered by humans. These questions are pushed to the participants via a socket connection, and the systems are needed to provide an answer which is less than 1000 characters length in less than 60 seconds. The answers given by the system are evaluated by human experts in terms of accuracy, readability, and preciseness. Our strategy for answering the questions include question decomposition, question relatedness identification, and answer generation. Evaluation results demonstrate that our system performed close to the average scores in question answering task. In the question focus generation task our system ranked fourth.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DatlaHLBLQPF16.bib) "
	```
	@inproceedings{DBLP:conf/trec/DatlaHLBLQPF16,
		author = {Vivek V. Datla and Sadid A. Hasan and Joey Liu and Yassine Benajiba and Kathy Lee and Ashequl Qadir and Aaditya Prakash and Oladimeji Farri},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Open Domain Real-Time Question Answering Based on Semantic and Syntactic Question Similarity},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/prna-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DatlaHLBLQPF16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2016: LiveQA Track

_Youjun E, Weitong Chen, Zhen Yang_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/BJUT-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/BJUT-QA.pdf)

??? abstract "Abstract"
	
	The paper presents the BJUT's liveQA system participating the TREC 2016. The Trec LiveQA track continues to use the last year's instruction, requiring that the system is able to answer the questions which had not been solved in one minutes based on Yahoo! Answers. Our work: (1) The key words are abstracted from the questions, so that more relevant questions will be returned. (2) The system searches in a larger scope on Yahoo! Answers to find the most accurate answers. (3) The answers should be detect whether they are more suitable for answering the given questions. The experiment results are presented at the end of the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ECY16.bib) "
	```
	@inproceedings{DBLP:conf/trec/ECY16,
		author = {Youjun E and Weitong Chen and Zhen Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2016: LiveQA Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/BJUT-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ECY16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT at the TREC 2016 LiveQA Track

_Joel M. Mackenzie, Ruey-Cheng Chen, J. Shane Culpepper_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/RMIT-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/RMIT-QA.pdf)
- :material-file-search: **Runs:** [RMIT-11](./runs.md#rmit-11) | [RMIT-12](./runs.md#rmit-12) | [RMIT-1](./runs.md#rmit-1) | [RMIT-2](./runs.md#rmit-2)

??? abstract "Abstract"
	
	This paper describes the four systems RMIT fielded for the TREC 2016 LiveQA task and the associated experiments. Similar to last year, the results show that simple solutions tend to work best, and that our improved baseline systems achieved an above-average performance. We use a commercial search engine as a first stage retrieval mechanism and compare it with our internal system which uses a carefully curated document collection. Somewhat surprisingly, we found that on average the small curated collection performed better within our current framework, warranting further studies on when and when not to use an external resource, such as a publicly available search engine API. Finally, we show that small improvements to performance can substantially reduce failure rates.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MackenzieCC16.bib) "
	```
	@inproceedings{DBLP:conf/trec/MackenzieCC16,
		author = {Joel M. Mackenzie and Ruey{-}Cheng Chen and J. Shane Culpepper},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{RMIT} at the {TREC} 2016 LiveQA Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/RMIT-QA.pdf},
		timestamp = {Mon, 26 Apr 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MackenzieCC16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Real, Live, and Concise: Answering Open-Domain Questions with Word  Embedding and Summarization

_Rana Malhas, Marwan Torki, Rahma Ali, Tamer Elsayed, Evi Yulianti_

- :fontawesome-solid-user-group: **Participant:** [QU](./participants.md#qu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/QU-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/QU-QA.pdf)
- :material-file-search: **Runs:** [QU](./runs.md#qu) | [QU2](./runs.md#qu2) | [QU3](./runs.md#qu3)

??? abstract "Abstract"
	
	Resorting to community question answering (CQA) websites for finding answers has gained momentum in the recent years with the explosive rate at which social media has been proliferating. With many questions left unanswered on those websites, automatic question answering (QA) systems have seen light. A main objective of those systems is to harness the plethora of existing answered questions; hence transforming the problem to finding good answers to newly-posed questions from similar previously-answered ones or composing a new concise one from those potential answers. In this paper, we describe the real-time Question Answering system we have developed to participate in TREC 2016 LiveQA track. Our QA system is composed of three phases: answer retrieval from three different Web sources (Yahoo! Answers, Google Search, and Bing Search), answer ranking using learning to rank models, and summarization of top ranked answers. Official track results of our three submitted runs show that our runs significantly outperformed the average scores of all participated runs across the entire spectrum of official evaluation measures deployed by the track organizers this year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MalhasTAEY16.bib) "
	```
	@inproceedings{DBLP:conf/trec/MalhasTAEY16,
		author = {Rana Malhas and Marwan Torki and Rahma Ali and Tamer Elsayed and Evi Yulianti},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Real, Live, and Concise: Answering Open-Domain Questions with Word Embedding and Summarization},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/QU-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MalhasTAEY16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Emory University at TREC LiveQA 2016: Combining Crowdsourcing and  Learning-To-Rank Approaches for Real-Time Complex Question Answering

_Denis Savenkov, Eugene Agichtein_

- :fontawesome-solid-user-group: **Participant:** [EmoryIrLab](./participants.md#emoryirlab)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/EmoryIrLab-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/EmoryIrLab-QA.pdf)
- :material-file-search: **Runs:** [EmoryCrowd](./runs.md#emorycrowd) | [OutOfmEmory](./runs.md#outofmemory)

??? abstract "Abstract"
	
	This paper describes the two QA systems we developed to participate in the TREC LiveQA 2016 shared task. The first run represents an improvement of our fully automatic real-time QA system from LiveQA 2015, Emory-QA. The second run, Emory-CRQA, which stands for Crowd-powered Real-time Question Answering, incorporates human feedback, in real-time, to improve answer candidate generation and ranking. The base Emory-QA system uses the title and the body of a question to query Yahoo! Answers, Answers.com, WikiHow and general web search and retrieve a set of candidate answers along with their topics and contexts. This information is used to represent each candidate by a set of features, rank them with a trained LambdaMART model, and return the top ranked candidates as an answer to the question. The second run, Emory-CRQA, integrates a crowdsourcing module, which provides the system with additional answer candidates and quality ratings, obtained in near real-time (under one minute) from a crowd of workers When Emory-CRQA receives a question, it is forwarded to the crowd, who can start working on the answer in parallel with the automatic pipeline. When the automatic pipeline is done generating and ranking candidates, a subset of them is immediately sent to the same workers who have been working on answering the questions. Workers then rate the quality of all human- or system-generated candidate answers. The resulting ratings, as well as original system scores, are used as features for the final re-ranking module, which returns the highest scoring answer. The official run results of the tasks indicate promising improvements for both runs compared to the best performing system from LiveQA 2015. Additionally, they demonstrate the effectiveness of the introduced crowdsourcing module, which allowed us to achieve an improvement of ∼20% in average answer score over a fully automatic Emory-QA system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SavenkovA16.bib) "
	```
	@inproceedings{DBLP:conf/trec/SavenkovA16,
		author = {Denis Savenkov and Eugene Agichtein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Emory University at {TREC} LiveQA 2016: Combining Crowdsourcing and Learning-To-Rank Approaches for Real-Time Complex Question Answering},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/EmoryIrLab-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SavenkovA16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CMU OAQA at TREC 2016 LiveQA: An Attentional Neural Encoder-Decoder  Approach for Answer Ranking

_Di Wang, Eric Nyberg_

- :fontawesome-solid-user-group: **Participant:** [CMU-OAQA](./participants.md#cmu-oaqa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/CMU-OAQA-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/CMU-OAQA-QA.pdf)
- :material-file-search: **Runs:** [CMU](./runs.md#cmu)

??? abstract "Abstract"
	
	In this paper, we present CMU's question answering system that was evaluated in the TREC 2016 LiveQA Challenge. Our overall approach this year is similar to the one used in 2015. This system answers real-user submitted questions from Yahoo! Answers website, which involves retrieving relevant web pages, extracting answer candidate texts, ranking and selecting answer candidates. The main improvement this year is the introduction of a novel answer passage ranking method based on attentional encoder-decoder recurrent neural networks (RNN). Our method uses one RNN to encode candidate answer passage into vectors, and then another RNN to decode the input question from the vectors. The perplexity of decoding the question is then used as the ranking score. In the TREC 2016 LiveQA evaluations, human assessors gave our system an average score of 1.1547 on a three-point scale and the average score was .5766 for all the 26 systems evaluated.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangN16.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangN16,
		author = {Di Wang and Eric Nyberg},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CMU} {OAQA} at {TREC} 2016 LiveQA: An Attentional Neural Encoder-Decoder Approach for Answer Ranking},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/CMU-OAQA-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangN16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### San Francisco State University at LiveQA Track of TREC 2016

_Maria Khvalchik, Anagha Kulkarni_

- :fontawesome-solid-user-group: **Participant:** [IR.SFSU.2016](./participants.md#ir.sfsu.2016)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/IR.SFSU.2016-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/IR.SFSU.2016-QA.pdf)
- :material-file-search: **Runs:** [IRSFSU](./runs.md#irsfsu)

??? abstract "Abstract"
	
	There are many situations in our everyday life where we look for answers to some questions - “Who wrote this book?”, “How to grill a fish?” or “Where is the Opera House located?”. Twenty years ago to answer these questions people were looking them up in the encyclopedias, recipe books or were asking other people. Moving the information into the electronic form and making it universally accessible helped to automate this process and save an enormous amount of time. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KhvalchikK16.bib) "
	```
	@inproceedings{DBLP:conf/trec/KhvalchikK16,
		author = {Maria Khvalchik and Anagha Kulkarni},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {San Francisco State University at LiveQA Track of {TREC} 2016},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/IR.SFSU.2016-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KhvalchikK16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

