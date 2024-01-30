# Overview - Clinical Decision Support 2015

[`Proceedings`](./proceedings.md), [`Data`](./data.md), [`Results`](./results.md), [`Runs`](./runs.md), [`Participants`](./participants.md)

{==

In making clinical decisions, physicians often seek out information about how to best care for their patients. Information relevant to a physician can be related to a variety of clinical tasks such as (i) determining a patient’s most likely diagnosis given a list of symptoms, (ii) determining if a particular test is indicated for a given situation, and (iii) deciding on the most effective treatment plan for a patient having a known condition. In some cases, physicians can find the information they seek in published biomedical literature. However, given the volume of the existing literature and the rapid pace at which new research is published, locating the most relevant and timely information for a particular clinical need can be a daunting and timeconsuming task. In order to make biomedical information more accessible and to meet the requirements for the meaningful use of electronic health records (EHRs), a goal of modern clinical decision support systems is to anticipate the needs of physicians by linking EHRs with information relevant for patient care. The goal of the 2015 TREC Clinical Decision Support (CDS) track was to evaluate biomedical literature retrieval systems for providing answers to generic clinical questions about patient cases. Short case reports, such as those published in biomedical articles and used in medical lectures, acted as idealized representations of medical records. A case report typically describes a challenging medical case. It is organized as a well-formed narrative summarizing the pertient portions of the patient’s medical record. Given a case, participants were challenged with retrieving full-text biomedical articles relevant for answering questions related to one of three generic clinical information needs. The three needs were: Diagnosis (i.e., “What is this patient’s diagnosis?”), Test (“What diagnostic test is appropriate for this patient?”), and Treatment (“What treatment is appropriate for this patient?”). Retrieved articles were judged relevant if they provided information of the specified type useful for the given case. The assessment was performed by physicians with training in biomedical informatics. The evaluation of individual submissions followed standard TREC procedures. The 2015 CDS track differed from the 2014 CDS track (Simpson et al., 2014) by offering two tasks. Task A mirrored the 2014 CDS track, only with 30 new topics/cases. Task B used the same topics from Task A, but included the patient diagnosis for the Test and Treatment topics. Since the diagnosis was not guaranteed to be written in the case (consistent with how physicians often write cases in practice), we theorized that providing the diagnosis may improve retrieval systems by (a) providing additional relevant information if the diagnosis is not stated in the case, or (b) emphasizing a key piece of information in the case if the diagnosis is stated.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Kirk Roberts, U.S. National Library of Medicine (NIH) 
- Matthew S. Simpson, U.S. National Library of Medicine (NIH) 
- Ellen M. Voorhees, National Institute of Standards and Technology (NIST) 
- William R. Hersh, Oregon Health and Science University 

:material-text-search: **Tasks:**

- `a`: Task A 
- `b`: Task B 

:fontawesome-solid-globe: **Track Web Page:** [`http://www.trec-cds.org/`](http://www.trec-cds.org/) 

---

