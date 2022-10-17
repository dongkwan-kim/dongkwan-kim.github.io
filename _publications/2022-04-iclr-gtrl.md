---
title: 'Efficient Representation Learning of Subgraphs by Subgraph-To-Node Translation'
authors: 'Dongkwan Kim and Alice Oh'
collection: 'publications'
permalink: '/publications/2022-04-iclr-gtrl'
date: '2022-04-29'
venue: 'Workshop on Geometrical and Topological Representation Learning at ICLR (ICLR GTRL)'
type: 'workshop'
summary: '*One-sentence Summary: We propose Subgraph-To-Node translation to efficiently learn representations of subgraphs by coarsely translating subgraphs into nodes.*'
venueurl: 'https://gt-rl.github.io/'
paperurl: 'https://openreview.net/forum?id=BgLaE-k6gc'
arxivurl: 'https://arxiv.org/abs/2204.04510'
---

A subgraph is a data structure that can represent various real-world problems. We propose Subgraph-To-Node (S2N) translation, which is a novel formulation to efficiently learn representations of subgraphs. Specifically, given a set of subgraphs in the global graph, we construct a new graph by coarsely transforming subgraphs into nodes. We perform subgraph-level tasks as node-level tasks through this translation. By doing so, we can significantly reduce the memory and computational costs in both training and inference. We conduct experiments on four real-world datasets to evaluate performance and efficiency. Our experiments demonstrate that models with S2N translation are more efficient than state-of-the-art models without substantial performance decrease.