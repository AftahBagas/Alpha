declare -i bgProc

_addHandler() {
    trap killProc HUP TERM INT
}

_removeHandler() {
    trap - HUP TERM INT
}

setProc() {
    bgProc=$1
}

_waitProc() {
    test $bgProc && wait $bgProc
}

waitProc() {
    _waitProc
    _removeHandler
    _waitProc
}

killProc() {
    test $bgProc && kill -TERM $bgProc &> /dev/null
}

reInitProc() {
    killProc
    waitProc
    _addHandler
}
