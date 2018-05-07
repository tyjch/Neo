# PropertyDict

## `class PropertyDict():`

### Instantiation

```python
property_dict = PropertyDict(iterable, **kwargs)
```

### Equality

```python
# Returns True if equal to 'other' 
# After all None values are removed from 'other' first
properties == other

# Returns True if unequal to 'other' 
# After all None values are removed from 'other' first
properties != other
```

### Properties

```python
# Returns the value associated with 'key'
# If 'key' is missing, None is returned
properties[key]

# Set the value of a property with 'key'
relationship[key] = value

# If 'key' is in 'properties' return its value
# If not, then insert key with value 'default'
properties.setdefault(key, default=None)

# Adds or overwrites the values with an iterable of key-value pairs
# Or with keyword arguments
# Any value of None will effectively delete the property with that key
properties.update(iterable=None, **kwargs)
```

