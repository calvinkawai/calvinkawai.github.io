---
tags:
  - cs
  - django
  - backend
links:
  - "[[020 CS]]"
title: usage of Django apps in scale
created: 2024-10-11
---

## When to create a new app

- most new things should be a new app
- new feature
    - e.g. comments on a blog website
- internal vs external
- multi-part features

## Doordash suggestions for any developers starting a Django project:

- If you don’t really understand the point of apps, ignore them and stick with a single app for your backend. You can still organize a growing codebase without using separate apps.
- If you do want to create separate applications, you will want to be very intentional about how you define them. Be very explicit about and minimize any dependencies between different apps. (If you are planning to migrate to microservices down the line, I can imagine that “apps” might be a useful construct to define precursors to a future microservice).

---

Resources:

1. [Doordash Tips for building high quality django apps at scale](https://doordash.engineering/2017/05/15/tips-for-building-high-quality-django-apps-at-scale/)
2. [Dan Palmer - Scaling Django to 500 apps](https://www.youtube.com/watch?v=NsHo-kThlqI&t=754s&ab_channel=DjangoConUS)
