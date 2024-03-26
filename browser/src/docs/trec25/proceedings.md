# Proceedings 2016 

## Clinical Decision Support 

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

- :fontawesome-solid-user-group: **Participant:** [NLM_NIH](./clinical/participants.md#nlm_nih)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/NLM_NIH-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/NLM_NIH-CL.pdf)
- :material-file-search: **Runs:** [NLMrun1](./clinical/runs.md#nlmrun1) | [NLMrun2](./clinical/runs.md#nlmrun2) | [NLMrun3](./clinical/runs.md#nlmrun3) | [NLMrun4](./clinical/runs.md#nlmrun4) | [NLMrun5](./clinical/runs.md#nlmrun5)

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

- :fontawesome-solid-user-group: **Participant:** [DUTH](./clinical/participants.md#duth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/DUTH-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/DUTH-CL.pdf)
- :material-file-search: **Runs:** [DUTHsaRPF](./clinical/runs.md#duthsarpf) | [DUTHmaRPF](./clinical/runs.md#duthmarpf) | [DUTHaaRPF](./clinical/runs.md#duthaarpf)

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

- :fontawesome-solid-user-group: **Participant:** [nch_risi](./clinical/participants.md#nch_risi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/nch_risi-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/nch_risi-CL.pdf)
- :material-file-search: **Runs:** [SumClsRerank](./clinical/runs.md#sumclsrerank) | [SumCmbRank](./clinical/runs.md#sumcmbrank) | [SumES](./clinical/runs.md#sumes) | [ManualRun](./clinical/runs.md#manualrun) | [NoteES](./clinical/runs.md#notees)

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

- :fontawesome-solid-user-group: **Participant:** [IAII_PUT](./clinical/participants.md#iaii_put)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/IAII_PUT-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/IAII_PUT-CL.pdf)
- :material-file-search: **Runs:** [SDPHBo1NE](./clinical/runs.md#sdphbo1ne) | [DDPHBo1MWRe](./clinical/runs.md#ddphbo1mwre) | [DDPHBo1CM](./clinical/runs.md#ddphbo1cm) | [NDPHBo1C](./clinical/runs.md#ndphbo1c) | [NDPHBo1CM](./clinical/runs.md#ndphbo1cm)

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

- :fontawesome-solid-user-group: **Participant:** [ETH](./clinical/participants.md#eth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/ETH-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/ETH-CL.pdf)
- :material-file-search: **Runs:** [ETHNote](./clinical/runs.md#ethnote) | [ETHSumm](./clinical/runs.md#ethsumm) | [ETHDescRR](./clinical/runs.md#ethdescrr) | [ETHNoteRR](./clinical/runs.md#ethnoterr) | [ETHSummRR](./clinical/runs.md#ethsummrr)

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

- :fontawesome-solid-user-group: **Participant:** [MERCKKGAA](./clinical/participants.md#merckkgaa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/MERCKKGAA-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/MERCKKGAA-CL.pdf)
- :material-file-search: **Runs:** [MrkUmlsXgb](./clinical/runs.md#mrkumlsxgb) | [MRKUmlsSolr](./clinical/runs.md#mrkumlssolr) | [MRKPrfNote](./clinical/runs.md#mrkprfnote) | [MRKSumCln](./clinical/runs.md#mrksumcln)

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

- :fontawesome-solid-user-group: **Participant:** [prna](./clinical/participants.md#prna)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/prna-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/prna-CL.pdf)
- :material-file-search: **Runs:** [prna2desc](./clinical/runs.md#prna2desc) | [prna3note](./clinical/runs.md#prna3note) | [prna4note](./clinical/runs.md#prna4note) | [prna5note](./clinical/runs.md#prna5note) | [prna1sum](./clinical/runs.md#prna1sum)

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

- :fontawesome-solid-user-group: **Participant:** [cbnu](./clinical/participants.md#cbnu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/cbnu-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/cbnu-CL.pdf)
- :material-file-search: **Runs:** [cbnus1](./clinical/runs.md#cbnus1) | [cbnus2](./clinical/runs.md#cbnus2) | [cbnun1](./clinical/runs.md#cbnun1)

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

- :fontawesome-solid-user-group: **Participant:** [CSIROmed](./clinical/participants.md#csiromed)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/CSIROmed-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/CSIROmed-CL.pdf)
- :material-file-search: **Runs:** [CSIROmnul](./clinical/runs.md#csiromnul) | [CSIROnote](./clinical/runs.md#csironote) | [CSIROdSum](./clinical/runs.md#csirodsum) | [CSIROsumm](./clinical/runs.md#csirosumm) | [CSIROmeta](./clinical/runs.md#csirometa)

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

- :fontawesome-solid-user-group: **Participant:** [SCIAICLTeam](./clinical/participants.md#sciaiclteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/SCIAICLTeam-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/SCIAICLTeam-CL.pdf)
- :material-file-search: **Runs:** [LucBase](./clinical/runs.md#lucbase) | [LucNote](./clinical/runs.md#lucnote) | [LucWghtFrame](./clinical/runs.md#lucwghtframe) | [LucNoteFrame](./clinical/runs.md#lucnoteframe) | [LucWeight](./clinical/runs.md#lucweight)

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

- :fontawesome-solid-user-group: **Participant:** [HAUT](./clinical/participants.md#haut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/HAUT-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/HAUT-CL.pdf)
- :material-file-search: **Runs:** [nacmmf](./clinical/runs.md#nacmmf) | [dacmmf](./clinical/runs.md#dacmmf) | [sacmmf](./clinical/runs.md#sacmmf)

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

- :fontawesome-solid-user-group: **Participant:** [ECNU](./clinical/participants.md#ecnu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/ECNU-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/ECNU-CL.pdf)
- :material-file-search: **Runs:** [ECNUmanual](./clinical/runs.md#ecnumanual) | [ECNUrun3](./clinical/runs.md#ecnurun3) | [ECNUrun1](./clinical/runs.md#ecnurun1) | [ECNUrun5](./clinical/runs.md#ecnurun5) | [ECNUrun4](./clinical/runs.md#ecnurun4)

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

- :fontawesome-solid-user-group: **Participant:** [DA_IICT](./clinical/participants.md#da_iict)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/DA_IICT-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/DA_IICT-CL.pdf)
- :material-file-search: **Runs:** [DAsummTM](./clinical/runs.md#dasummtm) | [DAdescTM](./clinical/runs.md#dadesctm) | [DAnoteTM](./clinical/runs.md#danotetm) | [DAnoteRoc](./clinical/runs.md#danoteroc) | [DAnote](./clinical/runs.md#danote)

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

- :fontawesome-solid-user-group: **Participant:** [UNTIIA](./clinical/participants.md#untiia)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/UNTIIA-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/UNTIIA-CL.pdf)
- :material-file-search: **Runs:** [UNTIIANA](./clinical/runs.md#untiiana) | [UNTIIANM](./clinical/runs.md#untiianm) | [UNTIIASA](./clinical/runs.md#untiiasa) | [UNTIIANMERG](./clinical/runs.md#untiianmerg) | [UNTIIASMERG](./clinical/runs.md#untiiasmerg)

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

- :fontawesome-solid-user-group: **Participant:** [WHUIRGroup](./clinical/participants.md#whuirgroup)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/WHUIRGroup-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/WHUIRGroup-CL.pdf)
- :material-file-search: **Runs:** [WHUIRGroup1](./clinical/runs.md#whuirgroup1) | [WHUIRGroup2](./clinical/runs.md#whuirgroup2) | [WHUIRGroup4](./clinical/runs.md#whuirgroup4) | [WHUIRGroup6](./clinical/runs.md#whuirgroup6) | [WHUIRGroup5](./clinical/runs.md#whuirgroup5)

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

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./clinical/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/udel_fang-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/udel_fang-CL.pdf)
- :material-file-search: **Runs:** [UDelInfoCDS1](./clinical/runs.md#udelinfocds1) | [UDelInfoCDS4](./clinical/runs.md#udelinfocds4) | [UDelInfoCDS5](./clinical/runs.md#udelinfocds5) | [UDelInfoCDS2](./clinical/runs.md#udelinfocds2) | [UDelInfoCDS3](./clinical/runs.md#udelinfocds3)

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

- :fontawesome-solid-user-group: **Participant:** [MayoNLPTeam](./clinical/participants.md#mayonlpteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/MayoNLPTeam-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/MayoNLPTeam-CL.pdf)
- :material-file-search: **Runs:** [mayoas](./clinical/runs.md#mayoas) | [mayoad](./clinical/runs.md#mayoad) | [mayoan](./clinical/runs.md#mayoan) | [mayomd](./clinical/runs.md#mayomd) | [mayomn](./clinical/runs.md#mayomn)

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

- :fontawesome-solid-user-group: **Participant:** [CCNU2016TREC](./clinical/participants.md#ccnu2016trec)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/CCNU2016TREC-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/CCNU2016TREC-CL.pdf)
- :material-file-search: **Runs:** [CCNUSUMR1](./clinical/runs.md#ccnusumr1) | [CCNUDESR2](./clinical/runs.md#ccnudesr2) | [CCNUNOTER1](./clinical/runs.md#ccnunoter1) | [CCNUNOTER2](./clinical/runs.md#ccnunoter2) | [CCNUNOTER3](./clinical/runs.md#ccnunoter3)

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

- :fontawesome-solid-user-group: **Participant:** [iris](./clinical/participants.md#iris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/iris-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/iris-CL.pdf)
- :material-file-search: **Runs:** [run1](./clinical/runs.md#run1) | [run2](./clinical/runs.md#run2) | [run3](./clinical/runs.md#run3) | [run4](./clinical/runs.md#run4) | [run5](./clinical/runs.md#run5)

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

- :fontawesome-solid-user-group: **Participant:** [NKU](./clinical/participants.md#nku)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/NKU-CL.pdf](http://trec.nist.gov/pubs/trec25/papers/NKU-CL.pdf)
- :material-file-search: **Runs:** [nkuRun5](./clinical/runs.md#nkurun5) | [nkuRun3](./clinical/runs.md#nkurun3) | [nkuRun2](./clinical/runs.md#nkurun2) | [nkuRun4](./clinical/runs.md#nkurun4) | [nkuRun1](./clinical/runs.md#nkurun1)

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

## LiveQA 

#### Overview of the TREC 2016 LiveQA Track

_Eugene Agichtein, David Carmel, Dan Pelleg, Yuval Pinter, Donna Harman_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec25/papers/Overview-QA.pdf](https://trec.nist.gov/pubs/trec25/papers/Overview-QA.pdf)
??? abstract "Abstract"
	
	The LiveQA track, now in its second year, is focused on real-time question answering for real-user questions. During the test period, real user questions are drawn from those newly submitted on a popular community question answering site, Yahoo Answers (YA), that have not yet been answered. These questions are sent to the participating systems, who provide an answer in real time. Returned answers are judged by the NIST assessors on a 4-level Likert scale. The most challenging aspects of this task are that the questions can be on any one of many popular topics, are informally stated, and are often complex and at least partly subjective. Furthermore, the participant systems must return an answer in under 60 seconds, which places additional, and realistic, constraints on the kind of processing that a system can do. In addition to the main real-time question answering task, this year we introduced a pilot task aimed at identifying the question intent. As human questions submitted on forums and CQA sites are verbose in nature and contain many redundant or unnecessary terms, participants were challenged to identify the signi cant parts of the question. The main theme of the question is marked by the systems by specifying a list of spans that capture its main intent. This automatic 'summary' of the question was evaluated by measuring its ROUGE-and METEOR-based similarity to a succinct rephrase of the question, manually provided by NIST assessors.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AgichteinCPPH16.bib) "
	```
	@inproceedings{DBLP:conf/trec/AgichteinCPPH16,
		author = {Eugene Agichtein and David Carmel and Dan Pelleg and Yuval Pinter and Donna Harman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2016 LiveQA Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {https://trec.nist.gov/pubs/trec25/papers/Overview-QA.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AgichteinCPPH16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ECNU at 2016 LiveQA Track: A Parameter Sharing Long Short Term  Memory Model for Learning Question Similarity

_Weijie An, Mengfei Shi, Xin Ouyang, Yan Yang, Qinmin Hu, Liang He_

- :fontawesome-solid-user-group: **Participant:** [ECNU](./qa/participants.md#ecnu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/ECNU-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/ECNU-QA.pdf)
- :material-file-search: **Runs:** [ECNU](./qa/runs.md#ecnu)

??? abstract "Abstract"
	
	In this paper, we present our system which is evaluated in the TREC 2016 LiveQA Challenge. Same as the last year, the TREC 2016 LiveQA track focuses on “live” question answering for the real-user questions from Yahoo! Answer. In this year, we first apply a parameter sharing Long Short Term Memory(LSTM) network to learn a high embedding of question representation. Then we combine the question representation with the key words information to strengthen the representation of semantic-similar questions, followed by calculating the question similarity with a simple metric function. Our approach outperforms the average score of all submitted runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnSOYHH16.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnSOYHH16,
		author = {Weijie An and Mengfei Shi and Xin Ouyang and Yan Yang and Qinmin Hu and Liang He},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ECNU} at 2016 LiveQA Track: {A} Parameter Sharing Long Short Term Memory Model for Learning Question Similarity},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/ECNU-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnSOYHH16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Texas Rio Grande Valley TREC LiveQA 2016: Using Topic  Modeling to Answer Complex Questions

_Josue Balandrano Coronel_

- :fontawesome-solid-user-group: **Participant:** [JBC-TREC2016](./qa/participants.md#jbc-trec2016)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/JBC-TREC2016-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/JBC-TREC2016-QA.pdf)
- :material-file-search: **Runs:** [UTRGV](./qa/runs.md#utrgv)

??? abstract "Abstract"
	
	This paper describes the system submitted to the TREC 2016 LiveQA track. This year, the TREC 2016 LiveQA track consists of implementing a web service to answer user-submitted questions. The newest unanswered question from Yahoo! Answers will be posted to the web service, a question every minute for 24 hours. The implementation described in this paper uses natural language processing (NLP) to extract keywords from the question given as input. A web search together with a Yahoo! Answer search is used to select candidate answers. A latent dirichlet allocation (LDA) model is trained in order to compute a topic distribution of the different candidate answers. Finally, the Jensen-Shannon distance is used as similarity measure between the candidate answers and the question given as input. This implementation performed better than the average scores.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Coronel16.bib) "
	```
	@inproceedings{DBLP:conf/trec/Coronel16,
		author = {Josue Balandrano Coronel},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Texas Rio Grande Valley {TREC} LiveQA 2016: Using Topic Modeling to Answer Complex Questions},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/JBC-TREC2016-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Coronel16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Open Domain Real-Time Question Answering Based on Semantic and Syntactic  Question Similarity

_Vivek V. Datla, Sadid A. Hasan, Joey Liu, Yassine Benajiba, Kathy Lee, Ashequl Qadir, Aaditya Prakash, Oladimeji Farri_

- :fontawesome-solid-user-group: **Participant:** [prna](./qa/participants.md#prna)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/prna-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/prna-QA.pdf)
- :material-file-search: **Runs:** [prna](./qa/runs.md#prna)

??? abstract "Abstract"
	
	In this paper, we describe our system and results of our participation in the Live-QA track of the Text Retrieval Conference(TREC) 2016. The Live-QA task involves real user questions, extracted from the stream of most recent questions submitted to the Yahoo Answers (YA) site, which have not yet been answered by humans. These questions are pushed to the participants via a socket connection, and the systems are needed to provide an answer which is less than 1000 characters length in less than 60 seconds. The answers given by the system are evaluated by human experts in terms of accuracy, readability, and preciseness. Our strategy for answering the questions include question decomposition, question relatedness identification, and answer generation. Evaluation results demonstrate that our system performed close to the average scores in question answering task. In the question focus generation task our system ranked fourth.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DatlaHLBLQPF16.bib) "
	```
	@inproceedings{DBLP:conf/trec/DatlaHLBLQPF16,
		author = {Vivek V. Datla and Sadid A. Hasan and Joey Liu and Yassine Benajiba and Kathy Lee and Ashequl Qadir and Aaditya Prakash and Oladimeji Farri},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Open Domain Real-Time Question Answering Based on Semantic and Syntactic Question Similarity},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/prna-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DatlaHLBLQPF16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2016: LiveQA Track

_Youjun E, Weitong Chen, Zhen Yang_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./qa/participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/BJUT-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/BJUT-QA.pdf)

??? abstract "Abstract"
	
	The paper presents the BJUT's liveQA system participating the TREC 2016. The Trec LiveQA track continues to use the last year's instruction, requiring that the system is able to answer the questions which had not been solved in one minutes based on Yahoo! Answers. Our work: (1) The key words are abstracted from the questions, so that more relevant questions will be returned. (2) The system searches in a larger scope on Yahoo! Answers to find the most accurate answers. (3) The answers should be detect whether they are more suitable for answering the given questions. The experiment results are presented at the end of the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ECY16.bib) "
	```
	@inproceedings{DBLP:conf/trec/ECY16,
		author = {Youjun E and Weitong Chen and Zhen Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2016: LiveQA Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/BJUT-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ECY16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT at the TREC 2016 LiveQA Track

_Joel M. Mackenzie, Ruey-Cheng Chen, J. Shane Culpepper_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./qa/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/RMIT-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/RMIT-QA.pdf)
- :material-file-search: **Runs:** [RMIT-11](./qa/runs.md#rmit-11) | [RMIT-12](./qa/runs.md#rmit-12) | [RMIT-1](./qa/runs.md#rmit-1) | [RMIT-2](./qa/runs.md#rmit-2)

??? abstract "Abstract"
	
	This paper describes the four systems RMIT fielded for the TREC 2016 LiveQA task and the associated experiments. Similar to last year, the results show that simple solutions tend to work best, and that our improved baseline systems achieved an above-average performance. We use a commercial search engine as a first stage retrieval mechanism and compare it with our internal system which uses a carefully curated document collection. Somewhat surprisingly, we found that on average the small curated collection performed better within our current framework, warranting further studies on when and when not to use an external resource, such as a publicly available search engine API. Finally, we show that small improvements to performance can substantially reduce failure rates.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MackenzieCC16.bib) "
	```
	@inproceedings{DBLP:conf/trec/MackenzieCC16,
		author = {Joel M. Mackenzie and Ruey{-}Cheng Chen and J. Shane Culpepper},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{RMIT} at the {TREC} 2016 LiveQA Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/RMIT-QA.pdf},
		timestamp = {Mon, 26 Apr 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MackenzieCC16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Real, Live, and Concise: Answering Open-Domain Questions with Word  Embedding and Summarization

_Rana Malhas, Marwan Torki, Rahma Ali, Tamer Elsayed, Evi Yulianti_

- :fontawesome-solid-user-group: **Participant:** [QU](./qa/participants.md#qu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/QU-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/QU-QA.pdf)
- :material-file-search: **Runs:** [QU](./qa/runs.md#qu) | [QU2](./qa/runs.md#qu2) | [QU3](./qa/runs.md#qu3)

??? abstract "Abstract"
	
	Resorting to community question answering (CQA) websites for finding answers has gained momentum in the recent years with the explosive rate at which social media has been proliferating. With many questions left unanswered on those websites, automatic question answering (QA) systems have seen light. A main objective of those systems is to harness the plethora of existing answered questions; hence transforming the problem to finding good answers to newly-posed questions from similar previously-answered ones or composing a new concise one from those potential answers. In this paper, we describe the real-time Question Answering system we have developed to participate in TREC 2016 LiveQA track. Our QA system is composed of three phases: answer retrieval from three different Web sources (Yahoo! Answers, Google Search, and Bing Search), answer ranking using learning to rank models, and summarization of top ranked answers. Official track results of our three submitted runs show that our runs significantly outperformed the average scores of all participated runs across the entire spectrum of official evaluation measures deployed by the track organizers this year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MalhasTAEY16.bib) "
	```
	@inproceedings{DBLP:conf/trec/MalhasTAEY16,
		author = {Rana Malhas and Marwan Torki and Rahma Ali and Tamer Elsayed and Evi Yulianti},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Real, Live, and Concise: Answering Open-Domain Questions with Word Embedding and Summarization},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/QU-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MalhasTAEY16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Emory University at TREC LiveQA 2016: Combining Crowdsourcing and  Learning-To-Rank Approaches for Real-Time Complex Question Answering

_Denis Savenkov, Eugene Agichtein_

- :fontawesome-solid-user-group: **Participant:** [EmoryIrLab](./qa/participants.md#emoryirlab)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/EmoryIrLab-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/EmoryIrLab-QA.pdf)
- :material-file-search: **Runs:** [EmoryCrowd](./qa/runs.md#emorycrowd) | [OutOfmEmory](./qa/runs.md#outofmemory)

??? abstract "Abstract"
	
	This paper describes the two QA systems we developed to participate in the TREC LiveQA 2016 shared task. The first run represents an improvement of our fully automatic real-time QA system from LiveQA 2015, Emory-QA. The second run, Emory-CRQA, which stands for Crowd-powered Real-time Question Answering, incorporates human feedback, in real-time, to improve answer candidate generation and ranking. The base Emory-QA system uses the title and the body of a question to query Yahoo! Answers, Answers.com, WikiHow and general web search and retrieve a set of candidate answers along with their topics and contexts. This information is used to represent each candidate by a set of features, rank them with a trained LambdaMART model, and return the top ranked candidates as an answer to the question. The second run, Emory-CRQA, integrates a crowdsourcing module, which provides the system with additional answer candidates and quality ratings, obtained in near real-time (under one minute) from a crowd of workers When Emory-CRQA receives a question, it is forwarded to the crowd, who can start working on the answer in parallel with the automatic pipeline. When the automatic pipeline is done generating and ranking candidates, a subset of them is immediately sent to the same workers who have been working on answering the questions. Workers then rate the quality of all human- or system-generated candidate answers. The resulting ratings, as well as original system scores, are used as features for the final re-ranking module, which returns the highest scoring answer. The official run results of the tasks indicate promising improvements for both runs compared to the best performing system from LiveQA 2015. Additionally, they demonstrate the effectiveness of the introduced crowdsourcing module, which allowed us to achieve an improvement of ∼20% in average answer score over a fully automatic Emory-QA system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SavenkovA16.bib) "
	```
	@inproceedings{DBLP:conf/trec/SavenkovA16,
		author = {Denis Savenkov and Eugene Agichtein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Emory University at {TREC} LiveQA 2016: Combining Crowdsourcing and Learning-To-Rank Approaches for Real-Time Complex Question Answering},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/EmoryIrLab-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SavenkovA16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CMU OAQA at TREC 2016 LiveQA: An Attentional Neural Encoder-Decoder  Approach for Answer Ranking

_Di Wang, Eric Nyberg_

- :fontawesome-solid-user-group: **Participant:** [CMU-OAQA](./qa/participants.md#cmu-oaqa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/CMU-OAQA-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/CMU-OAQA-QA.pdf)
- :material-file-search: **Runs:** [CMU](./qa/runs.md#cmu)

??? abstract "Abstract"
	
	In this paper, we present CMU's question answering system that was evaluated in the TREC 2016 LiveQA Challenge. Our overall approach this year is similar to the one used in 2015. This system answers real-user submitted questions from Yahoo! Answers website, which involves retrieving relevant web pages, extracting answer candidate texts, ranking and selecting answer candidates. The main improvement this year is the introduction of a novel answer passage ranking method based on attentional encoder-decoder recurrent neural networks (RNN). Our method uses one RNN to encode candidate answer passage into vectors, and then another RNN to decode the input question from the vectors. The perplexity of decoding the question is then used as the ranking score. In the TREC 2016 LiveQA evaluations, human assessors gave our system an average score of 1.1547 on a three-point scale and the average score was .5766 for all the 26 systems evaluated.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangN16.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangN16,
		author = {Di Wang and Eric Nyberg},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CMU} {OAQA} at {TREC} 2016 LiveQA: An Attentional Neural Encoder-Decoder Approach for Answer Ranking},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/CMU-OAQA-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangN16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### San Francisco State University at LiveQA Track of TREC 2016

_Maria Khvalchik, Anagha Kulkarni_

- :fontawesome-solid-user-group: **Participant:** [IR.SFSU.2016](./qa/participants.md#ir.sfsu.2016)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/IR.SFSU.2016-QA.pdf](http://trec.nist.gov/pubs/trec25/papers/IR.SFSU.2016-QA.pdf)
- :material-file-search: **Runs:** [IRSFSU](./qa/runs.md#irsfsu)

??? abstract "Abstract"
	
	There are many situations in our everyday life where we look for answers to some questions - “Who wrote this book?”, “How to grill a fish?” or “Where is the Opera House located?”. Twenty years ago to answer these questions people were looking them up in the encyclopedias, recipe books or were asking other people. Moving the information into the electronic form and making it universally accessible helped to automate this process and save an enormous amount of time. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KhvalchikK16.bib) "
	```
	@inproceedings{DBLP:conf/trec/KhvalchikK16,
		author = {Maria Khvalchik and Anagha Kulkarni},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {San Francisco State University at LiveQA Track of {TREC} 2016},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/IR.SFSU.2016-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KhvalchikK16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Contextual Suggestion 

#### Overview of the TREC 2016 Contextual Suggestion Track

_Seyyed Hadi Hashemi, Jaap Kamps, Julia Kiseleva, Charles L. A. Clarke, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec25/papers/Overview-CS.pdf](https://trec.nist.gov/pubs/trec25/papers/Overview-CS.pdf)
??? abstract "Abstract"
	
	The TREC Contextual Suggestion Track offers a personalized point of interest (POI) recommendation task, in which participants develop systems to give a ranked list of suggestions related to a profile and a context pair available in the tasks' requests provided by the track organizers. Previously, reusability of the contextual suggestion track suffered from using dynamic collections and a shallow pool depth. The main innovations at TREC 2016 are the following. First, the TREC CS web corpus, consisting of a web crawl of the TREC contextual suggestion collection, was made available. The rich textual descriptions of the web pages makes far more information available for each candidate POI in the collection. Second, we released endorsements (end user tags) of the attractions as given by NIST assessors, potentially matching the endorsements of POIs in another city as given by the person issuing the request as part of her profile. Third, a multi-depth pooling approach extending beyond the shallow top 5 pool was used. The multi-depth pooling approach has created a test collection that provides more reliable evaluation results in ranks deeper than the traditional pool cut-off.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HashemiKKCV16.bib) "
	```
	@inproceedings{DBLP:conf/trec/HashemiKKCV16,
		author = {Seyyed Hadi Hashemi and Jaap Kamps and Julia Kiseleva and Charles L. A. Clarke and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2016 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {https://trec.nist.gov/pubs/trec25/papers/Overview-CS.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HashemiKKCV16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Venue Appropriateness Prediction for Contextual Suggestion

_Mohammad Aliannejadi, Ida Mele, Fabio Crestani_

- :fontawesome-solid-user-group: **Participant:** [USI](./context/participants.md#usi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/USI-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/USI-CX.pdf)
- :material-file-search: **Runs:** [USI1](./context/runs.md#usi1) | [USI2](./context/runs.md#usi2) | [USI3](./context/runs.md#usi3) | [USI4](./context/runs.md#usi4) | [USI5](./context/runs.md#usi5)

??? abstract "Abstract"
	
	This technical report presents the work of Universit `a della Svizzera italiana (USI) at TREC 2016 Contextual Suggestion track. The goal of the Contextual Suggestion track is to develop systems that could make suggestions for venues that a user will potentially like. Our proposed method aempts to model the users' behavior and opinion by training a SVM classifier for each user. It then enriches the basic model using additional data sources such as venue categories and taste keywords to model users' interest. For predicting the contextual appropriateness of a venue to a user's context, we modeled the problem as a binary classification one. Furthermore, we built two datasets using crowdsourcing that are used to train a SVM classifier to predict the contextual appropriateness of venues. Finally, we show how to incorporate the multimodal scores in our model to produce the final ranking. The experimental results illustrate that our proposed method performed very well in terms of all the evaluation metrics used in TREC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AliannejadiMC16.bib) "
	```
	@inproceedings{DBLP:conf/trec/AliannejadiMC16,
		author = {Mohammad Aliannejadi and Ida Mele and Fabio Crestani},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Venue Appropriateness Prediction for Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/USI-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AliannejadiMC16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ADAPT_TCD: An Ontology-Based Context Aware Approach for Contextual  Suggestion

_Mostafa Bayomi, Séamus Lawless_

- :fontawesome-solid-user-group: **Participant:** [ADAPT_TCD](./context/participants.md#adapt_tcd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/ADAPT_TCD-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/ADAPT_TCD-CX.pdf)
- :material-file-search: **Runs:** [ADAPT_TCD_r1](./context/runs.md#adapt_tcd_r1) | [ADAPT_TCD_r2](./context/runs.md#adapt_tcd_r2) | [ADAPT_TCD_br1](./context/runs.md#adapt_tcd_br1) | [ADAPT_TCD_br2](./context/runs.md#adapt_tcd_br2) | [ADAPT_TCD_br3](./context/runs.md#adapt_tcd_br3)

??? abstract "Abstract"
	
	In this paper we give an overview of the participation of the ADAPT Centre, Trinity College Dublin, Ireland, in both phases of the TREC 2016 Contextual Suggestion Track. We present our ontology-based approach that consists of three models that are based on an ontology that was extracted from the Foursquare category hierarchy. The three models are: User Model, Document Model and Rule Model. In the User Model we build two models, one for each phase of the task, based upon the attractions that were rated in the user's profile. The Document Model enriches documents with extra metadata from Foursquare and categories (concepts) from the ontology are attached to each document. The Rule model is used to tune the score for candidate suggestions based on how the context of the trip aligns with the rules in the model. The results of our submitted runs, in both phases, demonstrate the effectiveness of the proposed methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BayomiL16.bib) "
	```
	@inproceedings{DBLP:conf/trec/BayomiL16,
		author = {Mostafa Bayomi and S{\'{e}}amus Lawless},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {ADAPT{\_}TCD: An Ontology-Based Context Aware Approach for Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/ADAPT\_TCD-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BayomiL16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Significant Words Language Models for Contextual Suggestion

_Mostafa Dehghani, Jaap Kamps, Hosein Azarbonyad, Maarten Marx_

- :fontawesome-solid-user-group: **Participant:** [ExPoSe](./context/participants.md#expose)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/ExPoSe-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/ExPoSe-CX.pdf)
- :material-file-search: **Runs:** [response_tags](./context/runs.md#response_tags) | [run_content](./context/runs.md#run_content) | [run_all](./context/runs.md#run_all) | [SWLM](./context/runs.md#swlm)

??? abstract "Abstract"
	
	In this paper, we present the participation of the University of Amsterdam's ExPoSe team in the TREC 2016 Contextual Suggestion Track. The main goal of contextual suggestion track is to evaluate methods for providing suggestions for activities or points of interest to users in a specific location, at a specific time, taking their personal preferences into consideration. One of the key steps of contextual suggestion methods is estimating a proper model for representing different objects in the data like users and attractions. Here, we describe our approach which is employing Significant Words Language Models (SWLM) [2] as an effective method for estimating models representing significant features of sets of attractions as user profiles and sets of users as group profile. We observe that using SWLM, we are able to better estimate a model representing the set of preferences positively rated by users as their profile, compared to the case we use standard language model as the profiling approach. We also find that using negatively rated attractions as negative samples along with positively rated attractions as positive samples, we may loose the performance when we use standard language model as the profiling approach. While, using SWLM, taking negatively rated attractions into consideration may help to improve the quality of suggestions. In addition, we investigate groups of users sharing a property (e.g. of a similar age) and study the effect of taking group-based profiles on the performance of suggestions provided for individual users. We noticed that group-based suggestion helps more when users have a tendency to rate attraction in a neutral way, compared to the case users are more subjective in their rating behavior.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DehghaniKAM16.bib) "
	```
	@inproceedings{DBLP:conf/trec/DehghaniKAM16,
		author = {Mostafa Dehghani and Jaap Kamps and Hosein Azarbonyad and Maarten Marx},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Significant Words Language Models for Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/ExPoSe-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DehghaniKAM16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Neural Endorsement Based Contextual Suggestion

_Seyyed Hadi Hashemi, Jaap Kamps, Nawal Ould Amer_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./context/participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/Uamsterdam-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/Uamsterdam-CX.pdf)
- :material-file-search: **Runs:** [UAmsterdam1](./context/runs.md#uamsterdam1) | [UAmsterdam2](./context/runs.md#uamsterdam2) | [UAmsterdamCB](./context/runs.md#uamsterdamcb) | [UAmsterdamDL](./context/runs.md#uamsterdamdl)

??? abstract "Abstract"
	
	This paper presents the University of Amsterdam's participation in the TREC 2016 Contextual Suggestion Track. In this research, we have studied a personallized neural document language modeling and a neural category preference modeling for contextual suggestion using available endorsements in TREC 2016 contextual suggestion track phase 2 requests. Specifically, our main aim is to answer the questions: How to model users' profiles by using the suggestions' endorsements as an additional data? How effective is using word embeddings to boost terms' weights relevant to the given endorsements? How to model users' attraction-category preferences? How effective is using deep neural networks to learn users' category preferences in contextual suggestion task? Our main findings are the following: First, the neural personalized document based user profiling using word embeddings improves the baseline content-based filtering approach based on all the common IR measures including TREC 2016 Contextual Suggestion official metric (NDCG@5). Second, neural users' category preference modeling beats both baseline content-based filtering and the user profiling model using word-embeddings in terms of all the common IR measures.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HashemiKA16.bib) "
	```
	@inproceedings{DBLP:conf/trec/HashemiKA16,
		author = {Seyyed Hadi Hashemi and Jaap Kamps and Nawal Ould Amer},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Neural Endorsement Based Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/Uamsterdam-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HashemiKA16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Recommending Points-of-Interest via Weighted kNN, Rated Rocchio, and  Borda Count Fusion

_Georgios Kalamatianos, Avi Arampatzis_

- :fontawesome-solid-user-group: **Participant:** [DUTH](./context/participants.md#duth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/DUTH-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/DUTH-CX.pdf)
- :material-file-search: **Runs:** [DUTH_rocchio](./context/runs.md#duth_rocchio) | [DUTH_knn](./context/runs.md#duth_knn) | [DUTH_bcf](./context/runs.md#duth_bcf)

??? abstract "Abstract"
	
	We present the work of the Democritus University of Thrace (DUTH) team in TREC's 2016 Contextual Suggestion Track. The goal of the Contextual Suggestion Track is to build a system capable of proposing venues which a user might be interested to visit, using any available contextual and personal information. First, we enrich the TREC-provided dataset by collecting more information on venues from web-services like Foursquare and Yelp. Then, we address the task with two different content-based methods, namely, a Weighted kNN classifier and a Rated Rocchio personalized query. Last, we also explore the use of a voting system, namely Borda Count, as a means of fusing the results of several suggestion systems. Our runs provided very good results, achieving top or near-top TREC performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KalamatianosA16.bib) "
	```
	@inproceedings{DBLP:conf/trec/KalamatianosA16,
		author = {Georgios Kalamatianos and Avi Arampatzis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Recommending Points-of-Interest via Weighted kNN, Rated Rocchio, and Borda Count Fusion},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/DUTH-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KalamatianosA16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Employing open-web for Contextual Suggestion using tag-tag similarity

_Sainyam Kapoor, Manajit Chakraborty, C. Ravindranath Chowdary_

- :fontawesome-solid-user-group: **Participant:** [DPLAB_IITBHU](./context/participants.md#dplab_iitbhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/DPLAB_IITBHU-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/DPLAB_IITBHU-CX.pdf)
- :material-file-search: **Runs:** [iitbhu01](./context/runs.md#iitbhu01) | [iitbhu04](./context/runs.md#iitbhu04) | [iitbhu05](./context/runs.md#iitbhu05)

??? abstract "Abstract"
	
	The TREC 2016 Contextual Suggestion task aims at providing recommendations on points of attraction for different kind of users and a varying context. Our group DPLAB IITBHU tries to recommend relevant point-of-interests to a user based on the information provided on the candidate attractions and her past preferences. We employ open-web information in a novel way to capture the best possible setting for a user's tastes and distastes in terms of tag scores. The scores are then ranked using a heuristic to suggest the most pertinent attraction to the user. One of our methods exceed the TREC-CS 2016 median of the standard evaluation scores of all participant runs, which reflects the effectiveness of our approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KapoorCC16.bib) "
	```
	@inproceedings{DBLP:conf/trec/KapoorCC16,
		author = {Sainyam Kapoor and Manajit Chakraborty and C. Ravindranath Chowdary},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Employing open-web for Contextual Suggestion using tag-tag similarity},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/DPLAB\_IITBHU-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KapoorCC16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Context Based Recommender System through Collaborative Filtering  and Word Embedding Techniques

_Mahsa Khorasani, Hamid Sadjadi, Faezeh Ramazani, Faezeh Ensan_

- :fontawesome-solid-user-group: **Participant:** [FUM-IRLAB](./context/participants.md#fum-irlab)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/FUM-IRLAB-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/FUM-IRLAB-CX.pdf)
- :material-file-search: **Runs:** [1](./context/runs.md#1) | [2](./context/runs.md#2) | [3](./context/runs.md#3) | [phase2_1](./context/runs.md#phase2_1) | [phase2_2](./context/runs.md#phase2_2)

??? abstract "Abstract"
	
	This report presents a description of the context-based recommender system that was developed by the FUM-IR team from the Ferdowsi University of Mashhad for the Contextual Suggestion track of TREC 2016. This will also include the description of the different runs were submitted to this track. In developing our system, we followed two main approaches for finding suitable attractions for a given user: a content-based approach and a category-based approach. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KhorasaniSRE16.bib) "
	```
	@inproceedings{DBLP:conf/trec/KhorasaniSRE16,
		author = {Mahsa Khorasani and Hamid Sadjadi and Faezeh Ramazani and Faezeh Ensan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {A Context Based Recommender System through Collaborative Filtering and Word Embedding Techniques},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/FUM-IRLAB-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KhorasaniSRE16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow Terrier Team at TREC 2016: Experiments in  Contextual Suggestions

_Jarana Manotumruksa, Craig MacDonald, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./context/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/uogTr-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/uogTr-CX.pdf)
- :material-file-search: **Runs:** [uogTrCs](./context/runs.md#uogtrcs) | [uogTrCsContext](./context/runs.md#uogtrcscontext)

??? abstract "Abstract"
	
	For TREC 2016, we focus on tackling the challenges posed by the Contextual Suggestion by investigating the use of user-generated data (e.g. textual content of comments and venue's information) in location-based social networks (LBSNs) to suggest a ranked list of venues to users. In particular, we exploit a word embedding technique to extract user-venue and context-venue preference features to train learning-to-rank models. In addition, we leverage each venue's information (e.g. number of check-in) to extract venue-dependent features. We train learning-to-rank models using these features on the TREC 2015 Contextual Suggestion dataset. We submit two runs (uogTrCs and uogTrCsContext) where uogTrCsContexl is a context-aware approach. The batch experimental results show that uogTrCS is competitive, performing above the TREC median in terms of NDCG@5 and P@5 and outperforms uogTrCsContext.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ManotumruksaMO16.bib) "
	```
	@inproceedings{DBLP:conf/trec/ManotumruksaMO16,
		author = {Jarana Manotumruksa and Craig MacDonald and Iadh Ounis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow Terrier Team at {TREC} 2016: Experiments in Contextual Suggestions},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/uogTr-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ManotumruksaMO16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Word embeddings and Global Preference for Contextual Suggestion

_Jian Mo, Luc Lamontagne, Richard Khoury_

- :fontawesome-solid-user-group: **Participant:** [LavalLakehead](./context/participants.md#lavallakehead)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/LavalLakehead-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/LavalLakehead-CX.pdf)
- :material-file-search: **Runs:** [Laval_run1](./context/runs.md#laval_run1) | [Laval_batch_1](./context/runs.md#laval_batch_1) | [Laval_batch_2](./context/runs.md#laval_batch_2) | [Laval_batch_3](./context/runs.md#laval_batch_3)

??? abstract "Abstract"
	
	In this paper we describe our effort on 2016 Contextual Suggestion Track. We present a new ranking model that captures both global trend of interests as well as contextual individual preference. We trained a regressor on common users data thus it can prioritize popular places and categories. In order to model individual user preference, we introduce word embeddings to represent both user profiles and candidate places as vectors in a same Euclidean space.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoLK16.bib) "
	```
	@inproceedings{DBLP:conf/trec/MoLK16,
		author = {Jian Mo and Luc Lamontagne and Richard Khoury},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Word embeddings and Global Preference for Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/LavalLakehead-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MoLK16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Beijing University of Posts and Telecommunications(BUPT) at TREC  2016: A Rating Model Based on Tags for ABSTRACT Contextual Suggestion

_Danping Yin, Siyuan Gao, Zonghui Peng, Yameng Li, Ruifang Liu_

- :fontawesome-solid-user-group: **Participant:** [bupt_pris_2016](./context/participants.md#bupt_pris_2016)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/bupt_pris_2016-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/bupt_pris_2016-CX.pdf)
- :material-file-search: **Runs:** [bupt_runA](./context/runs.md#bupt_runa) | [cs.2_.4_max](./context/runs.md#cs.2_.4_max) | [cs.4_.2_max](./context/runs.md#cs.4_.2_max) | [cs.3_.3_avg](./context/runs.md#cs.3_.3_avg)

??? abstract "Abstract"
	
	In this paper we focus on the effort of Beijing University of Posts and Telecommunications (BUPT) on the TREC 2016's Contextual Suggestion Track. The problem we are supposed to tackle is how to make suggestions for a particular person with the provided context as well as its preferences. Basically we regard tags as the most important factor, and get ratings for different attractions with the ratings of tags. Also we use Collaborative Filtering to fill the missing ratings. A ranked list is generated after calculating users' ratings for candidate attractions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YinGPLL16.bib) "
	```
	@inproceedings{DBLP:conf/trec/YinGPLL16,
		author = {Danping Yin and Siyuan Gao and Zonghui Peng and Yameng Li and Ruifang Liu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Beijing University of Posts and Telecommunications(BUPT) at {TREC} 2016: {A} Rating Model Based on Tags for {ABSTRACT} Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/bupt\_pris\_2016-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YinGPLL16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Real-time Summarization 

#### Overview of the TREC 2016 Real-Time Summarization Track

_Jimmy Lin, Adam Roegiest, Luchen Tan, Richard McCreadie, Ellen M. Voorhees, Fernando Diaz_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec25/papers/Overview-RT.pdf](https://trec.nist.gov/pubs/trec25/papers/Overview-RT.pdf)
??? abstract "Abstract"
	
	The TREC 2016 Real-Time Summarization (RTS) Track aims to explore techniques and systems that automatically monitor streams of social media posts such as Twitter to keep users up to date on topics of interest. We might think of these topics as “interest profiles”, specifying the user's prospective information needs. In real-time summarization, the goal is for a system to “push” (i.e., recommend or suggest) interesting and novel content to users in a timely fashion. For example, the user might be interested in poll results for the 2016 U.S. presidential elections and wishes to be notified whenever new results are published. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinRTMV016.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinRTMV016,
		author = {Jimmy Lin and Adam Roegiest and Luchen Tan and Richard McCreadie and Ellen M. Voorhees and Fernando Diaz},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2016 Real-Time Summarization Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {https://trec.nist.gov/pubs/trec25/papers/Overview-RT.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinRTMV016.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CCNU at TREC 2016 Real-Time Summarization Track

_Chao Bei, Po Hu_

- :fontawesome-solid-user-group: **Participant:** [CCNU2016NLP](./realtime/participants.md#ccnu2016nlp)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/CCNU2016NLP-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/CCNU2016NLP-RT.pdf)
- :material-file-search: **Runs:** [CCNUNLPrun1](./realtime/runs.md#ccnunlprun1) | [CCNUNLPrun2](./realtime/runs.md#ccnunlprun2) | [CCNUNLPrun1-06](./realtime/runs.md#ccnunlprun1-06) | [CCNUNLPrun2-07](./realtime/runs.md#ccnunlprun2-07)

??? abstract "Abstract"
	
	This paper describes our approach to real-time summarization track for push notification scenario and email digest scenario in TREC 2016. This track aims at monitoring a stream of twitter posts and pushing the most relevant tweets to the users according to their interest profiles. In the push notification scenario, we adopt a combined method by take into account several critical factors i.e., relevance, salience and redundancy to select some relevant but non-redundant tweets. In the email digest scenario, in addition to considering these factors, we additionally adopted a novel TF-IDF strategy to automatically rank tweets at the end of a day. The experimental results on both scenarios show the effectiveness of our approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BeiH16.bib) "
	```
	@inproceedings{DBLP:conf/trec/BeiH16,
		author = {Chao Bei and Po Hu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CCNU} at {TREC} 2016 Real-Time Summarization Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/CCNU2016NLP-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BeiH16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Assorted Textual Features and Dynamic Push Strategies for Real-time  Tweet Notification

_Kathy Lee, Ashequl Qadir, Vivek V. Datla, Sadid A. Hasan, Joey Liu, Aaditya Prakash, Oladimeji Farri_

- :fontawesome-solid-user-group: **Participant:** [prna](./realtime/participants.md#prna)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/prna-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/prna-RT.pdf)
- :material-file-search: **Runs:** [PRNABaseline-34](./realtime/runs.md#prnabaseline-34) | [PRNATaskA2-35](./realtime/runs.md#prnataska2-35) | [PRNATaskA3-36](./realtime/runs.md#prnataska3-36) | [PRNATaskB1](./realtime/runs.md#prnataskb1) | [PRNATaskB2](./realtime/runs.md#prnataskb2) | [PRNATaskB3](./realtime/runs.md#prnataskb3)

??? abstract "Abstract"
	
	In this paper, we describe our systems and corresponding results submitted to the Real-Time Summarization (RTS) track at the 2016 Text Retrieval Conference (TREC). The task involved identifying relevant tweets based on a user's interest profile. In Scenario A of the task, tweets relevant to an interest profile were pushed to a live user in real-time. In Scenario B, a daily digest of relevant tweets was sent to a user. We submitted three automatic runs for each scenario. Our overall method for identifying relevant tweets was based on 1) automatically identifying key textual features from a set of interest profiles provided by the Track organizers, 2) expanding the textual phrases with their paraphrases, and 3) exploiting the features for message filtering and relevance measurement after novelty recognition. We experimented with different push strategies to decide when to deliver a message to a user. The evaluation results (by mobile and NIST assessors) show that our system ranked 3rd for Scenario A and 6th for Scenario B.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeQDHLPF16.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeQDHLPF16,
		author = {Kathy Lee and Ashequl Qadir and Vivek V. Datla and Sadid A. Hasan and Joey Liu and Aaditya Prakash and Oladimeji Farri},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Assorted Textual Features and Dynamic Push Strategies for Real-time Tweet Notification},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/prna-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeQDHLPF16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HLJIT at TREC 2016: The Approaches Based on Document Language  Model for Real-Time Summarization Track

_Song Li, Zhenyuan Hao, Zhongyuan Han, Leilei Kong, Haoliang Qi_

- :fontawesome-solid-user-group: **Participant:** [HLJIT](./realtime/participants.md#hljit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/HLJIT-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/HLJIT-RT.pdf)
- :material-file-search: **Runs:** [HLJIT_LM-19](./realtime/runs.md#hljit_lm-19) | [MyBaseline-17](./realtime/runs.md#mybaseline-17) | [MyBaseline-18](./realtime/runs.md#mybaseline-18) | [HLJIT_LM_URL](./realtime/runs.md#hljit_lm_url) | [HLJIT_LM_TIME](./realtime/runs.md#hljit_lm_time) | [HLJIT_LM](./realtime/runs.md#hljit_lm)

??? abstract "Abstract"
	
	The paper describes the technology of HLJIT for TREC 2016 Real-Time Summarization Track for microblog. Three summarization approaches under the language model framework, the traditional language model, the temporal document language model and the hyperlink-extended language model, are proposed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiHHKQLK16.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiHHKQLK16,
		author = {Song Li and Zhenyuan Hao and Zhongyuan Han and Leilei Kong and Haoliang Qi},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{HLJIT} at {TREC} 2016: The Approaches Based on Document Language Model for Real-Time Summarization Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/HLJIT-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiHHKQLK16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Performance Prediction and Topic Shift in Microblog Retrieval

_Kuang Lu, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./realtime/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/udel_fang-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/udel_fang-RT.pdf)
- :material-file-search: **Runs:** [UDInfoDFP-47](./realtime/runs.md#udinfodfp-47) | [UDInfoSFP-46](./realtime/runs.md#udinfosfp-46) | [UDInfoSPP-48](./realtime/runs.md#udinfospp-48) | [UDInfo_TN](./realtime/runs.md#udinfo_tn) | [UDInfo_TlmN](./realtime/runs.md#udinfo_tlmn) | [UDInfo_TlmNlm](./realtime/runs.md#udinfo_tlmnlm)

??? abstract "Abstract"
	
	In Microblog retrieval, a system's ability to know when to ”shut up” and how many results to return for a given query can have huge impact on its performance [1]. In addition, since relevant but redundant tweets will be deemed as irrelevant, it is also important to detect whether a tweet contain novel information or not. Therefore, in this year's Real-Time Summarization Track, we focus on estimating result cut-off thresholds and redundancy thresholds. Query performance prediction techniques [2, 3] can be used to predict the performance of a query and therefore would be helpful in deciding both thresholds. Moreover, we define topic shift of a query as the change of subtopics or aspects discussed or mentioned on Twitter over time. We suggests that using it could help us further refine the thresholds since it reflects how much new information emerges on Twitter.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuF16.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuF16,
		author = {Kuang Lu and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Query Performance Prediction and Topic Shift in Microblog Retrieval},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/udel\_fang-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuF16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DAIICT at TREC RTS 2016: Live Push Notification and Email Digest

_Sandip Modha, Krati Agrawal, Deepali Verma, Prasenjit Majumder, Chintak Mandalia_

- :fontawesome-solid-user-group: **Participant:** [IRLAB_DA-IICT](./realtime/participants.md#irlab_da-iict)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/IRLAB_DA-IICT-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/IRLAB_DA-IICT-RT.pdf)
- :material-file-search: **Runs:** [runA_daiict_irlab-23](./realtime/runs.md#runa_daiict_irlab-23) | [IRLAB2](./realtime/runs.md#irlab2) | [IRLAB](./realtime/runs.md#irlab)

??? abstract "Abstract"
	
	This paper describes the participation of Information Retrieval Lab(IRLAB) at DA-IICT Gandhinagar,India in Real-Time Summarization track TREC 2016. This year TREC RTS offered two tasks. In the first task, that is scenario A, our system will be monitoring continuous posts from Twitter public stream and push the relevant tweet for each interest profile to RTS evaluation broker. For the same, we have expanded interest profile using Word2vec training model with past 30 days tweets. We have calculated relevance score between tweets and expanded interest profile using Okapi BM25 model. For Scenario B, Email digest, we anticipated summarization problem as a clustering problem. In scenario A, we reported result in terms of Expected Gain EG-1(primary metric)=0.1708 and in scenario B we have achieved primary metric nDCG-1 = 0.1972.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ModhaAVMM16.bib) "
	```
	@inproceedings{DBLP:conf/trec/ModhaAVMM16,
		author = {Sandip Modha and Krati Agrawal and Deepali Verma and Prasenjit Majumder and Chintak Mandalia},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{DAIICT} at {TREC} {RTS} 2016: Live Push Notification and Email Digest},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/IRLAB\_DA-IICT-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ModhaAVMM16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Light-weight, Conservative, yet Effective: Scalable Real-time Tweet  Summarization

_Reem Suwaileh, Maram Hasanain, Tamer Elsayed_

- :fontawesome-solid-user-group: **Participant:** [QU](./realtime/participants.md#qu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/QU-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/QU-RT.pdf)
- :material-file-search: **Runs:** [QUDR8](./realtime/runs.md#qudr8) | [QUJM16](./realtime/runs.md#qujm16) | [QUJMDR24](./realtime/runs.md#qujmdr24) | [QUBaseline-37](./realtime/runs.md#qubaseline-37) | [QUExpP-38](./realtime/runs.md#quexpp-38) | [QUExpT-39](./realtime/runs.md#quexpt-39)

??? abstract "Abstract"
	
	Microblogging platforms and Twitter specifically have become a major resource for exploring diverse topics of interest that vary from the world's breaking news to other topics such as sports, science, religion and even personal daily updates. Nevertheless, one by herself cannot easily follow her topics of interest while tackling the challenges that stem from the Twitter timeline nature. Among those challenges is the huge amount of posted tweets that are either not interesting, noisy, or redundant. Additionally, one cannot survive with manual techniques to summarize tweets related to topics that are discussed on the stream and are developed rapidly. In this paper, we tackle the problem of summarizing a stream of tweets given a pre-defined set of topics in the context of Qatar University's participation in TREC-2016 Real-Time Summarization (RTS) track. We participated in both push notification and e-mail digest scenarios. Given a set of users' interest profiles, our RTS system for push notifications scenario adopts a light-weight and conservative filtering strategy that monitors the continuous stream of tweets over a pipeline of multiple stages, while maintaining a scalable processing of a large number of interest profiles. For the e-mail digest scenario, we adopted a similar but even simpler approach. At the end of each day, a list of potentially relevant tweets is retrieved using a query of topic title terms that is issued against an index of all streamed tweets of that day. Our push-notification runs exhibited the best performance among all submitted automatic runs in the push notification task this year. Moreover, our best-performing email-digest run was the second-best among all submitted automatic runs in the email-digest task this year. However, the evaluation results show that the performance is still away from being adopted in practice.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SuwailehHE16.bib) "
	```
	@inproceedings{DBLP:conf/trec/SuwailehHE16,
		author = {Reem Suwaileh and Maram Hasanain and Tamer Elsayed},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Light-weight, Conservative, yet Effective: Scalable Real-time Tweet Summarization},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/QU-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SuwailehHE16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PolyU at TREC 2016 Real-Time Summarization

_Haihui Tan, Dajun Luo, Wenjie Li_

- :fontawesome-solid-user-group: **Participant:** [COMP2016](./realtime/participants.md#comp2016)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/COMP2016-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/COMP2016-RT.pdf)
- :material-file-search: **Runs:** [PolyURunB1](./realtime/runs.md#polyurunb1) | [PolyURunB2](./realtime/runs.md#polyurunb2) | [PolyURunB3](./realtime/runs.md#polyurunb3) | [run1-11](./realtime/runs.md#run1-11) | [run2-12](./realtime/runs.md#run2-12) | [run3-13](./realtime/runs.md#run3-13)

??? abstract "Abstract"
	
	This paper presents the participation of The Hong Kong Polytechnic University (PolyU) to the TREC 2016 Real-Time Summarization track. The two tasks related to Scenario A and Scenario B both focuses on information real-time processing. During the evaluation period, the system monitors the Twitter sample stream with respect to a number of “interest profiles”. We submitted three runs for both scenarios. We describe the system overview and the implementation details in this paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TanLL16.bib) "
	```
	@inproceedings{DBLP:conf/trec/TanLL16,
		author = {Haihui Tan and Dajun Luo and Wenjie Li},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {PolyU at {TREC} 2016 Real-Time Summarization},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/COMP2016-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TanLL16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2016: Real-Time Summarization Track

_Kai Wang, Zhen Yang_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./realtime/participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/BJUT-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/BJUT-RT.pdf)
- :material-file-search: **Runs:** [BJUTmydt-04](./realtime/runs.md#bjutmydt-04) | [BJUTmydt-05](./realtime/runs.md#bjutmydt-05) | [BJUTmyrf-03](./realtime/runs.md#bjutmyrf-03) | [bjutrf](./realtime/runs.md#bjutrf) | [bjutdt](./realtime/runs.md#bjutdt) | [bjutgbdt](./realtime/runs.md#bjutgbdt)

??? abstract "Abstract"
	
	This paper describes our approaches to Real-Time Summarization Track in the TREC 2016, including pushing notifications on a mobile phone task (Task A) and periodic email digesting task (Task B). In Task A, we applied the classifiers to categorize all of the input tweets. External information extracted from Google search engine was well incorporated to enhance the understanding of a users interest. In Task B, all the tweets were classified into a specific topic which was ranked by a scoring system. Finally, we used the non-negative matrix factorization clusering to remove redundancy of the classification results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangY16.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangY16,
		author = {Kai Wang and Zhen Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2016: Real-Time Summarization Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/BJUT-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangY16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PKUICST at TREC 2016 Real-Time Summarization Track: Push Notifications  and Email Digest

_Lili Yao, Chao Lv, Feifan Fan, Jianwu Yang, Dongyan Zhao_

- :fontawesome-solid-user-group: **Participant:** [PKUICST](./realtime/participants.md#pkuicst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/PKUICST-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/PKUICST-RT.pdf)
- :material-file-search: **Runs:** [PKUICSTRunB1](./realtime/runs.md#pkuicstrunb1) | [PKUICSTRunB2](./realtime/runs.md#pkuicstrunb2) | [PKUICSTRunB3](./realtime/runs.md#pkuicstrunb3) | [ru32-33](./realtime/runs.md#ru32-33) | [run1-31](./realtime/runs.md#run1-31) | [run2-32](./realtime/runs.md#run2-32)

??? abstract "Abstract"
	
	This paper describes our approaches for the TREC 2016 Real-Time Summarization track, including push notifications scenario and email digest scenario. In the push notifications scenario, we mainly focus on designing a real-time system, which listens to the Twitter sample stream and makes the push actions for the given topics. Low coupling modules are utilized to obtain the timely, relevant and novel features. In the email digest scenario, we apply the language model combined with the external knowledge base, i.e. Google, for query expansion. Besides, different text similarity algorithms are tried, such as negative KL-divergence and Simhash. Experimental results show that our two-stage filtering methods achieve good performance with respect to EG1 and nCG1 metrics for push notifications scenario. In addition, our systems for email digest scenario also obtain convincing nDCG1 scores.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YaoLFYZ16.bib) "
	```
	@inproceedings{DBLP:conf/trec/YaoLFYZ16,
		author = {Lili Yao and Chao Lv and Feifan Fan and Jianwu Yang and Dongyan Zhao},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{PKUICST} at {TREC} 2016 Real-Time Summarization Track: Push Notifications and Email Digest},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/PKUICST-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YaoLFYZ16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Total Recall 

#### TREC 2016 Total Recall Track Overview

_Maura R. Grossman, Gordon V. Cormack, Adam Roegiest_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/Overview-TR.pdf](http://trec.nist.gov/pubs/trec25/papers/Overview-TR.pdf)
??? abstract "Abstract"
	
	The primary purpose of the Total Recall Track is to evaluate, through controlled simulation, methods designed to achieve very high recall - as close as practicable to 100% - with a human assessor in the loop. Motivating applications include, among others, electronic discovery in legal proceedings [3], systematic review in evidence-based medicine [6], and the creation of fully labeled test collections for information retrieval (“IR”) evaluation [5]. A secondary, but no less important, purpose is to develop a sandboxed virtual test environment within which IR systems may be tested, while preventing the disclosure of sensitive test data to participants. At the same time, the test environment also operates as a “black box,” affording participants confidence that their proprietary systems cannot easily be reverse engineered. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanCR16.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanCR16,
		author = {Maura R. Grossman and Gordon V. Cormack and Adam Roegiest},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2016 Total Recall Track Overview},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/Overview-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanCR16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### "When to Stop" Waterloo (Cormack) Participation in the TREC 2016  Total Recall Track

_Gordon V. Cormack, Maura R. Grossman_

- :fontawesome-solid-user-group: **Participant:** [WaterlooCormack](./recall/participants.md#waterloocormack)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/WaterlooCormack-TR.pdf](http://trec.nist.gov/pubs/trec25/papers/WaterlooCormack-TR.pdf)
- :material-file-search: **Runs:** [UWathome4Knee](./recall/runs.md#uwathome4knee) | [UWathome4descKnee](./recall/runs.md#uwathome4descknee) | [UWathome4Target](./recall/runs.md#uwathome4target) | [UWathome4descTarget](./recall/runs.md#uwathome4desctarget) | [UWathome4descBaseline](./recall/runs.md#uwathome4descbaseline) | [UWathome4Baseline](./recall/runs.md#uwathome4baseline) | [uwsandboxknee](./recall/runs.md#uwsandboxknee) | [uwsandboxtarget](./recall/runs.md#uwsandboxtarget)

??? abstract "Abstract"
	
	In the course of developing tools for the 2015 Total Recal Track, Track Co-Coordinators Gordon V. Cormack and Maura R. Grossman created an autonomous continuous active learning (“CAL”) system, which was provided to participants as the baseline model implementation (“BMI”) [http://plg.uwaterloo.ca/∼gvcormac/trecvm/]. BMI employs the technology-assisted review (“TAR”) approach described by Cormack and Grossman [2]; the only difference is that BMI employs logistic regression implemented by Sofia ML [https://code.google.com/p/sofia-ml/], instead of SVMlight [http://svmlight.joachims.org/]. BMI was reprised, unchanged from TREC 2015, except for the addition of a default “call-your-shot” stopping rule indicating the system's estimate of the point at which a reasonable compromise between recall and effort had been achieved. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackG16.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackG16,
		author = {Gordon V. Cormack and Maura R. Grossman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {"When to Stop" Waterloo (Cormack) Participation in the {TREC} 2016 Total Recall Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/WaterlooCormack-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackG16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2016 Total Recall Track

_Ralph Losey, Jackson Lewis P. C., Jim Sullivan, Tony Reichenberger, Levi Kuehn, Jani Grant_

- :fontawesome-solid-user-group: **Participant:** [e-discoveryteam](./recall/participants.md#e-discoveryteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/e-Discoveryteam-TR.pdf](http://trec.nist.gov/pubs/trec25/papers/e-Discoveryteam-TR.pdf)
- :material-file-search: **Runs:** [Run1](./recall/runs.md#run1)

??? abstract "Abstract"
	
	The e-Discovery Team participated in the 2016 TREC Total Recall Track, Athome division, where thirty-four prejudged topics were considered using 290,099 emails of former Florida Governor Jeb Bush. The Team participated in TREC 2016 primarily to test the effectiveness of the standard search methodology it uses commercially to search for relevant evidence in legal proceedings: Predictive Coding 4.0 Hybrid Multimodal IST. The Team's method uses a hybrid approach to continuous active learning with both manual searches and active machine learning based document ranking searches. This is a systematic process involving implementation of a variety of search functions by skilled searchers. The Team calls this type of search multimodal because all types of search methods are used. A single expert reviewer was used in each topic along with Kroll Ontrack's search and review software, eDiscovery.com Review (EDR). The Team classified 9,863,366 documents as either relevant or irrelevant in all 34 review projects. A total of 34,723 documents were correctly classified as Relevant, as per the Team's judgment and corrected standard. The 34,723 relevant documents were found by manual review of 6,957 documents, taking a total of 234.25 man-hours. This represent an average project time of 6.89 hours per topic. The Team thus reviewed and classified documents at an average speed of 42,106 files per hour. The Team's attained an average 88% Recall score across all 34 topics using the corrected standard. The Team also attained F1 scores of greater than 90% in twelve topics, including two perfect scores of 100% F1.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LoseyCSRKG16.bib) "
	```
	@inproceedings{DBLP:conf/trec/LoseyCSRKG16,
		author = {Ralph Losey and Jackson Lewis P. C. and Jim Sullivan and Tony Reichenberger and Levi Kuehn and Jani Grant},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2016 Total Recall Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/e-Discoveryteam-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LoseyCSRKG16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Padua (IMS) at TREC 2016 Total Recall Track

_Giorgio Maria Di Nunzio, Maria Maistro, Daniel Zilio_

- :fontawesome-solid-user-group: **Participant:** [ims_unipd](./recall/participants.md#ims_unipd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/ims_unipd-TR.pdf](http://trec.nist.gov/pubs/trec25/papers/ims_unipd-TR.pdf)
- :material-file-search: **Runs:** [baseline_bm25](./recall/runs.md#baseline_bm25) | [baseline_bm25_smoothing](./recall/runs.md#baseline_bm25_smoothing) | [auto_shift_rotation](./recall/runs.md#auto_shift_rotation) | [auto_shift_rotation_exp](./recall/runs.md#auto_shift_rotation_exp)

??? abstract "Abstract"
	
	The participation of the Information Management System (IMS) Group of the University of Padua in the Total Recall track at TREC 2016 consisted in a set of fully automated experiments based on the two-dimensional probabilistic model. We trained the model in two ways that tried to mimic a real user, and we compared it to two versions of the BM25 model with different parameter settings. This initial set of experiments lays the ground for a wider study that will explore a gamification approach in the context of high recall situations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NunzioMZ16.bib) "
	```
	@inproceedings{DBLP:conf/trec/NunzioMZ16,
		author = {Giorgio Maria Di Nunzio and Maria Maistro and Daniel Zilio},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {The University of Padua {(IMS)} at {TREC} 2016 Total Recall Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/ims\_unipd-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NunzioMZ16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Exploration of Total Recall with Multiple Manual Seedings

_Jeremy Pickens, Tom Gricks, Bayu Hardi, Mark Noel, John Tredennick_

- :fontawesome-solid-user-group: **Participant:** [catres](./recall/participants.md#catres)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/catres-TR.pdf](http://trec.nist.gov/pubs/trec25/papers/catres-TR.pdf)
- :material-file-search: **Runs:** [manual_seed](./recall/runs.md#manual_seed)

??? abstract "Abstract"
	
	The Catalyst participation in the manual at home Total Recall Track had one fundamental question at the core of its run: What effect various kinds of limited human effort have on a total recall process. Our two primary modes were one-shot (single query) and interactive (multiple queries).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PickensGHNT16.bib) "
	```
	@inproceedings{DBLP:conf/trec/PickensGHNT16,
		author = {Jeremy Pickens and Tom Gricks and Bayu Hardi and Mark Noel and John Tredennick},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {An Exploration of Total Recall with Multiple Manual Seedings},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/catres-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PickensGHNT16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2016: Tasks, Total Recall, and Open Search Tracks

_Matthias Hagen, Johannes Kiesel, Payam Adineh, Masoud Alahyari, Ehsan Fatehifar, Arefeh Bahrami, Pia Fichtl, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [Webis](./recall/participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/Webis-T-TR-O.pdf](http://trec.nist.gov/pubs/trec25/papers/Webis-T-TR-O.pdf)

??? abstract "Abstract"
	
	We give a brief overview of the Webis group's participation in the TREC 2016 Tasks, Total Recall, and Open Search tracks. Our submissions to the Tasks track are similar to our last year's system. In the task understanding subtask of the Tasks track, we use different data sources (ClueWeb12 anchor texts, AOL query log, Wikidata, etc.) and APIs (Google, Bing, etc.) to retrieve suggestions related to a given query. For the task completion and ad-hoc subtask, we combine the results of the Indri search engine for the different related queries identified in the task understanding subtask. Our system for the the Total Recall track also is similar to our last year's idea with some slight changes in the details; we employ a simple SVM baseline with variable batch sizes equipped with a keyqueries step to identify potentially relevant documents. In the Open Search track, we axiomatically re-rank a BM25-ordered result list to come up with a final document ranking
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenKAAFBFS16.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenKAAFBFS16,
		author = {Matthias Hagen and Johannes Kiesel and Payam Adineh and Masoud Alahyari and Ehsan Fatehifar and Arefeh Bahrami and Pia Fichtl and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2016: Tasks, Total Recall, and Open Search Tracks},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/Webis-T-TR-O.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenKAAFBFS16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### San Francisco State University (SFSU) at Total Recall Track of TREC  2016

_Mon-Shih Chuang, Anagha Kulkarni_

- :fontawesome-solid-user-group: **Participant:** [IR.SFSU.2016](./recall/participants.md#ir.sfsu.2016)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/IR.SFSU.2016-TR.pdf](http://trec.nist.gov/pubs/trec25/papers/IR.SFSU.2016-TR.pdf)
- :material-file-search: **Runs:** [ah4_run1](./recall/runs.md#ah4_run1) | [ah4_run2_seed_expansion](./recall/runs.md#ah4_run2_seed_expansion) | [ah4_descsubset](./recall/runs.md#ah4_descsubset) | [sandbox_run](./recall/runs.md#sandbox_run)

??? abstract "Abstract"
	
	This paper describes the participation of San Francisco State University group in Text Retrieval Conference (TREC) 2016 Total Recall Track from National Institute of Standard and Technology (NIST). The TREC series provide large test collections and judgements for participant to design Information Retrieval (IR) systems for different proposes. The purpose of Total Recall Track is seeking text search system which achieves high recall with minimum number of return documents. This year, our team participates all automatic tasks, including 34 topics in athome task and 2 datasets in sandbox task. Our system is built based on the autonomous technology-assisted review (Auto TAR) model[1], which is also the baseline of Total Recall Track. In this paper, we will introduce several approaches which have improved the evaluation metrics compare to the baseline model. Our enhanced model combines seed expansion and feature engineering including adding n-gram, eliminating stop words, and preserving words contain digits.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChuangK16.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChuangK16,
		author = {Mon{-}Shih Chuang and Anagha Kulkarni},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {San Francisco State University {(SFSU)} at Total Recall Track of {TREC} 2016},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/IR.SFSU.2016-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChuangK16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Tasks 

#### Overview of the TREC Tasks Track 2016

_Manisha Verma, Emine Yilmaz, Rishabh Mehrotra, Evangelos Kanoulas, Ben Carterette, Nick Craswell, Peter Bailey_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/Overview-T.pdf](http://trec.nist.gov/pubs/trec25/papers/Overview-T.pdf)
??? abstract "Abstract"
	
	Research in Information Retrieval has traditionally focused on serving the best results for a single query, ignoring the reasons (or the task) that might have motivated the user to submit that query. Often times search engines are used to complete complex tasks (information needs); achieving these tasks with current search engines requires users to issue multiple queries. For example, booking travel to a location such as London could require the user to submit various queries such as flights to London, hotels in London, points of interest around London etc. Standard evaluation mechanisms focus on evaluating the quality of a retrieval system in terms of the relevance of the results retrieved, completely ignoring the fact that user satisfaction mainly depends on the usefulness of the system in helping the user complete the actual task that led the user issue the query. Similar to Tasks Track 2015 [1], Tasks Track 2016 is an attempt investigate quality of retrieval systems in terms of (1) how well they can understand the underlying task that led the user submit a query, and (2) how useful they are for helping users complete their tasks. In this overview, we first summarise the three categories of evaluation mechanisms used in the track and briefly describe the corpus, topics, and tasks that comprise the test collections. We then give an overview of the runs submitted to the Tasks Track and present evaluation results and analysis.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VermaYMKCCB16.bib) "
	```
	@inproceedings{DBLP:conf/trec/VermaYMKCCB16,
		author = {Manisha Verma and Emine Yilmaz and Rishabh Mehrotra and Evangelos Kanoulas and Ben Carterette and Nick Craswell and Peter Bailey},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} Tasks Track 2016},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/Overview-T.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VermaYMKCCB16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Stavanger at the TREC 2016 Tasks Track

_Darío Garigliotti, Krisztian Balog_

- :fontawesome-solid-user-group: **Participant:** [UiS](./task/participants.md#uis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/UiS-T.pdf](http://trec.nist.gov/pubs/trec25/papers/UiS-T.pdf)
- :material-file-search: **Runs:** [UiS_4](./task/runs.md#uis_4) | [UiS_8](./task/runs.md#uis_8) | [UiS_9](./task/runs.md#uis_9)

??? abstract "Abstract"
	
	This paper describes our participation in the Task understanding task of the Tasks track at TREC 2016. We introduce a general probabilistic framework in which we combine query suggestions from web search engines with keyphrases generated from top ranked documents. We achieved top performance among all submitted systems, on both official evaluation metrics, which attests the effectiveness of our approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GarigliottiB16.bib) "
	```
	@inproceedings{DBLP:conf/trec/GarigliottiB16,
		author = {Dar{\'{\i}}o Garigliotti and Krisztian Balog},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {The University of Stavanger at the {TREC} 2016 Tasks Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/UiS-T.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GarigliottiB16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2016: Tasks, Total Recall, and Open Search Tracks

_Matthias Hagen, Johannes Kiesel, Payam Adineh, Masoud Alahyari, Ehsan Fatehifar, Arefeh Bahrami, Pia Fichtl, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [Webis](./task/participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/Webis-T-TR-O.pdf](http://trec.nist.gov/pubs/trec25/papers/Webis-T-TR-O.pdf)
- :material-file-search: **Runs:** [webisA1](./task/runs.md#webisa1) | [webisA2](./task/runs.md#webisa2) | [webisA3](./task/runs.md#webisa3) | [webisC1](./task/runs.md#webisc1) | [webisC2](./task/runs.md#webisc2) | [webisC3](./task/runs.md#webisc3) | [webis1](./task/runs.md#webis1) | [webis2](./task/runs.md#webis2) | [webis3](./task/runs.md#webis3)

??? abstract "Abstract"
	
	We give a brief overview of the Webis group's participation in the TREC 2016 Tasks, Total Recall, and Open Search tracks. Our submissions to the Tasks track are similar to our last year's system. In the task understanding subtask of the Tasks track, we use different data sources (ClueWeb12 anchor texts, AOL query log, Wikidata, etc.) and APIs (Google, Bing, etc.) to retrieve suggestions related to a given query. For the task completion and ad-hoc subtask, we combine the results of the Indri search engine for the different related queries identified in the task understanding subtask. Our system for the the Total Recall track also is similar to our last year's idea with some slight changes in the details; we employ a simple SVM baseline with variable batch sizes equipped with a keyqueries step to identify potentially relevant documents. In the Open Search track, we axiomatically re-rank a BM25-ordered result list to come up with a final document ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenKAAFBFS16.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenKAAFBFS16,
		author = {Matthias Hagen and Johannes Kiesel and Payam Adineh and Masoud Alahyari and Ehsan Fatehifar and Arefeh Bahrami and Pia Fichtl and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2016: Tasks, Total Recall, and Open Search Tracks},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/Webis-T-TR-O.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenKAAFBFS16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Dynamic Domain 

#### TREC 2016 Dynamic Domain Track Overview

_Grace Hui Yang, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/Overview-DD.pdf](http://trec.nist.gov/pubs/trec25/papers/Overview-DD.pdf)
??? abstract "Abstract"
	
	The main goal of TREC dynamic domain track is to explore and evaluate systems for interactive information retrieval, which reflects real-world search scenarios. Due to the importance of learning from user interactions, this track has been held for the second year. The name of the track contains two parts. “Dynamic” means that the search system dynamically adapts the provided ranking to the user through interactions. “Domain” stems from the fact that the search task in the track is on the domains of special interests, which tend to bring information needs that would not be met within a single interaction. The task is inspired by interested groups in government, including the DARPA Memex program. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangS16.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangS16,
		author = {Grace Hui Yang and Ian Soboroff},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2016 Dynamic Domain Track Overview},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/Overview-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangS16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT @ TREC 2016 Dynamic Domain Track: Exploiting Passage Representation  for Retrieval and Relevance Feedback

_Ameer Albahem, Damiano Spina, Lawrence Cavedon, Falk Scholer_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./domain/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/RMIT-DD.pdf](http://trec.nist.gov/pubs/trec25/papers/RMIT-DD.pdf)
- :material-file-search: **Runs:** [rmit_lm_nqe](./domain/runs.md#rmit_lm_nqe) | [rmit_oracle.lm.1000](./domain/runs.md#rmit_oracle.lm.1000) | [rmit_lm_psg.max](./domain/runs.md#rmit_lm_psg.max) | [rmit_lm_rocchio.Rp.NRd.10](./domain/runs.md#rmit_lm_rocchio.rp.nrd.10)

??? abstract "Abstract"
	
	The TREC Dynamic Domain search task addresses search scenarios where users engage interactively with search systems to tackle domain specific information needs. In our participation, we focused on utilizing passage-based representations in document retrieval and user feedback processing. In addition, we submitted a baseline retrieval method and a manual run that considers only relevant documents in the top 1000 retrieved documents. Results show that the passage based representation is inferior to the baseline method but differences are not statistically significant in terms of the Cube Test and the Average Cube Test metrics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlbahemSCS16.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlbahemSCS16,
		author = {Ameer Albahem and Damiano Spina and Lawrence Cavedon and Falk Scholer},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{RMIT} @ {TREC} 2016 Dynamic Domain Track: Exploiting Passage Representation for Retrieval and Relevance Feedback},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/RMIT-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlbahemSCS16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Evaluation of a Feedback Algorithm inspired by Quantum Detection for  Dynamic Search Tasks

_Emanuele Di Buccio, Massimo Melucci_

- :fontawesome-solid-user-group: **Participant:** [UPD_IA](./domain/participants.md#upd_ia)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/UPD_IA-DD.pdf](http://trec.nist.gov/pubs/trec25/papers/UPD_IA-DD.pdf)
- :material-file-search: **Runs:** [UPD_IA_BiQBFi](./domain/runs.md#upd_ia_biqbfi) | [UPD_IA_BiQBDiJ](./domain/runs.md#upd_ia_biqbdij)

??? abstract "Abstract"
	
	In this paper we investigate the effectiveness of Relevance Feedback algorithms inspired by Quantum Detection in the context of the Dynamic Domain track. Documents and queries are represented as vectors; the query vector is projected into the subspace spanned by the eigenvector which maximizes the distance between the distribution of quantum probability of relevance and the distribution of quantum probability of non-relevance. When relevant documents are present in the feedback set, the algorithm performs Explicit RF exploiting evidence gathered from relevant passages; if all the documents in the top retrieved are judged as non-relevant, Pseudo RF is performed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuccioM16.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuccioM16,
		author = {Emanuele Di Buccio and Massimo Melucci},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Evaluation of a Feedback Algorithm inspired by Quantum Detection for Dynamic Search Tasks},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/UPD\_IA-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuccioM16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Laval University at TREC Dynamic Domain 2016: Subtopic extraction  focused on Named Entities

_Robin Joganah, Richard Khoury, Luc Lamontagne_

- :fontawesome-solid-user-group: **Participant:** [LavalLakehead](./domain/participants.md#lavallakehead)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/LavalLakehead-DD.pdf](http://trec.nist.gov/pubs/trec25/papers/LavalLakehead-DD.pdf)
- :material-file-search: **Runs:** [UL_BM25](./domain/runs.md#ul_bm25) | [UL_LDA_200](./domain/runs.md#ul_lda_200) | [UL_LDA_NE](./domain/runs.md#ul_lda_ne) | [UL_LDA_Psum](./domain/runs.md#ul_lda_psum) | [UL_Kmeans](./domain/runs.md#ul_kmeans)

??? abstract "Abstract"
	
	This paper describes the results submitted by Laval University to the TREC 2016 Dynamic Domain track. We submitted five runs. For this year we decided to focus around Named Entities to interpret the subtopics. Named Entities are one of the two types of queries we identified in this challenge, the other being queries about concepts. We describe in this paper our experiments to determine if targeting this type of query with a specific pipeline can lead to a global improvement of the system by taking into account the specificity of the queries
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JoganahKL16.bib) "
	```
	@inproceedings{DBLP:conf/trec/JoganahKL16,
		author = {Robin Joganah and Richard Khoury and Luc Lamontagne},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Laval University at {TREC} Dynamic Domain 2016: Subtopic extraction focused on Named Entities},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/LavalLakehead-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JoganahKL16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UFMG at the TREC 2016 Dynamic Domain track

_Felipe Moraes, Rodrygo L. T. Santos, Nivio Ziviani_

- :fontawesome-solid-user-group: **Participant:** [ufmg](./domain/participants.md#ufmg)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/ufmg-DD.pdf](http://trec.nist.gov/pubs/trec25/papers/ufmg-DD.pdf)
- :material-file-search: **Runs:** [ufmgHS2](./domain/runs.md#ufmghs2) | [ufmgXS2](./domain/runs.md#ufmgxs2) | [ufmgHM2](./domain/runs.md#ufmghm2) | [ufmgXM2](./domain/runs.md#ufmgxm2) | [ufmgHM3](./domain/runs.md#ufmghm3)

??? abstract "Abstract"
	
	In TREC 2016, we focus on tackling the challenges posed by the Dynamic Domain (DD) track. The goal of the TREC DD track is to support research in dynamic, exploratory search within a complex domain. To this end, our participation investigates the suitability of multiple diversification approaches for dynamic information retrieval. In particular, based on fine-grained real-time feedback obtained from a simulated user, we apply diversification strategies that make use of single-source as well multi-source information for mining flat or hierarchical query aspects.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoraesSZZ16.bib) "
	```
	@inproceedings{DBLP:conf/trec/MoraesSZZ16,
		author = {Felipe Moraes and Rodrygo L. T. Santos and Nivio Ziviani},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UFMG} at the {TREC} 2016 Dynamic Domain track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/ufmg-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MoraesSZZ16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Investigation of Basic Retrieval Models for the Dynamic Domain  Task

_Razieh Rahimi, Grace Hui Yang_

- :fontawesome-solid-user-group: **Participant:** [georgetown](./domain/participants.md#georgetown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/georgetown-DD.pdf](http://trec.nist.gov/pubs/trec25/papers/georgetown-DD.pdf)
- :material-file-search: **Runs:** [FirstIterBaseline](./domain/runs.md#firstiterbaseline) | [SecondIterationBaseline](./domain/runs.md#seconditerationbaseline) | [FifthIterBaseline](./domain/runs.md#fifthiterbaseline) | [TenthIterBaseline](./domain/runs.md#tenthiterbaseline)

??? abstract "Abstract"
	
	TREC dynamic domain is a new challenging task, which aims to simultaneously optimize the performance of retrieval and the number of iterations to accomplish the search task in a session-based search environment with a more sophisticated feedback information from the user. As a first step towards developing an effective search systems for this task, we investigate the characteristics of the newly created dataset for this task, and performance of basic well-known retrieval models for it. Our investigation demonstrates that the query sets contain multiple difficult queries, where initial results may provide very limited evidence for improvement in subsequent iterations. The new setting of the task and characteristics of dataset stress the need for more comprehensive metrics of performance evaluation, in terms of result diversity as an example.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RahimiY16.bib) "
	```
	@inproceedings{DBLP:conf/trec/RahimiY16,
		author = {Razieh Rahimi and Grace Hui Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {An Investigation of Basic Retrieval Models for the Dynamic Domain Task},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/georgetown-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RahimiY16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## OpenSearch 

#### Webis at TREC 2016: Tasks, Total Recall, and Open Search Tracks

_Matthias Hagen, Johannes Kiesel, Payam Adineh, Masoud Alahyari, Ehsan Fatehifar, Arefeh Bahrami, Pia Fichtl, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [Webis](./open/participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/Webis-T-TR-O.pdf](http://trec.nist.gov/pubs/trec25/papers/Webis-T-TR-O.pdf)
- :material-file-search: **Runs:** [webis-SSOAR-2](./open/runs.md#webis-ssoar-2) | [webis-CiteSeerX-2](./open/runs.md#webis-citeseerx-2)

??? abstract "Abstract"
	
	We give a brief overview of the Webis group's participation in the TREC 2016 Tasks, Total Recall, and Open Search tracks. Our submissions to the Tasks track are similar to our last year's system. In the task understanding subtask of the Tasks track, we use different data sources (ClueWeb12 anchor texts, AOL query log, Wikidata, etc.) and APIs (Google, Bing, etc.) to retrieve suggestions related to a given query. For the task completion and ad-hoc subtask, we combine the results of the Indri search engine for the different related queries identified in the task understanding subtask. Our system for the the Total Recall track also is similar to our last year's idea with some slight changes in the details; we employ a simple SVM baseline with variable batch sizes equipped with a keyqueries step to identify potentially relevant documents. In the Open Search track, we axiomatically re-rank a BM25-ordered result list to come up with a final document ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenKAAFBFS16.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenKAAFBFS16,
		author = {Matthias Hagen and Johannes Kiesel and Payam Adineh and Masoud Alahyari and Ehsan Fatehifar and Arefeh Bahrami and Pia Fichtl and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2016: Tasks, Total Recall, and Open Search Tracks},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/Webis-T-TR-O.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenKAAFBFS16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2016 OpenSearch Track: Search Ranking Based on Clickthrough  Data

_Cheng Li, Zhen Yang, David Lillis_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./open/participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/BJUT-O.pdf](http://trec.nist.gov/pubs/trec25/papers/BJUT-O.pdf)
- :material-file-search: **Runs:** [BJUT-CiteSeerX-1](./open/runs.md#bjut-citeseerx-1) | [BJUT-CiteSeerX-2](./open/runs.md#bjut-citeseerx-2)

??? abstract "Abstract"
	
	In this paper we describe our efforts for the TREC OpenSearch task. Our goal for this year is to evaluate the effectiveness of: (1) a ranking method using information crawled from an authoritative search engine; (2) search ranking based on clickthrough data taken from user feedback; and (3) a unified modeling method that combines knowledge from the web search engine and the users' clickthrough data. Finally, we conduct extensive experiments to evaluate the proposed framework on the TREC 2016 OpenSearch data set, with promising results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiYL16.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiYL16,
		author = {Cheng Li and Zhen Yang and David Lillis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2016 OpenSearch Track: Search Ranking Based on Clickthrough Data},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/BJUT-O.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiYL16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IR-IITBHU at TREC 2016 Open Search Track: Retrieving documents  using Divergence From Randomness model in Terrier

_Mitodru Niyogi, Sukomal Pal_

- :fontawesome-solid-user-group: **Participant:** [IR-IITBHU](./open/participants.md#ir-iitbhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/IR-IITBHU-O.pdf](http://trec.nist.gov/pubs/trec25/papers/IR-IITBHU-O.pdf)
- :material-file-search: **Runs:** [opensearch_404-CiteSeerX-1](./open/runs.md#opensearch_404-citeseerx-1) | [opensearch_404-CiteSeerX-2](./open/runs.md#opensearch_404-citeseerx-2) | [opensearch_404-SSOAR-1](./open/runs.md#opensearch_404-ssoar-1) | [opensearch_404-SSOAR-2](./open/runs.md#opensearch_404-ssoar-2)

??? abstract "Abstract"
	
	In our participation at TREC 2016 Open Search Track which focuses on ad-hoc scientifc literature search, we used Terrier, a modular and a scalable Information Retrieval framework as a tool to rank documents. The organizers provided live data as documents, queries and user interactions from real search engine that were available through Living Lab API framework. The data was then converted into TREC format to be used in Terrier. We used Divergence from Randomness (DFR) model, specifically, the Inverse expected document frequency model for randomness, the ratio of two Bernoulli's processes for first normalisation, and normalisation 2 for term frequency normalization with natural logarithm, i.e., In_expC2 model to rank the available documents in response to a set of queries. Altogether we submit 391 runs for sites CiteSeerX and SSOAR to the Open Search Track via the Living Lab API framework. We received an `outcome' of 0.72 for test queries and 0.62 for train queries of site CiteSeerX at the end of Round 3 Test Period where, the 'outcome' is computed as: #wins / (#wins + #losses). A `win' occurs when the participant achieves more clicks on his documents than those of the site and `loss' otherwise. Complete relevance judgments is awaited at the moment. We look forward to getting the users' feedback and work further with them.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NiyogiP16.bib) "
	```
	@inproceedings{DBLP:conf/trec/NiyogiP16,
		author = {Mitodru Niyogi and Sukomal Pal},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IR-IITBHU} at {TREC} 2016 Open Search Track: Retrieving documents using Divergence From Randomness model in Terrier},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/IR-IITBHU-O.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NiyogiP16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Popularity Ranking for Scientific Literature Using the Characteristic  Scores and Scale Method

_Philipp Schaer, Narges Tavakolpoursaleh_

- :fontawesome-solid-user-group: **Participant:** [THKoeln-GESIS](./open/participants.md#thkoeln-gesis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/THKoeln-GESIS-O.pdf](http://trec.nist.gov/pubs/trec25/papers/THKoeln-GESIS-O.pdf)
- :material-file-search: **Runs:** [Gesis-SSOAR-1](./open/runs.md#gesis-ssoar-1) | [Gesis-SSOAR-2](./open/runs.md#gesis-ssoar-2) | [Gesis-CiteSeerX-1](./open/runs.md#gesis-citeseerx-1) | [Gesis-CiteSeerX-2](./open/runs.md#gesis-citeseerx-2)

??? abstract "Abstract"
	
	The TREC 2016 OpenSearch track is focused on ad-hoc search for scientific literature. Three scientific search engines and document repositories were part of this living lab-centered evaluation campaign: (1) CiteSeerX, (2) Microsoft Academic Search, and (3) SSOAR - Social Science Open Access Repository. The authors of this paper are also responsible for the implementation of the living lab infrastructure and the LL4IR API that is necessary to include an online system into the OpenSearch evaluation campaign. This work is based on a Master's thesis at University of Bonn [7]. Implementation details can be found there and in the lab's overview paper [1] and from a higher perspective in [6]. In this paper we will present our work on popularity-based relevance ranking within the two systems CiteSeerX and SSOAR. Both offer different types of usage and popularity data. We would like to test a normalization method for these kind of data known as the Characteristic Scores and Scale Method (CSS).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchaerT16.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchaerT16,
		author = {Philipp Schaer and Narges Tavakolpoursaleh},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Popularity Ranking for Scientific Literature Using the Characteristic Scores and Scale Method},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/THKoeln-GESIS-O.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchaerT16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

