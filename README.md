# mdm_project_one

## Verwendetes Model
In diesem Projekt verwende ich [gpt2](https://huggingface.co/gpt2).

## Verwendete Daten
Das OpenAI-Team wollte dieses Modell mit einem möglichst großen Korpus trainieren. Um es zu erstellen, wurden alle Webseiten von ausgehenden Links auf Reddit, die mindestens 3 Karma erhalten haben, ausgewertet. Beachten Sie, dass alle Wikipedia-Seiten aus diesem Datensatz entfernt wurden, so dass das Modell nicht auf einem Teil von Wikipedia trainiert wurde. Der resultierende Datensatz (genannt WebText) wiegt 40 GB an Texten, wurde aber nicht veröffentlicht.

## Lokales Setup zum Entwickeln
1. Repository klonen
2. pip install -r requirements.txt
3. app.py ausführen