# parco_anki

This is a small repo with flashcards that can be imported into Anki to help study for your parallel computing lecture exam.

## Usage

Download the [Anki App](https://play.google.com/store/apps/details?id=com.ichi2.anki&hl=en) (or use the [PC/Web Version](https://apps.ankiweb.net/)) and import the .txt files into Anki. For how to use the application to learn for the exam, see various tutorials around the internet or the [Anki documentation](https://docs.ankiweb.net/), for instance [this](https://docs.ankiweb.net/#/studying) on studying with Anki.

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

To give the cards some structure, I recommend splitting the basic and cloze type cards into 2 separate txt files like in the GWG examples I have given (I probably will have provided the txt file structure already, just need to fill in the info).

## Contributing

1. Fork this repo
2. Add lines to the appropiate txt file (be careful for which type the card is to not break formatting)
3. Import your changes into Anki and check your addition
4. Commit your changes to your fork
5. Do a Pull Request to push your changes (after I have double checked them) into this repo!
