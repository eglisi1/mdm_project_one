# mdm_project_one

## Verwendetes Model
In diesem Projekt verwende ich [gpt2](https://huggingface.co/gpt2).

## Verwendete Daten
Die für dieses Modell verwendeten Trainingsdaten wurden nicht als Datensatz veröffentlicht, den man durchsuchen kann. Wir wissen, dass sie eine Menge ungefilterter Inhalte aus dem Internet enthalten, die alles andere als neutral sind.
Mher dazu [hier](https://github.com/openai/gpt-2/blob/master/model_card.md#out-of-scope-use-cases)

## Verwendete Library
### Pytorch
Um pytroch mit python3.11 zu verwenden, kann man noch keinen normalen Release beziehen.
Dafür kann man mit dem folgenden command den nightly build verwenden:
```python
pip install --pre torch -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html
```