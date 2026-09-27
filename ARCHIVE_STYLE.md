# Portfolio archive

The homepage, four course indexes and 35 article pages share `css/portfolio.css`.
Pages opt in with `class="portfolio"` on the body. No build step or external font service is required.

## Preview

From this directory run `python -m http.server 8765 --bind 127.0.0.1`, then open
http://127.0.0.1:8765/ in a browser. Stop the server with Ctrl+C.
The static pages also work when opened locally.

## Editing

- Change the theme colors in the variables at the top of `css/portfolio.css`.
- Design I / II reading refinements live in `de12/css/archive.css`, scoped to `.foundations`.
- Edit course entries in each course's `index.html`; homepage entry counts are maintained manually.
- Article text lives inside `<article class="article-content">`. Keep resource links relative to each article.
- Use `.media-gallery` for consecutive images (`.single` for a single image). Images link to their original file; do not add percentage widths. Preserve caption order.
- Long articles use a native `<details class="article-toc">` with links to heading IDs. Update these links when adding or renaming sections.
- Code blocks retain original whitespace and scroll independently. Avoid using heading tags for ordinary explanatory paragraphs.
- For a new article, copy a nearby article's header, breadcrumb, stylesheet link and bottom navigation. Update the title and content.
- Keep original media in their current folders so existing URLs continue to work.

The seminar index and four reports also use the shared portfolio theme. Seminar
layout rules remain in `zemi/CSSfile/main.css`, with archive-specific styling in
`zemi/CSSfile/archive.css`. Keep report section IDs and comment scripts intact
when editing content. Saved third-party reference pages in `zemi/image/` are unchanged.

Generated network visualizations, `Data-AF/`,
test/demo pages, the blank template and `de56/project/project_plan.html` retain
their independent layouts. Legacy stylesheets remain available to those pages.
