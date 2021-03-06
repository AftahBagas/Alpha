# alfareza

import aiohttp

from alpha import Message, alpha

LOG = alpha.getLogger(__name__)  # logger object
CHANNEL = alpha.getCLogger(__name__)  # channel logger object


@alpha.on_cmd(
    "dic",
    about={
        "header": "English Dictionary-telegram",
        "usage": "{tr}dic [word]",
        "examples": "word : Search for any word",
    },
)
async def dictionary(message: Message):
    """this is a dictionary"""
    LOG.info("starting dic command...")
    input_ = message.input_str

    await message.edit("`processing...âï¸ğ `")

    def combine(s_word, name):
        w_word = f"ğ--**__{name.title()}__**--\n"
        for i in s_word:
            if "definition" in i:
                if "example" in i:
                    w_word += (
                        "\nğ©âğ« **Definition** ğ¨âğ«\n<pre>"
                        + i["definition"]
                        + "</pre>\n\t\tâ<b>Example</b>â\n<pre>"
                        + i["example"]
                        + "</pre>"
                    )
                else:
                    w_word += (
                        "\nğ©âğ« **Definition** ğ¨âğ«\n"
                        + "<pre>"
                        + i["definition"]
                        + "</pre>"
                    )
        w_word += "\n\n"
        return w_word

    def out_print(word1):
        out = ""
        if "meaning" in list(word1):
            meaning = word1["meaning"]
            if "noun" in list(meaning):
                noun = meaning["noun"]
                out += combine(noun, "noun")
                # print(noun)
            if "verb" in list(meaning):
                verb = meaning["verb"]
                out += combine(verb, "verb")
                # print(verb)
            if "preposition" in list(meaning):
                preposition = meaning["preposition"]
                out += combine(preposition, "preposition")
                # print(preposition)
            if "adverb" in list(meaning):
                adverb = meaning["adverb"]
                out += combine(adverb, "adverb")
                # print(adverb)
            if "adjective" in list(meaning):
                adjec = meaning["adjective"]
                out += combine(adjec, "adjective")
                # print(adjec)
            if "abbreviation" in list(meaning):
                abbr = meaning["abbreviation"]
                out += combine(abbr, "abbreviation")
                # print(abbr)
            if "exclamation" in list(meaning):
                exclamation = meaning["exclamation"]
                out += combine(exclamation, "exclamation")
                # print(exclamation)
            if "transitive verb" in list(meaning):
                transitive_verb = meaning["transitive verb"]
                out += combine(transitive_verb, "transitive verb")
                # print(tt)
            if "determiner" in list(meaning):
                determiner = meaning["determiner"]
                out += combine(determiner, "determiner")
                # print(determiner)
            if "crossReference" in list(meaning):
                crosref = meaning["crossReference"]
                out += combine(crosref, "crossReference")
                # print(crosref)
        if "title" in list(word1):
            out += (
                "ğ--**__Error Note__**--\n\nâªï¸`"
                + word1["title"]
                + "ğ¥º\n\nâªï¸"
                + word1["message"]
                + "ğ¬\n\nâªï¸<i>"
                + word1["resolution"]
                + "</i>ğ¤`"
            )
        return out

    if not input_:
        await message.edit("`âPlz enter word to searchâ¼ï¸`", del_in=5)
    else:
        word = input_
        async with aiohttp.ClientSession() as ses:
            async with ses.get(
                f"https://api.dictionaryapi.dev/api/v1/entries/en/{word}"
            ) as res:
                r_dec = await res.json()
        v_word = input_
        if isinstance(r_dec, list):
            r_dec = r_dec[0]
            v_word = r_dec["word"]
        last_output = out_print(r_dec)
        if last_output:
            await message.edit(
                "`ğSearch reasult for   `" + f"ğ {v_word}\n\n" + last_output
            )
            await CHANNEL.log(f"Get dictionary results for ğ {v_word}")
        else:
            await message.edit("`No result found from the database.ğ`", del_in=5)
            await CHANNEL.log("Get dictionary results empty")
