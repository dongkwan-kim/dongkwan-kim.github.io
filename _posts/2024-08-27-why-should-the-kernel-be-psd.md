---
title: 'Why Should the Kernel Be Positive Semi-Definite?'
date: 2024-08-27
permalink: /blogs/psd-kernels/
tags:
  - Machine Learning Research
summary: ""
---

1. In Principle: According to [Mercer's Theorem](https://en.wikipedia.org/wiki/Mercer%27s_theorem), if a function $ k(x,y) $ is positive semi-definite, it can be represented as an inner product in some Hilbert space. This is important in machine learning, where kernel functions act similarly to inner products in a feature space. For example, in Support Vector Machines (SVMs) and other kernel methods, data is often mapped into a higher-dimensional space where a linear classifier or regressor is applied. The kernel function must be positive semi-definite to ensure that it behaves like an inner product in this space.

2. In Practice: When the kernel matrix is positive semi-definite, the optimization process is more stable. For instance, ["Soft margin SVM is a convex optimization problem only if kernel matrices are positive semidefinite"](https://mseeger.github.io/files/pcml_notes.pdf#page=169.20). This convexity ensures a global optimum and enhances numerical stability.

These reasons highlight why it is crucial for kernels to satisfy the positive semi-definite condition.
It solidifies the mathematical foundation of kernel methods and ensures stable learning. 