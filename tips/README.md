# Tips for KennaSecurity Search Syntax

I'm sharing some of my tips that I used to search (and create meters) in KennaSecurity. Here, you will find some tips that not available in KennaSecurity help pages. Kenna Search Term, is based on [Apache Lucene](https://lucene.apache.org/), and the supported searh term can be found at [Kenna Search Terms](https://help.kennasecurity.com/hc/en-us/articles/206280593). 

### :bulb: Kenna Score
> Quick notes on how [Kenna Score](Kenna-Score.md) works!

### :bulb: Excluding asset from the meter score 
> Sometimes you need to exclude some assets from participating in the (average) Kenna meter score, but you still like those asset to be shown in the same Kenna meter. Just set the (individual) asset priority to 0, and the Kenna meter score won't take into account for those asset (with priority 0). This is a handy way to manage the Kenna meter score without making big change.

### :bulb: Active_breach/Easily_exploit/Malware/Popular/Top_priority
> To search any vulnerability that are belongs to Active Internet breaches, easily exploitable, malware exploitable, popular target and top priority.
```sql
    active_internet_breach:true AND easily_exploitable:true AND malware_exploitable:true AND popular_target:true AND top_priority:true
```


### :bulb: Unmappable Vulnerability
> To list any unmappable vulnerability. 
```sql
    vulnerability_name:"Unmappable Vulnerability" AND vulnerability_score:>1
```


### :bulb: Pre-NVD Chatter 
> To search any threats that are not yet published in NVD or scored in CVSS. This can help us to manage newly disclosed vulnerabilities, even before they're published on the National Vulnerability Database (NVD), so we can proactively managing the vulnerabilties.
```sql
    cve_description:"This candidate has been reserved"
```


### :bulb: Empty Asset
> To list those weird assets in Kenna (without hostname, nor IP, nor URL).
```sql
    -_exists_:hostname AND -_exists_:IP AND -_exists_:url
```


### :bulb: Empty TAG 
> To list those asset that has no tag at all. This is useful to track down if any asset is beeing added to Kenna meter or not.
```sql
    -tag:"*"
    -_exists_:tag 
```


### :bulb: Empty OS 
> To list those asset that with no OS.
```sql
    -os:?*
```


### :bulb: Vulnerability without Fix
> To list those vulnerability that without any fix or solution.
```sql
    -_exists_:fix AND vulnerability_score:>0 
```


### :bulb: Vulnerabilities closed within SLA 
> To list those vulnerabilities that closed within the SLA in the past 45 days. 
```sql
    closed_at:>now-45d AND _exists_:due_date AND not_closed_by_due_date:false
```


### :bulb: Vulnerabilities without CVSS score 
> To list those vulnerabilities with empty CVSS score (most lilkely due to mis-configuration).
```sql
    -cvss_severity:"*"
```


### :bulb: Check if SLA is working (vulnerability without Due Date)
> If SLA is working fine, every vulnerability should have a due date. This is to list any vulnerability that has no due date. 
```sql
    -due_date:"*"
```


### :bulb: Vulnererability older than Asset Last Seen
> Assuming your "Asset Inactivity Limit" (within Asset Settings) is set to 31 days, this syntax here is to find out any vulnerability is older than asset's last seen date. This useful to find out those vulnerabilities that not closed by KennaSecurity automatically. It can be used to discover if the asset has been scanned correctly (with credential) or not.
```sql
    vulnerability_last_seen:<now-31d
```


### :bulb: Vulnererability older than Asset Last Seen
> Assuming your "Asset Inactivity Limit" (within Asset Settings) is set to 31 days, this syntax here is to find out any vulnerability is older than asset's last seen date. This useful to find out those vulnerabilities that not closed by KennaSecurity automatically. It can be used to discover if the asset has been scanned correctly (with credential) or not.
```sql
    vulnerability_last_seen:<now-31d
```

### :bulb: Vulnerability that could be exploited remotely
> This is to list out all the vulnerabilties with remote code execution. You will see a special "Remote Code Execution" tag (in red) below the CVE. It is useful for prioritizing the remediation.
```sql
    cve_description:"remote code execution" 
    cve_description:"remote code execution" AND vulnerability_score:>=20
```


### :bulb: Vulnerability that could be exploited in the near future (hidden)
> If you want to be more aggresive in prioritizing your vulnerability remediation, this is a useful (hidden) feature for you. For normal remediation, we can prioritize the remediation based on exploitability. With this option, we can filter those vulnerabilities that may potentially be exploitable in the future. This is based on Kenna proprietary algorithm. 
```sql
    predicted_exploitable:true
```

### :bulb: Vulnerabilities with a high CVSS score
> Both `cvss_v2_score` and `cvss_v3_score` parameters are newly added in Aug 2022. According to Kenna's article, below is the syntax for vulnerabilities with high CVSSS score. However, the syntax below will produce a blind spot in searching any CVE released before 2015 or after 2022-08, which may only contain either CVSS v2 or CVSS v3 score.
```sql
    cvss_v2_score:>=7 AND cvss_v3_score:>=7
```
> Supposedly the syntax should be `cvss_v2_score:>=7 OR cvss_v3_score:>=7`. But this is prohibited in Kenna syntax format. One of the possible solution to search any CVE with high CVSS score could be:
```sql
    cvss_v2_score:>=7 AND -cvss_v3_score:<7 
```

### :bulb: Closed Vulnerability but overdue
> First, need to change the `Status` to `all`. The we can search any closed vulnerability that is overdue (closed after the due_date).
> In this example below, I just filter with all the Microsoft CVE that belongs to year 2024.
```sql
    status:closed AND not_closed_by_due_date:true AND scanner_id:"msft-cve-2024-*"
```
