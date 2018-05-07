# Doc

## Attributes

| Name | Type | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| _`doc.text`_ | unicode | Unicode representation of document text |
| _`doc.text_with_ws`_ | unicode | Unicode with whitespace included |
| _`doc.mem`_ | Pool | Documents local memory heap |
| _`doc.vocab`_ | Vocab | Store of lexical types |
| _`doc.tensor`_ | object | Container for dense vector representations |
| _`doc.cats`_ | dictionary | Maps labels to a score for categories for doc or parts of doc |
| _`doc.user_data`_ | - | Generic storage area for user custom data |
| _`doc.is_tagged`_ | bool | A flag indicating the doc has been part-of-speech tagged |
| _`doc.is_parsed`_ | bool | A flag indicating the doc has been syntactically parsed |
| _`doc.sentiment`_ | float | The docs positivity/negativity score |
| _`doc.user_hooks`_ | dict | A dictionary that allows custom doc properties |
| _`doc.user_token_hooks`_ | dict | A dictionary that allows custom properties of Tokens |
| _`doc.user_span_hooks`_ | dict | A dictionary that allows custom properties of Spans |
| _`doc._`_ | - | User space for custom attribute extensions |

## Methods

### Magic Methods

#### Doc.\_\_init\_\_

```python
# Constructs a Doc object directly
doc = Doc.__init__(vocab,                   # Vocab
                   words,                   # List of strings
                   spaces)                  # Bool

# More commonly created through spacy.Language ('nlp')
doc = nlp('This is text')
```

#### Doc.\_\_getitem\_\_

```python
# Allows you to get a token from a doc by index
token = doc[0]

# Allows you to get a span from a doc by start and end indexes
span = doc[2:5]
```

#### Doc.\_\_iter\_\_

```python
# Allows you to iterate over the tokens in a doc
for token in doc:
    print(token.text)
```

#### Doc.\_\_len\_\_

### Extension Methods



