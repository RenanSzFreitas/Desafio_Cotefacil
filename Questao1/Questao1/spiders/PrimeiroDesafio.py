from typing import Iterable
import json
import scrapy
from scrapy.http import Response, HtmlResponse, Request
from ..items import CompraAgoraProdutoItem


class CompraAgoraSpider(scrapy.Spider):
    name = "compra-agora"
    url = "https://www.compra-agora.com"

    def _init_(self, login: str, password: str, **kw) -> None:
        super()._init_(**kw)
        self.login = login
        self.password = password

    def start_requests(self) -> Iterable[Request]:
        self.logger.info("Iniciando a busca de categorias")
        yield scrapy.Request(
            url=self.url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0"
            },
            callback=self.parse_categories
        )

    def parse_categories(self, response: HtmlResponse) -> Iterable[Request]:
        for category in response.css("li.lista-menu-itens a"):
            name = category.xpath('./text()[2]').get(default="").strip()

            if name == "Novidades":
                yield scrapy.Request(
                    url=category.css("::attr(href)").get(default=""),
                    callback=self.parse_html
                )

            self.logger.info(f"Processando produtos na categoria: {name}...")
            api_url = category.css("::attr(href)").get(default="").replace('/loja/', '/api/catalogproducts/')

            yield scrapy.Request(
                url=api_url,
                callback=self.parse
            )

    def parse(self, response: Response) -> Iterable[CompraAgoraProdutoItem]:
        json_response = json.loads(response.body)
        for product in json_response.get("produtos", []):
            yield CompraAgoraProdutoItem(
                name=product.get("Nome", ""),
                manufacter=product.get("Marca", ""),
                barcode=product.get("Codigo", ""),
                image_url=f'https://images-unilever.ifcshop.com.br/200x200/produto/{product.get("Foto", "")}'
            )

    def parse_html(self, response: HtmlResponse) -> Iterable[CompraAgoraProdutoItem]:
        for product in response.css("div#divProdutos ul li"):
            yield CompraAgoraProdutoItem(
                name=product.css("div.produto-nome::text").get(default="").strip(),
                manufacter=product.css("div.produto-marca::text").get(default="").strip(),
                barcode=product.css("div.produto-ean p").xpath('./text()[2]').get(default="").strip()[2:],
                image_url=product.css("img.img-fluid::attr(src)").get(default="").strip()
            )