#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import time
import os.path
from string import Template

from translator import gen_pdf


# Functions & classes =========================================================
def _resource_context(fn):
    """
    Compose path to the ``resources`` directory for given `fn`.

    Args:
        fn (str): Filename of file in ``resources`` directory.

    Returns:
        str: Absolute path to the file in resources directory.
    """
    return os.path.join(
        os.path.dirname(__file__),
        "resources",
        fn
    )


def get_contract(firma, pravni_forma, sidlo, ic, dic, zastoupen, jednajici):
    """
    Compose contract and create PDF.

    Args:
        firma (str): firma
        pravni_forma (str): pravni_forma
        sidlo (str): sidlo
        ic (str): ic
        dic (str): dic
        zastoupen (str): zastoupen
        jednajici (str): jednajici

    Returns:
        obj: StringIO file instance containing PDF file.
    """
    contract_fn = _resource_context(
        "Licencni_smlouva_o_dodavani_elektronickych_publikaci"
        "_a_jejich_uziti.rst"
    )

    # load contract
    with open(contract_fn) as f:
        contract = f.read()

    # make sure that `firma` has its heading mark
    firma = firma.strip()
    firma = firma + ":\n" + (len(firma) * "-")

    # patch template
    contract = Template(contract).substitute(
        firma=firma,
        pravni_forma=pravni_forma.strip(),
        sidlo=sidlo.strip(),
        ic=ic.strip(),
        dic=dic.strip(),
        zastoupen=zastoupen.strip(),
        jednajici=jednajici.strip(),
    )

    return gen_pdf(
        contract,
        open(_resource_context("style.json")).read(),
    )


def get_review(review_struct):
    """
    Generate review from `review_struct`.

    Args:
        review_struct (obj): :class:`.GenerateReview` instance.

    Returns:
        obj: StringIO file instance containing PDF file.
    """
    review_fn = _resource_context("review.rst")

    with open(review_fn) as f:
        review = f.read()

    res_path = os.path.join(
        os.path.dirname(__file__),
        "resources",
    )

    review = Template(review).substitute(
        content=review_struct.get_rst(),
        datum=time.strftime("%d.%m.%Y", time.localtime()),
        cas=time.strftime("%H:%M", time.localtime()),
        resources_path=res_path,
    )

    return gen_pdf(
        review,
        open(_resource_context("review_style.json")).read(),
    )
