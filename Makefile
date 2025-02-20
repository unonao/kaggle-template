CPU_FLAG :=
ifneq ($(CPU),)
    CPU_FLAG := -f compose.CPU.yaml
endif

default: build

build:
	docker compose $(CPU_FLAG) build

bash:
	docker compose $(CPU_FLAG) run --rm kaggle bash

jupyter:
	docker compose $(CPU_FLAG) up

down:
	docker compose $(CPU_FLAG) down