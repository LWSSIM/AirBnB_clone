# HTML and CSS Basics - README

## What is HTML?

HTML, or HyperText Markup Language, is the standard markup language for creating web pages. It structures the content of a web page using a system of elements or tags, each denoting different types of content such as headings, paragraphs, images, links, and more.

## How to create an HTML page

To create an HTML page, you need a simple text editor like Notepad or more advanced ones like Visual Studio Code. Start with the basic structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Page Title</title>
</head>
<body>
    <!-- Your content goes here -->
</body>
</html>
```

Inside the `<body>` tag, you can add various HTML elements to structure your content.

## What is a markup language?

A markup language is a system for annotating text documents to provide additional information about the structure of the document. HTML uses a markup system where tags are used to define elements and their attributes.

## What is the DOM?

The DOM, or Document Object Model, is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content dynamically.

## What is an element/tag?

An HTML element or tag is a building block of an HTML page. It consists of a start tag, content, and an end tag. For example:

```html
<p>This is a paragraph</p>
```

Here, `<p>` is the start tag, "This is a paragraph" is the content, and `</p>` is the end tag.

## What is an attribute?

HTML elements can have attributes that provide additional information about the element. Attributes are always included in the opening tag. Example:

```html
<a href="https://www.example.com">Visit Example</a>
```

Here, `href` is an attribute of the `<a>` (anchor) tag.

## How does the browser load a webpage?

When you enter a URL, the browser fetches the HTML file associated with that URL. It then parses the HTML to construct the DOM, fetches external resources like stylesheets and scripts, and renders the webpage.

## What is CSS?

CSS, or Cascading Style Sheets, is a stylesheet language used to describe the presentation of a document written in HTML. It controls the layout, colors, and fonts of the elements on a webpage.

## How to add style to an element?

You can add style to an element using inline styles, internal styles, or external stylesheets. Example:

Inline style:
```html
<p style="color: blue;">This is a blue paragraph.</p>
```

Internal style (inside `<head>`):
```html
<style>
    p {
        color: red;
    }
</style>
```

External stylesheet (linked from HTML):
```html
<link rel="stylesheet" href="styles.css">
```

## What is a class?

A class is a way to apply styles to multiple elements. Elements with the same class share the same styles. Example:

```html
<p class="highlight">This paragraph is highlighted.</p>
```

## What is a selector?

A selector is a pattern used to select and style HTML elements. For example:

```css
p {
    font-size: 16px;
}
```

Here, `p` is a selector that targets all `<p>` elements.

## How to compute CSS Specificity Value?

Specificity determines which style rule is applied when there is a conflict. It is calculated based on the combination of selectors in a rule. For example, the selector `#content .highlight` has a higher specificity than just `.highlight`.

## What are Box properties in CSS?

Box properties in CSS control the layout and dimensions of an element. Common box properties include `width`, `height`, `margin`, `padding`, `border`, and `display`. These properties define how an element occupies space on the page.

### Further Reading Material:

1. [MDN Web Docs - HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
2. [MDN Web Docs - CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
3. [W3Schools - HTML Tutorial](https://www.w3schools.com/html/)
4. [W3Schools - CSS Tutorial](https://www.w3schools.com/css/)
5. [Specificity in CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity)