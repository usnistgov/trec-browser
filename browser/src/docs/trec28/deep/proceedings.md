# Proceedings - Deep Learning 2019 

#### ICTNET at TREC 2019 Deep Learning Track

_Jiangui Chen, Yinqiong Cai, Haoquan Jiang_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ICTNET.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/ICTNET.DL.pdf)
- :material-file-search: **Runs:** [ICT-CKNRM_B](./runs.md#ict-cknrm_b) | [ICT-CKNRM_B50](./runs.md#ict-cknrm_b50) | [ICT-BERT2](./runs.md#ict-bert2)

??? abstract "Abstract"
	
	We participated in the Deep Learning Track at TREC 2019. We built a ranking system which combines a search component based on BM25 and a semantic matching component using pretraining knowledge. Our best run achieves NDCG@10 of 0.6650, MAP of 0.2035.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenCJ19.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenCJ19,
		author = {Jiangui Chen and Yinqiong Cai and Haoquan Jiang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at {TREC} 2019 Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/ICTNET.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenCJ19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCAS at TREC-2019 Deep Learning Track

_Xuanang Chen, Canjia Li, Ben He, Yingfei Sun_

- :fontawesome-solid-user-group: **Participant:** [UCAS](./participants.md#ucas)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UCAS.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/UCAS.DL.pdf)
- :material-file-search: **Runs:** [ucas_runid1](./runs.md#ucas_runid1) | [ucas_runid2](./runs.md#ucas_runid2) | [ucas_runid3](./runs.md#ucas_runid3)

??? abstract "Abstract"
	
	This paper describes the experiment conducted for our participation in the TREC-2019 Deep Learning track [1]. We test the effectiveness of two pre-trained language models, BERT [2] and XLNet [3], for the re-ranking subtask of the document ranking task, with an adoption of the passage-level document ranking approach as proposed in [4]. Our preliminary results indicate that the uses of BERT and XLNet lead to comparable performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenLHS19.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenLHS19,
		author = {Xuanang Chen and Canjia Li and Ben He and Yingfei Sun},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UCAS} at {TREC-2019} Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/UCAS.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenLHS19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Evaluation of Weakly-Supervised DeepCT in the TREC 2019 Deep  Learning Track

_Zhuyun Dai, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [CMU](./participants.md#cmu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CMU.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/CMU.DL.pdf)
- :material-file-search: **Runs:** [dct_qp_bm25e](./runs.md#dct_qp_bm25e) | [dct_tp_bm25e2](./runs.md#dct_tp_bm25e2) | [dct_tp_bm25e](./runs.md#dct_tp_bm25e)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2019 Deep Learning Track document ranking task. We developed a deep learning based document term weighting approach based on our previous work of DeepCT. It used the contextualized token embeddings generated by BERT to estimate a term's importance in passages, and combines passage term weights into document-level term weights. The weighted document is stored in an ordinary inverted index and searched using a multi-field BM25, which is efficient. We tested two ways of training DeepCT: a query-based method using sparse relevant query-document pairs, and a weakly-supervised method using document title-body pairs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DaiC19.bib) "
	```
	@inproceedings{DBLP:conf/trec/DaiC19,
		author = {Zhuyun Dai and Jamie Callan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {An Evaluation of Weakly-Supervised DeepCT in the {TREC} 2019 Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/CMU.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DaiC19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TUA1 at the TREC 2019: Deep Learning Track

_Yun Gao, Xin Kang, Fuji Ren, Haitao Yu_

- :fontawesome-solid-user-group: **Participant:** [TUA1](./participants.md#tua1)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/TUA1.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/TUA1.DL.pdf)
- :material-file-search: **Runs:** [TUA1-1](./runs.md#tua1-1)

??? abstract "Abstract"
	
	This paper details our participation in the TREC 2019 Deep Learning Track task including Passage Ranking task. In the Top-1000 Re-ranking subtask of Passage Ranking task, we performed passage ranking based on the technique of Conv-KNRM and BERT. In order to get a better ranking result, we divided the task into two stages. In the first stage we use Conv-KNRM model for initial ranking, then in the second stage we combine the results with a state-of-the-art BERT re-ranker.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaoKRY19.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaoKRY19,
		author = {Yun Gao and Xin Kang and Fuji Ren and Haitao Yu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TUA1} at the {TREC} 2019: Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/TUA1.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GaoKRY19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TU Wien @ TREC Deep Learning '19 - Simple Contextualization for  Re-ranking

_Sebastian Hofstätter, Markus Zlabinger, Allan Hanbury_

- :fontawesome-solid-user-group: **Participant:** [TU-Vienna](./participants.md#tu-vienna)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/TU-Vienna.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/TU-Vienna.DL.pdf)
- :material-file-search: **Runs:** [TUW19-p2-f](./runs.md#tuw19-p2-f) | [TUW19-p2-re](./runs.md#tuw19-p2-re) | [TUW19-d1-f](./runs.md#tuw19-d1-f) | [TUW19-d1-re](./runs.md#tuw19-d1-re) | [TUW19-p1-f](./runs.md#tuw19-p1-f) | [TUW19-p1-re](./runs.md#tuw19-p1-re) | [TUW19-p3-f](./runs.md#tuw19-p3-f) | [TUW19-p3-re](./runs.md#tuw19-p3-re) | [TUW19-d2-f](./runs.md#tuw19-d2-f) | [TUW19-d2-re](./runs.md#tuw19-d2-re) | [TUW19-d3-f](./runs.md#tuw19-d3-f) | [TUW19-d3-re](./runs.md#tuw19-d3-re)

??? abstract "Abstract"
	
	The usage of neural network models puts multiple objectives in conflict with each other: Ideally we would like to create a neural model that is effective, efficient, and interpretable at the same time. However, in most instances we have to choose which property is most important to us. We used the opportunity of the TREC 2019 Deep Learning track to evaluate the effectiveness of a balanced neural re-ranking approach. We submitted results of the TK (Transformer-Kernel) model: a neural re-ranking model for ad-hoc search using an efficient contextualization mechanism. TK employs a very small number of lightweight Transformer layers to contextualize query and document word embeddings. To score individual term interactions, we use a document-length enhanced kernel-pooling, which enables users to gain insight into the model. Our best result for the passage ranking task is: 0.420 MAP, 0.671 nDCG, 0.598 P@10 (TUW19-p3 full). Our best result for the document ranking task is: 0.271 MAP, 0.465 nDCG, 0.730 P@10 (TUW19-d3 re-ranking).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HofstatterZH19.bib) "
	```
	@inproceedings{DBLP:conf/trec/HofstatterZH19,
		author = {Sebastian Hofst{\"{a}}tter and Markus Zlabinger and Allan Hanbury},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TU} Wien @ {TREC} Deep Learning '19 - Simple Contextualization for Re-ranking},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/TU-Vienna.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HofstatterZH19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CCNU_IRGroup @ TREC 2019 Deep Learning Track

_Hao Hu, Junmei Wang, Xinhui Tu, Tingting He_

- :fontawesome-solid-user-group: **Participant:** [CCNU_IRGroup](./participants.md#ccnu_irgroup)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CCNU_IRGroup.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/CCNU_IRGroup.DL.pdf)
- :material-file-search: **Runs:** [runid1](./runs.md#runid1) | [runid2](./runs.md#runid2) | [runid5](./runs.md#runid5)

??? abstract "Abstract"
	
	The deep learning track consists of two tasks: passage ranking and document ranking. The former focuses on long text retrieval, while the latter focuses on short text retrieval. Both tasks use a large human-labeled set, which is from the MS-MARCO dataset. For different emphases of the two tasks, we adopt two different BERT-based retrieval models. In Section 2 and 3, we will introduce our methods in details. In Section 4 and 5, we will discuss the experiments setting and results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuWTH19.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuWTH19,
		author = {Hao Hu and Junmei Wang and Xinhui Tu and Tingting He},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {CCNU{\_}IRGroup @ {TREC} 2019 Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/CCNU\_IRGroup.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HuWTH19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SIB Text Mining at TREC 2019 Deep Learning Track: Working Note

_Julien Knafou, Matt Jeffryes, Luc Mottin, Douglas Teodoro, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [BITEM_DL](./participants.md#bitem_dl)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/BITEM_DL.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/BITEM_DL.DL.pdf)
- :material-file-search: **Runs:** [baseline](./runs.md#baseline) | [query2doc_RNN](./runs.md#query2doc_rnn)

??? abstract "Abstract"
	
	The TREC 2019 Deep Learning task aims at studying information retrieval in a large training data regime. It includes two tasks: the document ranking task (1) and the passage ranking task (2). Both of these tasks had a full ranking (a) and reranking (b) subtasks. The SIB Text Mining group participated at the full document ranking subtask (1a). In order to retrieve pertinent documents in the 3.2 million documents corpus, our strategy was two-fold. At first, we used a BM25 model to retrieve a subset of documents relevant to a query. We also tried to improve recall by using query expansion. The second step consisted in reranking the retrieved subset using an original model, so-called query2doc. This model, which has been designed to predict if a query-document pair was a good candidate to be ranked in position #1, was trained using the training dataset provided for the task. Our baseline, which is basically a BM25 ranking performed the best and achieve a MAP of 0.2892. Results of the query2doc run clearly indicates that the query2doc model could not learn any meaningful relationship. More precisely, to explain such a failure, we hypothesize that using documents returned by our baseline model as negative items confused our model. As future steps, it will be interesting to take into account features such as the document's BM25 score as well as the number of times a document's URL is mentioned in the corpus and use them along with learning to rank algorithms.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KnafouJMTR19.bib) "
	```
	@inproceedings{DBLP:conf/trec/KnafouJMTR19,
		author = {Julien Knafou and Matt Jeffryes and Luc Mottin and Douglas Teodoro and Patrick Ruch},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{SIB} Text Mining at {TREC} 2019 Deep Learning Track: Working Note},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/BITEM\_DL.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KnafouJMTR19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUET AT TREC 2019 DEEP LEARNING TRACK

_Bhaskar Mitra, Nick Craswell_

- :fontawesome-solid-user-group: **Participant:** [Microsoft](./participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/Microsoft.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/Microsoft.DL.pdf)
- :material-file-search: **Runs:** [ms_duet](./runs.md#ms_duet) | [ms_ensemble](./runs.md#ms_ensemble) | [ms_duet_passage](./runs.md#ms_duet_passage)

??? abstract "Abstract"
	
	This report discusses three submissions based on the Duet architecture to the Deep Learning track at TREC 2019. For the document retrieval task, we adapt the Duet model to ingest a “multiple field” view of documents—we refer to the new architecture as Duet with Multiple Fields (DuetMF). A second submission combines the DuetMF model with other neural and traditional relevance estimators in a learning-to-rank framework and achieves improved performance over the DuetMF baseline. For the passage retrieval task, we submit a single run based on an ensemble of eight Duet models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MitraC19.bib) "
	```
	@inproceedings{DBLP:conf/trec/MitraC19,
		author = {Bhaskar Mitra and Nick Craswell},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{DUET} {AT} {TREC} 2019 {DEEP} {LEARNING} {TRACK}},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/Microsoft.DL.pdf},
		timestamp = {Wed, 27 Apr 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MitraC19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow Terrier Team at the TREC 2019 Deep Learning  Track

_Ting Su, Xi Wang, Craig Macdonald, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/uogTr.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/uogTr.DL.pdf)
- :material-file-search: **Runs:** [uogTrDNN6LM](./runs.md#uogtrdnn6lm) | [uogTrDSSQE5LM](./runs.md#uogtrdssqe5lm) | [uogTrDSS6pLM](./runs.md#uogtrdss6plm)

??? abstract "Abstract"
	
	For TREC 2019, we focus on combining deep learning methods with traditional information retrieval methods, by using deep learning scores as an extra feature in the re-ranking process. In particular, we explore the effectiveness of using deep learning techniques based on the state-of-the-art BERT contextual language models, as well as tak- ing into account alternative query reformulations in the re-ranking process. We submitted three official runs to the document ranking task: uogTrDNN6LM, uogTrDSS6pLM, and uogTrDSSQE5LM, where all three runs deploy a deep learning method and the LambdaMART learning-to-rank method. Our results show that uogTrDNN6LM is competitive, performing above the TREC median in terms of MAP and NDCG, yet a simple untrained DFR query expansion run was more effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SuWMO19.bib) "
	```
	@inproceedings{DBLP:conf/trec/SuWMO19,
		author = {Ting Su and Xi Wang and Craig Macdonald and Iadh Ounis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow Terrier Team at the {TREC} 2019 Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/uogTr.DL.pdf},
		timestamp = {Tue, 04 May 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SuWMO19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IDST at TREC 2019 Deep Learning Track: Deep Cascade Ranking with  Generation-based Document Expansion and Pre-trained Language Modeling

_Ming Yan, Chenliang Li, Chen Wu, Bin Bi, Wei Wang, Jiangnan Xia, Luo Si_

- :fontawesome-solid-user-group: **Participant:** [IDST](./participants.md#idst)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/IDST.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/IDST.DL.pdf)
- :material-file-search: **Runs:** [idst_bert_v1](./runs.md#idst_bert_v1) | [idst_bert_v2](./runs.md#idst_bert_v2) | [idst_bert_r1](./runs.md#idst_bert_r1) | [idst_bert_r2](./runs.md#idst_bert_r2) | [idst_bert_v3](./runs.md#idst_bert_v3) | [idst_bert_p1](./runs.md#idst_bert_p1) | [idst_bert_p2](./runs.md#idst_bert_p2) | [idst_bert_p3](./runs.md#idst_bert_p3) | [idst_bert_pr1](./runs.md#idst_bert_pr1) | [idst_bert_pr2](./runs.md#idst_bert_pr2)

??? abstract "Abstract"
	
	This paper describes our participation in the passage and document ranking tasks of TREC 2019 Deep Learning Track. We propose a two-stage cascade ranking pipeline by taking the advantages of sequence-to-sequence generation and pre-trained language modeling. Firstly, we use a simple and effective index-based method to retrieve a collection of candidate passages. To overcome the vocabulary mismatch problem, we propose a query generation method for document expansion based on the pointer-generator model, where each passage is expanded with a set of generated queries for higher recall in the retrieval of candidate passages. Then we pre-train a BERT language model with a new sentence prediction objective, and adopt a pointwise ranking strategy for re-ranking the remained candidate passages. Our cascade ranking method achieves the best results among all participants on both the passage ranking and document ranking tasks, according to the official evaluation metric NDCG@10.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YanLWBWXS19.bib) "
	```
	@inproceedings{DBLP:conf/trec/YanLWBWXS19,
		author = {Ming Yan and Chenliang Li and Chen Wu and Bin Bi and Wei Wang and Jiangnan Xia and Luo Si},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IDST} at {TREC} 2019 Deep Learning Track: Deep Cascade Ranking with Generation-based Document Expansion and Pre-trained Language Modeling},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/IDST.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YanLWBWXS19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Brown University at TREC Deep Learning 2019

_George Zerveas, Ruochen Zhang, Leila Kim, Carsten Eickhoff_

- :fontawesome-solid-user-group: **Participant:** [Brown](./participants.md#brown)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/Brown.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/Brown.DL.pdf)
- :material-file-search: **Runs:** [test1](./runs.md#test1)

??? abstract "Abstract"
	
	This paper describes Brown University's submission to the TREC 2019 Deep Learning track. We followed a 2-phase method for producing a ranking of passages for a given input query: In the the first phase, the user's query is expanded by appending 3 queries generated by a transformer model which was trained to rephrase an input query into semantically similar queries. The expanded query can exhibit greater similarity in surface form and vocabulary overlap with the passages of interest and can therefore serve as enriched input to any downstream information retrieval method. In the second phase, we use a BERT-based model pre-trained for language modeling but fine-tuned for query - document relevance prediction to compute relevance scores for a set of 1000 candidate passages per query and subsequently obtain a ranking of passages by sorting them based on the predicted relevance scores.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZerveasZKE19.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZerveasZKE19,
		author = {George Zerveas and Ruochen Zhang and Leila Kim and Carsten Eickhoff},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Brown University at {TREC} Deep Learning 2019},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/Brown.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZerveasZKE19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Higway BERT for Passage Ranking

_Di Zhao, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/udel_fang.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/udel_fang.DL.pdf)
- :material-file-search: **Runs:** [runid3](./runs.md#runid3) | [runid4](./runs.md#runid4)

??? abstract "Abstract"
	
	This is the first year of TREC for deep learning and there are two tasks which are document ranking and passage ranking. Our task is passage ranking which can be described as given a query q and the 1000 most relevant passages p1, p2, ..., p1000 retrieved by BM25, passage ranking task expects to come up with a successful system to rank the most relevant passage as high as possible. In this work, we build a neural network based IR model for the passage rank- ing tasks. Basically we are trying to combine BERT [2] and highway network [6] to get a good performance on the task. Since BERT is the current SOTA model on several nlp related tasks and highway network [6] is kind of neural network with gate structure, since gate structure has already shown its success on some neural network models like lstm [3] and gru [1] on sequence modeling tasks. So we assume combining multi-head attention based transformer with gate based network structure to improve the model performance can be achieved. Meanwhile we also try different loss functions and different training strategies also with axiomatic thinking [5] approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoF19.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoF19,
		author = {Di Zhao and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Higway {BERT} for Passage Ranking},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/udel\_fang.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoF19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```
