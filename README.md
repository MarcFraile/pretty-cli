# Pretty-CLI: Pretty Printing for the CLI

This package provides `PrettyCli`, a class providing utilities for structured printing in the CLI. Simply use its `print()` and helper methods instead of the default `print()` and you're good to go!

Here is a full example:

```python
from pretty_cli import PrettyCli


cli = PrettyCli()


def main():
    cli.main_title("my example file:\nAmazing")
    cli.print("Hello, world!")
    cli.print("你好！")
    cli.big_divisor() # Divisors, titles, etc. add blank space above/under as needed.
    cli.print("Let's print a dict:")
    cli.blank() # Add a blank if the previous line is not blank already.
    cli.blank()
    cli.blank()
    cli.print({ # Enforces nice alignment of dict contents.
        "foo": "bar",
        "nested": { "hi": "there" },
        "another one": { "how": "are you?", "fine": "thanks" },
    })
    cli.small_divisor()
    cli.print("Some header styles:")
    cli.chapter("a chapter")
    cli.subchapter("a sub-chapter")
    cli.section("a section")
    cli.print("That's all, folks!")


if __name__ == "__main__":
    main()

```

And the produced output:

```
==================================================================
======================== MY EXAMPLE FILE: ========================
============================ AMAZING =============================
==================================================================

Hello, world!
你好！

================================

Let's print a dict:

foo:         bar
nested:
    hi:      there
another one:
    how:     are you?
    fine:    thanks

----------------

Some header styles:

================ A Chapter ================

-------- A Sub-Chapter --------

[A Section]

That's all, folks!
```
