---
title: 'Black Magic of LaTeX for Limited Spaces'
date: 2022-09-08
permalink: /blogs/black-magic-of-latex-for-limited-spaces/
tags:
  - Others
summary: ""
---

1. `\vspace{-Xcm}`
1. `\renewcommand{\arraystretch}{X}` (for tables, X < 1)
1. `{\small ... }`
1. `\resizebox{\columnwidth}{!}{ ... }`
1. `\newcommand*{\scale}[2][4]{\scalebox{#1}{$#2$}}` + `\scale[X]{ }` (for equations, X < 1)