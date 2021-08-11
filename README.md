# Aspidites [![codecov](https://codecov.io/gh/rjdbcm/Aspidites/branch/main/graph/badge.svg?token=78fHNV5al0)](https://codecov.io/gh/rjdbcm/Aspidites)

Aspidites is the reference implementation of the [Woma programming language](https://www.github.com/rjdbcm/woma) compiler.

### Core Dependencies
Aspidites has 6 core dependencies. In general, dependencies are vendored unless they contain Python Extensions.
- Cython
- Pyrsistent
- PyParsing
- MyPy
- PyTest
- NumPy

## Paradigms

- [`refinement-type system`](https://arxiv.org/pdf/2010.07763.pdf)
- [`pragmatic`](https://www.adaic.org/resources/add_content/standards/05rm/html/RM-2-8.html)
- `declarative`
- [`functional`](https://towardsdatascience.com/why-developers-are-falling-in-love-with-functional-programming-13514df4048e?gi=3361de79dc98)
- [`constrained logic`](https://www.cse.unsw.edu.au/~tw/brwhkr08.pdf)

## Inspirations

- [`coconut`](http://coconut-lang.org/)
- [`Ada`](https://www.adacore.com/get-started)
- [`Scala`](https://www.scala-lang.org/)
- [`Prolog`](https://www.swi-prolog.org/features.html)
- [`Curry`](https://curry.pages.ps.informatik.uni-kiel.de/curry-lang.org/)
- [`Cobra`](http://cobra-language.com/)
- [`J`](https://www.jsoftware.com/#/README)
- [`ELI`](https://fastarray.appspot.com/index.html)

## Goals

- Ultra-smooth runtime exception handling with useful warnings.
- Demonic non-determinism, favors non-termination and type-negotiation (constraint satisfaction).
- Terseness that mixes keywords and symbolic operations in order to make code both concise ___and___ readable.
- Great for writing high-integrity code that works natively with CPython.
- Usable for general purpose ___or___ scientific computing.

# Syntax

| Working?      | Symbol        | Verbage             |  Example                                                       |
|:--------------|:--------------|:--------------------|:---------------------------------------------------------------|
| ✅            | `->`          |respects             | `identifier` `->` `constraining clauses`                       |
| ✅            | `<-`          |imposes              | `identifier` `<-` `imposed clauses`                            |
| ❌            | `<@> `        |loops                | `identifier` `<@>` `iterable container`<br>`indent` `...`      |
| ✅            | `<*>`         |return               | `<*>` `statement `                                             |
| ✅            |  `#`          |pragma               | `#` `compiler directive`                                       |

# Examples

```
(Greeter(name -> str)) procedure
    <*>print('Greetings,', name)

```
