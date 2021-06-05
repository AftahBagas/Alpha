# alfareza

. init/logbot/logbot.sh
. init/proc.sh
. init/utils.sh
. init/checks.sh

trap 'handleSig SIGHUP' HUP
trap 'handleSig SIGTERM' TERM
trap 'handleSig SIGINT' INT
trap '' USR1

handleSig() {
    log "Exiting With $1 ..."
    killProc
}

initUserge() {
    printLogo
    assertPrerequisites
    sendMessage "Initializing Alpha ..."
    assertEnvironment
    editLastMessage "Starting Alpha ..."
    printLine
}

startUserge() {
    startLogBotPolling
    runPythonModule alpha "$@"
    waitProc
}

stopUserge() {
    sendMessage "Exiting Alpha ..."
    endLogBotPolling
}

runUserge() {
    initAlpha
    startAlpha "$@"
    local code=$?
    stopAlpha
    return $code
}
