---
selected: '1.0'
title: 'PertReasonQA: A Knowledge-Grounded Benchmark and Framework for Cell-State–Conditioned Mechanistic Reasoning of Perturbation Effects'
authors: 'Dongkwan Kim, Yiming Gao, Yining Yang, Yang Shen'
collection: 'publications'
permalink: '/publications/2026-07-icml-fm4ls'
date: '2026-07-01'
venue: 'Workshop on Multi-modal Foundation Models and Large Language Models for Life Sciences at ICML (ICML FM4LS)'
type: 'workshop'
summary: '*One-sentence Summary: We propose PertReasonQA, a knowledge-grounded QA benchmark designed to evaluate how models mechanistically reason through cell-state-specific perturbation effects by leveraging causal pathways.*'
venueurl: 'https://fm4ls.github.io/index.html'
paperurl: 'https://openreview.net/forum?id=ALWkvFC0O1'
---

Evaluating machine learning in scientific domains requires separating correct predictions from correct reasons under distribution shifts. We introduce PertReasonQA, a knowledge‑grounded benchmark for cell‑state--conditioned reasoning about perturbation effects. It tests whether models can generate mechanistically faithful explanations and assesses their robustness against complex shifts, such as new cells and unseen perturbations. PertReasonQA combines multiple single‑cell genetic and chemical perturbation data with knowledge graphs, and dynamically conditions pathways on cell‑specific basal states to avoid generic memorization. Evaluations on state-of-the-art models reveal systematic gaps between outcome prediction and mechanistic reasoning, exhibiting failure modes invisible to standard benchmarks. As a reference probe, we present PertReasonLM, a large language model that aligns outcome predictions with context-specific regulatory reasoning. PertReasonQA thus provides a rigorous diagnostic benchmark for studying faithful, generalizable reasoning in data-rich scientific systems.
