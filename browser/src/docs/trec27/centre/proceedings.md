# Proceedings - CENTRE 2018 

#### The University of Padua IMS Research Group at CENTRE@TREC 2018

_Giorgio Maria Di Nunzio, Stefano Marchesin_

- :fontawesome-solid-user-group: **Participant:** [ims_unipd](./participants.md#ims_unipd)
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

- :fontawesome-solid-user-group: **Participant:** [Anserini](./participants.md#anserini)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/anserini-CTR-CC-N.pdf](https://trec.nist.gov/pubs/trec27/papers/anserini-CTR-CC-N.pdf)
- :material-file-search: **Runs:** [Anserini-UDInfolabWEB1-1](./runs.md#anserini-udinfolabweb1-1) | [Anserini-UDInfolabWEB1-2](./runs.md#anserini-udinfolabweb1-2) | [Anserini-UDInfolabWEB1-3](./runs.md#anserini-udinfolabweb1-3) | [Anserini-UDInfolabWEB2-1](./runs.md#anserini-udinfolabweb2-1) | [Anserini-UDInfolabWEB2-2](./runs.md#anserini-udinfolabweb2-2) | [Anserini-UDInfolabWEB2-3](./runs.md#anserini-udinfolabweb2-3)

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

