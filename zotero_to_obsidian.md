# Exporting Zotero entries as Markdown files.

## install add-ons
The MD Notes add-on for Zotero is needed.  It depends on two other add-ons, so install these add-ons:

To install an Add-on in Zotero:

Tools | Add-ons | (click Gear icon) | Install Add-on from file | (select .xpi file)

### Zotfile

http://zotfile.com/

Click "Download" to get zotfile-5.0.16-fx (1).xpi  

### Better Bibtex

https://retorque.re/zotero-better-bibtex/

### MD Notes

https://github.com/argenos/zotero-mdnotes/releases/tag/0.1.3

Retart Zotero

In MDNotes preferences add @ for file prefix

In Zotero:

Tools | Mdnotes preferences | File names tab | Mdnotes - Prefix @

Click OK to save.

## Template to format an Mdnote...

Documentation about templates:
https://github.com/argenos/zotero-mdnotes/blob/master/docs/docs/advanced/templates/defaults.md#zotero-note-template

Create templates

https://argenos.gitbook.io/zotero-mdnotes/customization/templates

```
├── Mdnotes Default Template.md
├── Standalone Note Template.md
├── Zotero Metadata Template.md
└── Zotero Note Template.md
```

### Create a folder for templates.

Example:

C:\Users\User\OneDrive - Carleton University\obsidian\plugins\mdnotes\templates

### Set template folder in Zotero
In Zotero:

Tools | Mdnotes preferences | Export preferences tab | Templates folder

Set to: C:\Users\User\OneDrive - Carleton University\obsidian\plugins\mdnotes\templates

Also, set the export directory

C:\Users\User\OneDrive - Carleton University\obsidian\obsidian-student-starter-vault-main\obsidian-student-starter-vault-main\1 reading notes

(I want to be careful here since if I re-export from Zotero it could overwrite edits files.

Click OK to save.

### Create template

In the templates folder (C:\Users\User\OneDrive - Carleton University\obsidian\plugins\mdnotes\templates)

Create a file called Mdnotes Default Template.md  (It must have this exact name)

Put in the content below (but with no ```)

```
---
title: {{title}}
authors: {{author}}
year: 

tags: {{tags}}
date: {{date}}
---
{{title}}

[Open in Zotero]
{{localLibrary}}
{{cloudLibrary}}


### Summary
{{notes}}

### Own thoughts

### Related topics / notes
```


## Export a note as an Mdnote

In Zotero

Select a note

Right click

Mdnotes| Create Mdnotes file
