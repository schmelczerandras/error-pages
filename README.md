# error-pages

![Deploy everything](https://github.com/schmelczerandras/error-pages/workflows/Deploy%20everything/badge.svg)

Docker baseimage for generating some error pages.

## Usage

### Example Dockerfile

```Dockerfile
FROM schmelczera/error-pages as build-error-pages
RUN python build.py 403 404 50x

FROM nginx:alpine
COPY --from=build-error-pages /home/python/built /usr/share/nginx/html
```
