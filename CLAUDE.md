# web_help

## Writing help pages

Every help page (`.. help-page::` file under `<module>/help/`) must have the
following sections, in this order, each with its RST label so that
`.. help-inherit:: ... :section:` can target it:

| Section         | Label            | Views       | Content                                                         |
|-----------------|------------------|-------------|-----------------------------------------------------------------|
| Description     | `description`    | all         | Summary of the view / model                                     |
| New record      | `new_record`     | form only   | Steps to insert a new record                                    |
| Update record   | `update_record`  | form only   | Steps to update an existing record                              |
| How to search   | `search`         | list only   | How to search for records and how to group by                   |
| Configure       | `configure`      | all         | Statements to configure the model                               |
| Report          | `report`         | all         | How to show / print the report or the pdf attachment           |
| Example         | `example`        | all         | Some useful examples                                            |
| FAQ             | `faq`            | all         | Frequently asked questions (`.. help-question::` blocks)        |
| Footer          | `footer`         | all         | Date and time of page creation and copyright notice            |

Rules:

* A form page has no *How to search*; a list page has no *New record* nor
  *Update record*.
* Sections shared between pages (e.g. *Configure*, *Report*) may live in their
  own file and be pulled in with `.. help-include::`; the label stays the same.
* When a section does not apply to the model, keep it with one line saying so
  (e.g. "This model has no printable report.") — never drop it.
* Steps (*New record*, *Update record*) are numbered lists (`#.`); name fields
  with the `:field:` role and buttons in **bold**.
* `.. help-question::` blocks go in the *FAQ* section; end it with
  `.. help-question::` + `:auto:` to add the questions from the fields help.
* Footer format:

  ```rst
  .. _footer:

  Footer
  ------

  Page created on 2026-10-01 10:30 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
  ```

  Creation date/time is the moment the page is first written (keep it on later
  edits); the copyright holder follows the `copyright` skill.
* A page shows only the text of the running Odoo version: never write "on Odoo
  17 and later…" or "(Odoo 16) … (Odoo 18)". Use `.. help-version:: <cond>` for
  blocks and ``:version:`16|text;>=17|text` `` for words in a sentence
  (conditions `16`, `16-18`, `>=17`, `<17`, `*`, comma lists); use the version
  directories (`v10`, `v16_20`…) only for whole files that differ.
* Every page has its Italian twin (`page.it_IT.rst`) with the same sections and
  labels; Italian titles: Descrizione, Nuovo record, Modifica record, Come
  cercare, Configurazione, Stampe, Esempi, Domande frequenti, Piè di pagina ("Pagina creata il …").
