### This page is designed to help you make your markdown files fancy!

# Table of contents

- [Headings](#headings)
- [Line breaks](#line-breaks)
- [Emphasis](#emphasis)
  - [Bold and italic](#bold-and-italic)
  - [Strikethrough](#strikethrough)
- [Blockquotes](#blockquotes)
- [Lists](#lists)
  - [Ordered lists](#ordered-lists)
  - [Unordered lists](#unordered-lists)
  - [Task lists](#task-lists)
- [Code](#code)
  - [Code Blocks](#code-blocks)
  - [Fenced Code Blocks](#fenced-code-blocks)
- [Horizontal rule](#horizontal-rule)
- [(Hyper)links](#hyperlinks)
  - [Titles](#titles)
  - [Emails & URLs](#emails--urls)
- [Images](#images)
- [Sources](#sources)

---

# Headings

There are 6 heading types in markdown. Each with their own size.

# Heading level 1

## Heading level 2

### Heading level 3

#### Heading level 4

##### Heading level 5

###### Heading level 6

<br>

Alternatively, you can use underlined headings

# Alternative heading level 1

## Alternative heading level 2

```
# Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6

Underlined headings

Alternative heading level 1
======

Alternative heading level 2
------
```

# Line breaks

You can add 2 spaces after a line to add a line break  
Or, if you prefer you can use `<br>`

```
You can add 2 spaces after a line to add a line break
Or, if you prefer you can use `<br>`
```

# Emphasis

## Bold and italic

To add emphasis to a text, you can make it **bold** or _italic_

This text **might be** bold  
_"Very emotional italic example"_, - Me  
**_Really important_** text

```
This text **might be** bold
*"Very emotional italic example"*, - Me
***Really important*** text
```

Alternatively, you can use the [not recommended](https://www.markdownguide.org/basic-syntax/#bold-and-italic-best-practices) underscore syntax like so

```
This text __might be__ bold
_"Very emotional italic example"_, - Me
___Really important__ text
```

## Strikethrough

You can use two tildes (~~) to strike through a text.

~~Why would we go?~~ Lets go to the cinema!

```
~~Why would we go?~~ Lets go to the cinema!
```

# Blockquotes

> This is a quote

```
> This is a quote
```

> This is a quote with 2 paragraphs
>
> This is the second paragraph

```
> This is a quote with 2 paragraphs
>
> This is the second paragraph
```

> This is a quote
>
> > This is a nested quote

```
> This is a quote
> > This is a nested quote
```

Note that [not all](https://www.markdownguide.org/basic-syntax/#blockquotes-with-other-elements) markdown is supported in blockquotes

# Lists

## Ordered lists

Ordered lists do not have to be in numerical order, but do have to start with a 1.

1. First item
2. Second item 2. This is an indented item
3. This is the third item

```
1. First item
2. Second item
   2. This is an indented item
3. This is the third item
```

## Unordered lists

- First item
- Second item
  - Indented item
- Third item

```
- First item
- Second item
    - Indented item
- Third item
```

You can also use the asterisks or plus signs

```
* First item
* Second item
    * Indented item
* Third item

+ First item
+ Second item
    + Indented item
+ Third item
```

## Task lists

Task lists also referred to as checklists or todo lists are used to make a list of items with checkboxes. You can use the `- [x]` syntax to check a box and `- [ ]` to leave it open.

- [x] Create task list
- [x] Commit markdown syntax guide to Github
- [ ] Eat a pizza

# Code

You can use `single backticks` to highlight a piece of code.

```
You can use `single backticks` to highlight a piece of code.
```

`` You can  use `backticks` in your code without altering the highlighting ``

```
``You can  use `backticks` in your code without altering the highlighting``
```

## Code Blocks

    You can indent every line of your text with
    a tab (or 4 spaces) to make it a code block

```
    You can indent every line of your text with
    a tab (or 4 spaces) to make it a code block
```

## Fenced Code Blocks

If you find that inconvenient, you can also use three backticks (```) or tildes (~~~)

```
This is also a code block, but fenced.
```

````
```
This is also a code block, but fenced.
```
````

Or if you're using tildes

```
~~~
This is also a code block, but fenced.
~~~
```

Note: to use backticks or tildes inside of your fenced code blocks, use four backticks/tildes like so:

`````
````
```
This is also a code block, but fenced.
```
````
`````

# Horizontal rule

To add a horizontal rule, you can use three or more asterisks, dashes, or underscores in a single line.

---

---

---

```
***

----

_____________________
```

# (Hyper)links

To use links, you can use the `[text](link)` format.

Wow this [link](https://github.com/UndefinedToast/README-Templates/blob/main/markdown_syntax.md#hyperlinks) is so cool!

```
Wow this [link](https://github.com/UndefinedToast/README-Templates/blob/main/markdown_syntax.md#hyperlinks) is so cool!
```

## Titles

To add titles to your links, you can add an enclosed quotation mark text after the link

Wow this [link](https://github.com/UndefinedToast/README-Templates/blob/main/markdown_syntax.md#hyperlinks "Super cool link") is so cool!

```
Wow this [link](https://github.com/UndefinedToast/README-Templates/blob/main/markdown_syntax.md#hyperlinks "Super cool link") is so cool!
```

## Emails & URLs

You can enclose an URL or email adress in angle brackets to make it a link.

<https://github.com/UndefinedToast/README-Templates>
<cool@exampleemail.com>

```
<https://github.com/UndefinedToast/README-Templates>
<cool@exampleemail.com>
```

# Images

To use images in your markdown file, you can use the `![alt text](local file path or link)` syntax.

![Partially submerged Samanea saman](https://upload.wikimedia.org/wikipedia/commons/7/7b/Flooded_Albizia_Saman_%28rain_tree%29_in_the_Mekong.jpg)

<!--Basile Morin, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons-->

```
![Partially submerged Samanea saman](https://upload.wikimedia.org/wikipedia/commons/7/7b/Flooded_Albizia_Saman_%28rain_tree%29_in_the_Mekong.jpg)
```

# Sources

This work is based on or includes materials from the Markdown Guide website, which is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License. The original materials can be found at https://www.markdownguide.org/.
