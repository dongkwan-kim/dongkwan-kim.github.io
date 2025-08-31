---
selected: ''
title: 'LLM-as-an-Interviewer: Beyond Static Testing Through Dynamic LLM Evaluation'
authors: 'Eunsu Kim, Juyoung Suk, Seungone Kim, Niklas Muennighoff, Dongkwan Kim, Alice Oh'
collection: 'publications'
permalink: '/publications/2025-07-acl'
date: '2025-07-27'
venue: 'Findings of the Association for Computational Linguistics: ACL 2025 (ACL-Findings 2025, Long)'
type: 'conference'
summary: '*One-sentence Summary: We propose a new paradigm for evaluating large language models (LLMs), called LLM-as-an-Interviewer.*'
venueurl: 'https://2025.aclweb.org/'
arxivurl: 'https://arxiv.org/abs/2412.10424'
codeurl: 'https://github.com/interview-eval/interview-eval'
---

We introduce LLM-as-an-Interviewer, a novel paradigm for evaluating large language models (LLMs). This approach leverages multi-turn interactions where the LLM interviewer actively provides feedback on responses and poses follow-up questions to the evaluated LLM. At the start of the interview, the LLM interviewer dynamically modifies datasets to generate initial questions, mitigating data contamination. We apply the LLM-as-an-Interviewer framework to evaluate six models on the reasoning, factuality and instruction-following tasks. Our results show that the framework effectively provides insights into LLM performance, including the quality of initial responses, adaptability to feedback, and ability to address follow-up queries like clarification or additional knowledge requests. The framework also addresses key limitations of conventional methods like LLM-as-a-Judge, including verbosity bias and inconsistency across runs. Finally, we propose the Interview Report, which aggregates insights from the interview process, providing examples and a comprehensive analysis of the LLM’s strengths and weaknesses. This report offers a detailed snapshot of the model's real-world applicability.