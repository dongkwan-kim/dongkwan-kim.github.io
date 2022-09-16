---
permalink: /
title: "About"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a fourth-year Ph.D. student at [KAIST School of Computing](https://cs.kaist.ac.kr/), advised by [Alice Oh](https://aliceoh9.github.io/). My research interests are in developing graph neural networks for various domains: social networks, codes, or chemicals. In particular, I focus on (1) leveraging the inherent information in the graph structure (e.g., edges, subgraphs) and (2) analyzing the model performance by characteristics of graph datasets (e.g., homophily, average degree, or density).

## Recent Publications

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

- Reviewer: ICLR ([2020](https://iclr.cc/Conferences/2020), [2022](https://iclr.cc/Conferences/2022/Reviewers)), ICML GRL+ Workshop ([2020](https://grlplus.github.io/pcom/)), ACL ARR ([2021](https://openreview.net/group?id=aclweb.org/ACL/ARR/2021)), ICLR GTRL Workshop ([2022](https://gt-rl.github.io/)), NeurIPS ([2022](https://neurips.cc/Conferences/2022)), LoG ([2022](https://logconference.org/))
- Student volunteer: ICLR Social ML in Korea ([2020](https://twitter.com/aliceoh/status/1256032213226815488)), ICLR ([2021](https://iclr.cc/Conferences/2021/Volunteers))
- Organizer: KAIST AI Workshop ([21/22](https://mars-ai.github.io/kaist-ai-workshop-2122))
- Contributor: KAIST ILP Tech ([March 2022](https://ilp.kaist.ac.kr/ebook/220325/index.html))

## Teaching Experiences

- TA, Head TA of Data Structure (Spring 2018, Fall 2018)
- Head TA, TA of Machine Learning for Natural Language Processing ([Fall 2019](https://aliceoh9.github.io/mlnlp), [Spring 2021](https://uilab-kaist.github.io/cs475-mlnlp-spring-2021/)), *Best TA Award at Fall 2019*
- Head TA of Deep Learning for Real-world Problems ([Spring 2020](https://cs.kaist.ac.kr/board/view?bbs_id=news&bbs_sn=9172&menu=83), [Fall 2020](https://docs.google.com/document/d/1SC3-pOZMqrObRbWusZCag9XYHHbKQ1gQQ1bEF_OOxbY)), *Best TA Award at Spring 2020*

## Open Source Contributions

- [PyG (PyTorch Geometric): Graph Neural Network Library for PyTorch](https://github.com/pyg-team/pytorch_geometric/graphs/contributors)

