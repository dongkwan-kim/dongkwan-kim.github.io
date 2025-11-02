---
selected: ''
title: 'MUG-Eval: A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language'
authors: 'Seyoung Song, Seogyeong Jeong, Eunsu Kim, Jiho Jin, Dongkwan Kim, Jay Shin, Alice Oh'
collection: 'publications'
permalink: '/publications/2025-11-emnlp'
date: '2025-11-04'
venue: 'Findings of the Empirical Methods in Natural Language Processing: EMNLP 2025 (EMNLP-Findings 2025, Long)'
type: 'conference'
summary: '*One-sentence Summary: A language-agnostic framework that evaluates LLM multilingual generation by measuring task completion rates in self-communication scenarios, enabling objective assessment across 2,100+ languages without requiring language-specific tools or humans.*'
venueurl: 'https://2025.emnlp.org/'
paperurl: 'https://aclanthology.org/2025.findings-emnlp.1061/'
arxivurl: 'https://arxiv.org/abs/2505.14395'
codeurl: 'https://github.com/seyoungsong/mugeval'
---

Evaluating text generation capabilities of large language models (LLMs) is challenging, particularly for low-resource languages where methods for direct assessment are scarce. We propose MUG-Eval, a novel framework that evaluates LLMs' multilingual generation capabilities by transforming existing benchmarks into conversational tasks and measuring the LLMs' accuracies on those tasks. We specifically designed these conversational tasks to require effective communication in the target language. Then, we simply use task success rate as a proxy of successful conversation generation. Our approach offers two key advantages: it is independent of language-specific NLP tools or annotated datasets, which are limited for most languages, and it does not rely on LLMs-as-judges, whose evaluation quality degrades outside a few high-resource languages. We evaluate 8 LLMs across 30 languages spanning high, mid, and low-resource categories, and we find that MUG-Eval correlates strongly with established benchmarks (r > 0.75) while enabling standardized comparisons across languages and models. Our framework provides a robust and resource-efficient solution for evaluating multilingual generation that can be extended to thousands of languages.