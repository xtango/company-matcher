# company-matcher
Common company name matching algorithms are designed to handle variations in names due to differences in spelling, abbreviations, and typographical errors. 

Some widely used algorithms:

## Phonetic Matching:
### Soundex: Encodes names by their sounds.
### Metaphone: An improvement over Soundex, handling more phonetic nuances.
### Double Metaphone: Further refines Metaphone by providing two encodings for names with multiple pronunciations.

##  Edit Distance Algorithms:
### Levenshtein Distance: Measures the minimum number of single-character edits needed to change one name into another.
### Jaro-Winkler Distance: An extension of Jaro distance, giving more weight to matching the beginning of the strings.

## Token-Based Matching:
### Tokenization: Breaks names into tokens (words or parts) and compares them.
### N-grams: Compares sequences of ‘n’ characters or words.

## Probabilistic Matching:
Uses statistical models to estimate the likelihood of two names referring to the same entity.

## Hybrid Methods:
Combines multiple techniques to improve accuracy123.


# Common Abbreviations

This dictionary helps in normalizing and matching company names more effectively. 

COMPANY_ABBREVIATIONS = {
    "Corp": "Corporation",
    "Inc": "Incorporated",
    "LLC": "Limited Liability Company",
    "Ltd": "Limited",
    "PLC": "Public Limited Company",
    "Co": "Company",
    "Assoc": "Associates",
    "Bros": "Brothers",
    "Intl": "International",
    "Mfg": "Manufacturing",
    "Mgmt": "Management",
    "Svc": "Service",
    "Tech": "Technology",
    "Sys": "Systems",
    "Grp": "Group",
    "Pty": "Proprietary",
    "Pvt": "Private",
    "LLP": "Limited Liability Partnership",
    "AG": "Aktiengesellschaft",
    "SA": "Société Anonyme"
}
