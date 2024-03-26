# Proceedings 2022 

## NeuCLIR 

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

- :fontawesome-solid-user-group: **Participant:** [CFDA_CLIP](./neuclir/participants.md#cfda_clip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/CFDA_CLIP.N.pdf](https://trec.nist.gov/pubs/trec31/papers/CFDA_CLIP.N.pdf)
- :material-file-search: **Runs:** [CFDA_CLIP_dq](./neuclir/runs.md#cfda_clip_dq) | [CFDA_CLIP_rus_dq](./neuclir/runs.md#cfda_clip_rus_dq) | [CFDA_CLIP_zho_L](./neuclir/runs.md#cfda_clip_zho_l) | [CFDA_CLIP_fas_clf](./neuclir/runs.md#cfda_clip_fas_clf) | [CFDA_CLIP_rus_clf](./neuclir/runs.md#cfda_clip_rus_clf) | [CFDA_CLIP_fas_L](./neuclir/runs.md#cfda_clip_fas_l) | [CFDA_CLIP_rus_L](./neuclir/runs.md#cfda_clip_rus_l) | [CFDA_CLIP_zho_dq](./neuclir/runs.md#cfda_clip_zho_dq) | [CFDA_CLIP_zho_clf](./neuclir/runs.md#cfda_clip_zho_clf)

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

- :fontawesome-solid-user-group: **Participant:** [F4](./neuclir/participants.md#f4)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/F4.N.pdf](https://trec.nist.gov/pubs/trec31/papers/F4.N.pdf)
- :material-file-search: **Runs:** [F4-PyTerrierPL2](./neuclir/runs.md#f4-pyterrierpl2) | [F4-PyTerrierPL2-ru](./neuclir/runs.md#f4-pyterrierpl2-ru) | [F4-PyTerrierPL2-zh](./neuclir/runs.md#f4-pyterrierpl2-zh)

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

- :fontawesome-solid-user-group: **Participant:** [IDACCS](./neuclir/participants.md#idaccs)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/IDACCS.N.pdf](https://trec.nist.gov/pubs/trec31/papers/IDACCS.N.pdf)
- :material-file-search: **Runs:** [IDACCS-run1](./neuclir/runs.md#idaccs-run1) | [IDACCS-run1_reranking](./neuclir/runs.md#idaccs-run1_reranking) | [IDACCS-baseline_raranking](./neuclir/runs.md#idaccs-baseline_raranking) | [IDACCS-baseline](./neuclir/runs.md#idaccs-baseline) | [IDACCS-baseline_rus](./neuclir/runs.md#idaccs-baseline_rus) | [IDACCS-baseline_rrank_rus](./neuclir/runs.md#idaccs-baseline_rrank_rus) | [IDACCS-run1_rrank_rus](./neuclir/runs.md#idaccs-run1_rrank_rus) | [IDACCS-run1_rus](./neuclir/runs.md#idaccs-run1_rus) | [IDACCS-run1_zho](./neuclir/runs.md#idaccs-run1_zho) | [IDACCS-run1_rrank_zho](./neuclir/runs.md#idaccs-run1_rrank_zho) | [IDACCS-baseline_rrank_zho](./neuclir/runs.md#idaccs-baseline_rrank_zho) | [IDACCS-baseline_zho](./neuclir/runs.md#idaccs-baseline_zho) | [IDACCS-run2_fas](./neuclir/runs.md#idaccs-run2_fas) | [IDACCS-run2_rrank_fas](./neuclir/runs.md#idaccs-run2_rrank_fas) | [IDACCS-run2_rrank_rus](./neuclir/runs.md#idaccs-run2_rrank_rus) | [IDACCS-run2_rus](./neuclir/runs.md#idaccs-run2_rus) | [IDACCS-run2_zho](./neuclir/runs.md#idaccs-run2_zho) | [IDACCS-run2_rrank_zho](./neuclir/runs.md#idaccs-run2_rrank_zho)

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

- :fontawesome-solid-user-group: **Participant:** [KASYS](./neuclir/participants.md#kasys)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/KASYS.N.pdf](https://trec.nist.gov/pubs/trec31/papers/KASYS.N.pdf)
- :material-file-search: **Runs:** [KASYS-run](./neuclir/runs.md#kasys-run) | [KASYS-run-rus](./neuclir/runs.md#kasys-run-rus) | [KASYS-run-zho](./neuclir/runs.md#kasys-run-zho) | [KASYS_one_model-fas](./neuclir/runs.md#kasys_one_model-fas) | [KASYS_onemodel-rerank-fas](./neuclir/runs.md#kasys_onemodel-rerank-fas) | [KASYS_onemodel-rerank-rus](./neuclir/runs.md#kasys_onemodel-rerank-rus) | [KASYS_one_model-rus](./neuclir/runs.md#kasys_one_model-rus) | [KASYS_one_model-zho](./neuclir/runs.md#kasys_one_model-zho) | [KASYS_onemodel-rerank-zho](./neuclir/runs.md#kasys_onemodel-rerank-zho)

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

- :fontawesome-solid-user-group: **Participant:** [NLE](./neuclir/participants.md#nle)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/NLE.N.pdf](https://trec.nist.gov/pubs/trec31/papers/NLE.N.pdf)
- :material-file-search: **Runs:** [NLE_fa_mono_rr](./neuclir/runs.md#nle_fa_mono_rr) | [NLE_fa_mono](./neuclir/runs.md#nle_fa_mono) | [NLE_fa_adhoc](./neuclir/runs.md#nle_fa_adhoc) | [NLE_fa_adhoc_rr](./neuclir/runs.md#nle_fa_adhoc_rr) | [splade_farsi_ht](./neuclir/runs.md#splade_farsi_ht) | [splade_farsi_mt](./neuclir/runs.md#splade_farsi_mt) | [splade_farsi_dt](./neuclir/runs.md#splade_farsi_dt) | [splade_russian_dt](./neuclir/runs.md#splade_russian_dt) | [splade_russian_mt](./neuclir/runs.md#splade_russian_mt) | [splade_russian_ht](./neuclir/runs.md#splade_russian_ht) | [NLE_ru_mono_rr](./neuclir/runs.md#nle_ru_mono_rr) | [NLE_ru_mono](./neuclir/runs.md#nle_ru_mono) | [NLE_ru_adhoc_rr](./neuclir/runs.md#nle_ru_adhoc_rr) | [NLE_ru_adhoc](./neuclir/runs.md#nle_ru_adhoc)

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

- :fontawesome-solid-user-group: **Participant:** [NM.unicamp](./neuclir/participants.md#nm.unicamp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/NM.unicamp.N.pdf](https://trec.nist.gov/pubs/trec31/papers/NM.unicamp.N.pdf)
- :material-file-search: **Runs:** [p1.fa.hoc](./neuclir/runs.md#p1.fa.hoc) | [p1.ru.hoc](./neuclir/runs.md#p1.ru.hoc) | [p1.zh.hoc](./neuclir/runs.md#p1.zh.hoc) | [p2.fa.rerank](./neuclir/runs.md#p2.fa.rerank) | [p2.ru.rerank](./neuclir/runs.md#p2.ru.rerank) | [p2.zh.rerank](./neuclir/runs.md#p2.zh.rerank) | [p3.fa.mono](./neuclir/runs.md#p3.fa.mono) | [p3.ru.mono](./neuclir/runs.md#p3.ru.mono) | [p3.zh.mono](./neuclir/runs.md#p3.zh.mono) | [p4.fa.hoc](./neuclir/runs.md#p4.fa.hoc) | [p4.ru.hoc](./neuclir/runs.md#p4.ru.hoc)

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

- :fontawesome-solid-user-group: **Participant:** [h2oloo](./neuclir/participants.md#h2oloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/h2oloo.N.pdf](https://trec.nist.gov/pubs/trec31/papers/h2oloo.N.pdf)
- :material-file-search: **Runs:** [zh_2t](./neuclir/runs.md#zh_2t) | [zh_2tr](./neuclir/runs.md#zh_2tr) | [zh_qt](./neuclir/runs.md#zh_qt) | [zh_qtr](./neuclir/runs.md#zh_qtr) | [zh_dt](./neuclir/runs.md#zh_dt) | [zh_dtr](./neuclir/runs.md#zh_dtr) | [zh_4rrf](./neuclir/runs.md#zh_4rrf) | [zh_4rrfprf](./neuclir/runs.md#zh_4rrfprf) | [zh_4rrf2](./neuclir/runs.md#zh_4rrf2) | [ru_2t](./neuclir/runs.md#ru_2t) | [ru_2tr](./neuclir/runs.md#ru_2tr) | [ru_qt](./neuclir/runs.md#ru_qt) | [ru_qtr](./neuclir/runs.md#ru_qtr) | [ru_dt](./neuclir/runs.md#ru_dt) | [ru_dtr](./neuclir/runs.md#ru_dtr) | [ru_2rrf](./neuclir/runs.md#ru_2rrf) | [ru_2rrfprf](./neuclir/runs.md#ru_2rrfprf) | [ru_2rrf2](./neuclir/runs.md#ru_2rrf2) | [fa_2t](./neuclir/runs.md#fa_2t) | [fa_2tr](./neuclir/runs.md#fa_2tr) | [fa_qt](./neuclir/runs.md#fa_qt) | [fa_qtr](./neuclir/runs.md#fa_qtr) | [fa_dt](./neuclir/runs.md#fa_dt) | [fa_dtr](./neuclir/runs.md#fa_dtr) | [fa_3rrf](./neuclir/runs.md#fa_3rrf) | [fa_3rrfprf](./neuclir/runs.md#fa_3rrfprf) | [fa_3rrf2](./neuclir/runs.md#fa_3rrf2) | [fa_xdpr.xorHn-mm.EN.d.R](./neuclir/runs.md#fa_xdpr.xorhn-mm.en.d.r) | [zh_xdpr.xorHn-mm.EN.d.R](./neuclir/runs.md#zh_xdpr.xorhn-mm.en.d.r) | [ru_xdpr.xorHn-mm.EN.d.R](./neuclir/runs.md#ru_xdpr.xorhn-mm.en.d.r) | [fa_xdpr.mm.2rrf-mtQ.all.R](./neuclir/runs.md#fa_xdpr.mm.2rrf-mtq.all.r) | [zh_xdpr.mm.4rrf-mtQ.all.R](./neuclir/runs.md#zh_xdpr.mm.4rrf-mtq.all.r) | [ru_xdpr.mm.2rrf-mtQ.all.R](./neuclir/runs.md#ru_xdpr.mm.2rrf-mtq.all.r) | [fa_dense-rrf.prf](./neuclir/runs.md#fa_dense-rrf.prf) | [zh_dense-rrf.prf](./neuclir/runs.md#zh_dense-rrf.prf) | [ru_dense-rrf.prf](./neuclir/runs.md#ru_dense-rrf.prf) | [fa_dense-rrf.BM25.SPLADE](./neuclir/runs.md#fa_dense-rrf.bm25.splade) | [zh_dense-rrf.BM25](./neuclir/runs.md#zh_dense-rrf.bm25) | [ru_dense-rrf.BM25.SPLADE](./neuclir/runs.md#ru_dense-rrf.bm25.splade)

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

- :fontawesome-solid-user-group: **Participant:** [hltcoe-jhu](./neuclir/participants.md#hltcoe-jhu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/hltcoe-jhu.N.pdf](https://trec.nist.gov/pubs/trec31/papers/hltcoe-jhu.N.pdf)
- :material-file-search: **Runs:** [hltcoe22tht](./neuclir/runs.md#hltcoe22tht) | [coe22-mhq-zho_colxtt](./neuclir/runs.md#coe22-mhq-zho_colxtt) | [coe22-mhq-rus_colxtt](./neuclir/runs.md#coe22-mhq-rus_colxtt) | [coe22-mhq-fas_colxtt](./neuclir/runs.md#coe22-mhq-fas_colxtt) | [coe22-tdq-fas_colxtt](./neuclir/runs.md#coe22-tdq-fas_colxtt) | [coe22-tdq-rus_colxtt](./neuclir/runs.md#coe22-tdq-rus_colxtt) | [coe22-tdq-zho_colxtt](./neuclir/runs.md#coe22-tdq-zho_colxtt) | [coe22-tdq-fas_colxmtt](./neuclir/runs.md#coe22-tdq-fas_colxmtt) | [coe22-tdq-rus_colxmtt](./neuclir/runs.md#coe22-tdq-rus_colxmtt) | [coe22-tdq-zho_colxmtt](./neuclir/runs.md#coe22-tdq-zho_colxmtt) | [coe22-tq-fas_colxtt](./neuclir/runs.md#coe22-tq-fas_colxtt) | [coe22-tq-rus_colxtt](./neuclir/runs.md#coe22-tq-rus_colxtt) | [coe22-tq-zho_colxtt](./neuclir/runs.md#coe22-tq-zho_colxtt) | [coe22-tq-fas_colxmtt](./neuclir/runs.md#coe22-tq-fas_colxmtt) | [coe22-tq-rus_colxmtt](./neuclir/runs.md#coe22-tq-rus_colxmtt) | [coe22-tq-zho_colxmtt](./neuclir/runs.md#coe22-tq-zho_colxmtt) | [coe22-man-fas](./neuclir/runs.md#coe22-man-fas) | [coe22-man-rus](./neuclir/runs.md#coe22-man-rus) | [coe22-man-zho](./neuclir/runs.md#coe22-man-zho) | [coe22-bm25-td-dt-fas](./neuclir/runs.md#coe22-bm25-td-dt-fas) | [coe22-bm25-td-dt-rus](./neuclir/runs.md#coe22-bm25-td-dt-rus) | [coe22-bm25-td-dt-zho](./neuclir/runs.md#coe22-bm25-td-dt-zho) | [coe22-bm25-d-dt-zho](./neuclir/runs.md#coe22-bm25-d-dt-zho) | [coe22-bm25-d-dt-rus](./neuclir/runs.md#coe22-bm25-d-dt-rus) | [coe22-bm25-d-dt-fas](./neuclir/runs.md#coe22-bm25-d-dt-fas) | [coe22-bm25-t-dt-fas](./neuclir/runs.md#coe22-bm25-t-dt-fas) | [coe22-bm25-t-dt-rus](./neuclir/runs.md#coe22-bm25-t-dt-rus) | [coe22-bm25-t-dt-zho](./neuclir/runs.md#coe22-bm25-t-dt-zho) | [coe22-bm25-t-ht-zho](./neuclir/runs.md#coe22-bm25-t-ht-zho) | [coe22-bm25-t-ht-rus](./neuclir/runs.md#coe22-bm25-t-ht-rus) | [coe22-bm25-td-ht-rus](./neuclir/runs.md#coe22-bm25-td-ht-rus) | [coe22-bm25-td-ht-fas](./neuclir/runs.md#coe22-bm25-td-ht-fas) | [coe22-bm25-td-ht-zho](./neuclir/runs.md#coe22-bm25-td-ht-zho) | [coe22-bm25-d-ht-zho](./neuclir/runs.md#coe22-bm25-d-ht-zho) | [coe22-bm25-d-ht-rus](./neuclir/runs.md#coe22-bm25-d-ht-rus) | [coe22-bm25-d-ht-fas](./neuclir/runs.md#coe22-bm25-d-ht-fas) | [coe22-bm25-d-mt-fas](./neuclir/runs.md#coe22-bm25-d-mt-fas) | [coe22-bm25-d-mt-rus](./neuclir/runs.md#coe22-bm25-d-mt-rus) | [coe22-bm25-d-mt-zho](./neuclir/runs.md#coe22-bm25-d-mt-zho) | [coe22-bm25-td-mt-zho](./neuclir/runs.md#coe22-bm25-td-mt-zho) | [coe22-bm25-td-mt-rus](./neuclir/runs.md#coe22-bm25-td-mt-rus) | [coe22-bm25-td-mt-fas](./neuclir/runs.md#coe22-bm25-td-mt-fas) | [coe22-bm25-t-mt-fas](./neuclir/runs.md#coe22-bm25-t-mt-fas) | [coe22-bm25-t-mt-rus](./neuclir/runs.md#coe22-bm25-t-mt-rus) | [coe22-bm25-t-mt-zho](./neuclir/runs.md#coe22-bm25-t-mt-zho)

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

- :fontawesome-solid-user-group: **Participant:** [huaweimtl](./neuclir/participants.md#huaweimtl)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/huaweimtl.N.pdf](https://trec.nist.gov/pubs/trec31/papers/huaweimtl.N.pdf)
- :material-file-search: **Runs:** [fa_xdpr.ms.oht.d.R](./neuclir/runs.md#fa_xdpr.ms.oht.d.r) | [zh_xdpr.ms.oht.d.R](./neuclir/runs.md#zh_xdpr.ms.oht.d.r) | [ru_xdpr.ms.oht.d.R](./neuclir/runs.md#ru_xdpr.ms.oht.d.r) | [huaweimtl-fa-m-hybrid1](./neuclir/runs.md#huaweimtl-fa-m-hybrid1) | [huaweimtl-fa-c-hybrid2](./neuclir/runs.md#huaweimtl-fa-c-hybrid2) | [huaweimtl-fa-c-hybrid3](./neuclir/runs.md#huaweimtl-fa-c-hybrid3) | [huaweimtl-zh-m-hybrid1](./neuclir/runs.md#huaweimtl-zh-m-hybrid1) | [huaweimtl-zh-c-hybrid2](./neuclir/runs.md#huaweimtl-zh-c-hybrid2) | [huaweimtl-zh-c-hybrid3](./neuclir/runs.md#huaweimtl-zh-c-hybrid3) | [huaweimtl-ru-m-hybrid1](./neuclir/runs.md#huaweimtl-ru-m-hybrid1) | [huaweimtl-ru-c-hybrid2](./neuclir/runs.md#huaweimtl-ru-c-hybrid2) | [huaweimtl-ru-c-hybrid3](./neuclir/runs.md#huaweimtl-ru-c-hybrid3)

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

- :fontawesome-solid-user-group: **Participant:** [jhu.mcnamee](./neuclir/participants.md#jhu.mcnamee)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/jhu.mcnamee.N.pdf](https://trec.nist.gov/pubs/trec31/papers/jhu.mcnamee.N.pdf)
- :material-file-search: **Runs:** [jhumc.fa5.td.rf](./neuclir/runs.md#jhumc.fa5.td.rf) | [jhumc.ru5.td.rf](./neuclir/runs.md#jhumc.ru5.td.rf) | [jhumc.zh5.td.rf](./neuclir/runs.md#jhumc.zh5.td.rf) | [jhumc.ru5.td.ce.rf](./neuclir/runs.md#jhumc.ru5.td.ce.rf) | [jhumc.zh5.td.ce.rf](./neuclir/runs.md#jhumc.zh5.td.ce.rf) | [jhumc.fa4.td.rf](./neuclir/runs.md#jhumc.fa4.td.rf) | [jhumc.ru4.td.rf](./neuclir/runs.md#jhumc.ru4.td.rf) | [jhumc.zh4.td.rf](./neuclir/runs.md#jhumc.zh4.td.rf) | [jhumc.fawords.td.rf](./neuclir/runs.md#jhumc.fawords.td.rf) | [jhumc.ruwords.td.rf](./neuclir/runs.md#jhumc.ruwords.td.rf) | [jhumc.zhwords.td.rf](./neuclir/runs.md#jhumc.zhwords.td.rf) | [jhumc.fa5.td.ce.rf](./neuclir/runs.md#jhumc.fa5.td.ce.rf)

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

- :fontawesome-solid-user-group: **Participant:** [umcp](./neuclir/participants.md#umcp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/umcp.N.pdf](https://trec.nist.gov/pubs/trec31/papers/umcp.N.pdf)
- :material-file-search: **Runs:** [umcp_hmm_zh](./neuclir/runs.md#umcp_hmm_zh) | [umcp_hmm_fa](./neuclir/runs.md#umcp_hmm_fa) | [umcp_hmm_ru](./neuclir/runs.md#umcp_hmm_ru)

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

## Health Misinformation 

#### CiTIUS at the TREC 2022 Health Misinformation Track

_Marcos Fernández-Pichel, Manuel de Prada Corral, David E. Losada, Juan Carlos Pichel_

- :fontawesome-solid-user-group: **Participant:** [CiTIUS](./misinfo/participants.md#citius)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/CiTIUS.H.pdf](https://trec.nist.gov/pubs/trec31/papers/CiTIUS.H.pdf)
- :material-file-search: **Runs:** [citius.base](./misinfo/runs.md#citius.base) | [citius.r1](./misinfo/runs.md#citius.r1) | [citius.r2](./misinfo/runs.md#citius.r2) | [citius.r3](./misinfo/runs.md#citius.r3) | [citius.r4](./misinfo/runs.md#citius.r4) | [citius.r5](./misinfo/runs.md#citius.r5) | [citius.r6](./misinfo/runs.md#citius.r6) | [citius.gpt-3](./misinfo/runs.md#citius.gpt-3) | [citius.se](./misinfo/runs.md#citius.se) | [citius.se_gpt](./misinfo/runs.md#citius.se_gpt)

??? abstract "Abstract"
	
	The TREC Health Misinformation Track fosters the development of retrieval methods that promote credible and correct information over misinformation for health-related decision tasks. To make the procedure more realistic, an Answer Prediction challenge was added to this year's track. In these working notes, we describe our endeavours to estimate the correct response to each topic using search engine results and Transformer models. On the other hand, our adhoc retrieval solutions are based on new addons to our pipeline and the weighted fusion of signals.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Fernandez-Pichel22.bib) "
	```
	@inproceedings{DBLP:conf/trec/Fernandez-Pichel22,
		author = {Marcos Fern{\'{a}}ndez{-}Pichel and Manuel de Prada Corral and David E. Losada and Juan Carlos Pichel},
		editor = {Ian Soboroff and Angela Ellis},
		title = {CiTIUS at the {TREC} 2022 Health Misinformation Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/CiTIUS.H.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Fernandez-Pichel22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UWaterlooMDS at the TREC 2022 Health Misinformation Track

_Amir Vakili Tahami, Dake Zhang, Mark D. Smucker_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./misinfo/participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/UWaterlooMDS.H.pdf](https://trec.nist.gov/pubs/trec31/papers/UWaterlooMDS.H.pdf)
- :material-file-search: **Runs:** [WatS-MT5-MT5](./misinfo/runs.md#wats-mt5-mt5) | [WatS-Bigbird2_75-MT5](./misinfo/runs.md#wats-bigbird2_75-mt5) | [WatS-Bigbird2_75-MT5-TA2](./misinfo/runs.md#wats-bigbird2_75-mt5-ta2) | [WatS-BB75-MT5-TA](./misinfo/runs.md#wats-bb75-mt5-ta) | [WatS-manual-pred](./misinfo/runs.md#wats-manual-pred) | [WatS-BM25-Query](./misinfo/runs.md#wats-bm25-query) | [WatS-BM25-Question](./misinfo/runs.md#wats-bm25-question) | [WatS-Trust](./misinfo/runs.md#wats-trust) | [WatS-Trust-L1](./misinfo/runs.md#wats-trust-l1) | [WatS-Trust-MT5](./misinfo/runs.md#wats-trust-mt5) | [WatS-Trust-MT5-L1](./misinfo/runs.md#wats-trust-mt5-l1) | [WatS-AP-Baseline](./misinfo/runs.md#wats-ap-baseline) | [WatS-AP-Baseline-L1](./misinfo/runs.md#wats-ap-baseline-l1) | [WatS-AP-MT5](./misinfo/runs.md#wats-ap-mt5) | [WatS-AP-MT5-L1](./misinfo/runs.md#wats-ap-mt5-l1) | [WatS-Bigbird2_75-MT5-TA1](./misinfo/runs.md#wats-bigbird2_75-mt5-ta1) | [WatS-Manual](./misinfo/runs.md#wats-manual) | [WatS-AP-Manual](./misinfo/runs.md#wats-ap-manual)

??? abstract "Abstract"
	
	In this paper, we report our participation in the TREC 2022 Health Misinformation Track. With the aim to foster research on retrieval algorithms to promote correct information over misinformation for health-related queries, this year's track had two tasks: web retrieval and answer prediction. We reused our previous method with minor modifications to create our baselines. To overcome some limitations of our previous methods, we investigated a document-aware sentence-level passage extraction model based on the BigBird transformer. The upgraded pipeline with this model achieved our best automatic performance on the web retrieval task but failed to beat our baselines on the answer prediction task. Meanwhile, our manual runs still outperformed our automatic runs by great margins on both tasks, showing room for further improvements.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TahamiZS22.bib) "
	```
	@inproceedings{DBLP:conf/trec/TahamiZS22,
		author = {Amir Vakili Tahami and Dake Zhang and Mark D. Smucker},
		editor = {Ian Soboroff and Angela Ellis},
		title = {UWaterlooMDS at the {TREC} 2022 Health Misinformation Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/UWaterlooMDS.H.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/TahamiZS22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2022: Deep Learning and Health Misinformation

_Alexander Bondarenko, Maik Fröbe, Lukas Gienapp, Alexander Pugachev, Jan Heinrich Reimer, Ferdinand Schlatt, Ekaterina Artemova, Martin Potthast, Benno Stein, Pavel Braslavski, Matthias Hagen_

- :fontawesome-solid-user-group: **Participant:** [Webis](./misinfo/participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/Webis.DH.pdf](https://trec.nist.gov/pubs/trec31/papers/Webis.DH.pdf)
- :material-file-search: **Runs:** [webis-goo-lbert-abs](./misinfo/runs.md#webis-goo-lbert-abs) | [webis-nlm-lbert-abs](./misinfo/runs.md#webis-nlm-lbert-abs) | [webis-goo-lbert-title-abs](./misinfo/runs.md#webis-goo-lbert-title-abs) | [webis-goo-boolq-abs](./misinfo/runs.md#webis-goo-boolq-abs) | [webis-nlm-boolq-abs](./misinfo/runs.md#webis-nlm-boolq-abs) | [webis-longck-dis](./misinfo/runs.md#webis-longck-dis) | [webis-uniqa-dis](./misinfo/runs.md#webis-uniqa-dis) | [webis-verasent-dis](./misinfo/runs.md#webis-verasent-dis) | [webis-longck-uniqa-dis](./misinfo/runs.md#webis-longck-uniqa-dis) | [webis-longck-uniqa-ax-dis](./misinfo/runs.md#webis-longck-uniqa-ax-dis) | [webis-uniqa-ax-lin](./misinfo/runs.md#webis-uniqa-ax-lin) | [webis-uniqa-ax-pol](./misinfo/runs.md#webis-uniqa-ax-pol) | [webis-uniqa-ax-com](./misinfo/runs.md#webis-uniqa-ax-com) | [webis-longck-ax-lin](./misinfo/runs.md#webis-longck-ax-lin) | [webis-longck-ax-pol](./misinfo/runs.md#webis-longck-ax-pol) | [webis-longck-ax-com](./misinfo/runs.md#webis-longck-ax-com) | [webis-longck-uniqa-ax-pol](./misinfo/runs.md#webis-longck-uniqa-ax-pol) | [webis-longck-uniqa-ax-com](./misinfo/runs.md#webis-longck-uniqa-ax-com) | [webis-longck-uniqa-pol](./misinfo/runs.md#webis-longck-uniqa-pol) | [webis-longck-uniqa-ax-lin](./misinfo/runs.md#webis-longck-uniqa-ax-lin)

??? abstract "Abstract"
	
	We describe the Webis group's participation in the TREC 2022 Deep Learning and Health Misinformation tracks. Our runs submitted to the Deep Learning track focus on improving the pairwise retrieval model duoT5 by combining a greedy aggregation algorithm with document augmentation. In the Health Misinformation track, our submissions to the Answer Prediction task exploit pre-trained question answering and claim verification models, whose input is extended by evidence information from PubMed abstracts. For the Web Retrieval task, we explore re-ranking based on the closeness of the predicted answers for each web document in the initial ranking to the predicted “true” answer of a topic's question.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001FGPRSAP0BH22.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001FGPRSAP0BH22,
		author = {Alexander Bondarenko and Maik Fr{\"{o}}be and Lukas Gienapp and Alexander Pugachev and Jan Heinrich Reimer and Ferdinand Schlatt and Ekaterina Artemova and Martin Potthast and Benno Stein and Pavel Braslavski and Matthias Hagen},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Webis at {TREC} 2022: Deep Learning and Health Misinformation},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/Webis.DH.pdf},
		timestamp = {Tue, 29 Aug 2023 17:20:28 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0001FGPRSAP0BH22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Deep Learning 

#### Overview of the TREC 2022 Deep Learning Track

_Nick Craswell, Bhaskar Mitra, Emine Yilmaz, Daniel Campos, Jimmy Lin, Ellen M. Voorhees, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/Overview_deep.pdf](https://trec.nist.gov/pubs/trec31/papers/Overview_deep.pdf)
??? abstract "Abstract"
	
	This is the fourth year of the TREC Deep Learning track. As in previous years, we leverage the MS MARCO datasets that made hundreds of thousands of human annotated training labels available for both passage and document ranking tasks. In addition, this year we also leverage both the refreshed passage and document collections that were released last year leading to a nearly 16 times increase in the size of the passage collection and nearly four times increase in the document collection size. Unlike previous years, in 2022 we mainly focused on constructing a more complete test collection for the passage retrieval task, which has been the primary focus of the track. The document ranking task was kept as a secondary task, where document-level labels were inferred from the passage-level labels. Our analysis shows that similar to previous years, deep neural ranking models that employ large scale pretraining continued to outperform traditional retrieval methods. Due to the focusing our judging resources on passage judging, we are more confident in the quality of this year's queries and judgments, with respect to our ability to distinguish between runs and reuse the dataset in future. We also see some surprises in overall outcomes. Some top-performing runs did not do dense retrieval. Runs that did single-stage dense retrieval were not as competitive this year as they were last year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Craswell0YCLVS22.bib) "
	```
	@inproceedings{DBLP:conf/trec/Craswell0YCLVS22,
		author = {Nick Craswell and Bhaskar Mitra and Emine Yilmaz and Daniel Campos and Jimmy Lin and Ellen M. Voorhees and Ian Soboroff},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Overview of the {TREC} 2022 Deep Learning Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/Overview\_deep.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Craswell0YCLVS22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Hybrid Retrieval and Multi-stage Ranking at TREC 2022 Deep Learning  Track

_Guangwei Xu, Yanzhao Zhang, Longhui Zhang, Dingkun Long, Pengjun Xie, Ruijie Guo_

- :fontawesome-solid-user-group: **Participant:** [Ali](./deep/participants.md#ali)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/Ali.D.pdf](https://trec.nist.gov/pubs/trec31/papers/Ali.D.pdf)
- :material-file-search: **Runs:** [pass1](./deep/runs.md#pass1) | [doc1](./deep/runs.md#doc1) | [pass2](./deep/runs.md#pass2) | [pass3](./deep/runs.md#pass3) | [doc3](./deep/runs.md#doc3) | [doc2](./deep/runs.md#doc2)

??? abstract "Abstract"
	
	Large-scale text retrieval technology has been widely used in various practical business scenarios. This paper presents our systems for the TREC 2022 Deep Learning Track. We explain the hybrid text retrieval and multi-stage text ranking method adopted in our solution. The retrieval stage combined the two structures of traditional sparse retrieval and neural dense retrieval. In the ranking stage, in addition to the full interaction-based ranking model built on large pre-trained language model, we also proposes a lightweight sub-ranking module to further enhance the final text ranking performance. Evaluation results demonstrate the effectiveness of our proposed approach. Our models achieve the 1st and 4th rank on the test set of passage ranking and document ranking respectively.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuZZLXG22.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuZZLXG22,
		author = {Guangwei Xu and Yanzhao Zhang and Longhui Zhang and Dingkun Long and Pengjun Xie and Ruijie Guo},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Hybrid Retrieval and Multi-stage Ranking at {TREC} 2022 Deep Learning Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/Ali.D.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/XuZZLXG22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### M4D-MKLab/ITI-CERTH Participation in TREC Deep Learning Track 2022

_Alexandros-Michail Koufakis, Theodora Tsikrika, Stefanos Vrochidis, Ioannis Kompatsiaris_

- :fontawesome-solid-user-group: **Participant:** [CERTH_ITI_M4D](./deep/participants.md#certh_iti_m4d)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/CERTH_ITI_M4D.D.pdf](https://trec.nist.gov/pubs/trec31/papers/CERTH_ITI_M4D.D.pdf)
- :material-file-search: **Runs:** [rm3_term_filter_rerank](./deep/runs.md#rm3_term_filter_rerank) | [ceqe_custom_rerank](./deep/runs.md#ceqe_custom_rerank)

??? abstract "Abstract"
	
	Our team's (CERTH ITI M4D) participation in TREC Deep Learning Track this year focused on the use of the pretrained BERT model in Query Expansion. We submitted two runs in the document retrieval subtask; both include a final reranking step. The first run incorporates a novel pooling approach for the Contextualized Embedding Query Expansion (CEQE) methodology. The second run introduces a novel term selection mechanism that complements the RM3 query expansion method by filtering disadvantageous expansion terms. The term selection mechanism capitalizes on the BERT model by fine tuning it to predict the quality of terms as expansion terms and can be used on any query expansion technique.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KoufakisTVK22.bib) "
	```
	@inproceedings{DBLP:conf/trec/KoufakisTVK22,
		author = {Alexandros{-}Michail Koufakis and Theodora Tsikrika and Stefanos Vrochidis and Ioannis Kompatsiaris},
		editor = {Ian Soboroff and Angela Ellis},
		title = {M4D-MKLab/ITI-CERTH Participation in {TREC} Deep Learning Track 2022},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/CERTH\_ITI\_M4D.D.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KoufakisTVK22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CIP at TREC 2022 Deep Learning Track

_Jian Luo, Xinlin Peng, Xuanang Chen, Ben He, Le Sun, Yingfei Sun_

- :fontawesome-solid-user-group: **Participant:** [CIP](./deep/participants.md#cip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/CIP.D.pdf](https://trec.nist.gov/pubs/trec31/papers/CIP.D.pdf)
- :material-file-search: **Runs:** [cip_f1](./deep/runs.md#cip_f1) | [cip_f2](./deep/runs.md#cip_f2) | [cip_f3](./deep/runs.md#cip_f3) | [cip_r1](./deep/runs.md#cip_r1) | [cip_r2](./deep/runs.md#cip_r2) | [cip_r3](./deep/runs.md#cip_r3) | [cip_f1_r](./deep/runs.md#cip_f1_r) | [cip_f2_r](./deep/runs.md#cip_f2_r) | [cip_f3_r](./deep/runs.md#cip_f3_r)

??? abstract "Abstract"
	
	This paper describes the CIP participation in the TREC 2022 Deep Learning Track. We submitted runs to both full ranking and re-ranking subtasks of the passage ranking task. In the full ranking sub-task, we adopt a query noise resistant dense retrieval model RoDR. In the re-ranking subtask, we adopt localized contrastive estimation loss and hinge loss rather than pointwise cross-entropy loss for training rerankers. Besides, We utilize both the MS MARCO v1 and v2 passage datasets to generate hopefully sufficient training data, and our models are fine-tuned on these two kinds of training data one by one selectively. Additionally, we introduce docT5query to further enhance the performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuoPCH0S22.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuoPCH0S22,
		author = {Jian Luo and Xinlin Peng and Xuanang Chen and Ben He and Le Sun and Yingfei Sun},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{CIP} at {TREC} 2022 Deep Learning Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/CIP.D.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LuoPCH0S22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Efficient Document Representations for Neural Text Ranking

_David Rau, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./deep/participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/UAmsterdam.D.pdf](https://trec.nist.gov/pubs/trec31/papers/UAmsterdam.D.pdf)
- :material-file-search: **Runs:** [plm_512](./deep/runs.md#plm_512) | [plm_128](./deep/runs.md#plm_128) | [plm_64](./deep/runs.md#plm_64)

??? abstract "Abstract"
	
	This paper documents the University of Amsterdam's participation in the TREC 2022 Deep Learning Track. We investigate novel document representation approaches capturing long documents within the input token length of neural rankers, and even in a fraction of the maximum input token length. Reducing input length of the document representation leads to dramatic gains in efficiency, as the self-attention over token length is the main culprit of the high gpu memory footprint, low query latency, and small batch sizes. Our experiments result in a number of findings. First, we observe dramatic gains in efficiency of the document representation approaches mindful of what tokens matter most for the neural rankers. Second, we observe the expected trade-off between effectiveness and efficiency, but also observe that document native approaches retrieve numerous documents missed by passage based approaches. This leads to a significant underestimation of their effectiveness, but also highlights their potential to retrieve documents not considered by traditional rankers or passage based neural rankers. There is great potential to study these in future editions of the track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RauK22.bib) "
	```
	@inproceedings{DBLP:conf/trec/RauK22,
		author = {David Rau and Jaap Kamps},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Efficient Document Representations for Neural Text Ranking},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/UAmsterdam.D.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RauK22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Université Grenoble Alpes / LIG at TREC Deep Learning Track  2022

_Petra Galuscáková, Lucas Alberede, Gabriela Nicole González Sáez, Aidan Mannion, Philippe Mulhem, Georges Quénot_

- :fontawesome-solid-user-group: **Participant:** [UGA](./deep/participants.md#uga)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/UGA.D.pdf](https://trec.nist.gov/pubs/trec31/papers/UGA.D.pdf)
- :material-file-search: **Runs:** [fused_3runs](./deep/runs.md#fused_3runs) | [fused_2runs](./deep/runs.md#fused_2runs) | [hierarchical_2runs](./deep/runs.md#hierarchical_2runs) | [graph_colbert](./deep/runs.md#graph_colbert) | [hierarchcal_combination](./deep/runs.md#hierarchcal_combination) | [6systems](./deep/runs.md#6systems) | [2systems](./deep/runs.md#2systems) | [unicoil_reranked](./deep/runs.md#unicoil_reranked) | [4systems](./deep/runs.md#4systems) | [c47](./deep/runs.md#c47)

??? abstract "Abstract"
	
	This paper describes the submissions of the MRIM research Group/Laboratoire d'Informatique de Grenoble from the Universite Grenoble Alpes at the TREC Deep Learning Track 2022. We participated in both fullranking and reranking sub-tasks in the passages ranking task. We proposed several ways to combine neural and non-neural runs using reciprocal-rank based fusion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaluscakovaASMM22.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaluscakovaASMM22,
		author = {Petra Galusc{\'{a}}kov{\'{a}} and Lucas Alberede and Gabriela Nicole Gonz{\'{a}}lez S{\'{a}}ez and Aidan Mannion and Philippe Mulhem and Georges Qu{\'{e}}not},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Universit{\'{e}} Grenoble Alpes / {LIG} at {TREC} Deep Learning Track 2022},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/UGA.D.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GaluscakovaASMM22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments with Adaptive ReRanking and ColBERT-PRF: University of  Glasgow Terrier Team at TREC DL 2022

_Xiao Wang, Sean MacAvaney, Craig Macdonald, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [UoGTr](./deep/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/UoGTr.D.pdf](https://trec.nist.gov/pubs/trec31/papers/UoGTr.D.pdf)
- :material-file-search: **Runs:** [uogtr_dph](./deep/runs.md#uogtr_dph) | [uogtr_dph_bo1](./deep/runs.md#uogtr_dph_bo1) | [uogtr_s](./deep/runs.md#uogtr_s) | [uogtr_se](./deep/runs.md#uogtr_se) | [uogtr_be](./deep/runs.md#uogtr_be) | [uogtr_c](./deep/runs.md#uogtr_c) | [uogtr_be_gb](./deep/runs.md#uogtr_be_gb) | [uogtr_se_gb](./deep/runs.md#uogtr_se_gb) | [uogtr_e_gb](./deep/runs.md#uogtr_e_gb) | [uogtr_se_gt](./deep/runs.md#uogtr_se_gt) | [uogtr_t_cprf](./deep/runs.md#uogtr_t_cprf) | [uogtr_s_cprf](./deep/runs.md#uogtr_s_cprf) | [uogtr_c_cprf](./deep/runs.md#uogtr_c_cprf) | [uogtr_e_cprf_t5](./deep/runs.md#uogtr_e_cprf_t5) | [uogtr_doc_dph_bo1](./deep/runs.md#uogtr_doc_dph_bo1) | [uogtr_doc_dph](./deep/runs.md#uogtr_doc_dph)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2022 Deep Learning Track. In our participation, we applied the Adaptive ReRanking technique on the constructed corpus graph from various first-stage retrieval models, namely the BM25 and SPLADE retrieval models, before applying the reranker, namely the ELECTRA reranking model. In addition, we employed the ColBERT-PRF technique on various first stage retrieval models. Finally, we experimented with ensemble retrieval for implementing both the Adaptive ReRanking and the ColBERT-PRF techniques. We submitted 14 passage ranking runs (including six baseline runs). Among the submitted runs, the run where the Adaptive ReRanking technique is applied on the ensemble of BM25 and SPLADE retrieval, namely uogtr_e_gb, is the most effective in terms of nDCG@10.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangMMO22.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangMMO22,
		author = {Xiao Wang and Sean MacAvaney and Craig Macdonald and Iadh Ounis},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Experiments with Adaptive ReRanking and ColBERT-PRF: University of Glasgow Terrier Team at {TREC} {DL} 2022},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/UoGTr.D.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WangMMO22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2022: Deep Learning and Health Misinformation

_Alexander Bondarenko, Maik Fröbe, Lukas Gienapp, Alexander Pugachev, Jan Heinrich Reimer, Ferdinand Schlatt, Ekaterina Artemova, Martin Potthast, Benno Stein, Pavel Braslavski, Matthias Hagen_

- :fontawesome-solid-user-group: **Participant:** [Webis](./deep/participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/Webis.DH.pdf](https://trec.nist.gov/pubs/trec31/papers/Webis.DH.pdf)
- :material-file-search: **Runs:** [webis-dl-duot5](./deep/runs.md#webis-dl-duot5) | [webis-dl-duot5-g](./deep/runs.md#webis-dl-duot5-g) | [webis-dl-duot5-aug-1](./deep/runs.md#webis-dl-duot5-aug-1) | [webis-dl-duot5-aug-2](./deep/runs.md#webis-dl-duot5-aug-2)

??? abstract "Abstract"
	
	We describe the Webis group's participation in the TREC 2022 Deep Learning and Health Misinformation tracks. Our runs submitted to the Deep Learning track focus on improving the pairwise retrieval model duoT5 by combining a greedy aggregation algorithm with document augmentation. In the Health Misinformation track, our submissions to the Answer Prediction task exploit pre-trained question answering and claim verification models, whose input is extended by evidence information from PubMed abstracts. For the Web Retrieval task, we explore re-ranking based on the closeness of the predicted answers for each web document in the initial ranking to the predicted “true” answer of a topic's question.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001FGPRSAP0BH22.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001FGPRSAP0BH22,
		author = {Alexander Bondarenko and Maik Fr{\"{o}}be and Lukas Gienapp and Alexander Pugachev and Jan Heinrich Reimer and Ferdinand Schlatt and Ekaterina Artemova and Martin Potthast and Benno Stein and Pavel Braslavski and Matthias Hagen},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Webis at {TREC} 2022: Deep Learning and Health Misinformation},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/Webis.DH.pdf},
		timestamp = {Tue, 29 Aug 2023 17:20:28 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0001FGPRSAP0BH22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2022: Deep Learning Track

_Yizheng Huang, Jimmy X. Huang_

- :fontawesome-solid-user-group: **Participant:** [yorku22](./deep/participants.md#yorku22)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/yorku22.D.pdf](https://trec.nist.gov/pubs/trec31/papers/yorku22.D.pdf)
- :material-file-search: **Runs:** [yorku22b](./deep/runs.md#yorku22b) | [yorku22a](./deep/runs.md#yorku22a)

??? abstract "Abstract"
	
	The present study outlines the involvement of the YorkU group in the TREC 2022 Deep Learning Track. This year, the investigation into the fusion of BM25 and the deep learning model, which was initiated in the previous year, is pursued further. The findings from last year's experiments indicate that while the deep learning model was superior for most queries, BM25 demonstrated better performance for particular queries. In our contribution, the queries were classified: BM25 was utilized directly as the final ranking result for queries suited to it, whereas the results of the deep learning model were employed for queries incompatible with BM25. The experimental results indicate that this integrated approach yields improved results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangH22.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangH22,
		author = {Yizheng Huang and Jimmy X. Huang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {York University at {TREC} 2022: Deep Learning Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/yorku22.D.pdf},
		timestamp = {Tue, 17 Oct 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuangH22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Conversational Assistance 

#### TREC CAsT 2022: Going Beyond User Ask and System Retrieve with Initiative  and Response Generation

_Paul Owoicho, Jeff Dalton, Mohammad Aliannejadi, Leif Azzopardi, Johanne R. Trippas, Svitlana Vakulenko_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/Overview_cast.pdf](https://trec.nist.gov/pubs/trec31/papers/Overview_cast.pdf)
??? abstract "Abstract"
	
	The fourth year of the TREC Conversational Assistance Track (CAsT) continues to focus on evaluating Conversational Passage Ranking (ConvPR) for information seeking but with several new additions to improve the realism of the task and to improve our understanding of conversational search. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Owoicho0AATV22.bib) "
	```
	@inproceedings{DBLP:conf/trec/Owoicho0AATV22,
		author = {Paul Owoicho and Jeff Dalton and Mohammad Aliannejadi and Leif Azzopardi and Johanne R. Trippas and Svitlana Vakulenko},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TREC} CAsT 2022: Going Beyond User Ask and System Retrieve with Initiative and Response Generation},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/Overview\_cast.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Owoicho0AATV22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CFDA & CLIP at TREC 2022 Conversational Assistance Track  (CAsT)

_Jia-Huei Ju, Sheng-Chieh Lin, Li-Young Chang, Ming-Feng Tsai, Chuan-Ju Wang_

- :fontawesome-solid-user-group: **Participant:** [CFDA_CLIP](./cast/participants.md#cfda_clip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/CFDA_CLIP.C.pdf](https://trec.nist.gov/pubs/trec31/papers/CFDA_CLIP.C.pdf)
- :material-file-search: **Runs:** [CNC_kwqlm2_cqg](./cast/runs.md#cnc_kwqlm2_cqg) | [CNC_kwqlm_cqg](./cast/runs.md#cnc_kwqlm_cqg) | [CNC_cqg](./cast/runs.md#cnc_cqg) | [CNC_AS-C](./cast/runs.md#cnc_as-c) | [CNC_AD-C](./cast/runs.md#cnc_ad-c) | [CNC_MS-C](./cast/runs.md#cnc_ms-c) | [CNC_MD-C](./cast/runs.md#cnc_md-c) | [CNC_AD](./cast/runs.md#cnc_ad) | [CNC_AS](./cast/runs.md#cnc_as)

??? abstract "Abstract"
	
	In this notebook, we introduce a new pipeline for TREC CAsT 2022. Comparing to the common multistage pipeline for conversational search, we experimented an alternative that does not require conversational query reformulation (CQR). Specifically, our pipeline equipped with conversational dense retriever and conversational passage re-ranker. Our empirical evaluation result on TREC CAsT dataset is also reported in this paper
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JuLCTW22.bib) "
	```
	@inproceedings{DBLP:conf/trec/JuLCTW22,
		author = {Jia{-}Huei Ju and Sheng{-}Chieh Lin and Li{-}Young Chang and Ming{-}Feng Tsai and Chuan{-}Ju Wang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{CFDA} {\&} {CLIP} at {TREC} 2022 Conversational Assistance Track (CAsT)},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/CFDA\_CLIP.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JuLCTW22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Context Propagation in Conversational Search Utterances Participation  of the CNR Team in CAsT 2022

_Ida Mele, Cristina Ioana Muntean, Franco Maria Nardini, Raffaele Perego, Nicola Tonellotto_

- :fontawesome-solid-user-group: **Participant:** [CNR](./cast/participants.md#cnr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/CNR.C.pdf](https://trec.nist.gov/pubs/trec31/papers/CNR.C.pdf)
- :material-file-search: **Runs:** [CNR_run1](./cast/runs.md#cnr_run1) | [CNR_run2](./cast/runs.md#cnr_run2) | [CNR_run3](./cast/runs.md#cnr_run3) | [CNR_run4](./cast/runs.md#cnr_run4)

??? abstract "Abstract"
	
	Every year, NIST organizes the Text REtrieval Conference (TREC) which gathers competitions for forecasting research on text retrieval. Since 2019, it has included a contest on conversational assistant systems, called Conversational Assistant Track (CAsT) with the purpose of helping research on conversational information systems. CAsT provides test collections for open-domain conversational seeking where the users can ask multiple questions to the system and get answers like in a multi-turn conversation. For our participation in CAsT 2022, we implemented an architecture consisting of two steps: utterance rewriting and passage retrieval. Each run is based on a different utterance rewriting technique for enriching the raw utterance with context extracted from the previous utterances and/or from the replies in the conversation. Three of our approaches are completely automatic, while another one uses the manually rewritten utterances provided by the organizers of TREC CAsT 2022.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MeleMN0T22.bib) "
	```
	@inproceedings{DBLP:conf/trec/MeleMN0T22,
		author = {Ida Mele and Cristina Ioana Muntean and Franco Maria Nardini and Raffaele Perego and Nicola Tonellotto},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Context Propagation in Conversational Search Utterances Participation of the {CNR} Team in CAsT 2022},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/CNR.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MeleMN0T22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Cambridge at TREC Cast 2022

_Adian Liusie, Mengjie Qian, Xiang Li, Mark J. F. Gales_

- :fontawesome-solid-user-group: **Participant:** [HEATWAVE](./cast/participants.md#heatwave)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/HEATWAVE.C.pdf](https://trec.nist.gov/pubs/trec31/papers/HEATWAVE.C.pdf)
- :material-file-search: **Runs:** [monot5](./cast/runs.md#monot5) | [duo_reranker](./cast/runs.md#duo_reranker) | [gold](./cast/runs.md#gold) | [combine0.5](./cast/runs.md#combine0.5)

??? abstract "Abstract"
	
	Team heatwave (of the University of Cambridge) submitted 3 automatic runs to the TREC 2022 Conversational Assistance Track. This paper discusses our approach to the challenge of conversational informational retrieval. We first describe our four stage approach of query reformulation, BM25 retrieval, passage reranking, and response extraction. Our experiments then show that our multi-query approach, which uses the raw concatenated conversational context for BM25 and the rewritten query for reranking, shows considerable performance improvement over a single-query approach, where our best performing system achieves a NDCG@3 of 0.440 in the 2022 CAsT challenge.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiusieQLG22.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiusieQLG22,
		author = {Adian Liusie and Mengjie Qian and Xiang Li and Mark J. F. Gales},
		editor = {Ian Soboroff and Angela Ellis},
		title = {University of Cambridge at {TREC} Cast 2022},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/HEATWAVE.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LiusieQLG22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MLIA-DAC@TREC CAsT 2022: Sparse Contextualized Query Embedding

_Nam Le Hai, Thomas Gerald, Thibault Formal, Jian-Yun Nie, Benjamin Piwowarski, Laure Soulier_

- :fontawesome-solid-user-group: **Participant:** [MLIA-DAC](./cast/participants.md#mlia-dac)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/MLIA-DAC.C.pdf](https://trec.nist.gov/pubs/trec31/papers/MLIA-DAC.C.pdf)
- :material-file-search: **Runs:** [MLIA_DAC_splade](./cast/runs.md#mlia_dac_splade) | [splade_t5mse](./cast/runs.md#splade_t5mse) | [splade_t5mm_ens](./cast/runs.md#splade_t5mm_ens) | [splade_t5mm](./cast/runs.md#splade_t5mm)

??? abstract "Abstract"
	
	We extend SPLADE, a sparse information retrieval model, as our first stage ranker for the conversational task. This end-to-end approach achieves a high recall (as measure on TREC CAsT 2021). To further increase the effectiveness of our approach, we train a T5-based re-ranker. This working note fully describes our model and the four runs submitted to TREC CAsT 2022.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HaiGFNPS22.bib) "
	```
	@inproceedings{DBLP:conf/trec/HaiGFNPS22,
		author = {Nam Le Hai and Thomas Gerald and Thibault Formal and Jian{-}Yun Nie and Benjamin Piwowarski and Laure Soulier},
		editor = {Ian Soboroff and Angela Ellis},
		title = {MLIA-DAC@TREC CAsT 2022: Sparse Contextualized Query Embedding},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/MLIA-DAC.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HaiGFNPS22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Stavanger (IAI) at the TREC 2022 Conversational  Assistance Track

_Weronika Lajewska, Nolwenn Bernard, Ivica Kostric, Ivan Sekulic, Krisztian Balog_

- :fontawesome-solid-user-group: **Participant:** [UiS](./cast/participants.md#uis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/UiS.C.pdf](https://trec.nist.gov/pubs/trec31/papers/UiS.C.pdf)
- :material-file-search: **Runs:** [uis_clearboat](./cast/runs.md#uis_clearboat) | [uis_vagueboat](./cast/runs.md#uis_vagueboat) | [uis_duoboat](./cast/runs.md#uis_duoboat) | [uis_cargoboat](./cast/runs.md#uis_cargoboat) | [uis_sparseboat](./cast/runs.md#uis_sparseboat) | [uis_mixedboat](./cast/runs.md#uis_mixedboat)

??? abstract "Abstract"
	
	This paper describes the participation of the IAI group at the University of Stavanger in the TREC 2022 Conversational Assistance track. We employ an established two-stage passage ranking architecture, i.e., first-pass passage retrieval (with standard BM25 ranking and pseudo-relevance feedback) followed by re-ranking (with mono and duo T5) using a rewritten query (with a T5 model fine-tuned on the CANARD dataset). In our runs, we experiment with intent classification based on MSDialog-Intent and term expansion using beam search scores for query rewriting as well as with clarifying questions for the mixed-initiative subtask.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LajewskaBKSB22.bib) "
	```
	@inproceedings{DBLP:conf/trec/LajewskaBKSB22,
		author = {Weronika Lajewska and Nolwenn Bernard and Ivica Kostric and Ivan Sekulic and Krisztian Balog},
		editor = {Ian Soboroff and Angela Ellis},
		title = {The University of Stavanger {(IAI)} at the {TREC} 2022 Conversational Assistance Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/UiS.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LajewskaBKSB22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow Terrier Team at the TREC 2022 Conversational  Assistance Track

_Sarawoot Kongyoung, Craig Macdonald, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [UoGTr](./cast/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/UoGTr.C.pdf](https://trec.nist.gov/pubs/trec31/papers/UoGTr.C.pdf)
- :material-file-search: **Runs:** [uogTr-MI](./cast/runs.md#uogtr-mi) | [uogTr-MI-HB](./cast/runs.md#uogtr-mi-hb) | [uogTr-AT](./cast/runs.md#uogtr-at) | [uogTr-MT](./cast/runs.md#uogtr-mt)

??? abstract "Abstract"
	
	In this paper, we describe our methods and submitted runs for the TREC 2022 Conversational Assistance Track. In our participation, we leverage Multi-Task Learning (MTL) methods to enhance the performance of the conversational search system. For the main task, we use our recently proposed monoQA model, which applies Multi-Task Learning (MTL) on reranking and answer extraction by sharing a single text generation model, predicts both the answer and the reranking score simultaneously. For the mixed-initiative sub-task, we propose T5MI, which is trained on the ClariQ dataset, to determine whether a user utterance needs to ask clarifying questions, as well as to generate useful clarifying questions. This year, we submitted three runs based on the data used in the testing step consisting of 1) uogTr-MT: using the provided manually rewritten utterances as the queries; 2) uogTr-AT: using the raw utterances and the provided provenances as the context for rewriting the queries; 3) uogTr-MI-HB: using the raw utterances and the output from the mixed-initiative sub-task as the context for rewriting the queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KongyoungMO22.bib) "
	```
	@inproceedings{DBLP:conf/trec/KongyoungMO22,
		author = {Sarawoot Kongyoung and Craig Macdonald and Iadh Ounis},
		editor = {Ian Soboroff and Angela Ellis},
		title = {University of Glasgow Terrier Team at the {TREC} 2022 Conversational Assistance Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/UoGTr.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KongyoungMO22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WaterlooClarke at the TREC 2022 Conversational Assistant Track

_Siqing Huo, Xinyi Yan, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./cast/participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/WaterlooClarke.C.pdf](https://trec.nist.gov/pubs/trec31/papers/WaterlooClarke.C.pdf)
- :material-file-search: **Runs:** [UWCmanual22](./cast/runs.md#uwcmanual22) | [UWCcano22](./cast/runs.md#uwccano22) | [UWCauto22](./cast/runs.md#uwcauto22)

??? abstract "Abstract"
	
	The WaterlooClarke group submitted three runs to TREC Conversational Assistant Track (CAsT) 2022: UWCmanual22, UWCauto22, and UWCcano22. This report describes the techniques used and the results of these three runs. The pipeline to generate each run contains three main steps: 1) query reformulation, 2) passage retrieval and reranking, 3) passage summarization and reranking. For the UWCmanual22 run, we used the manual rewritten utterances provided as reformulated queries. For the UWCauto22 run, we used the automatic rewritten utterances provided as reformulated queries. For the UWCcano22 run, we augmented the automatic rewritten utterances provided with keywords extracted from the previous responses' titles, and used them as reformulated queries. We continued last year's strategy [6] of performing passage reranking with both MonoT5 and DuoT5 [2] on the pooled retrieved passages from both sparse and dense retrievers [1]. This year we focused on experimenting with the following changes: 1) Incorporating generative summarization techniques to make the produced answers more conversational. 2) Incorporating pseudo-relevance feedback into the passage retrieval stage to improve performance. In the next section, we will present the details of our pipeline
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuoYC22.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuoYC22,
		author = {Siqing Huo and Xinyi Yan and Charles L. A. Clarke},
		editor = {Ian Soboroff and Angela Ellis},
		title = {WaterlooClarke at the {TREC} 2022 Conversational Assistant Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/WaterlooClarke.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuoYC22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering-Based Query Expansion for Conversational Search:  IIIA@UNIPD at TREC CAsT 2022

_Guglielmo Faggioli, Nicola Ferro, Mattia Romanello_

- :fontawesome-solid-user-group: **Participant:** [iiia-unipd](./cast/participants.md#iiia-unipd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/iiia-unipd.C.pdf](https://trec.nist.gov/pubs/trec31/papers/iiia-unipd.C.pdf)
- :material-file-search: **Runs:** [DEI-run1](./cast/runs.md#dei-run1) | [DEI-run2](./cast/runs.md#dei-run2) | [DEI-run4](./cast/runs.md#dei-run4) | [DEI-run5.json](./cast/runs.md#dei-run5.json)

??? abstract "Abstract"
	
	Conversational Search task is becoming ubiquitous in our daily interaction with information systems. Nevertheless, it remains an extremely complex task due to its profoundly different nature from ad-hoc retrieval, and the challenges presented by the way a user interacts with the system. CAsT TREC Track explicitly aims at fostering the development of conversational systems and the discussion of the linked challenges within the research community. In this work, we describe the approach that we propose to CAsT 2022 to tackle the conversational task. In particular, our approach is based on expanding and rewriting the utterance at hand with the response to the previous utterance, using a QA model to extract it from the first passage retrieved in response to the previous query.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Faggioli0R22.bib) "
	```
	@inproceedings{DBLP:conf/trec/Faggioli0R22,
		author = {Guglielmo Faggioli and Nicola Ferro and Mattia Romanello},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Question Answering-Based Query Expansion for Conversational Search: IIIA@UNIPD at {TREC} CAsT 2022},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/iiia-unipd.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Faggioli0R22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Exploration Study of Mixed-initiative Query Reformulation in Conversational  Passage Retrieval

_Dayu Yang, Yue Zhang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./cast/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/udel_fang.C.pdf](https://trec.nist.gov/pubs/trec31/papers/udel_fang.C.pdf)
- :material-file-search: **Runs:** [mi_task_0822_1](./cast/runs.md#mi_task_0822_1) | [udinfo_best2021](./cast/runs.md#udinfo_best2021) | [udinfo_mi_b2021](./cast/runs.md#udinfo_mi_b2021) | [udinfo_onlyd](./cast/runs.md#udinfo_onlyd) | [udinfo_onlyd_mi](./cast/runs.md#udinfo_onlyd_mi)

??? abstract "Abstract"
	
	In this paper, we report our methods and experiments for the TREC Conversational Assistance Track (CAsT) 2022. In this work, we aim to reproduce multi-stage retrieval pipelines and explore one of the potential benefits of involving mixed-initiative interaction in conversational passage retrieval scenarios: reformulating raw queries. Before the first ranking stage of a multi-stage retrieval pipeline, we propose a mixed-initiative query reformulation module, which achieves query reformulation based on the mixed-initiative interaction between the users and the system, as the replacement for the neural reformulation method. Specifically, we design an algorithm to generate appropriate questions related to the ambiguities in raw queries, and another algorithm to reformulate raw queries by parsing users' feedback and incorporating it into the raw query. For the first ranking stage of our multi-stage pipelines, we adopt a sparse ranking function: BM25, and a dense retrieval method: TCT-ColBERT. For the second-ranking step, we adopt a pointwise reranker: MonoT5, and a pairwise reranker: DuoT5. Experiments on both TREC CAsT 2021 and TREC CAsT 2022 datasets show the effectiveness of our mixed-initiative-based query reformulation method on improving retrieval performance compared with two popular reformulators: a neural reformulator: CANARD-T5 and a rule-based reformulator: historical query reformulator(HQE)
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangZF22.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangZF22,
		author = {Dayu Yang and Yue Zhang and Hui Fang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {An Exploration Study of Mixed-initiative Query Reformulation in Conversational Passage Retrieval},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/udel\_fang.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YangZF22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Clinical Trials 

#### Overview of the TREC 2022 Clinical Trials Track

_Kirk Roberts, Dina Demner-Fushman, Ellen M. Voorhees, Steven Bedrick, William R. Hersh_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/Overview_trials.pdf](https://trec.nist.gov/pubs/trec31/papers/Overview_trials.pdf)
??? abstract "Abstract"
	
	Clinical trials are the primary means for new medical treatments-such as drugs, surgical procedures, and behavior interventions-to demonstrate their effectiveness in an evidence-based manner. However, clinical trials have high costs, can take years to complete, and oftentimes fail to identify a sufficient number of patients to establish clinical significance. Automated methods for improving the patient recruitment process can aid in all three areas: reducing manual and expensive chart review, more quickly identifying eligible patients, and expanding the pool of candidate patients that may be eligible. The primary means of automating clinical trial recruitment is through the use of electronic health record (EHR) data. EHRs are responsible for documenting routine medical care, as well as being the legal and billing record. However, the re-use of EHR data for research is well-established (Hersh, 2007), commonly for observational studies but also as the source data for informatics-driven models, including machine learning (ML) and information retrieval (IR). This was the inspiration behind the TREC Medical Records track (2011-2012) (Voorhees and Tong, 2011; Voorhees and Hersh, 2012), which used short cohort descriptions as queries (e.g., “Patients treated for vascular claudication surgically”) and used EHR visit records as the document collection. Unfortunately, this track was discontinued due to the the lack of an EHR dataset of sufficient size to merit a proper IR evaluation. The TREC Clinical Trials track, instead, flips the trial-to-patients paradigm to a patient-to-trials paradigm. This has enabled the building of a large test collection for clinical trial search. In this paradigm, the topic is a (synthetic) patient description and the document collection is a large set of clinical trial descriptions (which are, notably, publicly and freely available). There are several challenges involved with task, however. The first set of challenges revolve around using clinical trial descriptions as the document collection. Clinical trial descriptions are often very long (see link to trial in Table 2). The core part of the description with regards to trial matching is the eligibility criteria, a (often long) list of inclusion criteria (the patient must meet all these requirements) and exclusion criteria (if the patient meets any of these criteria, they are ineligible and would be excluded from the trial). These criteria not only use complex medical terminology, but they are often written in a way that does not correspond directly to how patient cases are described in the EHR, making direct term mapping problematic. The second set of challenges revolves around the patient cases. In addition to the linguistic issues of how identical clinical concepts in EHR text versus trial descriptions, patient cases contain significant amounts of extraneous information with respect to the clinical trial. That is, not all of the information in a patient case need be covered in the trial. Rather, a sufficient amount of information must be present to suggest the patient may be eligible, while also not containing information showing the patient to be excluded. This means that many of the conditions in the patient description are irrelevant for a single clinical trial, whereas matching to a different clinical trial may involve a different subset of conditions in the patient case. As in 2021 Roberts et al. (2021b), to ensure this task focuses on information retrieval and not supervised information extraction, we present a lengthy (5-10 sentence) patient case description as the topic that simulates an admission statement in an EHR. The evaluation is further be broken down into Eligible, Excludes, and Not Relevant to allow retrieval methods to distinguish between patients that do not have sufficient information to qualify for the trial (Not Relevant) and those that are explicitly Excluded. This latter category can be difficult for retrieval systems without strong semantic understanding.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsDVBH22.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsDVBH22,
		author = {Kirk Roberts and Dina Demner{-}Fushman and Ellen M. Voorhees and Steven Bedrick and William R. Hersh},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Overview of the {TREC} 2022 Clinical Trials Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/Overview\_trials.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RobertsDVBH22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Matching a Patient from An Admission Note to Clinical Trials: Experiments  with Query Generation and Neural-Ranking

_Vincent Nguyen, Maciej Rybinski, Sarvnaz Karimi_

- :fontawesome-solid-user-group: **Participant:** [CSIROmed](./trials/participants.md#csiromed)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/CSIROmed.T.pdf](https://trec.nist.gov/pubs/trec31/papers/CSIROmed.T.pdf)
- :material-file-search: **Runs:** [doct5query](./trials/runs.md#doct5query) | [CSIROmedANIR](./trials/runs.md#csiromedanir) | [ANIR_demo](./trials/runs.md#anir_demo) | [zs_bert_500](./trials/runs.md#zs_bert_500) | [monobert500](./trials/runs.md#monobert500)

??? abstract "Abstract"
	
	Many clinical trials fail to attract enough eligible participants. The TREC 2022 Clinical Trials track set a task where patient data, in the form of clinical notes, can be used to match eligible patients to a relevant clinical trial. We explore a number of dense retrieval methods using Bidirectional Encoder Representations from Transformers (BERT). Our best method used BERT reranking using models based on monoBERT architecture. Our self-supervised monoBERT run achieved effectiveness competitive to that of a fully-tuned monoBERT run.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NguyenRK22.bib) "
	```
	@inproceedings{DBLP:conf/trec/NguyenRK22,
		author = {Vincent Nguyen and Maciej Rybinski and Sarvnaz Karimi},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Matching a Patient from An Admission Note to Clinical Trials: Experiments with Query Generation and Neural-Ranking},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/CSIROmed.T.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NguyenRK22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UNIMIB at TREC 2022 Clinical Trials Track

_Georgios Peikos, Gabriella Pasi_

- :fontawesome-solid-user-group: **Participant:** [UNIMIB](./trials/participants.md#unimib)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/UNIMIB.T.pdf](https://trec.nist.gov/pubs/trec31/papers/UNIMIB.T.pdf)
- :material-file-search: **Runs:** [IKR3_BSL](./trials/runs.md#ikr3_bsl) | [IKR3_TT_MW](./trials/runs.md#ikr3_tt_mw) | [IKR3_TT_BW](./trials/runs.md#ikr3_tt_bw) | [IKR3_BSL_TT_HW](./trials/runs.md#ikr3_bsl_tt_hw) | [IKR3_BSL_TT_MW](./trials/runs.md#ikr3_bsl_tt_mw)

??? abstract "Abstract"
	
	This notebook summarizes our participation as the UNIMIB team in the TREC 2022 Clinical Trials Track. In this work, we extend our last year's participation by further investigating the retrieval performance achieved by our decision-theoretic model for relevance estimation. Specifically, our objective was to investigate the effectiveness of our decision-theoretic model by heavily penalizing those clinical trials for which the patient has high topical similarity to the exclusion criteria. The model has been employed to estimate relevance in two retrieval settings, ranking and re-ranking. The obtained results showed that the proposed model performs equally well in both of them, while the best results in terms of precision were achieved in the re-ranking setting.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PeikosP22.bib) "
	```
	@inproceedings{DBLP:conf/trec/PeikosP22,
		author = {Georgios Peikos and Gabriella Pasi},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{UNIMIB} at {TREC} 2022 Clinical Trials Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/UNIMIB.T.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/PeikosP22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Elsevier Data Science Health Sciences at TREC 2022 Clinical Trials:  Exploring Transformer Embeddings for Clinical Trial Retrieval

_Drahomira Herrmannova, Sharvari Jadhav, Harsh Sindhwa, Hina Nazir, Elia Lima-Walton_

- :fontawesome-solid-user-group: **Participant:** [els_dshs](./trials/participants.md#els_dshs)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/els_dshs.T.pdf](https://trec.nist.gov/pubs/trec31/papers/els_dshs.T.pdf)
- :material-file-search: **Runs:** [senttr](./trials/runs.md#senttr) | [bm25_bi_filtered](./trials/runs.md#bm25_bi_filtered) | [bm25_st_bienc](./trials/runs.md#bm25_st_bienc) | [st_distilbert](./trials/runs.md#st_distilbert)

??? abstract "Abstract"
	
	In this paper, we describe the submissions of Elsevier Data Science Health Sciences to the TREC 2022 Clinical Trials Track. Our submissions explored the applicability of transformer embeddings to the task and demonstrated a straightforward retriever using the MiniLM model can achieve competitive performance. Additionally, we share observations from a manual evaluation we performed to better understand the performance of our embedding-based retrievers
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HerrmannovaJSNL22.bib) "
	```
	@inproceedings{DBLP:conf/trec/HerrmannovaJSNL22,
		author = {Drahomira Herrmannova and Sharvari Jadhav and Harsh Sindhwa and Hina Nazir and Elia Lima{-}Walton},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Elsevier Data Science Health Sciences at {TREC} 2022 Clinical Trials: Exploring Transformer Embeddings for Clinical Trial Retrieval},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/els\_dshs.T.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HerrmannovaJSNL22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Summarize and Expand Queries in Clinical Trials Retrieval. The IIIA  Unipd at TREC 2022 Clinical Trials

_Giorgio Maria Di Nunzio, Guglielmo Faggioli, Stefano Marchesin_

- :fontawesome-solid-user-group: **Participant:** [iiia-unipd](./trials/participants.md#iiia-unipd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/iiia-unipd.T.pdf](https://trec.nist.gov/pubs/trec31/papers/iiia-unipd.T.pdf)
- :material-file-search: **Runs:** [ims_BM25Filtered_s](./trials/runs.md#ims_bm25filtered_s) | [ims_BM25Filtered_kw](./trials/runs.md#ims_bm25filtered_kw) | [ims_RM3Filtered_kw](./trials/runs.md#ims_rm3filtered_kw) | [ims_RM3Filtered_s](./trials/runs.md#ims_rm3filtered_s) | [ims_T5summarizer](./trials/runs.md#ims_t5summarizer)

??? abstract "Abstract"
	
	We present the methodology and the experimental setting we, the Intelligent Interactive Information Access (IIIA)1 UNIPD team, used in the TREC Clinical Trials 2022. This work continues the long streak of studies we carried out at TREC Precision Medicine to evaluate the effectiveness of query reformulation, pseudo-relevance feedback, and document filtering. Compared to the procedure proposed in 2021, we introduced the use of manual summarization and removed rank fusion. The obtained results provide interesting insights on the different per-topic effectiveness and will be used for further analyses.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NunzioF022.bib) "
	```
	@inproceedings{DBLP:conf/trec/NunzioF022,
		author = {Giorgio Maria Di Nunzio and Guglielmo Faggioli and Stefano Marchesin},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Summarize and Expand Queries in Clinical Trials Retrieval. The {IIIA} Unipd at {TREC} 2022 Clinical Trials},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/iiia-unipd.T.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NunzioF022.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JBNU at TREC 2022 Clinical Trials Track

_Dalya Sin, Woo-Kyoung Lee, Seung-Hyeon Jo, Kyung-Soon Lee_

- :fontawesome-solid-user-group: **Participant:** [jbnu](./trials/participants.md#jbnu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/jbnu.T.pdf](https://trec.nist.gov/pubs/trec31/papers/jbnu.T.pdf)
- :material-file-search: **Runs:** [jbnu1](./trials/runs.md#jbnu1) | [jbnu2](./trials/runs.md#jbnu2)

??? abstract "Abstract"
	
	This paper describes the participation of the JBNU team at the TREC 2022 Clinical Trials Track. Our approach is to focus on clinical terms detected from the ClinicalBERT and BioBERT. In order to expand clinical terms, the synonym terms are extracted by BERT embedding model. Our experimental results showed 0.4527, 0.3220 and 0.5543 by NDCG@10, P@10 and MRR, respectively.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SinLJL22.bib) "
	```
	@inproceedings{DBLP:conf/trec/SinLJL22,
		author = {Dalya Sin and Woo{-}Kyoung Lee and Seung{-}Hyeon Jo and Kyung{-}Soon Lee},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{JBNU} at {TREC} 2022 Clinical Trials Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/jbnu.T.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SinLJL22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CogStack Cohort at TREC 2022 Clinical Trials Track

_Jack Wu, Zeljko Kraljevic, Thomas Searle, Daniel Bean, Richard J. B. Dobson_

- :fontawesome-solid-user-group: **Participant:** [phi_lab](./trials/participants.md#phi_lab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/phi_lab.T.pdf](https://trec.nist.gov/pubs/trec31/papers/phi_lab.T.pdf)
- :material-file-search: **Runs:** [phir1m1](./trials/runs.md#phir1m1) | [phir2m2](./trials/runs.md#phir2m2) | [phir3m1prf](./trials/runs.md#phir3m1prf) | [phir4m1prf2](./trials/runs.md#phir4m1prf2) | [phir5m2prf](./trials/runs.md#phir5m2prf)

??? abstract "Abstract"
	
	This notebook paper describes the methodology used to produce the retrieval results we submitted for TREC 2022 Clinical Trials Track. The method is based on named entity recognition and linking (NER+L). Medical Concept Annotation Tool (MedCAT) is used to perform NER+L on the topics and documents to produce entities in the SNOMED Clinical Terms ontology. The clinical terms extracted by the annotation process are used for indexing and retrieval purposes. The retrieval model used is a passage-based retrieval model that gives different weights to different document portions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuKSBD22.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuKSBD22,
		author = {Jack Wu and Zeljko Kraljevic and Thomas Searle and Daniel Bean and Richard J. B. Dobson},
		editor = {Ian Soboroff and Angela Ellis},
		title = {CogStack Cohort at {TREC} 2022 Clinical Trials Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/phi\_lab.T.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WuKSBD22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Hybrid Re-ranking for Biomedical Information Retrieval at the TREC  2021 Clinical Trials Track

_Ming-Xuan Shi, Tsung-Hsuan Pan, Hsin-Hsi Chen, Hen-Hsen Huang_

- :fontawesome-solid-user-group: **Participant:** [NTU_NLP](./trials/participants.md#ntu_nlp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/NTU_NLP-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/NTU_NLP-CT.pdf)

??? abstract "Abstract"
	
	This paper presents our methodology for the task of TREC 2021 Clinical Trials Track, which requires a system to retrieve and return the most relevant biomedical articles after giving queries. We propose a novel approach to biomedical information retrieval by leveraging the term-based and the embedding-based retrieval models with a re-ranking strategy. In our hybrid framework, all the documents will be indexed by using a term-based, efficient search engine. For the given query, a smaller set of candidate results are retrieved from the search engine. The ranking is determined not only by the term-based ranking score but also by the term relationships labeled by the Amazon Comprehend service1 for refinement. Then, the candidate results are further scored by using the embedding-based model. We represent the document and the query with bioBERT and compute the cosine similarity between a pair of the document embedding and the query embedding as their relevance score. The final score is a linear combination of the term-based and the embedding-based scores. Experimental results show that our hybrid re-ranking method improves both Precision@k and R-precision scores on the 2016 Clinical Decision Support Track and 2021 Clinical Trials Track dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShiPCH21.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShiPCH21,
		author = {Ming{-}Xuan Shi and Tsung{-}Hsuan Pan and Hsin{-}Hsi Chen and Hen{-}Hsen Huang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Hybrid Re-ranking for Biomedical Information Retrieval at the {TREC} 2021 Clinical Trials Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/NTU\_NLP-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ShiPCH21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Fair Ranking 

#### Overview of the TREC 2022 Fair Ranking Track

_Michael D. Ekstrand, Graham McDonald, Amifa Raj, Isaac Johnson_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/Overview_fair.pdf](https://trec.nist.gov/pubs/trec31/papers/Overview_fair.pdf)
??? abstract "Abstract"
	
	The TREC Fair Ranking Track aims to provide a platform for participants to develop and evaluate novel retrieval algorithms that can provide a fair exposure to a mixture of demographics or attributes, such as ethnicity, that are represented by relevant documents in response to a search query. For example, particular demographics or attributes can be represented by the documents' topical content or authors. The 2022 Fair Ranking Track adopted a resource allocation task. The task focused on supporting Wikipedia editors who are looking to improve the encyclopedia's coverage of topics under the purview of a WikiProject.1 WikiProject coordinators and/or Wikipedia editors search for Wikipedia documents that are in need of editing to improve the quality of the article. The 2022 Fair Ranking track aimed to ensure that documents that are about, or somehow represent, certain protected characteristics receive a fair exposure to the Wikipedia editors, so that the documents have an fair opportunity of being improved and, therefore, be well-represented in Wikipedia. The under-representation of particular protected characteristics in Wikipedia can result in systematic biases that can have a negative human, social, and economic impact, particularly for disadvantaged or protected societal groups [4, 7].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EkstrandMR022.bib) "
	```
	@inproceedings{DBLP:conf/trec/EkstrandMR022,
		author = {Michael D. Ekstrand and Graham McDonald and Amifa Raj and Isaac Johnson},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Overview of the {TREC} 2022 Fair Ranking Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/Overview\_fair.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/EkstrandMR022.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT CIDDA IR at the TREC 2022 Fair Ranking Track

_Sachin Pathiyan Cherumanal, Marwah Alaofi, Reham Abdullah Altalhi, Elham Naghizade, Falk Scholer, Damiano Spina_

- :fontawesome-solid-user-group: **Participant:** [rmit_cidda_ir](./fair/participants.md#rmit_cidda_ir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/rmit_cidda_ir.F.pdf](https://trec.nist.gov/pubs/trec31/papers/rmit_cidda_ir.F.pdf)
- :material-file-search: **Runs:** [rmit_cidda_ir_1](./fair/runs.md#rmit_cidda_ir_1) | [rmit_cidda_ir_2](./fair/runs.md#rmit_cidda_ir_2) | [rmit_cidda_ir_3](./fair/runs.md#rmit_cidda_ir_3) | [rmit_cidda_ir_4](./fair/runs.md#rmit_cidda_ir_4) | [rmit_cidda_ir_5](./fair/runs.md#rmit_cidda_ir_5) | [rmit_cidda_ir_6](./fair/runs.md#rmit_cidda_ir_6) | [rmit_cidda_ir_7](./fair/runs.md#rmit_cidda_ir_7) | [rmit_cidda_ir_8](./fair/runs.md#rmit_cidda_ir_8)

??? abstract "Abstract"
	
	This report describes the participation of the RMIT CIDDA IR1 group at the TREC 2022 Fair Ranking Track (Task 1). We submitted 8 runs with the aim to explore the role of explicit search result diversification, ranking fusion, and the use of a multi-criteria decision-making method to generate fair rankings considering multiple protected attributes.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CherumanalAANSS22.bib) "
	```
	@inproceedings{DBLP:conf/trec/CherumanalAANSS22,
		author = {Sachin Pathiyan Cherumanal and Marwah Alaofi and Reham Abdullah Altalhi and Elham Naghizade and Falk Scholer and Damiano Spina},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{RMIT} {CIDDA} {IR} at the {TREC} 2022 Fair Ranking Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/rmit\_cidda\_ir.F.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CherumanalAANSS22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Exploration of Learning-to-re-rank Using a Two-step Framework for  Fair Ranking

_Fumian Chen, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./fair/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/udel_fang.F.pdf](https://trec.nist.gov/pubs/trec31/papers/udel_fang.F.pdf)
- :material-file-search: **Runs:** [UDInfo_F_bm25](./fair/runs.md#udinfo_f_bm25) | [UDInfo_F_mlp4](./fair/runs.md#udinfo_f_mlp4) | [UDInfo_F_lgbm4](./fair/runs.md#udinfo_f_lgbm4) | [UDInfo_F_mlp2](./fair/runs.md#udinfo_f_mlp2) | [UDInfo_F_lgbm2](./fair/runs.md#udinfo_f_lgbm2)

??? abstract "Abstract"
	
	As fairness has been attracting increasing attention in search engines, producing both fair and relevant rankings has become a major challenge for many information retrieval systems. In 2022, TREC fair ranking track launched an ad-hoc retrieval task for Wikipedia editors, which returns not only relevant documents of each query but also provides fair exposure to each document. The main goal of our participation in this track is to explore a fairness-aware two-step fair ranking framework using supervised learning-based re-rankers. Given a query, we first retrieve relevant documents and then use the re-ranker to re-rank the documents so that the final ranking is fair evaluated by the attention-weighted rank fairness (AWRF). We utilize the simple yet well-performed BM25 retrieval model to obtain relevant documents of each query. We tested a gradient-boosted tree-based (GBDT) LambdaMART model and a neural-based multilayer perceptron model. To better train the supervised learning models, we also extracted contextual-based features to augment our training data. We encoded fairness through a pre-processing method by constructing fairness scores. Our results also show the possibility of leveraging supervised learning-based re-rankers and contextual features.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenF22.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenF22,
		author = {Fumian Chen and Hui Fang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {An Exploration of Learning-to-re-rank Using a Two-step Framework for Fair Ranking},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/udel\_fang.F.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ChenF22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## CrisisFACTs 

#### IRIT-IRIS at TREC 2022: CrisisFACTS Track

_Alexis Dusart, Gilles Hubert, Karen Pinel-Sauvagnat_

- :fontawesome-solid-user-group: **Participant:** [IRIT_IRIS](./crisis/participants.md#irit_iris)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/IRIT_IRIS.R.pdf](https://trec.nist.gov/pubs/trec31/papers/IRIT_IRIS.R.pdf)
- :material-file-search: **Runs:** [IRIT_IRIS_tssubert](./crisis/runs.md#irit_iris_tssubert) | [IRIT_IRIS_mean_USE_INeeds](./crisis/runs.md#irit_iris_mean_use_ineeds) | [IRIT_IRIS_mean_USE](./crisis/runs.md#irit_iris_mean_use)

??? abstract "Abstract"
	
	This paper presents the approaches proposed by the IRIS team of the IRIT laboratory for the TREC CrisisFACTS track. The CrisisFACTS track aims to summarize online data sources during crisis events. In our participation, we used neural language models according to three different strategies.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DusartHP22.bib) "
	```
	@inproceedings{DBLP:conf/trec/DusartHP22,
		author = {Alexis Dusart and Gilles Hubert and Karen Pinel{-}Sauvagnat},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{IRIT-IRIS} at {TREC} 2022: CrisisFACTS Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/IRIT\_IRIS.R.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DusartHP22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Neural Reranking and GPT-3 for Social Media Disaster Content  Summarization

_Jayr Alencar Pereira, Robson do Nascimento Fidalgo, Roberto de Alencar Lotufo, Rodrigo Frassetto Nogueira_

- :fontawesome-solid-user-group: **Participant:** [NM.unicamp](./crisis/participants.md#nm.unicamp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/NM.unicamp.R.pdf](https://trec.nist.gov/pubs/trec31/papers/NM.unicamp.R.pdf)
- :material-file-search: **Runs:** [NM-1](./crisis/runs.md#nm-1) | [NM-2](./crisis/runs.md#nm-2)

??? abstract "Abstract"
	
	Managing emergency events, such as natural disasters, necessitates real-time situational awareness for management teams. This paper presents a novel approach to obtaining accurate and comprehensive summaries of these events by utilizing a state-of-the-art open-source search engine and a large language model to retrieve and summarize information from social media and online news sources. The efficacy of this approach was evaluated on the TREC CrisisFACTS challenge dataset, utilizing automatic summarization metrics (e.g. Rouge-2 and BERTScore) and manual evaluation by the challenge organizers. Results indicate that while our approach achieves high comprehensiveness, it also exhibits a high degree of summary redundancy. Importantly, the pipeline components are few-shot, avoiding the need for training data collection and enabling rapid deployment.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PereiraFLN22.bib) "
	```
	@inproceedings{DBLP:conf/trec/PereiraFLN22,
		author = {Jayr Alencar Pereira and Robson do Nascimento Fidalgo and Roberto de Alencar Lotufo and Rodrigo Frassetto Nogueira},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Using Neural Reranking and {GPT-3} for Social Media Disaster Content Summarization},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/NM.unicamp.R.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/PereiraFLN22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### L3S at the TREC 2022 CrisisFACTS Track

_Thi Huyen Nguyen, Koustav Rudra_

- :fontawesome-solid-user-group: **Participant:** [eXSum22](./crisis/participants.md#exsum22)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/eXSum22.R.pdf](https://trec.nist.gov/pubs/trec31/papers/eXSum22.R.pdf)
- :material-file-search: **Runs:** [eXSum22_submission_01](./crisis/runs.md#exsum22_submission_01) | [eXSum22_submission_02](./crisis/runs.md#exsum22_submission_02)

??? abstract "Abstract"
	
	This paper describes our proposed approach for the multi-stream summarization of the crisis-related events in the TREC 2022 CrisisFACTS track [2]. We apply a retrieval and ranking-based two-step summarization approach. First, we employ a sparse retrieval framework where content texts from multiple online streams are treated as a document corpus, and a term matching-based retrieval strategy is used to retrieve relevant contents, so-called facts, to the set of queries in a given event day. Next, we use several pre-trained models to measure semantic similarity between query-fact or fact-fact pairs, score and rank the facts for the extraction of daily event summaries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NguyenR22.bib) "
	```
	@inproceedings{DBLP:conf/trec/NguyenR22,
		author = {Thi Huyen Nguyen and Koustav Rudra},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{L3S} at the {TREC} 2022 CrisisFACTS Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/eXSum22.R.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NguyenR22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Deep Neural Reranking and Unsupervised Extraction for Multi-Query  Focused Summarization

_Philipp Seeberger, Korbinian Riedhammer_

- :fontawesome-solid-user-group: **Participant:** [ohm_kiz](./crisis/participants.md#ohm_kiz)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/ohm_kiz.R.pdf](https://trec.nist.gov/pubs/trec31/papers/ohm_kiz.R.pdf)
- :material-file-search: **Runs:** [BM25_QAcrisis_ILP](./crisis/runs.md#bm25_qacrisis_ilp) | [BM25_QAasnq_ILP](./crisis/runs.md#bm25_qaasnq_ilp) | [BM25_Heuristic_ILP](./crisis/runs.md#bm25_heuristic_ilp) | [ColBERT_ILP](./crisis/runs.md#colbert_ilp)

??? abstract "Abstract"
	
	The CrisisFACTS Track aims to tackle challenges such as multi-stream fact-finding in the domain of event tracking; participants' systems extract important facts from several disasterrelated events while incorporating the temporal order. We propose a combination of retrieval, reranking, and the well-known Integer Linear Programming (ILP) and Maximal Marginal Relevance (MMR) frameworks. In the former two modules, we explore various methods including an entity-based baseline, pre-trained and fine-tuned Question Answering systems, and ColBERT. We then use the latter module as an extractive summarization component by taking diversity and novelty criteria into account. The automatic scoring runs show strong results across the evaluation setups but also reveal shortcomings and challenges.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SeebergerR22.bib) "
	```
	@inproceedings{DBLP:conf/trec/SeebergerR22,
		author = {Philipp Seeberger and Korbinian Riedhammer},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Combining Deep Neural Reranking and Unsupervised Extraction for Multi-Query Focused Summarization},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/ohm\_kiz.R.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SeebergerR22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multi-Faceted Question Fusion in the TREC 2022 CrisisFACTS Track

_Nathaniel W. Rollings, Peter A. Rankel, Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [umcp](./crisis/participants.md#umcp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/umcp.R.pdf](https://trec.nist.gov/pubs/trec31/papers/umcp.R.pdf)
- :material-file-search: **Runs:** [mrr_all](./crisis/runs.md#mrr_all) | [mrr_no_dd](./crisis/runs.md#mrr_no_dd) | [rr_now](./crisis/runs.md#rr_now) | [mrr_nobrf](./crisis/runs.md#mrr_nobrf) | [mrr_main](./crisis/runs.md#mrr_main) | [mrr_sum](./crisis/runs.md#mrr_sum) | [combsum](./crisis/runs.md#combsum)

??? abstract "Abstract"
	
	To address the challenges of multi-faceted questions in rapidly evolving environments, this paper introduces a system with an architecture based on recency-weighted and score-weighted reciprocal rank fusion of per-facet ranked lists. In the absence of existing data for parameter tuning, a small test collection built to support formative evaluation was developed and employed in system refinement. Issues of duplication were addressed through pruning near duplicates and, in one variation, synthesizing rather than simply selecting responses.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RollingsRO22.bib) "
	```
	@inproceedings{DBLP:conf/trec/RollingsRO22,
		author = {Nathaniel W. Rollings and Peter A. Rankel and Douglas W. Oard},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Multi-Faceted Question Fusion in the {TREC} 2022 CrisisFACTS Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/umcp.R.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RollingsRO22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

