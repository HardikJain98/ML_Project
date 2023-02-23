---
layout: page
title: Introduction
permalink: /
nav_order: 1
---


## Problem Definition and Motivation
<br/>

**_The project aims to predict the core temperature of an electric vehicle (EV) battery, given standard measurements from sensors on-board the EV._**
<br/><br/>

Core temperature knowledge is critical for ensuring safety, as it enables the detection of thermal runaway, a common failure mode for lithium-ion batteries. Thermal runaway is a vicious cycle of heating, triggered by a spike in core temperature, which in turn, can be triggered by a variety of factors, including high ambient temperature, high load (i.e. sustained aggressive driving), and high-power charging (i.e. fast-charging). Once a battery enters thermal runaway, its temperature increases exponentially, ultimately resulting in explosion and emission of toxic compounds [\[1\]](references).
<br/><br/>

In smaller (gadget) batteries, the easily-measured case temperature is strongly correlated with core temperature [\[2\]](references). However, this is not true of larger EV batteries [\[1, 3\]](references). Though EV batteries’ core temperature can be measured by embedding sensors, it is prohibitively expensive. Consequently, the temperature prediction task is well-motivated.
