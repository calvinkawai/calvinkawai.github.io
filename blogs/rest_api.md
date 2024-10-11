---
tags:
  - cs
  - backend
  - algorithm
links:
  - "[[020 CS]]"
created: 2024-06-12
title: how to design an restful api
---

### Terminology

**API** is a set of rules or protocols that enable softwares application to communicate with each other to exchange data.

**REST** is a software architectural pattern that defines a set of constrains.

**RESTful API** delivers information of in one of following format, HTML, Json, PHP, Plain Text via http request.

### Constrains

A Client-Server Architecture

- client requests resources from server via http

Statelessness

- each request is independent

Cacheable

- data requested from server side can be stored in client, cdn etc

A Uniform Interface

- resources requested group by identity (URI)
- resources can be manipulated via representation they receive
- self-descriptive messages returned to client should have enough information to describe how client should process it
- hypertext/hypermedia is available, client can find related actions after accessing a resource

A layered System

- client does not need to know how server works for those responsible to authorization, load-balancing etc.

### Examples

**Retriever Blog by id**

- **URL Pattern**: `GET /blogs/{blogId}`
- **Example**: `GET /blogs/123`

**List all blogs**

- **URL Pattern**: `GET /blogs`
- **Example**: `GET /blogs`

**List blogs with pagination**

- **URL Pattern**: `GET /blogs?page={page}&limit={limit}`
- **Example**: `GET /blogs?page=2&limit=10`

**List blogs given a date**

- **URL Pattern**: `GET /blogs?date={YYYY-MM-DD}`
- **Example**: `GET /blogs?date=2023-01-01`

**Filter blogs between dates**

- **URL Pattern**: `GET /blogs?startDate={YYYY-MM-DD}&endDate={YYYY-MM-DD}`
- **Example**: `GET /blogs?startDate=2023-01-01&endDate=2023-01-31`

---

Reference:

1. [Rest API best practice](https://github.com/PragatiVerma18/Django-For-APIs/blob/master/Best-Practices-In-REST.md)
2. [Bytebytego - Why is restful api so popular](https://blog.bytebytego.com/p/why-is-restful-api-so-popular)
3. [Carson Gross - REST, HATEOAS & Django - It's OK to not use JSON... or Javascript](https://www.youtube.com/watch?v=L_UWY-zHlOA&ab_channel=DjangoConUS)
4. [Carson Gross - HATEOAS](https://htmx.org/essays/hateoas/)
