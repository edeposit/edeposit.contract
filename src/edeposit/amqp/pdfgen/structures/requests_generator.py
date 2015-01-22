#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from string import Template
from collections import OrderedDict


# Variables ===================================================================
COMMENT_WARNING = """#
# !!! DO NOT EDIT THIS FILE!!!
# !!! THIS IS AUTOMATICALLY GENERATED FILE !!!
# !!! SEE requests_template.py AND requests_generator.py FOR DETAILS !!!
#"""

REVIEW = OrderedDict([  #: This structure is used to construct GenerateReview
    ["nazev", ["Název", True]],
    ["podnazev", ["Podnázev", True]],
    ["cast", ["Část", True]],
    ["nazev_casti", ["Název části", True]],
    ["isbn", ["ISBN", True]],
    ["isbn_souboru_publikaci", [
        "ISBN souboru",
        True
    ]],
    ["generated_isbn", ['Přidělit ISBN', True]],
    ["author1", ["Autor", False]],
    ["author2", ["Autor 2", False]],
    ["author3", ["Autor 3", False]],
    ["poradi_vydani", ['Pořadí', True]],
    ["misto_vydani", ['Místo vydání', True]],
    ["rok_vydani", ["Rok vydání", True]],
    ["nakladatel_vydavatel", ["Nakladatel", True]],
    ["vydano_v_koedici_s", ['Vydáno v koedici s', True]],
    ["cena", ['Cena v Kč', True]],
    ["offer_to_riv", ['Zpřístupnit pro RIV', True]],
    ["category_for_riv", ["Kategorie pro RIV", True]],
    ["is_public", ['Veřejná publikace', True]],
    ["libraries_accessing", ["Oprávnění knihovnám", True]],
    ["libraries_that_can_access", ["Seznam knihoven", True]],
    ["zpracovatel_zaznamu", ['Zpracovatel záznamu', True]],
    ["url", ["URL", True]],
    ["format", ["Formát souboru", True]],
    ["filename", ["Název souboru", True]],
])


# Main program ================================================================
if __name__ == '__main__':
    with open("requests_template.txt") as f:
        template = f.read()

    all_keys = REVIEW.keys()

    # collect all required key
    required = map(
        lambda (key, val): key,
        filter(
            lambda (key, val): val[-1],
            REVIEW.items()
        )
    )

    # collect all optional keys and init them to None
    optional = map(
        lambda (key, val): "%s=None" % key,
        filter(
            lambda (key, val): not val[-1],
            REVIEW.items()
        )
    )

    # create OrderedDict as key_name: meaning
    semantic_dict = map(
        lambda (key, val): '["%s", "%s"],' % (key, val[0]),
        REVIEW.items()
    )
    semantic_dict = "\n            ".join(
        ["semantic_dict = OrderedDict(["] + semantic_dict
    )
    semantic_dict = semantic_dict +  "\n        ])"

    # create help for attributes
    attributes  = map(
        lambda (key, val): '%s (any%s): %s' % (
            key,
            ", default None" if not val[1] else "",
            val[0]
        ),
        REVIEW.items()
    )
    attributes = "\n        ".join(attributes)

    # construct template
    content = Template(template).substitute(
        warning_mark=COMMENT_WARNING,
        first_key="'" + all_keys[0] + "'",
        other_keys=(",\n" + (51 * " ")).join(
            map(lambda x: "'%s'" % x, all_keys[1:])
        ),
        required=",\n                ".join(required),
        optionals=",\n                ".join(optional),
        all_items=",\n            ".join(all_keys),
        semantic_dict=semantic_dict,
        attributes=attributes
    )

    with open("requests.py", "w") as f:
        f.write(content)

    print "requests.py rewritten"
