# Proceedings - Precision Medicine 2017 

#### Overview of the TREC 2017 Precision Medicine Track

_Kirk Roberts, Dina Demner-Fushman, Ellen M. Voorhees, William R. Hersh, Steven Bedrick, Alexander J. Lazar, Shubham Pant_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Overview-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/Overview-PM.pdf)
??? abstract "Abstract"
	
	For many complex diseases, there is no “one size fits all” solutions for patients with a particular diagnosis. The proper treatment for a patient depends upon genetic, environmental, and lifestyle choices. The ability to personalize treatment in a scientifically rigorous manner based on these factors is the hallmark of the emerging “precision medicine” paradigm. Nowhere is the potential impact of precision medicine more closely felt than in cancer, where lifesaving treatments for particular patients could prove ineffective or even deadly for other patients based entirely upon the particular genetic mutations in the patient's tumor(s). Significant effort, therefore, has been devoted to deepening the scientific research surrounding precision medicine. This includes a Precision Medicine Initiative (Collins and Varmus, 2015) launched by former President Barack Obama in 2015, now known as the All of Us Research Program. A fundamental difficulty with putting the findings of precision medicine into practice is that-by its very nature-precision medicine creates a huge space of treatment options (Frey et al., 2016). These can easily overwhelm clinicians attempting to stay up-to-date with the latest findings, and can easily inhibit a clinician's attempts to determine the best possible treatment for a particular patient. However, the ability to quickly locate relevant evidence is the hallmark of information retrieval (IR). Further, for three consecutive years the TREC Clinical Decision Support (CDS) track has sought to evaluate IR systems that provide medical evidence to the point-of-care. It was natural, then, to specialize the CDS track to the needs of precision medicine so IR systems can focus on this important issue. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsDVHBLP17.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsDVHBLP17,
		author = {Kirk Roberts and Dina Demner{-}Fushman and Ellen M. Voorhees and William R. Hersh and Steven Bedrick and Alexander J. Lazar and Shubham Pant},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2017 Precision Medicine Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/Overview-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsDVHBLP17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### POZNAN Contribution to TREC PM 2017

_Artur Cieslewicz, Jakub Dutkiewicz, Czeslaw Jedrzejek_

- :fontawesome-solid-user-group: **Participant:** [POZNAN_SEMMED](./participants.md#poznan_semmed)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/POZNAN-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/POZNAN-PM.pdf)
- :material-file-search: **Runs:** [LGDprfGOpt](./runs.md#lgdprfgopt) | [LGDnoprfGOpt](./runs.md#lgdnoprfgopt) | [LGDraw](./runs.md#lgdraw) | [LDGprfStrict](./runs.md#ldgprfstrict) | [POZabsBB2GRn](./runs.md#pozabsbb2grn) | [POZabsLGDGRn](./runs.md#pozabslgdgrn) | [POZabsBB2sn](./runs.md#pozabsbb2sn) | [LGDStrict](./runs.md#lgdstrict)

??? abstract "Abstract"
	
	This work describes the medical information retrieval systems designed by the Poznan Consortium for TREC PM, personalized medicine track, which was submitted to the TREC 2017. The baseline is the Terrier DPH Bo1 which recently has been shown to be the most effective Terrier option. We also used Mesh query expansion, word2vec query expansion, and the combination of these two options. In all measures our results are approximately 0,02 above the median.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CieslewiczDJ17.bib) "
	```
	@inproceedings{DBLP:conf/trec/CieslewiczDJ17,
		author = {Artur Cieslewicz and Jakub Dutkiewicz and Czeslaw Jedrzejek},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{POZNAN} Contribution to {TREC} {PM} 2017},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/POZNAN-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CieslewiczDJ17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ETH Zurich at TREC Precision Medicine 2017

_Negar Foroutan Eghlidi, Jannick Griner, Nicolas Mesot, Leandro von Werra, Carsten Eickhoff_

- :fontawesome-solid-user-group: **Participant:** [ETH](./participants.md#eth)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/ETH-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/ETH-PM.pdf)
- :material-file-search: **Runs:** [eth_a_ws](./runs.md#eth_a_ws) | [eth_a_luc](./runs.md#eth_a_luc) | [eth_a_nn](./runs.md#eth_a_nn) | [eth_a_ws_q](./runs.md#eth_a_ws_q) | [eth_a_gws](./runs.md#eth_a_gws) | [eth_t_ws](./runs.md#eth_t_ws) | [eth_t_luc](./runs.md#eth_t_luc) | [eth_t_nn](./runs.md#eth_t_nn) | [eth_t_wsb_q](./runs.md#eth_t_wsb_q) | [eth_t_gwsq](./runs.md#eth_t_gwsq)

??? abstract "Abstract"
	
	This paper describes ETH Zurich's submission to the TREC 2017 Precision Medicine (PM) track. We begin by performing literal query term matching, taking into account the likelihood of document relevance in terms of cancer types, genetic variants, and demographics. In a second, subsequent stage, we re-rank the most relevant results based on a range of deep neural gene embeddings that project literal genetic expressions into a semantics-preserving vector space using feed-forward networks trained on PubMed and NCBI information but also relying on generative adversarial methods to determine the likelihood of co-occurrence of various mutations within the same patient/article. Empirical results show that even without existing expert labels, the proposed method can introduce marginal improvements over competitive tf-idf baselines.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EghlidiGMWE17.bib) "
	```
	@inproceedings{DBLP:conf/trec/EghlidiGMWE17,
		author = {Negar Foroutan Eghlidi and Jannick Griner and Nicolas Mesot and Leandro von Werra and Carsten Eickhoff},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ETH} Zurich at {TREC} Precision Medicine 2017},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/ETH-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EghlidiGMWE17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UTD HLTRI at TREC 2017: Precision Medicine Track

_Travis R. Goodwin, Michael A. Skinner, Sanda M. Harabagiu_

- :fontawesome-solid-user-group: **Participant:** [UTDHLTRI](./participants.md#utdhltri)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/UTDHLTRI-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/UTDHLTRI-PM.pdf)
- :material-file-search: **Runs:** [UTDHLTJQ](./runs.md#utdhltjq) | [UTDHLTJQT](./runs.md#utdhltjqt) | [UTDHLTAFT](./runs.md#utdhltaft) | [UTDHLTSFT](./runs.md#utdhltsft) | [UTDHLTFFT](./runs.md#utdhltfft) | [UTDHLTSQT](./runs.md#utdhltsqt) | [UTDHLTAF](./runs.md#utdhltaf) | [UTDHLTSF](./runs.md#utdhltsf) | [UTDHLTFF](./runs.md#utdhltff) | [UTDHLTSQ](./runs.md#utdhltsq)

??? abstract "Abstract"
	
	In this paper, we describe the system designed for the TREC 2017 Precision Medicine track by the University of Texas at Dallas (UTD) Human Language Technology Research Institute (HLTRI). Our system incorporates an aspect-based retrieval paradigm wherein each of the four structured components of the topic is cast as a separate aspect, along with two “hidden” aspects encoding the need that retrieved documents be within the domain of precision medicine and that retrieved documents have a focus on treatment. To this end, we construct knowledge graph encoding the relationships between drugs, genes, and mutations. Our experiments reveal that the aspect-based approach leads to improved quality of retrieved scientific articles and clinical trials.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GoodwinSH17.bib) "
	```
	@inproceedings{DBLP:conf/trec/GoodwinSH17,
		author = {Travis R. Goodwin and Michael A. Skinner and Sanda M. Harabagiu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UTD} {HLTRI} at {TREC} 2017: Precision Medicine Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/UTDHLTRI-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GoodwinSH17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CBNU at TREC 2017 Precision Medicine Track

_Seung-Hyeon Jo, Kyung-Soon Lee_

- :fontawesome-solid-user-group: **Participant:** [cbnu](./participants.md#cbnu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/cbnu-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/cbnu-PM.pdf)
- :material-file-search: **Runs:** [cbnuCT1](./runs.md#cbnuct1) | [cbnuCT2](./runs.md#cbnuct2) | [cbnuCT3](./runs.md#cbnuct3) | [cbnuSA1](./runs.md#cbnusa1) | [cbnuSA2](./runs.md#cbnusa2) | [cbnuSA3](./runs.md#cbnusa3)

??? abstract "Abstract"
	
	This paper describes the participation of the CBNU team at the TREC Precision Medicine Track 2017. We have constructed cancer-centered document clusters using cancer-gene relation and clinical causal information. A query has been expanded with disease terms and pseudo-relevance feedback is applied for cancer disease document clusters.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JoL17.bib) "
	```
	@inproceedings{DBLP:conf/trec/JoL17,
		author = {Seung{-}Hyeon Jo and Kyung{-}Soon Lee},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CBNU} at {TREC} 2017 Precision Medicine Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/cbnu-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JoL17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Patient selection for clinical trials based on concept-based retrieval  and result filtering and ranking

_Johannes Leveling_

- :fontawesome-solid-user-group: **Participant:** [teckro](./participants.md#teckro)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/teckro-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/teckro-PM.pdf)
- :material-file-search: **Runs:** [teckro1](./runs.md#teckro1) | [teckro2](./runs.md#teckro2) | [teckro3](./runs.md#teckro3) | [teckro4](./runs.md#teckro4) | [teckro5](./runs.md#teckro5)

??? abstract "Abstract"
	
	For our participation at the clinical trials task in the TREC 2017 Precision Medicine track 2017, we investigated retrieving and matching clinical trial documents with patient information based on text and concept annotations of the text, filtering results for demographic information such as gender and age, and re-ranking results based on patient information. Experimental results show a competitive precision at high ranks for our least complex approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Leveling17.bib) "
	```
	@inproceedings{DBLP:conf/trec/Leveling17,
		author = {Johannes Leveling},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Patient selection for clinical trials based on concept-based retrieval and result filtering and ranking},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/teckro-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Leveling17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCAS at TREC-2017 Precision Medicine Track

_Canjia Li, Ben He, Yingfei Sun, Jungang Xu_

- :fontawesome-solid-user-group: **Participant:** [UCAS](./participants.md#ucas)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/UCAS-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/UCAS-PM.pdf)
- :material-file-search: **Runs:** [UCASBASE](./runs.md#ucasbase) | [UCASSEM3](./runs.md#ucassem3) | [UCASSEM2](./runs.md#ucassem2) | [UCASSEMUMLS](./runs.md#ucassemumls) | [UCASSEM1](./runs.md#ucassem1) | [UCASSEM3a](./runs.md#ucassem3a) | [UCASSEM2a](./runs.md#ucassem2a) | [UCASSEMUMLSa](./runs.md#ucassemumlsa) | [UCASSEM1a](./runs.md#ucassem1a) | [UCASBASEa](./runs.md#ucasbasea)

??? abstract "Abstract"
	
	The participation of UCAS at TREC Precision Medicine 2017 aims to evaluate the effectiveness of integrating semantic evidence to enhance medical information retrieval system. Benefited from the success of distributed semantic representation of words and documents in the natural language process (NLP) domain, two methods on generating document vectors are proposed. Based on the hypothesis that pseudo relevant feedback for a given query would be a better representation of the query in the semantic vector space, we propose a framework that integrates the semantic features to the final ranking process. In addition, query expansion using Medical Subject Headings (MeSH) and pseudo relevance feedback (PRF) are used. Experimental results show that our method achieves significant improvement over the PRF baseline for clinical trials, while full text articles might be required for learning local document embeddings that are effective for retrieval from abstracts.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiHSX17.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiHSX17,
		author = {Canjia Li and Ben He and Yingfei Sun and Jungang Xu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UCAS} at {TREC-2017} Precision Medicine Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/UCAS-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiHSX17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Hybrid Approach to Precision Medicine-related Biomedical Article  Retrieval and Clinical Trial Matching

_Yuan Ling, Sadid A. Hasan, Michele Filannino, Kevin P. Buchan, Kahyun Lee, Joey Liu, William Boag, Di Jin, Özlem Uzuner, Kathy Lee, Vivek V. Datla, Ashequl Qadir, Oladimeji Farri_

- :fontawesome-solid-user-group: **Participant:** [prna-mit-suny](./participants.md#prna-mit-suny)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/prna-mit-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/prna-mit-PM.pdf)
- :material-file-search: **Runs:** [pms_run1](./runs.md#pms_run1) | [pms_run1_tri](./runs.md#pms_run1_tri) | [pms_run2_abs](./runs.md#pms_run2_abs) | [pms_run2_tri](./runs.md#pms_run2_tri) | [pms_run3_abs](./runs.md#pms_run3_abs) | [pms_run3_tri](./runs.md#pms_run3_tri) | [pms_run4_abs](./runs.md#pms_run4_abs) | [pms_run4_tri](./runs.md#pms_run4_tri) | [pms_run5_abs](./runs.md#pms_run5_abs) | [pms_run5_tri](./runs.md#pms_run5_tri)

??? abstract "Abstract"
	
	We describe our systems implemented for the Text Retrieval Conference (TREC 2017) Precision Medicine track. We submitted five runs for biomedical article retrieval and five runs for clinical trial matching. Our approaches combine strict rule matching with an ontology-based solution. Evaluation results demonstrate that our best run obtained the 2nd highest precision (P@5) score for the clinical trial matching task and was consistently ranked within top 5 teams in all evaluation metrics for the biomedical literature retrieval task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LingHFBLLBJULDQ17.bib) "
	```
	@inproceedings{DBLP:conf/trec/LingHFBLLBJULDQ17,
		author = {Yuan Ling and Sadid A. Hasan and Michele Filannino and Kevin P. Buchan and Kahyun Lee and Joey Liu and William Boag and Di Jin and {\"{O}}zlem Uzuner and Kathy Lee and Vivek V. Datla and Ashequl Qadir and Oladimeji Farri},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {A Hybrid Approach to Precision Medicine-related Biomedical Article Retrieval and Clinical Trial Matching},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/prna-mit-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LingHFBLLBJULDQ17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2017 Precision Medicine - Medical University of Graz

_Pablo López-García, Michel Oleynik, Zdenko Kasác, Stefan Schulz_

- :fontawesome-solid-user-group: **Participant:** [imi_mug](./participants.md#imi_mug)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/imi_mug-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/imi_mug-PM.pdf)
- :material-file-search: **Runs:** [mugpubbase](./runs.md#mugpubbase) | [mugctbase](./runs.md#mugctbase) | [mugpubboost](./runs.md#mugpubboost) | [mugpubdiseas](./runs.md#mugpubdiseas) | [mugpubgene](./runs.md#mugpubgene) | [mugpubshould](./runs.md#mugpubshould) | [mugctboost](./runs.md#mugctboost) | [mugctmust](./runs.md#mugctmust) | [mugctdisease](./runs.md#mugctdisease) | [mugctgene](./runs.md#mugctgene)

??? abstract "Abstract"
	
	In this paper we report on our participation in the TREC 2017 Precision Medicine track (team name: imi_mug). We submitted 5 fully automatic runs to both the biomedical articles and clinical trials subtasks, focusing strongly on the former. Our system was based on Elasticsearch, whose queries were generated modularly via our own open source framework. Our results showed that a modern search engine with an advanced query language is a powerful solution for the proposed tasks but it requires deep medical knowledge and careful tuning to get top performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lopez-GarciaOK017.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lopez-GarciaOK017,
		author = {Pablo L{\'{o}}pez{-}Garc{\'{\i}}a and Michel Oleynik and Zdenko Kas{\'{a}}c and Stefan Schulz},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2017 Precision Medicine - Medical University of Graz},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/imi\_mug-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lopez-GarciaOK017.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UD_GU_BioTM at TREC 2017: Precision Medicine Track

_A. S. M. Ashique Mahmood, Gang Li, Shruti Rao, Peter B. McGarvey, Cathy H. Wu, Subha Madhavan, K. Vijay-Shanker_

- :fontawesome-solid-user-group: **Participant:** [UD_GU_BioTM](./participants.md#ud_gu_biotm)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/UD_GU_BioTM-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/UD_GU_BioTM-PM.pdf)
- :material-file-search: **Runs:** [UD_GU_SA_1](./runs.md#ud_gu_sa_1) | [UD_GU_SA_2](./runs.md#ud_gu_sa_2) | [UD_GU_SA_3](./runs.md#ud_gu_sa_3) | [UD_GU_SA_4](./runs.md#ud_gu_sa_4) | [UD_GU_SA_5](./runs.md#ud_gu_sa_5) | [UD_GU_CT_1](./runs.md#ud_gu_ct_1) | [UD_GU_CT_2](./runs.md#ud_gu_ct_2) | [UD_GU_CT_3](./runs.md#ud_gu_ct_3) | [UD_GU_CT_4](./runs.md#ud_gu_ct_4) | [UD_GU_CT_5](./runs.md#ud_gu_ct_5)

??? abstract "Abstract"
	
	This paper describes the system developed for the TREC 2017 PM track. We employed a two-part system to generate the ranked list of clinical trials and scientific abstracts. The first part pertains to query expansion and document retrieval from document index. The second part pertains to generating the final ranked list by implementing a heuristic scoring method. The scoring for clinical trials involved grouping trials based on different trial fields and extraction of features based on occurrences of gene/disease and other terms in the trial. The scoring for scientific abstracts involved applying a NLP system to extract relations from text, as well as extraction of additional information relevant to precision medicine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MahmoodLRMWMV17.bib) "
	```
	@inproceedings{DBLP:conf/trec/MahmoodLRMWMV17,
		author = {A. S. M. Ashique Mahmood and Gang Li and Shruti Rao and Peter B. McGarvey and Cathy H. Wu and Subha Madhavan and K. Vijay{-}Shanker},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UD{\_}GU{\_}BioTM at {TREC} 2017: Precision Medicine Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/UD\_GU\_BioTM-PM.pdf},
		timestamp = {Mon, 19 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MahmoodLRMWMV17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CSIRO at 2017 TREC Precision Medicine Track

_Vincent Nguyen, Sarvnaz Karimi, Sara Falamaki, Diego Mollá Aliod, Cécile Paris, Stephen Wan_

- :fontawesome-solid-user-group: **Participant:** [CSIROmed](./participants.md#csiromed)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/CSIRO-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/CSIRO-PM.pdf)
- :material-file-search: **Runs:** [aCSIROmedAll](./runs.md#acsiromedall) | [cCSIROmedAll](./runs.md#ccsiromedall) | [cCSIROmedNEG](./runs.md#ccsiromedneg) | [cCSIROmedMCM](./runs.md#ccsiromedmcm) | [cCSIROmedHGB](./runs.md#ccsiromedhgb) | [cCSIROmedMCB](./runs.md#ccsiromedmcb) | [aCSIROmedNEG](./runs.md#acsiromedneg) | [aCSIROmedPCB](./runs.md#acsiromedpcb) | [aCSIROmedMGB](./runs.md#acsiromedmgb) | [aCSIROmedMCB](./runs.md#acsiromedmcb)

??? abstract "Abstract"
	
	We report on our participation as the CSIROmed1 team in the TREC 2017 Precision Medicine track. We submitted five runs for the scientific abstracts collection (MEDLINE and Cancer Proceedings), and five runs for the clinical trials collection. We experimented with a number of query expansion and search result re-ranking techniques. We used citation and MeSH-based re-ranking methods, as well as reranking based on a merging algorithm proposed for federated search. Our results show that boosting the gene variant in the query increases the relevance of the retrieved results. One of our five runs for clinical trials task was ranked in top 10 runs out of 133 runs submitted for this task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NguyenKFAPW17.bib) "
	```
	@inproceedings{DBLP:conf/trec/NguyenKFAPW17,
		author = {Vincent Nguyen and Sarvnaz Karimi and Sara Falamaki and Diego Moll{\'{a}} Aliod and C{\'{e}}cile Paris and Stephen Wan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CSIRO} at 2017 {TREC} Precision Medicine Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/CSIRO-PM.pdf},
		timestamp = {Thu, 21 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NguyenKFAPW17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Team UKNLP at TREC 2017 Precision Medicine Track: A Knowledge-Based  IR System with Tuned Query-Time Boosting

_Jiho Noh, Ramakanth Kavuluru_

- :fontawesome-solid-user-group: **Participant:** [UKNLP](./participants.md#uknlp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/UKNLP-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/UKNLP-PM.pdf)
- :material-file-search: **Runs:** [UKY_BASE](./runs.md#uky_base) | [UKY_CJT](./runs.md#uky_cjt) | [UKY_AGG](./runs.md#uky_agg) | [UKY_COM](./runs.md#uky_com) | [UKY_MAN](./runs.md#uky_man) | [UKY_TRL](./runs.md#uky_trl) | [UKY_T2](./runs.md#uky_t2) | [UKY_T3](./runs.md#uky_t3) | [UKY_T4](./runs.md#uky_t4)

??? abstract "Abstract"
	
	This paper describes the system architecture of the University of Kentucky Natural Language Processing (UKNLP) team's entry for the TREC 2017 Precision Medicine Track. The goal of the challenge is to retrieve useful precision medicine-related information (abstracts, clinical trials) for the given synthetic cancer patient cases, each of which consists of a neoplastic condition, genetic variants, demographic details, and any additional information (e.g., comorbidities). We explored query expansion techniques using well-known broad knowledge sources such as the Unified Medical Language System (UMLS) and the Medical Subject Headings (MeSH) for each abstract, and additional specialized sources such as the Catalogue Of Somatic Mutations In Cancer (COSMIC) database, which allowed us to construct boosted queries. We conducted several experiments with model averaging techniques and our final system architecture placed 6th (in terms of infNDCG and R-prec) among 29 teams that submitted runs to the scientific abstract retrieval task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NohK17.bib) "
	```
	@inproceedings{DBLP:conf/trec/NohK17,
		author = {Jiho Noh and Ramakanth Kavuluru},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Team {UKNLP} at {TREC} 2017 Precision Medicine Track: {A} Knowledge-Based {IR} System with Tuned Query-Time Boosting},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/UKNLP-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NohK17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Customizing a Variant Annotation-Support Tool: an Inquiry into Probability  Ranking Principles for TREC Precision Medicine

_Emilie Pasche, Julien Gobeill, Luc Mottin, Anaïs Mottaz, Douglas Teodoro, Paul Van Rijen, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [BiTeM](./participants.md#bitem)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/BiTeM-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/BiTeM-PM.pdf)
- :material-file-search: **Runs:** [SIBTMlit1](./runs.md#sibtmlit1) | [SIBTMlit2](./runs.md#sibtmlit2) | [SIBTMlit3](./runs.md#sibtmlit3) | [SIBTMlit4](./runs.md#sibtmlit4) | [SIBTMlit5](./runs.md#sibtmlit5) | [SIBTct1](./runs.md#sibtct1) | [SIBTct2](./runs.md#sibtct2) | [SIBTct3](./runs.md#sibtct3) | [SIBTct4](./runs.md#sibtct4) | [SIBTct5](./runs.md#sibtct5)

??? abstract "Abstract"
	
	The TREC 2017 Precision Medicine Track aims at building systems providing meaningful precision medicine-related information to clinicians in the field of oncology. The track includes two tasks: 1) retrieving scientific abstracts addressing treatment effect and prognosis of a disease and 2) retrieving clinical trials for which a patient is eligible. The SIB Text Mining group participated in both tasks. Regarding the retrieval of scientific abstracts, we designed a set of different queries with decreasing levels of specificity. The idea was to start initiating a very specific query, from which less specific queries will be inferred. We may thus consider as relevant abstracts that did not mention all critical aspects of the complete query but could still be of interest. Therefore, the main component of our approach was a large query generation module (e.g. disease + gene + variant; disease + gene; gene + variant) - with each generated query being differentially weighted. To increase the scope of the queries, we applied query expansion strategies. In particular, a single nucleotide variant (SNV) generator was developed to recognize standard nomenclature as described by the Human Genome Variation Society (HGVS) as well as non-standard formats frequently found in the literature. We thus expect to retrieve a maximum of relevant abstracts. We then applied different strategies to favor relevant abstracts by re-ranking them based on more general criteria. First, we assumed that an abstract with a high frequency of drug names is more probably relevant to support our task. Therefore, we pre-annotated all the collection with DrugBank, thus enabling to retrieve the number of occurrences of drug names per abstract. Second, we assumed that the presence of some specific keywords (e.g. “treat”) in the abstract should increase the relevance of the paper, while the presence of some other keywords (e.g. “marker”) should decrease its relevance. Third, we assumed that some publications, such as clinical trials, should receive higher relevance for this task. Regarding the retrieval of clinical trials, we investigated for the competition different combinations of filtering and information retrieval strategies, mostly based on the exploitation of ontologies. Our preliminary analysis of the collection showed that : (1) demographic features (age and gender) are stored in a perfectly-structured form in clinical trials, thus this feature can be easily handled with strict filtering ; (2) the trials contain very few mentions of the requested genes and variants ; (3) diseases are stored in very inconsistent forms, as they are free text entities and can be mentioned in different fields such as condition, keywords, summary, criteria, etc. Thus, we assumed that identifying clinical trials dealing with the correct disease was the most challenging issue for this competition. For such a task, we perform Name Entity Recognition with the NCI thesaurus in order to recognize mentions of diseases in topics and in different fields of the clinical trials. This strategy handles several issues of free text descriptions, such as synonyms (“Cancer” and “Neoplasm” are equivalent) and hierarchies (“Colon carcinoma” is a subtype of “Colorectal carcinoma”). Then, for each topic, we apply different strategies of trials filtering - according to fields where the disease was identified - and hierarchies. Finally, classical information retrieval is performed with genes and variants as queries. The strictest filtering leads to an average of 62 retrieved trials per topic and tends to favor high precision, while the most relaxed filtering leads to an average of 379 retrieved trials per topic and tends to favor high recall. Yet, results show that the Precision values are poorly impacted by these strategies, while runs that favor Recall showed a better general behavior for this task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PascheGMMTRR17.bib) "
	```
	@inproceedings{DBLP:conf/trec/PascheGMMTRR17,
		author = {Emilie Pasche and Julien Gobeill and Luc Mottin and Ana{\"{\i}}s Mottaz and Douglas Teodoro and Paul Van Rijen and Patrick Ruch},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Customizing a Variant Annotation-Support Tool: an Inquiry into Probability Ranking Principles for {TREC} Precision Medicine},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/BiTeM-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PascheGMMTRR17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Identifying Personalised Treatments and Clinical Trials for Precision  Medicine using Semantic Search with Thalia

_Piotr Przybyla, Axel J. Soto, Sophia Ananiadou_

- :fontawesome-solid-user-group: **Participant:** [NaCTeM](./participants.md#nactem)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/NaCTeM-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/NaCTeM-PM.pdf)
- :material-file-search: **Runs:** [Textual](./runs.md#textual) | [Ontological](./runs.md#ontological) | [Broad](./runs.md#broad) | [Semantic](./runs.md#semantic) | [Focused](./runs.md#focused) | [Textualc](./runs.md#textualc) | [Ontologicalc](./runs.md#ontologicalc) | [Broadc](./runs.md#broadc) | [Semanticc](./runs.md#semanticc) | [Focusedc](./runs.md#focusedc)

??? abstract "Abstract"
	
	This paper reports the main methods applied in our submission to TREC 2017 Precision Medicine Track. The goal of this challenge was to retrieve documents containing potential treatments and clinical trials for specific patient characteristics. Our main strategy involved using a semantic search engine called Thalia (Text mining for Highlighting, Aggregating and Linking Information in Articles), which allows the recognition of diseases and genes mentioned in text. The recognition of named entities and its linking to concepts in ontologies facilitates more accurate retrieval than just relying on plain textual search and matching. We also highlight the different strategies applied when querying Thalia in the context of this Precision Medicine challenge, which aimed to support different use cases (i.e. more focused or broader searches).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PrzybylaSA17.bib) "
	```
	@inproceedings{DBLP:conf/trec/PrzybylaSA17,
		author = {Piotr Przybyla and Axel J. Soto and Sophia Ananiadou},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Identifying Personalised Treatments and Clinical Trials for Precision Medicine using Semantic Search with Thalia},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/NaCTeM-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PrzybylaSA17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ranking Clinical Trials Using Elasticsearch

_Ajinkya Yogesh Thorve, Haimonti Dutta_

- :fontawesome-solid-user-group: **Participant:** [TREC_UB](./participants.md#trec_ub)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/TREC_UB-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/TREC_UB-PM.pdf)
- :material-file-search: **Runs:** [1_ec_simple](./runs.md#1_ec_simple) | [2_ec_complex](./runs.md#2_ec_complex)

??? abstract "Abstract"
	
	The clinical trials task of the TREC 2017 Precision Medicine Track was designed to represent the potential for connecting patients with experimental treatments if existing treatments were ineffective. Participants were challenged with the task of retrieving appropriate clinical trials from ClinicalTrials.gov for which a patient is eligible. This paper presents an approach to solving the problem by first preparing an index for the clinical trial descriptions based on specific tags in the XML files and querying them using Elasticsearch. Initial results indicate that our approach performed very well for certain kinds of queries - however, more tuning may be required for ensuring generalizable results from the search.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ThorveD17.bib) "
	```
	@inproceedings{DBLP:conf/trec/ThorveD17,
		author = {Ajinkya Yogesh Thorve and Haimonti Dutta},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Ranking Clinical Trials Using Elasticsearch},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/TREC\_UB-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ThorveD17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UNT Precision Medicine Information Retrieval at TREC 2017

_Lokesh Kumar Viswavarapu, Jiangping Chen, Ana D. Cleveland, Haihua Chen_

- :fontawesome-solid-user-group: **Participant:** [UNTIIA](./participants.md#untiia)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/UNTIIA-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/UNTIIA-PM.pdf)
- :material-file-search: **Runs:** [UNTIIADW](./runs.md#untiiadw) | [UNTIIASY](./runs.md#untiiasy) | [UNTIIAIS](./runs.md#untiiais) | [UNTIIAGA](./runs.md#untiiaga) | [UNTIIALQ](./runs.md#untiialq) | [UNTIIACTDW](./runs.md#untiiactdw) | [UNTIIACTSY](./runs.md#untiiactsy) | [UNTIIACTIS](./runs.md#untiiactis) | [UNTIIACTGA](./runs.md#untiiactga) | [UNTIIACTLQ](./runs.md#untiiactlq)

??? abstract "Abstract"
	
	This paper reports our participation in TREC 2017 Precision Medicine (PM) track. Based on our TREC 2016 Clinical Decision Support System, we implemented and tested five different query construction strategies: Query construction with disease weighted terms, with synonyms of disease terms, with Internet search results, with gene alias terms, and with Terrier logical query language. A re-ranking strategy that considered the occurrence of disease names, gene names, and treatment terms were applied to adjust the order of the retrieved documents. A new experimental module called Relevance Judgment User System (RJUS), which is an augmentation to the information retrieval platform Terrier1 v4.2, was designed to facilitate the design of query construction and result re-ranking strategies. We submitted 5 runs applying the five query construction strategies respectively combining with pseudo relevance feedback and the reranking approach. The query construction with Terrier logical query language achieved the best performance among our submitted results. Our future study will investigate the use of topic modeling for query construction and effective approaches for finding relevant clinical trials.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ViswavarapuCCC17.bib) "
	```
	@inproceedings{DBLP:conf/trec/ViswavarapuCCC17,
		author = {Lokesh Kumar Viswavarapu and Jiangping Chen and Ana D. Cleveland and Haihua Chen},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UNT} Precision Medicine Information Retrieval at {TREC} 2017},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/UNTIIA-PM.pdf},
		timestamp = {Thu, 23 Dec 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ViswavarapuCCC17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Term-based and Concept-based Representation for Clinical  Retrieval

_Yue Wang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/udel_fang-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/udel_fang-PM.pdf)
- :material-file-search: **Runs:** [UDInfoPMCT3](./runs.md#udinfopmct3) | [UDInfoPMCT4](./runs.md#udinfopmct4) | [UDInfoPMCT6](./runs.md#udinfopmct6) | [UDInfoPMCT10](./runs.md#udinfopmct10) | [UDInfoPMSA2](./runs.md#udinfopmsa2) | [UDInfoPMSA3](./runs.md#udinfopmsa3) | [UDInfoPMSA5](./runs.md#udinfopmsa5) | [UDInfoPMSA6](./runs.md#udinfopmsa6) | [UDInfoPMSA7](./runs.md#udinfopmsa7) | [UDInfoPMCT8](./runs.md#udinfopmct8)

??? abstract "Abstract"
	
	Biomedical domain retrieval has been a trending topic that attracts many IR researchers. Different document representation methods, i.e., term based representation and concept based representation, have been proposed to solve this question. However, previous studies have focused the verbose queries. In this year's Precision Medicine track, we evaluated the performance of these two basic document representation methods on short queries. We also explored possible ways to combine these two methods. The results show that these two representations perform differently on the scientific abstract and clinical trail data sets. Simply merge the results list may not leads to optimal performance, while term based filtering on top of the concept based results could significantly improve the performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Wang017.bib) "
	```
	@inproceedings{DBLP:conf/trec/Wang017,
		author = {Yue Wang and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Combining Term-based and Concept-based Representation for Clinical Retrieval},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/udel\_fang-PM.pdf},
		timestamp = {Thu, 17 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Wang017.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HokieGo at 2017 PM Task: Genetic Programming based re-ranking method  In Biomedical Information Retrieval

_Junyan Wu, Xiaofu Ma, Weiguo Fan_

- :fontawesome-solid-user-group: **Participant:** [HokieGo](./participants.md#hokiego)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/HokieGo-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/HokieGo-PM.pdf)
- :material-file-search: **Runs:** [GP16Medline](./runs.md#gp16medline) | [GP16Trail](./runs.md#gp16trail) | [GP14Medline](./runs.md#gp14medline) | [GP14Trail](./runs.md#gp14trail)

??? abstract "Abstract"
	
	This paper summarizes our efforts on TREC 2017 Precision Medicine Track. We present a genetic programming based learning-to-rank algorithm. We perform two training experiments on 2014 and 2016 TREC CDS data and apply the pre-trained model as re-ranking method to improve the performance. In addition, two utility functions, CHK and FFP4, have been used for the training optimization.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuMF17.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuMF17,
		author = {Junyan Wu and Xiaofu Ma and Weiguo Fan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {HokieGo at 2017 {PM} Task: Genetic Programming based re-ranking method In Biomedical Information Retrieval},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/HokieGo-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuMF17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Retrieving documents based on gene name variations: MedIER at TREC  2017 Precision Medicine Track

_Tong Yin, Danny T. Y. Wu, V. G. Vinod Vydiswaran_

- :fontawesome-solid-user-group: **Participant:** [MedIER](./participants.md#medier)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/MedIER-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/MedIER-PM.pdf)
- :material-file-search: **Runs:** [MedIER_sa2](./runs.md#medier_sa2) | [MedIER_sa1](./runs.md#medier_sa1) | [MedIER_sa4](./runs.md#medier_sa4) | [MedIER_sa3](./runs.md#medier_sa3) | [MedIER_ct1](./runs.md#medier_ct1) | [MedIER_ct2](./runs.md#medier_ct2) | [MedIER_ct3](./runs.md#medier_ct3) | [MedIER_ct4](./runs.md#medier_ct4)

??? abstract "Abstract"
	
	The TREC 2017 Precision Medicine Track focused on finding relevant medical documents - scientific abstracts and clinical trials - for cancer patient cases based on specific genetic variation and demographic information. We focused on the genetic variations mentioned in the query and explored ways to modify the search query and the retrieval ranking using this information. Further, we explored filtering retrieved results based on demographic information matching for clinical trials. The results show little improvements of the approaches over baseline runs, and suggest need for additional exploration.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YinWV17.bib) "
	```
	@inproceedings{DBLP:conf/trec/YinWV17,
		author = {Tong Yin and Danny T. Y. Wu and V. G. Vinod Vydiswaran},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Retrieving documents based on gene name variations: MedIER at {TREC} 2017 Precision Medicine Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/MedIER-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YinWV17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Leveraging both Structured and Unstructured Data for Precision Information  Retrieval

_Yanshan Wang, Ravikumar Komandur Elayavilli, Majid Rastegar-Mojarad, Hongfang Liu_

- :fontawesome-solid-user-group: **Participant:** [MayoNLPTeam](./participants.md#mayonlpteam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/MayoNLPTeam_PM.pdf](https://trec.nist.gov/pubs/trec26/papers/MayoNLPTeam_PM.pdf)
- :material-file-search: **Runs:** [mayonlppm1](./runs.md#mayonlppm1) | [mayonlppm2](./runs.md#mayonlppm2) | [mayonlppm3](./runs.md#mayonlppm3) | [mayonlppm4](./runs.md#mayonlppm4) | [mayonlppm5](./runs.md#mayonlppm5) | [mayonlpct1](./runs.md#mayonlpct1) | [mayonlpct2](./runs.md#mayonlpct2) | [mayonlpct3](./runs.md#mayonlpct3) | [mayonlpct4](./runs.md#mayonlpct4) | [mayonlpct5](./runs.md#mayonlpct5)

??? abstract "Abstract"
	
	This paper describes the participation of the Mayo Clinic NLP team in the Text REtreival Conference (TREC) 2017 Precision Medicine track. The novelty of our systems is four-fold. First, compared to our submissions in the previous year, our systems utilized an enhanced named entity recognition (NER) method to extract genes, variants, proteins, and diseases from PubMed articles. This NER method combined several state-of-the-art NER tools including TaggerOne, beCAS, Reach and tmVAR. The extracted entities were indexed in different fields and treated as structured data for retrieval. Second, we used multi-field querying in a Pseudo Relevance Feedback (PRF) model. We first query the unstructured fields (i.e., the fields of title and abstract) and utilize information in structured fields from top-ranked documents as feedback for query expansion. Third, we explored the use of MeSH on Demand, a web service identifying MeSH terms in free-text and recommending similar PubMed articles which are relevant to the text, to boost the performance of our retrieval systems. The reason we used MeSH on Demand is due to its effectiveness for recommending relevant PubMed articles based on our manual judgments. Fourth, we utilized the demographic information (i.e., age and sex) as structured data to filter out the clinical trials that did not meet the criteria in each topic.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangERL17.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangERL17,
		author = {Yanshan Wang and Ravikumar Komandur Elayavilli and Majid Rastegar{-}Mojarad and Hongfang Liu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Leveraging both Structured and Unstructured Data for Precision Information Retrieval},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/MayoNLPTeam\_PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangERL17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

