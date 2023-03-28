DOCKER_USER=docker-user

fail(){
  echo "$@"
  exit 1
}

[ -n "${DOCKER_UID}" ] || fail "Please specify UID."
[ -n "${DOCKER_GID}" ] || fail "Please specify GID."

addgroup --quiet --gid "${DOCKER_GID}" "${DOCKER_USER}" 2>/dev/null ||:
adduser --quiet --uid "${DOCKER_UID}" --ingroup "$(getent group "${DOCKER_GID}" |  cut -d: -f1)" \
    --gecos "${DOCKER_USER}" --disabled-password "${DOCKER_USER}"


setsid pg_ctlcluster 13 main start
runuser -u postgres -- createuser "${DOCKER_USER}"
runuser -u postgres -- createdb "${DOCKER_USER}"

runuser -u postgres -- psql -c "alter role \"${DOCKER_USER}\" superuser"

setsid redis-server >/dev/null 2>&1 &
exec runuser -u "${DOCKER_USER}" -- "$@"

