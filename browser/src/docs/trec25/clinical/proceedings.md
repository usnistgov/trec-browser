# Proceedings - Clinical Decision Support 2016 

#### Overview of the TREC 2016 Clinical Decision Support Track

_Kirk Roberts, Dina Demner-Fushman, Ellen M. Voorhees, William R. Hersh_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/Overview-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/Overview-CL.pdf)
??? abstract "Abstract"
	
	In handling challenging cases, clinicians often seek out information to make better decisions in patient care. Typically, these information sources combine clinical experience with scientific medical research in a process known as evidence-based medicine (EBM). Information relevant to a physician can be related to a variety of clinical tasks, such as (i) determining a patient's most likely diagnosis given a list of symptoms, (ii) determining if a particular test is indicated for a given situation, and (iii) deciding on the most effective treatment plan for a patient having a known condition. Finding the most relevant and recent research, however, can be quite challenging due to the volume of scientific literature and the pace at which new research is published. As such, the time-consuming nature of information seeking means that most clinician questions go unanswered (Ely et al., 2005). In order to better enable access to the scientific literature in the clinical setting, research is necessary to evaluate information retrieval methods that connect clinical notes with the published literature. The TREC Clinical Decision Support (CDS) track simulates the information retrieval requirements of such systems to encourage the creation of tools and resources necessary for their implementation. In 2014 and 2015, the CDS tracks used simulated patient cases presented as if they were typical case reports used in medical education. However, in an actual electronic health record (EHR), patient notes are written in a much different manner, notably with terse language and heavy use of abbreviations and clinical jargon. To address the challenge specific to EHR notes, the 2016 CDS track used de-identified notes for actual patients. This enabled participants to experiment with a realistic topic/query and develop methods to handle the challenging nature of clinical text. For a given EHR note, participants were challenged with retrieving full-text biomedical articles relevant for answering questions related to one of three generic clinical information needs: Diagnosis (i.e., “What is this patient's diagnosis?”), Test (“What diagnostic test is appropriate for this patient?”), and Treatment (“What treatment is appropriate for this patient?”). Retrieved articles were judged relevant if they provided information of the specified type useful for the given case. The assessment was performed by physicians with training in biomedical informatics using a 3-point scale: relevant, partially relevant, not relevant. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsDVH16.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsDVH16,
		author = {Kirk Roberts and Dina Demner{-}Fushman and Ellen M. Voorhees and William R. Hersh},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2016 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/Overview-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsDVH16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NLM NIH at TREC 2016 Clinical Decision Support Track

_Asma Ben Abacha_

- :fontawesome-solid-user-group: **Participant:** [NLM_NIH](./participants.md#nlm_nih)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/NLM_NIH-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/NLM_NIH-CL.pdf)
- :material-file-search: **Runs:** [NLMrun1](./runs.md#nlmrun1) | [NLMrun2](./runs.md#nlmrun2) | [NLMrun3](./runs.md#nlmrun3) | [NLMrun4](./runs.md#nlmrun4) | [NLMrun5](./runs.md#nlmrun5)

??? abstract "Abstract"
	
	In this paper, we present our approach for TREC 2016 Clinical Decision Support (CDS) track. We combined methods for question analysis, query expansion, document retrieval and result fusion to find relevant documents to a given clinical question. We submitted three automatic runs using the summaries and two automatic runs using the notes, provided for the first time at the CDS track. Our experiments showed that query expansion and rank-based result fusion led to the best performance. Our runs exploring the clinical notes used MeSH for topic analysis and achieved our best P10 score of 0.2533. Using the summaries, we obtained an infNDCG score of 0.1872 and a R-prec score of 0.1465 (score in the top 10 of 107 automatic runs submitted to the 2016 CDS track).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Abacha16.bib) "
	```
	@inproceedings{DBLP:conf/trec/Abacha16,
		author = {Asma Ben Abacha},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{NLM} {NIH} at {TREC} 2016 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/NLM\_NIH-CL.pdf},
		timestamp = {Wed, 03 Feb 2021 08:31:25 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Abacha16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Augmenting Medical Queries with UMLS Concepts via MetaMap

_Christopher Agrafiotes, Avi Arampatzis_

- :fontawesome-solid-user-group: **Participant:** [DUTH](./participants.md#duth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/DUTH-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/DUTH-CL.pdf)
- :material-file-search: **Runs:** [DUTHsaRPF](./runs.md#duthsarpf) | [DUTHmaRPF](./runs.md#duthmarpf) | [DUTHaaRPF](./runs.md#duthaarpf)

??? abstract "Abstract"
	
	This report is an overview of the methods used by the Democritus University of Thrace team (DUTH) at the Clinical Decision Support (CDS) Track of the 25th Text REtrieval Conference (TREC). We investigated the concept of atoms from the United Medical Language System (UMLS) as a method to augment medical queries. We ultimately found that massively augmenting queries with too many words leads to a decreased overall performance, whereas adding a few specific words works reasonably well boosting the baseline effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AgrafiotesA16.bib) "
	```
	@inproceedings{DBLP:conf/trec/AgrafiotesA16,
		author = {Christopher Agrafiotes and Avi Arampatzis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Augmenting Medical Queries with {UMLS} Concepts via MetaMap},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/DUTH-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AgrafiotesA16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Evaluation of a Machine Learning Method to Rank PubMed Central Articles  For Clinical Relevancy: NCH at TREC 2016 Clinical Decision Support  Track

_Wei Chen, Soheil Moosavinasab, Steve Rust, Yungui Huang, Simon M. Lin, Anna Zemke, Ariana Prinzbach_

- :fontawesome-solid-user-group: **Participant:** [nch_risi](./participants.md#nch_risi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/nch_risi-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/nch_risi-CL.pdf)
- :material-file-search: **Runs:** [SumClsRerank](./runs.md#sumclsrerank) | [SumCmbRank](./runs.md#sumcmbrank) | [SumES](./runs.md#sumes) | [ManualRun](./runs.md#manualrun) | [NoteES](./runs.md#notees)

??? abstract "Abstract"
	
	The goal of the TREC 2016 Clinical Decision Support track is to retrieve and rank PubMed Central (PMC) articles that are relevant to potential tests, treatments or diagnoses of a patient case narrative. Our objective was to develop a machine learning method to rank PMC articles by taking advantage of the previous years' gold standard TREC competition results. The classifier we trained on 2014 data achieved high accuracy when tested with 2015 data (P10=0.59 and infNDCG=0.67) compared with the Elasticsearch method (P10=0.19 and infNDCG=0.22). However, when we applied the same classifier approach with both the 2014 and 2015 data sets combined, and then tested this method against the 2016 cases, the results did not improve over the Elasticsearch method. We concluded that although the machine learning approach was found effective on predicting previous years' results, it was not as effective for 2016 data, most likely due to the change in the topic structures.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenMRHLZP16.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenMRHLZP16,
		author = {Wei Chen and Soheil Moosavinasab and Steve Rust and Yungui Huang and Simon M. Lin and Anna Zemke and Ariana Prinzbach},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Evaluation of a Machine Learning Method to Rank PubMed Central Articles For Clinical Relevancy: {NCH} at {TREC} 2016 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/nch\_risi-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenMRHLZP16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PUT Contribution to TREC CDS 2016

_Jakub Dutkiewicz, Czeslaw Jedrzejek, Michal Frackowiak, Pawel Werda_

- :fontawesome-solid-user-group: **Participant:** [IAII_PUT](./participants.md#iaii_put)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/IAII_PUT-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/IAII_PUT-CL.pdf)
- :material-file-search: **Runs:** [SDPHBo1NE](./runs.md#sdphbo1ne) | [DDPHBo1MWRe](./runs.md#ddphbo1mwre) | [DDPHBo1CM](./runs.md#ddphbo1cm) | [NDPHBo1C](./runs.md#ndphbo1c) | [NDPHBo1CM](./runs.md#ndphbo1cm)

??? abstract "Abstract"
	
	This paper describes the medical information retrieval systems designed by the Poznan University of Technology of for clinical decision support CDS) which were submitted to the TREC 2016. The baseline is the Terrier DPH Bo1 which recently has been shown to be the most effective Terrier option. We also used Mesh query expansion, word2vec query expansion, and the combination of these two options. In all measures our results are approximately 0,02 above the median.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DutkiewiczJFW16.bib) "
	```
	@inproceedings{DBLP:conf/trec/DutkiewiczJFW16,
		author = {Jakub Dutkiewicz and Czeslaw Jedrzejek and Michal Frackowiak and Pawel Werda},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{PUT} Contribution to {TREC} {CDS} 2016},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/IAII\_PUT-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DutkiewiczJFW16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ETH Zurich at TREC Clinical Decision Support 2016

_Simon Greuter, Philip Junker, Lorenz Kuhn, Felix Mance, Virgile Mermet, Angela Rellstab, Carsten Eickhoff_

- :fontawesome-solid-user-group: **Participant:** [ETH](./participants.md#eth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/ETH-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/ETH-CL.pdf)
- :material-file-search: **Runs:** [ETHNote](./runs.md#ethnote) | [ETHSumm](./runs.md#ethsumm) | [ETHDescRR](./runs.md#ethdescrr) | [ETHNoteRR](./runs.md#ethnoterr) | [ETHSummRR](./runs.md#ethsummrr)

??? abstract "Abstract"
	
	This paper describes ETH Zurich's submission to the TREC 2016 Clinical Decision Support (CDS) track. In three successive stages, we apply query expansion based on literal as well as semantic term matches, rank documents in a negation-aware manner and, finally, re-rank them based on clinical intent types as well as semantic and conceptual affinity to the medical case in question. Empirical results show that the proposed method can distill patient representations from raw clinical notes that result in a retrieval performance superior to that of manually constructed case descriptions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GreuterJKMMRE16.bib) "
	```
	@inproceedings{DBLP:conf/trec/GreuterJKMMRE16,
		author = {Simon Greuter and Philip Junker and Lorenz Kuhn and Felix Mance and Virgile Mermet and Angela Rellstab and Carsten Eickhoff},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ETH} Zurich at {TREC} Clinical Decision Support 2016},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/ETH-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GreuterJKMMRE16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Semi-Supervised Information Retrieval System for Clinical Decision  Support

_Harsha Gurulingappa, Luca Toldo, Claudia Schepers, Alexander Bauer, Gerard Megaro_

- :fontawesome-solid-user-group: **Participant:** [MERCKKGAA](./participants.md#merckkgaa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/MERCKKGAA-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/MERCKKGAA-CL.pdf)
- :material-file-search: **Runs:** [MrkUmlsXgb](./runs.md#mrkumlsxgb) | [MRKUmlsSolr](./runs.md#mrkumlssolr) | [MRKPrfNote](./runs.md#mrkprfnote) | [MRKSumCln](./runs.md#mrksumcln)

??? abstract "Abstract"
	
	This article summarizes the approach developed for TREC 2016 Clinical Decision Support Track. In order to address the daunting challenge of retrieval of biomedical articles for answering clinical questions, an information retrieval methodology was developed that combines pseudo -relevance feedback, semantic query expansion and document similarity measures based on unsupervised word embeddings. The individual relevance metrics were combined through a supervised learning -to-rank model based on gradient boosting to maximize the normalized discounted cumulative gain (nDCG). Experimental results show that document distance measures derived from unsupervised word embeddings contribute to significant ranking improvements when combined with traditional document retrieval approaches.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GurulingappaTSB16.bib) "
	```
	@inproceedings{DBLP:conf/trec/GurulingappaTSB16,
		author = {Harsha Gurulingappa and Luca Toldo and Claudia Schepers and Alexander Bauer and Gerard Megaro},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Semi-Supervised Information Retrieval System for Clinical Decision Support},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/MERCKKGAA-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GurulingappaTSB16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Clinical Question Answering using Key-Value Memory Networks and Knowledge  Graph

_Sadid A. Hasan, Siyuan Zhao, Vivek V. Datla, Joey Liu, Kathy Lee, Ashequl Qadir, Aaditya Prakash, Oladimeji Farri_

- :fontawesome-solid-user-group: **Participant:** [prna](./participants.md#prna)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/prna-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/prna-CL.pdf)
- :material-file-search: **Runs:** [prna2desc](./runs.md#prna2desc) | [prna3note](./runs.md#prna3note) | [prna4note](./runs.md#prna4note) | [prna5note](./runs.md#prna5note) | [prna1sum](./runs.md#prna1sum)

??? abstract "Abstract"
	
	We describe our clinical question answering system implemented for the Text Retrieval Conference (TREC 2016) Clinical Decision Support (CDS) track. We submitted five runs using a combination of knowledge-driven (based on a curated knowledge graph) and deep learning-based (using key-value memory networks) approaches to retrieve relevant biomedical articles for answering generic clin- ical questions (diagnoses, treatment, and test) for each clinical scenario provided in three forms: notes, descriptions, and summaries. The submitted runs were varied based on the use of notes, descriptions, or summaries in association with different diagnostic inferencing methodologies applied prior to biomedical article retrieval. Evaluation results demonstrate that our systems achieved best or close to best scores for 20% of the topics and better than median scores for 40% of the topics across all participants considering all evaluation measures. Further analysis shows that on average our clinical question answering system performed best with summaries using diagnostic inferencing from the knowledge graph whereas our key-value memory network model with notes consistently outperformed the knowledge graph-based system for notes and descriptions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HasanZDLLQPF16.bib) "
	```
	@inproceedings{DBLP:conf/trec/HasanZDLLQPF16,
		author = {Sadid A. Hasan and Siyuan Zhao and Vivek V. Datla and Joey Liu and Kathy Lee and Ashequl Qadir and Aaditya Prakash and Oladimeji Farri},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Clinical Question Answering using Key-Value Memory Networks and Knowledge Graph},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/prna-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HasanZDLLQPF16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CBNU at TREC 2016 Clinical Decision Support Track

_Seung-Hyeon Jo, Kyung-Soon Lee_

- :fontawesome-solid-user-group: **Participant:** [cbnu](./participants.md#cbnu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/cbnu-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/cbnu-CL.pdf)
- :material-file-search: **Runs:** [cbnus1](./runs.md#cbnus1) | [cbnus2](./runs.md#cbnus2) | [cbnun1](./runs.md#cbnun1)

??? abstract "Abstract"
	
	This paper describes the participation of the CBNU team at the TREC Precision Medicine Track 2017. We have constructed cancer-centered document clusters using cancer-gene relation and clinical causal information. A query has been expanded with disease terms and pseudo-relevance feedback is applied for cancer disease document clusters.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JoL16.bib) "
	```
	@inproceedings{DBLP:conf/trec/JoL16,
		author = {Seung{-}Hyeon Jo and Kyung{-}Soon Lee},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CBNU} at {TREC} 2016 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/cbnu-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JoL16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CSIRO at TREC Clinical Decision Support Track

_Sarvnaz Karimi, Sara Falamaki, Vincent Nguyen_

- :fontawesome-solid-user-group: **Participant:** [CSIROmed](./participants.md#csiromed)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/CSIROmed-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/CSIROmed-CL.pdf)
- :material-file-search: **Runs:** [CSIROmnul](./runs.md#csiromnul) | [CSIROnote](./runs.md#csironote) | [CSIROdSum](./runs.md#csirodsum) | [CSIROsumm](./runs.md#csirosumm) | [CSIROmeta](./runs.md#csirometa)

??? abstract "Abstract"
	
	We report on the participation of the CSIRO1 team, named as CSIROmed, in the TREC 2016 Clinical Decision Support Track. We submitted three automatic runs and and one manual run. Our best submitted run was the manual run using the summaries. We expanded the summaries with synonyms of diseases, metamap concepts, abbreviations as well as boosting phrases. We also report on experiments post TREC conference, where we analyse effectiveness of some of query processing methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KarimiFN16.bib) "
	```
	@inproceedings{DBLP:conf/trec/KarimiFN16,
		author = {Sarvnaz Karimi and Sara Falamaki and Vincent Nguyen},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CSIRO} at {TREC} Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/CSIROmed-CL.pdf},
		timestamp = {Thu, 21 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KarimiFN16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Siena's Clinical Decision Assistant with Machine Learning

_Brendan Kish, Thomas Walsh, Katherine Small, Steven Gassert, Kylie Small, Sharon Gower Small_

- :fontawesome-solid-user-group: **Participant:** [SCIAICLTeam](./participants.md#sciaiclteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/SCIAICLTeam-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/SCIAICLTeam-CL.pdf)
- :material-file-search: **Runs:** [LucBase](./runs.md#lucbase) | [LucNote](./runs.md#lucnote) | [LucWghtFrame](./runs.md#lucwghtframe) | [LucNoteFrame](./runs.md#lucnoteframe) | [LucWeight](./runs.md#lucweight)

??? abstract "Abstract"
	
	This paper discusses Siena's Clinical Decision Assistant's (SCDA) system and its participation in the Text Retrieval Conference (TREC) Clinical Decision Support Track (CDST) of 2016. The overall goal of this track is to link medical cases to information that is pertinent to patient care. Participants were given a set of thirty topics in the form of medical case narratives and a snapshot of 1.25 million articles from PubMed Central (PMC). This snapshot was taken on March 28, 2016. New this year is that actual electronic health records (EHR) were used instead of synthetic cases. Admission notes from the MIMIC-III database were used to generate the topics. TREC describes the EHR notes as something that “describes a patient's chief complaint, relevant medical history, and any other information obtained during the first few hours of a patient's hospital stay, such as lab work.” Each topic consists of three fields. There is a new field this year, the admission notes, which is the actual admission's data generated by the clinicians (mostly physicians, including residents, and nurses). The other two fields continue from last year: the description field, which is a layman-terms account of the patient visit, and a summary field , which is typically a one or two sentence summary of the main points of the visit. The thirty topics were annotated in three major subsets: diagnosis, test and treatment, with ten of each type. SCDA used several methods to attempt to improve the accuracy of medical cases retrieved. SCDA used the metathesaurus Unified Medical Language System (UMLS) that was implemented using MetaMap (NIH, 2013), machine learning and query and document framing (Small and Stzalkowski, 2004). SCDA also used Lucene for initial document indexing and retrieval. The track received a total of 115 runs from 26 different groups. We submitted two notes runs where our highest P(10) run was 0.16 and three runs where we used just the summary field and our highest P(10) was 0.2767. The average P(10) from CDST TREC 2015 Task A was 0.33, with a low of .0867 and a high of 0.4733. Our best Task A run last year had a P(10) of 0.3767. The work described here was performed by a team of undergraduate researchers working together for just ten weeks during the summer of 2016. The team was funded under the Siena College Institute for Artificial Intelligence's National Science Foundation's Research Experience for Undergraduates Grant.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KishWSGSS16.bib) "
	```
	@inproceedings{DBLP:conf/trec/KishWSGSS16,
		author = {Brendan Kish and Thomas Walsh and Katherine Small and Steven Gassert and Kylie Small and Sharon Gower Small},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Siena's Clinical Decision Assistant with Machine Learning},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/SCIAICLTeam-CL.pdf},
		timestamp = {Tue, 15 Nov 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KishWSGSS16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Literature based Clinical Decision Support: Searching Articles According  to Medical Needs

_Baoli Li, Jikang Xiao, Shigen Jiang, Zhen Wang, Haoqi Ding, Yaojun Niu_

- :fontawesome-solid-user-group: **Participant:** [HAUT](./participants.md#haut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/HAUT-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/HAUT-CL.pdf)
- :material-file-search: **Runs:** [nacmmf](./runs.md#nacmmf) | [dacmmf](./runs.md#dacmmf) | [sacmmf](./runs.md#sacmmf)

??? abstract "Abstract"
	
	Physicians often seek helps from scientific medical literature for better diagnoses and treatment, especially when dealing with intractable cases. The task is becoming more and more difficult as thousands of new articles are published every month. It's quite challenging and helpful to assist physicians locating highly relevant articles in limited time. In this study, targeting at fulfilling the task of the TREC-2016 Clinical Decision Support track, we explore effective methods to search medical articles according to physicians' information needs. The best solution we obtained takes the following strategies: using Medical Text Indexer for query expansion, concentrating on articles with abstracts, tagging articles according to different information needs, and combining results of multiple models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiXJWDN16.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiXJWDN16,
		author = {Baoli Li and Jikang Xiao and Shigen Jiang and Zhen Wang and Haoqi Ding and Yaojun Niu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Literature based Clinical Decision Support: Searching Articles According to Medical Needs},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/HAUT-CL.pdf},
		timestamp = {Mon, 24 Aug 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LiXJWDN16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ECNU at TREC 2016: Web-based query expansion and experts diagnosis  in Medical Information Retrieval

_Hongyu Liu, Yang Song, Yun He, Yueyao Wang, Qinmin Hu, Liang He_

- :fontawesome-solid-user-group: **Participant:** [ECNU](./participants.md#ecnu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/ECNU-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/ECNU-CL.pdf)
- :material-file-search: **Runs:** [ECNUmanual](./runs.md#ecnumanual) | [ECNUrun3](./runs.md#ecnurun3) | [ECNUrun1](./runs.md#ecnurun1) | [ECNUrun5](./runs.md#ecnurun5) | [ECNUrun4](./runs.md#ecnurun4)

??? abstract "Abstract"
	
	In this paper, we present our work in TREC 2016 Clinical Decision Support Track. Among five submitted runs, two of them are based on summary topics and the others on note topics. In summary version run, we expand the original text with external data on web. Note topics are much longer than the summary, which contain a significant number of medical abbreviations as well as other linguistic jargon and style. An automatic method and a manual method are applied to process note topics. In the automatic method, we utilize KODA, a well-known knowledge drive annotator, to extract key information from the original text. In the manual one, we ask medical experts to diagnose and give their advice. For all of the five runs, we adopt Terrier search engine to implement various retrieval models. Furthermore, results combinations are applied to improve the performance of our model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuSHWHHLSHWHH16.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuSHWHHLSHWHH16,
		author = {Hongyu Liu and Yang Song and Yun He and Yueyao Wang and Qinmin Hu and Liang He},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ECNU} at {TREC} 2016: Web-based query expansion and experts diagnosis in Medical Information Retrieval},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/ECNU-CL.pdf},
		timestamp = {Tue, 22 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LiuSHWHHLSHWHH16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Team DA IICT at Clinical Decision Support Track in TREC 2016:  Topic Modeling for Query Expansion

_Jainisha Sankhavara, Prasenjit Majumder_

- :fontawesome-solid-user-group: **Participant:** [DA_IICT](./participants.md#da_iict)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/DA_IICT-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/DA_IICT-CL.pdf)
- :material-file-search: **Runs:** [DAsummTM](./runs.md#dasummtm) | [DAdescTM](./runs.md#dadesctm) | [DAnoteTM](./runs.md#danotetm) | [DAnoteRoc](./runs.md#danoteroc) | [DAnote](./runs.md#danote)

??? abstract "Abstract"
	
	Clinical Decision Support (CDS) task aims to find the biomedical literature articles related to medical case reports. These articles should help to get answers to the questions of generic clinical types. This paper reports the results on query expansion using topic modeling on CDS-2016 data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SankhavaraM16.bib) "
	```
	@inproceedings{DBLP:conf/trec/SankhavaraM16,
		author = {Jainisha Sankhavara and Prasenjit Majumder},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Team {DA} {IICT} at Clinical Decision Support Track in {TREC} 2016: Topic Modeling for Query Expansion},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/DA\_IICT-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SankhavaraM16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UNT Medical Information Retrieval at TREC 2016

_Lokesh Kumar Viswavarapu, Jiangping Chen, Ana D. Cleveland, Jodi Philbrick_

- :fontawesome-solid-user-group: **Participant:** [UNTIIA](./participants.md#untiia)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/UNTIIA-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/UNTIIA-CL.pdf)
- :material-file-search: **Runs:** [UNTIIANA](./runs.md#untiiana) | [UNTIIANM](./runs.md#untiianm) | [UNTIIASA](./runs.md#untiiasa) | [UNTIIANMERG](./runs.md#untiianmerg) | [UNTIIASMERG](./runs.md#untiiasmerg)

??? abstract "Abstract"
	
	This paper provides a description of a project to design and evaluate an information retrieval system for clinical decision support track. The target document collection for retrieval consisted of 1.25 million biomedical related documents taken from the Open Access Subset of PubMed Central. The topics provided by TREC for query construction consisted of 30 patient narrative cases, each of which includes a Note section, a Description section, and a Summary section. The PMCID, title, abstract, keywords, subheadings of article body, introduction and conclusion paragraphs were extracted from the documents. Terrier was used as the platform for indexing and retrieval. Several models, including the LemurTF_IDF weighting model with pseudo relevancy feedback, were applied to retrieve and rank relevant documents. Out of the five runs submitted, two runs were performed by merging the retrieval results of top five individual weighting models, and the remaining three runs were obtained through passing three types of queries constructed, manually and automatically, using the Note and the Summary sections. The automatic runs are observed to receive a better performance than the manual runs. The automatic run using the Note section for query construction performed better than other runs. Overall performance of the system is around the median when compared to all TREC 2016 CDS Track submissions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ViswavarapuCCP16.bib) "
	```
	@inproceedings{DBLP:conf/trec/ViswavarapuCCP16,
		author = {Lokesh Kumar Viswavarapu and Jiangping Chen and Ana D. Cleveland and Jodi Philbrick},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UNT} Medical Information Retrieval at {TREC} 2016},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/UNTIIA-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ViswavarapuCCP16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WHUIRGroup at TREC 2016 Clinical Decision Support Task

_Ruixue Wang, Heng Ding, Wei Lu_

- :fontawesome-solid-user-group: **Participant:** [WHUIRGroup](./participants.md#whuirgroup)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/WHUIRGroup-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/WHUIRGroup-CL.pdf)
- :material-file-search: **Runs:** [WHUIRGroup1](./runs.md#whuirgroup1) | [WHUIRGroup2](./runs.md#whuirgroup2) | [WHUIRGroup4](./runs.md#whuirgroup4) | [WHUIRGroup6](./runs.md#whuirgroup6) | [WHUIRGroup5](./runs.md#whuirgroup5)

??? abstract "Abstract"
	
	The goal of Clinical Decision Support(CDS) is to help physicians find academic papers in PubMed, and link medical records to information relevant for patient care. Participants attending the track have access to a data collection which is a snapshot of 1.25 million articles from PubMed Central (PMC) and a set of 30 topics which are EHR admission notes curated by physicians in the real condition from the MIMIC-III data. Our CDS systems are based on Indri toolkit, using Continuous Space Word Vectors expanding the queries. The 2015 topics and results are used to train the re-rank model, using the LambdaMART rank algorithms. The evaluation of run submissions are used partially marked results which is a promising methodologies.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangDL16.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangDL16,
		author = {Ruixue Wang and Heng Ding and Wei Lu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {WHUIRGroup at {TREC} 2016 Clinical Decision Support Task},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/WHUIRGroup-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangDL16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Extracting Useful Information from Clinical Notes

_Yue Wang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/udel_fang-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/udel_fang-CL.pdf)
- :material-file-search: **Runs:** [UDelInfoCDS1](./runs.md#udelinfocds1) | [UDelInfoCDS4](./runs.md#udelinfocds4) | [UDelInfoCDS5](./runs.md#udelinfocds5) | [UDelInfoCDS2](./runs.md#udelinfocds2) | [UDelInfoCDS3](./runs.md#udelinfocds3)

??? abstract "Abstract"
	
	A new type of query, i.e., note query, which contains plentiful information of the patients, is given in this year's CDS track. Previous results suggest that the additional information in the query may not lead to a better retrieval performance. Therefore, we proposed a method to extract important information from the clinical notes for retrieval. In addition, we also explored the expansion algorithms for abbreviation expansion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangF16.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangF16,
		author = {Yue Wang and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Extracting Useful Information from Clinical Notes},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/udel\_fang-CL.pdf},
		timestamp = {Thu, 17 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WangF16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Ensemble Model of Clinical Information Extraction and Information  Retrieval for Clinical Decision Support

_Yanshan Wang, Majid Rastegar-Mojarad, Ravikumar Komandur Elayavilli, Sijia Liu, Hongfang Liu_

- :fontawesome-solid-user-group: **Participant:** [MayoNLPTeam](./participants.md#mayonlpteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/MayoNLPTeam-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/MayoNLPTeam-CL.pdf)
- :material-file-search: **Runs:** [mayoas](./runs.md#mayoas) | [mayoad](./runs.md#mayoad) | [mayoan](./runs.md#mayoan) | [mayomd](./runs.md#mayomd) | [mayomn](./runs.md#mayomn)

??? abstract "Abstract"
	
	This paper describes the participation of Mayo Clinic NLP team in the Text REtreival Conference (TREC) 2016 Clinical Decision Support track. We propose an ensemble model which combines three components: a Part-of-Speech based query term weighting model (POS-BoW); a Markov Random Field model leveraging clinical information extraction (IE-MRF); and a Relevance Pseudo Feedback (RPF) model. We submitted three automatic runs and two manual runs. The experimental results show that the automatic runs outperform the median results of all participant teams for up to 76.7% of the given query topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangRELL16.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangRELL16,
		author = {Yanshan Wang and Majid Rastegar{-}Mojarad and Ravikumar Komandur Elayavilli and Sijia Liu and Hongfang Liu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {An Ensemble Model of Clinical Information Extraction and Information Retrieval for Clinical Decision Support},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/MayoNLPTeam-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangRELL16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CCNU at TREC 2016 Clinical Decision Support Track

_Yue Zhang, Po Hu, Fanghong Jian_

- :fontawesome-solid-user-group: **Participant:** [CCNU2016TREC](./participants.md#ccnu2016trec)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/CCNU2016TREC-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/CCNU2016TREC-CL.pdf)
- :material-file-search: **Runs:** [CCNUSUMR1](./runs.md#ccnusumr1) | [CCNUDESR2](./runs.md#ccnudesr2) | [CCNUNOTER1](./runs.md#ccnunoter1) | [CCNUNOTER2](./runs.md#ccnunoter2) | [CCNUNOTER3](./runs.md#ccnunoter3)

??? abstract "Abstract"
	
	The task of the clinical decision support track in TREC 2016 requires a system to retrieve and return the most relevant biomedical articles after giving the electronic health report as query. Firstly, we consider two important factors i.e., query length and specific term's occurrence, and adopt two models by the combination of a novel TF-IDF method and the traditional BM25. We name them as MATFB and MATFM respectively. Then, a linear combination of the two models which is denoted as NEWBM is considered. The experimental results show that different kinds of queries might prefer one of the three models, and our system performs better than the median performance on most metrics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangHJ16.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangHJ16,
		author = {Yue Zhang and Po Hu and Fanghong Jian},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CCNU} at {TREC} 2016 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/CCNU2016TREC-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangHJ16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Expansion with Automatically Predicted Diagnosis: iRiS at TREC  CDS track 2016

_Danchen Zhang, Daqing He, Sanqiang Zhao, Lei Li_

- :fontawesome-solid-user-group: **Participant:** [iris](./participants.md#iris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/iris-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/iris-CL.pdf)
- :material-file-search: **Runs:** [run1](./runs.md#run1) | [run2](./runs.md#run2) | [run3](./runs.md#run3) | [run4](./runs.md#run4) | [run5](./runs.md#run5)

??? abstract "Abstract"
	
	This paper describes the participation of the iRiS team from University of Pittsburgh in the TREC Clinical Decision Support (CDS) track in 2016. According to the track requirements, 1,000 most relevant biomedical articles from the PubMed Collection were retrieved based on information needs of 30 patients with their electronic health records (EHR) notes. Our approach focuses on using MetaMap to extract medical concepts, and using Wikipedia knowledge base to predict the patient diagnosis. Consequently, the original query is expanded with the predicted diagnosis before sent to search PubMed articles. Parameters were tuned based on CDS 2014 and 2015, and Indri is used to construct the index of the collection. Our automatic runs on description ranks 2nd and our manual runs on notes ranks 3rd in all submitted runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangHZL16.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangHZL16,
		author = {Danchen Zhang and Daqing He and Sanqiang Zhao and Lei Li},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Query Expansion with Automatically Predicted Diagnosis: iRiS at {TREC} {CDS} track 2016},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/iris-CL.pdf},
		timestamp = {Wed, 20 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangHZL16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NKU at TREC 2016: Clinical Decision Support Track

_Hualong Zhang, Liting Liu_

- :fontawesome-solid-user-group: **Participant:** [NKU](./participants.md#nku)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/NKU-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/NKU-CL.pdf)
- :material-file-search: **Runs:** [nkuRun5](./runs.md#nkurun5) | [nkuRun3](./runs.md#nkurun3) | [nkuRun2](./runs.md#nkurun2) | [nkuRun4](./runs.md#nkurun4) | [nkuRun1](./runs.md#nkurun1)

??? abstract "Abstract"
	
	This paper describes the participation of the NKU team at TREC2016 Clinical Decision Support track (CDS2016). The core problem is to find the most relevant literatures from the massive biomedical literatures according to the patient's condition and the needs of doctors. Unlike previous years' games, CDS2016 adds the note type querys[1], which are the original records from real clinical environment, apart from the summary and description topics. Our work involves three aspects: the expansion of the query, medical literature preprocessing and weight model selection. We use Terrier as the search engine to test the query expansion methods such as pseudo relevance feedback(PRF), MeSH synonym expansion, query type vocabulary expansion, and weighting models such as TF_IDF, BB2, In_expB2 and In_expC2. In the experiment, we build the model based on the CDS2015 data set and do performance evaluation. For both summary and description, we get NDCG values over 0.3.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangL16.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangL16,
		author = {Hualong Zhang and Liting Liu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{NKU} at {TREC} 2016: Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/NKU-CL.pdf},
		timestamp = {Fri, 09 Apr 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhangL16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

