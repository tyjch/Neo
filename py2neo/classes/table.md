# Table

## `class Table():`

### Attributes

```python
# Return a dictionary of metadata for a given field
table.field(key)

# Return a list of keys for this table
table.keys()
```

### Writing

```python
# Write to a human-readable table
table.write(file=None,
            header=None,
            skip=None,
            limit=None,
            auto_align=True,
            padding=1,
            separator='|',
            newline='\r\n')

# Write to a CSV file
table.write_csv(file=None,
                header=None,
                skip=None,
                limit=None)
                
# Write to HTML
table.write_html(file=None,
                 header=None,
                 skip=None,
                 limit=None,
                 auto_align=True)
                 
# Write separated values
table.write_separated_values(separator,
            file=None,
            header=None,
            skip=None,
            limit=None,
            newline='\r\n',
            quote='"')

# Write tab-separated values
table.write_tsv(file=None,
                header=None,
                skip=None,
                limit=None)
```

