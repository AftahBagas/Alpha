# alfareza

. init/logbot/logbot.sh
. init/utils.sh
. init/checks.sh

trap handleSigTerm TERM
trap handleSigInt INT

initAlpha() {
    printLogo
    assertPrerequisites
    sendMessage "Initializing Alpha ..."
    assertEnvironment
    editLastMessage "Starting Alpha ..."
    printLine
}

startAlpha() {
    startLogBotPolling
    runPythonModule alphaz "$@"
}

stopAlpha() {
    sendMessage "Exiting Alpha ..."
    endLogBotPolling
    exit 0
}

handleSigTerm() {
    log "Exiting With SIGTERM (143) ..."
    stopAlpha
    exit 143
}

handleSigInt() {
    log "Exiting With SIGINT (130) ..."
    stopAlpha
    exit 130
}

runAlpha() {
    initAlpha
    startAlpha "$@"
    stopAlpha
}
