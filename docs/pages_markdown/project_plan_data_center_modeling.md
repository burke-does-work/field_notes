---
title: "Project Plan: Data Center Energy Demand Drivers"
date: "2025-12-21"
tags: ["Energy", "Data Centers"]
---

# Project Plan: Data Center Energy Demand Drivers

![Energy via photosynthesis](../static/media/decrepid_data_center.jpg)

## Overview

There are many forecasts for data center energy demand. Most, if not all, of the fundamental-based models use company announcements and utility interconnection requests to derive energy demand.

This project develops an architecture to forecast future energy demand from data centers based on data center infrastructure design.

Data center design is the driver of energy demand, not a utility interconnection queue.

## Approach

Determine data center power demand based on key drivers, such as:

- Chip specs/generation
- Chip utiliziation
- Data center light & power

By going a layer deeper, the user can flex the drivers in key ways:

- Data center infrastructure specialization, i.e. CPU, GPU, or storage 
- Evolution of chip and support infrastructure energy efficiency over time

### Benchmarking

The standard approach to data center energy modeling is to take the utility interconnection queue and moderate it down based on the expectations for interconnection and utilization over time.

Or, to aggregate regional outlooks as published governments and NGOs, regardless of inconsistencies across forecasts.

Issues with this approach:

This approach is useful but limited. With this approach, it's hard to build in a picture of the evolution of AI and compute over time. It tends towards a binary discussion on whether or not data center build will happen.

An interconnection-based forecast quantifies the demand, which is miles better than the mind-numbing punditry on whether we are in a bubble or not.

But in the end, data center build is happening, it's just a matter of what it'll look like over time.

## Starting point

Primary focus for MVP: Research energy demand by data center infrastructure types.

Secondary focus but necessary: Aggregate regional capacity build data.

Base data is required to build out the model, but the focus for the initial product is on the relationship of the drivers in the framework.

## Work structure

**TBD**. Throwing stuff down so there's something:

The build-out will take awhile so perhaps best to publish research findings as the model develops.

Delivery cadence: **TBD**
First checkpoint: **TBD**

Signals to look for to change direction: **TBD**

## Success looks like

The final product will likely be a platform where data and assumptions can be loaded and updated.
