# Proceedings - Podcast 2020 

#### TREC 2020 Podcasts Track Overview

_Rosie Jones, Ben Carterette, Ann Clifton, Jussi Karlgren, Aasish Pappu, Sravana Reddy, Yongze Yu, Maria Eskevich, Gareth J. F. Jones_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.P.pdf](https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.P.pdf)
??? abstract "Abstract"
	
	The Podcast Track is new at the Text Retrieval Conference (TREC) in 2020. The podcast track was designed to encourage research into podcasts in the information retrieval and NLP research communities. The track consisted of two shared tasks: segment retrieval and summarization, both based on a dataset of over 100,000 podcast episodes (metadata, audio, and automatic transcripts) which was released concurrently with the track. The track generated considerable interest, aracted hundreds of new registrations to TREC and fifteen teams, mostly disjoint between search and summarization, made final submissions for assessment. Deep learning was the dominant experimental approach for both search experiments and summarization. This paper gives an overview of the tasks and the results of the participants' experiments. The track will return to TREC 2021 with the same two tasks, incorporating slight modifications in response to participant feedback.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JonesCCKPRYEJ20.bib) "
	```
	@inproceedings{DBLP:conf/trec/JonesCCKPRYEJ20,
		author = {Rosie Jones and Ben Carterette and Ann Clifton and Jussi Karlgren and Aasish Pappu and Sravana Reddy and Yongze Yu and Maria Eskevich and Gareth J. F. Jones},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2020 Podcasts Track Overview},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.P.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JonesCCKPRYEJ20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combine and Re-Rank: The University of Maryland at the TREC 2020  Podcasts Track

_Petra Galuscáková, Suraj Nair, Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [UMD_IR](./participants.md#umd_ir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/UMD_IR.P.pdf](https://trec.nist.gov/pubs/trec29/papers/UMD_IR.P.pdf)
- :material-file-search: **Runs:** [UMD_IR_run1](./runs.md#umd_ir_run1) | [UMD_IR_run2](./runs.md#umd_ir_run2) | [UMD_IR_run3](./runs.md#umd_ir_run3) | [UMD_ID_run4](./runs.md#umd_id_run4) | [UMD_IR_run5](./runs.md#umd_ir_run5)

??? abstract "Abstract"
	
	The University of Maryland submitted five runs to Task 1 of the TREC 2020 podcasts track. The best results, achieved by combining seven system variants and then re-ranking with using combinations of two neural models, achieved a 27% improvement in NDCG over a simple Indri baseline in the official evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaluscakovaNONO20.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaluscakovaNONO20,
		author = {Petra Galusc{\'{a}}kov{\'{a}} and Suraj Nair and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Combine and Re-Rank: The University of Maryland at the {TREC} 2020 Podcasts Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/UMD\_IR.P.pdf},
		timestamp = {Wed, 06 Sep 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GaluscakovaNONO20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LRG at TREC 2020: Document Ranking with XLNet-Based Models

_Abheesht Sharma, Harshit Pandey_

- :fontawesome-solid-user-group: **Participant:** [LRG_REtrievers](./participants.md#lrg_retrievers)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/LRG_REtrievers.P.pdf](https://trec.nist.gov/pubs/trec29/papers/LRG_REtrievers.P.pdf)
- :material-file-search: **Runs:** [LRGREtvrs-r_1](./runs.md#lrgretvrs-r_1) | [LRGREtvrs-r_2](./runs.md#lrgretvrs-r_2) | [LRGREtvrs-r_3](./runs.md#lrgretvrs-r_3) | [LRGREtvrs-r_4](./runs.md#lrgretvrs-r_4)

??? abstract "Abstract"
	
	Establishing a good information retrieval system in popular mediums of entertainment is a quickly growing area of investigation for companies and researchers alike. We delve into the domain of information retrieval for podcasts. In Spotify's Podcast Challenge, we are given a user's query with a description to find the most relevant short segment from the given dataset having all the podcasts. Previous techniques that include solely classical Information Retrieval (IR) techniques, perform poorly when descriptive queries are presented. On the other hand, models which exclusively rely on large neural networks tend to perform better. The downside to this technique is that a considerable amount of time and computing power are required to infer the result. We experiment with two hybrid models which first filter out the best podcasts based on user's query with a classical IR technique, and then perform re-ranking on the shortlisted documents based on the detailed description using a transformer-based model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SharmaP20.bib) "
	```
	@inproceedings{DBLP:conf/trec/SharmaP20,
		author = {Abheesht Sharma and Harshit Pandey},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{LRG} at {TREC} 2020: Document Ranking with XLNet-Based Models},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/LRG\_REtrievers.P.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SharmaP20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Automatic Summarization of Open-Domain Podcast Episodes

_Kaiqiang Song, Fei Liu, Chen Li, Xiaoyang Wang, Dong Yu_

- :fontawesome-solid-user-group: **Participant:** [UCF_NLP](./participants.md#ucf_nlp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/UCF_NLP.P.pdf](https://trec.nist.gov/pubs/trec29/papers/UCF_NLP.P.pdf)
- :material-file-search: **Runs:** [UCF_NLP1](./runs.md#ucf_nlp1) | [UCF_NLP2](./runs.md#ucf_nlp2)

??? abstract "Abstract"
	
	We present implementation details of our abstractive summarizers that achieve competitive results on the Podcast Summarization task of TREC 2020. A concise textual summary that captures important information is crucial for users to decide whether to listen to the podcast. Prior work focuses primarily on learning contextualized representations. Instead, we investigate several less-studied aspects of neural abstractive summarization, including (i) the importance of selecting important segments from transcripts to serve as input to the summarizer; (ii) striking a balance between the amount and quality of training instances; (iii) the appropriate summary length and start/end points. We highlight the design considerations behind our system and offer key insights into the strengths and weaknesses of neural abstractive systems. Our results suggest that identifying important segments from transcripts to use as input to an abstractive summarizer is advantageous for summarizing long documents. Our best system achieves a quality rating of 1.559 judged by NIST evaluators—an absolute increase of 0.268 (+21%) over the creator descriptions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SongLLWY20.bib) "
	```
	@inproceedings{DBLP:conf/trec/SongLLWY20,
		author = {Kaiqiang Song and Fei Liu and Chen Li and Xiaoyang Wang and Dong Yu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Automatic Summarization of Open-Domain Podcast Episodes},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/UCF\_NLP.P.pdf},
		timestamp = {Fri, 14 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SongLLWY20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Spotify at the TREC 2020 Podcasts Track: Segment Retrieval

_Yongze Yu, Jussi Karlgren, Ann Clifton, Md. Iftekhar Tanveer, Rosie Jones, Hamed R. Bonab_

- :fontawesome-solid-user-group: **Participant:** [spotify](./participants.md#spotify)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/Spotify.P.pdf](https://trec.nist.gov/pubs/trec29/papers/Spotify.P.pdf)
- :material-file-search: **Runs:** [BERT-DESC-S](./runs.md#bert-desc-s) | [BERT-DESC-Q](./runs.md#bert-desc-q) | [BERT-DESC-TD](./runs.md#bert-desc-td) | [coarse2fine](./runs.md#coarse2fine) | [categoryaware1](./runs.md#categoryaware1) | [categoryaware2](./runs.md#categoryaware2)

??? abstract "Abstract"
	
	In this notebook paper, we present the details of baselines and experimental runs of the segment retrieval task in TREC 2020 Podcasts Track. As baselines, we implemented traditional IR methods,i.e. BM25 and QL, and the neural re-ranking BERT model pre-trained on MS MARCO passage re-ranking task. We also detail experimental runs of the re-ranking model fine-tuned on additional external data sets from (1) crowd- sourcing, (2) automatically generated questions, and (3) episode title-description pairs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YuKCTJB20.bib) "
	```
	@inproceedings{DBLP:conf/trec/YuKCTJB20,
		author = {Yongze Yu and Jussi Karlgren and Ann Clifton and Md. Iftekhar Tanveer and Rosie Jones and Hamed R. Bonab},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Spotify at the {TREC} 2020 Podcasts Track: Segment Retrieval},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/Spotify.P.pdf},
		timestamp = {Sat, 11 Dec 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YuKCTJB20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Two-Phase Approach for Abstractive Podcast Summarization

_Chujie Zheng, Harry Jiannan Wang, Kunpeng Zhang, Ling Fan_

- :fontawesome-solid-user-group: **Participant:** [udel_wang_zheng](./participants.md#udel_wang_zheng)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/udel_wang_zheng.P.pdf](https://trec.nist.gov/pubs/trec29/papers/udel_wang_zheng.P.pdf)
- :material-file-search: **Runs:** [udel_wang_zheng1](./runs.md#udel_wang_zheng1) | [udel_wang_zheng2](./runs.md#udel_wang_zheng2) | [udel_wang_zheng3](./runs.md#udel_wang_zheng3) | [udel_wang_zheng4](./runs.md#udel_wang_zheng4)

??? abstract "Abstract"
	
	Podcast summarization is different from summarization of other data formats, such as news, patents, and scientific papers in that podcasts are often longer, conversational, colloquial, and full of sponsorship and advertising information, which imposes great challenges for existing models. In this paper, we focus on abstractive podcast summarization and propose a two-phase approach: sentence selection and seq2seq learning. Specifically, we first select important sentences from the noisy long podcast transcripts. The selection is based on sentence similarity to the reference to reduce the redundancy and the associated latent topics to preserve semantics. Then the selected sentences are fed into a pre-trained encoder-decoder framework for the summary generation. Our approach achieves promising results regarding both ROUGE-based measures and human evaluations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengWZF20.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengWZF20,
		author = {Chujie Zheng and Harry Jiannan Wang and Kunpeng Zhang and Ling Fan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {A Two-Phase Approach for Abstractive Podcast Summarization},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/udel\_wang\_zheng.P.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengWZF20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Abstract Podcast Summarization using BART with Longformer Attention

_Hannes Karlbom, Ann Clifton_

- :fontawesome-solid-user-group: **Participant:** [hk_uu_podcast](./participants.md#hk_uu_podcast)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/hk_uu_podcast.P.pdf](https://trec.nist.gov/pubs/trec29/papers/hk_uu_podcast.P.pdf)
- :material-file-search: **Runs:** [hk_uu_podcast1](./runs.md#hk_uu_podcast1)

??? abstract "Abstract"
	
	In this paper, we present our model submitted to the TREC (Text REtrieval Conference) summarization part of the Podcasts track 2020 edition. The goal of this task is to summarize podcast episodes using 100k open-domain podcast transcripts. The challenge lies in the long length of the transcript documents, diverse structures of the podcast format and that neither the creator descriptions nor the transcripts are a perfect gold truth of an episode. We propose a combined model that tackles the length challenge, by using a drop in replacement of the Longformer attention mechanism in a pre-trained BART model and fine-tuning the model on the podcasts dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KarlbomC20.bib) "
	```
	@inproceedings{DBLP:conf/trec/KarlbomC20,
		author = {Hannes Karlbom and Ann Clifton},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Abstract Podcast Summarization using {BART} with Longformer Attention},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/hk\_uu\_podcast.P.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KarlbomC20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREMA-UNH at TREC 2020

_Sumanta Kashyapi, Laura Dietz_

- :fontawesome-solid-user-group: **Participant:** [TREMA-UNH](./participants.md#trema-unh)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/TREMA_UNH.P.pdf](https://trec.nist.gov/pubs/trec29/papers/TREMA_UNH.P.pdf)
- :material-file-search: **Runs:** [unhtrema1](./runs.md#unhtrema1) | [unhtrema3](./runs.md#unhtrema3) | [unhtrema2](./runs.md#unhtrema2) | [unhtrema4](./runs.md#unhtrema4)

??? abstract "Abstract"
	
	This notebook describes the submissions of team TREMA-UNH to the TREC Podcasts track. We participate in the summarization task of the track. We focus on combining extractive and generative summarization technique. The extractive model is used to detect salient parts of the input text and the generative model is used to generate summaries of only the selected segments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KashyapiD20.bib) "
	```
	@inproceedings{DBLP:conf/trec/KashyapiD20,
		author = {Sumanta Kashyapi and Laura Dietz},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREMA-UNH} at {TREC} 2020},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/TREMA\_UNH.P.pdf},
		timestamp = {Tue, 21 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KashyapiD20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CUED_SPEECH at TREC 2020 Podcast Summarisation Track

_Potsawee Manakul, Mark J. F. Gales_

- :fontawesome-solid-user-group: **Participant:** [cued_speechUniv](./participants.md#cued_speechuniv)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/cued_speech.P.pdf](https://trec.nist.gov/pubs/trec29/papers/cued_speech.P.pdf)
- :material-file-search: **Runs:** [cued_speechUniv1](./runs.md#cued_speechuniv1) | [cued_speechUniv2](./runs.md#cued_speechuniv2) | [cued_speechUniv3](./runs.md#cued_speechuniv3) | [cued_speechUniv4](./runs.md#cued_speechuniv4)

??? abstract "Abstract"
	
	In this paper, we describe our approach for the Podcast Summarisation challenge in TREC 2020. Given a podcast episode with its transcription, the goal is to generate a summary that captures the most important information in the content. Our approach consists of two steps: (1) Filtering redundant or less informative sentences in the transcription using the attention of a hierarchical model; (2) Applying a state-of-the-art text summarisation system (BART) fine-tuned on the Podcast data using a sequence-level reward function. Furthermore, we perform ensembles of three and nine models for our submission runs. We also fine-tune the BART model on the Podcast data as our baseline. The human evaluation by NIST shows that our best submission achieves 1.777 in the EGFB scale, while the score of creator-provided description is 1.291. Our system won the Spotify Podcast Summarisation Challenge in the TREC2020 Podcast Track in both human and automatic evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ManakulG20.bib) "
	```
	@inproceedings{DBLP:conf/trec/ManakulG20,
		author = {Potsawee Manakul and Mark J. F. Gales},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {CUED{\_}SPEECH at {TREC} 2020 Podcast Summarisation Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/cued\_speech.P.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ManakulG20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DCU-ADAPT at the TREC 2020 Podcasts Track

_Yasufumi Moriya, Gareth J. F. Jones_

- :fontawesome-solid-user-group: **Participant:** [DCU-ADAPT](./participants.md#dcu-adapt)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/DCU-ADAPT.P.pdf](https://trec.nist.gov/pubs/trec29/papers/DCU-ADAPT.P.pdf)
- :material-file-search: **Runs:** [run_dcu1](./runs.md#run_dcu1) | [run_dcu2](./runs.md#run_dcu2) | [run_dcu3](./runs.md#run_dcu3) | [run_dcu4](./runs.md#run_dcu4) | [run_dcu5](./runs.md#run_dcu5)

??? abstract "Abstract"
	
	We describe DCU-ADAPT's participation in the TREC 2020 Podcasts Track. We participated in the ad-hoc segment retrieval task. The goal of the task was to search for fixed-length segments from a large archive of podcasts which contain good jump-in points to relevant content for a given query topic. The challenge of retrieving relevant segments with good jump-in points at high rank is made more difficult by the presence of transcription errors in transcripts created using automatic speech recognition. We investigated three query expan- sion techniques designed overcome this issue. Our first approach was to extract nouns and named entities from the query description provided with each query and to add them to the corresponding query. Our second approach was to retrieve documents for the query using a commercial online web search en- gine and add selected words from the web documents to the query. Our final approach was to select words to expand the query using a pseudo-relevance feedback method and WordNet. Combining the above approaches for query expansion, we achieved a normalised discounted cumulative gain (nDCG) value of 0.586.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoriyaJ20.bib) "
	```
	@inproceedings{DBLP:conf/trec/MoriyaJ20,
		author = {Yasufumi Moriya and Gareth J. F. Jones},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{DCU-ADAPT} at the {TREC} 2020 Podcasts Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/DCU-ADAPT.P.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MoriyaJ20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Glasgow Representation and Information Learning Lab (GRILL) at TREC  2020 Podcasts Track

_Paul Owoicho, Jeff Dalton_

- :fontawesome-solid-user-group: **Participant:** [UoGTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/uog_msc.P.pdf](https://trec.nist.gov/pubs/trec29/papers/uog_msc.P.pdf)
- :material-file-search: **Runs:** [2306987O_abs_run1](./runs.md#2306987o_abs_run1) | [2306987O_extabs_run2](./runs.md#2306987o_extabs_run2) | [2306987O_extabs_run3](./runs.md#2306987o_extabs_run3)

??? abstract "Abstract"
	
	In this paper, we discuss our participation in the Summarization Task of the TREC 2020 Podcasts Track. Our submission consists of summaries generated by (i) an abstractive model based on fine-tuning T5 on the Spotify Podcasts Dataset, (ii) an ensemble model where the first 15 sentences from the podcast transcript are extracted and passed as input to a fine-tuned T5 model, and (iii) another ensemble model where we use a SpanBERT and K-Means pipeline to extract the 15 most important sentences from the podcast transcript and pass them as input to a fine-tuned T5 model. Official results demonstrate that out of 179 evaluated summaries, our best performing model (ii) generated 42 good-quality summaries - on par with the average across all other submissions. This provides evidence that focusing on the first part of the podcast episode is a strong baseline for podcast summarization.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Owoicho020.bib) "
	```
	@inproceedings{DBLP:conf/trec/Owoicho020,
		author = {Paul Owoicho and Jeff Dalton},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Glasgow Representation and Information Learning Lab {(GRILL)} at {TREC} 2020 Podcasts Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/uog\_msc.P.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Owoicho020.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Spotify at TREC 2020: Genre-Aware Abstractive Podcast Summarization

_Rezvaneh Rezapour, Sravana Reddy, Ann Clifton, Rosie Jones_

- :fontawesome-solid-user-group: **Participant:** [spotify](./participants.md#spotify)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/Spotify.P2.pdf](https://trec.nist.gov/pubs/trec29/papers/Spotify.P2.pdf)
- :material-file-search: **Runs:** [BERT-DESC-S](./runs.md#bert-desc-s) | [BERT-DESC-Q](./runs.md#bert-desc-q) | [BERT-DESC-TD](./runs.md#bert-desc-td) | [coarse2fine](./runs.md#coarse2fine) | [categoryaware1](./runs.md#categoryaware1) | [categoryaware2](./runs.md#categoryaware2)

??? abstract "Abstract"
	
	This paper contains the description of our submissions to the summarization task of the Pod- cast Track in TREC (the Text REtrieval Conference) 2020. The goal of this challenge was to generate short, informative summaries that contain the key information present in a podcast episode using automatically generated transcripts of the podcast audio. Since podcasts vary with respect to their genre, topic, and granularity of information, we propose two summarization models that explicitly take genre and named entities into consideration in order to generate summaries appropriate to the style of the podcasts. Our models are abstractive, and supervised using creator-provided de- scriptions as ground truth summaries. The results of the submitted summaries show that our best model achieves an aggregate quality score of 1.58 in comparison to the creator descriptions and a baseline abstractive system which both score 1.49 (an improvement of 9%) as assessed by human evaluators
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RezapourRCJ20.bib) "
	```
	@inproceedings{DBLP:conf/trec/RezapourRCJ20,
		author = {Rezvaneh Rezapour and Sravana Reddy and Ann Clifton and Rosie Jones},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Spotify at {TREC} 2020: Genre-Aware Abstractive Podcast Summarization},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/Spotify.P2.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RezapourRCJ20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

