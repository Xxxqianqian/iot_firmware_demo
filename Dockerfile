FROM eclipse-temurin:8-jdk

RUN apt-get update && \
    apt-get install -y \
    ant \
    gcc-arm-none-eabi \
    libnewlib-arm-none-eabi \
    python3 \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

CMD ["ant", "-f", "build.xml"]