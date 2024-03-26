# Proceedings - Precision Medicine 2018 

#### Overview of the TREC 2018 Precision Medicine Track

_Kirk Roberts, Dina Demner-Fushman, Ellen M. Voorhees, William R. Hersh, Steven Bedrick, Alexander J. Lazar_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/Overview-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/Overview-PM.pdf)
??? abstract "Abstract"
	
	The fundamental philosophy behind precision medicine is that for many complex diseases, there is no “one size fits all” solutions for patients with a particular diagnosis. The proper treatment for a patient depends upon genetic, environmental, and lifestyle choices. The ability to personalize treatment in a scientifically rigorous manner based on these factors is thus the hallmark of the emerging precision medicine paradigm. Nowhere is the potential impact of precision medicine more closely focused at the moment than in cancer, where lifesaving treatments for particular patients could prove ineffective or even deadly for other patients based entirely upon the particular genetic mutations in the patient's tumor(s). Significant effort, therefore, has been devoted to deepening the scientific research surrounding precision medicine. This includes the Precision Medicine Initiative (Collins and Varmus, 2015) launched by former President Barack Obama in 2015, now known as the All of Us Research Program. A fundamental difficulty with putting the findings of precision medicine into practice is that-by its very nature-precision medicine creates a huge space of treatment options (Frey et al., 2016). These can easily overwhelm clinicians attempting to stay up-to-date with the latest findings, and can easily inhibit a clinician's attempts to determine the best possible treatment for a particular patient. However, the ability to quickly locate relevant evidence is the hallmark of information retrieval (IR). [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsDVHBL18.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsDVHBL18,
		author = {Kirk Roberts and Dina Demner{-}Fushman and Ellen M. Voorhees and William R. Hersh and Steven Bedrick and Alexander J. Lazar},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2018 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/Overview-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsDVHBL18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Padua IMS Research Group at TREC 2018 Precision  Medicine Track

_Maristella Agosti, Giorgio Maria Di Nunzio, Stefano Marchesin_

- :fontawesome-solid-user-group: **Participant:** [ims_unipd](./participants.md#ims_unipd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/ims_unipd-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/ims_unipd-PM.pdf)
- :material-file-search: **Runs:** [IMS_NO_PRF](./runs.md#ims_no_prf) | [IMS_TERM](./runs.md#ims_term) | [IMS_PRF](./runs.md#ims_prf)

??? abstract "Abstract"
	
	We report on the participation of the Information Management System (IMS) Research Group of the University of Padua in the second task of the Precision Medicine Track at TREC 2018: the Clinical Trials task. We designed a procedure to: i) expand query terms iteratively, based on knowledge bases, to increase the probability of finding relevant trials by adding neoplasm, gene, and protein term variants to the initial query; ii) filter out trials based on demographic data. We submitted three runs: a plain BM25 using the provided textual fields <gene> and <disease> as query, a BM25 with a first knowledge-based query expansion, and another BM25 with an additional knowledge-based query expansion. This initial set of experiments lays the ground for a deeper study on the effectiveness of (automatic) knowledge-based expansion techniques in the context of precision medicine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AgostiN018.bib) "
	```
	@inproceedings{DBLP:conf/trec/AgostiN018,
		author = {Maristella Agosti and Giorgio Maria Di Nunzio and Stefano Marchesin},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {The University of Padua {IMS} Research Group at {TREC} 2018 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/ims\_unipd-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AgostiN018.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Learning to rank clinical trials with rule-based criteria

_Gonçalo Araújo, André Mourão, João Magalhães_

- :fontawesome-solid-user-group: **Participant:** [NOVASearch](./participants.md#novasearch)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/NOVASearch-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/NOVASearch-PM.pdf)
- :material-file-search: **Runs:** [NS_PM_1](./runs.md#ns_pm_1) | [NS_PM_2](./runs.md#ns_pm_2) | [NS_PM_3](./runs.md#ns_pm_3) | [NS_PM_4](./runs.md#ns_pm_4) | [NS_PM_5](./runs.md#ns_pm_5)

??? abstract "Abstract"
	
	This report describes the NOVASearch retrieval system for the TREC 2018 Precision Medicine Track in the Clinical Trials matching task. The parsing of queries and documents in the Clinical Trials task were structured into multiple fields according to the details about inclusion and exclusion criteria. We also considered multiple text processing filters on the largest text fields.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AraujoMM18.bib) "
	```
	@inproceedings{DBLP:conf/trec/AraujoMM18,
		author = {Gon{\c{c}}alo Ara{\'{u}}jo and Andr{\'{e}} Mour{\~{a}}o and Jo{\~{a}}o Magalh{\~{a}}es},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Learning to rank clinical trials with rule-based criteria},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/NOVASearch-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AraujoMM18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RSA DSc on TREC's 2018 Precision Medicine Track

_Alexandros Bampoulidis, Mihai Lupu_

- :fontawesome-solid-user-group: **Participant:** [RSA_DSC](./participants.md#rsa_dsc)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/RSA_DSC-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/RSA_DSC-PM.pdf)
- :material-file-search: **Runs:** [RSA_DSC_CT_4](./runs.md#rsa_dsc_ct_4) | [RSA_DSC_CT_5](./runs.md#rsa_dsc_ct_5) | [RSA_DSC_CT_3](./runs.md#rsa_dsc_ct_3) | [RSA_DSC_CT_2](./runs.md#rsa_dsc_ct_2) | [RSA_DSC_CT_1](./runs.md#rsa_dsc_ct_1) | [RSA_DSC_LA_1](./runs.md#rsa_dsc_la_1) | [RSA_DSC_LA_5](./runs.md#rsa_dsc_la_5) | [RSA_DSC_LA_3](./runs.md#rsa_dsc_la_3) | [RSA_DSC_LA_4](./runs.md#rsa_dsc_la_4) | [RSA_DSC_LA_2](./runs.md#rsa_dsc_la_2)

??? abstract "Abstract"
	
	In this paper, we describe our approach to TREC's 2018 Precision Medicine challenge. We describe how we developed a system that semantically enriches the text documents and the disease part of the topic and issues extensive and detailed boolean queries to the Information Retrieval system and we present its results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BampoulidisL18.bib) "
	```
	@inproceedings{DBLP:conf/trec/BampoulidisL18,
		author = {Alexandros Bampoulidis and Mihai Lupu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{RSA} DSc on TREC's 2018 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/RSA\_DSC-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BampoulidisL18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Brown University at TREC Precision Medicine 2018

_Prakrit Baruah, Riya Dulepet, Kyle Qian, Carsten Eickhoff_

- :fontawesome-solid-user-group: **Participant:** [Brown](./participants.md#brown)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/Brown-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/Brown-PM.pdf)
- :material-file-search: **Runs:** [mnz](./runs.md#mnz) | [sum](./runs.md#sum) | [cubicmnz](./runs.md#cubicmnz) | [cubicsumEW](./runs.md#cubicsumew) | [cubicsumW](./runs.md#cubicsumw) | [sumEW](./runs.md#sumew) | [cubicsumWAbs](./runs.md#cubicsumwabs) | [sumAbs](./runs.md#sumabs) | [mnzAbs](./runs.md#mnzabs) | [cubicmnzAbs](./runs.md#cubicmnzabs)

??? abstract "Abstract"
	
	This paper describes Brown University's submission to the TREC 2018 Precision Medicine (PM) track. This report details our efforts to query processing and retrieval modeling. As a key difference to last year's edition of the task, we are able to include supervised rankers based on existing patient-document relevance labels. We use this information in the form of cubic rank transformations between initial weak rankers and the final ranking. The empirical evaluation is based on 50 synthetic precision oncology patients and shows solid retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BaruahDQE18.bib) "
	```
	@inproceedings{DBLP:conf/trec/BaruahDQE18,
		author = {Prakrit Baruah and Riya Dulepet and Kyle Qian and Carsten Eickhoff},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Brown University at {TREC} Precision Medicine 2018},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/Brown-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BaruahDQE18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### POZNAN Contribution to TREC PM 2018 (Notebook Paper)

_Artur Cieslewicz, Jakub Dutkiewicz, Czeslaw Jedrzejek_

- :fontawesome-solid-user-group: **Participant:** [Poznan](./participants.md#poznan)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/Poznan-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/Poznan-PM.pdf)
- :material-file-search: **Runs:** [BB2_sq_nprf](./runs.md#bb2_sq_nprf) | [BB2sqw2vprf](./runs.md#bb2sqw2vprf) | [BB2_vq_noprf](./runs.md#bb2_vq_noprf) | [BB2vqw2vprf](./runs.md#bb2vqw2vprf) | [sq](./runs.md#sq) | [bool51](./runs.md#bool51)

??? abstract "Abstract"
	
	This work describes the medical information retrieval systems designed by the Poznan Consortium for TREC PM, personalized medicine track, which was submitted to the TREC 2018. The baseline is the Terrier BB2. For Clinical Trials this work uses the following options: Terrier BB2_simple_noprf: query without extension (sq_nprf); Terrier BB2_simple_w2v_prf: query extended with w2v and terrier prf (sqw2vprf); Terrier BB2 _variant_noprf: query + gene variant; without extension (vq_noprf); BB2_variant_w2v_prf: query + gene variant extended with w2v and terrier prf (vqw2vprf); SQ_results: experimental search of the sql database using keywords from query (sq). Our best result is vq_noprf which is significantly better (approximately 0.08 for evaluated measures). With suitable word2method the results are better compared to query extension using Mesh and disease taxonomy. For Medline abstracts the documents are placed in the SQL database. For each document templates of diseases, genes, and applicability as Precision Medicine vs research objects are matched. Patterns are saved using regular expressions. The pattern association with the document is stored in the SQL database. For Medline abstracts our results are little worse than the TREC 2018 median.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CieslewiczDJ18.bib) "
	```
	@inproceedings{DBLP:conf/trec/CieslewiczDJ18,
		author = {Artur Cieslewicz and Jakub Dutkiewicz and Czeslaw Jedrzejek},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{POZNAN} Contribution to {TREC} {PM} 2018 (Notebook Paper)},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/Poznan-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CieslewiczDJ18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### InfoLabPM at TREC 2018 Precision Medicine Track

_João Ferreira, Carla Teixeira Lopes_

- :fontawesome-solid-user-group: **Participant:** [InfoLabPM](./participants.md#infolabpm)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/InfoLabPM-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/InfoLabPM-PM.pdf)
- :material-file-search: **Runs:** [minfolabBA](./runs.md#minfolabba) | [minfolabBC](./runs.md#minfolabbc) | [minfolabBD](./runs.md#minfolabbd) | [minfolabTH](./runs.md#minfolabth) | [tinfolabBF](./runs.md#tinfolabbf) | [tinfolabBK](./runs.md#tinfolabbk) | [tinfolabF](./runs.md#tinfolabf)

??? abstract "Abstract"
	
	This paper reports the participation of the InfoLab at the TREC Precision Medicine Track 2018. InfoLab is an informal group that brings together researchers with interest in the information area and is located at Faculty of Engineering of University of Porto. The experiments made in this participation include query expansion approaches for the disease and gene concepts. The expansion of the disease terms was done using Unified Medical Language System (UMLS). UMLS is a repository that provides the mapping between a large number of vocabularies. The gene terms were expanded using Ensembl. Ensembl provides a genome browser that maps genes to their synonyms. An additional layer was developed on top of Terrier to provide the execution of a large batch of experiments. Multiple runs were evaluated in order to measure the influence of each expansion approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FerreiraL18.bib) "
	```
	@inproceedings{DBLP:conf/trec/FerreiraL18,
		author = {Jo{\~{a}}o Ferreira and Carla Teixeira Lopes},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {InfoLabPM at {TREC} 2018 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/InfoLabPM-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FerreiraL18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CBNU at TREC 2018 Precision Medicine Track

_Seung-Hyeon Jo, Won-Kyu Choi, Kyung-Soon Lee_

- :fontawesome-solid-user-group: **Participant:** [cbnu](./participants.md#cbnu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/cbnu-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/cbnu-PM.pdf)
- :material-file-search: **Runs:** [cbnuCT1](./runs.md#cbnuct1) | [cbnuCT2](./runs.md#cbnuct2) | [cbnuCT3](./runs.md#cbnuct3) | [cbnuSA1](./runs.md#cbnusa1) | [cbnuSA3](./runs.md#cbnusa3) | [cbnuSA2](./runs.md#cbnusa2)

??? abstract "Abstract"
	
	This paper describes the participation of the CBNU team at the TREC Precision Medicine Track 2018. We propose construction of cancer-centered document clusters using gene information. Documents are retrieved by re-ranking documents and pseudo-relevance feedback based on cancer-centered document clusters.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JoCL18.bib) "
	```
	@inproceedings{DBLP:conf/trec/JoCL18,
		author = {Seung{-}Hyeon Jo and Won{-}Kyu Choi and Kyung{-}Soon Lee},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CBNU} at {TREC} 2018 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/cbnu-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JoCL18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Retrieving scientific abstracts iteratively: MedIER at TREC 2018  Precision Medicine Track

_Jinghui Liu, Clair A. Kronk, Wu-Chen Su, Danny T. Y. Wu, V. G. Vinod Vydiswaran_

- :fontawesome-solid-user-group: **Participant:** [MedIER](./participants.md#medier)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/MedIER-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/MedIER-PM.pdf)
- :material-file-search: **Runs:** [MedIER_sa11](./runs.md#medier_sa11) | [MedIER_sa12](./runs.md#medier_sa12) | [MedIER_sa13](./runs.md#medier_sa13) | [MedIER_sa14](./runs.md#medier_sa14) | [MedIER_sa15](./runs.md#medier_sa15)

??? abstract "Abstract"
	
	This paper describes the approach developed by the MedIER team - a collaboration between the University of Michigan and the University of Cincinnati - for the TREC 2018 Precision Medicine Track. We implement an iterative approach of document retrieval with modified queries, and combine the results by formulating re-ranking as a text classification task. We evaluate our proposed framework to retrieve biomedical research abstracts. Our experiments show that the iterative re-retrieval approach is effective in retrieving higher number of relevant scientific abstracts.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuVKSWV18.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuVKSWV18,
		author = {Jinghui Liu and Clair A. Kronk and Wu{-}Chen Su and Danny T. Y. Wu and V. G. Vinod Vydiswaran},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Retrieving scientific abstracts iteratively: MedIER at {TREC} 2018 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/MedIER-PM.pdf},
		timestamp = {Tue, 01 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LiuVKSWV18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2018 Precision Medicine - Medical University of Graz

_Pablo López-García_

- :fontawesome-solid-user-group: **Participant:** [imi_mug](./participants.md#imi_mug)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/imi_mug-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/imi_mug-PM.pdf)
- :material-file-search: **Runs:** [imi_mug_abs1](./runs.md#imi_mug_abs1) | [imi_mug_ct1](./runs.md#imi_mug_ct1) | [imi_mug_abs2](./runs.md#imi_mug_abs2) | [imi_mug_abs3](./runs.md#imi_mug_abs3) | [imi_mug_abs4](./runs.md#imi_mug_abs4) | [imi_mug_abs5](./runs.md#imi_mug_abs5) | [imi_mug_ct2](./runs.md#imi_mug_ct2) | [imi_mug_ct3](./runs.md#imi_mug_ct3) | [imi_mug_ct4](./runs.md#imi_mug_ct4) | [imi_mug_ct5](./runs.md#imi_mug_ct5)

??? abstract "Abstract"
	
	In this paper we report on our participation in the TREC 2018 Precision Medicine track (team name: imi_mug). We submitted 5 fully automatic runs to both the biomedical articles and clinical trials subtasks. Our system was based on Elasticsearch, templates, and parameter grid search query generation, building heavily on our previous participation and the reference standard from 2017. Our results were well above the median for the biomedical articles subtask and median/below median for the clinical trials subtask.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lopez-Garcia18.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lopez-Garcia18,
		author = {Pablo L{\'{o}}pez{-}Garc{\'{\i}}a},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2018 Precision Medicine - Medical University of Graz},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/imi\_mug-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lopez-Garcia18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Filtering and reranking using MetaMap named entities recognizer

_Pilar López-Úbeda, Manuel Carlos Díaz-Galiano, María Teresa Martín Valdivia, Luis Alfonso Ureña López_

- :fontawesome-solid-user-group: **Participant:** [SINAI](./participants.md#sinai)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/SINAI-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/SINAI-PM.pdf)
- :material-file-search: **Runs:** [SINAI_Base](./runs.md#sinai_base) | [SINAI_FU](./runs.md#sinai_fu) | [SINAI_FUO](./runs.md#sinai_fuo)

??? abstract "Abstract"
	
	In this paper we present our participation as SINAI research group from the Universidad of Ja´en at Text REtrieval Conference (TREC), specifically in sub-task Precision Medicine. The main objective of the task is to locate relevant information for a patient using information retrieval technologies. Our group applies one of the techniques of Natural Language Processing: Named Entities Recognition. For this task we have used MetaMap. This recognizer provide UMLS concepts from a given text. In addition, we have applied the document ranking technique to sort the final list of relevant documents using the common concepts found in the query and each document. The results obtained are not as expected because not all the concepts detected by MetaMap are relevant in the queries. However, our results are above the average of the runs sent by participants.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lopez-UbedaDVL18a.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lopez-UbedaDVL18a,
		author = {Pilar L{\'{o}}pez{-}{\'{U}}beda and Manuel Carlos D{\'{\i}}az{-}Galiano and Mar{\'{\i}}a Teresa Mart{\'{\i}}n Valdivia and Luis Alfonso Ure{\~{n}}a L{\'{o}}pez},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Filtering and reranking using MetaMap named entities recognizer},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/SINAI-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lopez-UbedaDVL18a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Team UVA_ART at TREC 2018 Precision Medicine Track: Graph-based  Concept Expansion and NLP for Document Relevance Boosting

_Sean Mullane, Kasi Vegesana, Valentina Baljak_

- :fontawesome-solid-user-group: **Participant:** [UVA_ART](./participants.md#uva_art)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/UVA_ART-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/UVA_ART-PM.pdf)
- :material-file-search: **Runs:** [UVAEXPBOOST](./runs.md#uvaexpboost) | [UVAEXPBSTNEG](./runs.md#uvaexpbstneg) | [UVAEXPBSTDIF](./runs.md#uvaexpbstdif) | [UVAEXPBSTSHD](./runs.md#uvaexpbstshd) | [UVAEXPBSTEXT](./runs.md#uvaexpbstext)

??? abstract "Abstract"
	
	This paper describes the UVA_ART* team entries in the TREC 2018 workshop series Precision Medicine Track. We submitted 5 runs for the Scientific Abstracts task. Our approach used an exclusivity-based relatedness measure defined on the UMLS Metathesaurus ontologies to add context to our queries. We combined this with natural language processing using cTAKES for concept annotation to effect a graph-based query expansion on an enriched document corpus. We used Elasticsearch as our ranking and query engine with different query templates for each run. Our efforts demonstrate that the existing medical ontologies can be leveraged to achieve moderate results with little to no other clinical input.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MullaneVB18.bib) "
	```
	@inproceedings{DBLP:conf/trec/MullaneVB18,
		author = {Sean Mullane and Kasi Vegesana and Valentina Baljak},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Team UVA{\_}ART at {TREC} 2018 Precision Medicine Track: Graph-based Concept Expansion and {NLP} for Document Relevance Boosting},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/UVA\_ART-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MullaneVB18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### KlickLabs at TREC 2018 Precision Medicine track

_Lediona Nishani, Maheedhar Kolla, Gaurav Baruah_

- :fontawesome-solid-user-group: **Participant:** [KlickLabs](./participants.md#klicklabs)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/KlickLabs-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/KlickLabs-PM.pdf)
- :material-file-search: **Runs:** [KLPM18T1Bl](./runs.md#klpm18t1bl) | [KLPM18T2Bl](./runs.md#klpm18t2bl) | [KL18AbsFuse](./runs.md#kl18absfuse) | [KL18absHY](./runs.md#kl18abshy) | [KL18absWV](./runs.md#kl18abswv) | [KL18TrialBF](./runs.md#kl18trialbf) | [KL18TriFuse](./runs.md#kl18trifuse) | [KL18TriHY](./runs.md#kl18trihy) | [KL18TrialWV](./runs.md#kl18trialwv)

??? abstract "Abstract"
	
	Precision medicine aims to provide the most accurate course of treatment, personalized for each patient. The 2018 Precision Medicine (PM) track aims to build systems, that sift through biomedical articles to find relevant cancer treatments for patients, as well as search for clinical trials for which a patient might be eligible. Cancer, as a disease, can occur in various forms, be of different types, and affect multiple organs as well as bodily systems. Additionally, every patient-cancer combination presents with slight variations depending on genetics, age, sex, and other factors. As of 2017, 16% of PubMed articles related to cancer [5], and over 500,000 articles are added to PubMed each year, thereby, making quality information retrieval for PM an important problem to tackle, for the benefit of doctors and patients alike. In this work, we develop query-expansion methods, with an aim to compare their performance over the 2018 PM task. Our experiments indicate that medical ontology (NCIt) based expansion performs well for retrieving scientific abstracts from PubMed. Utilizing demographic information in queries improves the performance for clinical trial retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NishaniKB18.bib) "
	```
	@inproceedings{DBLP:conf/trec/NishaniKB18,
		author = {Lediona Nishani and Maheedhar Kolla and Gaurav Baruah},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {KlickLabs at {TREC} 2018 Precision Medicine track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/KlickLabs-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NishaniKB18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HPI-DHC at TREC 2018 Precision Medicine Track

_Michel Oleynik, Erik Faessler, Ariane Morassi Sasso, Arpita Kappattanavar, Benjamin Bergner, Harry Freitas Da Cruz, Jan-Philipp Sachs, Suparno Datta, Erwin P. Böttinger_

- :fontawesome-solid-user-group: **Participant:** [hpi-dhc](./participants.md#hpi-dhc)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/hpi-dhc-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/hpi-dhc-PM.pdf)
- :material-file-search: **Runs:** [hpipubboost](./runs.md#hpipubboost) | [hpictboost](./runs.md#hpictboost) | [hpipubclass](./runs.md#hpipubclass) | [hpipubnone](./runs.md#hpipubnone) | [hpipubcommon](./runs.md#hpipubcommon) | [hpipubbase](./runs.md#hpipubbase) | [hpictall](./runs.md#hpictall) | [hpictphrase](./runs.md#hpictphrase) | [hpictcommon](./runs.md#hpictcommon) | [hpictbase](./runs.md#hpictbase)

??? abstract "Abstract"
	
	The TREC-PM challenge aims for advances in the field of information retrieval applied to precision medicine. Here we describe our experimental setup and the achieved results in its 2018 edition. We explored the use of unsupervised topic models, supervised document classification, and rule-based query-time search term boosting and expansion. We participated in the biomedical articles and clinical trials subtasks and were among the three highest-scoring teams. Our results showed that query expansion associated with hand-crafted rules contribute to better values of information retrieval metrics. However, the use of a precision medicine classifier did not show the expected improvement for the biomedical abstracts subtask. In the future, we plan to add different terminologies to replace hand-crafted rules and experiment with negation detection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OleynikFSKBCSDB18.bib) "
	```
	@inproceedings{DBLP:conf/trec/OleynikFSKBCSDB18,
		author = {Michel Oleynik and Erik Faessler and Ariane Morassi Sasso and Arpita Kappattanavar and Benjamin Bergner and Harry Freitas Da Cruz and Jan{-}Philipp Sachs and Suparno Datta and Erwin P. B{\"{o}}ttinger},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{HPI-DHC} at {TREC} 2018 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/hpi-dhc-PM.pdf},
		timestamp = {Thu, 21 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OleynikFSKBCSDB18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBI at TREC 2018: Precision Medicine Track

_Francesco Ronzano, Emilio Centeno, Judith Pérez-Granado, Laura I. Furlong_

- :fontawesome-solid-user-group: **Participant:** [PM_IBI](./participants.md#pm_ibi)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/PM_IBI-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/PM_IBI-PM.pdf)
- :material-file-search: **Runs:** [PM_IBI_run1](./runs.md#pm_ibi_run1) | [PM_IBI_run2](./runs.md#pm_ibi_run2) | [PM_IBI_run3](./runs.md#pm_ibi_run3)

??? abstract "Abstract"
	
	Nowadays, the growing amount of biomedical scientific literature that can be accessed online represents a valuable source of information useful to tailor medical decisions to a specific clinical case. With this respect, Information Retrieval tools play an essential role in enabling physicians to automatically analyze huge amounts of publications so as to retrieve relevant recent information related to the treatment, prevention or prognosis of specific clinical conditions and traits. In this paper, we present and discuss the biomedical scientific Information Retrieval strategy we developed in the context of our participation to the Precision Medicine Track of the Text Retrieval Conference 2018. Given the description of a clinical case, we describe how we retrieve from PubMed a ranked list of scientific abstracts that discuss medical care that may be relevant for the patient under consideration. To this purpose we rely on the query formulation capabilities provided by Elasticsearch, a full-text search engine, complemented by data processing steps useful both to properly build search queries and to refine the ranking of search results proposed by Elasticsearch.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RonzanoCPF18.bib) "
	```
	@inproceedings{DBLP:conf/trec/RonzanoCPF18,
		author = {Francesco Ronzano and Emilio Centeno and Judith P{\'{e}}rez{-}Granado and Laura I. Furlong},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IBI} at {TREC} 2018: Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/PM\_IBI-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RonzanoCPF18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UTD HLTRI at TREC 2018: Precision Medicine Track

_Stuart J. Taylor, Sanda M. Harabagiu, Travis R. Goodwin_

- :fontawesome-solid-user-group: **Participant:** [UTDHLTRI](./participants.md#utdhltri)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/UTDHLTRI-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/UTDHLTRI-PM.pdf)
- :material-file-search: **Runs:** [UTDHLTRI_RA](./runs.md#utdhltri_ra) | [UTDHLTRI_RAT](./runs.md#utdhltri_rat) | [UTDHLTRI_RF](./runs.md#utdhltri_rf) | [UTDHLTRI_RFT](./runs.md#utdhltri_rft) | [UTDHLTRI_NL](./runs.md#utdhltri_nl) | [UTDHLTRI_NLT](./runs.md#utdhltri_nlt) | [UTDHLTRI_SF](./runs.md#utdhltri_sf) | [UTDHLTRI_SFT](./runs.md#utdhltri_sft) | [UTDHLTRI_SS](./runs.md#utdhltri_ss) | [UTDHLTRI_SST](./runs.md#utdhltri_sst)

??? abstract "Abstract"
	
	In this paper, we describe the system designed for the TREC 2018 Precision Medicine track by the University of Texas at Dallas (UTD) Human Language Technology Research Institute (HLTRI). Our system extends the system submitted for the 2017 track which incorporates an aspect-based retrieval paradigm wherein each of the four structured components of the topic is cast as a separate aspect, along with two “hidden” aspects encoding the need that retrieved documents be within the domain of precision medicine and that retrieved documents have a focus on treatment. For the 2018 system, in addition to the aspect-based retrieval, we incorporated learning-to-rank (L2R). Our experiments show that our L2R approach leads to improved quality of retrieved clinical trials, but degrades performance for scientific articles.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TaylorHG18.bib) "
	```
	@inproceedings{DBLP:conf/trec/TaylorHG18,
		author = {Stuart J. Taylor and Sanda M. Harabagiu and Travis R. Goodwin},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UTD} {HLTRI} at {TREC} 2018: Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/UTDHLTRI-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TaylorHG18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploring post retrieval techniques for bio-medical domain retrieval

_Yue Wang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/udel_fang-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/udel_fang-PM.pdf)
- :material-file-search: **Runs:** [UDInfoPMCT1](./runs.md#udinfopmct1) | [UDInfoPMCT2](./runs.md#udinfopmct2) | [UDInfoPMCT3](./runs.md#udinfopmct3) | [UDInfoPMCT4](./runs.md#udinfopmct4) | [UDInfoPMCT5](./runs.md#udinfopmct5) | [UDInfoPMSA1](./runs.md#udinfopmsa1) | [UDInfoPMSA2](./runs.md#udinfopmsa2) | [UDInfoPMSA3](./runs.md#udinfopmsa3) | [UDInfoPMSA4](./runs.md#udinfopmsa4) | [UDInfoPMSA5](./runs.md#udinfopmsa5)

??? abstract "Abstract"
	
	Retrieval is a common way to access the huge data collection in bio-medical domain. For instance, the physicians would need to retrieve relevant documents to treat cancer for the patients. With the huge number of documents in the collection, a reliable retrieval system is critical for a satisfying performance. This year's TREC Precision Medicine track continues the same procedure as last year by providing us the platform for testing different methods for biomedical retrieval. For this year, we used similar methods as we used in TREC PM17, i.e., term based representation and concept based representation. In addition, we also tried to combine the different representation with results filtering and two-round retrieval. The results show that the modification on the methods, i.e., results filtering and two round retrieval, did not outperform the baseline methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Wang018.bib) "
	```
	@inproceedings{DBLP:conf/trec/Wang018,
		author = {Yue Wang and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Exploring post retrieval techniques for bio-medical domain retrieval},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/udel\_fang-PM.pdf},
		timestamp = {Thu, 17 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Wang018.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MayoNLPTeam at the TREC 2018 Precision Medicine Track: Simple Information  Retrieval Approach Is the Best

_Yanshan Wang, Andrew Wen, Sijia Liu, Hongfang Liu_

- :fontawesome-solid-user-group: **Participant:** [MayoNLPTeam](./participants.md#mayonlpteam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/MayoNLPTeam-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/MayoNLPTeam-PM.pdf)
- :material-file-search: **Runs:** [mayomedsimp](./runs.md#mayomedsimp) | [mayomedcomp](./runs.md#mayomedcomp) | [mayomedcreat](./runs.md#mayomedcreat) | [mayopubtator](./runs.md#mayopubtator) | [mayoctsimp](./runs.md#mayoctsimp) | [mayoctcomp](./runs.md#mayoctcomp) | [mayoctscreat](./runs.md#mayoctscreat)

??? abstract "Abstract"
	
	This paper describes the participation of the Mayo Clinic NLP team in the Text REtrieval Conference (TREC) 2018 Precision Medicine (PM) track. The TREC 2018 PM track repeats the TREC 2017 PM track on retrieving relevant biomedical articles or clinical trials to cancer-related topics. We tested three information retrieval (IR) approaches in our official submission, including a simple approach of matching keywords and MeSH terms, an approach of matching extracted and normalized medical concepts, and a Learning-To-Rank approach based on TREC 2017 PM training data. In our systems, we used the NCI thesaurus and COSMIC to expand disease and gene terms with synonyms, respectively. Submissions were evaluated by the standard TREC test collections. Evaluation results show that our submissions using the simple IR approach have the best performance for both biomedical article and clinical trial retrieval subtasks. Recalling that our submissions using pseudo relevance feedback and Markov Random Field information retrieval models are also inferior to those using simple IR approaches in the TREC 2017 PM track, we conclude that the IR approaches shown effective in the general domain are not generalizable whilst retaining good performance for this medical track and the simple IR approach using keyword matching has the best record for consistent performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangW0L18.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangW0L18,
		author = {Yanshan Wang and Andrew Wen and Sijia Liu and Hongfang Liu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {MayoNLPTeam at the {TREC} 2018 Precision Medicine Track: Simple Information Retrieval Approach Is the Best},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/MayoNLPTeam-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangW0L18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCAS at TREC-2018 Precision Medicine Track

_Zhi Zheng, Canjia Li, Ben He, Jungang Xu_

- :fontawesome-solid-user-group: **Participant:** [UCAS](./participants.md#ucas)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/UCAS-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/UCAS-PM.pdf)
- :material-file-search: **Runs:** [UCASSA1](./runs.md#ucassa1) | [UCASSA2](./runs.md#ucassa2) | [UCASSA3](./runs.md#ucassa3) | [UCASSA4](./runs.md#ucassa4) | [UCASSA5](./runs.md#ucassa5) | [UCASCT1](./runs.md#ucasct1) | [UCASCT2](./runs.md#ucasct2) | [UCASCT3](./runs.md#ucasct3) | [UCASCT4](./runs.md#ucasct4) | [UCASCT5](./runs.md#ucasct5)

??? abstract "Abstract"
	
	This paper describes the system developed for the TREC 2018 Precision Medicine track. We adopt BM25F model with query expansion to retrieve clinical trials. For scientific abstract task, we use BM25 model to generate an initial ranking list and then adopt two methods to re-rank. Experimental results show that a new model that penalizes the articles unrelated to treatment, prevention, and prognosis improves the performance for scientific abstracts task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengLHX18.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengLHX18,
		author = {Zhi Zheng and Canjia Li and Ben He and Jungang Xu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UCAS} at {TREC-2018} Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/UCAS-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhengLHX18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Team Cat-Garfield at TREC 2018 Precision Medicine Track

_Xuesi Zhou, Xin Chen, Jian Song, Gang Zhao, Ji Wu_

- :fontawesome-solid-user-group: **Participant:** [Cat_Garfield](./participants.md#cat_garfield)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/Cat_Garfield-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/Cat_Garfield-PM.pdf)
- :material-file-search: **Runs:** [MSIIP_BASE](./runs.md#msiip_base) | [MSIIP_PBAH](./runs.md#msiip_pbah) | [MSIIP_PBH](./runs.md#msiip_pbh) | [MSIIP_PBL](./runs.md#msiip_pbl) | [MSIIP_PBPK](./runs.md#msiip_pbpk) | [MSIIP_TRIAL1](./runs.md#msiip_trial1) | [MSIIP_TRIAL2](./runs.md#msiip_trial2) | [MSIIP_TRIAL3](./runs.md#msiip_trial3) | [MSIIP_TRIAL4](./runs.md#msiip_trial4) | [MSIIP_TRIAL5](./runs.md#msiip_trial5)

??? abstract "Abstract"
	
	This paper describes the system designed for the TREC 2018 Precision Medicine Track by the Team Cat-Garfield from Tsinghua University. Our system is composed of two parts: the retrieval part aiming at high recall metric and the re-ranking part aiming at boosting infNDCG, P@10 and R-prec metrics via a heuristic scoring scheme. In order to introduce more external information into our systems, we developed a knowledge graph named TREC-KG, which plays a significant role in both the query expansion and the re-ranking part, and we utilized the qrels of TREC 2017 Precision Medicine Track as annotated data to train a classifier for precision medicine-relatedness of biomedical articles, named PM Classifier. In particular, we employed a hybrid method to score the precision medicine-relatedness of each retrieved article, combining the data-driven PM Classifier and a rule-based scoring scheme. The final results demonstrate that our systems are effective in both the biomedical article retrieval task and the clinical trial retrieval task, and the usage of the PM Classifier would bring performance improvement on R-prec metric in the biomedical article retrieval task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhouCSZW18.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhouCSZW18,
		author = {Xuesi Zhou and Xin Chen and Jian Song and Gang Zhao and Ji Wu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Team Cat-Garfield at {TREC} 2018 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/Cat\_Garfield-PM.pdf},
		timestamp = {Tue, 16 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhouCSZW18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

