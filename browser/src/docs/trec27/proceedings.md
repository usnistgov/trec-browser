# Proceedings 2018 

## Precision Medicine 

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

- :fontawesome-solid-user-group: **Participant:** [ims_unipd](./pm/participants.md#ims_unipd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/ims_unipd-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/ims_unipd-PM.pdf)
- :material-file-search: **Runs:** [IMS_NO_PRF](./pm/runs.md#ims_no_prf) | [IMS_TERM](./pm/runs.md#ims_term) | [IMS_PRF](./pm/runs.md#ims_prf)

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

- :fontawesome-solid-user-group: **Participant:** [NOVASearch](./pm/participants.md#novasearch)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/NOVASearch-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/NOVASearch-PM.pdf)
- :material-file-search: **Runs:** [NS_PM_1](./pm/runs.md#ns_pm_1) | [NS_PM_2](./pm/runs.md#ns_pm_2) | [NS_PM_3](./pm/runs.md#ns_pm_3) | [NS_PM_4](./pm/runs.md#ns_pm_4) | [NS_PM_5](./pm/runs.md#ns_pm_5)

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

- :fontawesome-solid-user-group: **Participant:** [RSA_DSC](./pm/participants.md#rsa_dsc)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/RSA_DSC-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/RSA_DSC-PM.pdf)
- :material-file-search: **Runs:** [RSA_DSC_CT_4](./pm/runs.md#rsa_dsc_ct_4) | [RSA_DSC_CT_5](./pm/runs.md#rsa_dsc_ct_5) | [RSA_DSC_CT_3](./pm/runs.md#rsa_dsc_ct_3) | [RSA_DSC_CT_2](./pm/runs.md#rsa_dsc_ct_2) | [RSA_DSC_CT_1](./pm/runs.md#rsa_dsc_ct_1) | [RSA_DSC_LA_1](./pm/runs.md#rsa_dsc_la_1) | [RSA_DSC_LA_5](./pm/runs.md#rsa_dsc_la_5) | [RSA_DSC_LA_3](./pm/runs.md#rsa_dsc_la_3) | [RSA_DSC_LA_4](./pm/runs.md#rsa_dsc_la_4) | [RSA_DSC_LA_2](./pm/runs.md#rsa_dsc_la_2)

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

- :fontawesome-solid-user-group: **Participant:** [Brown](./pm/participants.md#brown)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/Brown-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/Brown-PM.pdf)
- :material-file-search: **Runs:** [mnz](./pm/runs.md#mnz) | [sum](./pm/runs.md#sum) | [cubicmnz](./pm/runs.md#cubicmnz) | [cubicsumEW](./pm/runs.md#cubicsumew) | [cubicsumW](./pm/runs.md#cubicsumw) | [sumEW](./pm/runs.md#sumew) | [cubicsumWAbs](./pm/runs.md#cubicsumwabs) | [sumAbs](./pm/runs.md#sumabs) | [mnzAbs](./pm/runs.md#mnzabs) | [cubicmnzAbs](./pm/runs.md#cubicmnzabs)

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

- :fontawesome-solid-user-group: **Participant:** [Poznan](./pm/participants.md#poznan)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/Poznan-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/Poznan-PM.pdf)
- :material-file-search: **Runs:** [BB2_sq_nprf](./pm/runs.md#bb2_sq_nprf) | [BB2sqw2vprf](./pm/runs.md#bb2sqw2vprf) | [BB2_vq_noprf](./pm/runs.md#bb2_vq_noprf) | [BB2vqw2vprf](./pm/runs.md#bb2vqw2vprf) | [sq](./pm/runs.md#sq) | [bool51](./pm/runs.md#bool51)

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

- :fontawesome-solid-user-group: **Participant:** [InfoLabPM](./pm/participants.md#infolabpm)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/InfoLabPM-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/InfoLabPM-PM.pdf)
- :material-file-search: **Runs:** [minfolabBA](./pm/runs.md#minfolabba) | [minfolabBC](./pm/runs.md#minfolabbc) | [minfolabBD](./pm/runs.md#minfolabbd) | [minfolabTH](./pm/runs.md#minfolabth) | [tinfolabBF](./pm/runs.md#tinfolabbf) | [tinfolabBK](./pm/runs.md#tinfolabbk) | [tinfolabF](./pm/runs.md#tinfolabf)

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

- :fontawesome-solid-user-group: **Participant:** [cbnu](./pm/participants.md#cbnu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/cbnu-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/cbnu-PM.pdf)
- :material-file-search: **Runs:** [cbnuCT1](./pm/runs.md#cbnuct1) | [cbnuCT2](./pm/runs.md#cbnuct2) | [cbnuCT3](./pm/runs.md#cbnuct3) | [cbnuSA1](./pm/runs.md#cbnusa1) | [cbnuSA3](./pm/runs.md#cbnusa3) | [cbnuSA2](./pm/runs.md#cbnusa2)

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

- :fontawesome-solid-user-group: **Participant:** [MedIER](./pm/participants.md#medier)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/MedIER-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/MedIER-PM.pdf)
- :material-file-search: **Runs:** [MedIER_sa11](./pm/runs.md#medier_sa11) | [MedIER_sa12](./pm/runs.md#medier_sa12) | [MedIER_sa13](./pm/runs.md#medier_sa13) | [MedIER_sa14](./pm/runs.md#medier_sa14) | [MedIER_sa15](./pm/runs.md#medier_sa15)

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

- :fontawesome-solid-user-group: **Participant:** [imi_mug](./pm/participants.md#imi_mug)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/imi_mug-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/imi_mug-PM.pdf)
- :material-file-search: **Runs:** [imi_mug_abs1](./pm/runs.md#imi_mug_abs1) | [imi_mug_ct1](./pm/runs.md#imi_mug_ct1) | [imi_mug_abs2](./pm/runs.md#imi_mug_abs2) | [imi_mug_abs3](./pm/runs.md#imi_mug_abs3) | [imi_mug_abs4](./pm/runs.md#imi_mug_abs4) | [imi_mug_abs5](./pm/runs.md#imi_mug_abs5) | [imi_mug_ct2](./pm/runs.md#imi_mug_ct2) | [imi_mug_ct3](./pm/runs.md#imi_mug_ct3) | [imi_mug_ct4](./pm/runs.md#imi_mug_ct4) | [imi_mug_ct5](./pm/runs.md#imi_mug_ct5)

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

- :fontawesome-solid-user-group: **Participant:** [SINAI](./pm/participants.md#sinai)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/SINAI-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/SINAI-PM.pdf)
- :material-file-search: **Runs:** [SINAI_Base](./pm/runs.md#sinai_base) | [SINAI_FU](./pm/runs.md#sinai_fu) | [SINAI_FUO](./pm/runs.md#sinai_fuo)

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

- :fontawesome-solid-user-group: **Participant:** [UVA_ART](./pm/participants.md#uva_art)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/UVA_ART-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/UVA_ART-PM.pdf)
- :material-file-search: **Runs:** [UVAEXPBOOST](./pm/runs.md#uvaexpboost) | [UVAEXPBSTNEG](./pm/runs.md#uvaexpbstneg) | [UVAEXPBSTDIF](./pm/runs.md#uvaexpbstdif) | [UVAEXPBSTSHD](./pm/runs.md#uvaexpbstshd) | [UVAEXPBSTEXT](./pm/runs.md#uvaexpbstext)

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

- :fontawesome-solid-user-group: **Participant:** [KlickLabs](./pm/participants.md#klicklabs)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/KlickLabs-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/KlickLabs-PM.pdf)
- :material-file-search: **Runs:** [KLPM18T1Bl](./pm/runs.md#klpm18t1bl) | [KLPM18T2Bl](./pm/runs.md#klpm18t2bl) | [KL18AbsFuse](./pm/runs.md#kl18absfuse) | [KL18absHY](./pm/runs.md#kl18abshy) | [KL18absWV](./pm/runs.md#kl18abswv) | [KL18TrialBF](./pm/runs.md#kl18trialbf) | [KL18TriFuse](./pm/runs.md#kl18trifuse) | [KL18TriHY](./pm/runs.md#kl18trihy) | [KL18TrialWV](./pm/runs.md#kl18trialwv)

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

- :fontawesome-solid-user-group: **Participant:** [hpi-dhc](./pm/participants.md#hpi-dhc)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/hpi-dhc-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/hpi-dhc-PM.pdf)
- :material-file-search: **Runs:** [hpipubboost](./pm/runs.md#hpipubboost) | [hpictboost](./pm/runs.md#hpictboost) | [hpipubclass](./pm/runs.md#hpipubclass) | [hpipubnone](./pm/runs.md#hpipubnone) | [hpipubcommon](./pm/runs.md#hpipubcommon) | [hpipubbase](./pm/runs.md#hpipubbase) | [hpictall](./pm/runs.md#hpictall) | [hpictphrase](./pm/runs.md#hpictphrase) | [hpictcommon](./pm/runs.md#hpictcommon) | [hpictbase](./pm/runs.md#hpictbase)

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

- :fontawesome-solid-user-group: **Participant:** [PM_IBI](./pm/participants.md#pm_ibi)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/PM_IBI-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/PM_IBI-PM.pdf)
- :material-file-search: **Runs:** [PM_IBI_run1](./pm/runs.md#pm_ibi_run1) | [PM_IBI_run2](./pm/runs.md#pm_ibi_run2) | [PM_IBI_run3](./pm/runs.md#pm_ibi_run3)

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

- :fontawesome-solid-user-group: **Participant:** [UTDHLTRI](./pm/participants.md#utdhltri)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/UTDHLTRI-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/UTDHLTRI-PM.pdf)
- :material-file-search: **Runs:** [UTDHLTRI_RA](./pm/runs.md#utdhltri_ra) | [UTDHLTRI_RAT](./pm/runs.md#utdhltri_rat) | [UTDHLTRI_RF](./pm/runs.md#utdhltri_rf) | [UTDHLTRI_RFT](./pm/runs.md#utdhltri_rft) | [UTDHLTRI_NL](./pm/runs.md#utdhltri_nl) | [UTDHLTRI_NLT](./pm/runs.md#utdhltri_nlt) | [UTDHLTRI_SF](./pm/runs.md#utdhltri_sf) | [UTDHLTRI_SFT](./pm/runs.md#utdhltri_sft) | [UTDHLTRI_SS](./pm/runs.md#utdhltri_ss) | [UTDHLTRI_SST](./pm/runs.md#utdhltri_sst)

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

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./pm/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/udel_fang-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/udel_fang-PM.pdf)
- :material-file-search: **Runs:** [UDInfoPMCT1](./pm/runs.md#udinfopmct1) | [UDInfoPMCT2](./pm/runs.md#udinfopmct2) | [UDInfoPMCT3](./pm/runs.md#udinfopmct3) | [UDInfoPMCT4](./pm/runs.md#udinfopmct4) | [UDInfoPMCT5](./pm/runs.md#udinfopmct5) | [UDInfoPMSA1](./pm/runs.md#udinfopmsa1) | [UDInfoPMSA2](./pm/runs.md#udinfopmsa2) | [UDInfoPMSA3](./pm/runs.md#udinfopmsa3) | [UDInfoPMSA4](./pm/runs.md#udinfopmsa4) | [UDInfoPMSA5](./pm/runs.md#udinfopmsa5)

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

- :fontawesome-solid-user-group: **Participant:** [MayoNLPTeam](./pm/participants.md#mayonlpteam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/MayoNLPTeam-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/MayoNLPTeam-PM.pdf)
- :material-file-search: **Runs:** [mayomedsimp](./pm/runs.md#mayomedsimp) | [mayomedcomp](./pm/runs.md#mayomedcomp) | [mayomedcreat](./pm/runs.md#mayomedcreat) | [mayopubtator](./pm/runs.md#mayopubtator) | [mayoctsimp](./pm/runs.md#mayoctsimp) | [mayoctcomp](./pm/runs.md#mayoctcomp) | [mayoctscreat](./pm/runs.md#mayoctscreat)

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

- :fontawesome-solid-user-group: **Participant:** [UCAS](./pm/participants.md#ucas)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/UCAS-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/UCAS-PM.pdf)
- :material-file-search: **Runs:** [UCASSA1](./pm/runs.md#ucassa1) | [UCASSA2](./pm/runs.md#ucassa2) | [UCASSA3](./pm/runs.md#ucassa3) | [UCASSA4](./pm/runs.md#ucassa4) | [UCASSA5](./pm/runs.md#ucassa5) | [UCASCT1](./pm/runs.md#ucasct1) | [UCASCT2](./pm/runs.md#ucasct2) | [UCASCT3](./pm/runs.md#ucasct3) | [UCASCT4](./pm/runs.md#ucasct4) | [UCASCT5](./pm/runs.md#ucasct5)

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

- :fontawesome-solid-user-group: **Participant:** [Cat_Garfield](./pm/participants.md#cat_garfield)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/Cat_Garfield-PM.pdf](https://trec.nist.gov/pubs/trec27/papers/Cat_Garfield-PM.pdf)
- :material-file-search: **Runs:** [MSIIP_BASE](./pm/runs.md#msiip_base) | [MSIIP_PBAH](./pm/runs.md#msiip_pbah) | [MSIIP_PBH](./pm/runs.md#msiip_pbh) | [MSIIP_PBL](./pm/runs.md#msiip_pbl) | [MSIIP_PBPK](./pm/runs.md#msiip_pbpk) | [MSIIP_TRIAL1](./pm/runs.md#msiip_trial1) | [MSIIP_TRIAL2](./pm/runs.md#msiip_trial2) | [MSIIP_TRIAL3](./pm/runs.md#msiip_trial3) | [MSIIP_TRIAL4](./pm/runs.md#msiip_trial4) | [MSIIP_TRIAL5](./pm/runs.md#msiip_trial5)

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

## Common Core 

#### UWaterlooMDS at the TREC 2018 Common Core Track

_Mustafa Abualsaud, Gordon V. Cormack, Nimesh Ghelani, Amira Ghenai, Maura R. Grossman, Shahin Rahbariasl, Haotian Zhang, Mark D. Smucker_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./core/participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/UWaterlooMDS-CC.pdf](https://trec.nist.gov/pubs/trec27/papers/UWaterlooMDS-CC.pdf)
- :material-file-search: **Runs:** [UWaterMDS_DS_A](./core/runs.md#uwatermds_ds_a) | [UWaterMDS_DS_B](./core/runs.md#uwatermds_ds_b) | [UWaterMDS_Rank](./core/runs.md#uwatermds_rank) | [UWaterMDS_SEQ](./core/runs.md#uwatermds_seq)

??? abstract "Abstract"
	
	This year we applied dynamic sampling (DS) [ 4] to create a sampled set of relevance judgments. One goal was to test the effectiveness and efficiency of this technique with a set of non-expert, secondary relevance assessors. We consider NIST assessors to be the experts and the primary assessors. Another goal was to make available to other researchers a sampled set of relevance judgments (prels) and thus allow the estimation of retrieval metrics that have the potential to be more robust than the standard NIST provided relevance judgments (qrels). In addition to creating the prels, we also submied several runs based on our manual judging and the models produced by our HiCAL system [1, 6].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbualsaudCGGGRZ18.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbualsaudCGGGRZ18,
		author = {Mustafa Abualsaud and Gordon V. Cormack and Nimesh Ghelani and Amira Ghenai and Maura R. Grossman and Shahin Rahbariasl and Haotian Zhang and Mark D. Smucker},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UWaterlooMDS at the {TREC} 2018 Common Core Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/UWaterlooMDS-CC.pdf},
		timestamp = {Wed, 03 Feb 2021 08:31:25 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AbualsaudCGGGRZ18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Expansion Based on NLP and Word Embeddings

_Billel Aklouche, Ibrahim Bounhas, Yahya Slimani_

- :fontawesome-solid-user-group: **Participant:** [JARIR](./core/participants.md#jarir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/JARIR-CC.pdf](https://trec.nist.gov/pubs/trec27/papers/JARIR-CC.pdf)
- :material-file-search: **Runs:** [jarir_cb_re](./core/runs.md#jarir_cb_re) | [jarir_cbow](./core/runs.md#jarir_cbow) | [jarir_sg_re](./core/runs.md#jarir_sg_re) | [jarir_skipgram](./core/runs.md#jarir_skipgram) | [jarir_cb_ind](./core/runs.md#jarir_cb_ind) | [jarir_sg_ind](./core/runs.md#jarir_sg_ind)

??? abstract "Abstract"
	
	Query Expansion is an important process in information retrieval, which consists in adding new related terms to the original query in order to better identify relevant documents. In this paper, we discuss the participation of the JARIR research group to the TREC 2018 Common Core Track. We present different Query Expansion methods, which are based on Natural Language Pre-processing (NLP) tools and Word2Vec embedding models. Using the title of TREC topics, we select semantically related terms to the query. Our approach is composed of four steps: (1) Data Pre-processing, (2) Model Training, (3) Query Expansion and (4) Documents Ranking. For our best runs, results show that most of our topics scores are above the published median scores with some topics having the best scores.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AkloucheBSABSAB18.bib) "
	```
	@inproceedings{DBLP:conf/trec/AkloucheBSABSAB18,
		author = {Billel Aklouche and Ibrahim Bounhas and Yahya Slimani},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Query Expansion Based on {NLP} and Word Embeddings},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/JARIR-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AkloucheBSABSAB18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT at the 2018 TREC CORE Track

_Rodger Benham, Luke Gallagher, Joel M. Mackenzie, Binsheng Liu, Xiaolu Lu, Falk Scholer, J. Shane Culpepper, Alistair Moffat_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./core/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/RMIT-CC.pdf](https://trec.nist.gov/pubs/trec27/papers/RMIT-CC.pdf)
- :material-file-search: **Runs:** [RMITUQVDBFDM3](./core/runs.md#rmituqvdbfdm3) | [RMITUQVDBFNZDM1](./core/runs.md#rmituqvdbfnzdm1) | [RMITUQVBestDM2](./core/runs.md#rmituqvbestdm2) | [RMITFDA4](./core/runs.md#rmitfda4) | [RMITEXTGIGADA5](./core/runs.md#rmitextgigada5)

??? abstract "Abstract"
	
	Ad-hoc retrieval is an important problem with many practical applications. It forms the basis of web search, question-answering, and a new generation of virtual assistants being developed by several of the largest software companies in the world. In this report, we continue our exploration of the importance of multiple expressions of information needs. Our thesis is that over-reliance on a single query can lead to suboptimal performance, and that by creating multiple query representations for an information need and combining the relevance signals through fusion and relevance modeling, highly effective systems can be produced. This approach may form the basis for more complex multi-stage retrieval systems in a variety of applications.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BenhamGML0SCM18.bib) "
	```
	@inproceedings{DBLP:conf/trec/BenhamGML0SCM18,
		author = {Rodger Benham and Luke Gallagher and Joel M. Mackenzie and Binsheng Liu and Xiaolu Lu and Falk Scholer and J. Shane Culpepper and Alistair Moffat},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{RMIT} at the 2018 {TREC} {CORE} Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/RMIT-CC.pdf},
		timestamp = {Mon, 26 Apr 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BenhamGML0SCM18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2018: Common Core Track

_Alexander Bondarenko, Matthias Hagen, Michael Völske, Benno Stein, Alexander Panchenko, Chris Biemann_

- :fontawesome-solid-user-group: **Participant:** [Webis](./core/participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/Webis-CC.pdf](https://trec.nist.gov/pubs/trec27/papers/Webis-CC.pdf)
- :material-file-search: **Runs:** [webis-argument](./core/runs.md#webis-argument) | [webis-bm25f](./core/runs.md#webis-bm25f) | [webis-baseline](./core/runs.md#webis-baseline)

??? abstract "Abstract"
	
	This paper gives a brief overview of the Webis network's participation in the TREC 2018 Common Core track. The basic idea applied in our approach is to axiomatically re-rank the top-50 results of BM25F for those topics that seem to be argumentative. To this end, we use three axioms with the goal of covering some aspects of argumentativeness in text documents. If all three argumentative axioms favor a re-ordering of two documents, they “overrule” the initial ranking and the documents change their ranks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BondarenkoHVSPB18.bib) "
	```
	@inproceedings{DBLP:conf/trec/BondarenkoHVSPB18,
		author = {Alexander Bondarenko and Matthias Hagen and Michael V{\"{o}}lske and Benno Stein and Alexander Panchenko and Chris Biemann},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2018: Common Core Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/Webis-CC.pdf},
		timestamp = {Fri, 19 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BondarenkoHVSPB18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FEUP at TREC 2018 Common Core Track - Reranking for Diversity  using Hypergraph-of-Entity and Document Profiling

_José Luís Devezas, Sérgio Nunes, Antonio Guillén, Yoan Gutiérrez, Rafael Muñoz_

- :fontawesome-solid-user-group: **Participant:** [FEUP](./core/participants.md#feup)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/FEUP-CC.pdf](https://trec.nist.gov/pubs/trec27/papers/FEUP-CC.pdf)
- :material-file-search: **Runs:** [feup-run1](./core/runs.md#feup-run1) | [feup-run2](./core/runs.md#feup-run2) | [feup-run3](./core/runs.md#feup-run3) | [feup-run5](./core/runs.md#feup-run5) | [feup-run7](./core/runs.md#feup-run7) | [feup-run8](./core/runs.md#feup-run8) | [feup-run4](./core/runs.md#feup-run4) | [feup-run6](./core/runs.md#feup-run6)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2018 Common Core track, where we experimented with hyperedge-based document ranking, over the hypergraph-of-entity. We compared a text-only implementation (feup-run1) with a different implementation that also included entities and triples from DBpedia (feup-run2). We also experimented with reranking for diversity, based on the maximal marginal relevance and document profiling, in order to find a balance between relevance and the dissimilarity of neighboring documents. This resulted in six additional runs (3 to 8), using feup-run1 and feup-run2 as the base runs for reranking. We then assessed the impact in effectiveness, along with the changes in diversity, particularly over the top-ranked documents. We evaluated retrieval effectiveness based on the mean average precision, over the relevance judgments provided by TREC. We also proposed a weighted diversity metric, based on the cosine distance between each document and all others, within results for the same topic. Documents with a lower rank were assigned a higher weight, more strongly contributing to the weighted diversity. Our best results were for feup-run1 and feup-run7, both with a MAP score of 0.0070 and a P@10 of 0.0680, as well as a weighted diversity of 0.1197 and 0.1218, respectively.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DevezasNGGM18.bib) "
	```
	@inproceedings{DBLP:conf/trec/DevezasNGGM18,
		author = {Jos{\'{e}} Lu{\'{\i}}s Devezas and S{\'{e}}rgio Nunes and Antonio Guill{\'{e}}n and Yoan Guti{\'{e}}rrez and Rafael Mu{\~{n}}oz},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{FEUP} at {TREC} 2018 Common Core Track - Reranking for Diversity using Hypergraph-of-Entity and Document Profiling},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/FEUP-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DevezasNGGM18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Improving Ad Hoc Retrieval With Bag Of Entities

_Gustavo Gonçalves, João Magalhães, Chenyan Xiong, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [NOVASearch](./core/participants.md#novasearch)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/NOVASearch-CC.pdf](https://trec.nist.gov/pubs/trec27/papers/NOVASearch-CC.pdf)
- :material-file-search: **Runs:** [bt-BoWBoE](./core/runs.md#bt-bowboe) | [bt-BoW](./core/runs.md#bt-bow) | [bt-BoE](./core/runs.md#bt-boe) | [b-BoE](./core/runs.md#b-boe) | [t-BoE](./core/runs.md#t-boe) | [eb-boost](./core/runs.md#eb-boost) | [b-BoW](./core/runs.md#b-bow) | [b-BoWBoE-t-BoE](./core/runs.md#b-bowboe-t-boe) | [b-BoW-t-BoWBoE](./core/runs.md#b-bow-t-bowboe) | [BM25-b-BoW](./core/runs.md#bm25-b-bow)

??? abstract "Abstract"
	
	This work explores the value of entity information for improving a feature-based learning-to-rank search engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GoncalvesMXC18.bib) "
	```
	@inproceedings{DBLP:conf/trec/GoncalvesMXC18,
		author = {Gustavo Gon{\c{c}}alves and Jo{\~{a}}o Magalh{\~{a}}es and Chenyan Xiong and Jamie Callan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Improving Ad Hoc Retrieval With Bag Of Entities},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/NOVASearch-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GoncalvesMXC18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MRG_UWaterloo Participation in the TREC 2018 Common Core Track

_Maura R. Grossman, Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [MRG_UWaterloo](./core/participants.md#mrg_uwaterloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/MRG_UWaterloo-CC.pdf](https://trec.nist.gov/pubs/trec27/papers/MRG_UWaterloo-CC.pdf)
- :material-file-search: **Runs:** [uwmrg](./core/runs.md#uwmrg) | [uwmrgx](./core/runs.md#uwmrgx)

??? abstract "Abstract"
	
	The MRG_UWaterloo team from the University of Waterloo participated in the TREC 2018 Common Core Track. We used logistic regression to score and rank all documents from the Washington Post dataset, using pseudo-relevant and pseudo-nonrelevant training documents fetched from the Web using Google search. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanC18.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanC18,
		author = {Maura R. Grossman and Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {MRG{\_}UWaterloo Participation in the {TREC} 2018 Common Core Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/MRG\_UWaterloo-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanC18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### H2oloo at TREC 2018: Cross-Collection Relevance Transfer for the  Common Core Track

_Ruifan Yu, Yuhao Xie, Jimmy Lin_

- :fontawesome-solid-user-group: **Participant:** [h2oloo](./core/participants.md#h2oloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/h2oloo-CC.pdf](https://trec.nist.gov/pubs/trec27/papers/h2oloo-CC.pdf)
- :material-file-search: **Runs:** [h2oloo_LR2AX0.6](./core/runs.md#h2oloo_lr2ax0.6) | [h2oloo_enax0.6](./core/runs.md#h2oloo_enax0.6) | [h2oloo_enax0.7](./core/runs.md#h2oloo_enax0.7) | [h2oloo_LR2_rm3](./core/runs.md#h2oloo_lr2_rm3) | [h2oloo_LRax0.6](./core/runs.md#h2oloo_lrax0.6) | [h2oloo_enrm30.6](./core/runs.md#h2oloo_enrm30.6) | [h2oloo_e7ax0.6](./core/runs.md#h2oloo_e7ax0.6) | [h2oloo_e7ax0.7](./core/runs.md#h2oloo_e7ax0.7) | [h2oloo_e7rm30.6](./core/runs.md#h2oloo_e7rm30.6) | [h2oloo_e7rm30.7](./core/runs.md#h2oloo_e7rm30.7)

??? abstract "Abstract"
	
	The h2oloo team at the University of Waterloo participated in the Common Core Track in TREC 2018. Our main effort involved reproducing the cross-collection relevance transfer technique of Grossman and Cormack [ 8 ] from the TREC 2017 Common Core Track, as captured in their WCrobust0405 run. Their idea was relatively simple: for information needs (topics) that are shared across more than one test collection, it is possible to train (per topic) relevance classifiers using one or more test collections (in their case, from the TREC 2004 and 2005 Robust Tracks) and apply the classifiers to a new document collection (in their case, the New York Times collection used in the TREC 2017 Common Core Track) to improve ranking effectiveness. Each classifier, in essence, learns a relevance model for a specific information need, and the experiments of Grossman and Cormack demonstrate that such models can generalize across document collections. According to the TREC 2017 Common Core Track overview paper [ 2 ], WCrobust0405 ranked third in terms of average precision of runs that contributed to the judgment pools. The two runs that were more effective than WCrobust0405 involved humans who interactively searched the target collection to find relevant documents. In other words, the relevance transfer technique yielded effectiveness levels that approach human searchers. Not only is the technique of Grossman and Cormack effective, it is also simple: According to their paper, a logistic regression classifier for each topic was trained on the union of relevance judgments from the TREC 2004 and 2005 Robust Tracks. Documents were represented using word-level tf-idf features and each logistic regression classifier was learned using Sofia-ML1 and then applied to the entire Common Core collection. The top 10000 scoring documents (per topic), in decreasing order of classifier score, was submitted as the final run. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YuXL18.bib) "
	```
	@inproceedings{DBLP:conf/trec/YuXL18,
		author = {Ruifan Yu and Yuhao Xie and Jimmy Lin},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {H2oloo at {TREC} 2018: Cross-Collection Relevance Transfer for the Common Core Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/h2oloo-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YuXL18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Anserini at trec 2018: Centre, Common Core, and News Tracks

_Yang, Peilin, Lin, Jimmy_

- :fontawesome-solid-user-group: **Participant:** [Anserini](./core/participants.md#anserini)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/anserini-CTR-CC-N.pdf](https://trec.nist.gov/pubs/trec27/papers/anserini-CTR-CC-N.pdf)
- :material-file-search: **Runs:** [anserini_ax](./core/runs.md#anserini_ax) | [anserini_ax17](./core/runs.md#anserini_ax17) | [anserini_sdm](./core/runs.md#anserini_sdm) | [anserini_rm3](./core/runs.md#anserini_rm3) | [anserini_bm25](./core/runs.md#anserini_bm25) | [anserini_qlax](./core/runs.md#anserini_qlax) | [anserini_qlax17](./core/runs.md#anserini_qlax17) | [anserini_qlsdm](./core/runs.md#anserini_qlsdm) | [anserini_qlrm3](./core/runs.md#anserini_qlrm3) | [anserini_ql](./core/runs.md#anserini_ql)

??? abstract "Abstract"
	
	Anserini is an open-source information retrieval toolkit built on Lucene [3, 4]. The goal of our effort is to support information retrieval research using the popular open-source Lucene search library by allowing researchers to easily replicate results with modern ranking models on diverse test collections. Although there are many open-source search engines developed and maintained by academic research groups, most of them are designed primarily to facilitate the publication of research papers, and as such, they often suffer from poor usability, incomplete documentation, and a host of other issues. The growing complexity of modern software ecosystems and the diverse capabilities that are required to build useful end-to-end search applications places academic research groups at a huge disadvantage relative to Lucene. Except for a handful of commercial web search engines that deploy custom infrastructure, Lucene has become the de facto platform in industry for building production search applications—used by organizations as diverse as Twitter, Reddit, Bloomberg, and Target. It has an active developer base, diverse features and capabilities, and lies at the center of a vibrant ecosystem. However, Lucene lacks systematic support for information retrieval research—in particu- lar, ad hoc experimentation using standard test collections. This is where Anserini comes in: we enable cutting-edge information retrieval research using Lucene. At TREC 2018, we participated in the CENTRE, Common Core, and News Tracks. Each is described in its own section below. Our development efforts centered around the v0.1.0 release of Anserini, which is based on Lucene 6.3.0 (not the latest release).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/) "
	```
	@inproceedings{yang2018anserini,
		title = {Anserini at trec 2018: Centre, Common Core, and News Tracks},
		author = {Yang, Peilin and Lin, Jimmy},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference (TREC 2018), Gaithersburg, MD},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/anserini-CTR-CC-N.pdf},
		biburl = {https://dblp.org/}
	}
	```

#### UMass at TREC 2018: CAR, Common Core and News Tracks

_Shahrzad Naseri, John Foley, James Allan_

- :fontawesome-solid-user-group: **Participant:** [UMass](./core/participants.md#umass)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/UMass-CAR-CC-N.pdf](https://trec.nist.gov/pubs/trec27/papers/UMass-CAR-CC-N.pdf)
- :material-file-search: **Runs:** [umass_cbsdm](./core/runs.md#umass_cbsdm) | [umass_bsdm](./core/runs.md#umass_bsdm) | [umass_sdm](./core/runs.md#umass_sdm) | [umass_ql](./core/runs.md#umass_ql)

??? abstract "Abstract"
	
	UMass participated in three TREC tasks in 2018: the TREC CAR, TREC Core tasks and TREC News (Background Linking). In this paper we detail the contents of our submissions and our lessons learned from this year's participation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NaseriFA18.bib) "
	```
	@inproceedings{DBLP:conf/trec/NaseriFA18,
		author = {Shahrzad Naseri and John Foley and James Allan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UMass at {TREC} 2018: CAR, Common Core and News Tracks},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/UMass-CAR-CC-N.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NaseriFA18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Real-time Summarization 

#### Overview of the TREC 2018 Real-Time Summarization Track

_Royal Sequiera, Luchen Tan, Jimmy Lin_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/Overview-RTS.pdf](https://trec.nist.gov/pubs/trec27/papers/Overview-RTS.pdf)
??? abstract "Abstract"
	
	The TREC 2018 Real-Time Summarization (RTS) Track is the third iteration of a community effort to explore techniques, algorithms, and systems that automatically monitor streams of social media posts such as tweets on Twier to address users' prospective information needs. These needs are articulated as “interest profiles”, akin to topics in ad hoc retrieval. In our formulation of real-time summarization, the goal is for a system to deliver relevant and novel content to users in a timely fashion. We refer to these messages generically as “updates”. As with previous iterations of the evaluation, the task setup required participating systems to monitor the live Twier sample stream during a pre-defined evaluation period, this year beginning Monday July 23, 2018 00:00:00 UTC and ending Friday August 3, 2018 23:59:59 UTC. The interest profiles were distributed to participants ahead of time. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SequieraTL18.bib) "
	```
	@inproceedings{DBLP:conf/trec/SequieraTL18,
		author = {Royal Sequiera and Luchen Tan and Jimmy Lin},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2018 Real-Time Summarization Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/Overview-RTS.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SequieraTL18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC Real-Time Summarization 2018

_Abdelhamid Chellal, Mohand Boughanem_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./rts/participants.md#irit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/IRIT-RT.pdf](https://trec.nist.gov/pubs/trec27/papers/IRIT-RT.pdf)
- :material-file-search: **Runs:** [IRIT-RunB3](./rts/runs.md#irit-runb3) | [IRIT-RunB1](./rts/runs.md#irit-runb1) | [IRIT-RunB2](./rts/runs.md#irit-runb2) | [IRIT-IRIT-Run1-06](./rts/runs.md#irit-irit-run1-06) | [IRIT-IRIT-Run2-07](./rts/runs.md#irit-irit-run2-07) | [IRIT-IRIT-Run3-08](./rts/runs.md#irit-irit-run3-08)

??? abstract "Abstract"
	
	This paper presents the participation of the IRIT laboratory (University of Toulouse) to the Real-Time Summarization track of TREC RTS 2018. This track is consisting of two scenarios ( A: push notification and B: Email digest) which tackle the challenge of fulfilling the prospective and the retrospection information needs repressively. We submitted three runs for both scenarios A and B. For scenario A, we propose to use a supervised learning approach to build a binary classifier that predicts the relevance of an incoming tweet with respect to the topic of interest. The proposed approach leverages social signals as well as query dependent features to enhance the detection of relevant tweets. Additionally, we investigate the impact of the use of live relevance feedback to re-train the classier each time new relevance assessments are made available. For scenario B, the daily digest is generated by iteratively selecting the top tweets that pass the relevance filter with discarding the redundant ones.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChellalB18.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChellalB18,
		author = {Abdelhamid Chellal and Mohand Boughanem},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IRIT} at {TREC} Real-Time Summarization 2018},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/IRIT-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChellalB18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### GPLSI at TREC 2018 RTS Track

_Javi Fernández, Fernando Llopis, Yoan Gutiérrez, Patricio Martínez-Barco, José M. Gómez, Rafael Muñoz_

- :fontawesome-solid-user-group: **Participant:** [UA-Gplsi](./rts/participants.md#ua-gplsi)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/UA-GPLSI-RT.pdf](https://trec.nist.gov/pubs/trec27/papers/UA-GPLSI-RT.pdf)
- :material-file-search: **Runs:** [IR-N](./rts/runs.md#ir-n) | [IR-NR1](./rts/runs.md#ir-nr1) | [IR-NR2](./rts/runs.md#ir-nr2) | [UA_GPLSI-GPLSI-runA1-13](./rts/runs.md#ua_gplsi-gplsi-runa1-13) | [UA_GPLSI-GPLSI-runA2-14](./rts/runs.md#ua_gplsi-gplsi-runa2-14) | [UA_GPLSI-GPLSI-runA3-15](./rts/runs.md#ua_gplsi-gplsi-runa3-15)

??? abstract "Abstract"
	
	n this paper we present our contribution for the TREC 2018 Real-Time Summarization track. This task contains two scenarios: push notifications, and email digest. We participated in both, submitting three runs on each one. Our main goal was to evaluate the effectiveness the techniques employed in Social Analytics, a reputation analysis platform, which finds relevant tweets for specific topics. Here, we describe these techniques, and discuss the results obtained
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FernandezLGMG018.bib) "
	```
	@inproceedings{DBLP:conf/trec/FernandezLGMG018,
		author = {Javi Fern{\'{a}}ndez and Fernando Llopis and Yoan Guti{\'{e}}rrez and Patricio Mart{\'{\i}}nez{-}Barco and Jos{\'{e}} M. G{\'{o}}mez and Rafael Mu{\~{n}}oz},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{GPLSI} at {TREC} 2018 {RTS} Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/UA-GPLSI-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FernandezLGMG018.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Complex Answer Retrieval 

#### TREC Complex Answer Retrieval Overview

_Laura Dietz, Ben Gamari, Jeff Dalton, Nick Craswell_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/Overview-CAR.pdf](https://trec.nist.gov/pubs/trec27/papers/Overview-CAR.pdf)
??? abstract "Abstract"
	
	This notebook gives an overview of activities, datasets, and results of the second year of TREC Complex Answer Retrieval. We lay out the tasks offered and how provided datasets are automatically derived from Wikipedia and TQA. Manual relevance assessments are created by NIST. We describe the details of the assessment procedures, inter-annotator agreement, and statistics. Nine teams submitted runs exploring interactions of entities and passages, neural as well as traditional retrieval methods. We see that combining traditional methods with learning-to-rank can outperform neural methods, even when many training queries are available.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DietzG0C18.bib) "
	```
	@inproceedings{DBLP:conf/trec/DietzG0C18,
		author = {Laura Dietz and Ben Gamari and Jeff Dalton and Nick Craswell},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} Complex Answer Retrieval Overview},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/Overview-CAR.pdf},
		timestamp = {Tue, 21 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DietzG0C18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CUIS Team at TREC 2018 CAR Track

_Xinshi Lin, Wai Lam_

- :fontawesome-solid-user-group: **Participant:** [CUIS](./car/participants.md#cuis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/CUIS-CAR.pdf](https://trec.nist.gov/pubs/trec27/papers/CUIS-CAR.pdf)
- :material-file-search: **Runs:** [CUIS-F150](./car/runs.md#cuis-f150) | [CUIS-MX5](./car/runs.md#cuis-mx5) | [CUIS-Swift](./car/runs.md#cuis-swift) | [CUIS-dogeDodge](./car/runs.md#cuis-dogedodge) | [CUIS-XTS](./car/runs.md#cuis-xts)

??? abstract "Abstract"
	
	We participated in the Complex Answer Retrieval(CAR) Track at TREC 2018. We propose a Markov random field based framework concerning unigrams, bigrams and concepts from differnt query sections. Besides, we employ a language modelling framework facilitating the Wikipedia article information and query entity mentions. Our best passage run achieves NDCG@5 of 0.3503 and MAP of 0.1715.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinL18.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinL18,
		author = {Xinshi Lin and Wai Lam},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CUIS} Team at {TREC} 2018 {CAR} Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/CUIS-CAR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinL18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Trec-CAR 2018: A Simple Unsupervised Semantic Query Expansion Model

_Robert Litschko, Federico Nanni, Goran Glavas_

- :fontawesome-solid-user-group: **Participant:** [DWS-UMA](./car/participants.md#dws-uma)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/DWS-UMA-CAR.pdf](https://trec.nist.gov/pubs/trec27/papers/DWS-UMA-CAR.pdf)
- :material-file-search: **Runs:** [DWS-UMA-SemqQueryExp](./car/runs.md#dws-uma-semqqueryexp) | [DWS-UMA-SemqQueryExp20](./car/runs.md#dws-uma-semqqueryexp20) | [DWS-UMA-SemqQueryExp30](./car/runs.md#dws-uma-semqqueryexp30) | [DWS-UMA-EntAspBM25none](./car/runs.md#dws-uma-entaspbm25none) | [DWS-UMA-EntAspQLrm](./car/runs.md#dws-uma-entaspqlrm)

??? abstract "Abstract"
	
	In this summary we present a simple and unsupervised Semantic Query Expansion model (SemQueryExp) for Complex Answer Retrieval (CAR). TREC CAR is a large-scale information retrieval shared evaluation task based on Wikipedia content. We have participated in the Passage Ranking Task of TREC CAR. Queries are provided as hierarchical section outlines and the goal is to retrieve the relevant paragraph, i.e., the original Wikipedia paragraphs of the respective section. The queries consist of the page title in which the section appears, the name of the main section and one or more sub-level sections (e.g., Thompson Capper // Early career // South African service). A section in turn contains a number of terms that we want to use in order to expand the query with semantically related terms. Here we rely on 300-dimensional GloVe [1] word embeddings, pre-trained on Wikipedia. For each word in the query we lookup its embedding, search for the k-nearest-neighbors and add the corresponding words to the query. Distances between word embeddings are measured with the cosine similarity. The final query consists now of its original query terms as well as the words added during query expansion. We assume that words appearing in lower sub-section levels, i.e. more specific sections, capture more relevance for the query than words appearing on higher levels such as the page title, which only describe the surrounding theme. This is encoded by assigning each query term a weight according to it's level in the hierarchical outline. If a word is in the title it receives a weight of 1, if it is in the main section it receives a weight of 2, etc. Expanded query terms are assumed to be noisy and scored with a value ranging between 0 and 1, depending on their cosine similarity. The final query consists of the union of all terms appearing in the outline and the expanded query terms, coupled with respective weights. All data is normalized by removing stop words and applying lemmatization. We execute the query on a Lucene index as a BoostedQuery using the BM25 retrieval model. We used no external data and we tuned the value of the parameter k on the benchmarkY1-train portion of the TREC CAR dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LitschkoNG18.bib) "
	```
	@inproceedings{DBLP:conf/trec/LitschkoNG18,
		author = {Robert Litschko and Federico Nanni and Goran Glavas},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Trec-CAR 2018: {A} Simple Unsupervised Semantic Query Expansion Model},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/DWS-UMA-CAR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LitschkoNG18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PACRR Gated Expansion for TREC CAR 2018

_Sean MacAvaney, Nazli Goharian, Ophir Frieder, Andrew Yates_

- :fontawesome-solid-user-group: **Participant:** [GUIR](./car/participants.md#guir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/GUIR-CAR.pdf](https://trec.nist.gov/pubs/trec27/papers/GUIR-CAR.pdf)
- :material-file-search: **Runs:** [guir](./car/runs.md#guir) | [guir-exp](./car/runs.md#guir-exp)

??? abstract "Abstract"
	
	In this work, we present our approach to the 2018 TREC Complex Answer Retrieval (CAR) task. We submitted two passage retrieval runs. The first uses the state-of-the-art technique from TREC CAR 2017: a modified neural ranker modified to incorporate query heading frequency information while performing term matching on each heading independently. The second run incorporates a novel gated technique for incorporating query expansion terms in a neural ranker. Our TREC runs indicate significant performance improvements can be achieved when using the expansion approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacAvaneyGFY18.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacAvaneyGFY18,
		author = {Sean MacAvaney and Nazli Goharian and Ophir Frieder and Andrew Yates},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{PACRR} Gated Expansion for {TREC} {CAR} 2018},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/GUIR-CAR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacAvaneyGFY18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UTD HLTRI at TREC 2018: Complex Answer Retrieval Track

_Ramón Maldonado, Sanda M. Harabagiu_

- :fontawesome-solid-user-group: **Participant:** [UTDHLTRI](./car/participants.md#utdhltri)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/UTDHLTRI-CAR.pdf](https://trec.nist.gov/pubs/trec27/papers/UTDHLTRI-CAR.pdf)
- :material-file-search: **Runs:** [UTDHLTRI2](./car/runs.md#utdhltri2)

??? abstract "Abstract"
	
	Finding answers to complex questions within a corpus of Wikipedia paragraphs needs to account for (a) the similarity between questions and paragraphs as well as (b) their shared semantics. In our participation in the 2018 TREC CAR track, we focused on developing a novel neural paragraph ranking model in our existing CAPAR system, developed for the 2017 TREC CAR track. The new system TRANS-CAPAR, takes advantage of the recently introduced Transformer architecture to encode information from the question and to semantically decode it in each paragraph. The results obtained during the official evaluations indicate that TRANSCAPAR makes good use of both discourse context and similarity when ranking paragraphs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MaldonadoH18.bib) "
	```
	@inproceedings{DBLP:conf/trec/MaldonadoH18,
		author = {Ram{\'{o}}n Maldonado and Sanda M. Harabagiu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UTD} {HLTRI} at {TREC} 2018: Complex Answer Retrieval Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/UTDHLTRI-CAR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MaldonadoH18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### New York University at TREC 2018 Complex Answer Retrieval Track

_Rodrigo Frassetto Nogueira, Kyunghyun Cho_

- :fontawesome-solid-user-group: **Participant:** [NYU-DL](./car/participants.md#nyu-dl)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/NYU-DL-CAR.pdf](https://trec.nist.gov/pubs/trec27/papers/NYU-DL-CAR.pdf)
- :material-file-search: **Runs:** [NYU-L](./car/runs.md#nyu-l) | [NYU-M](./car/runs.md#nyu-m) | [NYU-XL](./car/runs.md#nyu-xl)

??? abstract "Abstract"
	
	In this paper, we describe our submission to the TREC-CAR 2018. We use a method introduced by Nogueira et al. (2018) to efficiently learn diverse strategies in reinforcement learning for query reformulation and focus minimally on the ranking function. In this framework, an agent consists of multiple specialized sub-agents and a meta-agent that learns to aggregate the answers from sub-agents to produce a final answer. Sub-agents are trained on disjoint partitions of the training data, while the meta-agent is trained on the full training set. Our method makes learning faster, because it is highly parallelizable, and has better generalization performance than strong baselines, such as an ensemble of agents trained on the full data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NogueiraC18.bib) "
	```
	@inproceedings{DBLP:conf/trec/NogueiraC18,
		author = {Rodrigo Frassetto Nogueira and Kyunghyun Cho},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {New York University at {TREC} 2018 Complex Answer Retrieval Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/NYU-DL-CAR.pdf},
		timestamp = {Fri, 20 May 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NogueiraC18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREMA-UNH at TREC 2018: Complex Answer Retrieval and News Track

_Sumanta Kashyapi, Shubham Chatterjee, Jordan Ramsdell, Laura Dietz_

- :fontawesome-solid-user-group: **Participant:** [trema-unh](./car/participants.md#trema-unh)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/TREMA-UNH-CAR-N.pdf](https://trec.nist.gov/pubs/trec27/papers/TREMA-UNH-CAR-N.pdf)
- :material-file-search: **Runs:** [UNH-p-mixed](./car/runs.md#unh-p-mixed) | [UNH-p-l2r](./car/runs.md#unh-p-l2r) | [UNH-p-sdm](./car/runs.md#unh-p-sdm) | [UNH-e-mixed](./car/runs.md#unh-e-mixed) | [UNH-e-graph](./car/runs.md#unh-e-graph) | [UNH-e-L2R](./car/runs.md#unh-e-l2r)

??? abstract "Abstract"
	
	This notebook describes the submission of team TREMA-UNH to the TREC Complex Answer Retrieval track and the TREC News track in 2018. Our methods focus on passage retrieval, entity-aware passage retrieval, and entity retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KashyapiCRD18.bib) "
	```
	@inproceedings{DBLP:conf/trec/KashyapiCRD18,
		author = {Sumanta Kashyapi and Shubham Chatterjee and Jordan Ramsdell and Laura Dietz},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREMA-UNH} at {TREC} 2018: Complex Answer Retrieval and News Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/TREMA-UNH-CAR-N.pdf},
		timestamp = {Tue, 21 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KashyapiCRD18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2018: CAR, Common Core and News Tracks

_Shahrzad Naseri, John Foley, James Allan_

- :fontawesome-solid-user-group: **Participant:** [UMass](./car/participants.md#umass)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/UMass-CAR-CC-N.pdf](https://trec.nist.gov/pubs/trec27/papers/UMass-CAR-CC-N.pdf)
- :material-file-search: **Runs:** [entityEmbedLambdaMart](./car/runs.md#entityembedlambdamart)

??? abstract "Abstract"
	
	UMass participated in three TREC tasks in 2018: the TREC CAR, TREC Core tasks and TREC News (Background Linking). In this paper we detail the contents of our submissions and our lessons learned from this year's participation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NaseriFA18.bib) "
	```
	@inproceedings{DBLP:conf/trec/NaseriFA18,
		author = {Shahrzad Naseri and John Foley and James Allan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UMass at {TREC} 2018: CAR, Common Core and News Tracks},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/UMass-CAR-CC-N.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NaseriFA18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## News 

#### TREC 2018 News Track Overview

_Ian Soboroff, Shudong Huang, Donna Harman_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/Overview-News.pdf](https://trec.nist.gov/pubs/trec27/papers/Overview-News.pdf)
??? abstract "Abstract"
	
	The News track is a new track for TREC 2019, focused on information retrieval in the service of helping people read the news. In cooperation with the Washington Post1, we released a new collection of 600,000 news articles, and crafted two tasks related to how news is presented on the web.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SoboroffHH18.bib) "
	```
	@inproceedings{DBLP:conf/trec/SoboroffHH18,
		author = {Ian Soboroff and Shudong Huang and Donna Harman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2018 News Track Overview},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/Overview-News.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SoboroffHH18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### htw saar @ TREC 2018 News Track

_Agra Bimantara, Michelle Blau, Kevin Engelhardt, Johannes Gerwert, Tobias Gottschalk, Philipp Lukosz, Shenna Piri, Nima Saken Shaft, Klaus Berberich_

- :fontawesome-solid-user-group: **Participant:** [htwsaar](./news/participants.md#htwsaar)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/htwsaar-N.pdf](https://trec.nist.gov/pubs/trec27/papers/htwsaar-N.pdf)
- :material-file-search: **Runs:** [htwsaar1](./news/runs.md#htwsaar1) | [htwsaar2](./news/runs.md#htwsaar2) | [htwsaar3](./news/runs.md#htwsaar3) | [htwsaar4](./news/runs.md#htwsaar4)

??? abstract "Abstract"
	
	This paper describes our participation in the background linking task of the TREC 2018 News Track. We explored four different methods to address the task. All of our methods largely rely on off-the-shelf open-source components (e.g., Apache Lucene for indexing the documents). The methods differ in how they analyze the given input document to obtain a query (e.g., by keyword extraction or named entity recognition) and to what extent the returned results are re-ranked taking meta data of the documents (e.g., publication dates) into account.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BimantaraBEGGLP18.bib) "
	```
	@inproceedings{DBLP:conf/trec/BimantaraBEGGLP18,
		author = {Agra Bimantara and Michelle Blau and Kevin Engelhardt and Johannes Gerwert and Tobias Gottschalk and Philipp Lukosz and Shenna Piri and Nima Saken Shaft and Klaus Berberich},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {htw saar @ {TREC} 2018 News Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/htwsaar-N.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BimantaraBEGGLP18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREMA-UNH at TREC 2018: Complex Answer Retrieval and News Track

_Sumanta Kashyapi, Shubham Chatterjee, Jordan Ramsdell, Laura Dietz_

- :fontawesome-solid-user-group: **Participant:** [trema-unh](./news/participants.md#trema-unh)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/TREMA-UNH-CAR-N.pdf](https://trec.nist.gov/pubs/trec27/papers/TREMA-UNH-CAR-N.pdf)
- :material-file-search: **Runs:** [UNH-ParaBm25Ecm](./news/runs.md#unh-parabm25ecm) | [UNH-ParaBm25](./news/runs.md#unh-parabm25) | [UNH-TitleBm25](./news/runs.md#unh-titlebm25)

??? abstract "Abstract"
	
	This notebook describes the submission of team TREMA-UNH to the TREC Complex Answer Retrieval track and the TREC News track in 2018. Our methods focus on passage retrieval, entity-aware passage retrieval, and entity retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KashyapiCRD18.bib) "
	```
	@inproceedings{DBLP:conf/trec/KashyapiCRD18,
		author = {Sumanta Kashyapi and Shubham Chatterjee and Jordan Ramsdell and Laura Dietz},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREMA-UNH} at {TREC} 2018: Complex Answer Retrieval and News Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/TREMA-UNH-CAR-N.pdf},
		timestamp = {Tue, 21 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KashyapiCRD18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using clustering to filter results of an Information Retrieval system

_Pilar López-Úbeda, Manuel Carlos Díaz-Galiano, María Teresa Martín Valdivia, Luis Alfonso Ureña López_

- :fontawesome-solid-user-group: **Participant:** [SINAI](./news/participants.md#sinai)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/SINAI-N.pdf](https://trec.nist.gov/pubs/trec27/papers/SINAI-N.pdf)
- :material-file-search: **Runs:** [SINAI_base_A](./news/runs.md#sinai_base_a) | [SINAI_base_T](./news/runs.md#sinai_base_t) | [SINAI_base_TA](./news/runs.md#sinai_base_ta) | [SINAI_cluster_A](./news/runs.md#sinai_cluster_a) | [SINAI_cluster_T](./news/runs.md#sinai_cluster_t) | [SINAI_clusterTA](./news/runs.md#sinai_clusterta)

??? abstract "Abstract"
	
	In this paper we present our participation as SINAI research group from the Universidad de Ja´en at Text REtrieval Conceference (TREC) in the News task. Specifically we have participated in sub-task 1 called Background Linking. In this task we try to apply K-means clustering algorithms to obtain related news from different domains and topics. We also use document reordering techniques to obtain a new ordered list of relevant articles. For text processing we use the popular TF-IDF technique. The results obtained have not overcome the proposed baseline, although we are usually above average, improving in some cases 78% the average
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lopez-UbedaDVL18.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lopez-UbedaDVL18,
		author = {Pilar L{\'{o}}pez{-}{\'{U}}beda and Manuel Carlos D{\'{\i}}az{-}Galiano and Mar{\'{\i}}a Teresa Mart{\'{\i}}n Valdivia and Luis Alfonso Ure{\~{n}}a L{\'{o}}pez},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Using clustering to filter results of an Information Retrieval system},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/SINAI-N.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lopez-UbedaDVL18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Paragraph as Lead - Finding Background Documents for News Articles

_Kuang Lu, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./news/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/udel_fang-N.pdf](https://trec.nist.gov/pubs/trec27/papers/udel_fang-N.pdf)
- :material-file-search: **Runs:** [UDInfolab_kweh](./news/runs.md#udinfolab_kweh) | [UDInfolab_kwh](./news/runs.md#udinfolab_kwh) | [UDInfolab_kwef](./news/runs.md#udinfolab_kwef) | [UDInfolab_kwf](./news/runs.md#udinfolab_kwf) | [UDInfolab_kwev](./news/runs.md#udinfolab_kwev)

??? abstract "Abstract"
	
	When reading a news article, it is very useful that articles about the background of various aspects of the story are provided so that the readers can better understand the story. In this year's News Track, we tried to use paragraphs as leads to find background articles since they tend to cover different aspects of the main story [3]. More specifically, the keywords in the paragraphs were extracted and used as queries to find background articles. Entities were also leveraged to improve the retrieval performances of the keyword queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lu018.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lu018,
		author = {Kuang Lu and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Paragraph as Lead - Finding Background Documents for News Articles},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/udel\_fang-N.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lu018.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2018: CAR, Common Core and News Tracks

_Shahrzad Naseri, John Foley, James Allan_

- :fontawesome-solid-user-group: **Participant:** [UMass](./news/participants.md#umass)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/UMass-CAR-CC-N.pdf](https://trec.nist.gov/pubs/trec27/papers/UMass-CAR-CC-N.pdf)
- :material-file-search: **Runs:** [umass_cbrdm](./news/runs.md#umass_cbrdm) | [umass_rdm](./news/runs.md#umass_rdm) | [umass_rm](./news/runs.md#umass_rm)

??? abstract "Abstract"
	
	UMass participated in three TREC tasks in 2018: the TREC CAR, TREC Core tasks and TREC News (Background Linking). In this paper we detail the contents of our submissions and our lessons learned from this year's participation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NaseriFA18.bib) "
	```
	@inproceedings{DBLP:conf/trec/NaseriFA18,
		author = {Shahrzad Naseri and John Foley and James Allan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UMass at {TREC} 2018: CAR, Common Core and News Tracks},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/UMass-CAR-CC-N.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NaseriFA18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Signal at TREC 2018 News Track

_Dwane van der Sluis, Dyaa Albakour, Miguel Martinez_

- :fontawesome-solid-user-group: **Participant:** [signal](./news/participants.md#signal)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/signal.N.pdf](https://trec.nist.gov/pubs/trec27/papers/signal.N.pdf)
- :material-file-search: **Runs:** [signal-ucl-slst](./news/runs.md#signal-ucl-slst) | [signal-ucl-sel](./news/runs.md#signal-ucl-sel) | [signal-ucl-eff](./news/runs.md#signal-ucl-eff)

??? abstract "Abstract"
	
	This paper provides an overview of the experiments we carried out for the entity ranking task at the TREC 2018 News Track. In particular, we experimented with adapting the supervised salience component of Salient Entity Linking (SEL), a state-of-the-art unified framework for entity linking and salience ranking. In our adaptation, we assume perfect entity linking performance and rank the entities using the salience components of SEL. Furthermore, in this adaptation, we aim to enhance the efficiency of the supervised salience ranking, and also to introduce sentiment-based features for entity salience.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SluisAM18.bib) "
	```
	@inproceedings{DBLP:conf/trec/SluisAM18,
		author = {Dwane van der Sluis and Dyaa Albakour and Miguel Martinez},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Signal at {TREC} 2018 News Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/signal.N.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SluisAM18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Anserini at trec 2018: Centre, Common Core, and News Tracks

_Yang, Peilin, Lin, Jimmy_

- :fontawesome-solid-user-group: **Participant:** [Anserini](./news/participants.md#anserini)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/anserini-CTR-CC-N.pdf](https://trec.nist.gov/pubs/trec27/papers/anserini-CTR-CC-N.pdf)
- :material-file-search: **Runs:** [anserini_1000w](./news/runs.md#anserini_1000w) | [anserini_nsdm](./news/runs.md#anserini_nsdm) | [anserini_nax](./news/runs.md#anserini_nax) | [anserini_sdmp](./news/runs.md#anserini_sdmp) | [anserini_axp](./news/runs.md#anserini_axp)

??? abstract "Abstract"
	
	Anserini is an open-source information retrieval toolkit built on Lucene [3, 4]. The goal of our effort is to support information retrieval research using the popular open-source Lucene search library by allowing researchers to easily replicate results with modern ranking models on diverse test collections. Although there are many open-source search engines developed and maintained by academic research groups, most of them are designed primarily to facilitate the publication of research papers, and as such, they often suffer from poor usability, incomplete documentation, and a host of other issues. The growing complexity of modern software ecosystems and the diverse capabilities that are required to build useful end-to-end search applications places academic research groups at a huge disadvantage relative to Lucene. Except for a handful of commercial web search engines that deploy custom infrastructure, Lucene has become the de facto platform in industry for building production search applications—used by organizations as diverse as Twitter, Reddit, Bloomberg, and Target. It has an active developer base, diverse features and capabilities, and lies at the center of a vibrant ecosystem. However, Lucene lacks systematic support for information retrieval research—in particular, ad hoc experimentation using standard test collections. This is where Anserini comes in: we enable cutting-edge information retrieval research using Lucene. At TREC 2018, we participated in the CENTRE, Common Core, and News Tracks. Each is described in its own section below. Our development efforts centered around the v0.1.0 release of Anserini, which is based on Lucene 6.3.0 (not the latest release).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/) "
	```
	@inproceedings{yang2018anserini,
		title = {Anserini at trec 2018: Centre, Common Core, and News Tracks},
		author = {Yang, Peilin and Lin, Jimmy},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference (TREC 2018), Gaithersburg, MD},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/anserini-CTR-CC-N.pdf},
		biburl = {https://dblp.org/}
	}
	```

## Incident Streams 

#### CBNU at TREC 2018 Incident Streams Track

_Won-Gyu Choi, Seung-Hyeon Jo, Kyung-Soon Lee_

- :fontawesome-solid-user-group: **Participant:** [cbnu](./incident/participants.md#cbnu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/cbnu-IS.pdf](https://trec.nist.gov/pubs/trec27/papers/cbnu-IS.pdf)
- :material-file-search: **Runs:** [cbnuC1](./incident/runs.md#cbnuc1) | [cbnuC2](./incident/runs.md#cbnuc2) | [cbnuS2](./incident/runs.md#cbnus2) | [cbnuS1](./incident/runs.md#cbnus1)

??? abstract "Abstract"
	
	This paper describes the participation of the CBNU team at the TREC Incident Streams Track 2018. For tweet representation, crisis-related terms are represented as conceptual entities. For tweet classification, we have compared support vector machines and our deep learning model which combines class activation mapping with one-shot learning in convolutional neural networks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChoiJL18.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChoiJL18,
		author = {Won{-}Gyu Choi and Seung{-}Hyeon Jo and Kyung{-}Soon Lee},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CBNU} at {TREC} 2018 Incident Streams Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/cbnu-IS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChoiJL18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### EPIC_MR Participation in the TREC 2018 Incidence Stream Track

_Simon W. Y. Chung, K. K. Lo_

- :fontawesome-solid-user-group: **Participant:** [EPIC_MR](./incident/participants.md#epic_mr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/EPIC_MR-IS.pdf](https://trec.nist.gov/pubs/trec27/papers/EPIC_MR-IS.pdf)
- :material-file-search: **Runs:** [myrun-11](./incident/runs.md#myrun-11) | [myrun-10](./incident/runs.md#myrun-10) | [myrun-2](./incident/runs.md#myrun-2) | [myrun-21](./incident/runs.md#myrun-21)

??? abstract "Abstract"
	
	This paper describes our participation of the EPIC_MR group to the TREC 2018 Incident Streams Track. The target of the track is to monitor the social media and classify different type of information to help different response agencies. This paper describes our approach to use the words with Wikipedia articles to build the training vector, and also the result and comments of our runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChungL18.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChungL18,
		author = {Simon W. Y. Chung and K. K. Lo},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {EPIC{\_}MR Participation in the {TREC} 2018 Incidence Stream Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/EPIC\_MR-IS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChungL18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Neural Networks and Support Vector Machine based Approach for Classifying  Tweets by Information Types at TREC 2018 Incident Streams Task

_Abu Nowshed Chy, Umme Aymun Siddiqua, Masaki Aono_

- :fontawesome-solid-user-group: **Participant:** [KDEIS](./incident/participants.md#kdeis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/KDEIS-IS.pdf](https://trec.nist.gov/pubs/trec27/papers/KDEIS-IS.pdf)
- :material-file-search: **Runs:** [KDEIS2_ACBLSTM](./incident/runs.md#kdeis2_acblstm) | [KDEIS1_CLSTM](./incident/runs.md#kdeis1_clstm) | [KDEIS3_ACSBLSTM](./incident/runs.md#kdeis3_acsblstm) | [KDEIS4_DM](./incident/runs.md#kdeis4_dm)

??? abstract "Abstract"
	
	Microblog, especially twitter, is treated as an important source to serve the situational information needs during a disaster period. Monitoring and producing the curated tweets based on different information types from massive twitter posts provide enormous opportunities to different public safety personnel or used for post-incident analysis. In this paper, we present our approach to addressing the problem defined in the TREC 2018 incident streams (TREC-IS) task. The task is to classify the tweets in each event/incident's stream into different high-level information types within the incident ontology. In our approach, we employ different deep neural network (DNN) classifiers in combination with a multi-class support vector machine (SVM) classifier and a rule-based classifier. We consider a rich set of hand-crafted features to train our multi-class SVM classifier, whereas a pre-trained word2vec model is used for the DNN based classifiers. Moreover, we introduce a set of rules based on the language of tweets, exploiting indicator terms, and WH-orientation of tweets for our rule-based classifier. Experimental results showed that our proposed KDEIS4 DM method obtained the second position among the participants in TREC-IS task and outperforms the participant median by more than 8% and 5% in terms of F1 Score and accuracy, respectively
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChySA18.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChySA18,
		author = {Abu Nowshed Chy and Umme Aymun Siddiqua and Masaki Aono},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Neural Networks and Support Vector Machine based Approach for Classifying Tweets by Information Types at {TREC} 2018 Incident Streams Task},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/KDEIS-IS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChySA18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SINAI at TREC 2018: Experiments in Incident Streams

_Miguel Ángel García Cumbreras, Manuel Carlos Díaz-Galiano, Manuel García Vega, Salud María Jiménez Zafra_

- :fontawesome-solid-user-group: **Participant:** [SINAI](./incident/participants.md#sinai)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/SINAI-IS.pdf](https://trec.nist.gov/pubs/trec27/papers/SINAI-IS.pdf)
- :material-file-search: **Runs:** [SINAI_run1](./incident/runs.md#sinai_run1) | [SINAI_run2](./incident/runs.md#sinai_run2) | [SINAI_run3](./incident/runs.md#sinai_run3) | [SINAI_run4](./incident/runs.md#sinai_run4)

??? abstract "Abstract"
	
	This paper describes the system architecture of the University of Jaén - SINAI team's for the TREC 2018 Incident Streams Track. The goal of the challenge is to automatically process social media streams during emergency situations with the aim of categorizing information and aid requests made on social media for emergency service operators. We explored four alternatives: baseline experimentation, WordNet synonyms, spelling correction and word embeddings. All of them use Support Vector Machine (SVM) as machine learning method. Our experiments reveal that the last approach leads to improve the baseline result.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CumbrerasDVZ18.bib) "
	```
	@inproceedings{DBLP:conf/trec/CumbrerasDVZ18,
		author = {Miguel {\'{A}}ngel Garc{\'{\i}}a Cumbreras and Manuel Carlos D{\'{\i}}az{-}Galiano and Manuel Garc{\'{\i}}a Vega and Salud Mar{\'{\i}}a Jim{\'{e}}nez Zafra},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{SINAI} at {TREC} 2018: Experiments in Incident Streams},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/SINAI-IS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CumbrerasDVZ18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2018: Incident Streams Track

_Ning Lu, Hesong Wang, Zhen Yang_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./incident/participants.md#bjut)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/BJUT-IS.pdf](https://trec.nist.gov/pubs/trec27/papers/BJUT-IS.pdf)
- :material-file-search: **Runs:** [myrun2](./incident/runs.md#myrun2) | [myrun1](./incident/runs.md#myrun1)

??? abstract "Abstract"
	
	In this paper we will introduce our work on the 2018 TREC real-time event flow test task. With the development of social media, more and more people choose to use social media to share their lives. Similarly, when encountering unexpected situations such as fires, earthquakes, flash floods, tsunamis, mudslides and other natural disasters or shootings, robberies and other emergencies, people like to release the progress of the disaster situation or event through social media. This task is to filter the information of such natural disasters or emergencies through text detection, and to classify the information, and finally to report the marked information to relevant staff according to different priorities. Let the staff know about the progress of the incident and the local real-time situation in case of rescue. This article will introduce the framework and methods of the classification system, as well as the experimental results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuW018.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuW018,
		author = {Ning Lu and Hesong Wang and Zhen Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2018: Incident Streams Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/BJUT-IS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuW018.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT-BHU In TREC 2018 Incidents Stream Track

_Harshit Mehrotra, Sukomal Pal_

- :fontawesome-solid-user-group: **Participant:** [IIT-BHU](./incident/participants.md#iit-bhu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/IIT-BHU-IS.pdf](https://trec.nist.gov/pubs/trec27/papers/IIT-BHU-IS.pdf)
- :material-file-search: **Runs:** [IITBHU1](./incident/runs.md#iitbhu1) | [IITBHU12](./incident/runs.md#iitbhu12)

??? abstract "Abstract"
	
	This paper presents details of the work done by the team of IIT (BHU) Varanasi for the Incidents Stream track in TREC 2018. The task involved classifying tweets posted during a disaster into a number of categories, which are useful for relief work purposes at such a time. The data given was in the form of tweets from one earthquake, tornado, wildfire, flood, shooting and bombing incident.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MehrotraP18.bib) "
	```
	@inproceedings{DBLP:conf/trec/MehrotraP18,
		author = {Harshit Mehrotra and Sukomal Pal},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IIT-BHU} In {TREC} 2018 Incidents Stream Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/IIT-BHU-IS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MehrotraP18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NHK STRL at TREC 2018 Incident Streams track

_Taro Miyazaki, Kiminobu Makino, Yuka Takei, Hiroki Okamoto, Jun Goto_

- :fontawesome-solid-user-group: **Participant:** [NHK](./incident/participants.md#nhk)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/NHK-IS.pdf](https://trec.nist.gov/pubs/trec27/papers/NHK-IS.pdf)
- :material-file-search: **Runs:** [NHK_run2](./incident/runs.md#nhk_run2) | [NHK_run3](./incident/runs.md#nhk_run3) | [NHK_run1](./incident/runs.md#nhk_run1) | [NHK_run4](./incident/runs.md#nhk_run4)

??? abstract "Abstract"
	
	We describe NHK STRL's models for the TREC 2018 Incident Streams track. The goal of this track is classifying incident related Tweets into information types such as InformationWanted and EmergingThreats. The number of provided pieces of training data is about 2,000, which is not enough for current machine learning methods. We propose two models to overcome this small amount of data scenario: a knowledge base-based model and a model that considers meta-information. In addition, we used two bag-of-words baseline models, a multi-layer perceptron-based one and a support vector machine-based one, for comparison. Evaluation results show that our models can classify Tweets with a rather high F1 score.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MiyazakiMTOG18.bib) "
	```
	@inproceedings{DBLP:conf/trec/MiyazakiMTOG18,
		author = {Taro Miyazaki and Kiminobu Makino and Yuka Takei and Hiroki Okamoto and Jun Goto},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{NHK} {STRL} at {TREC} 2018 Incident Streams track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/NHK-IS.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MiyazakiMTOG18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DICE @ TREC-IS 2018: Combining Knowledge Graphs and Deep Learning  to Identify Crisis-Relevant Tweets

_Hamada M. Zahera, Rricha Jalota, Ricardo Usbeck_

- :fontawesome-solid-user-group: **Participant:** [DICE-UPB](./incident/participants.md#dice-upb)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/DICE-UPB-IS.pdf](https://trec.nist.gov/pubs/trec27/papers/DICE-UPB-IS.pdf)
- :material-file-search: **Runs:** [UPB_DICE1](./incident/runs.md#upb_dice1) | [UPB_DICE2](./incident/runs.md#upb_dice2) | [UPB_DICE4](./incident/runs.md#upb_dice4) | [UPB_DICE3](./incident/runs.md#upb_dice3)

??? abstract "Abstract"
	
	In this paper, we describe our submissions to the TREC Incident Stream (TREC-IS) challenge 2018. We investigated different machine learning approaches to classify crisis-related tweets into different information types. We incorporated knowledge graphs as features into this social media analysis, in addition to bag of words, word embeddings, time data, and event-types. Further, we evaluate state-of-the-art classification models on 31 generated features sets. Our TREC-IS results indicate that a model based on combining knowledge graphs (i.e., Babelfy), word embeddings and textual features outperformes classical machine learning models
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZaheraJU18.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZaheraJU18,
		author = {Hamada M. Zahera and Rricha Jalota and Ricardo Usbeck},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{DICE} @ {TREC-IS} 2018: Combining Knowledge Graphs and Deep Learning to Identify Crisis-Relevant Tweets},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/DICE-UPB-IS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZaheraJU18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## CENTRE 

#### The University of Padua IMS Research Group at CENTRE@TREC 2018

_Giorgio Maria Di Nunzio, Stefano Marchesin_

- :fontawesome-solid-user-group: **Participant:** [ims_unipd](./centre/participants.md#ims_unipd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/ims_unipd-C.pdf](https://trec.nist.gov/pubs/trec27/papers/ims_unipd-C.pdf)

??? abstract "Abstract"
	
	In this paper, we present our participation in one of the tasks of the CENTRE@TREC 2018 Track: the Clinical Decision Support task. We describe the steps of the original paper we wanted to reproduce, identifying the elements of ambiguity that may affect the reproducibility of the results. The experimental results we obtained follow a similar trend to those presented in the original paper: using clinical trials' “note” field decreases the retrieval performances significantly, while the pseudo-relevance feedback approach together with query expansion achieves the best results across different measures. In the experimental results we find out that the choice of the stoplist is fundamental to achieve a reasonable level of reproducibility. However, stoplist creation is not described sufficiently well in the original paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Nunzio018.bib) "
	```
	@inproceedings{DBLP:conf/trec/Nunzio018,
		author = {Giorgio Maria Di Nunzio and Stefano Marchesin},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {The University of Padua {IMS} Research Group at CENTRE@TREC 2018},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/ims\_unipd-C.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Nunzio018.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Anserini at trec 2018: Centre, Common Core, and News Tracks

_Yang, Peilin, Lin, Jimmy_

- :fontawesome-solid-user-group: **Participant:** [Anserini](./centre/participants.md#anserini)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/anserini-CTR-CC-N.pdf](https://trec.nist.gov/pubs/trec27/papers/anserini-CTR-CC-N.pdf)
- :material-file-search: **Runs:** [Anserini-UDInfolabWEB1-1](./centre/runs.md#anserini-udinfolabweb1-1) | [Anserini-UDInfolabWEB1-2](./centre/runs.md#anserini-udinfolabweb1-2) | [Anserini-UDInfolabWEB1-3](./centre/runs.md#anserini-udinfolabweb1-3) | [Anserini-UDInfolabWEB2-1](./centre/runs.md#anserini-udinfolabweb2-1) | [Anserini-UDInfolabWEB2-2](./centre/runs.md#anserini-udinfolabweb2-2) | [Anserini-UDInfolabWEB2-3](./centre/runs.md#anserini-udinfolabweb2-3)

??? abstract "Abstract"
	
	Anserini is an open-source information retrieval toolkit built on Lucene [3, 4]. The goal of our effort is to support information retrieval research using the popular open-source Lucene search library by allowing researchers to easily replicate results with modern ranking models on diverse test collections. Although there are many open-source search engines developed and maintained by academic research groups, most of them are designed primarily to facilitate the publication of research papers, and as such, they often suffer from poor usability, incomplete documentation, and a host of other issues. The growing complexity of modern software ecosystems and the diverse capabilities that are required to build useful end-to-end search applications places academic research groups at a huge disadvantage relative to Lucene. Except for a handful of commercial web search engines that deploy custom infrastructure, Lucene has become the de facto platform in industry for building production search applications—used by organizations as diverse as Twitter, Reddit, Bloomberg, and Target. It has an active developer base, diverse features and capabilities, and lies at the center of a vibrant ecosystem. However, Lucene lacks systematic support for information retrieval research—in particular, ad hoc experimentation using standard test collections. This is where Anserini comes in: we enable cutting-edge information retrieval research using Lucene. At TREC 2018, we participated in the CENTRE, Common Core, and News Tracks. Each is described in its own section below. Our development efforts centered around the v0.1.0 release of Anserini, which is based on Lucene 6.3.0 (not the latest release).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/) "
	```
	@inproceedings{yang2018anserini,
		title = {Anserini at trec 2018: Centre, Common Core, and News Tracks},
		author = {Yang, Peilin and Lin, Jimmy},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference (TREC 2018), Gaithersburg, MD},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/anserini-CTR-CC-N.pdf},
		biburl = {https://dblp.org/}
	}
	```

