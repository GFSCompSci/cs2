## Set

A set object is an unordered collection of distinct hashable objects. Common uses include membership testing, removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference, and symmetric difference.

Like other collections, sets support x in set, len(set), and for x in set. Being an unordered collection, sets do not record element position or order of insertion. Accordingly, sets do not support indexing, slicing, or other sequence-like behavior.

There are currently two built-in set types, set. The set type is mutable — the contents can be changed using methods like add() and remove(). Since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set.

Non-empty sets can be created by placing a comma-separated list of elements within braces, for example: {'jack', 'sjoerd'}, in addition to the set constructor.

## Set Operators:


len(s): Return the number of elements in set s (cardinality of s).

x in s: Test x for membership in s.

x not in s: Test x for non-membership in s.

isdisjoint(other): Return True if the set has no elements in common with other. Sets are disjoint if and only if their intersection is the empty set.

issubset(other), set <= other: Test whether every element in the set is in other.

set < other: Test whether the set is a proper subset of other, that is, set <= other and set != other.

issuperset(other), set >= other: Test whether every element in other is in the set.

set > other: Test whether the set is a proper superset of other, that is, set >= other and set != other.

union(*others), set | other | ...: Return a new set with elements from the set and all others.

intersection(*others), set & other & ... : Return a new set with elements common to the set and all others.

difference(*others), set - other - ...: Return a new set with elements in the set that are not in the others.

symmetric_difference(other), set ^ other: Return a new set with elements in either the set or other but not both.

copy(): Return a new set with a shallow copy of s.
