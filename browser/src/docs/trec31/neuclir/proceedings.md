# Proceedings - NeuCLIR 2022 

#### Overview of the TREC 2022 NeuCLIR Track

_Dawn J. Lawrie, Sean MacAvaney, James Mayfield, Paul McNamee, Douglas W. Oard, Luca Soldaini, Eugene Yang_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/Overview_neuclir.pdf](https://trec.nist.gov/pubs/trec31/papers/Overview_neuclir.pdf)
??? abstract "Abstract"
	
	This is the first year of the TREC Neural CLIR (NeuCLIR) track, which aims to study the impact of neural approaches to cross-language information retrieval. The main task in this year's track was ad hoc ranked retrieval of Chinese, Persian, or Russian newswire documents using queries expressed in English. Topics were developed using standard TREC processes, except that topics developed by an annotator for one language were assessed by a different annotator when evaluating that topic on a different language. There were 172 total runs submitted by twelve teams.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LawrieMMMOSY22.bib) "
	```
	@inproceedings{DBLP:conf/trec/LawrieMMMOSY22,
		author = {Dawn J. Lawrie and Sean MacAvaney and James Mayfield and Paul McNamee and Douglas W. Oard and Luca Soldaini and Eugene Yang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Overview of the {TREC} 2022 NeuCLIR Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/Overview\_neuclir.pdf},
		timestamp = {Wed, 30 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LawrieMMMOSY22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CFDA & CLIP at TREC 2022 NeuCLIR Track

_Jia-Huei Ju, Wei-Chih Chen, Heng-Ta Chang, Cheng-Wei Lin, Ming-Feng Tsai, Chuan-Ju Wang_

- :fontawesome-solid-user-group: **Participant:** [CFDA_CLIP](./participants.md#cfda_clip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/CFDA_CLIP.N.pdf](https://trec.nist.gov/pubs/trec31/papers/CFDA_CLIP.N.pdf)
- :material-file-search: **Runs:** [CFDA_CLIP_dq](./runs.md#cfda_clip_dq) | [CFDA_CLIP_rus_dq](./runs.md#cfda_clip_rus_dq) | [CFDA_CLIP_zho_L](./runs.md#cfda_clip_zho_l) | [CFDA_CLIP_fas_clf](./runs.md#cfda_clip_fas_clf) | [CFDA_CLIP_rus_clf](./runs.md#cfda_clip_rus_clf) | [CFDA_CLIP_fas_L](./runs.md#cfda_clip_fas_l) | [CFDA_CLIP_rus_L](./runs.md#cfda_clip_rus_l) | [CFDA_CLIP_zho_dq](./runs.md#cfda_clip_zho_dq) | [CFDA_CLIP_zho_clf](./runs.md#cfda_clip_zho_clf)

??? abstract "Abstract"
	
	In this notebook paper, we report our methods and submitted results for the NeuCLIR track in TREC 2022. We adopt the common multi-stage pipeline for the cross-language information retrieval task (CLIR). The pipeline includes machine translation, sparse passage retrieval, and cross-language passage re-ranking. Particularly, we fine-tune cross-language passage re-rankers with different settings of query formulation. In the empirical evaluation on the HC4 dataset, our passage re-rankers achieved better passage re-ranking effectiveness compared to the baseline multilingual re-rankers. The evaluation results of our submitted runs in NeuCLIR are also reported.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JuCCLTW22.bib) "
	```
	@inproceedings{DBLP:conf/trec/JuCCLTW22,
		author = {Jia{-}Huei Ju and Wei{-}Chih Chen and Heng{-}Ta Chang and Cheng{-}Wei Lin and Ming{-}Feng Tsai and Chuan{-}Ju Wang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{CFDA} {\&} {CLIP} at {TREC} 2022 NeuCLIR Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/CFDA\_CLIP.N.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JuCCLTW22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HNUST @ TREC 2022 NeuCLIR Track

_Ge Zhang, Qiwen Ye, Mengmeng Wang, Dong Zhou_

- :fontawesome-solid-user-group: **Participant:** [F4](./participants.md#f4)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/F4.N.pdf](https://trec.nist.gov/pubs/trec31/papers/F4.N.pdf)
- :material-file-search: **Runs:** [F4-PyTerrierPL2](./runs.md#f4-pyterrierpl2) | [F4-PyTerrierPL2-ru](./runs.md#f4-pyterrierpl2-ru) | [F4-PyTerrierPL2-zh](./runs.md#f4-pyterrierpl2-zh)

??? abstract "Abstract"
	
	With the rapid development of deep learning, neural-based cross-language information retrieval (CLIR) has attracted extensive attention from researchers. To explore the effectiveness of neural-based CLIR, large-scale efforts, and new platforms are in need. To that end, the TREC 2022 NeuCLIR track presents a cross-language information retrieval challenge. This paper describes our first participation in the TREC 2022 NeuCLIR track. We explored two approaches for CLIR: (1) the lexical-based CLIR method and (2) the neural-based CLIR method, where the lexical-based method consists of two steps of translation and retrieval, and the neural-based method introduces the DISTILDistilmBERT model, an end-to-end neural network. In our preliminary results, the lexical-based CLIR method performs better than the neural-based method.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangYWZ22.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangYWZ22,
		author = {Ge Zhang and Qiwen Ye and Mengmeng Wang and Dong Zhou},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{HNUST} @ {TREC} 2022 NeuCLIR Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/F4.N.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhangYWZ22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Extremely Fast Fine-Tuning for Cross Language Information Retrieval  via Generalized Canonical Correlation

_John M. Conroy, Neil P. Molino, Julia S. Yang_

- :fontawesome-solid-user-group: **Participant:** [IDACCS](./participants.md#idaccs)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/IDACCS.N.pdf](https://trec.nist.gov/pubs/trec31/papers/IDACCS.N.pdf)
- :material-file-search: **Runs:** [IDACCS-run1](./runs.md#idaccs-run1) | [IDACCS-run1_reranking](./runs.md#idaccs-run1_reranking) | [IDACCS-baseline_raranking](./runs.md#idaccs-baseline_raranking) | [IDACCS-baseline](./runs.md#idaccs-baseline) | [IDACCS-baseline_rus](./runs.md#idaccs-baseline_rus) | [IDACCS-baseline_rrank_rus](./runs.md#idaccs-baseline_rrank_rus) | [IDACCS-run1_rrank_rus](./runs.md#idaccs-run1_rrank_rus) | [IDACCS-run1_rus](./runs.md#idaccs-run1_rus) | [IDACCS-run1_zho](./runs.md#idaccs-run1_zho) | [IDACCS-run1_rrank_zho](./runs.md#idaccs-run1_rrank_zho) | [IDACCS-baseline_rrank_zho](./runs.md#idaccs-baseline_rrank_zho) | [IDACCS-baseline_zho](./runs.md#idaccs-baseline_zho) | [IDACCS-run2_fas](./runs.md#idaccs-run2_fas) | [IDACCS-run2_rrank_fas](./runs.md#idaccs-run2_rrank_fas) | [IDACCS-run2_rrank_rus](./runs.md#idaccs-run2_rrank_rus) | [IDACCS-run2_rus](./runs.md#idaccs-run2_rus) | [IDACCS-run2_zho](./runs.md#idaccs-run2_zho) | [IDACCS-run2_rrank_zho](./runs.md#idaccs-run2_rrank_zho)

??? abstract "Abstract"
	
	Recently, work using language agnostic transformer neural sentence embeddings show promise for a robust multilingual sentence representation. Our submission to TREC was to test how well these embeddings could be fine-tuned cheaply to perform the task of cross-lingual information retrieval. We explore the use of the MS MARCO dataset with machine translations as a model problem. We demonstrate that a single generalized canonical correlation analysis (GCCA) model trained on previous queries significantly improves the ability of sentence embeddings to find relevant passages. The dominant computational cost for training is computing dense singular value decompositions (SVDs) of matrices derived from the fine-tuning training data. (The number of SVDs used is the number of languages retrieval views and query views plus 1). This approach illustrates that GCCA methods can be used as a rapid training alternative to fine-tuning a neural net, allowing models to be fine-tuned frequently based on a user's previous queries. This model was then used to prepare submissions for the re-ranking NeuCLIR task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ConroyMY22.bib) "
	```
	@inproceedings{DBLP:conf/trec/ConroyMY22,
		author = {John M. Conroy and Neil P. Molino and Julia S. Yang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Extremely Fast Fine-Tuning for Cross Language Information Retrieval via Generalized Canonical Correlation},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/IDACCS.N.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ConroyMY22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### KASYS at the TREC 2022 NeuCLIR Track

_Kenya Abe_

- :fontawesome-solid-user-group: **Participant:** [KASYS](./participants.md#kasys)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/KASYS.N.pdf](https://trec.nist.gov/pubs/trec31/papers/KASYS.N.pdf)
- :material-file-search: **Runs:** [KASYS-run](./runs.md#kasys-run) | [KASYS-run-rus](./runs.md#kasys-run-rus) | [KASYS-run-zho](./runs.md#kasys-run-zho) | [KASYS_one_model-fas](./runs.md#kasys_one_model-fas) | [KASYS_onemodel-rerank-fas](./runs.md#kasys_onemodel-rerank-fas) | [KASYS_onemodel-rerank-rus](./runs.md#kasys_onemodel-rerank-rus) | [KASYS_one_model-rus](./runs.md#kasys_one_model-rus) | [KASYS_one_model-zho](./runs.md#kasys_one_model-zho) | [KASYS_onemodel-rerank-zho](./runs.md#kasys_onemodel-rerank-zho)

??? abstract "Abstract"
	
	This paper describes the KASYS team's participation in the TREC 2022 NeuCLIR track. Our approach is One-for-All, which employs a single multilingual pre-trained language model to retrieve documents of any languages in response to an English query. The basic architecture is the same as ColBERT and its application to CLIR, ColBERT-X, but only a single model was trained with the mixture of MS MARCO and its translated version, neuMARCO, in our approach. Through the run submission, we evaluated two variants of the One-for-All approach, namely, the end-to-end and reranking approaches. As the first-stage retriever, the former uses approximated nearest neighbor search proposed in ColBERT, while the latter uses the track organizers' (top 1,000 documents in the baseline run were used as the results of the first-stage retrieval). To evaluate our runs, we used the results provided by the track organizers as a baseline (document translation). The official evaluation results showed that the reranking approaches outperforms the baseline in all the languages. On the other hand, the end-to-end approach achieved higher scores than the baseline only in Russian. In addition to the submissions to the TREC 2022 NeuCLIR track, we also conducted experiments with the development data called HC4. The results in HC4 also showed a similar trend: the reranking approach was superior to the end-to-end approach in Persian and Russian. We also found the discrepancy that even in the same language, the performance of our approaches varies depending on the datasets.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Abe22.bib) "
	```
	@inproceedings{DBLP:conf/trec/Abe22,
		author = {Kenya Abe},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{KASYS} at the {TREC} 2022 NeuCLIR Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/KASYS.N.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Abe22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Naver Labs Europe (SPLADE) @ TREC NeuCLIR 2022

_Carlos Lassance, Stéphane Clinchant_

- :fontawesome-solid-user-group: **Participant:** [NLE](./participants.md#nle)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/NLE.N.pdf](https://trec.nist.gov/pubs/trec31/papers/NLE.N.pdf)
- :material-file-search: **Runs:** [NLE_fa_mono_rr](./runs.md#nle_fa_mono_rr) | [NLE_fa_mono](./runs.md#nle_fa_mono) | [NLE_fa_adhoc](./runs.md#nle_fa_adhoc) | [NLE_fa_adhoc_rr](./runs.md#nle_fa_adhoc_rr) | [splade_farsi_ht](./runs.md#splade_farsi_ht) | [splade_farsi_mt](./runs.md#splade_farsi_mt) | [splade_farsi_dt](./runs.md#splade_farsi_dt) | [splade_russian_dt](./runs.md#splade_russian_dt) | [splade_russian_mt](./runs.md#splade_russian_mt) | [splade_russian_ht](./runs.md#splade_russian_ht) | [NLE_ru_mono_rr](./runs.md#nle_ru_mono_rr) | [NLE_ru_mono](./runs.md#nle_ru_mono) | [NLE_ru_adhoc_rr](./runs.md#nle_ru_adhoc_rr) | [NLE_ru_adhoc](./runs.md#nle_ru_adhoc)

??? abstract "Abstract"
	
	This paper describes our participation in the 2022 TREC NeuCLIR challenge. We submitted runs to two out of the three languages (Farsi and Russian), with a focus on first-stage rankers and comparing mono-lingual strategies to Adhoc ones. For monolingual runs, we start from pretraining models on the target language using MLM+FLOPS and then finetuning using the MSMARCO translated to the language either with ColBERT or SPLADE as the retrieval model. While for the Adhoc task we test both query translation (to the target language) and back-translation of the documents (to english). Initial result analysis shows that the monolingual strategy is strong, but that for the moment Adhoc achieved the best results, with back-translating documents being better than translating queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LassanceC22.bib) "
	```
	@inproceedings{DBLP:conf/trec/LassanceC22,
		author = {Carlos Lassance and St{\'{e}}phane Clinchant},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Naver Labs Europe {(SPLADE)} @ {TREC} NeuCLIR 2022},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/NLE.N.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LassanceC22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NeuralMind-UNICAMP at 2022 TREC NeuCLIR: Large Boring Rerankers  for Cross-lingual Retrieval

_Vitor Jeronymo, Roberto de Alencar Lotufo, Rodrigo Frassetto Nogueira_

- :fontawesome-solid-user-group: **Participant:** [NM.unicamp](./participants.md#nm.unicamp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/NM.unicamp.N.pdf](https://trec.nist.gov/pubs/trec31/papers/NM.unicamp.N.pdf)
- :material-file-search: **Runs:** [p1.fa.hoc](./runs.md#p1.fa.hoc) | [p1.ru.hoc](./runs.md#p1.ru.hoc) | [p1.zh.hoc](./runs.md#p1.zh.hoc) | [p2.fa.rerank](./runs.md#p2.fa.rerank) | [p2.ru.rerank](./runs.md#p2.ru.rerank) | [p2.zh.rerank](./runs.md#p2.zh.rerank) | [p3.fa.mono](./runs.md#p3.fa.mono) | [p3.ru.mono](./runs.md#p3.ru.mono) | [p3.zh.mono](./runs.md#p3.zh.mono) | [p4.fa.hoc](./runs.md#p4.fa.hoc) | [p4.ru.hoc](./runs.md#p4.ru.hoc)

??? abstract "Abstract"
	
	This paper reports on a study of cross-lingual information retrieval (CLIR) using the mT5-XXL reranker on the NeuCLIR track of TREC 2022. Perhaps the biggest contribution of this study is the finding that despite the mT5 model being fine-tuned only on query-document pairs of the same language it proved to be viable for CLIR tasks, where query-document pairs are in different languages, even in the presence of suboptimal first-stage retrieval performance. The results of the study show outstanding performance across all tasks and languages, leading to a high number of winning positions. Finally, this study provides valuable insights into the use of mT5 in CLIR tasks and highlights its potential as a viable solution.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JeronymoLN22.bib) "
	```
	@inproceedings{DBLP:conf/trec/JeronymoLN22,
		author = {Vitor Jeronymo and Roberto de Alencar Lotufo and Rodrigo Frassetto Nogueira},
		editor = {Ian Soboroff and Angela Ellis},
		title = {NeuralMind-UNICAMP at 2022 {TREC} NeuCLIR: Large Boring Rerankers for Cross-lingual Retrieval},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/NM.unicamp.N.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JeronymoLN22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Simple Yet Effective Neural Ranking and Reranking Baselines for Cross-Lingual  Information Retrieval

_Jimmy Lin, David Alfonso-Hermelo, Vitor Jeronymo, Ehsan Kamalloo, Carlos Lassance, Rodrigo Frassetto Nogueira, Odunayo Ogundepo, Mehdi Rezagholizadeh, Nandan Thakur, Jheng-Hong Yang, Xinyu Zhang_

- :fontawesome-solid-user-group: **Participant:** [h2oloo](./participants.md#h2oloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/h2oloo.N.pdf](https://trec.nist.gov/pubs/trec31/papers/h2oloo.N.pdf)
- :material-file-search: **Runs:** [zh_2t](./runs.md#zh_2t) | [zh_2tr](./runs.md#zh_2tr) | [zh_qt](./runs.md#zh_qt) | [zh_qtr](./runs.md#zh_qtr) | [zh_dt](./runs.md#zh_dt) | [zh_dtr](./runs.md#zh_dtr) | [zh_4rrf](./runs.md#zh_4rrf) | [zh_4rrfprf](./runs.md#zh_4rrfprf) | [zh_4rrf2](./runs.md#zh_4rrf2) | [ru_2t](./runs.md#ru_2t) | [ru_2tr](./runs.md#ru_2tr) | [ru_qt](./runs.md#ru_qt) | [ru_qtr](./runs.md#ru_qtr) | [ru_dt](./runs.md#ru_dt) | [ru_dtr](./runs.md#ru_dtr) | [ru_2rrf](./runs.md#ru_2rrf) | [ru_2rrfprf](./runs.md#ru_2rrfprf) | [ru_2rrf2](./runs.md#ru_2rrf2) | [fa_2t](./runs.md#fa_2t) | [fa_2tr](./runs.md#fa_2tr) | [fa_qt](./runs.md#fa_qt) | [fa_qtr](./runs.md#fa_qtr) | [fa_dt](./runs.md#fa_dt) | [fa_dtr](./runs.md#fa_dtr) | [fa_3rrf](./runs.md#fa_3rrf) | [fa_3rrfprf](./runs.md#fa_3rrfprf) | [fa_3rrf2](./runs.md#fa_3rrf2) | [fa_xdpr.xorHn-mm.EN.d.R](./runs.md#fa_xdpr.xorhn-mm.en.d.r) | [zh_xdpr.xorHn-mm.EN.d.R](./runs.md#zh_xdpr.xorhn-mm.en.d.r) | [ru_xdpr.xorHn-mm.EN.d.R](./runs.md#ru_xdpr.xorhn-mm.en.d.r) | [fa_xdpr.mm.2rrf-mtQ.all.R](./runs.md#fa_xdpr.mm.2rrf-mtq.all.r) | [zh_xdpr.mm.4rrf-mtQ.all.R](./runs.md#zh_xdpr.mm.4rrf-mtq.all.r) | [ru_xdpr.mm.2rrf-mtQ.all.R](./runs.md#ru_xdpr.mm.2rrf-mtq.all.r) | [fa_dense-rrf.prf](./runs.md#fa_dense-rrf.prf) | [zh_dense-rrf.prf](./runs.md#zh_dense-rrf.prf) | [ru_dense-rrf.prf](./runs.md#ru_dense-rrf.prf) | [fa_dense-rrf.BM25.SPLADE](./runs.md#fa_dense-rrf.bm25.splade) | [zh_dense-rrf.BM25](./runs.md#zh_dense-rrf.bm25) | [ru_dense-rrf.BM25.SPLADE](./runs.md#ru_dense-rrf.bm25.splade)

??? abstract "Abstract"
	
	The advent of multilingual language models has generated a resurgence of interest in cross-lingual information retrieval (CLIR), which is the task of searching documents in one language with queries from another. However, the rapid pace of progress has led to a confusing panoply of methods and reproducibility has lagged behind the state of the art. In this context, our work makes two important contributions: First, we provide a conceptual framework for organizing different approaches to cross-lingual retrieval using multi-stage architectures for mono-lingual retrieval as a scaffold. Second, we implement simple yet effective reproducible baselines in the Anserini and Pyserini IR toolkits for test collections from the TREC 2022 NeuCLIR Track, in Persian, Russian, and Chinese. Our efforts are built on a collaboration of the two teams that submitted the most effective runs to the TREC evaluation. These contributions provide a firm foundation for future advances.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinAJKLNORTYZ22.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinAJKLNORTYZ22,
		author = {Jimmy Lin and David Alfonso{-}Hermelo and Vitor Jeronymo and Ehsan Kamalloo and Carlos Lassance and Rodrigo Frassetto Nogueira and Odunayo Ogundepo and Mehdi Rezagholizadeh and Nandan Thakur and Jheng{-}Hong Yang and Xinyu Zhang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Simple Yet Effective Neural Ranking and Reranking Baselines for Cross-Lingual Information Retrieval},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/h2oloo.N.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LinAJKLNORTYZ22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HLTCOE at TREC 2022 NeuCLIR Track

_Eugene Yang, Dawn J. Lawrie, James Mayfield_

- :fontawesome-solid-user-group: **Participant:** [hltcoe-jhu](./participants.md#hltcoe-jhu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/hltcoe-jhu.N.pdf](https://trec.nist.gov/pubs/trec31/papers/hltcoe-jhu.N.pdf)
- :material-file-search: **Runs:** [hltcoe22tht](./runs.md#hltcoe22tht) | [coe22-mhq-zho_colxtt](./runs.md#coe22-mhq-zho_colxtt) | [coe22-mhq-rus_colxtt](./runs.md#coe22-mhq-rus_colxtt) | [coe22-mhq-fas_colxtt](./runs.md#coe22-mhq-fas_colxtt) | [coe22-tdq-fas_colxtt](./runs.md#coe22-tdq-fas_colxtt) | [coe22-tdq-rus_colxtt](./runs.md#coe22-tdq-rus_colxtt) | [coe22-tdq-zho_colxtt](./runs.md#coe22-tdq-zho_colxtt) | [coe22-tdq-fas_colxmtt](./runs.md#coe22-tdq-fas_colxmtt) | [coe22-tdq-rus_colxmtt](./runs.md#coe22-tdq-rus_colxmtt) | [coe22-tdq-zho_colxmtt](./runs.md#coe22-tdq-zho_colxmtt) | [coe22-tq-fas_colxtt](./runs.md#coe22-tq-fas_colxtt) | [coe22-tq-rus_colxtt](./runs.md#coe22-tq-rus_colxtt) | [coe22-tq-zho_colxtt](./runs.md#coe22-tq-zho_colxtt) | [coe22-tq-fas_colxmtt](./runs.md#coe22-tq-fas_colxmtt) | [coe22-tq-rus_colxmtt](./runs.md#coe22-tq-rus_colxmtt) | [coe22-tq-zho_colxmtt](./runs.md#coe22-tq-zho_colxmtt) | [coe22-man-fas](./runs.md#coe22-man-fas) | [coe22-man-rus](./runs.md#coe22-man-rus) | [coe22-man-zho](./runs.md#coe22-man-zho) | [coe22-bm25-td-dt-fas](./runs.md#coe22-bm25-td-dt-fas) | [coe22-bm25-td-dt-rus](./runs.md#coe22-bm25-td-dt-rus) | [coe22-bm25-td-dt-zho](./runs.md#coe22-bm25-td-dt-zho) | [coe22-bm25-d-dt-zho](./runs.md#coe22-bm25-d-dt-zho) | [coe22-bm25-d-dt-rus](./runs.md#coe22-bm25-d-dt-rus) | [coe22-bm25-d-dt-fas](./runs.md#coe22-bm25-d-dt-fas) | [coe22-bm25-t-dt-fas](./runs.md#coe22-bm25-t-dt-fas) | [coe22-bm25-t-dt-rus](./runs.md#coe22-bm25-t-dt-rus) | [coe22-bm25-t-dt-zho](./runs.md#coe22-bm25-t-dt-zho) | [coe22-bm25-t-ht-zho](./runs.md#coe22-bm25-t-ht-zho) | [coe22-bm25-t-ht-rus](./runs.md#coe22-bm25-t-ht-rus) | [coe22-bm25-td-ht-rus](./runs.md#coe22-bm25-td-ht-rus) | [coe22-bm25-td-ht-fas](./runs.md#coe22-bm25-td-ht-fas) | [coe22-bm25-td-ht-zho](./runs.md#coe22-bm25-td-ht-zho) | [coe22-bm25-d-ht-zho](./runs.md#coe22-bm25-d-ht-zho) | [coe22-bm25-d-ht-rus](./runs.md#coe22-bm25-d-ht-rus) | [coe22-bm25-d-ht-fas](./runs.md#coe22-bm25-d-ht-fas) | [coe22-bm25-d-mt-fas](./runs.md#coe22-bm25-d-mt-fas) | [coe22-bm25-d-mt-rus](./runs.md#coe22-bm25-d-mt-rus) | [coe22-bm25-d-mt-zho](./runs.md#coe22-bm25-d-mt-zho) | [coe22-bm25-td-mt-zho](./runs.md#coe22-bm25-td-mt-zho) | [coe22-bm25-td-mt-rus](./runs.md#coe22-bm25-td-mt-rus) | [coe22-bm25-td-mt-fas](./runs.md#coe22-bm25-td-mt-fas) | [coe22-bm25-t-mt-fas](./runs.md#coe22-bm25-t-mt-fas) | [coe22-bm25-t-mt-rus](./runs.md#coe22-bm25-t-mt-rus) | [coe22-bm25-t-mt-zho](./runs.md#coe22-bm25-t-mt-zho)

??? abstract "Abstract"
	
	The HLTCOE team applied ColBERT-X to the TREC 2022 NeuCLIR track with two training techniques - translate-train (TT) and multilingual translate-train (MTT). TT trains ColBERT-X with English queries and passages automatically translated into the document language from the MS-MARCO v1 collection. This results in three cross-language models for the track, one per language. MTT creates a single model for all three document languages by combining the translations of MS-MARCO passages in all three languages into mixed language batches. Thus the model learns about matching queries to passages simultaneously in all languages. While TT is more effective than MTT in each individual language due to its specificity, MTT still outperforms a strong baseline of BM25 with document translation. On average, MTT and TT perform 34% and 48% higher than the median in MAP with title queries, respectively.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangLM22.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangLM22,
		author = {Eugene Yang and Dawn J. Lawrie and James Mayfield},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{HLTCOE} at {TREC} 2022 NeuCLIR Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/hltcoe-jhu.N.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YangLM22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Huawei Noah's Ark Lab at TREC NeuCLIR 2022

_Ehsan Kamalloo, David Alfonso-Hermelo, Mehdi Rezagholizadeh_

- :fontawesome-solid-user-group: **Participant:** [huaweimtl](./participants.md#huaweimtl)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/huaweimtl.N.pdf](https://trec.nist.gov/pubs/trec31/papers/huaweimtl.N.pdf)
- :material-file-search: **Runs:** [fa_xdpr.ms.oht.d.R](./runs.md#fa_xdpr.ms.oht.d.r) | [zh_xdpr.ms.oht.d.R](./runs.md#zh_xdpr.ms.oht.d.r) | [ru_xdpr.ms.oht.d.R](./runs.md#ru_xdpr.ms.oht.d.r) | [huaweimtl-fa-m-hybrid1](./runs.md#huaweimtl-fa-m-hybrid1) | [huaweimtl-fa-c-hybrid2](./runs.md#huaweimtl-fa-c-hybrid2) | [huaweimtl-fa-c-hybrid3](./runs.md#huaweimtl-fa-c-hybrid3) | [huaweimtl-zh-m-hybrid1](./runs.md#huaweimtl-zh-m-hybrid1) | [huaweimtl-zh-c-hybrid2](./runs.md#huaweimtl-zh-c-hybrid2) | [huaweimtl-zh-c-hybrid3](./runs.md#huaweimtl-zh-c-hybrid3) | [huaweimtl-ru-m-hybrid1](./runs.md#huaweimtl-ru-m-hybrid1) | [huaweimtl-ru-c-hybrid2](./runs.md#huaweimtl-ru-c-hybrid2) | [huaweimtl-ru-c-hybrid3](./runs.md#huaweimtl-ru-c-hybrid3)

??? abstract "Abstract"
	
	In this paper, we describe our participation in the NeuCLIR track at TREC 2022. Our focus is to build strong ensembles of full-ranking models including dense retrievers, BM25 and learned sparse models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KamallooAR22.bib) "
	```
	@inproceedings{DBLP:conf/trec/KamallooAR22,
		author = {Ehsan Kamalloo and David Alfonso{-}Hermelo and Mehdi Rezagholizadeh},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Huawei Noah's Ark Lab at {TREC} NeuCLIR 2022},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/huaweimtl.N.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KamallooAR22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Non-Neural Baselines Experiments for CLIR at TREC 2022

_Paul McNamee_

- :fontawesome-solid-user-group: **Participant:** [jhu.mcnamee](./participants.md#jhu.mcnamee)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/jhu.mcnamee.N.pdf](https://trec.nist.gov/pubs/trec31/papers/jhu.mcnamee.N.pdf)
- :material-file-search: **Runs:** [jhumc.fa5.td.rf](./runs.md#jhumc.fa5.td.rf) | [jhumc.ru5.td.rf](./runs.md#jhumc.ru5.td.rf) | [jhumc.zh5.td.rf](./runs.md#jhumc.zh5.td.rf) | [jhumc.ru5.td.ce.rf](./runs.md#jhumc.ru5.td.ce.rf) | [jhumc.zh5.td.ce.rf](./runs.md#jhumc.zh5.td.ce.rf) | [jhumc.fa4.td.rf](./runs.md#jhumc.fa4.td.rf) | [jhumc.ru4.td.rf](./runs.md#jhumc.ru4.td.rf) | [jhumc.zh4.td.rf](./runs.md#jhumc.zh4.td.rf) | [jhumc.fawords.td.rf](./runs.md#jhumc.fawords.td.rf) | [jhumc.ruwords.td.rf](./runs.md#jhumc.ruwords.td.rf) | [jhumc.zhwords.td.rf](./runs.md#jhumc.zhwords.td.rf) | [jhumc.fa5.td.ce.rf](./runs.md#jhumc.fa5.td.ce.rf)

??? abstract "Abstract"
	
	Cross-Language Information Retrieval (CLIR) returned to TREC with the advent of the NeuCLIR track in 2022. The track provided document collections in three languages: Chinese, Farsi, and Russian, and the principal task involved ranking documents in response to English language queries. Our goal in participating in the NeuCLIR track was to provide a statistical baseline for retrieval, for which we used the HAIRCUT retrieval engine. Experiments included use of character n-gram indexing, use of pseudo-relevance feedback, and application of collection enrichment.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McNamee22.bib) "
	```
	@inproceedings{DBLP:conf/trec/McNamee22,
		author = {Paul McNamee},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Non-Neural Baselines Experiments for {CLIR} at {TREC} 2022},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/jhu.mcnamee.N.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/McNamee22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Probabilistic Structured Queries: The University of Maryland at the  TREC 2022 NeuCLIR Track

_Suraj Nair, Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [umcp](./participants.md#umcp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/umcp.N.pdf](https://trec.nist.gov/pubs/trec31/papers/umcp.N.pdf)
- :material-file-search: **Runs:** [umcp_hmm_zh](./runs.md#umcp_hmm_zh) | [umcp_hmm_fa](./runs.md#umcp_hmm_fa) | [umcp_hmm_ru](./runs.md#umcp_hmm_ru)

??? abstract "Abstract"
	
	The University of Maryland submitted three baseline runs to the Ad Hoc CLIR Task of the TREC 2022 NeuCLIR track. This paper describes three baseline systems that cross the language barrier using a well-known translation-based CLIR technique, Probabilistic Structured Queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NairO22.bib) "
	```
	@inproceedings{DBLP:conf/trec/NairO22,
		author = {Suraj Nair and Douglas W. Oard},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Probabilistic Structured Queries: The University of Maryland at the {TREC} 2022 NeuCLIR Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/umcp.N.pdf},
		timestamp = {Wed, 06 Sep 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NairO22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

