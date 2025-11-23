# sqlpretty.py

A minimal Python helper for **pretty-printing SQL query results from SQLite databases** — right in your terminal.  
It automatically numbers each query you run and neatly formats the output.

---

## Author

Name : Adam Simonov
Github : https://github.com/AdamSimon1106
Email : adam.simonov@gmail.com

##  Features
- Runs any SQL query on a given SQLite database.
- Prints results in a clean, readable format.
- Automatically increments “Question” numbers with each call.
- If the result has more than 10 rows → shows **top 5 and bottom 5**.
- Otherwise → shows **all rows**.
- Works both as a **library** and **command-line tool**.

---

##  Usage

```python
import sqlpretty

print(sqlpretty.query("world.db", "SELECT * FROM City"))
print(sqlpretty.query("world.db", "SELECT * FROM Country"))
```
# Example Output
```markdown
=============================================
Question: 1
The query:
SELECT *
FROM City
Num of rows: 4079
The results: 
        ID            Name CountryCode       District  Population
0        1           Kabul         AFG          Kabol     1780000
1        2        Qandahar         AFG       Qandahar      237500
2        3           Herat         AFG          Herat      186800
3        4  Mazar-e-Sharif         AFG          Balkh      127800
4        5       Amsterdam         NLD  Noord-Holland      731200
4074  4075      Khan Yunis         PSE     Khan Yunis      123175
4075  4076          Hebron         PSE         Hebron      119401
4076  4077        Jabaliya         PSE     North Gaza      113901
4077  4078          Nablus         PSE         Nablus      100231
4078  4079           Rafah         PSE          Rafah       92020


=============================================
Question: 2
The query:
SELECT *
FROM Country
Num of rows: 239
The results: 
    Code                                          Name      Continent                     Region  SurfaceArea  IndepYear  Population  LifeExpectancy       GNP    GNPOld                                     LocalName                                GovernmentForm           HeadOfState  Capital Code2
0    AFG                                   Afghanistan           Asia  Southern and Central Asia     652090.0     1919.0    22720000            45.9    5976.0       NaN                         Afganistan/Afqanestan                               Islamic Emirate         Mohammad Omar      1.0    AF
1    NLD                                   Netherlands         Europe             Western Europe      41526.0     1581.0    15864000            78.3  371362.0  360478.0                                     Nederland                       Constitutional Monarchy               Beatrix      5.0    NL
2    ANT                          Netherlands Antilles  North America                  Caribbean        800.0        NaN      217000            74.7    1941.0       NaN                          Nederlandse Antillen  Nonmetropolitan Territory of The Netherlands               Beatrix     33.0    AN
3    ALB                                       Albania         Europe            Southern Europe      28748.0     1912.0     3401200            71.6    3205.0    2500.0                                     Shqipëria                                      Republic        Rexhep Mejdani     34.0    AL
4    DZA                                       Algeria         Africa            Northern Africa    2381741.0     1962.0    31471000            69.7   49982.0   46966.0                            Al-Jaza’ir/Algérie                                      Republic  Abdelaziz Bouteflika     35.0    DZ
234  IOT                British Indian Ocean Territory         Africa             Eastern Africa         78.0        NaN           0             NaN       0.0       NaN                British Indian Ocean Territory                 Dependent Territory of the UK          Elisabeth II      NaN    IO
235  SGS  South Georgia and the South Sandwich Islands     Antarctica                 Antarctica       3903.0        NaN           0             NaN       0.0       NaN  South Georgia and the South Sandwich Islands                 Dependent Territory of the UK          Elisabeth II      NaN    GS
236  HMD             Heard Island and McDonald Islands     Antarctica                 Antarctica        359.0        NaN           0             NaN       0.0       NaN                    Heard and McDonald Islands                        Territory of Australia          Elisabeth II      NaN    HM
237  ATF                   French Southern territories     Antarctica                 Antarctica       7780.0        NaN           0             NaN       0.0       NaN                   Terres australes françaises           Nonmetropolitan Territory of France        Jacques Chirac      NaN    TF
238  UMI          United States Minor Outlying Islands        Oceania       Micronesia/Caribbean         16.0        NaN           0             NaN       0.0       NaN          United States Minor Outlying Islands                 Dependent Territory of the US        George W. Bush      NaN    UM


```

