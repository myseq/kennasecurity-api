# Tips for KennaSecurity Searches

I'm sharing some of my tips that I used to search (and create meters) in KennaSecurity. Here, you will find some tips that not available in KennaSecurity help pages.


### Pre-NVD Chatter 
```
    cve_description:"This candidate has been reserved"
```
To search any threats that are not yet published in NVD or scored in CVSS. This can help us to manage newly disclosed vulnerabilities, even before they're published on the National Vulnerability Database (NVD), so we can proactively managing the vulnerabilties.


### Empty TAG 
```
    -tag:"*"
```
To list those asset that has no tag at all. 


### Empty OS
```
    -os:?*
```
To list those asset that with no OS.


### Vulnerability without Fix
```
    -_exists_:fix AND vulnerability_score:>0 
```
To list those vulnerability that without any fix or solution.

