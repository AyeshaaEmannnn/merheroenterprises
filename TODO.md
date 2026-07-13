# TODO - Catalog/Flipbook Improvements

- [x] Update `static/css/pages/catalog.css` to remove extra padding/min-height causing side whitespace and improve vertical centering between fixed navbar and footer.
- [x] Update `templates/cataloge/cataloge.html` to render layout immediately (show loader overlay instead of hiding full section) and improve perceived loading time.
- [x] Implement flipbook performance improvements in `templates/cataloge/cataloge.html`:
  - [x] Progressive/batched PDF page rendering (render first pages first)
  - [x] Prevent full re-renders / re-init where possible (only re-load after each batch)
  - [x] Add resize handler to recompute flipbook size
- [ ] Responsive fixes in CSS/JS for mobile: scale to viewport width, avoid horizontal scrolling, keep controls usable.
- [ ] Run server and manually test desktop/tablet/mobile.
- [ ] Verify no layout shifts during loading and flipbook remains centered.

