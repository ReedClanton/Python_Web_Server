# auth

Handles user account management and authentication.

# Build

To build docker container, run the bellow from the repo's root:

```sh
docker buildx build -t auth:<version> src/auth
```

# Run

To launch the application, from the repo's root run:

```sh
docker run -p 5000:5000 auth:1
```

