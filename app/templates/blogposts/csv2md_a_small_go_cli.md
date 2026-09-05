# csv2md - A Small Go CLI
## What ?
csv2md is a command line tool that I have written in Go that converts CSV files
into Markdown tables. It reads from a file or stdin and writes a formatted
Markdown table, aligning columns so the output is readable straight in a
terminal, an editor, in a markdown wiki or in a chat with a stakeholder.

Repo: [csv2md](https://github.com/AdrianHRedhe/csv2md)

### Installation
```bash
brew install adrianhredhe/tap/csv2md
```

### Usage
```bash
# From file
csv2md input.csv -o output.md

# From stdin
cat data.csv | csv2md
```

## Demo
<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/asciinema-player@3.17.0/dist/bundle/asciinema-player.css" />
<div id="csv2md-demo"></div>
<script src="https://cdn.jsdelivr.net/npm/asciinema-player@3.17.0/dist/bundle/asciinema-player.min.js"></script>
<script>
AsciinemaPlayer.create('/static/casts/csv2md_demo.cast', document.getElementById('csv2md-demo'), { cols: 80, rows: 14, idleTimeLimit: 2 });
</script>

## Why ? 
I built this for 3 reasons: 

**a)** I wanted to build something real with Go that makes sense for my workflow.  
**b)** I wanted to try creating a CLI that is easily downloadable from brew.   
**c)** This specifically makes sense as I sometimes want to throw a few lines from
a .csv file and send them over to a non-technical stakeholder or want to paste
them as an example in a markdown wiki. Generally I can copy csv in the terminal,
or in databricks and put it in my clipboard and then run something like:
```bash
pbpaste | csv2md | pbcopy
```
to get a nicely formatted output for the stakeholder that I can just paste in a
chat it does not solve any big problems but was super quick to write and is
more of a foundation which I can reuse for small similar fixes later on. And
that is something that adds up over time in terms of having a nice workflow in
my experience.

## How ?
Implementation is very simple by design. Put full input into memory and do one
pass to find the widest value in each column. Then another pass to create the
markdown table with appropriate dividers. No external dependencies used, only
the Go standard libraries `encoding/csv`, `bufio` and `flag`.

The release pipeline is the part that is actually nice. Pushing a `v*` tag
kicks off a GitHub Actions workflow that hands off to GoReleaser. Before it
builds anything it runs `go mod tidy` and `go test ./...` as a hook, so a
broken test blocks the release outright. From there it cross-compiles static
binaries for linux/darwin/windows on amd64/arm64, and via the `brews` section
of `.goreleaser.yml` pushes an updated formula straight to my `homebrew-tap`
repo using a repo token. One config file and a tag push, and `brew install
adrianhredhe/tap/csv2md` works for the new updated version. `homebrew-tap` repo
can be reused for all future brew plugins. So that setting up new CLIs will be
a breeze.
