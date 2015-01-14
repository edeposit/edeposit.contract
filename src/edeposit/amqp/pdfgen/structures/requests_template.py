#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
$warning_mark
# Imports =====================================================================
from collections import namedtuple, OrderedDict


# Functions & classes =========================================================
class GenerateContract(namedtuple("GenerateContract", ["firma",
                                                       "pravni_forma",
                                                       "sidlo",
                                                       "ic",
                                                       "dic",
                                                       "zastoupen",
                                                       "jednajici"])):
    """
    Request to generate contract.

    Attributes:
        firma (str): As it is defined in contract.
        pravni_forma (str): As it is defined in contract.
        sidlo (str): As it is defined in contract.
        ic (str): As it is defined in contract.
        dic (str): As it is defined in contract.
        zastoupen (str): As it is defined in contract.
        jednajici (str): As it is defined in contract.
    """
    pass


$warning_mark
class GenerateReview(namedtuple("GenerateReview", [$first_key,
                                                   $other_keys])):
    def __new__(self,
                $required,
                $optionals):
        return super(GenerateReview, self).__new__(
            self,
            $all_items
        )

    def get_rst(self):
        $semantic_dict

        rst = ""
        for key, val in semantic_dict.items():
            val = val.strip()
            rst += ":%s: %s\n" % (val, key)

        return str(rst)
$warning_mark


class RST2PDF(namedtuple("RST2PDF", ["rst_content",
                                     "style",
                                     "header",
                                     "footer"])):
    """
    Generic request to convert RST file to PDF.

    Attributes:
        rst_content (str): Content of the generated PDF file.
        style (str): Style for the generated PDF file.
        header (str, default None): Header of each page.
        footer (str, default pagecount): Footer of each page.
    """
    def __new__(self, rst_content, style, header=None, footer=None):
        return super(RST2PDF, self).__new__(
            self,
            rst_content,
            style,
            header,
            footer
        )