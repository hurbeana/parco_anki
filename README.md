# parco_anki

This is a small repo with flashcards that can be imported into Anki to help study for your parallel computing lecture exam.

## Usage

Download the [Anki App](https://play.google.com/store/apps/details?id=com.ichi2.anki&hl=en) (or use the [PC/Web Version](https://apps.ankiweb.net/)) and import the .txt files into Anki. For how to use the application to learn for the exam, see various tutorials around the internet or the [Anki documentation](https://docs.ankiweb.net/), for instance [this](https://docs.ankiweb.net/#/studying) on studying with Anki.

I will combine all of the basic and clozure cards into two txt files and put them in the releases every time somebody contributes (I'll try to do it at least once a day). Check out the "Releases" Tab and download the txts, so you can import everything into Anki at once.

## Structure

There are following sections for which flashcards are needed (one per slide PDF mostly):

- [ ] Introduction (intro)
- [ ] Performance and Objectives (perf)
- [ ] Patterns and Paradigms (pat)
- [ ] Merging and Prefix Sums (merg)
- [ ] Shared Memory (shmem)
- [ ] PThreads (pth)
- [ ] OpenMP (omp)
- [ ] Distributed Memory Systems (dismem)
- [ ] MPI (mpi)

I will have created a git issue for each of these where we can discuss per slide issue etc. Also feel free to report additional issues you find.

## Flashcards

There are 2 (general useful) types of flashcards in Anki:

- Basic
- [Clozure](https://docs.ankiweb.net/#/editing?id=cloze-deletion)

For how to write Cards for both of those types is described in the documentation. I have written some cards in the past for [GWG](https://gist.github.com/hurbeana/dd9e8a335c6c5bdbeed267d9e70ec7e2). These can be used as a guide. You can also include some HTML for styling, but don't [overdo it](https://en.wikipedia.org/wiki/KISS_principle). To show the HTML styling in Anki, you have to check the checkbox for it when importing the txt file.

It has come to my attention that Anki has changed the default template for basic and cloze type cards, so I think its good if contribution use following format:

### Basic Card

One line in the txt per card with following formatting:

```
{Front Side};{Back Side};{Tags (separated by space)}
```

For examples look into txts with content already present.

### Clozure Cards

One line in the txt per card with following formatting:

```
{Text with some amount of clozures};{Tags (separated by space)}
```

For examples look into txts with content already present.

Anki even supports [LaTeX](https://docs.ankiweb.net/#/math?id=example) in cards, and these can even be used with clozures.

### Structure

To give the cards some structure, I recommend splitting the basic and cloze type cards into 2 separate txt files like in the GWG examples I have given (I probably will have provided the txt file structure already, just need to fill in the info).

## Contributing

1. Comment on the cardset you want to work on so I can assign the issue to you. This helps others to see which cards are being worked on and which still need work. I will then assign the issue to you (github only allows me to assign a issue to commenters of the issue).
2. [Fork](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) this repo
3. Add lines to the appropiate txt file (be careful for which type the card is to not break formatting while importing)
4. Import your changes into Anki and check whether your addition works properly
5. Commit your changes to your fork
6. Do a [Pull Request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork) to push your changes (after I have double checked them) into this repo!
