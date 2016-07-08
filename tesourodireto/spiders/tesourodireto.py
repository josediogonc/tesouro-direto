# -*- coding: utf-8 -*-
import scrapy

class TesouroDiretoSpider(scrapy.Spider):
    name = "tesourodireto"
    allowed_domains = ["fazenda.gov.br"]
    start_urls = (
        'http://www.tesouro.fazenda.gov.br/tesouro-direto-precos-e-taxas-dos-titulos',
    )

    def parse(self, response):

        list_resp = response.xpath('//tr/td/text()').extract()
        i = 0

        for index in xrange((len(list_resp)/6)):
            Desc        = list_resp[i+1]
            Vencto      = list_resp[i+2]
            TaxaCompra  = list_resp[i+3]
            TaxaVenda   = list_resp[i+4]
            PrecoCompra = list_resp[i+5]
            PrecoVenda  = list_resp[i+6]
            print Desc, Vencto, TaxaCompra, TaxaVenda, PrecoCompra, PrecoVenda
            i+=6
