# Proceedings - Cross-Language 2001 

#### The TREC-2001 Cross-Language Information Retrieval Track: Searching  Arabic Using English, French or Arabic Queries

_Fredric C. Gey, Douglas W. Oard_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/clirtrack.pdf](http://trec.nist.gov/pubs/trec10/papers/clirtrack.pdf)
??? abstract "Abstract"
	
	Ten groups participated in the TREC-2001 cross-language information retrieval track, which focussed on retrieving Arabic language documents based on 25 queries that were originally prepared in English. French and Arabic translations of the queries were also available. This was the first year in which a large Arabic test collection was available, so a variety of approaches were tried and a rich set of experiments performed using resources such as machine translation, parallel corpora, several approaches to stemming and/or morphology, and both pre-translation and post-translation blind relevance feedback. On average, forty percent of the relevant documents discovered by a participating team were found by no other team, a higher rate than normally observed at TREC. This raises some concern that the relevance judgment pools may be less complete than has historically been the case.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GeyO01.bib) "
	```
	@inproceedings{DBLP:conf/trec/GeyO01,
		author = {Fredric C. Gey and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC-2001} Cross-Language Information Retrieval Track: Searching Arabic Using English, French or Arabic Queries},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/clirtrack.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GeyO01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2001 Cross-lingual Retrieval at BBN

_Jinxi Xu, Alexander M. Fraser, Ralph M. Weischedel_

- :fontawesome-solid-user-group: **Participant:** [BBN](./participants.md#bbn)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/BBNTREC2001.pdf](http://trec.nist.gov/pubs/trec10/papers/BBNTREC2001.pdf)
- :material-file-search: **Runs:** [BBN10XLA](./runs.md#bbn10xla) | [BBN10XLB](./runs.md#bbn10xlb) | [BBN10XLC](./runs.md#bbn10xlc) | [BBN10XLD](./runs.md#bbn10xld) | [BBN10MON](./runs.md#bbn10mon)

??? abstract "Abstract"
	
	BBN only participated in the cross-lingual track in TREC 2001. Arabic, the language of the TREC 2001 corpus, presents a number of challenges to both monolingual and cross-lingual IR. First, many inflected Arabic words can correspond to multiple uninflected words, requiring context to disambiguate them. Second, orthographic variations are prevalent; certain glyphs are sometimes written as different, but similar looking glyphs. Third, broken plurals, analogous to irregular nouns in English, are very common. Such nouns cannot be easily reduced to their singular forms using a rule-based approach. Fourth, Arabic words are highly ambiguous due to the tri-literal root system and the omission of short vowels in written Arabic. The focus of this report is to explore the impact of these issues on Arabic monolingual and cross-lingual retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuFW01.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuFW01,
		author = {Jinxi Xu and Alexander M. Fraser and Ralph M. Weischedel},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC} 2001 Cross-lingual Retrieval at {BBN}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/BBNTREC2001.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuFW01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Hummingbird SearchServer at TREC 2001

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird](./participants.md#hummingbird)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/HumTREC2001.pdf](http://trec.nist.gov/pubs/trec10/papers/HumTREC2001.pdf)
- :material-file-search: **Runs:** [humAR01t](./runs.md#humar01t) | [humAR01tdn](./runs.md#humar01tdn) | [humAR01tdm](./runs.md#humar01tdm) | [humAR01tdx](./runs.md#humar01tdx) | [humAR01td](./runs.md#humar01td)

??? abstract "Abstract"
	
	Hummingbird submitted ranked result sets for the topic relevance task of the TREC 2001 Web Track (10GB of web data) and for the monolingual Arabic task of the TREC 2001 Cross-Language Track (869MB of Arabic news data). SearchServer's Intuitive Searching tied or exceeded the median Precision@10 score in 46 of the 50 web queries. For the web queries, enabling SearchServer's document length normalization increased Precision@10 by 65% and average precision by 55%. SearchServer's option to square the importance of inverse document frequency (V2:4 vs. V2:3) increased Precision@10 by 8% and average precision by 12%. SearchServer’s stemming increased Precision@10 by 5% and average precision by 13%. For the Arabic queries, a combination of experimental Arabic morphological normalizations, Arabic stop words and pseudo-relevance feedback increased average precision by 53% and Precision@10 by 9%.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson01,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Hummingbird SearchServer at {TREC} 2001},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/HumTREC2001.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Keep It Simple Sheffield - A KISS Approach to the Arabic Track

_Mark Sanderson, Asaad Alberair_

- :fontawesome-solid-user-group: **Participant:** [sheffield](./participants.md#sheffield)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/sheffield_arabic.pdf](http://trec.nist.gov/pubs/trec10/papers/sheffield_arabic.pdf)
- :material-file-search: **Runs:** [shefea](./runs.md#shefea) | [shefeaa](./runs.md#shefeaa) | [sheffea](./runs.md#sheffea) | [sheffeaa](./runs.md#sheffeaa) | [shefma](./runs.md#shefma)

??? abstract "Abstract"
	
	Sheffield’s participation in the inaugural Arabic cross language track is described here. Our goal was to examine how well one could achieve retrieval of Arabic text with the minimum of resources and adaptation of existing retrieval systems. To this end the public translators used for query translation and the minimal changes to our retrieval system are described. While the effectiveness of our resulting system is not as high as one might desire, it nevertheless provides reasonable performance particularly in the monolingual track: on average, just under four relevant documents were found in the 10 top ranked documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SandersonA01.bib) "
	```
	@inproceedings{DBLP:conf/trec/SandersonA01,
		author = {Mark Sanderson and Asaad Alberair},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Keep It Simple Sheffield - {A} {KISS} Approach to the Arabic Track},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/sheffield\_arabic.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SandersonA01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JHU/APL at TREC 2001: Experiments in Filtering and in Arabic,  Video, and Web Retrieval

_James Mayfield, Paul McNamee, Cash Costello, Christine D. Piatko, Amit Banerjee_

- :fontawesome-solid-user-group: **Participant:** [apl-jhu](./participants.md#apl-jhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/jhuapl01.pdf](http://trec.nist.gov/pubs/trec10/papers/jhuapl01.pdf)
- :material-file-search: **Runs:** [apl10ca1](./runs.md#apl10ca1) | [apl10ce1](./runs.md#apl10ce1) | [apl10ce2](./runs.md#apl10ce2) | [apl10cf1](./runs.md#apl10cf1) | [apl10ce3](./runs.md#apl10ce3)

??? abstract "Abstract"
	
	The outsider might wonder whether, in its tenth year, the Text Retrieval Conference would be a moribund workshop encouraging little innovation and undertaking few new challenges, or whether fresh research problems would continue to be addressed. We feel strongly that it is the later that is true; our group at the Johns Hopkins University Applied Physics Laboratory (JHU/APL) participated in four tracks at this year’s conference, three of which presented us with new and interesting problems. For the first time we participated in the filtering track, and we submitted official results for both the batch and routing subtasks. This year, a first attempt was made to hold a content-based video retrieval track at TREC, and we developed a new suite of tools for image analysis and multimedia retrieval. Finally, though not a stranger to cross-language text retrieval, we made a first attempt at Arabic language retrieval while emphasizing a language-neutral approach that has worked well in other languages. Thus, our team found several challenges to face this year, and this paper mainly reports our initial findings. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MayfieldMCPB01.bib) "
	```
	@inproceedings{DBLP:conf/trec/MayfieldMCPB01,
		author = {James Mayfield and Paul McNamee and Cash Costello and Christine D. Piatko and Amit Banerjee},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{JHU/APL} at {TREC} 2001: Experiments in Filtering and in Arabic, Video, and Web Retrieval},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/jhuapl01.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MayfieldMCPB01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Arabic Information Retrieval at UMass in TREC-10

_Leah S. Larkey, Margaret E. Connell_

- :fontawesome-solid-user-group: **Participant:** [umass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/UMass_TREC10_Final.pdf](http://trec.nist.gov/pubs/trec10/papers/UMass_TREC10_Final.pdf)
- :material-file-search: **Runs:** [UMass1](./runs.md#umass1) | [UMass2](./runs.md#umass2) | [UMass3](./runs.md#umass3) | [UMass4](./runs.md#umass4)

??? abstract "Abstract"
	
	The University of Massachusetts took on the TREC10 cross-language track with no prior experience with Arabic, and no Arabic speakers among any of our researchers or students. We intended to implement some standard approaches, and to extend a language modeling approach to handle co-occurrences. Given the lack of resources – training data, electronic bilingual dictionaries, and stemmers, and our unfamiliarity with Arabic, we had our hands full carrying out some standard approaches to monolingual and cross-language Arabic retrieval, and did not submit any runs based on novel approaches. We submitted three monolingual runs and one cross-language run. We first describe the models, techniques, and resources we used, then we describe each run in detail. Our official runs performed moderately well, in the second tier (3rd or 4 th place). Since submitting these results, we have improved normalization and stemming, improved dictionary construction, expanded Arabic queries, improved estimation and smoothing in language models, and added combination of evidence, increasing performance by a substantial amount.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LarkeyC01.bib) "
	```
	@inproceedings{DBLP:conf/trec/LarkeyC01,
		author = {Leah S. Larkey and Margaret E. Connell},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Arabic Information Retrieval at UMass in {TREC-10}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/UMass\_TREC10\_Final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LarkeyC01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC2001 Question-Answer, Web and Cross Language Experiments using  PIRCS

_Kui-Lam Kwok, Laszlo Grunfeld, Norbert Dinstl, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/queenst2001.pdf](http://trec.nist.gov/pubs/trec10/papers/queenst2001.pdf)
- :material-file-search: **Runs:** [pir1XEtd](./runs.md#pir1xetd) | [pir1XEtdn](./runs.md#pir1xetdn) | [pir1XAtdn](./runs.md#pir1xatdn) | [pir1XAtd](./runs.md#pir1xatd)

??? abstract "Abstract"
	
	We applied our PIRCS system for the Question-Answer, ad-hoc Web retrieval using the 10-GB collection, and the English-Arabic cross language tracks. These are described in Sections 2,3,4 respectively. We also attempted to complete the adaptive filtering experiments with our upgraded programs but found that we did not have sufficient time to do so.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokGDC01.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokGDC01,
		author = {Kui{-}Lam Kwok and Laszlo Grunfeld and Norbert Dinstl and M. Chan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC2001} Question-Answer, Web and Cross Language Experiments using {PIRCS}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/queenst2001.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokGDC01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-10 Experiments at University of Maryland CLIR and Video

_Kareem Darwish, David S. Doermann, Ryan C. Jones, Douglas W. Oard, Mika Rautiainen_

- :fontawesome-solid-user-group: **Participant:** [UMaryland](./participants.md#umaryland)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/umdTREC2000.pdf](http://trec.nist.gov/pubs/trec10/papers/umdTREC2000.pdf)
- :material-file-search: **Runs:** [UMmanual](./runs.md#ummanual) | [UMmonoAuto](./runs.md#ummonoauto) | [UMclirAutoXP](./runs.md#umclirautoxp) | [UMclirAutoFL](./runs.md#umclirautofl) | [UMclirAutoTJ](./runs.md#umclirautotj)

??? abstract "Abstract"
	
	The University of Maryland Researchers participated in both the Arabic-English Cross Language Information Retrieval (CLIR) and Video tracks of TREC-10. In the CLIR track, our goal was to explore effective monolingual Arabic IR techniques and effective query translation from English to Arabic for cross language IR. For the monolingual part, the use of the different index terms including words, stems, roots, and character n-grams were explored. For the English-Arabic CLIR, the use of MT, wordlist based translation, and non-dictionary words transliteration was explored. In the video track, we participated in the shot boundary detection, and known item search with the primary goals being to evaluate existing technology for shot detection and a new approach to extending simple visual image queries to video sequences. We present a general overview of the approaches, summarize the results in discuss how the algorithms are being extended.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DarwishDJOR01.bib) "
	```
	@inproceedings{DBLP:conf/trec/DarwishDJOR01,
		author = {Kareem Darwish and David S. Doermann and Ryan C. Jones and Douglas W. Oard and Mika Rautiainen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-10} Experiments at University of Maryland {CLIR} and Video},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/umdTREC2000.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DarwishDJOR01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Translation Term Weighting and Combining Translation Resources in  Cross-Language Retrieval

_Aitao Chen, Fredric C. Gey_

- :fontawesome-solid-user-group: **Participant:** [berkeley-clir](./participants.md#berkeley-clir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/berkeley_trec10.pdf](http://trec.nist.gov/pubs/trec10/papers/berkeley_trec10.pdf)
- :material-file-search: **Runs:** [BKYAAA1](./runs.md#bkyaaa1) | [BKYEAA1](./runs.md#bkyeaa1) | [BKYEAA2](./runs.md#bkyeaa2) | [BKYEAA3](./runs.md#bkyeaa3) | [BKYEAA4](./runs.md#bkyeaa4)

??? abstract "Abstract"
	
	In TREC-10 the Berkeley group participated only in the English-Arabic cross-language retrieval (CLIR) track. One Arabic monolingual run and four English-Arabic cross-language runs were submitted. Our approach to the cross-language retrieval was to translate the English topics into Arabic using online English-Arabic bilingual dictionaries and machine translation software. The five official runs are named as BKYAAA1, BKYAA1, BYEA2, BKYAA3, and BKYEAA4. The BKYAAA1 is the Arabic monolingual run, and the rest are English-to-Arabic cross-language runs. The same logistic regression based document ranking algorithm without pseudo relevance feedback was applied in all five runs. We refer the readers to the paper in [1] for details.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenG01.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenG01,
		author = {Aitao Chen and Fredric C. Gey},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Translation Term Weighting and Combining Translation Resources in Cross-Language Retrieval},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/berkeley\_trec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenG01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT at TREC-10

_Mohammed Aljlayl, Steven M. Beitzel, Eric C. Jensen, Abdur Chowdhury, David O. Holmes, M. Lee, David A. Grossman, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [IIT](./participants.md#iit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/IIT-TREC10.pdf](http://trec.nist.gov/pubs/trec10/papers/IIT-TREC10.pdf)
- :material-file-search: **Runs:** [iit01mlr](./runs.md#iit01mlr) | [iit01ml](./runs.md#iit01ml) | [iit01md](./runs.md#iit01md) | [iit01xma](./runs.md#iit01xma) | [iit01xdi](./runs.md#iit01xdi)

??? abstract "Abstract"
	
	For TREC-10, we participated in the adhoc and manual web tracks and in both the site-finding and cross-lingual tracks. For the adhoc track, we did extensive calibrations and learned that combining similarity measures yields little improvement. This year, we focused on a single high-performance similarity measure. For site finding, we implemented several algorithms that did well on the data provided for calibration, but poorly on the real dataset. For the cross-lingual track, we calibrated on the monolingual collection, and developed new Arabic stemming algorithms as well as a novel dictionary-based means of cross-lingual retrieval. Our results in this track were quite promising, with seventeen of our queries performing at or above the median.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AljlaylBJCHLGF01.bib) "
	```
	@inproceedings{DBLP:conf/trec/AljlaylBJCHLGF01,
		author = {Mohammed Aljlayl and Steven M. Beitzel and Eric C. Jensen and Abdur Chowdhury and David O. Holmes and M. Lee and David A. Grossman and Ophir Frieder},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{IIT} at {TREC-10}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/IIT-TREC10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AljlaylBJCHLGF01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

