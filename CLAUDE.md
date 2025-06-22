# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal blog built with Hugo static site generator, hosted on GitHub Pages at callas1900.net. The blog contains 20+ years of posts (2005-2025) primarily in Japanese, covering technology, personal development, coaching, and travel.

## Development Commands

### Local Development
```bash
hugo serve --poll 500ms
```

### Creating New Posts
```bash
hugo new posts/20191224.md
```

### Build and Deploy
The site automatically builds and deploys via GitHub Actions when pushed to main branch.

## Architecture and Structure

### Content Management
- **Primary markup**: AsciiDoc (.adoc) for recent posts, Markdown (.md) for older content
- **Content organization**: Posts organized by year in `/content/posts/YYYY/`
- **Naming convention**: Posts use format `YYYYMMDD_title.adoc` or descriptive titles

### Hugo Configuration
- **Theme**: Terminal theme with green color scheme
- **Base URL**: Root-relative URLs for GitHub Pages
- **Security**: Configured to allow asciidoctor, dart-sass, postcss
- **Permalinks**: `/posts/YEAR/MONTH/SLUG/` structure

### Key Directories
- `/content/posts/`: All blog posts organized by year
- `/static/`: Static assets including legacy tools in `/beta/`
- `/themes/terminal/`: Hugo theme with customizations
- `/public/`: Generated static site (ignored in git)

### Dependencies and Toolchain
- **Hugo**: v0.120.2 extended (supports Sass)
- **AsciiDoc**: Processed via asciidoctor v2.0.18
- **Ruby**: v2.7 required for AsciiDoc processing
- **Node.js**: For theme asset processing

### Deployment Pipeline
GitHub Actions workflow (`.github/workflows/hugo.yaml`) handles:
1. Hugo CLI installation (v0.120.2 extended)
2. Dart Sass and Node.js dependencies
3. Ruby and Asciidoctor setup
4. Production build with minification
5. Deployment to GitHub Pages

### Content Patterns
- **Mixed languages**: Primarily Japanese with English technical terms
- **Topics**: Technology (Android, web dev, cloud), coaching/Scrum, books, travel
- **Legacy content**: Maintains historical posts from 2005, some with outdated formatting
- **Static tools**: Legacy calculators and tools preserved in `/static/beta/`

## Theme Customization
The Terminal theme includes:
- Custom color scheme (green)
- Japanese content support
- Google Analytics integration
- Custom pagination and menu structure
- Legacy asset support for historical content