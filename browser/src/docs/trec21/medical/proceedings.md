# Proceedings - Medical 2012 

#### Overview of the TREC 2012 Medical Records Track

_Ellen M. Voorhees, William R. Hersh_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/MED12OVERVIEW.pdf](http://trec.nist.gov/pubs/trec21/papers/MED12OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC Medical Records track fosters research that allows electronic health records to be retrieved based on the semantic content of free-text fields. The ability to find records by matching semantic content will enhance clinical care and support the secondary use of medical records in clinical trials and epidemiological studies. TREC 2012 is the sophomore year of the track, which attracted 24 participating research groups. The track repeated the cohort-finding task from its initial year. This task is an ad hoc search task in which systems search a set of de-identified clinical reports to identify cohorts for (possible) clinical studies. A topic statement for the task describes the criteria for inclusion in a study, and a system returns a list of “visits” ordered by the likelihood that the inclusion criteria are satisfied. Physicians created fifty topics and performed relevance judgments for the track. Top-performing groups each used some sort of vocabulary normalization device specific to the medical domain, supporting the hypothesis that language use within electronic health records is sufficiently different from general use to warrant domain-specific processing. Such devices must be used carefully, however, as multiple groups also demonstrated that aggressive use harms baseline performance. Exploiting human expertise through manual query construction proved most effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VoorheesH12.bib) "
	```
	@inproceedings{DBLP:conf/trec/VoorheesH12,
		author = {Ellen M. Voorhees and William R. Hersh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2012 Medical Records Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/MED12OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VoorheesH12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Meda-data to Search for Clinical Records: RMIT at TREC 2012  Medical Track

_Iman Amini, Mark Sanderson, Xiaodong Li, David Martínez_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/RMIT.medical.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/RMIT.medical.nb.pdf)
- :material-file-search: **Runs:** [APRel1](./runs.md#aprel1) | [GE4](./runs.md#ge4) | [APRel2](./runs.md#aprel2) | [RAPRel2](./runs.md#raprel2)

??? abstract "Abstract"
	
	Clinical records contain International Classification of Diseases (ICD) codes summarizing the primary and/or secondary diseases of patients; these codes can be used as evidence to find relevant documents. In this paper we propose a novel approach to locally build a knowledge source from the existing data set to be used for query expansion, exploiting the ICD codes. While this approach does not rely on any external knowledge sources, it proves to be significantly superior to our global expansion and baseline systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AminiSLM12.bib) "
	```
	@inproceedings{DBLP:conf/trec/AminiSLM12,
		author = {Iman Amini and Mark Sanderson and Xiaodong Li and David Mart{\'{\i}}nez},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Meda-data to Search for Clinical Records: {RMIT} at {TREC} 2012 Medical Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/RMIT.medical.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AminiSLM12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Identifying Patients for Clinical Studies from Electronic Health Records:  TREC 2012 Medical Records Track at OHSU

_Steven Bedrick, Tracy Edinger, Aaron M. Cohen, William R. Hersh_

- :fontawesome-solid-user-group: **Participant:** [OHSU](./participants.md#ohsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/OHSU.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/OHSU.medical.final.pdf)
- :material-file-search: **Runs:** [ohsuManBool](./runs.md#ohsumanbool) | [OHSUCombICD](./runs.md#ohsucombicd) | [OHSUCombET](./runs.md#ohsucombet) | [OHSUCEtICD](./runs.md#ohsuceticd)

??? abstract "Abstract"
	
	The goal of the TREC 2012 Medical Records Track was to search medical record documents to identify patients as possible candidates for clinical studies based on diagnosis, age, and other attributes. For TREC 2012, the Oregon Health & Science University (OHSU) group experimented with both manual and automated techniques. We used a derivative of Lucene to build an interactive retrieval system that can process queries in one of two ways. Users can manually specify Boolean queries whose terms may include words as well as ICD-9 codes. Alternatively, the system features an automated query parser that transforms free-text queries into structured Boolean queries. The query parser is built on top of MetaMap and the UMLS Metathesaurus. We submitted both automatic runs (which relied solely on the automated query parser) as well as manual runs consisting of queries built by an expert clinician. Overall, our automated query parser performed below the mean of other groups, although there were individual topics for which it performed very well. This irregular performance was in part due to our parser's tendency to over-specify queries, leading to reduced recall. There were, however, several topics for which our parser performed very well, suggesting that our fundamental approach has merit. In contrast, our manual runs performed very well, scoring second-best among official manual runs. With further modification of the manual queries, we were able to achieve even better performance. Query of electronic health records for the use case of identifying patients as candidates for clinical studies still requires manual query development, at least until better automated methods can be developed that outperform them.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BedrickECH12.bib) "
	```
	@inproceedings{DBLP:conf/trec/BedrickECH12,
		author = {Steven Bedrick and Tracy Edinger and Aaron M. Cohen and William R. Hersh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Identifying Patients for Clinical Studies from Electronic Health Records: {TREC} 2012 Medical Records Track at {OHSU}},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/OHSU.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BedrickECH12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCD IIRG at TREC 2012 Medical Track

_James Cogley, Nicola Stokes, John Dunnion, Joe Carthy_

- :fontawesome-solid-user-group: **Participant:** [UCD_CSI](./participants.md#ucd_csi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UCD_CSI.medical.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/UCD_CSI.medical.nb.pdf)
- :material-file-search: **Runs:** [UCDCSI1](./runs.md#ucdcsi1) | [UCDCSI2](./runs.md#ucdcsi2) | [UCDCSI3](./runs.md#ucdcsi3) | [UCDCSI4](./runs.md#ucdcsi4)

??? abstract "Abstract"
	
	This paper describes the participation of UCD IIRG in the TREC 2012 Medical Records track, which fosters research in the retrieval of electronic health records using free text fields. Our contributions to this track investigate several problem areas in the retrieval of medical documents. Multiple knowledge sources are investigated to alleviate the issue of vocabulary mismatch. Medical records are verbose documents that give a full picture of a patient's medical status including their family health information and their own medical history. A Condition Attribution and Temporal Grounding system is implemented to address such occurrences. A rule-based system is employed in order to extract the patient's demographic information from their medical record. All extracted information is then leveraged using Indri's structured query language. These methods are combined to identify patients who fit the exact criteria as described in natural language queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CogleySDC12.bib) "
	```
	@inproceedings{DBLP:conf/trec/CogleySDC12,
		author = {James Cogley and Nicola Stokes and John Dunnion and Joe Carthy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UCD} {IIRG} at {TREC} 2012 Medical Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/UCD\_CSI.medical.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CogleySDC12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NLM at TREC 2012 Medical Records Track

_Dina Demner-Fushman, Swapna Abhyankar, Antonio Jimeno-Yepes, Russell F. Loane, François-Michel Lang, James G. Mork, Nicolas Ide, Alan R. Aronson_

- :fontawesome-solid-user-group: **Participant:** [NLM](./participants.md#nlm)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/NLM.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/NLM.medical.final.pdf)
- :material-file-search: **Runs:** [NLMManual](./runs.md#nlmmanual) | [NLMLuceneExp](./runs.md#nlmluceneexp) | [EssieAuto](./runs.md#essieauto) | [NLMLuceneSec](./runs.md#nlmlucenesec)

??? abstract "Abstract"
	
	The NLM team used the relevance judgments for the 2011 Medical Records track (that focused on finding patients eligible for clinical studies) to analyze the components of our 2011 systems. The analysis showed that the components provided moderate improvements over the baseline (established submitting 2011 topics 'as is' to Lucene) for some topics and did not harm the results for any other topics. Our experiments confirmed that implementing methods (such as negation detection and section splitting) motivated by clinical text processing experience could improve identifying patients that meet complex criteria for inclusion in cohort studies. We therefore largely used the 2011 system with minor modifications for document processing. We submitted three automatic runs: an Essie baseline run, and two Lucene runs that used the 2011 system with minor modifications. We also submitted an interactive run for which the queries were interactively modified using Essie until either the top ten retrieved documents appeared mostly relevant or no relevant documents could be found. Our interactive queries submitted to Essie significantly outperformed all our other runs and were significantly above the medians for all submission types (achieving 0.37 infAP; 0.68 infNDCG; 0.75 P@10; and 0.48 R-prec). Interestingly, the values of the two metrics common for the two years of this track are very close to the values achieved in 2011. The hypothetical overall-best and best-manual performances are significantly better than our interactive run. Our Lucene run that used the topic frames and web-based expansion is significantly better than the Lucene baseline run and the medians (on all metrics but P@10 for the medians), but it is not significantly better than our other automatic runs. Our other automatic runs are not significantly above the medians. As in 2011, we conclude that the existing search engines are mature enough to support cohort selection tasks, and the quality of the queries could be significantly improved with a modest interactive effort.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Demner-FushmanA12.bib) "
	```
	@inproceedings{DBLP:conf/trec/Demner-FushmanA12,
		author = {Dina Demner{-}Fushman and Swapna Abhyankar and Antonio Jimeno{-}Yepes and Russell F. Loane and Fran{\c{c}}ois{-}Michel Lang and James G. Mork and Nicolas Ide and Alan R. Aronson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{NLM} at {TREC} 2012 Medical Records Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/NLM.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Demner-FushmanA12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCM at TREC 2012: Does Negation Influence The Retrieval of Medical  Reports?

_Alberto Díaz, Miguel Ballesteros, Jorge Carrillo de Albornoz, Laura Plaza_

- :fontawesome-solid-user-group: **Participant:** [NIL_UCM](./participants.md#nil_ucm)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/NIL_UCM.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/NIL_UCM.medical.final.pdf)
- :material-file-search: **Runs:** [ucm4](./runs.md#ucm4) | [ucm5](./runs.md#ucm5) | [ucm3](./runs.md#ucm3) | [ucm1](./runs.md#ucm1)

??? abstract "Abstract"
	
	This paper details the UCM participation in the TREC 2012 Medical Records Track. We present several experiments directed to evaluate the effect of detecting negation in the task of retrieving medical reports. In particular, two different algorithms based on syntactic analysis have been applied to detect negations and to infer their scope. These algorithms are then combined with a simple term-frequency approach using Lucene to retrieve the reports that are relevant to a given query. We evaluate whether ignoring the information that is within the scope of negation may result in a higher retrieving performance. However, our experiments reveal that the effect of negation in this task is not significant.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DiazBAP12.bib) "
	```
	@inproceedings{DBLP:conf/trec/DiazBAP12,
		author = {Alberto D{\'{\i}}az and Miguel Ballesteros and Jorge Carrillo de Albornoz and Laura Plaza},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UCM} at {TREC} 2012: Does Negation Influence The Retrieval of Medical Reports?},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/NIL\_UCM.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DiazBAP12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Cohort Sherpherd II: Verifying Cohort Constraints from Hospital  Visits

_Travis R. Goodwin, Kirk Roberts, Bryan Rink, Sanda M. Harabagiu_

- :fontawesome-solid-user-group: **Participant:** [UTDHLT](./participants.md#utdhlt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UTDHLT.medical.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/UTDHLT.medical.nb.pdf)
- :material-file-search: **Runs:** [UTDHLTNASK](./runs.md#utdhltnask) | [UTDHLTASK](./runs.md#utdhltask) | [UTDHLTNA](./runs.md#utdhltna) | [UTDHLTA](./runs.md#utdhlta)

??? abstract "Abstract"
	
	This paper describes the updated system created by the University of Texas at Dallas for content-based medical record retrieval submitted to the TREC 2012 Medical Records Track. Our system updates our work from the previous year by building a structured query for each cohort that captures the patient's age, gender, hospital status, and medical assertion information. Further, all keywords that encode any medical phenomena from the query are recursively decomposed before being expanded using knowledge from UMLS, SNOMED, Wikipedia, and PubMed co-occurrences. An initial ranking of hospital visits is then obtained using BM25 relevance on an interpolation of these decomposed keywords. Finally, hospital visits are re-ranked according to the constraints extracted in the structured query. Four runs were submitted, comparing pair-wise combinations of complete vs. shallow keyword decomposition and full vs. negation-only assertion processing. Our highest scoring submission achieved an infNDCG score of 0.426.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GoodwinRRH12.bib) "
	```
	@inproceedings{DBLP:conf/trec/GoodwinRRH12,
		author = {Travis R. Goodwin and Kirk Roberts and Bryan Rink and Sanda M. Harabagiu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Cohort Sherpherd {II:} Verifying Cohort Constraints from Hospital Visits},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/UTDHLT.medical.nb.pdf},
		timestamp = {Mon, 19 Apr 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GoodwinRRH12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LSIS at TREC 2012 Medical Track - Experiments With Conceptualization,  a DFR Model and a Semantic Measure

_Hussam Hamdan, Shereen Albitar, Patrice Bellot, Bernard Espinasse, Sébastien Fournier_

- :fontawesome-solid-user-group: **Participant:** [LSIS](./participants.md#lsis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/LSIS.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/LSIS.medical.final.pdf)
- :material-file-search: **Runs:** [LSIS1](./runs.md#lsis1) | [LSIS2](./runs.md#lsis2) | [LSIS3](./runs.md#lsis3)

??? abstract "Abstract"
	
	In this paper, we present our participation in the Medical Records Track of TREC2012. We focus on the impact of combining the word space and the concept space in the information retrieval process. For this track, we submitted a baseline run by employing the In_expC2 weighting model implemented in the Terrier platform, which achieved fair results (0.304 MAP, 0.51P@10). Then, we expanded the documents by performing automatic text conceptualization using UMLS® and the MetaMap software on medical records. These textual and conceptual representations, still using the DFR model, led to precision (0.29 MAP, 0.47 P@10). We also automatically extended the topics with UMLS® concepts. This led to a lower precision (0.27 MAP, 0.46 P@10) Lastly, we experimented the usage of semantic IR measures only (0.21 MAP, 0.41 P@10)..
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HamdanABEF12.bib) "
	```
	@inproceedings{DBLP:conf/trec/HamdanABEF12,
		author = {Hussam Hamdan and Shereen Albitar and Patrice Bellot and Bernard Espinasse and S{\'{e}}bastien Fournier},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{LSIS} at {TREC} 2012 Medical Track - Experiments With Conceptualization, a {DFR} Model and a Semantic Measure},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/LSIS.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HamdanABEF12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Exploration and Learning for Medical Records Search: An Experiment  in Identifying Cohorts for Comparative Effectiveness Research

_Harvey S. Hyman, Warren Fridy III_

- :fontawesome-solid-user-group: **Participant:** [USF_ISDS](./participants.md#usf_isds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/USF_ISDS.medical.pdf](http://trec.nist.gov/pubs/trec21/papers/USF_ISDS.medical.pdf)
- :material-file-search: **Runs:** [USFISDS1](./runs.md#usfisds1) | [USFISDS2](./runs.md#usfisds2)

??? abstract "Abstract"
	
	This paper describes an experiment performed on a medical record data set, using an information retrieval (IR) tool that applies the techniques of exploration and learning, to assist a researcher in identifying the most relevant cohorts. The paper presents some brief background on exploration and learning, how they are incorporated in the IR tool, and an instantiation of exploration and learning used for selecting cohorts for a research population. The research problem addressed in this paper is the TREC 2012 Medical Track task: How to provide content-based access to free-text fields of electronic medical records? The stated goal of the task is to 'find a population over which comparative effectiveness studies can be done.'
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HymanF12.bib) "
	```
	@inproceedings{DBLP:conf/trec/HymanF12,
		author = {Harvey S. Hyman and Warren Fridy III},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Exploration and Learning for Medical Records Search: An Experiment in Identifying Cohorts for Comparative Effectiveness Research},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/USF\_ISDS.medical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HymanF12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploiting SNOMED CT Concepts & Relationships for Clinical  Information Retrieval: Australian e-Health Research Centre and Queensland  University of Technology at the TREC 2012 Medical Track

_Bevan Koopman, Guido Zuccon, Anthony N. Nguyen, Deanne Vickers, Luke Butt, Peter Bruza_

- :fontawesome-solid-user-group: **Participant:** [AEHRC](./participants.md#aehrc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/AEHRC.medical.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/AEHRC.medical.nb.pdf)
- :material-file-search: **Runs:** [AEHRClvl0](./runs.md#aehrclvl0) | [AEHRClvl1](./runs.md#aehrclvl1) | [AEHRClvl2](./runs.md#aehrclvl2) | [AEHRCsub](./runs.md#aehrcsub)

??? abstract "Abstract"
	
	The Australian e-Health Research Centre and Queensland University of Technology recently participated in the TREC 2012 Medical Records Track. This paper reports on our methods, results and experience using an approach that exploits the concept and inter-concept relationships defined in the SNOMED CT medical ontology. Our concept-based approach is intended to overcome specific challenges in searching medical records, namely vocabulary mismatch and granularity mismatch. Queries and documents are transformed from their term-based originals into medical concepts as defined by the SNOMED CT ontology, this is done to tackle vocabulary mismatch. In addition, we make use of the SNOMED CT parent-child 'is-a' relationships between concepts to weight documents that contained concept subsumed by the query concepts; this is done to tackle the problem of granularity mismatch. Finally, we experiment with other SNOMED CT relationships besides the is-a relationship to weight concepts related to query concepts. Results show our concept-based approach performed significantly above the median in all four performance metrics. Further improvements are achieved by the incorporation of weighting subsumed concepts, overall leading to improvement above the median of 28% infAP, 10% infNDCG, 12% R-prec and 7% Prec@10. The incorporation of other relations besides is-a demonstrated mixed results, more research is required to determined which SNOMED CT relationships are best employed when weighting related concepts.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KoopmanZNVBB12.bib) "
	```
	@inproceedings{DBLP:conf/trec/KoopmanZNVBB12,
		author = {Bevan Koopman and Guido Zuccon and Anthony N. Nguyen and Deanne Vickers and Luke Butt and Peter Bruza},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploiting {SNOMED} {CT} Concepts {\&} Relationships for Clinical Information Retrieval: Australian e-Health Research Centre and Queensland University of Technology at the {TREC} 2012 Medical Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/AEHRC.medical.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KoopmanZNVBB12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DCU@TRECMed 2012: Using adhoc Baselines for Domain-Specific Retrieval

_Johannes Leveling, Lorraine Goeuriot, Liadh Kelly, Gareth J. F. Jones_

- :fontawesome-solid-user-group: **Participant:** [DCU](./participants.md#dcu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/DCU.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/DCU.medical.final.pdf)
- :material-file-search: **Runs:** [DCU21](./runs.md#dcu21) | [DCU22](./runs.md#dcu22) | [DCU23b](./runs.md#dcu23b) | [DCU24b](./runs.md#dcu24b)

??? abstract "Abstract"
	
	This paper describes the first participation of DCU in the TREC Medical Records Track (TRECMed) 2012. We performed initial experiments on the the 2011 TRECMed data based on the BM25 retrieval model. Surprisingly, we found that the standard BM25 model with default parameters performs comparable to the best automatic runs submitted to TRECMed 2011 and our experiments would have ranked among the top four out of 29 participating groups. We expected that some form of domain adaptation would increase performance. However, results on the 2011 data proved otherwise: query expansion decreased performance, and filtering and reranking by term proximity also de- creased performance slightly. We submitted four runs based on the BM25 retrieval model to TRECMed 2012 using standard BM25, standard query expansion, result filtering, and concept-based query expansion. Official results for 2012 confirm that domain-specific knowledge, as applied by us, does not increase performance compared to the BM25 baseline.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LevelingGKJ12.bib) "
	```
	@inproceedings{DBLP:conf/trec/LevelingGKJ12,
		author = {Johannes Leveling and Lorraine Goeuriot and Liadh Kelly and Gareth J. F. Jones},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {DCU@TRECMed 2012: Using adhoc Baselines for Domain-Specific Retrieval},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/DCU.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LevelingGKJ12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NICTA and UBC at the TREC 2012 Medical Track

_David Martínez, Arantxa Otegi, Eneko Agirre_

- :fontawesome-solid-user-group: **Participant:** [NICTA](./participants.md#nicta)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/NICTA.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/NICTA.medical.final.pdf)
- :material-file-search: **Runs:** [NICTAUBC1](./runs.md#nictaubc1) | [NICTAUBC2](./runs.md#nictaubc2) | [NICTAUBC4](./runs.md#nictaubc4) | [NICTAUBC6](./runs.md#nictaubc6)

??? abstract "Abstract"
	
	We introduce two heterogeneous query expansion techniques, and a combined system to the TREC 2012 Medical Track. Our methods are based on external resources that provide expansion concepts related to the query terms, by means of the PageRank algorithm, and simple rules based on UMLS Semantic Types. In this paper we show that our systems are able to reach competitive performances at both the TREC-2011 and TREC-2012 tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MartinezOA12.bib) "
	```
	@inproceedings{DBLP:conf/trec/MartinezOA12,
		author = {David Mart{\'{\i}}nez and Arantxa Otegi and Eneko Agirre},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{NICTA} and {UBC} at the {TREC} 2012 Medical Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/NICTA.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MartinezOA12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Siena College Medical Information Retrieval System (MIRS)

_Larry R. Medsker, Sharon G. Small_

- :fontawesome-solid-user-group: **Participant:** [SCIAITeam](./participants.md#sciaiteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/SCIAITeam.medical.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/SCIAITeam.medical.nb.pdf)
- :material-file-search: **Runs:** [Siena1](./runs.md#siena1) | [Siena2](./runs.md#siena2) | [Siena3](./runs.md#siena3)

??? abstract "Abstract"
	
	The work done by our MIRS team of three students and two faculty mentors resulted in a baseline system for content-based medical record retrieval. We also made significant progress on an alternative system based on neural computing concepts. The task for the Medical Records TREC in 2012 was to process a list of thirty-four randomly selected queries against a large medical records database to simulate searches for patients who meet the criteria for participating in various clinical trials. The task was to analyze a data set of over 100,000 reports associated with hospital visits and identify patients whose situations were relevant to the queries. Our text retrieval process was done in two separate ways: one used an index created from standard Information Retrieval (IR) software called Lucene and an alternate method based on principles of neural computing. We submitted three runs to the TREC competition, two using our standard Lucene-based approach and one that used elements of neural network analysis. The MIRS team was provided the code necessary to download the Medical Records corpus, consisting of an average of 15 reports from each of approximately 100K patient visits to a hospital. Teams were also provided a training set of 34 sample topic statements from TREC 2011. The records, which comprised one month of reports from multiple hospitals, came from the University of Pittsburgh NLP Repository and were de-identified in regard to specific patient names. The Medical Record track organizers from TREC also provided year 2011 judgment sets, produced by medical professionals at the Oregon Health Science University, that we then used in testing our MIRS software at different states of development. For each topic the system was required to search the medical records data corpus and return a ranked list of the top 10 relevant hospital visits, which were proxies for specific patients whose personal identification was made anonymous by the TREC organizers. It is not yet clear how traditional IR should perform on the identification of patients suitable for the clinical trials. Our first logical step was to run an experiment using traditional simple keyword informational retrieval. We used the open source IR system Lucene to index the NIST-supplied Medical Records corpus and to run our baseline experiments. This Lucene version became the first version of our MIRS system and these results were used as our baseline. Modules were proposed and implemented to improve the keyword identification. Then, the first round of experimentation was run with full error analysis. Modules were modified based on this error analysis, run again on the training collection and finally run on the test collection. Results were submitted to NIST before the deadline of August 11, 2012.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MedskerS12.bib) "
	```
	@inproceedings{DBLP:conf/trec/MedskerS12,
		author = {Larry R. Medsker and Sharon G. Small},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Siena College Medical Information Retrieval System {(MIRS)}},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/SCIAITeam.medical.nb.pdf},
		timestamp = {Thu, 09 Sep 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MedskerS12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2012: Medical Records Track

_Jun Miao, Zheng Ye, Jimmy X. Huang_

- :fontawesome-solid-user-group: **Participant:** [york](./participants.md#york)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/york.medical.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/york.medical.nb.pdf)
- :material-file-search: **Runs:** [YorkUMB1](./runs.md#yorkumb1) | [YorkUMC2](./runs.md#yorkumc2) | [YorkUMQ3](./runs.md#yorkumq3) | [YorkUMP4](./runs.md#yorkump4)

??? abstract "Abstract"
	
	In this paper, we present our participation in the Medical Records Track of TREC 2012. This is the second time we take part in this track. 50 new topics have been published in this year. The goal of this track is still to find relevant patients that have particular diseases and/or treatments. To achieve this goal, we try four methods which include popular techniques like query expansion, concept recognition and so on. Four runs have been submitted and they are based on our previous work. Detailed discussion has been made to show the effectiveness of different techniques on the Medical Records dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MiaoYH12.bib) "
	```
	@inproceedings{DBLP:conf/trec/MiaoYH12,
		author = {Jun Miao and Zheng Ye and Jimmy X. Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2012: Medical Records Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/york.medical.nb.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MiaoYH12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploiting Domain Thesaurus for Medical Record Retrieval

_Miguel A. Callejas P., Yue Wang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/udel_fang.medical.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/udel_fang.medical.nb.pdf)
- :material-file-search: **Runs:** [UDInfoMed123](./runs.md#udinfomed123) | [UDInfoMed12](./runs.md#udinfomed12) | [UDInfoMed1](./runs.md#udinfomed1)

??? abstract "Abstract"
	
	InfoLab at the University of Delaware participated in the TREC 2012 Medical Records Track. This paper explains our method and describes experiment results. One limitation of existing keyword matching based retrieval functions is the problem of vocabulary mismatch. To overcome this limitation, we propose to first map topics and visits to bags of concepts using domain thesaurus, and then model the relevance based on the similarities between those concepts.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PWF12.bib) "
	```
	@inproceedings{DBLP:conf/trec/PWF12,
		author = {Miguel A. Callejas P. and Yue Wang and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploiting Domain Thesaurus for Medical Record Retrieval},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/udel\_fang.medical.nb.pdf},
		timestamp = {Thu, 17 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/PWF12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Retrieving Medical Records with "sennamed": NEC Labs America at  TREC 2012 Medical Record Track

_Yanjun Qi, Pierre-François Laquerre_

- :fontawesome-solid-user-group: **Participant:** [sennamed](./participants.md#sennamed)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/sennamed.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/sennamed.medical.final.pdf)
- :material-file-search: **Runs:** [sennamedlsi](./runs.md#sennamedlsi) | [sennamed1](./runs.md#sennamed1) | [sennamed2](./runs.md#sennamed2) | [sennamed3](./runs.md#sennamed3)

??? abstract "Abstract"
	
	In this notebook, we describe the automatic retrieval runs from NEC Laboratories America (NECLA) for the Text REtrieval Conference (TREC) 2012 Medical Records track. Our approach is based on a combination of UMLS medical concept detection and a set of simple retrieval models. Our best run, sennamed2, has achieved the best inferred average precision (infAP) score on 5 of the 47 test topics, and obtained a higher score than the median of all submission runs on 27 other topics. Overall, sennamed2 ranks at the second place amongst all the 82 automatic runs submitted for this track, and obtains the third place amongst both automatic and manual submissions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QiL12.bib) "
	```
	@inproceedings{DBLP:conf/trec/QiL12,
		author = {Yanjun Qi and Pierre{-}Fran{\c{c}}ois Laquerre},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Retrieving Medical Records with "sennamed": {NEC} Labs America at {TREC} 2012 Medical Record Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/sennamed.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QiL12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Ensemble Approach for Expanding Queries

_Duy Duc An Bui, Doug Redd, Thomas C. Rindflesch, Qing Zeng-Treitler_

- :fontawesome-solid-user-group: **Participant:** [BMIUOU](./participants.md#bmiuou)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/BMIUOU.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/BMIUOU.medical.final.pdf)
- :material-file-search: **Runs:** [BMIUOUsyn](./runs.md#bmiuousyn) | [BMIUOUbase](./runs.md#bmiuoubase) | [BMIUOUens](./runs.md#bmiuouens) | [BMIUOUensneg](./runs.md#bmiuouensneg)

??? abstract "Abstract"
	
	In our TREC participation, we used an ensemble approach in query expansion. Query expansion, such as synonym expansion, had shown promising results in medical literature search. On the other hand, some of the 2011 papers reported worse results from expansion. Since there are multiple knowledge sources available and each resource has clear strengths and weaknesses, we tested the combination of three expansion methods versus each individual method. We found that the ensemble approach performed better (in terms of average infAP, infNDCG, R-prec, and P10) than the individual methods and better than the Lucene baseline. The individual expansion methods, however, did not improve the baseline Lucene performance. We also performed an unofficial run using a concept index to boost the query performance, which led to small improvements in infAP, infNDCG, and R-prec.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ReddZBRR12.bib) "
	```
	@inproceedings{DBLP:conf/trec/ReddZBRR12,
		author = {Duy Duc An Bui and Doug Redd and Thomas C. Rindflesch and Qing Zeng{-}Treitler},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {An Ensemble Approach for Expanding Queries},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/BMIUOU.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ReddZBRR12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Atigeo at TREC 2012 Medical Records Track: ICD-9 Code Description  Injection to Enhance Electronic Medical Record Search Accuracy

_Bryan Tinsley, Alex Thomas, Joseph F. McCarthy, Mike Lazarus_

- :fontawesome-solid-user-group: **Participant:** [xMusketeers](./participants.md#xmusketeers)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/atigeo.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/atigeo.medical.final.pdf)
- :material-file-search: **Runs:** [atigeo0](./runs.md#atigeo0) | [atigeo1](./runs.md#atigeo1) | [atigeo2](./runs.md#atigeo2) | [atigeo3](./runs.md#atigeo3)

??? abstract "Abstract"
	
	The TREC 2012 Medical Records Track task involves the identification of electronic medical records (EMRs) that are relevant to a set of search topics. Atigeo has a Computer-Aided Coding (CAC) product that analyzes electronic medical records (EMRs) and recommends ICD-9 codes that represent the diagnoses and procedures described in those medical records. We have developed a suite of natural language processing (NLP) components that are useful for both tasks. Our TREC 2012 experiments focused on the ICD-9 admission and diagnosis codes included in more than 90% of the TREC EMRs: we used our comprehensive ICD-9 database to insert one of three variants of the text descriptions associated with each code found in each EMR. We describe the variations of ICD-9 code descriptions we inserted, the NLP components used for processing all the reports and topics, and report on the results of our experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TinsleyTML12.bib) "
	```
	@inproceedings{DBLP:conf/trec/TinsleyTML12,
		author = {Bryan Tinsley and Alex Thomas and Joseph F. McCarthy and Mike Lazarus},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Atigeo at {TREC} 2012 Medical Records Track: {ICD-9} Code Description Injection to Enhance Electronic Medical Record Search Accuracy},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/atigeo.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TinsleyTML12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Three Questions About Clinical Information Retrieval

_Stephen T. Wu, James J. Masanz, K. E. Ravikumar, Hongfang Liu_

- :fontawesome-solid-user-group: **Participant:** [MayoClinicNLP](./participants.md#mayoclinicnlp)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/MayoClinicNLP.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/MayoClinicNLP.medical.final.pdf)
- :material-file-search: **Runs:** [MayoLucene](./runs.md#mayolucene) | [MayoMetaData](./runs.md#mayometadata) | [MayoPayload](./runs.md#mayopayload) | [MayoExpanded](./runs.md#mayoexpanded)

??? abstract "Abstract"
	
	Electronic Medical Records (EMRs) have greatly expanded the potential for the evidence-based improvement of clinical practice by providing a data source for computable medical information. The Text REtrieval Conference 2012 Medical Records Track (TREC-med) explored how information retrieval may support clinical research by providing an efficient means to identify cohorts for clinical studies. A shared task called participants to find cohorts of relevant patients for 50 different topic queries. The users in TREC-med information retrieval systems would be medical experts who are searching for cohorts. In our previous work, we have collaborated with such experts on specific queries; the assortment of 50 queries makes this competition a standardized benchmark task. Thus, techniques that have shown case-by-case improvement can be tested against a much larger number of queries. We have taken this opportunity to investigate three core questions around which many of our algorithms are designed: 1. What is the relative value of structured data (e.g., fields in EMRs, or document metadata) compared to clinical text? 2. Are extensive information extraction (IE) efforts any benefit when we consider the applied question of information retrieval (IR)? 3. Can distributional semantics help supply missing information in a query? For each of these three questions, we have extended Apache Lucene1 with pre-existing techniques and tested on the TREC-med cohort identification task. In testing these independently, we aim to find generalizable principles for cohort identification in other documents collections and queries. The rest of this paper describes the TREC 2012 Medical Records task, describes Mayo Clinic's run submissions in detail, and reports evaluation results with subsequent discussion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuMRL12.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuMRL12,
		author = {Stephen T. Wu and James J. Masanz and K. E. Ravikumar and Hongfang Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Three Questions About Clinical Information Retrieval},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/MayoClinicNLP.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuMRL12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at 2012 TREC Medical Track: Query Expansion, Retrieval and  Ranking

_Jiayue Zhang, Lin Lin, Shudang Diao, Yukun Li, Runnan Liu, Weiran Xu, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/PRIS.medical.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/PRIS.medical.nb.pdf)
- :material-file-search: **Runs:** [buptprisBase](./runs.md#buptprisbase) | [buptprisInt](./runs.md#buptprisint) | [buptprisCscr](./runs.md#buptpriscscr) | [buptprisLrnk](./runs.md#buptprislrnk)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangLDLLXG12.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangLDLLXG12,
		author = {Jiayue Zhang and Lin Lin and Shudang Diao and Yukun Li and Runnan Liu and Weiran Xu and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at 2012 {TREC} Medical Track: Query Expansion, Retrieval and Ranking},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/PRIS.medical.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangLDLLXG12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploring Evidence Aggregation Methods and External Expansion Sources  for Medical Record Search

_Dongqing Zhu, Ben Carterette_

- :fontawesome-solid-user-group: **Participant:** [udel](./participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/udel.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/udel.medical.final.pdf)
- :material-file-search: **Runs:** [udelMNZ](./runs.md#udelmnz) | [udelSUM](./runs.md#udelsum) | [udelMRF](./runs.md#udelmrf) | [udelMED](./runs.md#udelmed)

??? abstract "Abstract"
	
	This paper describes and analyzes experiments we performed for the Medical Records track in the 2012 Text REtrieval Conference (TREC). We mainly investigated three research problems: 1. Evidence Aggregation: In last year's track there were two different methods in general for obtaining a visit ranking out of reports (smaller document units), i.e., (A) using reports as indexing and retrieval units and then converting a report ranking into a visit ranking, and (B) using visits as indexing and retrieval units by concatenating reports at the very first stage and then obtain a visit ranking directly. Method A avoids the potential problem of varying visit document length, while Method B naturally aggregates evidence scatter over multiple reports and easily obtains a visit ranking. It is unclear which method is better based on all reported results. Thus, we compared the two approaches, tried various score aggregation methods for (A), and combined both approaches in a way that further improved the system performance. 2. Expansion Sources: We tested a variety of external collections (ranging from general web datasets to domain-specific thesauri, and from Megabyte datasets to Terabyte datasets) for query expansion, compared their effectiveness, and obtained useful insights into the data. 3. Retrieval Models: We tested several statistical IR models (proven to be effective on news and web collections) on this medical collection, and explored ways to combine these models to address different aspects of task. For instance, we used MRF model to model term proximity since most medical concepts are phrases. We also used a mixture of relevance models to obtain various relevant expansion terms covered by different expansion collections respectively, which is expect to significantly alleviate the vocabulary mismatch between medical terminologies. For TREC submissions, we tested systems that combined multiple IR models, leveraged diverse expansion sources, and used various evidence aggregation methods. We implemented all the retrieval models in the Indri1 retrieval system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhuC12.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhuC12,
		author = {Dongqing Zhu and Ben Carterette},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploring Evidence Aggregation Methods and External Expansion Sources for Medical Record Search},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/udel.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhuC12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2012: Experiments with Terrier in  Medical Records, Microblog, and Web Tracks

_Nut Limsopatham, Richard McCreadie, M-Dyaa Albakour, Craig Macdonald, Rodrygo L. T. Santos, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/uogTr.medical.microblog.web.final.pdf](http://trec.nist.gov/pubs/trec21/papers/uogTr.medical.microblog.web.final.pdf)
- :material-file-search: **Runs:** [uogTrMConQ](./runs.md#uogtrmconq) | [uogTrMConQRa](./runs.md#uogtrmconqra) | [uogTrMConQRd](./runs.md#uogtrmconqrd) | [uogTrMConQT](./runs.md#uogtrmconqt)

??? abstract "Abstract"
	
	In TREC 2012, we focus on tackling the new challenges posed by the Medical, Microblog and Web tracks, using our Terrier Information Retrieval Platform. In particular, for the Medical track, we investigate how to exploit implicit knowledge within medical records, with the aim of better identifying those records from patients with specific medical conditions. For the Microblog track adhoc task, we investigate novel techniques to leverage documents hyperlinked from tweets to better estimate relevance of those tweets and increase recall. Meanwhile, for the Microblog track filtering task, we developed a new stream processing infrastructure for real-time adaptive filtering on top of the Storm framework. For the TREC Web track, we continue to build upon our learning-to-rank approaches and novel xQuAD framework within Terrier, increasing both effectiveness and efficiency when ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LimsopathamMAMS12.bib) "
	```
	@inproceedings{DBLP:conf/trec/LimsopathamMAMS12,
		author = {Nut Limsopatham and Richard McCreadie and M{-}Dyaa Albakour and Craig Macdonald and Rodrygo L. T. Santos and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2012: Experiments with Terrier in Medical Records, Microblog, and Web Tracks},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/uogTr.medical.microblog.web.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LimsopathamMAMS12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

