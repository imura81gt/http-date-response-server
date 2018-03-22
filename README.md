http-date-response-server
============================

install serverless framework
----------------------------

* install node.js
* install serverless framework


deploy
----------------------------

### (Option) set AWS_PROFILE

```
$ export AWS_PROFILEa=sandbox
```

### deploy to dev

```
$ sls deploy -v
```

### request & response

#### e.g. HTTPie

request

```
$ http --follow https://<domain>/dev/
$ http --follow https://<domain>/dev/now
```

response

```
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 38
Content-Type: application/json
Date: Thu, 22 Mar 2018 12:57:37 GMT
Via: 1.1 e4404fd3b1d2ac38d3124fbc6bbedc8b.cloudfront.net (CloudFront)
X-Amz-Cf-Id: yBoPlmaBGjNa5oDRlkOgOSfYOkAyK3hRLC1c1Xh7ANFY6b_0t0u6tA==
X-Amzn-Trace-Id: sampled=0;root=1-5ab3a841-7c3e3b0599ec773602888084
X-Cache: Miss from cloudfront
x-amzn-RequestId: 98a8160c-2dd0-11e8-9fe7-3dc0ad372e91

{
    "date": "2018-03-22T12:57:37.271836"
}

```
