# Runs - Genomics 2004 

#### akoike 
[**`Results`**](./results.md#akoike), [**`Participants`**](./participants.md#utokyo), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.akoike.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.akoike.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.tokyo.adhoc.table.pdf) 

- :material-rename: **Name:** akoike 
- :fontawesome-solid-user-group: **Participant:** u.tokyo 
- :material-email: **Email:** yayamamo [at] ims [dot] u-tokyo [dot] ac [dot] jp 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/16/2004 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Strong heuristic 

---
#### akoyama 
[**`Results`**](./results.md#akoyama), [**`Participants`**](./participants.md#utokyo), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.akoyama.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.akoyama.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.tokyo.adhoc.table.pdf) 

- :material-rename: **Name:** akoyama 
- :fontawesome-solid-user-group: **Participant:** u.tokyo 
- :material-email: **Email:** yayamamo [at] ims [dot] u-tokyo [dot] ac [dot] jp 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/16/2004 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Initial result screening 

---
#### aliasiBase 
[**`Results`**](./results.md#aliasibase), [**`Participants`**](./participants.md#alias-i), [**`Proceedings`**](./proceedings.md#phrasal-queries-with-lingpipe-and-lucene-ad-hoc-genomics-text-retrieval), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.aliasiBase.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.aliasiBase.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/alias-i.adhoc.table.pdf) 

- :material-rename: **Name:** aliasiBase 
- :fontawesome-solid-user-group: **Participant:** alias-i 
- :material-email: **Email:** carp [at] aliasi [dot] com 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/7/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** SYSTEM  Jakarta Lucene 1.3 (jakarta.apache.org/lucene) LINGUISTICS  Alias-i LingPipe (www.aliasi.com/lingpipe) INDEXING  Tokenized with LingPipe IndoEuropeanTokenizer, lowercased, without a stop list.  Combined document text into single field with boosts  4*title, 1*abstract, 2*ordinary MESH, 4*starred MESH, 1*chemical names.  Took 5 hours, producing 9GB index, including storing original titles, abstracts, MESH terms and chemical names. SEARCH  Tokenized with LingPipe IndoEuropeanTokenizer, lowercased, removed stop terms.  Used fields with boosts  4*title, 2*need, 1*context.  Lucene's standard TF/IDF implementation  TF is square root of raw frequency; IDF is log(num docs/doc freq + 1) + 1; doc and query normalized to unit length.  Took 15 minutes per result set of 50 topics with 1000 results/topic.        

---
#### aliasiTerms 
[**`Results`**](./results.md#aliasiterms), [**`Participants`**](./participants.md#alias-i), [**`Proceedings`**](./proceedings.md#phrasal-queries-with-lingpipe-and-lucene-ad-hoc-genomics-text-retrieval), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.aliasiTerms.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.aliasiTerms.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/alias-i.adhoc.table.pdf) 

- :material-rename: **Name:** aliasiTerms 
- :fontawesome-solid-user-group: **Participant:** alias-i 
- :material-email: **Email:** carp [at] aliasi [dot] com 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/7/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** SYSTEM  Jakarta Lucene 1.3 (jakarta.apache.org/lucene) LINGUISTICS  Alias-i LingPipe (www.aliasi.com/lingpipe) INDEXING  Tokenized with LingPipe IndoEuropeanTokenizer, lowercased, without a stop list.  Combined document text into single field with boosts  4*title, 1*abstract, 2*ordinary MESH, 4*starred MESH, 1*chemical names.  Took 5 hours, producing 9GB index, including storing original titles, abstracts, MESH terms and chemical names. SEARCH  Tokenized with LingPipe IndoEuropeanTokenizer, lowercased, removed stop terms.  Used fields with boosts  4*title, 2*need, 1*context.  Lucene's standard TF/IDF implementation  TF is square root of raw frequency; IDF is log(num docs/doc freq + 1) + 1; doc and query normalized to unit length.  Took 15 minutes per result set of 50 topics with 1000 results/topic. TERMS  Added all terms recognized by LingPipe's GENIA-corpus trained Genomics named entity annotator as quoted search terms with a boost of 4 (multiplied by field boost).         

---
#### biotext1trge 
[**`Results`**](./results.md#biotext1trge), [**`Participants`**](./participants.md#ucberkeleyhearst), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.biotext1trge.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.biotext1trge.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.cberkeley.hearst.triage.table.pdf) 

- :material-rename: **Name:** biotext1trge 
- :fontawesome-solid-user-group: **Participant:** u.cberkeley.hearst 
- :material-email: **Email:** hearst [at] sims [dot] berkeley [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:**  Threshold change       

---
#### BIOTEXT21 
[**`Results`**](./results.md#biotext21), [**`Participants`**](./participants.md#ucberkeleyhearst), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.BIOTEXT21.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.BIOTEXT21.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.cberkeley.hearst.annhi.table.pdf) 

- :material-rename: **Name:** BIOTEXT21 
- :fontawesome-solid-user-group: **Participant:** u.cberkeley.hearst 
- :material-email: **Email:** nakov [at] cs [dot] berkeley [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** GO code extraction, MGI before 2003 

---
#### BIOTEXT22 
[**`Results`**](./results.md#biotext22), [**`Participants`**](./participants.md#ucberkeleyhearst), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.BIOTEXT22.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.BIOTEXT22.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.cberkeley.hearst.annhi.table.pdf) 

- :material-rename: **Name:** BIOTEXT22 
- :fontawesome-solid-user-group: **Participant:** u.cberkeley.hearst 
- :material-email: **Email:** nakov [at] cs [dot] berkeley [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** GO code extraction 

---
#### BIOTEXT23 
[**`Results`**](./results.md#biotext23), [**`Participants`**](./participants.md#ucberkeleyhearst), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.BIOTEXT23.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.BIOTEXT23.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.cberkeley.hearst.annhi.table.pdf) 

- :material-rename: **Name:** BIOTEXT23 
- :fontawesome-solid-user-group: **Participant:** u.cberkeley.hearst 
- :material-email: **Email:** nakov [at] cs [dot] berkeley [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** GO identification + classification (SVM) + human 

---
#### BIOTEXT24 
[**`Results`**](./results.md#biotext24), [**`Participants`**](./participants.md#ucberkeleyhearst), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.BIOTEXT24.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.BIOTEXT24.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.cberkeley.hearst.annhi.table.pdf) 

- :material-rename: **Name:** BIOTEXT24 
- :fontawesome-solid-user-group: **Participant:** u.cberkeley.hearst 
- :material-email: **Email:** nakov [at] cs [dot] berkeley [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** GO identification + classification (SVM) 

---
#### BIOTEXT25 
[**`Results`**](./results.md#biotext25), [**`Participants`**](./participants.md#ucberkeleyhearst), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.BIOTEXT25.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.BIOTEXT25.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.cberkeley.hearst.annhi.table.pdf) 

- :material-rename: **Name:** BIOTEXT25 
- :fontawesome-solid-user-group: **Participant:** u.cberkeley.hearst 
- :material-email: **Email:** nakov [at] cs [dot] berkeley [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** GO identification + classification (SVM); window of 50 

---
#### biotext2trge 
[**`Results`**](./results.md#biotext2trge), [**`Participants`**](./participants.md#ucberkeleyhearst), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.biotext2trge.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.biotext2trge.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.cberkeley.hearst.triage.table.pdf) 

- :material-rename: **Name:** biotext2trge 
- :fontawesome-solid-user-group: **Participant:** u.cberkeley.hearst 
- :material-email: **Email:** hearst [at] sims [dot] berkeley [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:**  Threshold change       

---
#### biotext3trge 
[**`Results`**](./results.md#biotext3trge), [**`Participants`**](./participants.md#ucberkeleyhearst), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.biotext3trge.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.biotext3trge.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.cberkeley.hearst.triage.table.pdf) 

- :material-rename: **Name:** biotext3trge 
- :fontawesome-solid-user-group: **Participant:** u.cberkeley.hearst 
- :material-email: **Email:** hearst [at] sims [dot] berkeley [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:**  Threshold change       

---
#### biotext4trge 
[**`Results`**](./results.md#biotext4trge), [**`Participants`**](./participants.md#ucberkeleyhearst), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.biotext4trge.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.biotext4trge.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.cberkeley.hearst.triage.table.pdf) 

- :material-rename: **Name:** biotext4trge 
- :fontawesome-solid-user-group: **Participant:** u.cberkeley.hearst 
- :material-email: **Email:** hearst [at] sims [dot] berkeley [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:**  Threshold change       

---
#### biotext5trge 
[**`Results`**](./results.md#biotext5trge), [**`Participants`**](./participants.md#ucberkeleyhearst), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.biotext5trge.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.biotext5trge.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.cberkeley.hearst.triage.table.pdf) 

- :material-rename: **Name:** biotext5trge 
- :fontawesome-solid-user-group: **Participant:** u.cberkeley.hearst 
- :material-email: **Email:** hearst [at] sims [dot] berkeley [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:**  Threshold change       

---
#### BioTextAdHoc 
[**`Results`**](./results.md#biotextadhoc), [**`Participants`**](./participants.md#ucberkeleyhearst), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.BioTextAdHoc.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.BioTextAdHoc.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.cberkeley.hearst.adhoc.table.pdf) 

- :material-rename: **Name:** BioTextAdHoc 
- :fontawesome-solid-user-group: **Participant:** u.cberkeley.hearst 
- :material-email: **Email:** sariel [at] cs [dot] berkeley [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/16/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Features include MeSH descriptors, gene mappings, and gene families.         

---
#### ConversAuto 
[**`Results`**](./results.md#conversauto), [**`Participants`**](./participants.md#converspeech), [**`Proceedings`**](./proceedings.md#concept-extraction-and-synonymy-management-for-biomedical-information-retrieval), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.ConversAuto.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.ConversAuto.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/converspeech.adhoc.table.pdf) 

- :material-rename: **Name:** ConversAuto 
- :fontawesome-solid-user-group: **Participant:** converspeech 
- :material-email: **Email:** xfb52 [at] dial [dot] pipex [dot] com 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/14/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Automatic  Query terms and filter terms are constructed from the topics using automated term extraction. Query terms are combined to form queries using a federated biomedical and English-language ontology. Filter terms  order and score the results of the searches, which are implemented using PubMed e-utilities.  

---
#### ConversManu 
[**`Results`**](./results.md#conversmanu), [**`Participants`**](./participants.md#converspeech), [**`Proceedings`**](./proceedings.md#concept-extraction-and-synonymy-management-for-biomedical-information-retrieval), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.ConversManu.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.ConversManu.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/converspeech.adhoc.table.pdf) 

- :material-rename: **Name:** ConversManu 
- :fontawesome-solid-user-group: **Participant:** converspeech 
- :material-email: **Email:** xfb52 [at] dial [dot] pipex [dot] com 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/14/2004 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Manual  Queries and filter terms generated automatically were modified in consultation with a biologist based on an understanding of the intended search for each topic. Three kinds of general modifications were made.  

---
#### csusm 
[**`Results`**](./results.md#csusm), [**`Participants`**](./participants.md#usanmarcos), [**`Proceedings`**](./proceedings.md#categorization-of-genomics-text-based-on-decision-rules), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.csusm.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.csusm.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.sanmarcos.adhoc.table.pdf) 

- :material-rename: **Name:** csusm 
- :fontawesome-solid-user-group: **Participant:** u.sanmarcos 
- :material-email: **Email:** rguillen [at] csusm [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Removed stop words from XML Medline files and topics file. Query constructed using title field, in some cases information from the need field. Word-based search, each term in the query is assigned an equivalent weight. If there is a match add term weight to totalweight. If totalweight is >= total# terms for query * .5 * weight then document is retrieved.  

---
#### cuhkrun1 
[**`Results`**](./results.md#cuhkrun1), [**`Participants`**](./participants.md#chineseuhongkong), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.cuhkrun1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.cuhkrun1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/chinese.u.hongkong.annhi.table.pdf) 

- :material-rename: **Name:** cuhkrun1 
- :fontawesome-solid-user-group: **Participant:** chinese.u.hongkong 
- :material-email: **Email:** kchan [at] se [dot] cuhk [dot] edu [dot] hk 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** SVM classification is used with term weighting scheme of tf-idf; and with cost ration automatically tuned. 

---
#### cuhkrun2 
[**`Results`**](./results.md#cuhkrun2), [**`Participants`**](./participants.md#chineseuhongkong), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.cuhkrun2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.cuhkrun2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/chinese.u.hongkong.annhi.table.pdf) 

- :material-rename: **Name:** cuhkrun2 
- :fontawesome-solid-user-group: **Participant:** chinese.u.hongkong 
- :material-email: **Email:** kchan [at] se [dot] cuhk [dot] edu [dot] hk 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Target gene identification is conducted which SVM classification is used with term weight considering distance between the term and target gene. Also, with cost ration automatically tuned. 

---
#### cuhkrun3 
[**`Results`**](./results.md#cuhkrun3), [**`Participants`**](./participants.md#chineseuhongkong), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.cuhkrun3.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.cuhkrun3.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/chinese.u.hongkong.annhi.table.pdf) 

- :material-rename: **Name:** cuhkrun3 
- :fontawesome-solid-user-group: **Participant:** chinese.u.hongkong 
- :material-email: **Email:** kchan [at] se [dot] cuhk [dot] edu [dot] hk 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Using SVM with term weighting tf-idf and with different set of features. Also, automatically tuning the cost ration. 

---
#### DCUma 
[**`Results`**](./results.md#dcuma), [**`Participants`**](./participants.md#dubblincityu), [**`Proceedings`**](./proceedings.md#experiments-in-terabyte-searching-genomic-retrieval-and-novelty-detection-for-trec-2004), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.DCUma.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.DCUma.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/dubblincity.u.adhoc.table.pdf) 

- :material-rename: **Name:** DCUma 
- :fontawesome-solid-user-group: **Participant:** dubblincity.u 
- :material-email: **Email:** fcamous [at] computing [dot] dcu [dot] ie 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** We built a MeSH term index and it is the only index used by our system for this run.  With the help of an expert, we manually build mesh queries from the topics. 

---
#### DCUmatn1 
[**`Results`**](./results.md#dcumatn1), [**`Participants`**](./participants.md#dubblincityu), [**`Proceedings`**](./proceedings.md#experiments-in-terabyte-searching-genomic-retrieval-and-novelty-detection-for-trec-2004), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.DCUmatn1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.DCUmatn1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/dubblincity.u.adhoc.table.pdf) 

- :material-rename: **Name:** DCUmatn1 
- :fontawesome-solid-user-group: **Participant:** dubblincity.u 
- :material-email: **Email:** fcamous [at] computing [dot] dcu [dot] ie 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:**  Two indices were built for this run, one with MeSH descriptors and one with title/abstract terms. We used the title and need fields to automatically generate abstract/title query and produced a ranking with the BM25 algorithm. We then queried the MeSH index using MeSH queries generated manually from the topics with the help of an expert and obtained a second ranking.  The two ranking were combined and only the top 1000 documents were retained for each topic.        

---
#### dimacsAabsw1 
[**`Results`**](./results.md#dimacsaabsw1), [**`Participants`**](./participants.md#rutgersdayanik), [**`Proceedings`**](./proceedings.md#dimacs-at-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.dimacsAabsw1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.dimacsAabsw1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/rutgers.dayanik.annhi.table.pdf) 

- :material-rename: **Name:** dimacsAabsw1 
- :fontawesome-solid-user-group: **Participant:** rutgers.dayanik 
- :material-email: **Email:** dfradkin [at] paul [dot] rutgers [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/27/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Title, subject and abstract of the article were used to represent document-gene pair. Text representation   stemmed, logtf-idf, cosine normalization. A classifier, Bayesian Binary Regression (BBR) with Gaussian prior, was trained separately for each domain. The test results across domains were then combined into one file. 

---
#### dimacsAg3mh 
[**`Results`**](./results.md#dimacsag3mh), [**`Participants`**](./participants.md#rutgersdayanik), [**`Proceedings`**](./proceedings.md#dimacs-at-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.dimacsAg3mh.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.dimacsAg3mh.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/rutgers.dayanik.annhi.table.pdf) 

- :material-rename: **Name:** dimacsAg3mh 
- :fontawesome-solid-user-group: **Participant:** rutgers.dayanik 
- :material-email: **Email:** aynur [at] cs [dot] rutgers [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/29/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** MeSH terms from MEDLINE abstracts were used to represent document-gene pairs. Each MeSH term was represented as a token. Text representation binary. A classifier, Bayesian Binary Regression (BBR) with Gaussian prior was trained separately for each domain.  The test results across domains were then combined into one file. 

---
#### dimacsAl3w 
[**`Results`**](./results.md#dimacsal3w), [**`Participants`**](./participants.md#rutgersdayanik), [**`Proceedings`**](./proceedings.md#dimacs-at-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.dimacsAl3w.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.dimacsAl3w.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/rutgers.dayanik.annhi.table.pdf) 

- :material-rename: **Name:** dimacsAl3w 
- :fontawesome-solid-user-group: **Participant:** rutgers.dayanik 
- :material-email: **Email:** aynur [at] cs [dot] rutgers [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/29/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Fulltext taken from journal articles' subject, title, abstract, and body fields were used to represent document-gene pairs.  Text representation  stemmed, logtf-idf and cosine normalization. A classifier, Bayesian Binary Regression (BBR) with Laplace prior was trained separately for each domain.  The test results across domains were then combined into one file. 

---
#### dimacsAp5w5 
[**`Results`**](./results.md#dimacsap5w5), [**`Participants`**](./participants.md#rutgersdayanik), [**`Proceedings`**](./proceedings.md#dimacs-at-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.dimacsAp5w5.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.dimacsAp5w5.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/rutgers.dayanik.annhi.table.pdf) 

- :material-rename: **Name:** dimacsAp5w5 
- :fontawesome-solid-user-group: **Participant:** rutgers.dayanik 
- :material-email: **Email:** dfradkin [at] paul [dot] rutgers [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/27/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Paragraphs containing gene symbol/description (taken from gtrain  and from LocusLink) were used to represent document-gene pair. Text representation  stemmed, logtf-idf, cosine normalization. Positive instances in the training were given weight 5. A classifier, Bayesian Binary Regression (BBR) with Gaussian prior, was trained separately for each domain. The test results across domains were then combined into one file. 

---
#### dimacsAw20w5 
[**`Results`**](./results.md#dimacsaw20w5), [**`Participants`**](./participants.md#rutgersdayanik), [**`Proceedings`**](./proceedings.md#dimacs-at-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.dimacsAw20w5.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.dimacsAw20w5.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/rutgers.dayanik.annhi.table.pdf) 

- :material-rename: **Name:** dimacsAw20w5 
- :fontawesome-solid-user-group: **Participant:** rutgers.dayanik 
- :material-email: **Email:** dfradkin [at] paul [dot] rutgers [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/27/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Join of windows of half-size 20 around gene symbol/description (taken from gtrain and from LocusLink) were used to represent document-gene pair. Text representation  stemmed, logtf-idf, cosine normalization. Positive instances in the training were given weight 5. A classifier, Bayesian Binary Regression (BBR) with Gaussian prior, was trained separately for each domain. The test results across domains were then combined into one file. 

---
#### dimacsTfl9d 
[**`Results`**](./results.md#dimacstfl9d), [**`Participants`**](./participants.md#rutgersdayanik), [**`Proceedings`**](./proceedings.md#dimacs-at-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.dimacsTfl9d.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.dimacsTfl9d.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/rutgers.dayanik.triage.table.pdf) 

- :material-rename: **Name:** dimacsTfl9d 
- :fontawesome-solid-user-group: **Participant:** rutgers.dayanik 
- :material-email: **Email:** aynur [at] cs [dot] rutgers [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/27/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Training and test set documents were prefiltered to obtain documents with MeSH term Mice. Prefiltered training set was used to construct a classifier.  Article title, abstract and MEDLINE MeSH terms were used for document representation. Text representation  stemmed, logtf-idf, cosine normalization.  A classifier, Bayesian Binary Regression (BBR) with Laplace prior, was trained, and used to make predictions with maximum expected effectiveness threshold tuning. 

---
#### dimacsTfl9w 
[**`Results`**](./results.md#dimacstfl9w), [**`Participants`**](./participants.md#rutgersdayanik), [**`Proceedings`**](./proceedings.md#dimacs-at-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.dimacsTfl9w.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.dimacsTfl9w.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/rutgers.dayanik.triage.table.pdf) 

- :material-rename: **Name:** dimacsTfl9w 
- :fontawesome-solid-user-group: **Participant:** rutgers.dayanik 
- :material-email: **Email:** aynur [at] cs [dot] rutgers [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/27/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Training and test set documents were prefiltered to obtain documents with MeSH term Mice. Prefiltered training set was used to construct a classifier.  Fulltext obtained from journal articles' title, abstract and body fields were used for document representation. Text representation  stemmed, logtf-idf, cosine normalization.  A classifier, Bayesian Binary Regression (BBR) with Laplace prior, was trained, and used to make predictions with maximum expected effectiveness threshold tuning. 

---
#### dimacsTl9md 
[**`Results`**](./results.md#dimacstl9md), [**`Participants`**](./participants.md#rutgersdayanik), [**`Proceedings`**](./proceedings.md#dimacs-at-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.dimacsTl9md.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.dimacsTl9md.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/rutgers.dayanik.triage.table.pdf) 

- :material-rename: **Name:** dimacsTl9md 
- :fontawesome-solid-user-group: **Participant:** rutgers.dayanik 
- :material-email: **Email:** aynur [at] cs [dot] rutgers [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/27/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Article title, abstract and MEDLINE MeSH terms were used for document representation. Text representation  stemmed, logtf-idf, cosine normalization.  A classifier, Bayesian Binary Regression (BBR) with Laplace prior, was trained and used to make predictions with maximum expected effectiveness threshold tuning. 

---
#### dimacsTl9mhg 
[**`Results`**](./results.md#dimacstl9mhg), [**`Participants`**](./participants.md#rutgersdayanik), [**`Proceedings`**](./proceedings.md#dimacs-at-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.dimacsTl9mhg.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.dimacsTl9mhg.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/rutgers.dayanik.triage.table.pdf) 

- :material-rename: **Name:** dimacsTl9mhg 
- :fontawesome-solid-user-group: **Participant:** rutgers.dayanik 
- :material-email: **Email:** aynur [at] cs [dot] rutgers [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/27/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** For each document, MeSH terms and GENBANK references were taken from the corresponding MEDLINE abstracts, and each MeSH term and organism from the corresponding GENBANK entry was represented as a token.  Text representation  binary. A classifier, Bayesian Binary Regression (BBR) with Laplace prior, was trained and used to make predictions with maximum expected effectiveness threshold tuning. 

---
#### dimacsTl9w 
[**`Results`**](./results.md#dimacstl9w), [**`Participants`**](./participants.md#rutgersdayanik), [**`Proceedings`**](./proceedings.md#dimacs-at-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.dimacsTl9w.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.dimacsTl9w.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/rutgers.dayanik.triage.table.pdf) 

- :material-rename: **Name:** dimacsTl9w 
- :fontawesome-solid-user-group: **Participant:** rutgers.dayanik 
- :material-email: **Email:** aynur [at] cs [dot] rutgers [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/27/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Fulltext obtained from journal articles' subject, title, abstract and body fields were used for document representation. Text representation  stemmed, logtf-idf, cosine normalization.  A classifier, Bayesian Binary Regression (BBR) with Laplace prior, was trained, and used to make predictions with maximum expected effectiveness threshold tuning. 

---
#### edinauto2 
[**`Results`**](./results.md#edinauto2), [**`Participants`**](./participants.md#uedinburghsinclair), [**`Proceedings`**](./proceedings.md#trec-genomics-2004), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.edinauto2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.edinauto2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.edinburgh.sinclair.adhoc.table.pdf) 

- :material-rename: **Name:** edinauto2 
- :fontawesome-solid-user-group: **Participant:** u.edinburgh.sinclair 
- :material-email: **Email:** csincla1 [at] inf [dot] ed [dot] ac [dot] uk 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:**         Lucene retrieval engine; queries weighted according to Web counts and expanded with noun phrases and synonyms 

---
#### edinauto5 
[**`Results`**](./results.md#edinauto5), [**`Participants`**](./participants.md#uedinburghsinclair), [**`Proceedings`**](./proceedings.md#trec-genomics-2004), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.edinauto5.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.edinauto5.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.edinburgh.sinclair.adhoc.table.pdf) 

- :material-rename: **Name:** edinauto5 
- :fontawesome-solid-user-group: **Participant:** u.edinburgh.sinclair 
- :material-email: **Email:** csincla1 [at] inf [dot] ed [dot] ac [dot] uk 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:**         Lucene retrieval engine; queries weighted according to Web counts and expanded with noun phrases and synonyms 

---
#### edis2 
[**`Results`**](./results.md#edis2), [**`Participants`**](./participants.md#uedinburghsinclair), [**`Proceedings`**](./proceedings.md#trec-genomics-2004), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.edis2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.edis2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.edinburgh.sinclair.triage.table.pdf) 

- :material-rename: **Name:** edis2 
- :fontawesome-solid-user-group: **Participant:** u.edinburgh.sinclair 
- :material-email: **Email:** csincla1 [at] inf [dot] ed [dot] ac [dot] uk 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Mice relevance based on Discussion sections and MH and RN headings, with triage decision based on Discussion section only. 

---
#### eint2 
[**`Results`**](./results.md#eint2), [**`Participants`**](./participants.md#uedinburghsinclair), [**`Proceedings`**](./proceedings.md#trec-genomics-2004), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.eint2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.eint2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.edinburgh.sinclair.triage.table.pdf) 

- :material-rename: **Name:** eint2 
- :fontawesome-solid-user-group: **Participant:** u.edinburgh.sinclair 
- :material-email: **Email:** csincla1 [at] inf [dot] ed [dot] ac [dot] uk 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Based on introduction and MH and RN headings only 

---
#### EMCTNOT1 
[**`Results`**](./results.md#emctnot1), [**`Participants`**](./participants.md#tnokraaij), [**`Proceedings`**](./proceedings.md#mesh-based-feedback-concept-recognition-and-stacked-classification-for-curation-tasks), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.EMCTNOT1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.EMCTNOT1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/tno.kraaij.triage.table.pdf) 

- :material-rename: **Name:** EMCTNOT1 
- :fontawesome-solid-user-group: **Participant:** tno.kraaij 
- :material-email: **Email:** kraaij [at] tpd [dot] tno [dot] nl 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Documents were indexed for three different ontologies using concept recognition (Collexis). MesH terms were also encoded using semantic groups. This resulted in 4 different feature representations for which 5 different classifiers were trained. The output of these classifiers was combined in a meta-classifier. 

---
#### emet2 
[**`Results`**](./results.md#emet2), [**`Participants`**](./participants.md#uedinburghsinclair), [**`Proceedings`**](./proceedings.md#trec-genomics-2004), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.emet2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.emet2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.edinburgh.sinclair.triage.table.pdf) 

- :material-rename: **Name:** emet2 
- :fontawesome-solid-user-group: **Participant:** u.edinburgh.sinclair 
- :material-email: **Email:** csincla1 [at] inf [dot] ed [dot] ac [dot] uk 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Based on Methods sections and MH and RN headings only 

---
#### epub2 
[**`Results`**](./results.md#epub2), [**`Participants`**](./participants.md#uedinburghsinclair), [**`Proceedings`**](./proceedings.md#trec-genomics-2004), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.epub2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.epub2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.edinburgh.sinclair.triage.table.pdf) 

- :material-rename: **Name:** epub2 
- :fontawesome-solid-user-group: **Participant:** u.edinburgh.sinclair 
- :material-email: **Email:** csincla1 [at] inf [dot] ed [dot] ac [dot] uk 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Based on title, abstract and MH and RN headings only 

---
#### eres2 
[**`Results`**](./results.md#eres2), [**`Participants`**](./participants.md#uedinburghsinclair), [**`Proceedings`**](./proceedings.md#trec-genomics-2004), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.eres2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.eres2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.edinburgh.sinclair.triage.table.pdf) 

- :material-rename: **Name:** eres2 
- :fontawesome-solid-user-group: **Participant:** u.edinburgh.sinclair 
- :material-email: **Email:** csincla1 [at] inf [dot] ed [dot] ac [dot] uk 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Mice relevance based on Results sections and MH and RN headings, with triage decision based on Results section only. 

---
#### geneteam1 
[**`Results`**](./results.md#geneteam1), [**`Participants`**](./participants.md#uhospitalgeneva), [**`Proceedings`**](./proceedings.md#biotext-team-experiments-for-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.geneteam1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.geneteam1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.hospital.geneva.triage.table.pdf) 

- :material-rename: **Name:** geneteam1 
- :fontawesome-solid-user-group: **Participant:** u.hospital.geneva 
- :material-email: **Email:** marty [at] eurecom [dot] fr 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Triage with bigrams only 

---
#### geneteam2 
[**`Results`**](./results.md#geneteam2), [**`Participants`**](./participants.md#uhospitalgeneva), [**`Proceedings`**](./proceedings.md#biotext-team-experiments-for-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.geneteam2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.geneteam2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.hospital.geneva.triage.table.pdf) 

- :material-rename: **Name:** geneteam2 
- :fontawesome-solid-user-group: **Participant:** u.hospital.geneva 
- :material-email: **Email:** marty [at] eurecom [dot] fr 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Triage with bigrams and monograms  

---
#### geneteam3 
[**`Results`**](./results.md#geneteam3), [**`Participants`**](./participants.md#uhospitalgeneva), [**`Proceedings`**](./proceedings.md#biotext-team-experiments-for-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.geneteam3.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.geneteam3.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.hospital.geneva.triage.table.pdf) 

- :material-rename: **Name:** geneteam3 
- :fontawesome-solid-user-group: **Participant:** u.hospital.geneva 
- :material-email: **Email:** marty [at] eurecom [dot] fr 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Triage with only monograms 

---
#### geneteamA1 
[**`Results`**](./results.md#geneteama1), [**`Participants`**](./participants.md#uhospitalgeneva), [**`Proceedings`**](./proceedings.md#biotext-team-experiments-for-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.geneteamA1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.geneteamA1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.hospital.geneva.annhi.table.pdf) 

- :material-rename: **Name:** geneteamA1 
- :fontawesome-solid-user-group: **Participant:** u.hospital.geneva 
- :material-email: **Email:** ehrler [at] cui [dot] unige [dot] ch 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** sentence selection V1 categorizer "categMatcher" threshold selection 

---
#### geneteamA2 
[**`Results`**](./results.md#geneteama2), [**`Participants`**](./participants.md#uhospitalgeneva), [**`Proceedings`**](./proceedings.md#biotext-team-experiments-for-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.geneteamA2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.geneteamA2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.hospital.geneva.annhi.table.pdf) 

- :material-rename: **Name:** geneteamA2 
- :fontawesome-solid-user-group: **Participant:** u.hospital.geneva 
- :material-email: **Email:** ehrler [at] cui [dot] unige [dot] ch 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** sentence selection V1 categorizer "GOMAP" threshold selection 

---
#### geneteamA3 
[**`Results`**](./results.md#geneteama3), [**`Participants`**](./participants.md#uhospitalgeneva), [**`Proceedings`**](./proceedings.md#biotext-team-experiments-for-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.geneteamA3.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.geneteamA3.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.hospital.geneva.annhi.table.pdf) 

- :material-rename: **Name:** geneteamA3 
- :fontawesome-solid-user-group: **Participant:** u.hospital.geneva 
- :material-email: **Email:** ehrler [at] cui [dot] unige [dot] ch 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** sentence selection V2 categorizer "categMatcher" threshold selection 

---
#### geneteamA4 
[**`Results`**](./results.md#geneteama4), [**`Participants`**](./participants.md#uhospitalgeneva), [**`Proceedings`**](./proceedings.md#biotext-team-experiments-for-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.geneteamA4.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.geneteamA4.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.hospital.geneva.annhi.table.pdf) 

- :material-rename: **Name:** geneteamA4 
- :fontawesome-solid-user-group: **Participant:** u.hospital.geneva 
- :material-email: **Email:** ehrler [at] cui [dot] unige [dot] ch 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** sentence selection V2 categorizer "GOMAP" threshold selection 

---
#### geneteamA5 
[**`Results`**](./results.md#geneteama5), [**`Participants`**](./participants.md#uhospitalgeneva), [**`Proceedings`**](./proceedings.md#biotext-team-experiments-for-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.geneteamA5.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.geneteamA5.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.hospital.geneva.annhi.table.pdf) 

- :material-rename: **Name:** geneteamA5 
- :fontawesome-solid-user-group: **Participant:** u.hospital.geneva 
- :material-email: **Email:** ehrler [at] cui [dot] unige [dot] ch 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Use of naive bayes  info gain feature selection sentence selection V2 

---
#### GUCbase 
[**`Results`**](./results.md#gucbase), [**`Participants`**](./participants.md#germanucairo), [**`Proceedings`**](./proceedings.md#the-guc-goes-to-trec-2004-using-whole-or-partial-documents-for-retrieval-and-classification-in-the-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.GUCbase.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.GUCbase.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/german.u.cairo.annhi.table.pdf) 

- :material-rename: **Name:** GUCbase 
- :fontawesome-solid-user-group: **Participant:** german.u.cairo 
- :material-email: **Email:** kareem [at] darwish [dot] org 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Baseline run all possible combinations generated 

---
#### GUCir30 
[**`Results`**](./results.md#gucir30), [**`Participants`**](./participants.md#germanucairo), [**`Proceedings`**](./proceedings.md#the-guc-goes-to-trec-2004-using-whole-or-partial-documents-for-retrieval-and-classification-in-the-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.GUCir30.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.GUCir30.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/german.u.cairo.annhi.table.pdf) 

- :material-rename: **Name:** GUCir30 
- :fontawesome-solid-user-group: **Participant:** german.u.cairo 
- :material-email: **Email:** kareem [at] darwish [dot] org 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Lemur Text segments with gene names only Threshold for + Okapi score 30 w/ Backup 

---
#### GUCir50 
[**`Results`**](./results.md#gucir50), [**`Participants`**](./participants.md#germanucairo), [**`Proceedings`**](./proceedings.md#the-guc-goes-to-trec-2004-using-whole-or-partial-documents-for-retrieval-and-classification-in-the-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.GUCir50.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.GUCir50.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/german.u.cairo.annhi.table.pdf) 

- :material-rename: **Name:** GUCir50 
- :fontawesome-solid-user-group: **Participant:** german.u.cairo 
- :material-email: **Email:** kareem [at] darwish [dot] org 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Lemur Text segments with gene names only Threshold for + Okapi score 50 w/ Backup 

---
#### GUClin1260 
[**`Results`**](./results.md#guclin1260), [**`Participants`**](./participants.md#germanucairo), [**`Proceedings`**](./proceedings.md#the-guc-goes-to-trec-2004-using-whole-or-partial-documents-for-retrieval-and-classification-in-the-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.GUClin1260.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.GUClin1260.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/german.u.cairo.triage.table.pdf) 

- :material-rename: **Name:** GUClin1260 
- :fontawesome-solid-user-group: **Participant:** german.u.cairo 
- :material-email: **Email:** kareem [at] darwish [dot] org 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Linear SVM model top 1260 returned documents 

---
#### GUClin1700 
[**`Results`**](./results.md#guclin1700), [**`Participants`**](./participants.md#germanucairo), [**`Proceedings`**](./proceedings.md#the-guc-goes-to-trec-2004-using-whole-or-partial-documents-for-retrieval-and-classification-in-the-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.GUClin1700.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.GUClin1700.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/german.u.cairo.triage.table.pdf) 

- :material-rename: **Name:** GUClin1700 
- :fontawesome-solid-user-group: **Participant:** german.u.cairo 
- :material-email: **Email:** kareem [at] darwish [dot] org 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Linear SVM model top 1700 returned documents 

---
#### GUCply1260 
[**`Results`**](./results.md#gucply1260), [**`Participants`**](./participants.md#germanucairo), [**`Proceedings`**](./proceedings.md#the-guc-goes-to-trec-2004-using-whole-or-partial-documents-for-retrieval-and-classification-in-the-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.GUCply1260.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.GUCply1260.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/german.u.cairo.triage.table.pdf) 

- :material-rename: **Name:** GUCply1260 
- :fontawesome-solid-user-group: **Participant:** german.u.cairo 
- :material-email: **Email:** kareem [at] darwish [dot] org 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Polynomial SVM model top 1260 returned documents captions only 

---
#### GUCply1700 
[**`Results`**](./results.md#gucply1700), [**`Participants`**](./participants.md#germanucairo), [**`Proceedings`**](./proceedings.md#the-guc-goes-to-trec-2004-using-whole-or-partial-documents-for-retrieval-and-classification-in-the-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.GUCply1700.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.GUCply1700.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/german.u.cairo.triage.table.pdf) 

- :material-rename: **Name:** GUCply1700 
- :fontawesome-solid-user-group: **Participant:** german.u.cairo 
- :material-email: **Email:** kareem [at] darwish [dot] org 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Polynomial SVM model top 1700 returned documents captions only 

---
#### GUCsvm0 
[**`Results`**](./results.md#gucsvm0), [**`Participants`**](./participants.md#germanucairo), [**`Proceedings`**](./proceedings.md#the-guc-goes-to-trec-2004-using-whole-or-partial-documents-for-retrieval-and-classification-in-the-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.GUCsvm0.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.GUCsvm0.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/german.u.cairo.annhi.table.pdf) 

- :material-rename: **Name:** GUCsvm0 
- :fontawesome-solid-user-group: **Participant:** german.u.cairo 
- :material-email: **Email:** kareem [at] darwish [dot] org 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Linear SVM  Text segments with gene names only Threshold for + 0.0 

---
#### GUCsvm5 
[**`Results`**](./results.md#gucsvm5), [**`Participants`**](./participants.md#germanucairo), [**`Proceedings`**](./proceedings.md#the-guc-goes-to-trec-2004-using-whole-or-partial-documents-for-retrieval-and-classification-in-the-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.GUCsvm5.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.GUCsvm5.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/german.u.cairo.annhi.table.pdf) 

- :material-rename: **Name:** GUCsvm5 
- :fontawesome-solid-user-group: **Participant:** german.u.cairo 
- :material-email: **Email:** kareem [at] darwish [dot] org 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Linear SVM  Text segments with gene names only Threshold for + -5.0 

---
#### GUCwdply2000 
[**`Results`**](./results.md#gucwdply2000), [**`Participants`**](./participants.md#germanucairo), [**`Proceedings`**](./proceedings.md#the-guc-goes-to-trec-2004-using-whole-or-partial-documents-for-retrieval-and-classification-in-the-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.GUCwdply2000.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.GUCwdply2000.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/german.u.cairo.triage.table.pdf) 

- :material-rename: **Name:** GUCwdply2000 
- :fontawesome-solid-user-group: **Participant:** german.u.cairo 
- :material-email: **Email:** kareem [at] darwish [dot] org 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Polynomial SVM model top 2000 returned documents full documents 

---
#### IBMIRLver1 
[**`Results`**](./results.md#ibmirlver1), [**`Participants`**](./participants.md#ibmindia), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.IBMIRLver1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.IBMIRLver1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/ibm.india.triage.table.pdf) 

- :material-rename: **Name:** IBMIRLver1 
- :fontawesome-solid-user-group: **Participant:** ibm.india 
- :material-email: **Email:** smukherj [at] in [dot] ibm [dot] com 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:**         used bioannotator, followed by classifier 

---
#### iowarun1 
[**`Results`**](./results.md#iowarun1), [**`Participants`**](./participants.md#uiowa), [**`Proceedings`**](./proceedings.md#novelty-question-answering-and-genomics-the-university-of-iowa-response), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.iowarun1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.iowarun1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.iowa.annhi.table.pdf) 

- :material-rename: **Name:** iowarun1 
- :fontawesome-solid-user-group: **Participant:** u.iowa 
- :material-email: **Email:** shannon-bradshaw [at] uiowa [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Iowa team's first run  390 lines        

---
#### iowarun2 
[**`Results`**](./results.md#iowarun2), [**`Participants`**](./participants.md#uiowa), [**`Proceedings`**](./proceedings.md#novelty-question-answering-and-genomics-the-university-of-iowa-response), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.iowarun2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.iowarun2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.iowa.annhi.table.pdf) 

- :material-rename: **Name:** iowarun2 
- :fontawesome-solid-user-group: **Participant:** u.iowa 
- :material-email: **Email:** shannon-bradshaw [at] uiowa [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Iowa's team run 2  305 lines        

---
#### iowarun3 
[**`Results`**](./results.md#iowarun3), [**`Participants`**](./participants.md#uiowa), [**`Proceedings`**](./proceedings.md#novelty-question-answering-and-genomics-the-university-of-iowa-response), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.iowarun3.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.iowarun3.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.iowa.annhi.table.pdf) 

- :material-rename: **Name:** iowarun3 
- :fontawesome-solid-user-group: **Participant:** u.iowa 
- :material-email: **Email:** shannon-bradshaw [at] uiowa [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Iowa's team run 3  447 lines 

---
#### iowarun4 
[**`Results`**](./results.md#iowarun4), [**`Participants`**](./participants.md#uiowa), [**`Proceedings`**](./proceedings.md#novelty-question-answering-and-genomics-the-university-of-iowa-response), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.iowarun4.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.iowarun4.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.iowa.annhi.table.pdf) 

- :material-rename: **Name:** iowarun4 
- :fontawesome-solid-user-group: **Participant:** u.iowa 
- :material-email: **Email:** shannon-bradshaw [at] uiowa [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:**   Used a retrieval approach based on citation sentences.       

---
#### KoikeyaHi1 
[**`Results`**](./results.md#koikeyahi1), [**`Participants`**](./participants.md#utokyo), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.KoikeyaHi1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.KoikeyaHi1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.tokyo.annhi.table.pdf) 

- :material-rename: **Name:** KoikeyaHi1 
- :fontawesome-solid-user-group: **Participant:** u.tokyo 
- :material-email: **Email:** yayamamo [at] hgc [dot] jp 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Efficient structural analyses of sentences. 

---
#### KoikeyaHiev1 
[**`Results`**](./results.md#koikeyahiev1), [**`Participants`**](./participants.md#utokyo), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.KoikeyaHiev1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.KoikeyaHiev1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.tokyo.annhiev.table.pdf) 

- :material-rename: **Name:** KoikeyaHiev1 
- :fontawesome-solid-user-group: **Participant:** u.tokyo 
- :material-email: **Email:** yayamamo [at] hgc [dot] jp 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** annhiev 
- :material-text: **Run description:** Efficient structural analyses of sentences. 

---
#### KoikeyaTri1 
[**`Results`**](./results.md#koikeyatri1), [**`Participants`**](./participants.md#utokyo), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.KoikeyaTri1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.KoikeyaTri1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.tokyo.triage.table.pdf) 

- :material-rename: **Name:** KoikeyaTri1 
- :fontawesome-solid-user-group: **Participant:** u.tokyo 
- :material-email: **Email:** yayamamo [at] hgc [dot] jp 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Efficient structural analyses of sentences. 

---
#### KoikeyaTri2 
[**`Results`**](./results.md#koikeyatri2), [**`Participants`**](./participants.md#utokyo), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.KoikeyaTri2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.KoikeyaTri2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.tokyo.triage.table.pdf) 

- :material-rename: **Name:** KoikeyaTri2 
- :fontawesome-solid-user-group: **Participant:** u.tokyo 
- :material-email: **Email:** yayamamo [at] hgc [dot] jp 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Efficient structural analyses of sentences. Extended version. 

---
#### KoikeyaTri3 
[**`Results`**](./results.md#koikeyatri3), [**`Participants`**](./participants.md#utokyo), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.KoikeyaTri3.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.KoikeyaTri3.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.tokyo.triage.table.pdf) 

- :material-rename: **Name:** KoikeyaTri3 
- :fontawesome-solid-user-group: **Participant:** u.tokyo 
- :material-email: **Email:** yayamamo [at] hgc [dot] jp 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Efficient structural analyses of sentences. Extended and high-rank documents version. 

---
#### lga1 
[**`Results`**](./results.md#lga1), [**`Participants`**](./participants.md#indianauseki), [**`Proceedings`**](./proceedings.md#trec-2004-genomics-track-experiments-at-iub), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.lga1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.lga1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/indiana.u.seki.adhoc.table.pdf) 

- :material-rename: **Name:** lga1 
- :fontawesome-solid-user-group: **Participant:** indiana.u.seki 
- :material-email: **Email:** kseki [at] slis [dot] indiana [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/16/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** query expansion and pseudo-relevance feedback  

---
#### lga2 
[**`Results`**](./results.md#lga2), [**`Participants`**](./participants.md#indianauseki), [**`Proceedings`**](./proceedings.md#trec-2004-genomics-track-experiments-at-iub), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.lga2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.lga2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/indiana.u.seki.adhoc.table.pdf) 

- :material-rename: **Name:** lga2 
- :fontawesome-solid-user-group: **Participant:** indiana.u.seki 
- :material-email: **Email:** kseki [at] slis [dot] indiana [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/16/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** query expansion 

---
#### lgcab1 
[**`Results`**](./results.md#lgcab1), [**`Participants`**](./participants.md#indianauseki), [**`Proceedings`**](./proceedings.md#trec-2004-genomics-track-experiments-at-iub), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.lgcab1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.lgcab1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/indiana.u.seki.annhiev.table.pdf) 

- :material-rename: **Name:** lgcab1 
- :fontawesome-solid-user-group: **Participant:** indiana.u.seki 
- :material-email: **Email:** kseki [at] slis [dot] indiana [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhiev 
- :material-text: **Run description:** knn+svd 

---
#### lgcab2 
[**`Results`**](./results.md#lgcab2), [**`Participants`**](./participants.md#indianauseki), [**`Proceedings`**](./proceedings.md#trec-2004-genomics-track-experiments-at-iub), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.lgcab2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.lgcab2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/indiana.u.seki.annhiev.table.pdf) 

- :material-rename: **Name:** lgcab2 
- :fontawesome-solid-user-group: **Participant:** indiana.u.seki 
- :material-email: **Email:** kseki [at] slis [dot] indiana [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhiev 
- :material-text: **Run description:** knn 

---
#### lgcad1 
[**`Results`**](./results.md#lgcad1), [**`Participants`**](./participants.md#indianauseki), [**`Proceedings`**](./proceedings.md#trec-2004-genomics-track-experiments-at-iub), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.lgcad1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.lgcad1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/indiana.u.seki.annhi.table.pdf) 

- :material-rename: **Name:** lgcad1 
- :fontawesome-solid-user-group: **Participant:** indiana.u.seki 
- :material-email: **Email:** kseki [at] slis [dot] indiana [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** knn+svd 

---
#### lgcad2 
[**`Results`**](./results.md#lgcad2), [**`Participants`**](./participants.md#indianauseki), [**`Proceedings`**](./proceedings.md#trec-2004-genomics-track-experiments-at-iub), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.lgcad2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.lgcad2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/indiana.u.seki.annhi.table.pdf) 

- :material-rename: **Name:** lgcad2 
- :fontawesome-solid-user-group: **Participant:** indiana.u.seki 
- :material-email: **Email:** kseki [at] slis [dot] indiana [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** knn 

---
#### lgct1 
[**`Results`**](./results.md#lgct1), [**`Participants`**](./participants.md#indianauseki), [**`Proceedings`**](./proceedings.md#trec-2004-genomics-track-experiments-at-iub), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.lgct1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.lgct1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/indiana.u.seki.triage.table.pdf) 

- :material-rename: **Name:** lgct1 
- :fontawesome-solid-user-group: **Participant:** indiana.u.seki 
- :material-email: **Email:** jccostel [at] indiana [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Naive Bayes Classifier Gene Filter Mesh Terms 

---
#### lgct2 
[**`Results`**](./results.md#lgct2), [**`Participants`**](./participants.md#indianauseki), [**`Proceedings`**](./proceedings.md#trec-2004-genomics-track-experiments-at-iub), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.lgct2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.lgct2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/indiana.u.seki.triage.table.pdf) 

- :material-rename: **Name:** lgct2 
- :fontawesome-solid-user-group: **Participant:** indiana.u.seki 
- :material-email: **Email:** jccostel [at] indiana [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/31/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Naive Bayes Classifier Gene Filter Mesh Terms 

---
#### LHCUMDSE 
[**`Results`**](./results.md#lhcumdse), [**`Participants`**](./participants.md#nlmumdul), [**`Proceedings`**](./proceedings.md#knowledge-intensive-and-statistical-approaches-to-the-retrieval-and-annotation-of-genomics-medline-citations), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.LHCUMDSE.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.LHCUMDSE.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/nlm.umd.ul.adhoc.table.pdf) 

- :material-rename: **Name:** LHCUMDSE 
- :fontawesome-solid-user-group: **Participant:** nlm.umd.ul 
- :material-email: **Email:** alan [at] nlm [dot] nih [dot] gov 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:**         Search engine (SE) queries were formulated by extracting information from the task queries  gene names recognized by ABGene, the corresponding MeSH terms for the gene names, phrases/concepts identified by MetaMap, organisms extracted using the NCBI Taxonomy, and other useful words extracted based on their form and TFIDF score. The extracted information was translated into SE syntax and weighted, and the results were filtered to those identified as likely genetically related by Journal Descriptor Indexing (JDI).  

---
#### MeijiHilG 
[**`Results`**](./results.md#meijihilg), [**`Participants`**](./participants.md#meijiu), [**`Proceedings`**](./proceedings.md#meiji-university-web-novelty-and-genomic-track-experiments), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.MeijiHilG.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.MeijiHilG.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/meiji.u.adhoc.table.pdf) 

- :material-rename: **Name:** MeijiHilG 
- :fontawesome-solid-user-group: **Participant:** meiji.u 
- :material-email: **Email:** t-kondo [at] cs [dot] meiji [dot] ac [dot] jp 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** query expansion depended on context 

---
#### NLMA1 
[**`Results`**](./results.md#nlma1), [**`Participants`**](./participants.md#nlmumdul), [**`Proceedings`**](./proceedings.md#knowledge-intensive-and-statistical-approaches-to-the-retrieval-and-annotation-of-genomics-medline-citations), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.NLMA1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.NLMA1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/nlm.umd.ul.annhi.table.pdf) 

- :material-rename: **Name:** NLMA1 
- :fontawesome-solid-user-group: **Participant:** nlm.umd.ul 
- :material-email: **Email:** alan [at] nlm [dot] nih [dot] gov 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** A machine learning method which is a variation of decision list learning. NLMA1 is obtained using the whole training set (T1=0.5, T2=50) 

---
#### NLMA2 
[**`Results`**](./results.md#nlma2), [**`Participants`**](./participants.md#nlmumdul), [**`Proceedings`**](./proceedings.md#knowledge-intensive-and-statistical-approaches-to-the-retrieval-and-annotation-of-genomics-medline-citations), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.NLMA2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.NLMA2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/nlm.umd.ul.annhi.table.pdf) 

- :material-rename: **Name:** NLMA2 
- :fontawesome-solid-user-group: **Participant:** nlm.umd.ul 
- :material-email: **Email:** alan [at] nlm [dot] nih [dot] gov 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** A machine learning method which is a variation of decision list learning. NLMA2 is obtained with an additional bootstrapping step, for (PMID, gene) pairs with a summation that is larger than T3 (i.e., 100), add them into the training set, and redo the categorization (with a threshold T1=0.8, T2=80). 

---
#### NLMT21 
[**`Results`**](./results.md#nlmt21), [**`Participants`**](./participants.md#nlmumdul), [**`Proceedings`**](./proceedings.md#knowledge-intensive-and-statistical-approaches-to-the-retrieval-and-annotation-of-genomics-medline-citations), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.NLMT21.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.NLMT21.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/nlm.umd.ul.triage.table.pdf) 

- :material-rename: **Name:** NLMT21 
- :fontawesome-solid-user-group: **Participant:** nlm.umd.ul 
- :material-email: **Email:** alan [at] nlm [dot] nih [dot] gov 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:**  Using all training data, create theme in + with background + or - Query test set with theme Keep if score > 0        

---
#### NLMT22 
[**`Results`**](./results.md#nlmt22), [**`Participants`**](./participants.md#nlmumdul), [**`Proceedings`**](./proceedings.md#knowledge-intensive-and-statistical-approaches-to-the-retrieval-and-annotation-of-genomics-medline-citations), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.NLMT22.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.NLMT22.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/nlm.umd.ul.triage.table.pdf) 

- :material-rename: **Name:** NLMT22 
- :fontawesome-solid-user-group: **Participant:** nlm.umd.ul 
- :material-email: **Email:** alan [at] nlm [dot] nih [dot] gov 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Split into three sets, JBC,JCB,PNAS Create theme for each set in + with background + or - Split test set by journal Query each set by its theme Combine sco > 0 for all 3 journals   

---
#### NLMT2ADA 
[**`Results`**](./results.md#nlmt2ada), [**`Participants`**](./participants.md#nlmumdul), [**`Proceedings`**](./proceedings.md#knowledge-intensive-and-statistical-approaches-to-the-retrieval-and-annotation-of-genomics-medline-citations), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.NLMT2ADA.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.NLMT2ADA.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/nlm.umd.ul.triage.table.pdf) 

- :material-rename: **Name:** NLMT2ADA 
- :fontawesome-solid-user-group: **Participant:** nlm.umd.ul 
- :material-email: **Email:** alan [at] nlm [dot] nih [dot] gov 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** ADA machine learning algorithm using 3-fold cross validation on train 

---
#### NLMT2BAYES 
[**`Results`**](./results.md#nlmt2bayes), [**`Participants`**](./participants.md#nlmumdul), [**`Proceedings`**](./proceedings.md#knowledge-intensive-and-statistical-approaches-to-the-retrieval-and-annotation-of-genomics-medline-citations), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.NLMT2BAYES.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.NLMT2BAYES.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/nlm.umd.ul.triage.table.pdf) 

- :material-rename: **Name:** NLMT2BAYES 
- :fontawesome-solid-user-group: **Participant:** nlm.umd.ul 
- :material-email: **Email:** alan [at] nlm [dot] nih [dot] gov 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** BAYES machine learning algorithm using 3-fold cross validation on train 

---
#### NLMT2SVM 
[**`Results`**](./results.md#nlmt2svm), [**`Participants`**](./participants.md#nlmumdul), [**`Proceedings`**](./proceedings.md#knowledge-intensive-and-statistical-approaches-to-the-retrieval-and-annotation-of-genomics-medline-citations), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.NLMT2SVM.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.NLMT2SVM.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/nlm.umd.ul.triage.table.pdf) 

- :material-rename: **Name:** NLMT2SVM 
- :fontawesome-solid-user-group: **Participant:** nlm.umd.ul 
- :material-email: **Email:** alan [at] nlm [dot] nih [dot] gov 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** SVM machine learning algorithm using 3-fold cross validation on train 

---
#### NTU2v3N1 
[**`Results`**](./results.md#ntu2v3n1), [**`Participants`**](./participants.md#ntuchen), [**`Proceedings`**](./proceedings.md#identifying-relevant-full-text-articles-for-go-annotation-without-mesh-terms), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.NTU2v3N1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.NTU2v3N1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/ntu.chen.triage.table.pdf) 

- :material-rename: **Name:** NTU2v3N1 
- :fontawesome-solid-user-group: **Participant:** ntu.chen 
- :material-email: **Email:** clee [at] nlg [dot] csie [dot] ntu [dot] edu [dot] tw 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/27/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** title + abstract + fig/tbl captions 

---
#### NTU3v3N1 
[**`Results`**](./results.md#ntu3v3n1), [**`Participants`**](./participants.md#ntuchen), [**`Proceedings`**](./proceedings.md#identifying-relevant-full-text-articles-for-go-annotation-without-mesh-terms), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.NTU3v3N1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.NTU3v3N1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/ntu.chen.triage.table.pdf) 

- :material-rename: **Name:** NTU3v3N1 
- :fontawesome-solid-user-group: **Participant:** ntu.chen 
- :material-email: **Email:** clee [at] nlg [dot] csie [dot] ntu [dot] edu [dot] tw 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/29/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** atl + abs + fig/tbl captions + body(if no abs) 

---
#### NTU3v3N1c2 
[**`Results`**](./results.md#ntu3v3n1c2), [**`Participants`**](./participants.md#ntuchen), [**`Proceedings`**](./proceedings.md#identifying-relevant-full-text-articles-for-go-annotation-without-mesh-terms), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.NTU3v3N1c2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.NTU3v3N1c2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/ntu.chen.triage.table.pdf) 

- :material-rename: **Name:** NTU3v3N1c2 
- :fontawesome-solid-user-group: **Participant:** ntu.chen 
- :material-email: **Email:** clee [at] nlg [dot] csie [dot] ntu [dot] edu [dot] tw 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/29/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** atl + abs + fig/tbl captions + body(if no abs) different parameters 

---
#### NTU4v3N1416 
[**`Results`**](./results.md#ntu4v3n1416), [**`Participants`**](./participants.md#ntuchen), [**`Proceedings`**](./proceedings.md#identifying-relevant-full-text-articles-for-go-annotation-without-mesh-terms), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.NTU4v3N1416.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.NTU4v3N1416.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/ntu.chen.triage.table.pdf) 

- :material-rename: **Name:** NTU4v3N1416 
- :fontawesome-solid-user-group: **Participant:** ntu.chen 
- :material-email: **Email:** clee [at] nlg [dot] csie [dot] ntu [dot] edu [dot] tw 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** atl + abs + fig/tbl captions + BODY (if no abs) or result/discussion/conclusion Sections in BODY (if has abs) 

---
#### nusbird2004a 
[**`Results`**](./results.md#nusbird2004a), [**`Participants`**](./participants.md#mlgnus), [**`Proceedings`**](./proceedings.md#experience-of-using-svm-for-the-triage-task-in-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.nusbird2004a.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.nusbird2004a.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/mlg.nus.triage.table.pdf) 

- :material-rename: **Name:** nusbird2004a 
- :fontawesome-solid-user-group: **Participant:** mlg.nus 
- :material-email: **Email:** smadellz [at] nus [dot] edu [dot] sg 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/26/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** SVM 

---
#### nusbird2004b 
[**`Results`**](./results.md#nusbird2004b), [**`Participants`**](./participants.md#mlgnus), [**`Proceedings`**](./proceedings.md#experience-of-using-svm-for-the-triage-task-in-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.nusbird2004b.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.nusbird2004b.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/mlg.nus.triage.table.pdf) 

- :material-rename: **Name:** nusbird2004b 
- :fontawesome-solid-user-group: **Participant:** mlg.nus 
- :material-email: **Email:** smadellz [at] nus [dot] edu [dot] sg 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/29/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** SVM 

---
#### nusbird2004c 
[**`Results`**](./results.md#nusbird2004c), [**`Participants`**](./participants.md#mlgnus), [**`Proceedings`**](./proceedings.md#experience-of-using-svm-for-the-triage-task-in-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.nusbird2004c.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.nusbird2004c.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/mlg.nus.triage.table.pdf) 

- :material-rename: **Name:** nusbird2004c 
- :fontawesome-solid-user-group: **Participant:** mlg.nus 
- :material-email: **Email:** smadellz [at] nus [dot] edu [dot] sg 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/29/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** SVM, with additional positive training examples. 

---
#### nusbird2004d 
[**`Results`**](./results.md#nusbird2004d), [**`Participants`**](./participants.md#mlgnus), [**`Proceedings`**](./proceedings.md#experience-of-using-svm-for-the-triage-task-in-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.nusbird2004d.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.nusbird2004d.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/mlg.nus.triage.table.pdf) 

- :material-rename: **Name:** nusbird2004d 
- :fontawesome-solid-user-group: **Participant:** mlg.nus 
- :material-email: **Email:** smadellz [at] nus [dot] edu [dot] sg 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** SVM 

---
#### nusbird2004e 
[**`Results`**](./results.md#nusbird2004e), [**`Participants`**](./participants.md#mlgnus), [**`Proceedings`**](./proceedings.md#experience-of-using-svm-for-the-triage-task-in-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.nusbird2004e.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.nusbird2004e.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/mlg.nus.triage.table.pdf) 

- :material-rename: **Name:** nusbird2004e 
- :fontawesome-solid-user-group: **Participant:** mlg.nus 
- :material-email: **Email:** smadellz [at] nus [dot] edu [dot] sg 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** SVM 

---
#### OHSUAll 
[**`Results`**](./results.md#ohsuall), [**`Participants`**](./participants.md#ohsuhersh), [**`Proceedings`**](./proceedings.md#feature-generation-feature-selection-classifiers-and-conceptual-drift-for-biomedical-document-triage), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.OHSUAll.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.OHSUAll.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/ohsu.hersh.adhoc.table.pdf) 

- :material-rename: **Name:** OHSUAll 
- :fontawesome-solid-user-group: **Participant:** ohsu.hersh 
- :material-email: **Email:** hersh [at] ohsu [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Automatic query generation, processed by Lucene using TF-IDF without normalization 

---
#### OHSUNBAYES 
[**`Results`**](./results.md#ohsunbayes), [**`Participants`**](./participants.md#ohsuhersh), [**`Proceedings`**](./proceedings.md#feature-generation-feature-selection-classifiers-and-conceptual-drift-for-biomedical-document-triage), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.OHSUNBAYES.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.OHSUNBAYES.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/ohsu.hersh.triage.table.pdf) 

- :material-rename: **Name:** OHSUNBAYES 
- :fontawesome-solid-user-group: **Participant:** ohsu.hersh 
- :material-email: **Email:** cohenaa [at] ohsu [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/24/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** CHI SQUARE 0.025 FULL FEATURE SET NAIVE BAYES CLASSIFIER         

---
#### OHSUNeeds 
[**`Results`**](./results.md#ohsuneeds), [**`Participants`**](./participants.md#ohsuhersh), [**`Proceedings`**](./proceedings.md#feature-generation-feature-selection-classifiers-and-conceptual-drift-for-biomedical-document-triage), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.OHSUNeeds.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.OHSUNeeds.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/ohsu.hersh.adhoc.table.pdf) 

- :material-rename: **Name:** OHSUNeeds 
- :fontawesome-solid-user-group: **Participant:** ohsu.hersh 
- :material-email: **Email:** hersh [at] ohsu [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Automatic query generation, processed by Lucene using TF-IDF without normalization 

---
#### OHSUSVMJ20 
[**`Results`**](./results.md#ohsusvmj20), [**`Participants`**](./participants.md#ohsuhersh), [**`Proceedings`**](./proceedings.md#feature-generation-feature-selection-classifiers-and-conceptual-drift-for-biomedical-document-triage), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.OHSUSVMJ20.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.OHSUSVMJ20.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/ohsu.hersh.triage.table.pdf) 

- :material-rename: **Name:** OHSUSVMJ20 
- :fontawesome-solid-user-group: **Participant:** ohsu.hersh 
- :material-email: **Email:** cohenaa [at] ohsu [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/24/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** CHI SQUARE 0.025 FULL FEATURE SET SVMLIGHT j=20.0 CLASSIFIER      

---
#### OHSUVP 
[**`Results`**](./results.md#ohsuvp), [**`Participants`**](./participants.md#ohsuhersh), [**`Proceedings`**](./proceedings.md#feature-generation-feature-selection-classifiers-and-conceptual-drift-for-biomedical-document-triage), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.OHSUVP.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.OHSUVP.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/ohsu.hersh.triage.table.pdf) 

- :material-rename: **Name:** OHSUVP 
- :fontawesome-solid-user-group: **Participant:** ohsu.hersh 
- :material-email: **Email:** cohenaa [at] ohsu [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/24/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** CHI SQUARE 0.025 FULL FEATURE SET VOTING PERCEPTRON CLASSIFIER LINEAR KERNEL FN LEARNING RATE 20.0 FP LEARNING RATE 1.0   

---
#### PD50501 
[**`Results`**](./results.md#pd50501), [**`Participants`**](./participants.md#upadova), [**`Proceedings`**](./proceedings.md#expanding-queries-using-stems-and-symbols), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.PD50501.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.PD50501.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.padova.adhoc.table.pdf) 

- :material-rename: **Name:** PD50501 
- :fontawesome-solid-user-group: **Participant:** u.padova 
- :material-email: **Email:** massimo [dot] melucci [at] unipd [dot] it 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** MySQL has been employed as IR engine. PD50501 has been obtained by using a new query expansion technique. After retrieving 20 documents, all the symbols are selected  together with the keywords occurring in the 10-word window built around each symbol. The 50 most frequent keywords are selected and linked to the symbols co-occurring in the text  windows. This way, a bi-partite graph is generated where symbols "point-to" frequent and close keywords.SPLIT (see PDTNsmp4 description) is then performed to disclose the mutual reinforcement relationship  between symbols and keywords. The most "authoritative" keywords  are frequently pointed-to by the symbols which frequently point-to "authoritative" keywords. The most "authoritative" keywords are added to expand the query which is in turn used to retrieve  1000 documents.  

---
#### PDTNsmp4 
[**`Results`**](./results.md#pdtnsmp4), [**`Participants`**](./participants.md#upadova), [**`Proceedings`**](./proceedings.md#expanding-queries-using-stems-and-symbols), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.PDTNsmp4.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.PDTNsmp4.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.padova.adhoc.table.pdf) 

- :material-rename: **Name:** PDTNsmp4 
- :fontawesome-solid-user-group: **Participant:** u.padova 
- :material-email: **Email:** massimo [dot] melucci [at] unipd [dot] it 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** MySQL has been employed as IR engine.  PDTNsmp4 has been obtained by indexing the collection using SPLIT,  a stemming algorithm proposed and  tested for some European languages.  SPLIT infers directly the word formation rules from the corpus of words  in the collection by exploiting a mutual reinforcement between  the prefixes and suffixes of words. The hypothesis that SPLIT is effective has been tested in this domain-specific context, in which word formation rules can be different from those of common English.  

---
#### pllsgen4a1 
[**`Results`**](./results.md#pllsgen4a1), [**`Participants`**](./participants.md#patolisfujita), [**`Proceedings`**](./proceedings.md#revisiting-again-document-length-hypotheses-trec-2004-genomics-track-experiments-at-patolis), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.pllsgen4a1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.pllsgen4a1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/patolis.fujita.adhoc.table.pdf) 

- :material-rename: **Name:** pllsgen4a1 
- :fontawesome-solid-user-group: **Participant:** patolis.fujita 
- :material-email: **Email:** s_fujita [at] patolis [dot] co [dot] jp 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/14/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Word based indexing, no stemmer, Inquery stopwords, TF*IDF,BM25TF, MESH expansion,LocusLink Expansion, Pseudo feedback. 

---
#### pllsgen4a2 
[**`Results`**](./results.md#pllsgen4a2), [**`Participants`**](./participants.md#patolisfujita), [**`Proceedings`**](./proceedings.md#revisiting-again-document-length-hypotheses-trec-2004-genomics-track-experiments-at-patolis), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.pllsgen4a2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.pllsgen4a2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/patolis.fujita.adhoc.table.pdf) 

- :material-rename: **Name:** pllsgen4a2 
- :fontawesome-solid-user-group: **Participant:** patolis.fujita 
- :material-email: **Email:** s_fujita [at] patolis [dot] co [dot] jp 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/14/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Word based indexing, porter stemmer, Inquery stopwords, TF*IDF,BM25TF, MESH expansion,LocusLink Expansion, Pseudo feedback. 

---
#### pllsgen4t1 
[**`Results`**](./results.md#pllsgen4t1), [**`Participants`**](./participants.md#patolisfujita), [**`Proceedings`**](./proceedings.md#revisiting-again-document-length-hypotheses-trec-2004-genomics-track-experiments-at-patolis), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.pllsgen4t1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.pllsgen4t1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/patolis.fujita.triage.table.pdf) 

- :material-rename: **Name:** pllsgen4t1 
- :fontawesome-solid-user-group: **Participant:** patolis.fujita 
- :material-email: **Email:** s_fujita [at] patolis [dot] co [dot] jp 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/27/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** SVM Classifier using features from fulltext words, MeSH terms, Gene names, weighted by log-TF. 

---
#### pllsgen4t2 
[**`Results`**](./results.md#pllsgen4t2), [**`Participants`**](./participants.md#patolisfujita), [**`Proceedings`**](./proceedings.md#revisiting-again-document-length-hypotheses-trec-2004-genomics-track-experiments-at-patolis), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.pllsgen4t2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.pllsgen4t2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/patolis.fujita.triage.table.pdf) 

- :material-rename: **Name:** pllsgen4t2 
- :fontawesome-solid-user-group: **Participant:** patolis.fujita 
- :material-email: **Email:** s_fujita [at] patolis [dot] co [dot] jp 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/27/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** SVM Classifier using features from fulltext words, MeSH terms, Gene names, weighted by log-TF. 

---
#### pllsgen4t3 
[**`Results`**](./results.md#pllsgen4t3), [**`Participants`**](./participants.md#patolisfujita), [**`Proceedings`**](./proceedings.md#revisiting-again-document-length-hypotheses-trec-2004-genomics-track-experiments-at-patolis), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.pllsgen4t3.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.pllsgen4t3.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/patolis.fujita.triage.table.pdf) 

- :material-rename: **Name:** pllsgen4t3 
- :fontawesome-solid-user-group: **Participant:** patolis.fujita 
- :material-email: **Email:** s_fujita [at] patolis [dot] co [dot] jp 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/27/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** SVM Classifier using features from fulltext words, MeSH terms, Gene names, weighted by log-TF. 

---
#### pllsgen4t4 
[**`Results`**](./results.md#pllsgen4t4), [**`Participants`**](./participants.md#patolisfujita), [**`Proceedings`**](./proceedings.md#revisiting-again-document-length-hypotheses-trec-2004-genomics-track-experiments-at-patolis), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.pllsgen4t4.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.pllsgen4t4.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/patolis.fujita.triage.table.pdf) 

- :material-rename: **Name:** pllsgen4t4 
- :fontawesome-solid-user-group: **Participant:** patolis.fujita 
- :material-email: **Email:** s_fujita [at] patolis [dot] co [dot] jp 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** SVM classifier using features from fulltext  words, MeSH terms and Gene names, weighted by log-TF  

---
#### pllsgen4t5 
[**`Results`**](./results.md#pllsgen4t5), [**`Participants`**](./participants.md#patolisfujita), [**`Proceedings`**](./proceedings.md#revisiting-again-document-length-hypotheses-trec-2004-genomics-track-experiments-at-patolis), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.pllsgen4t5.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.pllsgen4t5.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/patolis.fujita.triage.table.pdf) 

- :material-rename: **Name:** pllsgen4t5 
- :fontawesome-solid-user-group: **Participant:** patolis.fujita 
- :material-email: **Email:** s_fujita [at] patolis [dot] co [dot] jp 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** SVM classifier using features from fulltext  words, MeSH terms and Gene names, weighted by log-TF  

---
#### PSE 
[**`Results`**](./results.md#pse), [**`Participants`**](./participants.md#germanucairo), [**`Proceedings`**](./proceedings.md#the-guc-goes-to-trec-2004-using-whole-or-partial-documents-for-retrieval-and-classification-in-the-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.PSE.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.PSE.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/german.u.cairo.adhoc.table.pdf) 

- :material-rename: **Name:** PSE 
- :fontawesome-solid-user-group: **Participant:** german.u.cairo 
- :material-email: **Email:** kareem [at] darwish [dot] org 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/16/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** no query expansion, no-stemming, hyphenated expressions, OKAPI-BM25, PSE 

---
#### RMITa 
[**`Results`**](./results.md#rmita), [**`Participants`**](./participants.md#rmitscholer), [**`Proceedings`**](./proceedings.md#rmit-university-at-trec-2004), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.RMITa.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.RMITa.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/rmit.scholer.adhoc.table.pdf) 

- :material-rename: **Name:** RMITa 
- :fontawesome-solid-user-group: **Participant:** rmit.scholer 
- :material-email: **Email:** abhijit [at] cs [dot] rmit [dot] edu [dot] au 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/14/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Plain text search using 'title', and 'need' fields from the query, and all fields from the Medline data. Searches were conducted using indexes from the Zettaire search system.  

---
#### RMITb 
[**`Results`**](./results.md#rmitb), [**`Participants`**](./participants.md#rmitscholer), [**`Proceedings`**](./proceedings.md#rmit-university-at-trec-2004), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.RMITb.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.RMITb.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/rmit.scholer.adhoc.table.pdf) 

- :material-rename: **Name:** RMITb 
- :fontawesome-solid-user-group: **Participant:** rmit.scholer 
- :material-email: **Email:** abhijit [at] cs [dot] rmit [dot] edu [dot] au 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/14/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Novel technique using o 'title', and 'need' fields from the       queries o all fields from Medline data o term expansion  o species-based search-space    partitioning Searches were conducted using indexes from the Zettaire search system. 

---
#### run1 
[**`Results`**](./results.md#run1), [**`Participants`**](./participants.md#utwente), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.run1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.run1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/utwente.adhoc.table.pdf) 

- :material-rename: **Name:** run1 
- :fontawesome-solid-user-group: **Participant:** utwente 
- :material-email: **Email:** borssumw [at] cs [dot] utwente [dot] nl 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** We just recently joined the genomics track, because of this our system couldnt run all queries yet. the ones it could run are included in our results. The titles and abstracts from the medline records were used.  

---
#### rutgersGAH1 
[**`Results`**](./results.md#rutgersgah1), [**`Participants`**](./participants.md#rutgersdayanik), [**`Proceedings`**](./proceedings.md#dimacs-at-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.rutgersGAH1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.rutgersGAH1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/rutgers.dayanik.adhoc.table.pdf) 

- :material-rename: **Name:** rutgersGAH1 
- :fontawesome-solid-user-group: **Participant:** rutgers.dayanik 
- :material-email: **Email:** aynur [at] cs [dot] rutgers [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/14/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** We used MG retrieval system to index the MEDLINE article collection. We used title, abstract, chemical names and mesh terms sections of the articles to index the collection. We constructed queries from topic titles and needs. We performed the retrieval as a two-stage process. First we identifed the relevant documents by MG, and then we performed boolean full-text on the results using MySQL.  

---
#### rutgersGAH2 
[**`Results`**](./results.md#rutgersgah2), [**`Participants`**](./participants.md#rutgersdayanik), [**`Proceedings`**](./proceedings.md#dimacs-at-the-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.rutgersGAH2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.rutgersGAH2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/rutgers.dayanik.adhoc.table.pdf) 

- :material-rename: **Name:** rutgersGAH2 
- :fontawesome-solid-user-group: **Participant:** rutgers.dayanik 
- :material-email: **Email:** aynur [at] cs [dot] rutgers [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/14/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** We used MG retrieval system to index the MEDLINE article collection. We used title, abstract, chemical names and mesh terms sections of the articles to index the collection. We constructed queries from topic titles and needs. We computed a relevance score for ranking using the frequency and inverse document frequency of query terms as well as the proximity of topic title query terms.  

---
#### shefauto1 
[**`Results`**](./results.md#shefauto1), [**`Participants`**](./participants.md#usheffieldgaizauskas), [**`Proceedings`**](./proceedings.md#sheffield-university-and-the-trec-2004-genomics-track-query-expansion-using-synonymous-terms), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.shefauto1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.shefauto1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.sheffield.gaizauskas.adhoc.table.pdf) 

- :material-rename: **Name:** shefauto1 
- :fontawesome-solid-user-group: **Participant:** u.sheffield.gaizauskas 
- :material-email: **Email:** g [dot] yikun [at] dcs [dot] shef [dot] ac [dot] uk 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Use the UMLS to extend synonyms for each keywords. Use LT chunker to find noun phrases and abbrievations. 

---
#### shefauto2 
[**`Results`**](./results.md#shefauto2), [**`Participants`**](./participants.md#usheffieldgaizauskas), [**`Proceedings`**](./proceedings.md#sheffield-university-and-the-trec-2004-genomics-track-query-expansion-using-synonymous-terms), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.shefauto2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.shefauto2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.sheffield.gaizauskas.adhoc.table.pdf) 

- :material-rename: **Name:** shefauto2 
- :fontawesome-solid-user-group: **Participant:** u.sheffield.gaizauskas 
- :material-email: **Email:** g [dot] yikun [at] dcs [dot] shef [dot] ac [dot] uk 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** No synonyms are used. Use LT chunker to find noun phrases and abbrievations. 

---
#### tgnNecaux 
[**`Results`**](./results.md#tgnnecaux), [**`Participants`**](./participants.md#tarragon), [**`Proceedings`**](./proceedings.md#information-needs-and-automatic-queries), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.tgnNecaux.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.tgnNecaux.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/tarragon.adhoc.table.pdf) 

- :material-rename: **Name:** tgnNecaux 
- :fontawesome-solid-user-group: **Participant:** tarragon 
- :material-email: **Email:** rtong [at] tgncorp [dot] com 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/12/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Variant run. Eliminates noise phrases, then uses <FREETEXT> on all fields and combines using <NECAUX>, with CONTEXT field as the auxiliary.       

---
#### tgnSplit 
[**`Results`**](./results.md#tgnsplit), [**`Participants`**](./participants.md#tarragon), [**`Proceedings`**](./proceedings.md#information-needs-and-automatic-queries), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.tgnSplit.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.tgnSplit.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/tarragon.adhoc.table.pdf) 

- :material-rename: **Name:** tgnSplit 
- :fontawesome-solid-user-group: **Participant:** tarragon 
- :material-email: **Email:** rtong [at] tgncorp [dot] com 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/12/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Base run. Eliminates noise phrases, then uses <FREETEXT> on all fields and combines using <ACCRUE>.        

---
#### THIRcat01 
[**`Results`**](./results.md#thircat01), [**`Participants`**](./participants.md#tsinghuama), [**`Proceedings`**](./proceedings.md#thuir-at-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.THIRcat01.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.THIRcat01.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/tsinghua.ma.triage.table.pdf) 

- :material-rename: **Name:** THIRcat01 
- :fontawesome-solid-user-group: **Participant:** tsinghua.ma 
- :material-email: **Email:** zx97 [at] mails [dot] tsinghua [dot] edu [dot] cn 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** balanced between +/- subsets 

---
#### THIRcat02 
[**`Results`**](./results.md#thircat02), [**`Participants`**](./participants.md#tsinghuama), [**`Proceedings`**](./proceedings.md#thuir-at-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.THIRcat02.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.THIRcat02.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/tsinghua.ma.triage.table.pdf) 

- :material-rename: **Name:** THIRcat02 
- :fontawesome-solid-user-group: **Participant:** tsinghua.ma 
- :material-email: **Email:** zx97 [at] mails [dot] tsinghua [dot] edu [dot] cn 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** kmeans clustering, low threshold 

---
#### THIRcat03 
[**`Results`**](./results.md#thircat03), [**`Participants`**](./participants.md#tsinghuama), [**`Proceedings`**](./proceedings.md#thuir-at-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.THIRcat03.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.THIRcat03.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/tsinghua.ma.triage.table.pdf) 

- :material-rename: **Name:** THIRcat03 
- :fontawesome-solid-user-group: **Participant:** tsinghua.ma 
- :material-email: **Email:** zx97 [at] mails [dot] tsinghua [dot] edu [dot] cn 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** using GO-item related words to expand the feature directory 

---
#### THIRcat04 
[**`Results`**](./results.md#thircat04), [**`Participants`**](./participants.md#tsinghuama), [**`Proceedings`**](./proceedings.md#thuir-at-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.THIRcat04.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.THIRcat04.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/tsinghua.ma.triage.table.pdf) 

- :material-rename: **Name:** THIRcat04 
- :fontawesome-solid-user-group: **Participant:** tsinghua.ma 
- :material-email: **Email:** zx97 [at] mails [dot] tsinghua [dot] edu [dot] cn 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** kmeans clustering, high threshold 

---
#### THIRcat05 
[**`Results`**](./results.md#thircat05), [**`Participants`**](./participants.md#tsinghuama), [**`Proceedings`**](./proceedings.md#thuir-at-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.THIRcat05.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.THIRcat05.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/tsinghua.ma.triage.table.pdf) 

- :material-rename: **Name:** THIRcat05 
- :fontawesome-solid-user-group: **Participant:** tsinghua.ma 
- :material-email: **Email:** zx97 [at] mails [dot] tsinghua [dot] edu [dot] cn 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** bool weight instead of TFIDF weight 

---
#### THUIRgen01 
[**`Results`**](./results.md#thuirgen01), [**`Participants`**](./participants.md#tsinghuama), [**`Proceedings`**](./proceedings.md#thuir-at-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.THUIRgen01.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.THUIRgen01.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/tsinghua.ma.adhoc.table.pdf) 

- :material-rename: **Name:** THUIRgen01 
- :fontawesome-solid-user-group: **Participant:** tsinghua.ma 
- :material-email: **Email:** liuyiqun03 [at] mails [dot] tsinghua [dot] edu [dot] cn 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:**         Use our IR systerm named TMiner.Recognize term in non_text fields,in particular MeSH,Other Term (OT),Gene Symbol(GS) and substance name(RN).Give different weights to weights the field of title(TI) and MeSH.Use relevance feedback technology. All above processes are done autaomatiacally. Manually select gene names and expend queries by an abbreviations dictionary. 

---
#### THUIRgen02 
[**`Results`**](./results.md#thuirgen02), [**`Participants`**](./participants.md#tsinghuama), [**`Proceedings`**](./proceedings.md#thuir-at-trec-2004-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.THUIRgen02.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.THUIRgen02.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/tsinghua.ma.adhoc.table.pdf) 

- :material-rename: **Name:** THUIRgen02 
- :fontawesome-solid-user-group: **Participant:** tsinghua.ma 
- :material-email: **Email:** liuyiqun03 [at] mails [dot] tsinghua [dot] edu [dot] cn 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:**        Use our IR systerm named TMiner  Recognize term in non_text fields,in particular MeSH,Other Term (OT),Gene Symbol(GS) and substance name(RN).Give different weights to weights the fields of title(TI) and MeSH.Use relevance feedback technology.Query Expansion (QE) uses an abbreviation dictionary. All processes are done automatically.  

---
#### tnog2 
[**`Results`**](./results.md#tnog2), [**`Participants`**](./participants.md#tnokraaij), [**`Proceedings`**](./proceedings.md#mesh-based-feedback-concept-recognition-and-stacked-classification-for-curation-tasks), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.tnog2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.tnog2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/tno.kraaij.adhoc.table.pdf) 

- :material-rename: **Name:** tnog2 
- :fontawesome-solid-user-group: **Participant:** tno.kraaij 
- :material-email: **Email:** kraaij [at] tpd [dot] tno [dot] nl 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Baseline run, using only title and abstract fields. LM based retrieval model       

---
#### tnog3 
[**`Results`**](./results.md#tnog3), [**`Participants`**](./participants.md#tnokraaij), [**`Proceedings`**](./proceedings.md#mesh-based-feedback-concept-recognition-and-stacked-classification-for-curation-tasks), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.tnog3.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.tnog3.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/tno.kraaij.adhoc.table.pdf) 

- :material-rename: **Name:** tnog3 
- :fontawesome-solid-user-group: **Participant:** tno.kraaij 
- :material-email: **Email:** kraaij [at] tpd [dot] tno [dot] nl 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Combination run  baseline run tnog2 interpolated with a run based on MeSH queries. MeSH queries were automatically derived from the top 3 documents in the tnog2 run. 

---
#### tq0 
[**`Results`**](./results.md#tq0), [**`Participants`**](./participants.md#nlmumdul), [**`Proceedings`**](./proceedings.md#knowledge-intensive-and-statistical-approaches-to-the-retrieval-and-annotation-of-genomics-medline-citations), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.tq0.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.tq0.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/nlm.umd.ul.adhoc.table.pdf) 

- :material-rename: **Name:** tq0 
- :fontawesome-solid-user-group: **Participant:** nlm.umd.ul 
- :material-email: **Email:** alan [at] nlm [dot] nih [dot] gov 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** TexTool, a text neighboring program based on TFIDF vector retrieval, was applied to the queries after removing common stopwords (the, we, etc.) from a list of 313, entering the title twice and the need and context once, to find 1,000 similar abstracts.  

---
#### TRICSUSM 
[**`Results`**](./results.md#tricsusm), [**`Participants`**](./participants.md#usanmarcos), [**`Proceedings`**](./proceedings.md#categorization-of-genomics-text-based-on-decision-rules), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.TRICSUSM.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.TRICSUSM.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.sanmarcos.triage.table.pdf) 

- :material-rename: **Name:** TRICSUSM 
- :fontawesome-solid-user-group: **Participant:** u.sanmarcos 
- :material-email: **Email:** rguillen [at] csusm [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/26/2004 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** We have designed a decision tree learning algorithm for the text categorization. The set of atributes is based on the keywords, the contents of the glosref tag, and font-change tags.  We searched in the abstract for such attributes to determine whether to select the text or not.       

---
#### UBgtNormJM1 
[**`Results`**](./results.md#ubgtnormjm1), [**`Participants`**](./participants.md#sunybuffalo), [**`Proceedings`**](./proceedings.md#ub-at-trec-13-genomics-track), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.UBgtNormJM1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.UBgtNormJM1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/suny.buffalo.adhoc.table.pdf) 

- :material-rename: **Name:** UBgtNormJM1 
- :fontawesome-solid-user-group: **Participant:** suny.buffalo 
- :material-email: **Email:** meruiz [at] buffalo [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** Document indexing  Language models using linear interpolation smoothing, Query construction  topic expanded with NLM's MetaMap, common phrases discarded before retrieval.  

---
#### UIowaGN1 
[**`Results`**](./results.md#uiowagn1), [**`Participants`**](./participants.md#uiowa), [**`Proceedings`**](./proceedings.md#novelty-question-answering-and-genomics-the-university-of-iowa-response), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.UIowaGN1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.UIowaGN1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.iowa.adhoc.table.pdf) 

- :material-rename: **Name:** UIowaGN1 
- :fontawesome-solid-user-group: **Participant:** u.iowa 
- :material-email: **Email:** padmini-srinivasan [at] uiowa [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/16/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:**         We use all fields in the topics.  We automatically expand synonyms using LocusLink.  We then conduct retrieval using Lucy/Zettair search engine and rank documents by relevance score.  Phrases are in the queries. 

---
#### utaauto 
[**`Results`**](./results.md#utaauto), [**`Participants`**](./participants.md#utampere), [**`Proceedings`**](./proceedings.md#trec-2004-genomics-track-experiments-at-uta-the-effects-of-primary-keys-bigram-phrases-and-query-expansion-on-retrieval-performance), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.utaauto.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.utaauto.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.tampere.adhoc.table.pdf) 

- :material-rename: **Name:** utaauto 
- :fontawesome-solid-user-group: **Participant:** u.tampere 
- :material-email: **Email:** pirkola [at] cc [dot] jyu [dot] fi 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/7/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** -InQuery retrieval system -Title, Abstract, MH, RN, and GS  fields indexed -Text- and MH-field based retrieval -Removal of non-topic words from the  topics using average term frequency  statistics -Identification of phrases in topics  using a collocation method -Pseudorelevance feedback – MH terms  added to the first queries -Weighting of query keys whose  document frequency is low (structural  weighting) 

---
#### utamanu 
[**`Results`**](./results.md#utamanu), [**`Participants`**](./participants.md#utampere), [**`Proceedings`**](./proceedings.md#trec-2004-genomics-track-experiments-at-uta-the-effects-of-primary-keys-bigram-phrases-and-query-expansion-on-retrieval-performance), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.utamanu.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.utamanu.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.tampere.adhoc.table.pdf) 

- :material-rename: **Name:** utamanu 
- :fontawesome-solid-user-group: **Participant:** u.tampere 
- :material-email: **Email:** pirkola [at] cc [dot] jyu [dot] fi 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/10/2004 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** -InQuery retrieval system  -Title, Abstract, MH, RN, and GS fields  indexed  -Text- and MH-field based retrieval -The formulation of Boolean queries -New terms from MeSH, genome databases,  and dictionaries -Queries were reformulated using MH  terms from the top documents of the  initial search   

---
#### uwmtDg04n 
[**`Results`**](./results.md#uwmtdg04n), [**`Participants`**](./participants.md#uwaterlooclarke), [**`Proceedings`**](./proceedings.md#domain-specific-synonym-expansion-and-validation-for-biomedical-information-retrieval-multitext-experiments-for-trec-2004), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.uwmtDg04n.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.uwmtDg04n.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.waterloo.clarke.adhoc.table.pdf) 

- :material-rename: **Name:** uwmtDg04n 
- :fontawesome-solid-user-group: **Participant:** u.waterloo.clarke 
- :material-email: **Email:** sbuettch [at] uwaterloo [dot] ca 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** From the initial topic, after the removal of stopwords, we have created a plain query (without any expansions) and an expanded query that used data from the Medstract project, LocusLink and the EuGenes database to find acronym expansions and aliases/synonyms for gene names and proteins. We have run these two queries and analyzed the top documents returned in order to validate the possible expansions found in the databases and to find additional terms resulting from permutations of terms (such as "nf.kappa.b" and "kappa.b.nf"). In the second pass, we have run the resulting query (validated expansions/aliases) and scored the documents using Okapi. For the third pass, we computed additional expansion terms based on statistical feedback (obtained by analyzing the top documents returned) and Google feedback (analyzing the passages for the top 20 documents returned by Google for the unexpanded "need-only" query). We then executed the query (expanded by the feedback terms) and scored the documents using Okapi. In the last pass, we used the species names found in the topic to re-rank the documents. In general, if, for instance, "mice" occurs in the need of a topic, all documents containing "mouse", "mice", or "mus.musculus" are getting a better rank.  

---
#### uwmtDg04tn 
[**`Results`**](./results.md#uwmtdg04tn), [**`Participants`**](./participants.md#uwaterlooclarke), [**`Proceedings`**](./proceedings.md#domain-specific-synonym-expansion-and-validation-for-biomedical-information-retrieval-multitext-experiments-for-trec-2004), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.uwmtDg04tn.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.uwmtDg04tn.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.waterloo.clarke.adhoc.table.pdf) 

- :material-rename: **Name:** uwmtDg04tn 
- :fontawesome-solid-user-group: **Participant:** u.waterloo.clarke 
- :material-email: **Email:** sbuettch [at] uwaterloo [dot] ca 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/15/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** From the initial topic, after the removal of stopwords, we have created a plain query (without any expansions) and an expanded query that used data from the Medstract project, LocusLink and the EuGenes database to find acronym expansions and aliases/synonyms for gene names and proteins. We have run these two queries and analyzed the top documents returned in order to validate the possible expansions found in the databases and to find additional terms resulting from permutations of terms (such as "nf.kappa.b" and "kappa.b.nf"). In the second pass, we have run the resulting query (validated expansions/aliases) and scored the documents using Okapi. For the third pass, we computed additional expansion terms based on statistical feedback (obtained by analyzing the top documents returned) and Google feedback (analyzing the passages for the top 20 documents returned by Google for the unexpanded "need-only" query). We then executed the query (expanded by the feedback terms) and scored the documents using Okapi. In the last pass, we used the species names found in the topic to re-rank the documents. In general, if, for instance, "mice" occurs in the need of a topic, all documents containing "mouse", "mice", or "mus.musculus" are getting a better rank.  

---
#### wdtriage1 
[**`Results`**](./results.md#wdtriage1), [**`Participants`**](./participants.md#indianauyang), [**`Proceedings`**](./proceedings.md#widit-in-trec-2004-genomics-hard-robust-and-web-tracks), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.wdtriage1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.wdtriage1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/indiana.u.yang.triage.table.pdf) 

- :material-rename: **Name:** wdtriage1 
- :fontawesome-solid-user-group: **Participant:** indiana.u.yang 
- :material-email: **Email:** kiyang [at] indiana [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/30/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** triage 
- :material-text: **Run description:** Categorizing by Rainbow with Bayes   

---
#### wdvqlx1 
[**`Results`**](./results.md#wdvqlx1), [**`Participants`**](./participants.md#indianauyang), [**`Proceedings`**](./proceedings.md#widit-in-trec-2004-genomics-hard-robust-and-web-tracks), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.wdvqlx1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.wdvqlx1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/indiana.u.yang.adhoc.table.pdf) 

- :material-rename: **Name:** wdvqlx1 
- :fontawesome-solid-user-group: **Participant:** indiana.u.yang 
- :material-email: **Email:** kiyang [at] indiana [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/16/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** query expansion with nouns and phrases 

---
#### wdvqlxa1 
[**`Results`**](./results.md#wdvqlxa1), [**`Participants`**](./participants.md#indianauyang), [**`Proceedings`**](./proceedings.md#widit-in-trec-2004-genomics-hard-robust-and-web-tracks), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.wdvqlxa1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.wdvqlxa1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/indiana.u.yang.adhoc.table.pdf) 

- :material-rename: **Name:** wdvqlxa1 
- :fontawesome-solid-user-group: **Participant:** indiana.u.yang 
- :material-email: **Email:** kiyang [at] indiana [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/16/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** query expansion with Gene Ontology synonyms, nouns, and phrases 

---
#### wiscW 
[**`Results`**](./results.md#wiscw), [**`Participants`**](./participants.md#uwisconsin), [**`Proceedings`**](./proceedings.md#exploiting-zone-information-syntactic-rules-and-informative-terms-in-gene-ontology-annotation-of-biomedical-documents), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.wiscW.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.wiscW.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.wisconsin.annhi.table.pdf) 

- :material-rename: **Name:** wiscW 
- :fontawesome-solid-user-group: **Participant:** u.wisconsin 
- :material-email: **Email:** bsettles [at] cs [dot] wisc [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/20/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Statistical model using words only as features. 

---
#### wiscWR 
[**`Results`**](./results.md#wiscwr), [**`Participants`**](./participants.md#uwisconsin), [**`Proceedings`**](./proceedings.md#exploiting-zone-information-syntactic-rules-and-informative-terms-in-gene-ontology-annotation-of-biomedical-documents), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.wiscWR.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.wiscWR.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.wisconsin.annhi.table.pdf) 

- :material-rename: **Name:** wiscWR 
- :fontawesome-solid-user-group: **Participant:** u.wisconsin 
- :material-email: **Email:** bsettles [at] cs [dot] wisc [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/20/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Statistical model using words plus learned syntactic/contextual rules as features. 

---
#### wiscWRT 
[**`Results`**](./results.md#wiscwrt), [**`Participants`**](./participants.md#uwisconsin), [**`Proceedings`**](./proceedings.md#exploiting-zone-information-syntactic-rules-and-informative-terms-in-gene-ontology-annotation-of-biomedical-documents), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.wiscWRT.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.wiscWRT.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.wisconsin.annhi.table.pdf) 

- :material-rename: **Name:** wiscWRT 
- :fontawesome-solid-user-group: **Participant:** u.wisconsin 
- :material-email: **Email:** bsettles [at] cs [dot] wisc [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/20/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Statistical model using words, learned syntactic rules, and induced GO-specific terms as features. 

---
#### wiscWT 
[**`Results`**](./results.md#wiscwt), [**`Participants`**](./participants.md#uwisconsin), [**`Proceedings`**](./proceedings.md#exploiting-zone-information-syntactic-rules-and-informative-terms-in-gene-ontology-annotation-of-biomedical-documents), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.wiscWT.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.wiscWT.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/u.wisconsin.annhi.table.pdf) 

- :material-rename: **Name:** wiscWT 
- :fontawesome-solid-user-group: **Participant:** u.wisconsin 
- :material-email: **Email:** bsettles [at] cs [dot] wisc [dot] edu 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 8/20/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** annhi 
- :material-text: **Run description:** Statistical model using words plus induced GO-specific terms as features. 

---
#### york04g1 
[**`Results`**](./results.md#york04g1), [**`Participants`**](./participants.md#yorku), [**`Proceedings`**](./proceedings.md#york-university-at-trec-2004-hard-and-genomics-tracks), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.york04g1.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.york04g1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/york.u.adhoc.table.pdf) 

- :material-rename: **Name:** york04g1 
- :fontawesome-solid-user-group: **Participant:** york.u 
- :material-email: **Email:** jhuang [at] yorku [dot] ca 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/16/2004 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** 1. Retrieval using probability model 2. Weighting using BM25 3. Indexing using Okapi2.31 4. Relevance feedback using Okapi 5. Using machine learning techniques for query expansion   

---
#### york04g2 
[**`Results`**](./results.md#york04g2), [**`Participants`**](./participants.md#yorku), [**`Proceedings`**](./proceedings.md#york-university-at-trec-2004-hard-and-genomics-tracks), [**`Input`**](https://trec.nist.gov/results/trec13/genomics/input.york04g2.gz), [**`Summary`**](https://trec.nist.gov/results/trec13/genomics/summary.york04g2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec13/appendices/genomics/york.u.adhoc.table.pdf) 

- :material-rename: **Name:** york04g2 
- :fontawesome-solid-user-group: **Participant:** york.u 
- :material-email: **Email:** jhuang [at] yorku [dot] ca 
- :material-format-text: **Track:** Genomics 
- :material-calendar: **Year:** 2004 
- :material-upload: **Submission:** 7/16/2004 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** adhoc 
- :material-text: **Run description:** 1. Retireval using probabilistic model 2. Weighting using BM25 3. Indexing using Okapi2.31 4. Relevance feedback using Okapi 5. Using machine learning techniques for query expansion 

---
