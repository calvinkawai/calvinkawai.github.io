---
tags:
  - cs
  - backend
  - algorithm
links:
  - "[[020 CS]]"
created: 2024-06-12
title: Rest API
---

### Terminology

**API** is a set of rules or protocols that enable softwares application to communicate with each other to exchange data

**REST** is a software architectural pattern that defines a set of constrains.

**RESTful API** delivers information of in one of following format, HTML, Json, PHP, Plain Text via http request.

### Constrains

**A Client-Server Architecture**
- client requests resources from server via http
**Statelessness**
- each request is independent
**Cacheable**
- data requested from server side can be stored in client browser, CDN etc
**A Uniform Interface**
- resources requested group by identity (URI)
```
URI         = scheme ":" hier-part [ "?" query ] [ "#" fragment ]

hier-part   = "//" authority path-abempty
	  / path-absolute
	  / path-rootless
	  / path-empty
```
- resources can be manipulated via representation they receive
- self-descriptive messages returned to client should have enough information to describe how client should process it
- hypertext/hypermedia is available, client can find related actions after accessing a resource
 **A layered System**
- client does not need to know how server works for those responsible to authorization, load-balancing, API gateway etc.

### When to use REST API

If your applications require simple and standard API, can leverage http caching, and consistent data requirements.

Examples:
- Cloud Application - due to it is stateless nature, rest api can be easily scaled, and if some component fails, we can easily redeploy without needing to remember previous state of the application
- Web Application - since REST is client server architecture, APIs can be accessible from wide variety of clients, such as browser, IoT device, mobile etc.


### Design Process

`Object Modelling -> Create Resources URIs -> Resources Representations -> Assign Http request`

In a simple blog application, we will have two main resources, author and blog. Let's first create these two resources URIs. Assume each resource has unique id as integer. In production, we can mask the or using UUID.

```
/authors
/authors/{authorId}

/authors/{authorId}/blogs
/authors/{authorId}/blogs/{blogId}

/blogs
/blogs/{blogId}
```

Some common patterns,

Retriever Blog by id
`GET /blogs/{blogId}`

List all blogs
`GET /blogs`

List blogs with pagination
`GET /blogs?page={page}&limit={limit}`

List blogs given a date
`GET /blogs?date={YYYY-MM-DD}`

Filter blogs between dates
`GET /blogs?startDate={YYYY-MM-DD}&endDate={YYYY-MM-DD}`


---
Reference:

1. [Rest API best practice](https://github.com/PragatiVerma18/Django-For-APIs/blob/master/Best-Practices-In-REST.md)
2. [Why is restful api so popular - Bytebytego](https://blog.bytebytego.com/p/why-is-restful-api-so-popular)
3. [REST, HATEOAS & Django - It's OK to not use JSON... or Javascript - Carson Gross](https://www.youtube.com/watch?v=L_UWY-zHlOA&ab_channel=DjangoConUS)
4. [HATEOAS - Carson Gross](https://htmx.org/essays/hateoas/)
5. [URI - Roy T. Fielding](https://www.ietf.org/rfc/rfc3986.txt)
6. [Rest API design example](https://restfulapi.net/rest-api-design-tutorial-with-example/)
