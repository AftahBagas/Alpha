# Alfareza

from urllib.error import HTTPError

import urbandict

from alpha import alpha, Message


@alpha.on_cmd("ud", about={
    'header': "Searches Urban Dictionary for the query",
    'flags': {'-l': "limit : defaults to 1"},
    'usage': "{tr}ud [flag] [query]",
    'examples': ["{tr}ud alpha", "{tr}ud -l3 alpha"]})
async def urban_dict(message: Message):
    await message.edit("Processing...")
    query = message.filtered_input_str
    if not query:
        await message.err(text="No found any query!")
        return
    try:
        mean = urbandict.define(query)
    except HTTPError:
        await message.err(text=f"Sorry, couldn't find any results for: `{query}``")
        return
    output = ''
    limit = int(message.flags.get('-l', 1))
    for i, mean_ in enumerate(mean, start=1):
        output += f"{i}. **{mean_['def']}**\n" + \
            f"  Examples:\n  * `{mean_['example'] or 'not found'}`\n\n"
        if limit <= i:
            break
    if not output:
        await message.err(text=f"No result found for **{query}**")
        return
    output = f"**Query:** `{query}`\n**Limit:** `{limit}`\n\n{output}"
    await message.edit_or_send_as_file(text=output, caption=query)
