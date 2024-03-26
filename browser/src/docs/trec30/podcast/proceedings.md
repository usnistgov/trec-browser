# Proceedings - Podcast 2021 

#### TREC 2021 Podcasts Track Overview

_Jussi Karlgren, Rosie Jones, Ben Carterette, Ann Clifton, Edgar Tanaka, Maria Eskevich, Gareth J. F. Jones, Sravana Reddy_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Overview-Pod.pdf](https://trec.nist.gov/pubs/trec30/papers/Overview-Pod.pdf)
??? abstract "Abstract"
	
	The TREC Podcasts Track is intended to facilitate research in language technologies applied to podcasts specifically by lowering the barrier-to-entry for data-oriented research for podcasts and for diverse spoken documents in general. This year, 2021, is the second year of the track. A more general overview of some of the challenges is given in last year's Podcasts Track Overview. The track this year consisted of two shared tasks: segment retrieval and summarisation, both based on a dataset of over 100,000 podcast episodes (metadata, audio, and automatic transcripts) which was released concurrently with the track. The tasks were slightly elaborated this year to encourage participants to use audio analysis. This paper gives an overview of the tasks and the results of the participants' experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KarlgrenJCCTEJR21.bib) "
	```
	@inproceedings{DBLP:conf/trec/KarlgrenJCCTEJR21,
		author = {Jussi Karlgren and Rosie Jones and Ben Carterette and Ann Clifton and Edgar Tanaka and Maria Eskevich and Gareth J. F. Jones and Sravana Reddy},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TREC} 2021 Podcasts Track Overview},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Overview-Pod.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KarlgrenJCCTEJR21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2021: Deep Learning, Health Misinformation, and Podcasts  Tracks

_Alexander Bondarenko, Maik Fröbe, Sebastian Günther, Matthias Hagen, Marcel Gohsen, Johannes Kiesel, Michael Völske, Benno Stein, Jakob Schwerter, Shahbaz Syed, Martin Potthast_

- :fontawesome-solid-user-group: **Participant:** [Webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Webis-DL-HM-Pod.pdf](https://trec.nist.gov/pubs/trec30/papers/Webis-DL-HM-Pod.pdf)
- :material-file-search: **Runs:** [Webis_pc_bs](./runs.md#webis_pc_bs) | [Webis_pc_cola](./runs.md#webis_pc_cola) | [Webis_pc_rob](./runs.md#webis_pc_rob) | [Webis_pc_co_rob](./runs.md#webis_pc_co_rob) | [Webis_pc_extr](./runs.md#webis_pc_extr) | [Webis_pc_abstr](./runs.md#webis_pc_abstr)

??? abstract "Abstract"
	
	We describe the Webis group's participation in the TREC 2021 Deep Learning, Health Misinformation, and Podcasts tracks. Our three LambdaMART-based runs submitted to the Deep Learning track focus on the question whether anchor text is an effective retrieval feature in the MS MARCO scenario. In the Health Misinformation track, we axiomatically re-ranked the top-20 results of BM25 and MonoT5 for argumentative topics. As for the Podcasts track, our submitted six runs focus on supervised classification of podcasts as entertaining, subjective, or containing discussion by using audio and text embeddings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001F0HGKV0SSP21.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001F0HGKV0SSP21,
		author = {Alexander Bondarenko and Maik Fr{\"{o}}be and Sebastian G{\"{u}}nther and Matthias Hagen and Marcel Gohsen and Johannes Kiesel and Michael V{\"{o}}lske and Benno Stein and Jakob Schwerter and Shahbaz Syed and Martin Potthast},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Webis at {TREC} 2021: Deep Learning, Health Misinformation, and Podcasts Tracks},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Webis-DL-HM-Pod.pdf},
		timestamp = {Mon, 28 Aug 2023 17:23:07 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0001F0HGKV0SSP21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TU Wien at TREC DL and Podcast 2021: Simple Compression for  Dense Retrieval

_Sebastian Hofstätter, Mete Sertkan, Allan Hanbury_

- :fontawesome-solid-user-group: **Participant:** [TU_Vienna](./participants.md#tu_vienna)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/TU_Vienna-DL-Pod.pdf](https://trec.nist.gov/pubs/trec30/papers/TU_Vienna-DL-Pod.pdf)
- :material-file-search: **Runs:** [TUW_hybrid_ws](./runs.md#tuw_hybrid_ws) | [TUW_hybrid_cat](./runs.md#tuw_hybrid_cat) | [TUW_tasb_cat](./runs.md#tuw_tasb_cat) | [TUW_tasb192_ann](./runs.md#tuw_tasb192_ann)

??? abstract "Abstract"
	
	The IR group of TU Wien participated in two tracks at TREC 2021: Deep Learning and Podcast segment retrieval. We continued our focus from our previous TREC participations on efficient approaches for retrieval and re-ranking. We propose a simple training process for compressing a dense retrieval model's output. First, we train it with full capacity, and then add a compression, or dimensionality reduction, layer on top and conduct a second full training pass. At TREC 2021 we test this model in a blind evaluation and zero-shot collection transfer for both Deep Learning and Podcast tracks. For our participation at the Podcast segment retrieval track, we also employ hybrid sparse-dense retrieval. Furthermore, we utilize auxiliary information to re-rank the retrieved segments by entertainment and subjectivity signals. Our results show that our simple compression procedure with approximate nearest neighbor search achieves comparable in-domain results (minus 2 points nDCG@10 difference) to a full TAS-Balanced retriever and reasonable effectiveness in a zero-shot domain transfer (Podcast track), where we outperform BM25 by 6 points nDCG@10.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HofstatterSH21.bib) "
	```
	@inproceedings{DBLP:conf/trec/HofstatterSH21,
		author = {Sebastian Hofst{\"{a}}tter and Mete Sertkan and Allan Hanbury},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TU} Wien at {TREC} {DL} and Podcast 2021: Simple Compression for Dense Retrieval},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/TU\_Vienna-DL-Pod.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HofstatterSH21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multilingual Podcast Summarization using Longformers

_Edgar Tanaka, Ann Clifton, Md. Iftekhar Tanveer_

- :fontawesome-solid-user-group: **Participant:** [Unicamp](./participants.md#unicamp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Unicamp-Pod.pdf](https://trec.nist.gov/pubs/trec30/papers/Unicamp-Pod.pdf)
- :material-file-search: **Runs:** [Unicamp1](./runs.md#unicamp1) | [Unicamp2](./runs.md#unicamp2)

??? abstract "Abstract"
	
	Most literature on automated summarization, including podcast summarization, has been restricted to the English language. At the same time, podcasts are now an important form of media in many countries and in many languages and therefore, it is crucial that we expand the problem of podcast summarization to a wider range of languages. In this work, we explore the application of multilingual models to the task of summarizing podcasts in English and Portuguese. We compare various training scenarios including adapting a Longformer encoder, cross-lingual and cross-task transfer learning and we demonstrate that a unified model fine-tuned to multilingual data can perform on par with dedicated models that are fine-tuned monolingually. As a result, our models significantly outperform the TREC baseline based on the first minute of each episode.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TanakaCT21.bib) "
	```
	@inproceedings{DBLP:conf/trec/TanakaCT21,
		author = {Edgar Tanaka and Ann Clifton and Md. Iftekhar Tanveer},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Multilingual Podcast Summarization using Longformers},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Unicamp-Pod.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/TanakaCT21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PoliTO at TREC 2021 Podcast Summarization Track

_Lorenzo Vaiani, Moreno La Quatra, Luca Cagliero, Paolo Garza_

- :fontawesome-solid-user-group: **Participant:** [PoliTO](./participants.md#polito)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/PoliTO-Pod.pdf](https://trec.nist.gov/pubs/trec30/papers/PoliTO-Pod.pdf)
- :material-file-search: **Runs:** [PoliTO_50_32-128](./runs.md#polito_50_32-128) | [PoliTO_25_32-128](./runs.md#polito_25_32-128) | [PoliTO_100_32-128](./runs.md#polito_100_32-128) | [PoliTO_50_64-128](./runs.md#polito_50_64-128)

??? abstract "Abstract"
	
	This paper presents the approach proposed by the PoliTO team to accomplish the TREC 2021 podcast summarization task. The purpose is to extract synchronized text/audio segments that convey the most relevant podcast information. The main challenge is to consider is the multimodal nature of the data source, which comprises both textual and acoustic sequences. PoliTO presents a two-stage pipeline that (i) extracts relevant content from multimodal sources and (ii) leverages the extracted content to generate abstractive summaries by using an attention-based Deep Learning architecture. The extractive stage combines the high-dimensional encodings of both textual and audio sources to build a neural network-based regression model. The key idea is to predict the textual similarity between the selected text snippets and the podcast description by also exploiting the underlying information provided by the acoustic features. While audio summaries are obtained by concatenating selected audio samples, summaries in textual form are generated by exploiting the selected information as input of a sequence-to-sequence generative model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VaianiQCG21.bib) "
	```
	@inproceedings{DBLP:conf/trec/VaianiQCG21,
		author = {Lorenzo Vaiani and Moreno La Quatra and Luca Cagliero and Paolo Garza},
		editor = {Ian Soboroff and Angela Ellis},
		title = {PoliTO at {TREC} 2021 Podcast Summarization Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/PoliTO-Pod.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/VaianiQCG21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

