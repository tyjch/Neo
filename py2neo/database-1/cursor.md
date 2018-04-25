# Cursor

## `class Cursor():`

### Instantiation

```python
# Any Cypher execution method returns a cursor
cursor = transaction.run(cypher)

# So in most cases, you won't have to instantiate directly
cursor = Cursor(result)
```

### Navigation

Most use cases only need `cursor.forward()` and `cursor.current()`

```python
# Use a while loop to navigate through all available records
while cursor.forward():
    print(cursor.current()["name"])
    
# Use an if statement to get the first record only
if cursor.forward():
    print(cursor.current()["name"])
    
# To combine forward and current into a single step, use next()
print(cursor.next()["name")

# Use a for loop to iterate over records in a cursor
for record in cursor:
    print(record["name"])
```

### Basic Methods

```python
# Close this cursor and free up associated resources
cursor.close()

# Return current record in cursor
cursor.current()

# Move the cursor one record forward
cursor.forward()

# Move the cursor 'n' steps forward
cursor.forward(amount = n)

# Attempts to move forward and returns a value from the next record
cursor.evaluate()
cursor.evaluate(field = 1)
cursor.evaluate(field = "name")

# Returns the field names of records in the stream
cursor.keys()

# Returns the next record in the stream or raises StopIteration
cursor.next()

# Returns the plan returned with this result, if any
cursor.plan()

# Returns query statistics
cursor.stats()
```

### Converting Results

```python
# Convert to pandas.DataFrame
df = cursor.to_data_frame(index = None,
                          columns = None
                          dtype = None)

# Convert to sympy.Matrix
matrix = cursor.to_matrix(mutable = False)

# Convert to numpy.ndarray
ndarray = cursor.to_ndarray(dtype = None,
                            order = 'K')
                            
# Convert to pandas.Series
series = cursor.to_series(field = 0,
                          index = None,
                          dtype = None)
                          
# Convert to subgraph
subgraph = cursor.to_subgraph()

# Convert to table
table = cursor.to_table()

```

