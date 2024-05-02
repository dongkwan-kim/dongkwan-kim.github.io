---
permalink: /
title: "About"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a Ph.D. student at the [KAIST](https://www.kaist.ac.kr/en) [School of Computing](https://cs.kaist.ac.kr), advised by [Alice Oh](https://aliceoh9.github.io/). My research interests are in learning representations of structured and unstructured knowledge. In particular, I have focused on (1) leveraging the inherent structures (e.g., edges and subgraphs) to learn graph-structured data [[C2](https://openreview.net/forum?id=Wi5KUNlqWty), [C3](https://dl.acm.org/doi/10.1145/3511808.3557647)] and (2) designing a new data structure for efficient representation learning of subgraphs [[C4](https://arxiv.org/abs/2204.04510), [W3](https://openreview.net/forum?id=BgLaE-k6gc)].

## Recent Publications ([See all](/publications))

{% assign reversed_publications = site.publications | reverse %}
{% for post in reversed_publications limit:7 %}
{% include archive-short-publications.html %}
{% endfor %}

## Education

- M.S. School of Computing, *KAIST*, Sep 2019
- B.S. Major in Computer Science and Minor in Chemistry, *KAIST*, Feb 2018

## Talks

{% assign reversed_talks = site.talks | reverse %}
{% for post in reversed_talks limit:7 %}
{% include archive-short-talks.html %}
{% endfor %}

## Academic Services

- Reviewer: ICLR ([2020](https://iclr.cc/Conferences/2020), [2022](https://iclr.cc/Conferences/2022/Reviewers), [2024](https://iclr.cc/Conferences/2024/Reviewers)), GRL+ Workshop ([2020](https://grlplus.github.io/pcom/)), ACL ARR ([2021](https://openreview.net/group?id=aclweb.org/ACL/ARR/2021)), GTRL Workshop ([2022](https://gt-rl.github.io/)), NeurIPS ([2022](https://neurips.cc/Conferences/2022/ProgramCommittee), [2023](https://neurips.cc/Conferences/2023/ProgramCommittee)), LoG ([2022](http://log2022.logconference.org/program-committee/), [2023](https://logconference.org/)), ICML ([2023](https://icml.cc/Conferences/2023/Reviewers)), GLB Workshop ([2023](https://graph-learning-benchmarks.github.io/glb2023#program-committee))
- Student volunteer: ICLR Social ML in Korea ([2020](https://twitter.com/aliceoh/status/1256032213226815488)), ICLR ([2021](https://iclr.cc/Conferences/2021/Volunteers)), NeurIPS 2022 at KAIST ([2022](https://www.facebook.com/alice.oh1/posts/pfbid0LEXJrzMfSikhWFkNZG1zc8H9AUDeWjRfiiTChF5BN85wgikuom1ALbgxUiJjkvxxl)), NYU-KAIST Talk Series on LMs ([2023](https://www.youtube.com/playlist?list=PLgJQ1dsC4sffmGYTPeR3AC0T-UeXjgDCl))
- Organizer: KAIST AI Workshop ([21/22](https://mars-ai.github.io/kaist-ai-workshop-2122))
- Contributor: KAIST ILP Tech ([March 2022](https://ilp.kaist.ac.kr/ebook/220325/index.html))

## Teaching Experiences

- TA, Head TA of Data Structure (Spring 2018, Fall 2018)
- Head TA, TA of Machine Learning for Natural Language Processing ([Fall 2019](https://aliceoh9.github.io/mlnlp), [Spring 2021](https://uilab-kaist.github.io/cs475-mlnlp-spring-2021/)), *Best TA Award at Fall 2019*
- Head TA of Deep Learning for Real-world Problems ([Spring 2020](https://cs.kaist.ac.kr/board/view?bbs_id=news&bbs_sn=9172&menu=83), [Fall 2020](https://docs.google.com/document/d/1SC3-pOZMqrObRbWusZCag9XYHHbKQ1gQQ1bEF_OOxbY)), *Best TA Award at Spring 2020*

## Open Source Contributions

- [PyG (PyTorch Geometric): Graph Neural Network Library for PyTorch](https://github.com/pyg-team/pytorch_geometric/graphs/contributors)

