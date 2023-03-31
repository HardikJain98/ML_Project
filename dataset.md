---
layout: page
title: Dataset
permalink: /dataset
nav_order: 3
---

# Core Temperature Estimation of Electric Vehicle Battery Packs

## Dataset
<br/>

The dataset for this project is available [here](https://ieee-dataport.org/open-access/battery-and-heating-data-real-driving-cycles). These data were collected as part of a research effort on recuperation of thermal energy in EVs [8]. A vehicle (BMW i3) was specially-instrumented, and high-resolution time-series measurements of 48 quantities (features) were collected over 72 trips with the vehicle. The trips were each of a different duration, made in different geographical regions, and made during different seasons. Though this research effort is unrelated to battery temperature estimation, a subset of the collected data is suitable for our purposes, as the vehicle’s battery pack was specially instrumented to measure temperature as part of this research. The measurement data is split across 70 files. When combined, the dataset comprises of 1,094,793 observations, where each observation represents a set of (up to) 48 feature measurements at a single time instant (i.e. samples of the time-series). The dataset is largely clean, but has a significant amount of missing data.
