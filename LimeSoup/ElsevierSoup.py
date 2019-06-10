import re

import bs4

from LimeSoup.lime_soup import Soup, RuleIngredient
from LimeSoup.parser.elsevier_xml import (
    resolve_elsevier_entities, extract_ce_text, find_non_empty_children,
    node_named, extract_ce_para, extract_ce_section, extract_ce_abstract,
    extract_ce_title)

__author__ = 'Haoyan Huo, Nicolas Mingione'
__maintainer__ = 'Nicolas Mingione'
__version__ = '0.3.1'


class ElsevierParseXML(RuleIngredient):
    @staticmethod
    def _parse(xml_str):
        xml_str = resolve_elsevier_entities(xml_str)
        return bs4.BeautifulSoup(xml_str, 'lxml-xml')


class ElsevierReadMetaData(RuleIngredient):
    @staticmethod
    def get_text_or_none(soup, name, handler=None):
        if soup is None:
            return None

        node = soup.find(name=name)
        if node is None:
            return None
        elif handler is not None:
            return handler(node)
        else:
            return node.get_text().strip()

    @staticmethod
    def _parse(soup):
        # journal
        journal_name = ElsevierReadMetaData.get_text_or_none(soup, 'xocs:srctitle') or \
            ElsevierReadMetaData.get_text_or_none(soup, 'prism:publicationName')
        doi = ElsevierReadMetaData.get_text_or_none(soup, 'xocs:doi')

        # https://www.elsevier.com/__data/assets/pdf_file/0003/58872/ja5_tagbytag5_v1.9.5.pdf
        # Elsevier XML definition pp. 46
        head_node = soup.find('head')

        title = ElsevierReadMetaData.get_text_or_none(head_node, 'ce:title', extract_ce_title) or \
                ElsevierReadMetaData.get_text_or_none(soup, 'dc:title')

        keywords = []
        if head_node is not None:
            # Elsevier XML definition pp. 366
            for node in head_node.find_all('ce:keyword'):
                text_node = node.find('ce:text')
                if text_node is not None:
                    keywords.append(extract_ce_text(text_node))

        if len(keywords) == 0:
            for subject in soup.find_all('dcterms:subject'):
                keywords.append(subject.get_text().strip())

        return soup, {
            'Journal': journal_name,
            'DOI': doi,
            'Title': title,
            'Keywords': keywords
        }


class ElsevierCollect(RuleIngredient):

    @staticmethod
    def _parse(args):
        soup, obj = args

        paragraphs = []

        # find all sections
        for node in soup.find_all('ce:abstract'):
            abstract_paragraph = extract_ce_abstract(node)
            normalized_name = re.sub(r'[^\w]', '', abstract_paragraph['name'])
            if re.match(r'abstracts?', normalized_name, re.IGNORECASE):
                paragraphs.append(abstract_paragraph)

        sections = soup.find('ce:sections')
        if sections is not None:
            for node in find_non_empty_children(sections):
                if node_named(node, 'ce:para'):
                    paragraphs.extend(extract_ce_para(node).split('\n'))
                elif node_named(node, 'ce:section'):
                    paragraphs.append(extract_ce_section(node))

        obj['Sections'] = paragraphs
        return obj


ElsevierSoup = Soup(parser_version=__version__)
ElsevierSoup.add_ingredient(ElsevierParseXML())
ElsevierSoup.add_ingredient(ElsevierReadMetaData())
ElsevierSoup.add_ingredient(ElsevierCollect())
