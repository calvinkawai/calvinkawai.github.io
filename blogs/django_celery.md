---
tags:
  - django
  - python
  - backend
  - "#backlog"
links:
  - "[[020 CS]]"
title: django celery
created: 2024-10-11
---

A Celery task is much like a web view, in that it should only define how to perform the action in the context of being called as a task.


This means optimally tasks only handle things like **serializatio**, **message header**,**retries** and so on, with the actual logic implemented elsewhere.
