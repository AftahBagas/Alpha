# alfareza


class StopConversation(Exception):
    """ raise if conversation has terminated """


class ProcessCanceled(Exception):
    """ raise if thread has terminated """


class AlphaBotNotFound(Exception):
    """ raise if alpha plugins bot not found """
