---
permalink: /
title: "About"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a postdoctoral researcher at [Texas A&M University](https://www.tamu.edu/), working with Prof. [Yang Shen](https://shen-lab.github.io/). My research aims to build foundational models for biology and chemistry that understand and integrate multiple data modalities such as graphs and texts. The goal of my work is to accelerate scientific discovery by enabling AI systems to reason over complex relational and hierarchical structures found in biological, chemical, and biomedical domains.

During my Ph.D. at [KAIST](https://www.kaist.ac.kr/en) [School of Computing](https://cs.kaist.ac.kr), advised by Prof. [Alice Oh](https://aliceoh9.github.io/), I studied representation learning for structured data, focusing on the intersection of graph neural networks (GNNs) and large language models (LLMs). My Ph.D. research contributed to graph representation learning methods that leverage pairwise and higher-order interactions for graph-structured data (edges [[C2](https://openreview.net/forum?id=Wi5KUNlqWty)], partial subgraphs [[C3](https://dl.acm.org/doi/10.1145/3511808.3557647)], subgraphs [[C4](https://arxiv.org/abs/2204.04510)], and k-hop subgraphs [[C6](https://openreview.net/forum?id=HZgZrtIreg)]).

## Selected Publications ([See all](/publications))

{% assign publications = site.publications | sort: "selected" %}
{% for post in publications %}
{% if post.selected != "" %}
{% include archive-short-publications.html %}
{% endif %}
{% endfor %}

## Education

- Ph.D., School of Computing, *KAIST*, Aug 2025
- M.S., School of Computing, *KAIST*, Aug 2019
- B.S., Major in Computer Science and Minor in Chemistry, *KAIST*, Feb 2018

## Talks & Presentations

{% assign reversed_talks = site.talks | reverse %}
{% for post in reversed_talks limit:7 %}
{% include archive-short-talks.html %}
{% endfor %}

## Academic Services

- Reviewer: ICLR ([2026](https://iclr.cc/Conferences/2026/ProgramCommittee#all-reviewer), [2025](https://iclr.cc/Conferences/2025/ProgramCommittee#all-reviewer), [2024](https://iclr.cc/Conferences/2024/Reviewers#all-reviewer), [2022](https://iclr.cc/Conferences/2022/Reviewers), [2020](https://iclr.cc/Conferences/2020)), NeurIPS ([2025](https://neurips.cc/Conferences/2025/ProgramCommittee#all-reviewer), [2024](https://neurips.cc/Conferences/2024/ProgramCommittee#all-reviewers), [2023](https://neurips.cc/Conferences/2023/ProgramCommittee), [2022](https://neurips.cc/Conferences/2022/ProgramCommittee)), ACL ARR ([2024/06](https://openreview.net/group?id=aclweb.org/ACL/ARR/2024/June), [2021/09](https://openreview.net/group?id=aclweb.org/ACL/ARR/2021/September)), LoG ([2023](http://log2023.logconference.org/program-committee/), [2022](http://log2022.logconference.org/program-committee/)), ICML ([2023](https://icml.cc/Conferences/2023/Reviewers)), GLB Workshop ([2023](https://graph-learning-benchmarks.github.io/glb2023#program-committee)), GTRL Workshop ([2022](https://gt-rl.github.io/)), GRL+ Workshop ([2020](https://grlplus.github.io/pcom/))
- Student volunteer: NYU-KAIST Talk Series on LMs ([2023](https://www.youtube.com/playlist?list=PLgJQ1dsC4sffmGYTPeR3AC0T-UeXjgDCl)), NeurIPS 2022 at KAIST ([2022](https://www.facebook.com/alice.oh1/posts/pfbid0LEXJrzMfSikhWFkNZG1zc8H9AUDeWjRfiiTChF5BN85wgikuom1ALbgxUiJjkvxxl)), ICLR ([2021](https://iclr.cc/Conferences/2021/Volunteers)), ICLR Social ML in Korea ([2020](https://twitter.com/aliceoh/status/1256032213226815488))
- Organizer: KAIST AI Workshop ([21/22](https://mars-ai.github.io/kaist-ai-workshop-2122)), International NLP Workshop at KAIST ([2024](https://x.com/aliceoh/status/1822779544555905157))
- Contributor: KAIST ILP Tech ([2022/03](https://ilp.kaist.ac.kr/ebook/220325/index.html))

## Teaching Experiences

- TA of AI Tech Boostcamp at NAVER Connect Foundation ([Fall 2024](https://boostcamp.connect.or.kr/program_ai.html))
- Head TA, TA of Machine Learning for Natural Language Processing ([Spring 2021](https://uilab-kaist.github.io/cs475-mlnlp-spring-2021/), [Fall 2019](https://aliceoh9.github.io/mlnlp)), *Best TA Award at Fall 2019*
- Head TA of Deep Learning for Real-world Problems ([Fall 2020](https://docs.google.com/document/d/1SC3-pOZMqrObRbWusZCag9XYHHbKQ1gQQ1bEF_OOxbY), [Spring 2020](https://cs.kaist.ac.kr/board/view?bbs_id=news&bbs_sn=9172&menu=83)), *Best TA Award at Spring 2020*
- TA, Head TA of Data Structure (Fall 2018, Spring 2018)

## Open Source Contributions

- [PyG (PyTorch Geometric): Graph Neural Network Library for PyTorch](https://github.com/pyg-team/pytorch_geometric/commits?author=dongkwan-kim)

