# Proceedings - LiveQA 2017 

#### Overview of the Medical Question Answering Task at TREC 2017 LiveQA

_Asma Ben Abacha, Eugene Agichtein, Yuval Pinter, Dina Demner-Fushman_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Overview-QA.pdf](https://trec.nist.gov/pubs/trec26/papers/Overview-QA.pdf)
??? abstract "Abstract"
	
	We present an overview of the medical question answering task organized at the TREC 2017 LiveQA track. The task addresses the automatic answering of consumer health questions received by the U.S. National Library of Medicine. We provided both training question-answer pairs, and test questions with reference answers1. All questions were manually annotated with the main entities (foci) and question types. The medical task received eight runs from five participating teams. Different approaches have been applied, including classical answer retrieval based on question analysis and similar question retrieval. In particular, several deep learning approaches were tested, including attentional encoder-decoder networks, long short-term memory networks and convolutional neural networks. The training datasets were both from the open domain and the medical domain. We discuss the obtained results and give some insights for future research in medical question answering.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbachaAPD17.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbachaAPD17,
		author = {Asma Ben Abacha and Eugene Agichtein and Yuval Pinter and Dina Demner{-}Fushman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the Medical Question Answering Task at {TREC} 2017 LiveQA},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/Overview-QA.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AbachaAPD17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Open domain real-time question answering based on asynchronous multiperspective  context-driven retrieval and neural paraphrasing

_Vivek V. Datla, Tilak Raj Arora, Joey Liu, Viraj Adduru, Sadid A. Hasan, Kathy Lee, Ashequl Qadir, Yuan Ling, Aaditya Prakash, Oladimeji Farri_

- :fontawesome-solid-user-group: **Participant:** [prna](./participants.md#prna)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/prna-QA.pdf](https://trec.nist.gov/pubs/trec26/papers/prna-QA.pdf)
- :material-file-search: **Runs:** [prnar1](./runs.md#prnar1) | [prnarun2](./runs.md#prnarun2) | [prnarun3](./runs.md#prnarun3)

??? abstract "Abstract"
	
	The live-QA task involves real user questions, extracted from the stream of most recent questions submitted to the Yahoo Answers (YA) site that has not yet been answered. There are two tracks in the live-QA task, general domain, and medical domain. In general domain, unanswered questions are taken from six categories of real-time yahoo question answering feed, and for the medical domain, they are taken from the consumer health questions asked in NLM forums. The answers given by the system for both general and medical tasks are evaluated by human experts looking into accuracy, readability, and preciseness. The features of our open-domain question answering include question decomposition, question focus identification, context identification, answer retrieval and summarization. The current system builds an asynchronous system which has a multi-perspective view of the question being asked by decomposing the question into multiple smaller questions and identifying answers to sub-questions and summarizing the answers. Our system performed close to the median in the live-QA task and ranked second in the medical sub-task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DatlaALAHLQLPF17.bib) "
	```
	@inproceedings{DBLP:conf/trec/DatlaALAHLQLPF17,
		author = {Vivek V. Datla and Tilak Raj Arora and Joey Liu and Viraj Adduru and Sadid A. Hasan and Kathy Lee and Ashequl Qadir and Yuan Ling and Aaditya Prakash and Oladimeji Farri},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Open domain real-time question answering based on asynchronous multiperspective context-driven retrieval and neural paraphrasing},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/prna-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DatlaALAHLQLPF17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CMU OAQA at TREC 2017 LiveQA: A Neural Dual Entailment Approach  for Question Paraphrase Identification

_Di Wang, Eric Nyberg_

- :fontawesome-solid-user-group: **Participant:** [CMU-OAQA](./participants.md#cmu-oaqa)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/CMU-OAQA-QA.pdf](https://trec.nist.gov/pubs/trec26/papers/CMU-OAQA-QA.pdf)
- :material-file-search: **Runs:** [CMUOAQA](./runs.md#cmuoaqa)

??? abstract "Abstract"
	
	In this paper, we present CMU's question answering system that was evaluated in the TREC 2017 LiveQA Challenge. Our overall approach this year is similar to the one used in 2015 and 2016. This system answers real-user submitted questions from Yahoo! Answers website and medical questions, which involves retrieving relevant web pages, extracting answer candidate texts, ranking and selecting final answer text. The main improvement this year is the introduction of our new question paraphrase identification module based on a neural dual entailment model. The model uses bidirectional recurrent neural network to encode the premise question into phrase vectors, and then align corresponding phrase vectors from the candidate question with the attention mechanism. The final similarity score is produced based on aggregated phrase-wise comparisons of both entailment directions. In the TREC 2017 LiveQA evaluations, human assessors gave our system an average score of 1.139 on a three-point scale and the median score was 0.777 for all the systems evaluated. Overall, our approach received the highest average scores among automatic systems in main tasks of 2015, 2016 and 2017, and also the highest average score in the new medical subtask of 2017.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangN17.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangN17,
		author = {Di Wang and Eric Nyberg},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CMU} {OAQA} at {TREC} 2017 LiveQA: {A} Neural Dual Entailment Approach for Question Paraphrase Identification},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/CMU-OAQA-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangN17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

