# -*- coding: utf-8 -*-
import scrapy

class TesouroDiretoSpider(scrapy.Spider):
    name = "tesourodireto"
    allowed_domains = ["fazenda.gov.br"]
    start_urls = (
        'http://www.tesouro.fazenda.gov.br/tesouro-direto-precos-e-taxas-dos-titulos',
    )

    def parse(self, response):

        list_resp = response.xpath("//tr[contains(@class, 'camposTesouroDireto')]/td/text()").extract()
        i = 0
        contador = 0

        for index in xrange((len(list_resp)/5)):
            Titulo = list_resp[i+0]
            Vencto = list_resp[i+1]
            TaxaRendimentoAa = list_resp[i+2]

            print('Titulo: %s Vencimento: %s Taxa a.a: %s \n' % (Titulo, Vencto, TaxaRendimentoAa))
            i+=5

            if (Titulo.strip() == "Tesouro IPCA+ 2019 (NTNB Princ)"):
                contador+=1
            
            if contador == 2:
                break


