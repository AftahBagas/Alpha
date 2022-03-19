# alfareza

import os

from alpha import alpha


async def _worker() -> None:
    chat_id = int(os.environ.get("CHAT_ID") or 0)
    type_ = 'unofficial' if os.path.exists("../alpha/plugins/unofficial") else 'main'
    await alpha.send_message(chat_id, f'`{type_} build completed !`')

if __name__ == "__main__":
    alpha.begin(_worker())
    print('Alpha test has been finished!')
