$ErrorActionPreference = "Stop"

Set-Location $PSScriptRoot

# MiKTeX is commonly installed per-user and may not be visible to a Codex
# terminal opened before installation. Add its standard location explicitly.
$miktexBin = Join-Path $env:LOCALAPPDATA "Programs\MiKTeX\miktex\bin\x64"
if (Test-Path $miktexBin) {
    $env:Path = "$miktexBin;$env:Path"
}

if (-not (Get-Command pdflatex -ErrorAction SilentlyContinue)) {
    throw "pdflatex was not found. Install MiKTeX, restart Codex, and run this script again."
}

pdflatex -interaction=nonstopmode -halt-on-error main.tex
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
if (Test-Path main.aux) { bibtex main }
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
pdflatex -interaction=nonstopmode -halt-on-error main.tex
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
pdflatex -interaction=nonstopmode -halt-on-error main.tex
exit $LASTEXITCODE
