[![Build Status](https://travis-ci.com/jorge-3/flaskbook.svg?token=CpgTPHGMFe4PoRnkeQqo&branch=master)](https://travis-ci.com/jorge-3/flaskbook)

# Step 1

## What is an API?
API stands for "Application program interface", and it's a set of routines, protocols and tools for building interactions between clients and servers.

## What is REST?
REST stands for "Representational State Transfer" and it has six constraints:
- Uniform interface
- Stateless
- Cacheable
- Client-server
- Layered System
- Code on Demand (optional)

## Uniform interface
- Resource-Based: Individual resources are identified in requests using URIs as resource identifiers. The resources themselves are conceptually separate from the representations that are returned to the client.
- Manipulation of Resources Through Representations: When a client holds a representation of a resource, including any metadata attached, it has enough information to modify or delete the resource on the server, provided it has permission to do so.
- Self-descriptive Messages: Each message includes enough information to describe how to process the message.
- Hypermedia as the Engine of Application State (HATEOAS): Clients deliver state via body contents, query-string parameters, request headers and the requested URI (the resource name). Services deliver state to clients via body content, response codes, and response headers. This is technically referred-to as hypermedia (or hyperlinks within hypertext). The service tells the client about next actions within the response BODY. (HATEOAS is pronounced ha-tee-oss), including available actions. For example an account id GET point might have deposit and withdraw hyperlinks, but only deposit if the account is overdrawn. That is a way to communicate state with hypermedia.

## Stateless
As REST is an acronym for REpresentational State Transfer, statelessness is key. Essentially, what this means is that the necessary state to handle the request is contained within the request itself, whether as part of the URI, query-string parameters, body, or headers.

## Cacheable
Responses must, implicitly or explicitly, define themselves as cacheable, or not, to prevent clients reusing stale or inappropriate data in response to further requests. Well-managed caching partially or completely eliminates some client–server interactions, further improving scalability and performance.

## Client-server
The uniform interface separates clients from servers. This separation of concerns means that, for example, clients are not concerned with data storage, which remains internal to each server, so that the portability of client code is improved. Servers are not concerned with the user interface or user state, so that servers can be simpler and more scalable.

## Layered System
A client cannot ordinarily tell whether it is connected directly to the end server, or to an intermediary along the way. Intermediary servers may improve system scalability by enabling load-balancing and by providing shared caches. Layers may also enforce security policies.

## Code on Demand (optional)
Servers are able to temporarily extend or customize the functionality of a client by transferring logic to it that it can execute. Examples of this may include compiled components such as Java applets and client-side scripts such as JavaScript.
