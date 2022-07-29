Best practices for shuffling (if your business depends on it).

* Use a hardware random-number generator that has passed both
    the FIPS 140-2 and the NIST statistical test suites.
    
* Continuously monitor statistic properties: 
  hardware random-number generators are fragile and fail silently.

* Use an unbiased shuffling algorithm.