---
selected: 'False'
title: 'Supervised Graph Attention Network for Semi-Supervised Node Classification'
authors: 'Dongkwan Kim and Alice Oh'
collection: 'publications'
permalink: '/publications/2019-12-neurips-grl'
date: '2019-12-09'
venue: 'Workshop on Graph Representation Learning at NeurIPS (NeurIPS GRL)'
type: 'workshop'
summary: '*Note: The [full version](/publications/2021-05-iclr) is published at ICLR 2021.*'
venueurl: 'https://grlearning.github.io/'
paperurl: 'https://grlearning.github.io/papers/103.pdf'
---

We propose supervised graph attention network  (super-GAT), a novel neural network architecture for semi-supervised node classification in graphs. While learning (unsupervised) graph attention from the original graph attention network (GAT), we jointly train the attention values by supervised learning with information whether an edge exists between a pair of nodes. By giving supervision, we can assign not only implicit weights to nodes in the neighborhood but also explicit weights to nodes in any relation. Our model is based on GAT, and it only needs a few additional parameters and computation. We show how super-GAT performs on three transductive benchmark citation datasets: Cora, CiteSeer, and PubMed, and compared to baseline models including GAT, super-GAT achieves higher prediction accuracy for the first two datasets.