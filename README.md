# Luann Batuira | Portfólio de Fotografia

Site de portfólio do fotógrafo de arquitetura **Luann Batuira** (São Paulo). Substitui a versão hospedada no Canva por um site próprio, estático, rápido e com SEO configurado, para dar mais controle sobre conteúdo, tags e hospedagem.

- Projeto visível em: https://wesleylcs.github.io/Fotografo_LuannBatuira
- HTML, CSS e JavaScript puros. Sem frameworks, sem bundler e sem dependências em runtime.
- Página única com as seções: Início, Sobre mim, Meu trabalho (P&B), Coloridas e Trabalhe comigo.
- Lighthouse medido localmente: **100** em Acessibilidade, Boas práticas e SEO; Performance **100** no desktop e **97-98** no mobile.

## Estrutura

```
index.html               Página (conteúdo, meta tags, Open Graph, JSON-LD)
css/styles.css           Estilos (fonte; é embutido no dist/)
js/main.js               Visualizador de fotos (lightbox) e ano do rodapé
js/analytics.js          Carregamento do Google Tag Manager e Google Analytics 4
img/                     Imagens otimizadas e responsivas (geradas, mas versionadas)
originais/               Fotos originais usadas como fonte das imagens
tools/build_images.py    Gera as imagens de img/ a partir de originais/
tools/inline_css.py      Gera dist/ pronto para publicar (CSS embutido)
dist/                    Saída de produção
favicon.svg, manifest.webmanifest, robots.txt, sitemap.xml
_headers                 Cache longo e cabeçalhos de segurança (Netlify / Cloudflare Pages)
```

## Editar o conteúdo

| Quero... | Onde |
|---|---|
| Alterar textos, legendas, links, e-mail | `index.html` |
| Alterar cores, fontes, espaçamentos | `css/styles.css` (variáveis em `:root`) |
| Alterar o comportamento do visualizador de fotos | `js/main.js` |
| Trocar título, descrição e imagem de compartilhamento | `<head>` do `index.html` |

## Cabeçalhos e cache

O arquivo `_headers` define cache de 1 ano para `/img`, `/css` e `/js`, além de CSP, `X-Content-Type-Options`, `Referrer-Policy` e `X-Frame-Options`. Em outros hosts, replique essas regras e ative compressão gzip ou brotli. Se mudar uma imagem, CSS ou JS, renomeie o arquivo ou limpe o cache da CDN, pois o cache é `immutable`.

## Analytics (GTM e GA4)

Os IDs ficam no topo de `js/analytics.js`:

```js
const GTM_ID = 'GTM-XXXXXXX';   // contêiner do Google Tag Manager
const GA_ID = 'G-XXXXXXXXXX';   // ID de métricas do GA4
```

- Enquanto os IDs tiverem `XXXX`, nenhum script do Google é carregado.
- Os scripts só carregam depois da página pronta ou na primeira interação, para não afetar o Lighthouse.
- O GA4 aqui é enviado direto pelo `gtag`. **Não crie também uma tag de configuração do GA4 dentro do GTM**, ou cada visita será contada duas vezes. Se preferir gerenciar o GA4 pelo GTM, deixe `GA_ID` com `XXXX`.
- O `_headers` já libera os domínios do Google no CSP. Se mudar de host, replique essa liberação.
- Pela LGPD, avalie incluir um aviso de cookies e só carregar o analytics após o consentimento.

## Antes de ir ao ar

- [ ] Trocar o domínio provisório `https://luannbatuira.com.br/` em `index.html` (canonical, Open Graph, JSON-LD), `sitemap.xml` e `robots.txt`.
- [ ] Trocar os links de **VSCO**, **Flickr** e **Behance** pelos perfis reais, na seção de contato do `index.html` e em `sameAs` no JSON-LD. Hoje apontam para a página inicial de cada serviço.
- [ ] Atualizar `lastmod` em `sitemap.xml` quando o conteúdo mudar.
- [ ] Preencher `GTM_ID` e `GA_ID` em `js/analytics.js` e confirmar as visualizações no GA4 (relatório em tempo real).
- [ ] Rodar o Lighthouse na URL publicada.
- [ ] Opcional: substituir `boa-viagem` por um original maior (o atual tem só 582 px de largura).

## Desempenho e acessibilidade

- Imagens em WebP com `srcset`/`sizes` e dimensões declaradas, o que evita salto de layout (CLS 0).
- Só a imagem principal carrega de imediato (`fetchpriority="high"`); as demais usam `loading="lazy"`, inclusive os fundos das seções.
- Fontes do sistema, sem requisições de fontes externas. JavaScript com `defer` e cerca de 1 KB.
- Navegação por teclado, link "Pular para o conteúdo", foco visível, `alt` descritivo, `prefers-reduced-motion` respeitado e visualizador baseado em `<dialog>` nativo (fecha com Esc, setas para navegar).

## Créditos

Todas as fotografias © Luann Batuira. Todos os direitos reservados; não reutilize sem autorização.
