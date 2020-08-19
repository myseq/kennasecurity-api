# Tips for KennaSecurity Search Syntax

I'm sharing some of my tips that I used to search (and create meters) in KennaSecurity. Here, you will find some tips that not available in KennaSecurity help pages.


### :bulb: Active_breach/Easily_exploit/Malware/Popular/Top_priority
```sql
    active_internet_breach:true AND easily_exploitable:true AND malware_exploitable:true AND popular_target:true AND top_priority:true
```
To search any vulnerability that are belongs to Active Internet breaches, easily exploitable, malware exploitable, popular target and top priority.


### :bulb: Unmappable Vulnerability
To list any unmappable vulnerability. 
```sql
    vulnerability_name:"Unmappable Vulnerability" AND vulnerability_score:>1
```


### :bulb: Unmappable Vulnerability
To list any unmappable vulnerability. 
>  vulnerability_name:"Unmappable Vulnerability" AND vulnerability_score:>1



| ### :bulb: Unmappable Vulnerability | |
| --- | |
| To list any unmappable vulnerability.  |
| Syntax | vulnerability_name:"Unmappable Vulnerability" AND vulnerability_score:>1 |

# GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG

### :bulb: Pre-NVD Chatter 
```
    cve_description:"This candidate has been reserved"
```
To search any threats that are not yet published in NVD or scored in CVSS. This can help us to manage newly disclosed vulnerabilities, even before they're published on the National Vulnerability Database (NVD), so we can proactively managing the vulnerabilties.


### :bulb: Empty Asset
```
    -_exists_:hostname AND -_exists_:IP AND -_exists_:url
```
To list those weird assets in Kenna (without hostname, nor IP, nor URL).


### :bulb: Empty TAG 
```
    -tag:"*"
```
To list those asset that has no tag at all. 


### :bulb: Empty OS 
```
    -os:?*
```
To list those asset that with no OS.


### :bulb: Vulnerability without Fix
```
    -_exists_:fix AND vulnerability_score:>0 
```
To list those vulnerability that without any fix or solution.


### :bulb: Vulnerabilitiies closed within SLA 
```
    closed_at:>now-45d AND _exists_:due_date AND not_closed_by_due_date:false
```
To list those vulnerabilities that closed within the SLA in the past 45 days. 


### :bulb: Check if SLA is working (vulnerability without Due Date)
```
    -due_date:"*"
```
 If SLA is working fine, every vulnerability should have a due date. This is to list any vulnerability that has no due date. 


### :bulb: Vulnererability older than Asset Last Seen
```
    vulnerability_last_seen:<now-31d
```
Assuming your "Asset Inactivity Limit" (within Asset Settings) is set to 31 days, this syntax here is to find out any vulnerability is older than asset's last seen date. This useful to find out those vulnerabilities that not closed by KennaSecurity automatically. It can be used to discover if the asset has been scanned correctly (with credential) or not.


