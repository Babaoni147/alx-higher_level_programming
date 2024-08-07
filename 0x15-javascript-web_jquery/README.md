# JavaScript Task Scripts

This repository contains JavaScript scripts for various DOM manipulations and API interactions. The scripts follow specific requirements regarding the use of jQuery, `document.querySelector`, and other constraints.

## Scripts

1. **Update `<header>` Text Color to Red (No jQuery)**
   - Updates the text color of the `<header>` element to red using `document.querySelector`.

2. **Update `<header>` Text Color to Red (Using jQuery)**
   - Updates the text color of the `<header>` element to red using jQuery.

3. **Update `<header>` Text Color on Click (Using jQuery)**
   - Changes the text color of `<header>` to red when clicking on `<div id="red_header">` using jQuery.

4. **Add Class `red` to `<header>` on Click (Using jQuery)**
   - Adds the class `red` to `<header>` when clicking on `<div id="red_header">` using jQuery.

5. **Toggle Class Between `red` and `green` on Click (Using jQuery)**
   - Toggles the class of `<header>` between `red` and `green` on click using jQuery.

6. **Add `<li>` Element to List on Click (Using jQuery)**
   - Adds a `<li>Item</li>` to `<ul class="my_list">` when clicking on `<div id="add_item">` using jQuery.

7. **Update `<header>` Text on Click (Using jQuery)**
   - Updates the text of `<header>` to `New Header!!!` when clicking on `<div id="update_header">` using jQuery.

8. **Fetch and Display Character Name (Using jQuery)**
   - Fetches the character name from a given API and displays it in `<div id="character">` using jQuery.

9. **Fetch and List Movie Titles (Using jQuery)**
   - Fetches movie titles from an API and lists them in `<ul id="list_movies">` using jQuery.

10. **Fetch and Display Hello Translation (Using jQuery)**
    - Fetches the translation of "hello" and displays it in `<div id="hello">` using jQuery.

11. **Update `<header>` Text Color to Red (Imported from `<head>`)**
    - Updates the text color of `<header>` to red using `document.querySelector` and should be imported from the `<head>` tag.

12. **Fetch and Display Hello Translation Based on Language (Using jQuery)**
    - Fetches how to say "Hello" based on language code input and displays it in `<div id="hello">` using jQuery.

13. **Fetch and Display Hello Translation with ENTER Key (Using jQuery)**
    - Fetches how to say "Hello" based on language code input and displays it in `<div id="hello">` using jQuery. The translation is fetched when clicking the button or pressing ENTER.

## Requirements

- jQuery version 3.x must be used.
- Use of `document.querySelector` or jQuery API as specified.
- Scripts must be compatible with browsers interpreting files on Chrome (version 57.0).
- Files should end with a new line.
- A `README.md` file is mandatory at the root of the project.
- Code should be semistandard compliant with the flag `--global $: semistandard *.js --global $`.

## Usage

To use these scripts, include them in your HTML files or import them from the `<head>` tag as needed.

