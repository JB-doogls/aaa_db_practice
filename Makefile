IIDFILE:=.iidfile
DOCKER_IMG="$$(cat "$(IIDFILE)")"

ifeq ($(OS), Windows_NT)
		DOCKER_CMD=powershell docker run --rm -v "$${pwd}:/app" -e "DOCKER_UID=1001" -e "DOCKER_GID=1001" --entrypoint="./entrypoint.sh" --workdir="/app" --init -t
else
	DOCKER_CMD=docker run --rm -v "$$(pwd):/app" \
			-e "DOCKER_UID=$$(id -u)" \
		-e "DOCKER_GID=$$(id -g)" \
		-e "TEST=$(TEST)" \
		--entrypoint="./entrypoint.sh" \
		--workdir="/app" \
		--init -t
endif

vendor:
	python3 -m pip install -r requirements.txt

docker:
	docker build --iidfile "$(IIDFILE)" .

run: docker
	$(DOCKER_CMD) -i $(DOCKER_IMG) bash
