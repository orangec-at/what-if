# Raw Sources

`raw/` is the immutable evidence layer.

- `inbox/`: sources waiting to be processed.
- `processed/`: sources already summarized into `wiki/sources/`.
- `assets/`: images, diagrams, screenshots, and attachments.

Agents may read these files but should not edit them unless the user explicitly asks. If a source is web-only, preserve its URL in the relevant `wiki/sources/` page.
